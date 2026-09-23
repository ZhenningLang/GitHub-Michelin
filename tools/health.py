#!/usr/bin/env python3
"""Deterministic OSS-health scorer for oss-atlas.

Implements the LOCKED 6-axis "JoJo Stand-stats" rubric (see the health spec): each
project is graded A/B/C/D/E or "?" (unknown, first-class) on six axes —
maintenance, responsiveness, adoption, longevity, governance, risk_license — then
an overall grade is derived (mean over scored axes, with a Risk/License CAP).

This is the SCORER half of the pipeline (the SVG generator is separate). It:
  - reads a project from --repo owner/name --type <t>  OR  --page <path>.md
    (parsing repo:/type: from the page's YAML frontmatter, stdlib only)
  - computes all six axes deterministically (same inputs -> same grades)
  - emits the `health:` YAML block (spec §5.2) to stdout; with --write splices the
    identical block into BOTH the .md and .zh.md frontmatter of the page.

Data sources (NO pip deps): the authenticated `gh` CLI for GitHub (REST + GraphQL,
shelled out) and urllib for ecosyste.ms / direct registries. Every network/API
failure on an axis degrades to "?" + a machine-readable reason code — never a crash,
never a silent downgrade.

Determinism: the only stochastic element is the responsiveness window offset, which
is SEEDED off the repo full_name (md5) so a re-run is reproducible; the offset is
recorded in the YAML.

Rate-limit hygiene (spec §4.2): calls run serial; stats/* 202 cold-cache is retried
up to 3x with backoff, then degrades to "?".

Pure stdlib + `gh` + urllib. Style mirrors tools/lint.py.

Usage:
  python3 tools/health.py --repo openinterpreter/open-interpreter --type framework
  python3 tools/health.py --page categories/agent-tooling/agent-orchestrator.md
  python3 tools/health.py --page <path> --write     # splice block into .md + .zh.md
"""
from __future__ import annotations

import argparse
import datetime as dt
import functools
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SCHEMA_VERSION = 1
USER_AGENT = "oss-atlas-health/1.0 (+https://github.com/oss-atlas)"

# ---------------------------------------------------------------------------
# TIER / threshold tables (spec §2) — kept near the top so the rubric is auditable.
# ---------------------------------------------------------------------------

GRADE_POINTS = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}  # spec §3.1; "?" excluded
GRADE_ORDER = ["A", "B", "C", "D", "E"]                   # for max(tier1, tier2)

# Bot / AI-agent author filter (spec §1.3). Leaky in both directions; documented.
BOT_RE = re.compile(
    r"(\[bot\]$)|(^dependabot)|(^renovate)|(-bot$)|(^github-actions)|"
    r"( bot$)|(^mergify)|(^release-please)|(^pre-commit-ci)",
    re.IGNORECASE,
)
AI_COMMITTERS = {"claude", "ampagent", "devin", "cursor-agent", "copilot", "sweep-ai"}

# 2.2 responsiveness — type-aware TTFR bands, in HOURS (and qualifying-issue floors).
RESP_BANDS = {
    "default": {  # library, framework, service
        "A": 48, "A_min_issues": 5,
        "B": 7 * 24, "B_min_issues": 3,
        "C": 30 * 24,
        "D": 180 * 24,
        # E: >= D ceiling
    },
    "relaxed": {  # tool, app
        "A": 7 * 24, "A_min_issues": 3,
        "B": 30 * 24, "B_min_issues": 3,
        "C": 90 * 24,
        "D": 365 * 24,
    },
}
RESP_RELAXED_TYPES = {"tool", "app"}
RESP_NA_TYPES = {"skill-pack", "model"}

# 2.3 adoption — per-registry absolute anchors for volume_tier (A/B/C/D/E floors).
# Each entry: (A_floor, B_floor, C_floor, E_floor). D = (>0 and < C). E = (< E_floor).
ADOPTION_VOLUME_ANCHORS = {
    "npmjs.org":   (5_000_000, 500_000, 50_000, 1_000),
    "pypi.org":    (2_000_000, 200_000, 20_000, 1_000),
    "crates.io":   (1_000_000, 100_000, 10_000, 500),
    "rubygems.org": (500_000, 50_000, 5_000, 500),
    "packagist.org": (500_000, 50_000, 5_000, 500),
    "nuget.org":   (1_000_000, 100_000, 10_000, 500),
    "conda-forge.org": (1_000_000, 100_000, 10_000, 500),
    "anaconda.org": (1_000_000, 100_000, 10_000, 500),
    "gem.coop":    (500_000, 50_000, 5_000, 500),
    "open-vsx.org": (500_000, 50_000, 5_000, 500),
    "formulae.brew.sh": (100_000, 10_000, 1_000, 100),
}
# Any registry not named above. Without this, `volume_tier_from_downloads` returned None
# for an unlisted registry and the download figure was **discarded entirely** — so
# selenium (345,857,423 downloads/month on gem.coop) scored its dependents-only tier and
# landed on E. 20 pages carried a silently-dropped download count this way. A default
# that is merely approximate beats throwing a nine-figure measurement away.
ADOPTION_VOLUME_ANCHORS_DEFAULT = (1_000_000, 100_000, 10_000, 500)

# A package's *ecosystem* (not its registry name) says whether it is the project's own
# distribution channel. ecosyste.ms indexes 100 registries and most are distro archives
# that repackage other people's software — jq's 37 candidates are almost all Alpine,
# Debian, Ubuntu, Nix and Adelie builds, and letting one win made the page report
# `registry: alpine-v3.19, canonical_package: jq-dev`. Version-suffixed names
# (`alpine-v3.19`, `alpine-edge`, `nixpkgs-24.11`, `ubuntu-23.10`) also make a
# name-based denylist unmaintainable, so this is an allowlist keyed on ecosystem.
PRIMARY_ECOSYSTEMS = {
    "npm", "pypi", "cargo", "rubygems", "packagist", "maven", "nuget", "go", "hex",
    "pub", "cocoapods", "cran", "cpan", "clojars", "hackage", "luarocks", "elm",
    "julia", "swiftpm", "deno", "bower", "dub", "vcpkg",
}
# Mirrors of a primary registry: right ecosystem, wrong copy. `gem.coop` mirrors
# RubyGems and, by winning canonical, put selenium (345,857,423 downloads/month),
# asciidoctor and loki on a registry the anchor table did not cover — all three scored E.
MIRROR_REGISTRIES = {"gem.coop"}
# Redistribution channels kept out of canonical selection unless they carry real counts,
# since dropping them entirely would lose the only signal some projects have.
SECONDARY_REGISTRIES = {"conda-forge.org", "anaconda.org", "formulae.brew.sh", "spack.io"}
# dependent_repos_count -> graph_tier (A/B/C/D/E). Go importers map to this same column.
ADOPTION_GRAPH_ANCHORS = (10_000, 1_000, 100)  # A, B, C floors; D = 1..99; E = 0
ADOPTION_NO_PACKAGE_TYPES = {"app", "skill-pack", "service", "model"}
# Every type gets the §2.3b instruments before any `?` is conceded: any project can ship
# a binary, an image or a bundle, and which channel it uses is a fact to be measured
# rather than assumed from its `type:` label.
# Types that fall back to N/A when *no* instrument answers. A skill-pack is copied into
# a directory; if it also ships no release bundle, there is no install event anywhere to
# count, and "how many installs" stops being a question about its health. Measured first,
# conceded second: 18 of this index's 84 skill-packs do publish downloadable bundles.
ADOPTION_NA_TYPES = {"skill-pack"}

# Install-signal anchors (A_floor, B_floor, C_floor) = the **top 10% / 25% / 50% of that
# channel's own population**. They are deliberately NOT calibrated to mean the same
# absolute reach as a registry grade, because the evidence says no such mapping exists:
# across 138 projects measured both ways, Spearman correlation between release-asset
# downloads and registry downloads is 0.124, and against dependent_repos 0.002. The
# channels see different users. angular ships 24.6M npm downloads a month and 324 release
# downloads; jq ships 295M release downloads and reads as a minor package on a registry.
# A letter therefore means "top decile *of the channel this project actually ships
# through*", and `signal_basis` on every page names which channel that was.
RELEASE_DOWNLOAD_ANCHORS = (10_000_000, 1_000_000, 100_000)   # p90/p75/p50 of this index's
                                                              # 270 asset-publishing repos
BREW_INSTALL_ANCHORS = (3_000, 500, 100)                      # p90/p75/p50 of Homebrew's
                                                              # own 7,900 formulae + casks
# Docker has no population we can enumerate, so these stay absolute and are the weakest
# of the three; pull_count is cumulative and inflated by CI (envoy alone reports 5.76e9).
DOCKER_PULL_ANCHORS = (100_000_000, 10_000_000, 1_000_000)
# Docker Hub's anonymous API rate-limits hard (429 observed live at 8 concurrent
# requests), and it is the weakest of the three instruments — pull_count is cumulative
# and CI-inflated. So it is spent only where a container image is plausibly the project's
# primary distribution channel, which cuts the call volume across a full rescore by
# roughly 70% (177 of 607 pages) and keeps the batch clear of the one limit this scorer
# has actually been refused by. A library or a skill-pack that happens to publish an
# image is not measured by it.
DOCKER_PROBE_TYPES = {"service", "app"}
DOCKER_PROBE_DELAY_S = 1.2
# ecosyste.ms registry name -> direct-registry cross-check kind.
REGISTRY_CROSSCHECK = {
    "npmjs.org": "npm", "pypi.org": "pypi", "crates.io": "crates",
    "rubygems.org": "rubygems", "packagist.org": "packagist",
}

# 2.4 longevity — type-relative age bars in DAYS (A-age, B-age, C-age).
LONGEVITY_AGE_BARS = {
    "library":   (1825, 1095, 365),
    "framework": (1825, 1095, 365),
    "tool":      (1095, 548, 183),
    "app":       (1095, 548, 183),
    "service":   (1095, 548, 183),
    "skill-pack": (548, 274, 91),
    "model":     (548, 274, 91),
}

# 2.6 risk_license permissiveness classes -> tier.
PERMISSIVENESS_TIER = {
    "permissive": "A",
    "permissive_clause_addon": "B",
    "weak_file_copyleft": "C",
    "strong_network_copyleft": "D",
    "source_available": "E",
}
# Known source-available / non-OSI keys (used when conditions/limitations are unhelpful).
SOURCE_AVAILABLE_SPDX = {
    "SSPL-1.0", "Elastic-2.0", "BSL-1.1", "BUSL-1.1", "CC-BY-NC-4.0",
    "CC-BY-NC-SA-4.0", "CC-BY-NC-3.0", "Commons-Clause",
}
STRONG_COPYLEFT_SPDX_PREFIXES = ("GPL-", "AGPL-")
DECLARED_PROPRIETARY_LICENSES = {"Proprietary", "Source-available"}
# Content licenses tracked on a separate flag, never via the code-copyleft map (spec §2.6).
CONTENT_LICENSE_RE = re.compile(r"^CC-BY", re.IGNORECASE)
# Base names that mean "this file IS the license", plus the extensions a license text is
# allowed to carry. Used only to check whether a license exists at all, after GitHub's
# detector has already declined to classify one.
LICENSE_BASE_NAMES = ("license", "licence", "copying", "unlicense", "copyright")
LICENSE_TEXT_EXTS = ("", "txt", "md", "rst", "html")
# Directories projects actually park a license in when it is not at the root. Kept short
# on purpose: each entry is an extra API call on the repos that reach this path.
LICENSE_SEARCH_DIRS = ("legal", "license", "licenses", "LICENSES", "doc", "docs", ".github")
# Of those, the ones whose whole purpose is to hold licenses, so any text file inside counts
# (the REUSE spec names each file after its SPDX id, e.g. `LICENSES/LGPL-2.1-or-later.txt`).
LICENSE_DEDICATED_DIRS = {"legal", "license", "licenses"}
# A page's own `license:` frontmatter is a human-verified fact. It cannot earn a good grade,
# but it does distinguish "the maintainers published a license the machine can't parse" from
# "this really is all-rights-reserved" — and the pages already say which: pygame declares
# LGPL-2.1, swarm-forge declares "NONE (no LICENSE file — all rights reserved)".
DECLARED_NO_LICENSE_RE = re.compile(r"^\s*(none|no\b|not declared|unlicensed|proprietary)", re.I)
DECLARED_REAL_LICENSE_RE = re.compile(
    r"^\s*(mit|apache|bsd|[al]?gpl|lgpl|mpl|isc|unlicense|cc[\s-]|cc0|epl|zlib|"
    r"artistic|boost|bsl|eupl|ms-pl|postgresql|python|ruby|openssl|wtfpl)", re.I)

RELICENSE_WINDOW_DAYS = 36 * 30  # "trailing 36mo" approximation


# ---------------------------------------------------------------------------
# Tiny frontmatter reader (no PyYAML) — mirrors tools/lint.py parse_frontmatter.
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end].strip("\n")
    data: dict = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key, raw = key.strip(), raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            data[key] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        else:
            data[key] = raw.strip().strip('"').strip("'")
    return data


def repo_url_to_owner_name(url: str) -> str | None:
    """Extract owner/name from a github.com repo URL (frontmatter `repo:` is a URL)."""
    m = re.search(r"github\.com[/:]([^/]+)/([^/#?]+?)(?:\.git)?/?$", url.strip())
    if not m:
        return None
    return f"{m.group(1)}/{m.group(2)}"


# ---------------------------------------------------------------------------
# HTTP helpers — gh CLI for GitHub; urllib for ecosyste.ms / registries.
# A GhResult carries (status, body_text, parsed_json_or_None) so 202 is visible.
# ---------------------------------------------------------------------------

class GhResult:
    def __init__(self, status: int, body: str):
        self.status = status
        self.body = body
        self.json = None
        if body:
            try:
                self.json = json.loads(body)
            except (ValueError, json.JSONDecodeError):
                self.json = None

    @property
    def ok(self) -> bool:
        return 200 <= self.status < 300


