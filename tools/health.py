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
}
# dependent_repos_count -> graph_tier (A/B/C/D/E). Go importers map to this same column.
ADOPTION_GRAPH_ANCHORS = (10_000, 1_000, 100)  # A, B, C floors; D = 1..99; E = 0
ADOPTION_NO_PACKAGE_TYPES = {"app", "skill-pack", "service", "model"}
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
    return GhResult(status, body)


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


def http_get_json(url: str, *, timeout: int = 25) -> tuple[int, object | None]:
    """GET a URL with urllib; return (status, parsed_json_or_None). Never raises."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "replace")
            try:
                return resp.status, json.loads(body)
            except (ValueError, json.JSONDecodeError):
                return resp.status, None
    except urllib.error.HTTPError as e:
        return e.code, None
    except (urllib.error.URLError, OSError, ValueError):
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

    Returns None ("?") if registry has no anchors (Maven/Go) or downloads is None.
    """
    if downloads is None:
        return None
    anchors = ADOPTION_VOLUME_ANCHORS.get(registry)
    if anchors is None:
        return None  # Maven/Go: no download counts -> volume "?"
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
    """One axis result: grade (A-E or '?'), raw measured values, optional ? reason."""

    def __init__(self, grade: str, raw: dict, reason: str | None = None,
                 evidence: str = ""):
        self.grade = grade
        self.raw = raw
        self.reason = reason          # set iff grade == "?"
        self.evidence = evidence      # one-line human note for the report

    @classmethod
    def unknown(cls, reason: str, raw: dict | None = None, evidence: str = "") -> "Axis":
        return cls("?", raw or {}, reason=reason, evidence=evidence or f"? ({reason})")


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


def _name_fuzzy_match(pkg_name: str, repo_name: str) -> bool:
    """Loose match: normalize separators, check containment either way."""
    norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())
    p, r = norm(pkg_name), norm(repo_name)
    if not p or not r:
        return False
    return p == r or p in r or r in p


def _select_canonical(candidates: list[dict], repo_name: str) -> dict | None:
    """Canonical = name-fuzzy-match + max downloads, dropping noise (spec §2.3).

    Drop entries with downloads < 1000 OR rank == null, EXCEPT when all candidates
    have rank == null and one has high downloads (crewai case) -> fall back to max-dl.
    """
    if not candidates:
        return None
    named = [c for c in candidates if _name_fuzzy_match(c.get("name", ""), repo_name)]
    pool = named or candidates

    def dl(c):
        return c.get("downloads") or 0

    clean = [c for c in pool if dl(c) >= 1000 and c.get("rank") is not None]
    if clean:
        return max(clean, key=dl)
    # All rank==null (crewai case): fall back to the max-downloads candidate if it has real volume.
    all_rank_null = all(c.get("rank") is None for c in pool)
    if all_rank_null:
        best = max(pool, key=dl)
        if dl(best) >= 1000:
            return best
    # Otherwise: still take best-by-downloads if any clears 1000 (avoid false ?).
    over = [c for c in pool if dl(c) >= 1000]
    if over:
        return max(over, key=dl)
    return None


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


def axis_adoption(repo: RepoData) -> Axis:
    url = ECOSYSTE_LOOKUP + urllib.parse.quote(
        f"https://github.com/{repo.full}", safe="")
    status, data = http_get_json(url)
    archived = bool(repo.core.json.get("archived")) if isinstance(repo.core.json, dict) else False

    if status == 0 or status >= 400:
        return Axis.unknown("registry_lookup_failed", evidence=f"? ecosyste.ms lookup HTTP {status}")

    candidates = data if isinstance(data, list) else []
    canonical = _select_canonical(candidates, repo.name)

    if canonical is None:
        # No package cleared the noise filter.
        if repo.type in ADOPTION_NO_PACKAGE_TYPES:
            return Axis.unknown("no_package_structural",
                                evidence=f"type {repo.type} & no canonical package -> no_package_structural")
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
    if archived:
        raw["archived"] = True
    ax = Axis(tier, raw,
              evidence=f"registry={registry} pkg={pkg_name} dep_repos={dep_repos} "
                       f"dl={downloads} graph={graph_tier} vol={volume_tier} -> {tier}")
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
        # 404 on the LICENSE endpoint = NONE (all-rights-reserved). Distinguish repo 404.
        if not repo.core.ok:
            return Axis.unknown("repo_unreachable", evidence=f"? repo HTTP {repo.core.status}")
        return Axis("E", {"spdx_id": "NONE", "permissiveness": "source_available",
                          "relicense_36mo": False, "content_license": None},
                    evidence="no LICENSE (404) -> NONE -> E")
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
    if n < 3:
        return {"overall": "?", "overall_score": None, "scored_axes": n,
                "capped": False, "cap_reason": None}
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
            "scored_axes": n, "capped": capped, "cap_reason": cap_reason}


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
    "adoption": ["registry", "canonical_package", "dependent_repos_count",
                 "downloads_last_month", "graph_tier", "volume_tier",
                 "cross_check_divergence", "archived"],
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
        or s in ("?", "null", "true", "false", "~", "-", ">", "|", "*", "&", "!", "%", "@", "`")
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
    lines.append(f"  capped: {_yaml_scalar(agg['capped'])}")
    lines.append(f"  cap_reason: {_yaml_scalar(agg['cap_reason'])}")
    lines.append(f"  needs_human_review: {_yaml_scalar(needs_human_review)}")
    lines.append("  axes:")
    for name in AXIS_ORDER:
        ax = axes[name]
        lines.append(f"    {name}:")
        lines.append(f"      grade: {_yaml_scalar(ax.grade)}")
        if ax.grade == "?":
            # ? axes carry no raw block; reason lives in unknowns.
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