def gh_api(path: str, *, method: str = "GET", fields: dict | None = None,
           graphql: bool = False) -> GhResult:
    """Call `gh api` and return a GhResult, capturing the HTTP status via -i headers.

    Never raises on an API error — returns a GhResult with the real status code so the
    caller can degrade to "?" with a reason. (A nonzero gh exit on 4xx/5xx is expected.)
    """
    gh_bin = resolve_gh_cli()
    if gh_bin is None:
        return GhResult(0, json.dumps({"_transport_error": "gh CLI not found; set OSS_ATLAS_GH or put gh on PATH"}))

    if graphql:
        cmd = [gh_bin, "api", "graphql", "-f", f"query={path}"]
        for k, v in (fields or {}).items():
            cmd += ["-f", f"{k}={v}"]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        except (subprocess.TimeoutExpired, OSError) as e:
            return GhResult(0, json.dumps({"_transport_error": str(e)}))
        status = 200 if proc.returncode == 0 else 502
        return GhResult(status, proc.stdout or proc.stderr)

    # REST: use -i to read the status line, then split headers from body.
    cmd = [gh_bin, "api", "-i", "-X", method, path]
    for k, v in (fields or {}).items():
        cmd += ["-f", f"{k}={v}"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    except (subprocess.TimeoutExpired, OSError) as e:
        return GhResult(0, json.dumps({"_transport_error": str(e)}))
    raw = proc.stdout or ""
    status, body = _split_http(raw)
    if status == 0 and proc.returncode != 0:
        # gh printed an error to stderr without an HTTP status line.
        err = proc.stderr or ""
        m = re.search(r"HTTP (\d{3})", err)
        status = int(m.group(1)) if m else 502
        body = body or err
    if _rate_limited(status, raw) and _retry_after_reset(raw):
        return gh_api(path, method=method, fields=fields, graphql=graphql)
    return GhResult(status, body)


def _rate_limited(status: int, raw: str) -> bool:
    return status in (403, 429) and re.search(
        r"(?im)^x-ratelimit-remaining:\s*0\s*$", raw) is not None


def _retry_after_reset(raw: str, *, max_wait_s: int = 3700) -> bool:
    """Block until the rate-limit window resets, then report that a retry is warranted.

    Without this, a 403 from an exhausted quota reaches the axis functions as an ordinary
    API failure and degrades to `?` — indistinguishable on the page from "this project is
    genuinely unmeasurable". Across a 600-page batch that silently overwrites real grades
    with a wall of unknowns, which is far worse than waiting.
    """
    m = re.search(r"(?im)^x-ratelimit-reset:\s*(\d+)\s*$", raw)
    if not m:
        return False
    wait = int(m.group(1)) - int(time.time()) + 5
    if wait <= 0 or wait > max_wait_s:
        return False
    print(f"# rate limit exhausted; sleeping {wait}s until reset", file=sys.stderr, flush=True)
    time.sleep(wait)
    return True


def resolve_gh_cli() -> str | None:
    """Resolve the GitHub CLI used by the scorer.

    `OSS_ATLAS_GH` is an explicit override for non-standard installs and tests.
    Otherwise use PATH discovery so the scorer works outside Apple Silicon Homebrew.
    """
    override = os.environ.get("OSS_ATLAS_GH")
    if override:
        return override
    return shutil.which("gh")


def _split_http(raw: str) -> tuple[int, str]:
    """Split `gh api -i` output (possibly multiple header blocks for redirects)."""
    status = 0
    rest = raw
    # Walk past any number of "HTTP/.. <code>\r?\n...headers...\r?\n\r?\n" blocks.
    while True:
        m = re.match(r"HTTP/[\d.]+ (\d{3})[^\n]*\n", rest)
        if not m:
            break
        status = int(m.group(1))
        sep = rest.find("\n\n", m.end() - 1)
        sep2 = rest.find("\r\n\r\n")
        cut = min([p for p in (sep, sep2) if p != -1], default=-1)
        if cut == -1:
            rest = ""
            break
        rest = rest[cut:].lstrip("\r\n")
        if not re.match(r"HTTP/[\d.]+ \d{3}", rest):
            break
    return status, rest


def gh_stats(path: str, retries: int = 3) -> GhResult:
    """Fetch a stats/* endpoint, retrying 202 (cold cache) up to `retries` with backoff.

    Returns the final GhResult; caller treats a still-202 (or empty 200) as "?".
    """
    backoff = 1.5
    for attempt in range(retries + 1):
        res = gh_api(path)
        if res.status == 202:
            if attempt < retries:
                time.sleep(backoff)
                backoff *= 2
                continue
            return res  # still 202 after retries
        return res
    return res


def http_get_json(url: str, *, timeout: int = 25, retries: int = 0,
                  backoff: float = 1.5) -> tuple[int, object | None]:
    """GET a URL with urllib; return (status, parsed_json_or_None). Never raises.

    `retries` re-attempts only *transport* failures (status 0) and 429/5xx — the
    transient class. A 404 or a parsed 200 is returned immediately: retrying those
    burns budget without changing the answer. Retry matters because a transport blip
    on the ecosyste.ms lookup is otherwise indistinguishable from "no package exists",
    and `registry_lookup_failed` then masquerades as missing adoption data
    (observed live: playwright/material-ui/chakra-ui/radix-ui all scored `?` this way).
    """
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    delay = backoff
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = resp.read().decode("utf-8", "replace")
                try:
                    return resp.status, json.loads(body)
                except (ValueError, json.JSONDecodeError):
                    return resp.status, None
        except urllib.error.HTTPError as e:
            status = e.code
        except (urllib.error.URLError, OSError, ValueError):
            status = 0
        transient = status == 0 or status == 429 or status >= 500
        if not transient or attempt == retries:
            return status, None
        time.sleep(delay)
        delay *= 2
    return 0, None


def http_get_text(url: str, *, timeout: int = 25) -> tuple[int, str | None]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, None
    except (urllib.error.URLError, OSError, ValueError):
        return 0, None


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_iso(ts: str | None) -> dt.datetime | None:
    if not ts:
        return None
    try:
        return dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None


def days_since(ts: str | None, now: dt.datetime) -> float | None:
    d = parse_iso(ts)
    if d is None:
        return None
    return (now - d).total_seconds() / 86400.0


def is_bot_author(login: str | None, email: str | None = None) -> bool:
    """Drop bot/AI authors (spec §1.3). Falls back to email local-part when login null."""
    name = login
    if not name and email:
        name = email.split("@", 1)[0]
    if not name:
        return False
    if BOT_RE.search(name):
        return True
    return name.lower() in AI_COMMITTERS


def graph_tier_from_dependents(n: int) -> str:
    a, b, c = ADOPTION_GRAPH_ANCHORS
    if n >= a:
        return "A"
    if n >= b:
        return "B"
    if n >= c:
        return "C"
    if n >= 1:
        return "D"
    return "E"


def volume_tier_from_downloads(downloads: int | None, registry: str) -> str | None:
    """Map absolute last-month downloads to a tier vs the per-registry anchor table.

    Returns None ("?") only when there is no download figure to tier. A registry we have
    no bespoke table for falls back to ADOPTION_VOLUME_ANCHORS_DEFAULT rather than
    discarding the number: an unrecognised registry name is our gap, not the project's.
    """
    if downloads is None:
        return None
    anchors = ADOPTION_VOLUME_ANCHORS.get(registry) or ADOPTION_VOLUME_ANCHORS_DEFAULT
    a, b, c, e_floor = anchors
    if downloads >= a:
        return "A"
    if downloads >= b:
        return "B"
    if downloads >= c:
        return "C"
    if downloads >= e_floor:
        return "D"
    return "E"


def tier_max(*tiers: str | None) -> str:
    """Return the best (A>B>C>D>E) of the given tiers, ignoring None."""
    present = [t for t in tiers if t in GRADE_ORDER]
    if not present:
        return "E"
    return min(present, key=lambda t: GRADE_ORDER.index(t))


# ---------------------------------------------------------------------------
# Axis result container
# ---------------------------------------------------------------------------

class Axis:
    """One axis result: grade (A-E, '?' or 'N/A'), raw values, optional reason.

    Three states, deliberately distinct (spec §2.3, §3.2):
      A-E   measured.
      '?'   we tried to measure and could not — the reader should treat the axis as an
            open question and go look, and the failure may be ours.
      'N/A' the axis asks a question this artifact type cannot answer, no matter how
            healthy it is. A skill-pack is copied, never installed: there is no install
            event to count anywhere, so an adoption number does not exist to be found.
    `?` is a gap in our data; `N/A` is a gap in the question. Collapsing them (as this
    scorer did through 2026-09) tells the reader "unknown" in both cases and hides which
    one they are looking at — and it drags the aggregate denominator down for projects
    that are not missing anything.
    """

    NOT_APPLICABLE = "N/A"

    def __init__(self, grade: str, raw: dict, reason: str | None = None,
                 evidence: str = ""):
        self.grade = grade
        self.raw = raw
        self.reason = reason          # set iff grade in ("?", "N/A")
        self.evidence = evidence      # one-line human note for the report

    @classmethod
    def unknown(cls, reason: str, raw: dict | None = None, evidence: str = "") -> "Axis":
        return cls("?", raw or {}, reason=reason, evidence=evidence or f"? ({reason})")

    @classmethod
    def not_applicable(cls, reason: str, raw: dict | None = None, evidence: str = "") -> "Axis":
        return cls(cls.NOT_APPLICABLE, raw or {}, reason=reason,
                   evidence=evidence or f"N/A ({reason})")


# ---------------------------------------------------------------------------
# Core repo fetch (shared across maintenance / longevity / governance / adoption)
# ---------------------------------------------------------------------------

class RepoData:
    """Lazily-fetched, cached GitHub facts shared across axes (spec §4.1 shared calls)."""

    def __init__(self, owner: str, name: str, ptype: str, now: dt.datetime,
                 declared_license: str | None = None):
        self.owner = owner
        self.name = name
        self.full = f"{owner}/{name}"
        self.type = ptype
        self.declared_license = declared_license
        self.now = now
        self._core: GhResult | None = None
        self._last_commit_date: str | None = None
        self._last_commit_fetched = False

    @property
    def core(self) -> GhResult:
        if self._core is None:
            self._core = gh_api(f"repos/{self.full}")
        return self._core

    def last_commit_date(self) -> str | None:
        """Committer date of the newest default-branch commit (spec §1.4)."""
        if not self._last_commit_fetched:
            self._last_commit_fetched = True
            res = gh_api(f"repos/{self.full}/commits?per_page=1")
            if res.ok and isinstance(res.json, list) and res.json:
                try:
                    self._last_commit_date = res.json[0]["commit"]["committer"]["date"]
                except (KeyError, TypeError, IndexError):
                    self._last_commit_date = None
        return self._last_commit_date


# ---------------------------------------------------------------------------
# Axis 1 — maintenance (spec §2.1)
# ---------------------------------------------------------------------------

def axis_maintenance(repo: RepoData) -> Axis:
    core = repo.core
    if core.status in (404, 451) or (core.status == 403 and core.json is None):
        return Axis.unknown("repo_404_or_private",
                            evidence=f"? core repo HTTP {core.status}")
    if not core.ok or not isinstance(core.json, dict):
        return Axis.unknown("recency_unreadable",
                            evidence=f"? core repo HTTP {core.status}")

    c = core.json
    archived = bool(c.get("archived"))
    disabled = bool(c.get("disabled"))
    created_at = c.get("created_at")
    repo_age_days = days_since(created_at, repo.now)

    # last_commit_age_days from /commits?per_page=1 (committer date).
    commit_res = gh_api(f"repos/{repo.full}/commits?per_page=1")
    if commit_res.status == 409:  # empty repo
        return Axis.unknown("empty_repo", evidence="? /commits 409 empty repo")
    last_commit_date = repo.last_commit_date()
    last_age = days_since(last_commit_date, repo.now)

    # active_weeks_13 from stats/participation (count nonzero of last 13 weeks).
    part_res = gh_stats(f"repos/{repo.full}/stats/participation")
    active_weeks_13 = None
    if part_res.ok and isinstance(part_res.json, dict):
        allw = part_res.json.get("all")
        if isinstance(allw, list) and allw:
            active_weeks_13 = sum(1 for w in allw[-13:] if isinstance(w, (int, float)) and w > 0)

    # Spine unreadable: stats still 202 AND no commit date -> "?".
    if last_age is None and active_weeks_13 is None:
        return Axis.unknown("recency_unreadable",
                            evidence="? participation 202 + /commits unreadable")

    raw = {
        "archived": archived,
        "last_commit_age_days": _round(last_age),
        "active_weeks_13": active_weeks_13,
        "carve_out": None,
    }

    # E override: archived/disabled or stale >= 730d.
    if archived or disabled:
        raw["last_commit_age_days"] = _round(last_age)
        return Axis("E", raw, evidence=f"archived={archived} disabled={disabled} -> E")
    if last_age is not None and last_age >= 730:
        return Axis("E", raw, evidence=f"last_commit {last_age:.0f}d (>=730) -> E")

    aw = active_weeks_13 if active_weeks_13 is not None else 0

    if last_age is not None and last_age < 30 and aw >= 6:
        return Axis("A", raw, evidence=f"last_commit {last_age:.0f}d <30 & active_weeks {aw}>=6 -> A")
    if last_age is not None and last_age < 90 and aw >= 2:
        return Axis("B", raw, evidence=f"last_commit {last_age:.0f}d <90 & active_weeks {aw}>=2 -> B")

    # C / D bands.
    base_grade = None
    if last_age is not None and last_age < 90 and aw < 2:
        base_grade = "C"  # lone recent commit, no sustained activity
        ev = f"last_commit {last_age:.0f}d <90 but active_weeks {aw}<2 -> C"
    elif last_age is not None and 90 <= last_age < 365:
        base_grade = "C"
        ev = f"last_commit {last_age:.0f}d in [90,365) -> C"
    elif last_age is not None and 365 <= last_age < 730:
        base_grade = "D"
        ev = f"last_commit {last_age:.0f}d in [365,730) -> D"
    else:
        # last_age None but participation readable -> can't place recency band -> "?".
        return Axis.unknown("recency_unreadable",
                            evidence="? last_commit date unreadable for band placement")

    # Mature-library Lindy carve-out (overrides C/D up to one tier -> B), spec §2.1.
    if base_grade in ("C", "D") and repo.type in ("library", "framework") \
            and repo_age_days is not None and repo_age_days >= 1095 \
            and not archived and last_age is not None and last_age < 365:
        raw["carve_out"] = "mature_library_lindy"
        return Axis("B", raw,
                    evidence=f"{base_grade}->B mature_library_lindy "
                             f"(age {repo_age_days:.0f}d>=3y, last_commit {last_age:.0f}d<365)")

    return Axis(base_grade, raw, evidence=ev)


# ---------------------------------------------------------------------------
# Axis 2 — responsiveness (spec §2.2)
# ---------------------------------------------------------------------------

# NOTE: spec §2.2 wrote `issues(last:60, ...DESC)`, but in GraphQL `last:N` slices the
# END of the ordered connection — with DESC that returns the 60 OLDEST issues, the
# opposite of the spec's stated intent ("issues opened in a 90-day window", recent
# traffic). Use `first:60` with DESC to get the 60 NEWEST issues. Documented deviation.
RESP_GRAPHQL = """query($o:String!,$n:String!){ repository(owner:$o,name:$n){
  hasIssuesEnabled isArchived createdAt
  issues(first:60, orderBy:{field:CREATED_AT,direction:DESC}){ nodes{
    number createdAt closedAt author{login}
    comments(first:5){nodes{createdAt author{login} bodyText}}
    timelineItems(first:10, itemTypes:[LABELED_EVENT,ASSIGNED_EVENT,CLOSED_EVENT]){
      nodes{__typename
        ... on LabeledEvent{createdAt actor{login}}
        ... on AssignedEvent{createdAt actor{login}}
        ... on ClosedEvent{createdAt actor{login}}}}
  }}
  pullRequests(first:30, orderBy:{field:CREATED_AT,direction:DESC}){ nodes{
    createdAt author{login}
    reviews(first:10){nodes{createdAt author{login}}}
    comments(first:10){nodes{createdAt author{login}}}
  }}
}}"""


def _seeded_window_offset(full_name: str) -> int:
    """Deterministic 0..13 day window offset, seeded off the repo full_name (md5)."""
    h = hashlib.md5(full_name.encode("utf-8")).hexdigest()
    return int(h, 16) % 14


def _shingles(text: str, k: int = 4) -> set:
    words = re.findall(r"\w+", (text or "").lower())
    if len(words) < k:
        return {" ".join(words)} if words else set()
    return {" ".join(words[i:i + k]) for i in range(len(words) - k + 1)}


def _jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def axis_responsiveness(repo: RepoData) -> Axis:
    if repo.type in RESP_NA_TYPES:
        return Axis.unknown("type_na", evidence=f"type {repo.type} -> issues not the channel")

    offset = _seeded_window_offset(repo.full)
    res = gh_api(RESP_GRAPHQL, graphql=True,
                 fields={"o": repo.owner, "n": repo.name})
    if not res.ok or not isinstance(res.json, dict):
        return Axis.unknown("github_unavailable", evidence=f"? GraphQL HTTP {res.status}")
    data = res.json.get("data") or {}
    r = data.get("repository")
    if not isinstance(r, dict):
        return Axis.unknown("github_unavailable", evidence="? GraphQL repository null")

    if r.get("hasIssuesEnabled") is False:
        return Axis.unknown("issues_disabled", evidence="hasIssuesEnabled=false")
    if r.get("isArchived"):
        band = "relaxed" if repo.type in RESP_RELAXED_TYPES else "default"
        return Axis("E", {"median_ttfr_hours": None, "qualifying_issues": 0,
                          "band": _band_label(band), "window_offset_days": offset},
                    evidence="archived -> E")

    created = parse_iso(r.get("createdAt"))
    repo_age_days = (repo.now - created).total_seconds() / 86400.0 if created else None

    issue_nodes = ((r.get("issues") or {}).get("nodes")) or []
    pr_nodes = ((r.get("pullRequests") or {}).get("nodes")) or []

    # Trailing-365d traffic for the no_traffic / too_young gates.
    yr_ago = repo.now - dt.timedelta(days=365)
    issues_365 = sum(1 for n in issue_nodes if (parse_iso(n.get("createdAt")) or repo.now) >= yr_ago)
    prs_365 = sum(1 for n in pr_nodes if (parse_iso(n.get("createdAt")) or repo.now) >= yr_ago)

    band = "relaxed" if repo.type in RESP_RELAXED_TYPES else "default"
    bands = RESP_BANDS[band]

    # Seeded 90-day window ending `offset` days before now.
    win_end = repo.now - dt.timedelta(days=offset)
    win_start = win_end - dt.timedelta(days=90)

    # =========================================================================
    # LAYER 1: Issue median TTFR (most precise signal)
    # =========================================================================
    issue_ttfrs: list[float] = []
    first_resp_shingles: list[set] = []
    for n in issue_nodes:
        created_i = parse_iso(n.get("createdAt"))
        if created_i is None or not (win_start <= created_i <= win_end):
            continue
        author = (n.get("author") or {}).get("login")
        if is_bot_author(author):
            continue
        candidates: list[tuple[dt.datetime, str]] = []
        # First non-author, non-bot comment
        for cm in ((n.get("comments") or {}).get("nodes") or []):
            cm_author = (cm.get("author") or {}).get("login")
            cm_time = parse_iso(cm.get("createdAt"))
            if cm_time is None:
                continue
            if cm_author and author and cm_author == author:
                continue
            if is_bot_author(cm_author):
                continue
            sh = _shingles(cm.get("bodyText", ""))
            if any(_jaccard(sh, prev) >= 0.8 for prev in first_resp_shingles):
                continue
            first_resp_shingles.append(sh)
            candidates.append((cm_time, "comment"))
            break
        # Timeline events (label/assign/close) — non-author only
        for tl in ((n.get("timelineItems") or {}).get("nodes") or []):
            t = parse_iso(tl.get("createdAt"))
            if t is None:
                continue
            actor = (tl.get("actor") or {}).get("login")
            if is_bot_author(actor):
                continue
            if actor and author and actor == author:
                continue
            candidates.append((t, tl.get("__typename", "event")))
        if candidates:
            first = min(candidates, key=lambda x: x[0])[0]
            ttfr_h = (first - created_i).total_seconds() / 3600.0
            if ttfr_h >= 0:
                issue_ttfrs.append(ttfr_h)

    qualifying_issues = len(issue_ttfrs)
    issue_median = _median(issue_ttfrs) if issue_ttfrs else None

    # =========================================================================
    # LAYER 2: PR median TTR (fallback signal, used when issue sample < 3)
    # =========================================================================
    pr_ttrs: list[float] = []
    for n in pr_nodes:
        created_p = parse_iso(n.get("createdAt"))
        if created_p is None or not (win_start <= created_p <= win_end):
            continue
        author = (n.get("author") or {}).get("login")
        if is_bot_author(author):
            continue
        # PR "response" = first review or comment from non-author
        candidates: list[tuple[dt.datetime, str]] = []
        for rv in ((n.get("reviews") or {}).get("nodes") or []):
            rv_author = (rv.get("author") or {}).get("login")
            rv_time = parse_iso(rv.get("createdAt"))
            if rv_time is None:
                continue
            if rv_author and author and rv_author == author:
                continue
            if is_bot_author(rv_author):
                continue
            candidates.append((rv_time, "review"))
            break  # earliest review only
        for cm in ((n.get("comments") or {}).get("nodes") or []):
            cm_author = (cm.get("author") or {}).get("login")
            cm_time = parse_iso(cm.get("createdAt"))
            if cm_time is None:
                continue
            if cm_author and author and cm_author == author:
                continue
            if is_bot_author(cm_author):
                continue
            candidates.append((cm_time, "comment"))
            break
        if candidates:
            first = min(candidates, key=lambda x: x[0])[0]
            ttr_h = (first - created_p).total_seconds() / 3600.0
            if ttr_h >= 0:
                pr_ttrs.append(ttr_h)

    pr_qualifying = len(pr_ttrs)
    pr_median = _median(pr_ttrs) if pr_ttrs else None

    # Choose the best signal: issues preferred, PRs as fallback
    if qualifying_issues >= 3:
        median_h = issue_median
        qualifying = qualifying_issues
        source = "issue"
    elif pr_qualifying >= 3:
        median_h = pr_median
        qualifying = pr_qualifying
        source = "pr"
    else:
        median_h = None
        qualifying = 0
        source = "none"

    # =========================================================================
    # LAYER 3: No direct signal → do NOT infer from maintenance (adversarial fix)
    # =========================================================================
    # When qualifying == 0, we do NOT fabricate a median_h from maintenance.
    # Inferred grades hide the fact that there is no direct response data.
    # The user should see "?" (no data) rather than "C" (a machine guess).
    # =========================================================================
    maintenance_signal = "direct"
    inferred_from = ""
    if median_h is None:
        # Do not infer — keep median_h as None.
        # Only fetch maintenance for the evidence note in the fallback.
        maint_axis = axis_maintenance(repo)
        maint_grade = maint_axis.grade
        inferred_from = f"maintenance={maint_grade}"
        # maintenance_signal stays "direct" so zero_response can still trigger.
        # median_h stays None.
        # E grade = archived, already handled above

    # =========================================================================
    # ? gates (checked after layer-3 inference)
    # =========================================================================
    if repo_age_days is not None and repo_age_days < 180 and (issues_365 + prs_365) < 6:
        return Axis.unknown("too_young", raw={"window_offset_days": offset},
                            evidence=f"age {repo_age_days:.0f}d<180 & thin traffic -> too_young")
    if issues_365 < 3 and prs_365 < 3:
        return Axis.unknown("no_traffic", raw={"window_offset_days": offset},
                            evidence=f"issues_365={issues_365} prs_365={prs_365} (<3 each) -> no_traffic")

    # Zero-response E clause: last >=10 issues each opened >30d ago, none got a response.
    older = [n for n in issue_nodes
             if (parse_iso(n.get("createdAt")) or repo.now) < (repo.now - dt.timedelta(days=30))
             and not is_bot_author((n.get("author") or {}).get("login"))]
    zero_response = False
    if len(older) >= 10:
        any_resp = False
        for n in older[:10]:
            author = (n.get("author") or {}).get("login")
            has = False
            for cm in ((n.get("comments") or {}).get("nodes") or []):
                ca = (cm.get("author") or {}).get("login")
                if ca and ca != author and not is_bot_author(ca):
                    has = True
                    break
            if not has and ((n.get("timelineItems") or {}).get("nodes") or []):
                for tl in (n.get("timelineItems") or {}).get("nodes" or []):
                    if not is_bot_author((tl.get("actor") or {}).get("login")):
                        has = True
                        break
            if not has and n.get("closedAt"):
                has = True
            any_resp = any_resp or has
        zero_response = not any_resp

    raw = {
        "median_ttfr_hours": _round(median_h, 1) if median_h is not None else None,
        # Historical key name kept for frontmatter compatibility. When source == "pr",
        # this count is qualifying PRs rather than issues.
        "qualifying_issues": qualifying,
        "band": _band_label(band),
        "window_offset_days": offset,
        "source": source,
        "inferred": maintenance_signal == "inferred",
    }

    if zero_response and qualifying == 0 and maintenance_signal != "inferred":
        return Axis("E", raw, evidence="zero non-bot response to last >=10 old issues -> E")

    if median_h is None:
        if zero_response:
            return Axis("E", raw, evidence="no in-window issues + zero-response on old issues -> E")
        return Axis.unknown("no_window_signal", raw=raw,
                            evidence="traffic present but no qualifying issue/PR response in sampled window -> no_window_signal")

    # A-E by median TTFR with type-aware bands.
    if maintenance_signal == "inferred":
        # Inferred grades are capped at C (we don't want to claim A/B without direct data)
        if median_h < bands["C"]:
            return Axis("C", raw, evidence=f"inferred from {inferred_from} -> C (capped)")
        elif median_h < bands["D"]:
            return Axis("D", raw, evidence=f"inferred from {inferred_from} -> D (capped)")
        else:
            return Axis("E", raw, evidence=f"inferred from {inferred_from} -> E")

    sample_label = "issues" if source == "issue" else "PRs"
    if median_h < bands["A"] and qualifying >= bands["A_min_issues"]:
        return Axis("A", raw, evidence=f"median TTFR {median_h:.1f}h <{bands['A']}h & {qualifying}>={bands['A_min_issues']} {sample_label} -> A")
    if median_h < bands["B"] and qualifying >= bands["B_min_issues"]:
        return Axis("B", raw, evidence=f"median TTFR {median_h:.1f}h <{bands['B']}h & {qualifying}>={bands['B_min_issues']} {sample_label} -> B")
    if median_h < bands["C"]:
        return Axis("C", raw, evidence=f"median TTFR {median_h:.1f}h <{bands['C']}h -> C")
    if median_h < bands["D"]:
        return Axis("D", raw, evidence=f"median TTFR {median_h:.1f}h <{bands['D']}h -> D")
    return Axis("E", raw, evidence=f"median TTFR {median_h:.1f}h >={bands['D']}h -> E")


def _band_label(band: str) -> str:
    return "relaxed_solo" if band == "relaxed" else "default"


# ---------------------------------------------------------------------------
# Axis 3 — adoption (spec §2.3)
# ---------------------------------------------------------------------------

ECOSYSTE_LOOKUP = "https://packages.ecosyste.ms/api/v1/packages/lookup?repository_url="
ECOSYSTE_REGISTRY_PKG = "https://packages.ecosyste.ms/api/v1/registries/{reg}/packages/{name}"
NOISE_FLOOR_DOWNLOADS = 1000
# Registries worth a by-name retry when the repo_url lookup maps to nothing usable,
# ordered by how often this index's pages ship there.
NAME_LOOKUP_REGISTRIES = ("npmjs.org", "pypi.org", "crates.io", "rubygems.org", "packagist.org")


# A containment match is only meaningful if the repo name is a substantial part of the
# candidate's name. Without a bound, any long coordinate that happens to embed the repo
# name matches: `com.skillsjars:coreyhaines31__marketingskills__ab-test-setup`, a
# third-party auto-published Maven shell, was accepted as `marketingskills`'s canonical
# package and its 0 dependents then scored the page E.
NAME_MATCH_MAX_LENGTH_RATIO = 3.0


def _name_fuzzy_match(pkg_name: str, repo_name: str) -> bool:
    """Match on normalized names, bounded so containment cannot be arbitrarily diluted."""
    norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
    p, r = norm(pkg_name), norm(repo_name)
    if not p or not r:
        return False
    if p == r:
        return True
    longer, shorter = (p, r) if len(p) >= len(r) else (r, p)
    if shorter not in longer:
        return False
    return len(longer) <= len(shorter) * NAME_MATCH_MAX_LENGTH_RATIO


def _split_scope(pkg_name: str) -> tuple[str | None, str]:
    """`@mui/utils` -> ("mui", "utils"); unscoped names -> (None, name)."""
    if pkg_name.startswith("@") and "/" in pkg_name:
        scope, _, rest = pkg_name[1:].partition("/")
        return scope, rest
    return None, pkg_name


def _match_quality(entry: dict, repo_owner: str, repo_name: str) -> int:
    """How strongly a candidate package claims to BE this repo. Higher is better.

    2 = its name matches the repo name.
    1 = it is scoped to the repo's owner (`@mui/material` for `mui/material-ui`) — the
        monorepo case, where no single package carries the repo's name.
    0 = neither; usable only as a last resort.
    """
    name = entry.get("name", "") or ""
    scope, bare = _split_scope(name)
    # A Go module path is `github.com/{owner}/{repo}`, so the repo name is always a small
    # fraction of it and the length bound in _name_fuzzy_match would reject every Go
    # module outright. Compare the final path segment instead.
    tail = name
    if "/" in name and not name.startswith("@"):
        # Strip a Go major-version suffix first: `github.com/apache/casbin/v3` has the
        # tail `v3`, which matches nothing.
        path = re.sub(r"/v\d+$", "", name)
        tail = path.rsplit("/", 1)[-1]
    if any(_name_fuzzy_match(n, repo_name) for n in (name, bare, tail)):
        return 2
    if scope and _name_fuzzy_match(scope, repo_owner):
        return 1
    return 0


def _is_vcs_pseudo(entry: dict) -> bool:
    """proxy.golang.org synthesizes a module for *any* GitHub repo, named
    `github.com/{owner}/{repo}` — so it always contains the repo name and always wins a
    substring name match, whatever language the repo is actually written in.

    Left in the general pool it silently hijacks the canonical slot: material-ui's real
    npm packages (154k dependents) lost to its Go pseudo-module (2 dependents) and the
    page scored D instead of A. Real Go projects are unaffected — they reach the same
    number through the pkg.go.dev importers fallback below.
    """
    reg = _registry_name(entry)
    return reg == "proxy.golang.org"


def _select_canonical(candidates: list[dict], repo_owner: str, repo_name: str,
                      repo_language: str | None = None) -> dict | None:
    """Canonical = strongest repo claim, then max downloads (spec §2.3).

    Anti-typosquat defense = **name/scope match AND max-downloads**, in that order.
    The spec's original third condition (`rank != null`) is no longer applied: as of
    2026-09 ecosyste.ms returns `rank: null` for *every* candidate of every repo probed
    (flask 18/18, playwright 100/100, material-ui 83/83), so the filter it described
    dropped 100% of candidates and every repo fell through to the fallback branches.

    Dropping it does not weaken the defense, which was always carried by the other two
    conditions: flask's squatters (`f-ask`, dl=18) fail the name match, and the ones that
    pass it (`flask-mirror-upstream`, dl=17) lose max-downloads to the real package
    (dl=133M) by seven orders of magnitude.
    """
    if not candidates:
        return None
    # The Go proxy synthesizes a module for every GitHub repo whatever its language, so
    # its entry is evidence of nothing unless the repo is actually Go. Keeping it as a
    # last-resort candidate turned "no package anywhere" into "a package with 0
    # dependents" — i.e. into a measured E — for 39 pages, among them `swe-agent`, a
    # Python project. It is dropped outright for non-Go repos; real Go projects still
    # reach their number through the pkg.go.dev importers fallback below.
    pool = [c for c in candidates
            if not _is_vcs_pseudo(c) or (repo_language or "").lower() == "go"]
    if not pool:
        return None
    # Prefer the project's own distribution channel over distro archives, mirrors and
    # repackagers. A repackaged build is kept only when it carries a real count, since
    # for some projects it is the only number that exists.
    primary = [c for c in pool if _is_primary_registry(c)]
    if not primary:
        # Nothing on a primary ecosystem. A distro or repackaged entry is worth keeping
        # only if it actually counts something; one with neither downloads nor dependents
        # says only "somebody built this once", and letting it through would license an
        # E verdict off a number nobody measured.
        primary = [c for c in pool
                   if (c.get("downloads") or 0) > 0 or (c.get("dependent_repos_count") or 0) > 0]
        if not primary:
            return None
    pool = primary

    def dl(c):
        return c.get("downloads") or 0

    scored = [(c, _match_quality(c, repo_owner, repo_name)) for c in pool]
    for want in (2, 1):
        tier = [c for c, q in scored if q == want and dl(c) >= NOISE_FLOOR_DOWNLOADS]
        if tier:
            return max(tier, key=dl)
    # Nothing claims the repo by name or scope. Do NOT fall back to whichever candidate
    # has the most downloads: ecosyste.ms's repo -> package mapping carries wrong entries,
    # and picking on volume alone labels a stranger's package as this project's canonical.
    # `jaegertracing/jaeger` was reported as shipping `digitalbanking` on NuGet this way.
    # An unidentified package is `?`; a misidentified one is a false fact on the page, and
    # the install-signal path (§2.3b) still measures whatever the project really ships.
    # No download figures at all (Go, Maven, Spack). Keep the strongest name claimant
    # anyway: identifying the package and finding it has no counts is `registry_no_counts`,
    # a different and more informative answer than `ambiguous` ("we could not tell which
    # package this repo is"). Dependents, where present, still tier it.
    countless = [c for c, q in scored if q > 0 and c.get("downloads") is None]
    if countless:
        return max(countless, key=lambda c: c.get("dependent_repos_count") or 0)
    return None


def _name_variants(repo_name: str) -> list[str]:
    """Plausible package names for a repo, most-likely first.

    ecosyste.ms maps repo -> package by scraping manifests, and the mapping is missing
    for a long tail of repos whose package name differs from the repo name (the usual
    cause is a language suffix: `elasticsearch-dsl-py` ships as `elasticsearch-dsl`).
    """
    base = (repo_name or "").strip()
    out = [base]
    low = base.lower()
    for suf in ("-py", ".py", "-python", "-js", ".js", "-node", "-go", ".go",
                "-rs", ".rs", "-rb", "-ruby", "-php", "-java"):
        if low.endswith(suf) and len(base) > len(suf) + 1:
            out.append(base[: -len(suf)])
    for pre in ("python-", "node-", "go-", "rust-", "ruby-", "php-"):
        if low.startswith(pre) and len(base) > len(pre) + 1:
            out.append(base[len(pre):])
    seen, uniq = set(), []
    for n in out:
        if n and n.lower() not in seen:
            seen.add(n.lower())
            uniq.append(n)
    return uniq


_REPO_IDENTITY_CACHE: dict[str, str | None] = {}


def _resolves_to(recorded: str, want_full: str) -> bool:
    """Is `recorded` (owner/name from a package's metadata) the same repo as `want_full`?

    Matching on the repo *name* alone is not enough, and getting this wrong is silent:
    it attaches a stranger's download figures to a page as a real measurement. Two live
    collisions caught before the backfill ran — `crates.io/waza` is a placeholder crate
    at `mattjperez/waza` ("Reserved name"), nothing to do with `tw93/Waza`; `npmjs.org/d2`
    is `dhis2/d2`, a DHIS2 client library, nothing to do with `d2lang/d2`.

    Owner equality alone is too strict the other way, because org renames and transfers
    leave the old owner in ecosyste.ms's record. GitHub resolves those: asking it for
    `elasticsearch/elasticsearch-dsl-py` returns `elastic/elasticsearch-dsl-py`. So:
    accept on exact match, else accept only if GitHub redirects the recorded repo to
    exactly the repo we are scoring.
    """
    if recorded.lower() == want_full.lower():
        return True
    if recorded not in _REPO_IDENTITY_CACHE:
        res = gh_api(f"repos/{recorded}")
        full = None
        if isinstance(res.json, dict):
            full = res.json.get("full_name")
        _REPO_IDENTITY_CACHE[recorded] = full
    resolved = _REPO_IDENTITY_CACHE[recorded]
    return bool(resolved) and resolved.lower() == want_full.lower()


def _github_repos_in(urls) -> list[str]:
    """owner/name for every github.com repo URL among `urls`, first-seen order.

    Registry metadata spells the same link many ways — `git+https://github.com/o/r.git`,
    `github:o/r`, `https://github.com/o/r/issues` — and all of them name the repo in the
    first two path segments.
    """
    out: list[str] = []
    for u in urls:
        if not isinstance(u, str):
            continue
        m = (re.search(r"github\.com[/:]([\w.-]+)/([\w.-]+)", u)
             or re.fullmatch(r"\s*github:([\w.-]+)/([\w.-]+)\s*", u))
        if not m:
            continue
        full = f"{m.group(1)}/{m.group(2).removesuffix('.git')}"
        if full.lower() not in (x.lower() for x in out):
            out.append(full)
    return out


def _registry_links_back(reg: str, name: str, want_full: str,
                         default_branch: str | None) -> str | None:
    """Ask the registry itself whether package `name` was published from `want_full`.

    Consulted only when ecosyste.ms's record for the package carries no repository_url.
    Its mapping is a scrape of the registry, and the scrape misses links the registry
    does hold: PyPI's `harnessrouter` lists the repo as `Source` while ecosyste.ms has
    an empty field. Returns how the link was shown, or None.

    A name match alone is never enough (see `_resolves_to`); the registry has to name
    this repo. npm packages often omit `repository` entirely, so npm also accepts the
    commit the tarball was built from (`gitHead`) when it lies on this repo's default
    branch. Default branch, not "exists in the repo": GitHub serves any commit of the
    fork network through the parent's API, so a stranger's fork that published under
    the same name would otherwise pass.
    """
    q = urllib.parse.quote(name, safe="@")
    urls: list = []
    commit = None
    if reg == "npmjs.org":
        st, j = http_get_json(f"https://registry.npmjs.org/{q}/latest", retries=1)
        if st != 200 or not isinstance(j, dict):
            return None
        repo_field = j.get("repository")
        urls = [repo_field.get("url") if isinstance(repo_field, dict) else repo_field,
                j.get("homepage"),
                (j.get("bugs") or {}).get("url") if isinstance(j.get("bugs"), dict) else j.get("bugs")]
        commit = j.get("gitHead")
    elif reg == "pypi.org":
        st, j = http_get_json(f"https://pypi.org/pypi/{q}/json", retries=1)
        info = (j or {}).get("info") if isinstance(j, dict) else None
        if st != 200 or not isinstance(info, dict):
            return None
        urls = [info.get("home_page"), info.get("download_url"),
                *((info.get("project_urls") or {}).values())]
    elif reg == "crates.io":
        st, j = http_get_json(f"https://crates.io/api/v1/crates/{q}", retries=1)
        crate = (j or {}).get("crate") if isinstance(j, dict) else None
        if st != 200 or not isinstance(crate, dict):
            return None
        urls = [crate.get("repository"), crate.get("homepage")]
    elif reg == "rubygems.org":
        st, j = http_get_json(f"https://rubygems.org/api/v1/gems/{q}.json", retries=1)
        if st != 200 or not isinstance(j, dict):
            return None
        urls = [j.get("source_code_uri"), j.get("homepage_uri"), j.get("bug_tracker_uri")]
    elif reg == "packagist.org":
        st, j = http_get_json(f"https://packagist.org/packages/{name}.json", retries=1)
        pkg = (j or {}).get("package") if isinstance(j, dict) else None
        if st != 200 or not isinstance(pkg, dict):
            return None
        urls = [pkg.get("repository")]

    for full in _github_repos_in(urls):
        if _resolves_to(full, want_full):
            return f"{reg}_metadata"
    if commit and default_branch and re.fullmatch(r"[0-9a-f]{40}", str(commit)):
        res = gh_api(f"repos/{want_full}/compare/{commit}...{urllib.parse.quote(default_branch, safe='')}")
        if isinstance(res.json, dict) and res.json.get("status") in ("ahead", "identical"):
            return f"{reg}_git_head"
    return None


def _lookup_by_name(repo_owner: str, repo_name: str, *,
                    default_branch: str | None = None) -> dict | None:
    """Secondary discovery: find the package by *name* when repo_url lookup came up empty.

    ecosyste.ms builds its repo -> package mapping by scraping manifests and the mapping
    has a long tail of gaps; a gap there is not evidence of an unpackaged project
    (`elasticsearch-dsl-py` ships as `elasticsearch-dsl` and is mapped to neither).
    Every hit must be shown to come from this repo before its numbers are used: its
    ecosyste.ms `repository_url` survives `_resolves_to`, or — when that field is empty —
    the registry's own metadata links back (`_registry_links_back`). A field that names
    a *different* repo is a rejection, not a gap, and is never overruled.
    """
    want_full = f"{repo_owner}/{repo_name}"
    best = None
    for name in _name_variants(repo_name):
        for reg in NAME_LOOKUP_REGISTRIES:
            url = ECOSYSTE_REGISTRY_PKG.format(
                reg=reg, name=urllib.parse.quote(name, safe=""))
            status, data = http_get_json(url, retries=1)
            if status != 200 or not isinstance(data, dict):
                continue
            if (data.get("downloads") or 0) < NOISE_FLOOR_DOWNLOADS \
                    and not (data.get("dependent_repos_count") or 0):
                continue
            back = (data.get("repository_url") or "").strip().rstrip("/")
            if back:
                m = re.search(r"github\.com/([^/]+/[^/\s]+?)(?:\.git)?$", back)
                if not m or not _resolves_to(m.group(1), want_full):
                    continue
                link = "ecosystems_repository_url"
            else:
                link = _registry_links_back(reg, data.get("name") or name, want_full,
                                            default_branch)
                if link is None:
                    continue
            cand = dict(data)
            cand["registry"] = reg
            cand["_via"] = "name_lookup"
            cand["_package_link"] = link
            if best is None or (cand.get("downloads") or 0) > (best.get("downloads") or 0):
                best = cand
        if best is not None:
            return best
    return best


# ecosyste.ms returns `registry` as an object carrying `ecosystem`, but some call paths
# (and this suite's fixtures) carry only the name. Fall back to the name for the primary
# registries, so a bare string is not silently treated as an unknown repackager.
REGISTRY_NAME_TO_ECOSYSTEM = {
    "npmjs.org": "npm", "pypi.org": "pypi", "crates.io": "cargo",
    "rubygems.org": "rubygems", "packagist.org": "packagist",
    "repo1.maven.org": "maven", "nuget.org": "nuget", "proxy.golang.org": "go",
    "hex.pm": "hex", "pub.dev": "pub", "cocoapods.org": "cocoapods",
    "cran.r-project.org": "cran", "metacpan.org": "cpan", "bower.io": "bower",
}


def _registry_ecosystem(entry: dict) -> str | None:
    reg = entry.get("registry")
    if isinstance(reg, dict):
        return reg.get("ecosystem") or REGISTRY_NAME_TO_ECOSYSTEM.get(reg.get("name") or "")
    return REGISTRY_NAME_TO_ECOSYSTEM.get(reg or "")


def _is_primary_registry(entry: dict) -> bool:
    """Is this candidate the project's own distribution channel, rather than a repackage?"""
    if _registry_name(entry) in MIRROR_REGISTRIES:
        return False
    if _registry_name(entry) in SECONDARY_REGISTRIES:
        return False
    return _registry_ecosystem(entry) in PRIMARY_ECOSYSTEMS


def _registry_name(entry: dict) -> str | None:
    reg = entry.get("registry")
    if isinstance(reg, dict):
        return reg.get("name")
    return reg


def _direct_registry_downloads(kind: str, pkg: str) -> int | None:
    """Cross-check last-month downloads via the direct registry API (spec §2.3)."""
    pkg_q = urllib.parse.quote(pkg, safe="")
    if kind == "npm":
        st, j = http_get_json(f"https://api.npmjs.org/downloads/point/last-month/{pkg_q}")
        return j.get("downloads") if isinstance(j, dict) else None
    if kind == "pypi":
        st, j = http_get_json(f"https://pypistats.org/api/packages/{pkg_q}/recent")
        if isinstance(j, dict):
            return (j.get("data") or {}).get("last_month")
        return None
    if kind == "crates":
        st, j = http_get_json(f"https://crates.io/api/v1/crates/{pkg_q}")
        if isinstance(j, dict):
            return (j.get("crate") or {}).get("recent_downloads")
        return None
    if kind == "rubygems":
        st, j = http_get_json(f"https://rubygems.org/api/v1/gems/{pkg_q}.json")
        return j.get("downloads") if isinstance(j, dict) else None
    if kind == "packagist":
        st, j = http_get_json(f"https://packagist.org/packages/{pkg_q}.json")
        if isinstance(j, dict):
            return ((j.get("package") or {}).get("downloads") or {}).get("monthly")
        return None
    return None


# ---------------------------------------------------------------------------
# Adoption fallback instruments (spec §2.3b)
#
# Registry downloads answer "how many projects install this" only for things that ship
# to a registry. An IDE, a database server or a CLI binary is adopted just as measurably
# — it just leaves its trace somewhere else. Scoring those `?` reported a gap in our
# instruments as a gap in the project.
#
# Each instrument below counts a real install/pull event, never attention (stars, forks,
# watchers). Measured on this index's own cohort, star count ranks essentially
# independently of adoption (Spearman 0.13 vs grade, 0.065 vs dependents, 0.007 vs
# downloads over 268 scored pages), so it is not a usable stand-in and is not used.
# ---------------------------------------------------------------------------

HEALTH_CACHE_DIR = Path(
    os.environ.get("OSS_ATLAS_HEALTH_CACHE")
    or (Path(__file__).resolve().parent.parent / ".health-cache"))
BREW_CACHE_TTL_S = 24 * 3600


def _cache_json(key: str, ttl: int, fetch):
    """Disk-cached JSON, shared across processes.

    The batch runner invokes this scorer once per page, so a whole-registry index that is
    cheap once (Homebrew ships ~20MB of formula + analytics JSON) would otherwise be
    re-downloaded several hundred times in a single rerun.
    """
    path = HEALTH_CACHE_DIR / f"{key}.json"
    try:
        if path.exists() and (time.time() - path.stat().st_mtime) < ttl:
            return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        pass
    data = fetch()
    # Never cache an empty result. A transport failure and "this index is genuinely
    # empty" produce the same {} here, and persisting it would serve that emptiness as
    # a measured fact for the whole TTL — every later page would score as if Homebrew
    # had no record of it, which is indistinguishable from a real answer.
    if data:
        try:
            HEALTH_CACHE_DIR.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(data), encoding="utf-8")
        except OSError:
            pass
    return data


_BREW: dict | None = None


def _brew_tables() -> dict:
    """{"<owner>/<repo>": installs_90d} built from Homebrew's own formula/cask metadata.

    Keyed by the GitHub repo each formula declares, not by formula name: `bat` the
    formula and `bat` the repo agree, but `visual-studio-code` and `microsoft/vscode`
    do not, and name-guessing silently attaches one project's installs to another.
    """
    global _BREW
    if _BREW is not None:
        return _BREW

    def build():
        repo_to_tokens: dict[str, list[list[str]]] = {}
        for api, kind in (("formula", "formula"), ("cask", "cask")):
            st, data = http_get_json(f"https://formulae.brew.sh/api/{api}.json",
                                     timeout=120, retries=1)
            if st != 200 or not isinstance(data, list):
                continue
            for it in data:
                urls = [it.get("homepage"), it.get("url")]
                u = it.get("urls") or {}
                for kk in ("stable", "head"):
                    v = u.get(kk) or {}
                    if isinstance(v, dict):
                        urls.append(v.get("url"))
                tok = it.get("token") or it.get("name")
                if isinstance(tok, list):
                    tok = tok[0] if tok else None
                if not tok:
                    continue
                for uu in urls:
                    m = re.search(r"github\.com/([^/]+)/([^/\s#?]+?)(?:\.git)?(?:/|$)", str(uu or ""))
                    if m:
                        key = f"{m.group(1).lower()}/{m.group(2).lower()}"
                        repo_to_tokens.setdefault(key, []).append([kind, str(tok)])
                        break
        counts: dict[str, int] = {}
        for path, kind in (("analytics/install/90d.json", "formula"),
                           ("analytics/cask-install/90d.json", "cask")):
            st, d = http_get_json(f"https://formulae.brew.sh/api/{path}", timeout=120, retries=1)
            if st != 200 or not isinstance(d, dict):
                continue
            for item in d.get("items", []):
                nm = item.get("formula") or item.get("cask") or item.get("token")
                try:
                    counts[f"{kind}:{str(nm).split()[0]}"] = int(
                        str(item.get("count", "0")).replace(",", ""))
                except (ValueError, AttributeError):
                    pass
        out = {}
        for repo_key, toks in repo_to_tokens.items():
            best = max((counts.get(f"{k}:{t}", 0) for k, t in toks), default=0)
            if best:
                out[repo_key] = best
        return out

    _BREW = _cache_json("homebrew_installs_90d", BREW_CACHE_TTL_S, build) or {}
    return _BREW


def _homebrew_installs(owner: str, name: str) -> int | None:
    return _brew_tables().get(f"{owner.lower()}/{name.lower()}")


def _release_downloads(repo: RepoData) -> tuple[int | None, int]:
    """(total asset downloads across published releases, asset count).

    Counts only uploaded release *assets* — installers, binaries, wheels attached by
    hand. A source-tarball-only release reports nothing here, which is correct: GitHub
    generates those for every tag whether or not anyone wants them.
    """
    res = gh_api(f"repos/{repo.full}/releases?per_page=100")
    data = res.json if isinstance(res.json, list) else None
    if data is None:
        return None, 0
    total, assets = 0, 0
    for rel in data:
        for a in (rel.get("assets") or []):
            total += a.get("download_count") or 0
            assets += 1
    return (total if assets else None), assets


def _docker_pulls(repo: RepoData) -> tuple[int | None, str | None]:
    """Docker Hub pull count, only for a repository that names this GitHub repo back.

    Namespace guessing alone is unsafe — `grafana/loki` and `prometheus/prometheus` are
    fine, but plenty of short names collide with unrelated images. Each guess is accepted
    only if Docker Hub's description or full description points at the same GitHub repo,
    or the namespace equals the GitHub owner.
    """
    owner, name = repo.owner.lower(), repo.name.lower()
    for ns, rn in ((owner, name), (name, name), ("library", name)):
        time.sleep(DOCKER_PROBE_DELAY_S)
        st, d = http_get_json(f"https://hub.docker.com/v2/repositories/{ns}/{rn}", retries=1)
        if st != 200 or not isinstance(d, dict):
            continue
        pulls = d.get("pull_count")
        if not pulls:
            continue
        blob = f"{d.get('description') or ''} {d.get('full_description') or ''}".lower()
        if ns == owner or ns == "library" or f"github.com/{owner}/{name}" in blob:
            return int(pulls), f"{ns}/{rn}"
    return None, None


def _tier_from_anchors(value: int | None, anchors: tuple[int, int, int]) -> str | None:
    """value -> A/B/C/D against (A_floor, B_floor, C_floor). None -> None.

    **E is deliberately unreachable here**, unlike the registry path. The two directions
    of this evidence are not symmetric: a large install count proves the project is
    adopted, but a small one does not prove it is not, because the channel we can read
    may not be the channel its users take. A tool distributed mainly by `git clone` or a
    curl-to-shell script can show a handful of release-asset downloads while being widely
    used, and calling that E would assert "measurably unadopted" from a number that never
    measured the main path. The registry path keeps E because there the registry *is* the
    distribution channel, so absence there is real absence.
    """
    if value is None:
        return None
    a, b, c = anchors
    if value >= a:
        return "A"
    if value >= b:
        return "B"
    if value >= c:
        return "C"
    return "D"


def _adoption_from_install_signals(repo: RepoData, archived: bool) -> Axis | None:
    """Score adoption from install events for projects that ship no registry package.

    Tier = max() over whatever instruments answered, matching the registry path's
    max(graph_tier, volume_tier): a project is as adopted as its strongest real
    distribution channel, and being absent from a channel it never used is not evidence
    against it. Returns None when nothing answered, leaving the caller to decide between
    `?`, `N/A` and E.
    """
    raw: dict = {"registry": None, "canonical_package": None}
    tiers: list[str] = []

    brew = _homebrew_installs(repo.owner, repo.name)
    if brew is not None:
        raw["homebrew_installs_90d"] = brew
        t = _tier_from_anchors(brew, BREW_INSTALL_ANCHORS)
        raw["homebrew_tier"] = t
        tiers.append(t)

    rel, n_assets = _release_downloads(repo)
    if rel is not None:
        raw["release_downloads"] = rel
        raw["release_assets"] = n_assets
        t = _tier_from_anchors(rel, RELEASE_DOWNLOAD_ANCHORS)
        raw["release_tier"] = t
        tiers.append(t)

    pulls, image = _docker_pulls(repo) if repo.type in DOCKER_PROBE_TYPES else (None, None)
    if pulls is not None:
        raw["docker_pulls"] = pulls
        raw["docker_image"] = image
        t = _tier_from_anchors(pulls, DOCKER_PULL_ANCHORS)
        raw["docker_tier"] = t
        tiers.append(t)

    tiers = [t for t in tiers if t]
    if not tiers:
        return None
    tier = functools.reduce(tier_max, tiers)
    # Name the channel the grade actually came from. Without it a reader sees a letter
    # and `registry: null` and cannot tell whether it rests on 112M binary downloads or
    # on a Docker counter that a CI pipeline inflated.
    raw["signal_basis"] = "+".join(
        k for k, present in (("homebrew", "homebrew_tier" in raw),
                             ("releases", "release_tier" in raw),
                             ("docker", "docker_tier" in raw)) if present)
    if archived:
        raw["archived"] = True
    ax = Axis(tier, raw,
              evidence=f"install signals brew={raw.get('homebrew_installs_90d')} "
                       f"releases={raw.get('release_downloads')} "
                       f"docker={raw.get('docker_pulls')} -> {tier}")
    return ax


def axis_adoption(repo: RepoData) -> Axis:
    url = ECOSYSTE_LOOKUP + urllib.parse.quote(
        f"https://github.com/{repo.full}", safe="")
    status, data = http_get_json(url, retries=2)
    archived = bool(repo.core.json.get("archived")) if isinstance(repo.core.json, dict) else False

    if status == 0 or status >= 400:
        return Axis.unknown("registry_lookup_failed", evidence=f"? ecosyste.ms lookup HTTP {status}")

    candidates = data if isinstance(data, list) else []
    canonical = _select_canonical(candidates, repo.owner, repo.name,
                                  (repo.core.json or {}).get("language")
                                  if isinstance(repo.core.json, dict) else None)

    # Secondary discovery before conceding: ecosyste.ms's repo -> package mapping has a
    # long tail of gaps, and a gap there is not evidence of an unpackaged project.
    if canonical is None:
        canonical = _lookup_by_name(
            repo.owner, repo.name,
            default_branch=(repo.core.json or {}).get("default_branch")
            if isinstance(repo.core.json, dict) else None)

    if canonical is None:
        # Ships no registry package. Before concluding anything, ask the instruments that
        # fit how this kind of artifact actually reaches its users (spec §2.3b).
        fallback = _adoption_from_install_signals(repo, archived)
        if fallback is not None:
            return fallback
        if repo.type in ADOPTION_NO_PACKAGE_TYPES:
            if repo.type in ADOPTION_NA_TYPES:
                return Axis.not_applicable(
                    "no_install_channel",
                    evidence=f"type {repo.type}: copied, not installed — no install event exists to count")
            return Axis.unknown("no_package_structural",
                                evidence=f"type {repo.type} & no canonical package or install signal")
        # A successful empty lookup for package-relevant types is measurably unadopted -> E (spec §2.3).
        if candidates:
            return Axis.unknown("ambiguous",
                                evidence=f"{len(candidates)} candidates, none clears noise filter -> ambiguous")
        return Axis("E", {"registry": None, "canonical_package": None,
                          "dependent_repos_count": 0, "downloads_last_month": None,
                          "graph_tier": "E", "volume_tier": None,
                          "cross_check_divergence": None,
                          "archived": archived},
                    evidence=f"type {repo.type}, ecosyste.ms found 0 packages -> E (unadopted)")

    registry = _registry_name(canonical)
    pkg_name = canonical.get("name")
    dep_repos_raw = canonical.get("dependent_repos_count")
    downloads = canonical.get("downloads")
    dep_repos = int(dep_repos_raw) if dep_repos_raw is not None else None

    graph_tier = graph_tier_from_dependents(dep_repos) if dep_repos is not None else None
    volume_tier = volume_tier_from_downloads(downloads, registry or "")

    # Go importers fallback (no download counts): map importers to the dependents column.
    if registry == "proxy.golang.org" and downloads is None:
        importers = _go_importers(pkg_name)
        if importers is not None:
            graph_tier = tier_max(graph_tier, graph_tier_from_dependents(importers))
            dep_repos = max(dep_repos or 0, importers)

    if dep_repos is None and volume_tier is None:
        # A package exists but carries no comparable counts. That is a gap in the
        # registry's bookkeeping, not proof the project has no measurable reach — try
        # the install channels before conceding, same as the no-package path.
        fallback = _adoption_from_install_signals(repo, archived)
        if fallback is not None:
            fallback.raw["registry"] = registry
            fallback.raw["canonical_package"] = pkg_name
            return fallback
        return Axis.unknown("registry_no_counts",
                            raw={"registry": registry, "canonical_package": pkg_name},
                            evidence="? canonical package exists but comparable dependents/download counts unavailable")

    tier = tier_max(graph_tier, volume_tier)

    # E guard: only if dep_repos == 0 AND downloads below E-floor (AND on both).
    e_floor = (ADOPTION_VOLUME_ANCHORS.get(registry or "") or (0, 0, 0, 0))[3]
    if dep_repos == 0 and downloads is not None and downloads < e_floor:
        tier = "E"
    elif dep_repos == 0 and downloads is None and volume_tier is None and graph_tier == "E":
        tier = "E"
    # Mandatory cross-check for A/B results.
    divergence = None
    needs_review = False
    if tier in ("A", "B"):
        kind = REGISTRY_CROSSCHECK.get(registry or "")
        if kind and pkg_name:
            direct = _direct_registry_downloads(kind, pkg_name)
            if direct is not None and downloads:
                ratio = max(direct, downloads) / max(1, min(direct, downloads))
                divergence = round(ratio, 2)
                if ratio > 2.0:
                    needs_review = True

    raw = {
        "registry": registry,
        "canonical_package": pkg_name,
        "dependent_repos_count": dep_repos,
        "downloads_last_month": downloads,
        "graph_tier": graph_tier if graph_tier else "?",
        "volume_tier": volume_tier if volume_tier else "?",
        "cross_check_divergence": divergence,
    }
    # How a by-name hit was tied to this repo, so a reader can audit the one path where
    # the package was not found through the repo itself.
    if canonical.get("_package_link"):
        raw["package_link"] = canonical["_package_link"]

    # Having a registry package does not mean the registry is where this project's users
    # get it. Binary-first tools keep a token package and ship through releases: jq reads
    # as a minor conda package (-> D) while 295M people pulled its binaries; ripgrep the
    # same (-> D, 53M binaries); ImageMagick and ComfyUI scored E. So the install channels
    # are measured for every project, not only for those with no package at all, and the
    # axis takes the best of the two — the same max() the registry path already applies
    # across its own two sub-signals.
    #
    # This cannot inflate a registry-first project, which is what the symmetric evidence
    # shows: angular publishes 24.6M npm downloads a month and 324 release-asset
    # downloads, ray 276, faker 716. A channel a project does not use reports nothing,
    # and max() with nothing is unchanged.
    install = _adoption_from_install_signals(repo, archived)
    if install is not None:
        raw.update({k: v for k, v in install.raw.items()
                    if k not in ("registry", "canonical_package")})
        if GRADE_ORDER.index(install.grade) < GRADE_ORDER.index(tier):
            raw["tier_source"] = raw.get("signal_basis")
            tier = install.grade
        else:
            raw["tier_source"] = "registry"
    else:
        raw["tier_source"] = "registry"

    if archived:
        raw["archived"] = True
    ax = Axis(tier, raw,
              evidence=f"registry={registry} pkg={pkg_name} dep_repos={dep_repos} "
                       f"dl={downloads} graph={graph_tier} vol={volume_tier} "
                       f"install={install.grade if install else None} -> {tier}")
    ax.needs_human_review = needs_review
    return ax


def _go_importers(module: str | None) -> int | None:
    if not module:
        return None
    status, text = http_get_text(f"https://pkg.go.dev/{module}?tab=importedby")
    if not text:
        return None
    m = re.search(r"([0-9,]+)\s+packages? import", text) or \
        re.search(r"Imported By[^0-9]*([0-9,]+)", text)
    if m:
        return int(m.group(1).replace(",", ""))
    return None


# ---------------------------------------------------------------------------
# Axis 4 — longevity (spec §2.4)
# ---------------------------------------------------------------------------

def axis_longevity(repo: RepoData) -> Axis:
    core = repo.core
    if core.status in (404, 451) or (core.status == 403 and core.json is None):
        return Axis.unknown("not_found", evidence=f"? core repo HTTP {core.status}")
    if not core.ok or not isinstance(core.json, dict):
        return Axis.unknown("not_found", evidence=f"? core repo HTTP {core.status}")

    c = core.json
    archived = bool(c.get("archived"))
    disabled = bool(c.get("disabled"))
    created_at = c.get("created_at")
    repo_age_days = days_since(created_at, repo.now)

    if repo_age_days is None:
        return Axis.unknown("not_found", evidence="? created_at unreadable")

    last_commit_date = repo.last_commit_date()
    last_age = days_since(last_commit_date, repo.now)
    if last_age is None:
        # Fall back to pushed_at only if /commits errored (spec §2.4 fallback).
        last_age = days_since(c.get("pushed_at"), repo.now)
    if last_age is None:
        return Axis.unknown("no_activity_signal",
                            evidence="? created_at present but no commit/pushed_at signal")

    cohort = repo.type if repo.type in LONGEVITY_AGE_BARS else "tool"
    a_age, b_age, c_age = LONGEVITY_AGE_BARS[cohort]
    raw = {
        "repo_age_days": _round(repo_age_days),
        "last_commit_age_days": _round(last_age),
        "cohort": cohort,
    }

    if archived or disabled or last_age > 730:
        return Axis("E", raw,
                    evidence=f"archived={archived} disabled={disabled} last_commit {last_age:.0f}d -> E")
    if last_age <= 90 and repo_age_days >= a_age:
        return Axis("A", raw, evidence=f"age {repo_age_days:.0f}d>={a_age} & last_commit {last_age:.0f}d<=90 -> A")
    if last_age <= 180 and repo_age_days >= b_age:
        return Axis("B", raw, evidence=f"age {repo_age_days:.0f}d>={b_age} & last_commit {last_age:.0f}d<=180 -> B")
    if last_age <= 365 and repo_age_days >= c_age:
        return Axis("C", raw, evidence=f"age {repo_age_days:.0f}d>={c_age} & last_commit {last_age:.0f}d<=365 -> C")
    # D: nascent-unproven (recent but young) OR 1-2y stalling.
    return Axis("D", raw,
                evidence=f"age {repo_age_days:.0f}d (cohort C-age {c_age}) / last_commit {last_age:.0f}d -> D")


# ---------------------------------------------------------------------------
# Axis 5 — governance (spec §2.5)
# ---------------------------------------------------------------------------

def axis_governance(repo: RepoData) -> Axis:
    core = repo.core
    if not core.ok or not isinstance(core.json, dict):
        return Axis.unknown("empty_or_gated", evidence=f"? core repo HTTP {core.status}")
    if bool(core.json.get("fork")):
        return Axis.unknown("fork", evidence="native fork (.fork=true) -> fork")

    res = gh_stats(f"repos/{repo.full}/stats/contributors")
    if res.status == 409:
        return Axis.unknown("empty_or_gated", evidence="? stats/contributors 409 empty")
    if res.status == 202 or not res.ok or not isinstance(res.json, list):
        return Axis.unknown("empty_or_gated",
                            evidence=f"? stats/contributors HTTP {res.status} (cold 202 / gated)")
    if not res.json:
        return Axis.unknown("unattributable", evidence="? stats/contributors empty list")

    # Sum each author's weekly commits over the trailing 52 weeks (unbiased 12mo).
    cutoff = int((repo.now - dt.timedelta(weeks=52)).timestamp())
    author_counts: dict[str, int] = {}
    null_login_squash = 0
    total_in_window = 0
    for entry in res.json:
        author = entry.get("author") or {}
        login = author.get("login")
        weeks = entry.get("weeks") or []
        cnt = sum(w.get("c", 0) for w in weeks
                  if isinstance(w, dict) and w.get("w", 0) >= cutoff and w.get("c", 0))
        if cnt <= 0:
            continue
        total_in_window += cnt
        if login is None:
            null_login_squash += cnt
        if is_bot_author(login):
            continue
        key = login or f"_anon_{len(author_counts)}"
        author_counts[key] = author_counts.get(key, 0) + cnt

    # Unattributable: >50% in-window commits have null login (monorepo-export/vendored).
    if total_in_window > 0 and null_login_squash / total_in_window > 0.5:
        return Axis.unknown("unattributable",
                            evidence=f"{null_login_squash}/{total_in_window} null-login commits -> unattributable")

    active = len(author_counts)
    if active == 0:
        return Axis.unknown("unattributable", evidence="active==0 after filtering -> unattributable")

    human_total = sum(author_counts.values())
    counts_sorted = sorted(author_counts.values(), reverse=True)
    top1_share = counts_sorted[0] / human_total if human_total else 0.0
    top3_share = sum(counts_sorted[:3]) / human_total if human_total else 0.0

    raw = {
        "active_maintainers_12mo": active,
        "top1_share": round(top1_share, 3),
        "top3_share": round(top3_share, 3),
        "window_source": "stats_contributors",
        "carve_out": None,
    }

    # Tiers (NO E on this axis; "no one home" is Maintenance's E).
    if active >= 5 and top1_share <= 0.40 and top3_share <= 0.75:
        return Axis("A", raw, evidence=f"active={active}>=5 top1={top1_share:.2f}<=.40 top3={top3_share:.2f}<=.75 -> A")
    if active >= 3 and top1_share <= 0.60:
        return Axis("B", raw, evidence=f"active={active}>=3 top1={top1_share:.2f}<=.60 -> B")
    if active == 2 or (active >= 3 and 0.60 < top1_share <= 0.80):
        return Axis("C", raw, evidence=f"active={active} top1={top1_share:.2f} -> C")

    # D: active==1 OR top1_share>0.80 regardless of headcount.
    base = "D"
    ev = f"active={active} top1={top1_share:.2f} -> D"
    # Single-maintainer carve-out (stable_solo): D driven solely by active==1, for
    # type in {library,tool}, age>=3y, maintenance not D/E. Needs maintenance result;
    # applied later in score() where maintenance is known. Mark candidacy here.
    raw["_solo_candidate"] = (active == 1 and top1_share <= 0.80
                              and repo.type in ("library", "tool"))
    return Axis(base, raw, evidence=ev)


# ---------------------------------------------------------------------------
# Axis 6 — risk_license (spec §2.6)
# ---------------------------------------------------------------------------

_LICENSE_KEY_CACHE: dict[str, dict] = {}


def _license_conditions(key: str) -> dict | None:
    if key in _LICENSE_KEY_CACHE:
        return _LICENSE_KEY_CACHE[key]
    res = gh_api(f"licenses/{key}")
    if res.ok and isinstance(res.json, dict):
        out = {"conditions": res.json.get("conditions") or [],
               "limitations": res.json.get("limitations") or []}
        _LICENSE_KEY_CACHE[key] = out
        return out
    return None


def _classify_permissiveness(conditions: list[str]) -> str:
    cond = set(conditions or [])
    if cond <= {"include-copyright", "document-changes"}:
        return "permissive"
    has_disclose = "disclose-source" in cond
    has_same = any(item == "same-license" or item.startswith("same-license--") for item in cond)
    has_network = "network-use-disclose" in cond
    if has_disclose and has_same and has_network:
        return "strong_network_copyleft"
    if has_disclose and has_same:  # disclose-source + same-license, no network
        return "weak_file_copyleft"
    return "permissive"


def axis_risk_license(repo: RepoData) -> Axis:
    if repo.declared_license in DECLARED_PROPRIETARY_LICENSES:
        return Axis("E", {"spdx_id": repo.declared_license,
                          "permissiveness": "source_available",
                          "relicense_36mo": False, "content_license": None},
                    evidence=f"declared {repo.declared_license} license -> E")

    res = gh_api(f"repos/{repo.full}/license")
    if res.status == 404:
        # A 404 here does NOT mean "unlicensed". GitHub's endpoint 404s whenever its
        # detector cannot *classify* a license, which includes a perfectly real license
        # in a place it does not look. apache/poi keeps Apache-2.0 at `legal/LICENSE`
        # and this endpoint returns 404, so the old `404 -> NONE -> E` shortcut graded
        # the ASF's flagship Java library as all-rights-reserved and capped the whole
        # page to D. Same shape as the bugs in rubric 1.2b: "could not detect" became
        # "does not exist". So look for the file before concluding there isn't one.
        if not repo.core.ok:
            return Axis.unknown("repo_unreachable", evidence=f"? repo HTTP {repo.core.status}")
        found, how = _find_license_path(repo)
        if how == "dedicated_dir":
            return Axis.unknown(
                "license_multi_file",
                evidence=f"? repo uses a per-SPDX license directory ({found}); no single file "
                         "states the project's own terms")
        if found:
            # A license exists but GitHub could not classify it — exactly the state the
            # NOASSERTION path already handles, so reuse it rather than inventing a
            # second, looser verdict. It stays conservative: SSPL/BSL/Elastic still
            # grade E, and an OSI-looking blob yields `?` for manual review instead of
            # an unearned A (rubric 2.6).
            return _risk_noassertion(repo, found)
        # No license *file*, which is not the same as no license: pygame ships LGPL-2.1
        # and openresty/lua-nginx-module BSD-2-Clause, both declared in the README with no
        # LICENSE file to find. Calling those all-rights-reserved is a false claim, and it
        # capped their pages. The page's own `license:` field already separates the two
        # cases, and the scorer trusts that field in the other direction already (a
        # declared Proprietary license grades E above), so consult it here too. It can only
        # buy `?` — never a grade — so a human-entered field still cannot flatter a page.
        declared = (repo.declared_license or "").strip()
        if declared and DECLARED_REAL_LICENSE_RE.match(declared) \
                and not DECLARED_NO_LICENSE_RE.match(declared):
            return Axis.unknown(
                "license_declared_unverifiable",
                evidence=f"? page declares {declared} but no LICENSE file exists to confirm it "
                         f"(GitHub's detector found none either)")
        return Axis("E", {"spdx_id": "NONE", "permissiveness": "source_available",
                          "relicense_36mo": False, "content_license": None},
                    evidence="no LICENSE file anywhere and none declared -> NONE -> E")
    if res.status in (403, 451) and res.json is None and not repo.core.ok:
        return Axis.unknown("repo_unreachable", evidence=f"? repo HTTP {repo.core.status}")
    if not res.ok or not isinstance(res.json, dict):
        return Axis.unknown("repo_unreachable", evidence=f"? license endpoint HTTP {res.status}")

    lic = res.json.get("license") or {}
    spdx = lic.get("spdx_id")
    key = lic.get("key")
    lic_path = res.json.get("path")

    content_license = None
    if spdx and CONTENT_LICENSE_RE.match(spdx):
        content_license = spdx

    # NOASSERTION disambiguation: read the LICENSE blob.
    if spdx in (None, "NOASSERTION"):
        return _risk_noassertion(repo, lic_path)

    # Source-available / non-OSI -> E.
    if spdx in SOURCE_AVAILABLE_SPDX:
        perm = "source_available"
        relicense = _detect_relicense(repo, lic_path)
        raw = {"spdx_id": spdx, "permissiveness": perm,
               "relicense_36mo": relicense, "content_license": content_license}
        return Axis("E", raw, evidence=f"spdx {spdx} source-available/non-OSI -> E")

    if spdx.startswith(STRONG_COPYLEFT_SPDX_PREFIXES):
        relicense = _detect_relicense(repo, lic_path)
        raw = {"spdx_id": spdx, "permissiveness": "strong_network_copyleft",
               "relicense_36mo": relicense, "content_license": content_license}
        tier = "E" if relicense else "D"
        return Axis(tier, raw, evidence=f"spdx {spdx} strong copyleft relicense={relicense} -> {tier}")

    # Permissiveness from conditions/limitations.
    cond_info = _license_conditions(key) if key else None
    if cond_info is None:
        # Couldn't fetch the conditions map; fall back on spdx heuristic but never force A.
        return Axis.unknown("license_unparsed",
                            evidence=f"? spdx {spdx} but licenses/{key} unreadable")

    perm_class = _classify_permissiveness(cond_info["conditions"])

    # Benign attribution add-on (e.g. BSD-2-Clause-Patent) bumps permissive -> B.
    if perm_class == "permissive" and spdx in ("BSD-2-Clause-Patent",):
        perm_class = "permissive_clause_addon"

    relicense = _detect_relicense(repo, lic_path)
    tier = PERMISSIVENESS_TIER.get(perm_class, "A")
    if relicense:
        tier = "E"  # detected permissive->copyleft/source-available transition

    raw = {
        "spdx_id": spdx,
        "permissiveness": perm_class,
        "relicense_36mo": relicense,
        "content_license": content_license,
    }
    return Axis(tier, raw,
                evidence=f"spdx {spdx} perm={perm_class} relicense={relicense} -> {tier}")


# Iconic license-template fragments for high-confidence NOASSERTION disambiguation.
# GitHub's licensee sometimes fails when a LICENSE file appends trailing notices
# (e.g. third-party attribution) that push the text outside the template-match
# tolerance. These fragments are the *unambiguous* paragraphs of each license.
MIT_FRAGMENTS = [
    "permission is hereby granted, free of charge, to any person obtaining a copy",
    "the above copyright notice and this permission notice shall be included",
    'the software is provided "as is"',
]

APACHE2_FRAGMENTS = [
    "licensed under the apache license, version 2.0",
    "http://www.apache.org/licenses/license-2.0",
]

BSD3_FRAGMENTS = [
    "redistribution and use in source and binary forms",
    "with or without modification",
    "the name of the copyright holder",
]


def _matches_mit_template(text: str) -> bool:
    """Check if text contains the iconic MIT license paragraphs.
    Tolerant of trailing addenda (third-party notices, etc.) that confuse
    GitHub's licensee."""
    return sum(1 for f in MIT_FRAGMENTS if f in text) >= 2


def _matches_apache2_template(text: str) -> bool:
    return sum(1 for f in APACHE2_FRAGMENTS if f in text) >= 1


def _matches_bsd3_template(text: str) -> bool:
    return sum(1 for f in BSD3_FRAGMENTS if f in text) >= 2


def _risk_noassertion(repo: RepoData, lic_path: str | None) -> Axis:
    """NOASSERTION: read the LICENSE blob and pattern-match SSPL/BSL/EULA vs OSI."""
    blob = _fetch_license_blob(repo, lic_path)
    if blob is None:
        return Axis.unknown("license_unparsed",
                            evidence="? NOASSERTION & LICENSE blob unreadable")
    low = blob.lower()
    if any(k in low for k in ("server side public license", "sspl")):
        return Axis("E", {"spdx_id": "NOASSERTION", "permissiveness": "source_available",
                          "relicense_36mo": False, "content_license": None},
                    evidence="NOASSERTION blob matches SSPL -> E")
    if "business source license" in low or "bsl" in low and "licensed work" in low:
        return Axis("E", {"spdx_id": "NOASSERTION", "permissiveness": "source_available",
                          "relicense_36mo": False, "content_license": None},
                    evidence="NOASSERTION blob matches BSL -> E")
    if "elastic license" in low:
        return Axis("E", {"spdx_id": "NOASSERTION", "permissiveness": "source_available",
                          "relicense_36mo": False, "content_license": None},
                    evidence="NOASSERTION blob matches Elastic License -> E")
    # A NOASSERTION blob is NOT a verifiable permissive verdict. Even a
    # high-confidence OSI template hit can be a composite file: the preamble may
    # grant AGPL/commercial (Mattermost's LICENSE.txt) or split CE/EE terms
    # (Rocket.Chat's LICENSE) while embedding the OSI text as a sub-license or
    # appendix. Promoting that to A silently understates the real restrictions.
    # Rubric §2.6: OSI-looking NOASSERTION -> ? (license_unparsed) + caveats bullet.
    if _matches_mit_template(low) or _matches_apache2_template(low) or _matches_bsd3_template(low):
        return Axis.unknown(
            "license_unparsed",
            evidence="? NOASSERTION blob contains an OSI template but the file may be "
                     "composite/multi-licensed (manual review)")
    # Fallback: looks like OSI but template match was inconclusive -> ? for human review.
    if any(k in low for k in ("mit license", "apache license", "bsd ", "gnu general public",
                              "mozilla public license", "isc license")):
        return Axis.unknown("license_unparsed",
                            evidence="? NOASSERTION blob looks OSI but template match inconclusive (manual review)")
    return Axis.unknown("license_unparsed",
                        evidence="? NOASSERTION blob unclassifiable (manual review)")


def _is_license_filename(name: str) -> bool:
    """Does this filename mean "the license text lives here"?

    Has to accept the real spellings — `LICENSE`, `COPYING`, `LICENSE.md`,
    `LICENSE-APACHE`, `LICENSE-2.0.txt` — while rejecting files that merely *mention*
    licensing: `LICENSING.md` is a policy doc, and `license_test.go` and `LICENSE.py`
    are source. A single regex kept letting those two through, because the variant
    suffix that allows `-APACHE` also allows `_test.go`, so the extension is checked
    separately against an allow-list instead.
    """
    low = (name or "").lower()
    base, _, ext = low.rpartition(".")
    if not base:            # no dot at all: rpartition puts everything in `ext`
        base, ext = ext, ""
    # A version fragment like the `0` of `license-2.0` is not an extension.
    if ext.isdigit():
        base, ext = low, ""
    if ext not in LICENSE_TEXT_EXTS:
        return False
    # `-`/`_` separate a variant (LICENSE-MIT); a bare suffix (LICENSING) does not count.
    head = re.split(r"[-_]", base, maxsplit=1)[0]
    return head in LICENSE_BASE_NAMES


def _find_license_path(repo: RepoData) -> str | None:
    """Locate a license file that GitHub's own detector did not classify.

    Only called after `repos/{full}/license` 404s, so the cost is paid on the handful of
    repos that need it (33 of 615 pages at the time this was written), not on every scan.
    Checks the repo root first, then the small set of directories projects actually use;
    `apache/poi` is the case that motivated this — Apache-2.0 at `legal/LICENSE`.
    Returns the path of the first match, or None when the repo really has no license.
    """
    def first_license_in(dir_path: str, *, dedicated: bool = False) -> str | None:
        suffix = f"/{urllib.parse.quote(dir_path)}" if dir_path else ""
        res = gh_api(f"repos/{repo.full}/contents{suffix}")
        if not res.ok or not isinstance(res.json, list):
            return None
        for entry in res.json:
            if entry.get("type") != "file":
                continue
            name = entry.get("name") or ""
            # Inside a directory that exists to hold licenses, the REUSE convention names
            # each file after its SPDX id — cockpit-project/cockpit keeps
            # `LICENSES/LGPL-2.1-or-later.txt`. The filename test would reject those, so
            # the directory's own intent is what qualifies them.
            if dedicated and name.lower().endswith((".txt", ".md")):
                return entry.get("path")
            if _is_license_filename(name):
                return entry.get("path")
        return None

    hit = first_license_in("")
    if hit:
        return hit, "file"
    for d in LICENSE_SEARCH_DIRS:
        dedicated = d.lower() in LICENSE_DEDICATED_DIRS
        hit = first_license_in(d, dedicated=dedicated)
        if hit:
            # A REUSE `LICENSES/` tree lists every license appearing anywhere in the repo,
            # bundled dependencies included, so whichever file sorts first says nothing
            # about the project's own terms — cockpit declares LGPL-2.1-or-later and the
            # first entry is `BSD-3-Clause.txt`. Classifying from it would be a coin flip,
            # and a bundled `SSPL-1.0.txt` would produce a confident, wrong E.
            return hit, ("dedicated_dir" if dedicated and _has_spdx_named_files(hit) else "file")
    return None, None


def _has_spdx_named_files(path: str) -> bool:
    """Is this a REUSE-style per-SPDX file rather than a plain `legal/LICENSE`?"""
    name = path.rsplit("/", 1)[-1]
    return not _is_license_filename(name)


def _fetch_license_blob(repo: RepoData, lic_path: str | None) -> str | None:
    path = lic_path or "LICENSE"
    res = gh_api(f"repos/{repo.full}/contents/{urllib.parse.quote(path)}")
    if res.ok and isinstance(res.json, dict) and res.json.get("content"):
        import base64
        try:
            return base64.b64decode(res.json["content"]).decode("utf-8", "replace")
        except (ValueError, TypeError):
            return None
    return None


def _detect_relicense(repo: RepoData, lic_path: str | None) -> bool:
    """Relicense flag: permissive->copyleft/NOASSERTION transition in trailing 36mo.

    Resolves the real LICENSE filename first (spec §2.6 fix), then checks commit
    history on that exact path; for >1 commit diffs the two newest blobs' SPDX class.
    Best-effort: any failure returns False (never crashes, never false-positives blind).
    """
    if not lic_path:
        return False
    res = gh_api(f"repos/{repo.full}/commits?path={urllib.parse.quote(lic_path)}&per_page=100")
    if not res.ok or not isinstance(res.json, list) or len(res.json) <= 1:
        return False
    # Only consider commits within the 36mo window.
    recent = []
    for c in res.json:
        d = parse_iso(((c.get("commit") or {}).get("committer") or {}).get("date"))
        if d and (repo.now - d).days <= RELICENSE_WINDOW_DAYS:
            recent.append((d, c.get("sha")))
    if len(recent) < 1:
        return False
    # Diff the two newest blobs' permissiveness class (newest vs the one before it).
    if len(res.json) >= 2:
        new_sha = res.json[0].get("sha")
        old_sha = res.json[1].get("sha")
        new_class = _blob_perm_class(repo, lic_path, new_sha)
        old_class = _blob_perm_class(repo, lic_path, old_sha)
        if new_class and old_class:
            # permissive -> (copyleft/source-available) within window = relicense.
            permissive = {"permissive", "permissive_clause_addon"}
            if old_class in permissive and new_class not in permissive and recent:
                return True
            # also catch -> source_available
            if new_class == "source_available" and old_class != "source_available" and recent:
                return True
    return False


def _blob_perm_class(repo: RepoData, path: str, sha: str | None) -> str | None:
    if not sha:
        return None
    res = gh_api(f"repos/{repo.full}/contents/{urllib.parse.quote(path)}?ref={sha}")
    if not res.ok or not isinstance(res.json, dict) or not res.json.get("content"):
        return None
    import base64
    try:
        text = base64.b64decode(res.json["content"]).decode("utf-8", "replace").lower()
    except (ValueError, TypeError):
        return None
    if any(k in text for k in ("server side public license", "business source license",
                               "elastic license")):
        return "source_available"
    if "gnu affero" in text or "affero general public" in text:
        return "strong_network_copyleft"
    if "gnu lesser general public" in text:
        return "weak_file_copyleft"
    if "gnu general public" in text:
        return "strong_network_copyleft"
    if "mozilla public license" in text:
        return "weak_file_copyleft"
    if any(k in text for k in ("mit license", "apache license", "bsd ", "isc license",
                               "permission is hereby granted")):
        return "permissive"
    return None


# ---------------------------------------------------------------------------
# Aggregate (spec §3)
# ---------------------------------------------------------------------------

OVERALL_BANDS = [(3.5, "A"), (2.5, "B"), (1.5, "C"), (0.5, "D")]  # else E


def _overall_letter(mean: float) -> str:
    for floor, letter in OVERALL_BANDS:
        if mean >= floor:
            return letter
    return "E"


def aggregate(axes: dict[str, Axis]) -> dict:
    scored = {k: a for k, a in axes.items()
              if isinstance(a, Axis) and a.grade in GRADE_POINTS}
    n = len(scored)
    # Denominator = axes this artifact type can be asked about at all. An N/A axis is
    # removed from the question, not left unanswered, so a skill-pack with all five of
    # its meaningful axes measured reads "5/5" rather than a deceptively thin "5/6".
    applicable = sum(1 for k, a in axes.items()
                     if isinstance(a, Axis) and a.grade != Axis.NOT_APPLICABLE)
    if n < 3:
        return {"overall": "?", "overall_score": None, "scored_axes": n,
                "applicable_axes": applicable, "capped": False, "cap_reason": None}
    mean = sum(GRADE_POINTS[a.grade] for a in scored.values()) / n
    overall = _overall_letter(mean)

    # Risk/License CAP (spec §3.3): only when risk_license tier == E AND a genuine
    # "cannot legally embed" case; skill-packs EXEMPT.
    capped = False
    cap_reason = None
    rl = axes.get("risk_license")
    if rl is not None and rl.grade == "E":
        perm = rl.raw.get("permissiveness")
        spdx = rl.raw.get("spdx_id")
        legal_block = perm == "source_available" or spdx in ("NONE", "NOASSERTION") \
            or spdx in SOURCE_AVAILABLE_SPDX
        is_skillpack = axes["_meta_type"] == "skill-pack" if "_meta_type" in axes else False
        if legal_block and not is_skillpack:
            if GRADE_POINTS[overall] > GRADE_POINTS["D"]:
                overall = "D"
            capped = True
            cap_reason = f"source-available/no-license: {spdx}"

    return {"overall": overall, "overall_score": round(mean, 2),
            "scored_axes": n, "applicable_axes": applicable,
            "capped": capped, "cap_reason": cap_reason}


# ---------------------------------------------------------------------------
# Carve-out resolution that needs cross-axis info
# ---------------------------------------------------------------------------

def apply_governance_solo_carveout(axes: dict[str, Axis]) -> None:
    """stable_solo: lift governance D->C when active==1, low churn, maintenance not D/E."""
    gov = axes.get("governance")
    maint = axes.get("maintenance")
    if gov is None or gov.grade != "D":
        return
    if not gov.raw.pop("_solo_candidate", False):
        gov.raw.pop("_solo_candidate", None)
        return
    if maint is not None and maint.grade not in ("D", "E", "?"):
        gov.grade = "C"
        gov.raw["carve_out"] = "stable_solo"
        gov.evidence += " | stable_solo carve-out -> C"


# ---------------------------------------------------------------------------
# Number formatting
# ---------------------------------------------------------------------------

def _round(x, ndigits=0):
    if x is None:
        return None
    if ndigits == 0:
        return int(round(x))
    return round(x, ndigits)


def _median(xs: list[float]) -> float:
    s = sorted(xs)
    n = len(s)
    if n == 0:
        return 0.0
    mid = n // 2
    if n % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2.0


# ---------------------------------------------------------------------------
# YAML emission (spec §5.2) — hand-rolled, deterministic key order.
# ---------------------------------------------------------------------------

AXIS_ORDER = ["maintenance", "responsiveness", "adoption", "longevity",
              "governance", "risk_license"]
RAW_KEY_ORDER = {
    "maintenance": ["archived", "last_commit_age_days", "active_weeks_13", "carve_out"],
    "responsiveness": ["median_ttfr_hours", "qualifying_issues", "band", "window_offset_days", "source", "inferred"],
    # Registry path, then the §2.3b install-signal path. Every field that can decide the
    # grade must be listed: emission filters raw to these keys, so a measurement missing
    # here is written nowhere and the grade becomes unauditable — ollama/dbeaver/valkey
    # each landed "A" with nothing but `registry: null` on the page to show for it.
    "adoption": ["registry", "canonical_package", "package_link", "dependent_repos_count",
                 "downloads_last_month", "graph_tier", "volume_tier",
                 "cross_check_divergence",
                 "homebrew_installs_90d", "homebrew_tier",
                 "release_downloads", "release_assets", "release_tier",
                 "docker_pulls", "docker_image", "docker_tier",
                 "signal_basis", "tier_source", "archived"],
    "longevity": ["repo_age_days", "last_commit_age_days", "cohort"],
    "governance": ["active_maintainers_12mo", "top1_share", "top3_share",
                   "window_source", "carve_out"],
    "risk_license": ["spdx_id", "permissiveness", "relicense_36mo", "content_license"],
}


def _yaml_scalar(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v) if isinstance(v, float) else str(v)
    s = str(v)
    # Quote anything that would mis-parse as a YAML indicator: the unknown grade "?"
    # (explicit-key indicator), flow/comment chars, reserved words, or number-leading
    # strings that aren't plain identifiers.
    needs_quote = (
        s == ""
        or s in ("?", "N/A", "null", "true", "false", "~", "-", ">", "|", "*", "&", "!", "%", "@", "`")
        or s[0] in "?-:#[]{},&*!|>%@`\"'"
        or re.search(r"[:#\[\]{}]", s)
        or (re.match(r"^[\d.+-]", s) and not re.match(r"^[\w./@+-]+$", s))
    )
    if needs_quote:
        return '"' + s.replace('"', '\\"') + '"'
    return s


def emit_health_yaml(agg: dict, axes: dict[str, Axis], computed_at: str,
                     needs_human_review: bool) -> str:
    lines = ["health:"]
    lines.append(f"  schema: {SCHEMA_VERSION}")
    lines.append(f"  computed_at: {computed_at}")
    lines.append(f"  overall: {_yaml_scalar(agg['overall'])}")
    lines.append(f"  overall_score: {_yaml_scalar(agg['overall_score'])}")
    lines.append(f"  scored_axes: {agg['scored_axes']}")
    lines.append(f"  applicable_axes: {agg.get('applicable_axes', 6)}")
    lines.append(f"  capped: {_yaml_scalar(agg['capped'])}")
    lines.append(f"  cap_reason: {_yaml_scalar(agg['cap_reason'])}")
    lines.append(f"  needs_human_review: {_yaml_scalar(needs_human_review)}")
    lines.append("  axes:")
    for name in AXIS_ORDER:
        ax = axes[name]
        lines.append(f"    {name}:")
        lines.append(f"      grade: {_yaml_scalar(ax.grade)}")
        if ax.grade in ("?", Axis.NOT_APPLICABLE):
            # Unscored axes carry no raw block; the reason lives in unknowns/not_applicable.
            lines.append("      raw: {}")
            continue
        lines.append("      raw:")
        for k in RAW_KEY_ORDER[name]:
            if k not in ax.raw:
                continue
            lines.append(f"        {k}: {_yaml_scalar(ax.raw[k])}")
    unknowns = {name: axes[name].reason for name in AXIS_ORDER if axes[name].grade == "?"}
    if unknowns:
        lines.append("  unknowns:")
        for name, reason in unknowns.items():
            lines.append(f"    {name}: {{ reason: {reason} }}")
    na = {name: axes[name].reason for name in AXIS_ORDER
          if axes[name].grade == Axis.NOT_APPLICABLE}
    if na:
        lines.append("  not_applicable:")
        for name, reason in na.items():
            lines.append(f"    {name}: {{ reason: {reason} }}")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def score_repo(owner: str, name: str, ptype: str,
               declared_license: str | None = None) -> tuple[dict, dict[str, Axis], str, bool]:
    now = now_utc()
    computed_at = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    repo = RepoData(owner, name, ptype, now, declared_license)

    # Serial axis computation (spec §4.2: serial + backoff for stats/*).
    axes: dict[str, Axis] = {}
    axes["maintenance"] = _safe(axis_maintenance, repo, "maintenance", "recency_unreadable")
    axes["responsiveness"] = _safe(axis_responsiveness, repo, "responsiveness", "no_traffic")
    axes["adoption"] = _safe(axis_adoption, repo, "adoption", "registry_no_counts")
    axes["longevity"] = _safe(axis_longevity, repo, "longevity", "not_found")
    axes["governance"] = _safe(axis_governance, repo, "governance", "empty_or_gated")
    axes["risk_license"] = _safe(axis_risk_license, repo, "risk_license", "repo_unreachable")

    # Cross-axis carve-out.
    apply_governance_solo_carveout(axes)

    # needs_human_review from adoption A/B cross-check divergence.
    needs_review = getattr(axes["adoption"], "needs_human_review", False)

    # Aggregate (CAP needs the type via a sentinel key to know skill-pack exemption).
    agg = aggregate(_with_meta_type(axes, ptype))

    return agg, axes, computed_at, needs_review


def _with_meta_type(axes: dict[str, Axis], ptype: str) -> dict:
    out = dict(axes)
    out["_meta_type"] = ptype
    return out


def _safe(fn, repo: RepoData, axis_name: str, default_reason: str) -> Axis:
    """Run an axis function; any uncaught exception degrades to ? (never crash)."""
    try:
        return fn(repo)
    except Exception as e:  # noqa: BLE001 — graceful degradation is the contract
        return Axis.unknown(default_reason,
                            evidence=f"? {axis_name} raised {type(e).__name__}: {e}")


# Note: aggregate() reads axes['_meta_type'] only for the skill-pack CAP exemption;
# AXIS_ORDER iteration ignores it, so emission is unaffected.


# ---------------------------------------------------------------------------
# --write: splice the health: block into a page's frontmatter
# ---------------------------------------------------------------------------

def splice_health_block(text: str, health_block: str) -> str:
    """Replace an existing top-level `health:` block in frontmatter, or append one.

    Operates only inside the YAML frontmatter (between the first two '---' lines).
    """
    if not text.startswith("---"):
        raise ValueError("page has no frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("unterminated frontmatter")
    fm = text[3:end]  # without leading ---\n
    fm_lines = fm.split("\n")

    # Find an existing top-level `health:` key and its (indented) block extent.
    start_i = None
    for i, ln in enumerate(fm_lines):
        if re.match(r"^health:\s*$", ln) or re.match(r"^health:\s", ln):
            start_i = i
            break
    block_lines = health_block.rstrip("\n").split("\n")
    if start_i is not None:
        # Remove the old block: this line + all subsequent indented lines.
        j = start_i + 1
        while j < len(fm_lines) and (fm_lines[j].startswith(("  ", "\t")) or fm_lines[j].strip() == ""):
            # stop if we hit a new top-level key
            if fm_lines[j].strip() and not fm_lines[j].startswith((" ", "\t")):
                break
            j += 1
        new_fm_lines = fm_lines[:start_i] + block_lines + fm_lines[j:]
    else:
        # Append before the closing --- (strip trailing blank lines first).
        trimmed = fm_lines[:]
        while trimmed and trimmed[-1].strip() == "":
            trimmed.pop()
        new_fm_lines = trimmed + block_lines
    new_fm = "\n".join(new_fm_lines)
    return "---" + new_fm + text[end:]


def extract_grades(text: str) -> dict[str, str]:
    """Read {axis: grade, 'overall': grade} from a page's existing health: block.

    Empty dict when the page has no parseable block (fresh page). Used by --write to
    report grade changes so the operator reconciles the prose `## Health & viability`
    section — the radar is machine-refreshed but that section is hand-written, and they
    drift silently otherwise.
    """
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    m = re.search(r"(?ms)^health:\n(.*?)(?=^\S|\Z)", text[3:end])
    if not m:
        return {}
    block = m.group(0)
    out: dict[str, str] = {}
    om = re.search(r"(?m)^  overall:\s*(\S+)", block)
    if om:
        out["overall"] = om.group(1).strip("\"'")
    for am in re.finditer(r"(?m)^    (\w+):\n      grade:\s*(\S+)", block):
        out[am.group(1)] = am.group(2).strip("\"'")
    return out


def grade_changes(old: dict[str, str], new: dict[str, str]) -> list[tuple[str, str, str]]:
    """Return [(key, old_grade, new_grade)] for grades that moved (keys present in both)."""
    return [(k, old[k], new[k]) for k in new if k in old and old[k] != new[k]]


def write_to_pages(en_page: Path, health_block: str) -> list[Path]:
    written = []
    zh_page = en_page.with_name(en_page.name[: -len(".md")] + ".zh.md")
    for p in (en_page, zh_page):
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        new_text = splice_health_block(text, health_block)
        p.write_text(new_text, encoding="utf-8")
        written.append(p)
    return written


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def resolve_target(args) -> tuple[str, str, str, str | None, Path | None]:
    """Return (owner, name, type, declared_license, page_path_or_None)."""
    if args.page:
        page = Path(args.page).resolve()
        if not page.exists():
            sys.exit(f"page not found: {page}")
        fm = parse_frontmatter(page.read_text(encoding="utf-8"))
        if not fm:
            sys.exit(f"page has no parseable frontmatter: {page}")
        repo_url = fm.get("repo", "")
        ptype = fm.get("type", "")
        declared_license = fm.get("license")
        on = repo_url_to_owner_name(repo_url)
        if not on:
            sys.exit(f"could not parse owner/name from repo: {repo_url}")
        owner, name = on.split("/", 1)
        return owner, name, ptype, declared_license, page
    if args.repo:
        if "/" not in args.repo:
            sys.exit("--repo must be owner/name")
        owner, name = args.repo.split("/", 1)
        if not args.type:
            sys.exit("--type is required with --repo")
        return owner, name, args.type, None, None
    sys.exit("provide --repo owner/name --type <t>  OR  --page <path>.md")


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic OSS-health scorer (oss-atlas).")
    ap.add_argument("--repo", help="owner/name")
    ap.add_argument("--type", help="project type (with --repo)")
    ap.add_argument("--page", help="path to a category page (.md); reads repo:/type: from frontmatter")
    ap.add_argument("--write", action="store_true",
                    help="splice the health: block into the page's .md and .zh.md")
    ap.add_argument("--evidence", action="store_true",
                    help="also print a per-axis evidence note to stderr")
    args = ap.parse_args()

    owner, name, ptype, declared_license, page = resolve_target(args)
    agg, axes, computed_at, needs_review = score_repo(owner, name, ptype, declared_license)
    block = emit_health_yaml(agg, axes, computed_at, needs_review)

    if args.write:
        if page is None:
            sys.exit("--write requires --page")
        old_grades = extract_grades(page.read_text(encoding="utf-8"))
        written = write_to_pages(page, block)
        for p in written:
            print(f"wrote health: block to {p}", file=sys.stderr)
        new_grades = {n: axes[n].grade for n in AXIS_ORDER}
        new_grades["overall"] = agg["overall"]
        changes = grade_changes(old_grades, new_grades)
        if changes:
            print("grade changes vs previous block:", file=sys.stderr)
            for key, old_g, new_g in changes:
                print(f"  {key}: {old_g} -> {new_g}", file=sys.stderr)
            print("reconcile prose: re-read '## Health & viability' (+ zh sibling) — and the"
                  " 'When NOT to use' abandonment flag if maintenance/overall dropped.",
                  file=sys.stderr)
        elif old_grades:
            print("grades unchanged vs previous block", file=sys.stderr)
    else:
        sys.stdout.write(block)

    if args.evidence:
        print("\n# evidence", file=sys.stderr)
        for n in AXIS_ORDER:
            print(f"#   {n}: {axes[n].evidence}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
