#!/usr/bin/env python3
"""Structural linter for oss-atlas.

This repo has no runtime logic, so it has no unit tests. THIS LINTER IS THE TEST:
it enforces the entry schema (tools/schema.md) so the index stays machine-navigable
for the coding agents that read it.

Model:
  - Bilingual pair: each project is <slug>.md (English, canonical) + <slug>.zh.md.
  - Recursive taxonomy: categories/ is a tree of arbitrary depth. A directory with an
    INDEX.md is a *category node*; it may hold project pages AND/OR child sub-categories.
    Routing splits by language: INDEX.md (EN) + INDEX.zh.md (ZH) at every node and the root.
  - type-adaptive sections: frontmatter `type` decides which body sections are required.
    skill-pack pages omit Tech stack / Dependencies / Ops difficulty; `Health & viability` and
    `Caveats` are required for EVERY type.

Checks (ERROR = non-zero exit; WARNING = printed, exit still 0):
  - each page: required frontmatter keys + types, slug==base filename, category==parent dir,
    type in the allowed set, required body sections for its type+language, sibling parity
  - each page starts with an H1 title (`# <name>`) -> ERROR if absent
  - bilingual pair frontmatter is identical (facts are language-neutral) -> ERROR on any drift
  - skill-pack pages must OMIT Tech stack / Dependencies / Ops difficulty (not pad them) -> ERROR if present
  - last_verified parses; staleness > STALE_DAYS -> WARNING; a date ahead of UTC today -> ERROR
  - dates are compared against UTC today, never the runner's local clock (CI is UTC; a machine
    ahead of UTC must not be able to write a page that the gate then calls "in the future").
    See today_utc().
  - every page has a health radar frontmatter block + card embed -> ERROR if absent/malformed
  - health computed_at parses; staleness > STALE_DAYS -> WARNING (time-decay axes rot even
    when upstream is unchanged — a quiet repo decays while its SHA never moves)
  - every page has an upstream snapshot for cheap stale checks -> ERROR if absent/malformed
  - page Comparison tables include an explicit Our verdict / 我们的评价 column -> ERROR if absent
  - every page: a Caveats ledger section (## Caveats (unverified) / ## 存疑（未验证）) -> ERROR if absent
  - optional Q&A / 快问快答: if present, non-empty, bilingual pair matches, sits after
    When to use and before How it works (or When NOT if that section is absent)
    -> ERROR on empty / one-sided / wrong position
    NOTE: the *decision* to write the section (schema §2: "required decision, optional section",
    recorded as `no leftover Q&A` in the change summary) is intentionally NOT gateable — absence
    here cannot distinguish a considered "none" from an agent that never looked.
  - prose-region [未验证]/[推断] density > PROSE_LABEL_MAX -> WARNING (converge into the Caveats section)
  - every directory under categories/ is a category node: must have INDEX.md + INDEX.zh.md
    (traversal is NOT gated on INDEX existence, so a dir missing its INDEX is reported, not skipped)
  - pages/sub-categories linked from their node INDEX; root INDEX links the top categories
  - recursive: sub-categories validated to any depth
  - leaf category with > MAX_FANOUT pages -> WARNING (self-balancing: split via refactor-index)
  - a flow spec whose 'phase' transitions land exactly on its lane changes -> WARNING
    (the label restates the handoff; flow_card.advisories)
  - internal relative links resolve
  - .zh.md bodies use fullwidth Chinese punctuation: ASCII , ; ! ? : ( ) " adjacent to a CJK char
    -> ERROR (frontmatter / code / links / URLs are exempt; facts stay language-neutral)
  - README.md / README.zh.md master listing stays in parity with the indexed pages
    (every EN page listed in README.md, every ZH page in README.zh.md) -> ERROR on drift
  - README/category INDEX project summary tables include Health / 健康度 -> ERROR if absent
  - How it works / 怎么用起来 (backbone user-story flow, SSOT flows/<stem>.json):
    absent -> ERROR when the page's last_verified >= OSS_ATLAS_FLOW_REQUIRED_FROM (new + re-synced
    pages are authored under the contract), otherwise one aggregate backfill WARNING;
    present -> ERROR on: wrong position (must sit between When to use and When NOT to use), no
    mechanism prose, missing/invalid spec, missing/stale card, card not embedded, generated
    step list drifting from the spec; a spec without a page section, or with no page -> ERROR

NOTE: this linter is a STRUCTURAL gate, not a semantic review. It cannot judge whether a
"When to use" is a real trigger scenario, whether a Comparison compares real substitutes, or whether
prose is accurate — those stay human/agent judgment (see tools/schema.md).

Pure stdlib. Usage:  python3 tools/lint.py [--root .]
Env: OSS_ATLAS_STALE_DAYS (default 90), OSS_ATLAS_MAX_FANOUT (default 12),
     OSS_ATLAS_PROSE_LABEL_MAX (default 3), OSS_ATLAS_REQUIRE_FLOW (default 0),
     OSS_ATLAS_FLOW_REQUIRED_FROM (default 2026-09-20)
"""
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from pathlib import Path

import flow_card
# Reuse the scorer's own name matcher rather than reimplementing it: the gate's whole
# point is to re-check what health.py wrote, and a second copy of the rule would drift
# from the one that produced the data. Import-only — health.py does no work at import.
from health import _match_quality

REQUIRED_KEYS = ["name", "slug", "repo", "category", "tags", "language", "license", "maturity", "last_verified", "type"]
ALLOWED_TYPES = {"tool", "library", "app", "framework", "service", "model", "skill-pack"}
CORE_EN = ["## When to use", "## When NOT to use", "## Comparison"]
EXTRA_EN = ["## Tech stack", "## Dependencies", "## Ops difficulty"]
HEALTH_EN = ["## Health & viability"]   # required for ALL types (incl. skill-pack)
CORE_ZH = ["## 何时使用", "## 何时不用", "## 横向对比"]
EXTRA_ZH = ["## 技术栈", "## 依赖", "## 运维难度"]
HEALTH_ZH = ["## 健康度与可持续性"]
NO_EXTRA_TYPES = {"skill-pack"}  # these omit Tech stack / Dependencies / Ops difficulty

INDEX_EN = "INDEX.md"
INDEX_ZH = "INDEX.zh.md"
ZH_SUFFIX = ".zh.md"
STALE_DAYS = int(os.environ.get("OSS_ATLAS_STALE_DAYS", "90"))
MAX_FANOUT = int(os.environ.get("OSS_ATLAS_MAX_FANOUT", "12"))
PROSE_LABEL_MAX = int(os.environ.get("OSS_ATLAS_PROSE_LABEL_MAX", "3"))
REQUIRE_FLOW = os.environ.get("OSS_ATLAS_REQUIRE_FLOW", "0") == "1"
# Pages verified on/after this date were authored under the How-it-works contract, so the section is
# required for them (add-project writes it; sync-entry bumps last_verified only after re-checking it).
# Older pages are the backfill backlog: one aggregate WARNING, not 1000 errors.
FLOW_REQUIRED_FROM = os.environ.get("OSS_ATLAS_FLOW_REQUIRED_FROM", "2026-09-20")
# A generator that has not read the upstream sources must say so with this marker instead of
# writing plausible prose over the hole: prose that nobody earned reads exactly like prose that
# somebody did, and no wording-based check can tell them apart after the fact. The marker gives the
# unresearched state a name, and an ERROR here means a page carrying one cannot merge. Evading it
# requires claiming research that did not happen, which is a different (and visible) problem.
UNRESEARCHED_MARKER = "<!-- oss-atlas:unresearched -->"


def today_utc() -> dt.date:
    """The date every freshness check compares against, in UTC.

    Not dt.date.today(): that reads the runner's local clock. CI runs in UTC while a developer
    8 hours ahead can write `last_verified: <local tomorrow>` after local midnight and pass
    locally, only to have CI reject it as "in the future" (observed 2026-09-22 on a page written
    at 00:05 UTC+8). Fixing the clock removes the environment-dependent verdict; facts elsewhere
    in the schema (upstream.pushed_at, health.computed_at) are UTC too, so this matches them.
    """
    return dt.datetime.now(dt.timezone.utc).date()


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
# Caveats ledger heading — tolerant prefix match (the parenthetical varies: (unverified)/（未验证）).
CAVEATS_RE_EN = re.compile(r"(?m)^##\s+Caveats\b")
CAVEATS_RE_ZH = re.compile(r"(?m)^##\s+存疑")
QA_RE_EN = re.compile(r"(?m)^##\s+Q&A\s*$")
QA_RE_ZH = re.compile(r"(?m)^##\s+快问快答\s*$")
# Health & viability is a labeled-judgment section (like Caveats) — exempt from the inline
# label-density count, so the density boundary ends at whichever of Health/Caveats comes first.
HEALTH_RE_EN = re.compile(r"(?m)^##\s+Health\s*&\s*viability\b")
HEALTH_RE_ZH = re.compile(r"(?m)^##\s+健康度与可持续性")
LABEL_RE = re.compile(r"\[未验证\]|\[推断\]")

# --- health radar block (frontmatter `health:`) -----------------------------
# A separate concern from the prose `## Health & viability` section above:
# `health:` is the machine SSOT for the 6-axis JoJo-style radar card.
# Computed by tools/health.py; the SVG is regenerated by tools/health_card.py.
# Health radar is required after the Phase 1 backfill; missing blocks are schema errors.
# "?" = measurement failed (may be our bug); "N/A" = the axis asks a question this
# artifact type cannot answer (a skill-pack is copied, never installed, so no install
# count exists anywhere). Both are unscored, but only "?" is a gap worth chasing, and
# only "N/A" is removed from the aggregate denominator.
GRADES = {"A", "B", "C", "D", "E", "?", "N/A"}
UNSCORED_GRADES = {"?", "N/A"}
HEALTH_AXES = ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]
# Every count an adoption E can legitimately rest on. An E asserts "measurably
# unadopted", which is a claim about a number — so at least one of these must be
# present and non-null. Without this gate a lookup that found nothing scores the
# same as a package with genuinely zero installs, and that failure mode shipped:
# 39 pages carried E purely because the scorer matched no package at all.
ADOPTION_COUNT_KEYS = ["dependent_repos_count", "downloads_last_month",
                       "homebrew_installs_90d", "release_downloads", "docker_pulls"]
UPSTREAM_KEYS = ["pushed_at", "default_branch", "default_branch_sha", "archived"]
# Chinese punctuation: ASCII , ; ! ? : adjacent to a CJK char in a .zh.md body should be the
# fullwidth form (，；！？：). Detection mirrors the normalizer: skip frontmatter, fenced/inline
# code, link targets, and URLs; flag only ASCII punctuation touching a CJK ideograph.
CJK_RANGE = "㐀-䶿一-鿿"
ZH_PUNCT_PROTECT = re.compile(r"`[^`]*`|\]\([^)]*\)|https?://\S+")
# ASCII punctuation that must be fullwidth when touching a CJK char: , ; ! ? : ( ) and "
_ZH_ASCII = r',;!?:()"'
ZH_PUNCT_HIT = re.compile(r"[" + CJK_RANGE + r"][" + _ZH_ASCII + r"]|[" + _ZH_ASCII + r"][" + CJK_RANGE + r"]")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.flow_missing: list[Path] = []   # pages still lacking How it works (backfill tally)
        self.flow_stems: set[str] = set()    # stems referenced by some page (orphan-spec check)

    def error(self, where: Path | str, msg: str) -> None:
        self.errors.append(f"ERROR  {where}: {msg}")

    def warn(self, where: Path | str, msg: str) -> None:
        self.warnings.append(f"WARN   {where}: {msg}")


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


def md_links(text: str) -> list[str]:
    return LINK_RE.findall(text)


def zh_punct_violations(text: str) -> int:
    """Count ASCII , ; ! ? : adjacent to a CJK char in a .zh.md body.

    Skips YAML frontmatter (facts, kept identical to the EN sibling), fenced code blocks,
    inline code, link targets, and URLs — the same regions the normalizer protects.
    """
    n = 0
    in_front = in_fence = False
    for i, line in enumerate(text.split("\n")):
        if i == 0 and line.strip() == "---":
            in_front = True
            continue
        if in_front:
            if line.strip() == "---":
                in_front = False
            continue
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        n += len(ZH_PUNCT_HIT.findall(ZH_PUNCT_PROTECT.sub("", line)))
    return n


def linked_targets(index_path: Path) -> set[Path]:
    if not index_path.exists():
        return set()
    return {
        (index_path.parent / l.split("#", 1)[0]).resolve()
        for l in md_links(index_path.read_text(encoding="utf-8"))
        if not l.startswith(("http://", "https://", "#", "mailto:"))
    }


def is_page(name: str) -> bool:
    return name.endswith(".md") and name not in (INDEX_EN, INDEX_ZH)


def base_slug(name: str) -> str:
    return name[: -len(ZH_SUFFIX)] if name.endswith(ZH_SUFFIX) else name[: -len(".md")]


def duplicate_slugs(root: Path) -> set[str]:
    counts: dict[str, int] = {}
    for page in (root / "categories").rglob("*.md"):
        if page.name.startswith("INDEX") or page.name.endswith(ZH_SUFFIX):
            continue
        counts[page.stem] = counts.get(page.stem, 0) + 1
    return {slug for slug, count in counts.items() if count > 1}


def health_card_stem(path: Path, root: Path, base: str, duplicate_bases: set[str]) -> str:
    if base not in duplicate_bases:
        return base
    try:
        rel_parent = path.parent.relative_to(root / "categories")
    except ValueError:
        return base
    return f"{'-'.join(rel_parent.parts)}-{base}"


def required_sections(ptype: str, zh: bool) -> list[str]:
    core = CORE_ZH if zh else CORE_EN
    extra = EXTRA_ZH if zh else EXTRA_EN
    health = HEALTH_ZH if zh else HEALTH_EN
    return core + health + ([] if ptype in NO_EXTRA_TYPES else extra)


def table_cells(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    cells: list[str] = []
    cur: list[str] = []
    escaped = False
    for ch in body:
        if ch == "|" and not escaped:
            cells.append("".join(cur).strip())
            cur = []
            continue
        cur.append(ch)
        escaped = (ch == "\\" and not escaped)
        if ch != "\\":
            escaped = False
    cells.append("".join(cur).strip())
    return cells


def normalized_frontmatter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    lines = [line.rstrip() for line in text[3:end].strip("\n").splitlines()]
    return "\n".join(lines)


def is_table_separator(line: str) -> bool:
    cells = table_cells(line)
    return bool(cells) and all(cell and set(cell) <= set("-: ") and cell.count("-") >= 3 for cell in cells)


def check_comparison_table(path: Path, text: str, zh: bool, rep: Report) -> None:
    heading = "## 横向对比" if zh else "## Comparison"
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() != heading:
            continue
        next_h2 = next((j for j in range(i + 1, len(lines)) if re.match(r"^##[ \t]+\S", lines[j])), len(lines))
        for j in range(i + 1, next_h2 - 1):
            header = lines[j].strip()
            if header.startswith("|") and header.endswith("|") and is_table_separator(lines[j + 1].strip()):
                cells = table_cells(header)
                required = "我们的评价" if zh else "Our verdict"
                if required not in cells:
                    rep.error(path, f"Comparison table must include '{required}' column")
                width = len(cells)
                sep_width = len(table_cells(lines[j + 1].strip()))
                if sep_width != width:
                    rep.error(path, f"Comparison table separator has {sep_width} columns, expected {width}")
                for row in lines[j + 2 : next_h2]:
                    row_s = row.strip()
                    if not (row_s.startswith("|") and row_s.endswith("|")):
                        break
                    row_width = len(table_cells(row_s))
                    if row_width != width:
                        rep.error(path, f"Comparison table row has {row_width} columns, expected {width}")
                return
        rep.error(path, f"{heading} must contain a Markdown table")
        return


def check_summary_health_columns(path: Path, rep: Report) -> None:
    """Project/option summary tables carry health as the index's machine verdict.

    Route-only tables such as Category/Route or schema documentation tables are intentionally out
    of scope; they do not summarize project choices.
    """
    zh = path.name.endswith(ZH_SUFFIX)
    required = "健康度" if zh else "Health"
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines[:-1]):
        header = line.strip()
        if not (header.startswith("|") and header.endswith("|") and is_table_separator(lines[i + 1])):
            continue
        cells = table_cells(header)
        if cells[:2] in (["Project", "Use when"], ["项目", "何时用"], ["Collection", "Use when"], ["合集", "何时用"],
                         ["Option", "Indexed"], ["选项", "是否收录"]):
            if required not in cells:
                rep.error(path, f"summary table must include '{required}' column")


def page_health_label(page_path: Path, zh: bool) -> str | None:
    """Render a page's `health:` frontmatter SSOT as its index label: `B (5/6)` / `B（5/6）`."""
    try:
        text = page_path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    overall = re.search(r"(?m)^\s+overall:\s*(\S+)\s*$", block)
    if not overall:
        return None
    axes = re.search(r"(?m)^\s+scored_axes:\s*(\d+)\s*$", block)
    if axes:
        # Denominator = applicable axes, not a hardcoded 6: an axis marked N/A is out of
        # the question for this artifact type, so counting it would understate coverage.
        app = re.search(r"(?m)^\s+applicable_axes:\s*(\d+)\s*$", block)
        denom = app.group(1) if app else "6"
        return f"{overall.group(1)} ({axes.group(1)}/{denom})" if not zh else f"{overall.group(1)}（{axes.group(1)}/{denom}）"
    return overall.group(1)


def health_parity_rows(path: Path, root: Path) -> list[tuple[int, str, str, Path]]:
    """Summary-table rows in an INDEX/README whose Health cell must equal the linked page's SSOT.

    A row qualifies when it carries a Health/健康度 column and links exactly ONE page of the
    table's language (EN tables read .md, ZH tables read .zh.md; the README lines carry both —
    the sibling is filtered by suffix). Composite rows (several pages) and 未收录 rows (no page)
    are skipped: there is no single SSOT to compare against.
    Returns (drifts, malformed): drifts are (line_no_1based, current_cell, expected, page_path)
    for every row whose Health cell differs from the linked page's SSOT; malformed are
    (line_no_1based, n_row_cells, n_header_cells, snippet) for rows whose column count does not
    match the header (a missing Health cell would otherwise silently re-align the projection).
    """
    zh = path.name.endswith(ZH_SUFFIX)
    required = "健康度" if zh else "Health"
    drifts: list[tuple[int, str, str, Path]] = []
    malformed: list[tuple[int, int, int, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines[:-1]):
        header = line.strip()
        if not (header.startswith("|") and header.endswith("|") and is_table_separator(lines[i + 1])):
            continue
        cells = table_cells(header)
        if required not in cells:
            continue
        hcol = cells.index(required)
        for j in range(i + 2, len(lines)):
            rs = lines[j].strip()
            if not (rs.startswith("|") and rs.endswith("|")):
                break
            rcells = table_cells(rs)
            if len(rcells) != len(cells):
                malformed.append((j + 1, len(rcells), len(cells), rs[:60]))
                continue
            pages: list[Path] = []
            for l in LINK_RE.findall(rs):
                if l.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                p = (path.parent / l.split("#", 1)[0]).resolve()
                try:
                    rel = p.relative_to(root)
                except ValueError:
                    continue
                if not str(rel).startswith("categories/") or not is_page(p.name):
                    continue
                if p.name.endswith(ZH_SUFFIX) != zh:
                    continue
                pages.append(p)
            uniq = list(dict.fromkeys(pages))
            if len(uniq) != 1:
                continue
            want = page_health_label(uniq[0], zh)
            if want is None or rcells[hcol] == want:
                continue
            drifts.append((j + 1, rcells[hcol], want, uniq[0]))
    return drifts, malformed


def adoption_raw(block: str) -> dict[str, str] | None:
    """Return the adoption axis's `raw:` mapping as {key: literal}, or None if absent.

    Values stay as their YAML literals (`null`, `1234`, `pypi.org`); callers decide
    what counts as a real number.
    """
    m = re.search(r"(?ms)^    adoption:\n(.*?)(?=^    \w|\Z)", block)
    if not m:
        return None
    return {k: v.strip() for k, v in re.findall(r"(?m)^\s{8}(\w+):\s*(.*)$", m.group(1))}


def check_adoption_evidence(path: Path, fmtext: str, block: str, rep: Report) -> None:
    """Two machine gates on the adoption axis, both closing shipped fail-open bugs.

    1. An `E` must rest on a real count. `E` asserts "measurably unadopted", which is a
       claim about a number; a lookup that found nothing is a different state (`?`).
       39 pages once carried `E` only because no package matched at all.
    2. A `canonical_package` must plausibly BE this repo. A by-name lookup once attached
       `crates.io/waza` (a reserved name owned by someone else) to `tw93/Waza` and
       `npmjs.org/d2` (DHIS2's library) to `d2lang/d2`, and an unmatched max-downloads
       fallback reported `digitalbanking` as jaeger's package. Re-checking the stored
       name against the repo offline catches the whole class without a network call.
    """
    raw = adoption_raw(block)
    if raw is None:
        return
    grade_m = re.search(r"(?ms)^    adoption:\n\s+grade:\s*(\S+)", block)
    grade = grade_m.group(1).strip("\"'") if grade_m else None

    if grade == "E":
        counts = {k: raw[k] for k in ADOPTION_COUNT_KEYS
                  if k in raw and re.fullmatch(r"\d+", raw[k])}
        if not counts:
            rep.error(path, "health: adoption 'E' carries no measured count — an E claims "
                            f"'measurably unadopted'; with none of {ADOPTION_COUNT_KEYS} "
                            "set to a number this is a failed measurement, which is '?'")

    if grade == "N/A":
        counts = {k: raw[k] for k in ADOPTION_COUNT_KEYS
                  if k in raw and re.fullmatch(r"\d+", raw[k])}
        if counts:
            rep.error(path, f"health: adoption 'N/A' contradicts its own evidence {counts} — "
                            "N/A claims no install event exists anywhere to count, so a page "
                            "carrying a real count must be graded, not excused")

    pkg = raw.get("canonical_package", "null")
    if pkg and pkg != "null":
        repo_m = re.search(r"(?m)^repo:\s*(\S+)\s*$", fmtext)
        slug = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)",
                        (repo_m.group(1) if repo_m else "").rstrip("/"))
        if slug:
            owner, name = slug.group(1), slug.group(2).removesuffix(".git")
            if _match_quality({"name": pkg.strip("\"'")}, owner, name) == 0:
                rep.error(path, f"health: adoption canonical_package '{pkg}' matches neither "
                                f"the repo name '{name}' nor the owner scope '{owner}' — a "
                                "package that cannot be shown to be this repo must not "
                                "supply its adoption grade")


def check_health_block(path: Path, text: str, base: str, zh: bool, root: Path, duplicate_bases: set[str], rep: Report, today: dt.date) -> None:
    """Validate a frontmatter `health:` radar block + its SVG card, if present.

    Validates shape (overall +
    6 axis grades in A–E/?), that the SVG card exists, and that it is embedded.
    Also warns when computed_at is older than STALE_DAYS: maintenance/longevity are
    functions of elapsed time, so grades rot even when the upstream repo is unchanged.
    """
    if not text.startswith("---"):
        return
    end = text.find("\n---", 3)
    if end == -1:
        return
    fmtext = text[3:end]
    if not re.search(r"(?m)^health:\s*$", fmtext):
        rep.error(path, "health: missing required frontmatter block")
        return
    block_m = re.search(r"(?ms)^health:\n(.*)\Z", fmtext)
    block = block_m.group(0) if block_m else ""

    computed = re.search(r"(?m)^\s{2}computed_at:\s*(\S+)\s*$", block)
    if not computed or not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", computed.group(1)):
        rep.error(path, "health: computed_at missing or not an ISO UTC timestamp")
    else:
        age = (today - dt.date.fromisoformat(computed.group(1)[:10])).days
        if age > STALE_DAYS:
            rep.warn(path, f"health: computed_at {computed.group(1)[:10]} is {age}d old (> {STALE_DAYS}); grades decay with time — run score-health or sync-entry")

    overall = re.search(r"(?m)^\s+overall:\s*(\S+)\s*$", block)
    if not overall or overall.group(1).strip("\"'") not in GRADES:
        rep.error(path, "health: missing/invalid 'overall' grade (must be A–E or ?)")
    for axis in HEALTH_AXES:
        if not re.search(r"(?m)^\s{4}" + axis + r":\s*$", block):
            rep.error(path, f"health: missing axis '{axis}'")
    grades = re.findall(r"(?m)^\s+grade:\s*(\S+)\s*$", block)
    bad = sorted({g for g in grades if g.strip("\"'") not in GRADES})
    if bad:
        rep.error(path, f"health: invalid grade value(s): {bad}")
    if len(grades) != 6:
        rep.error(path, f"health: expected 6 axis grades, found {len(grades)}")
    # Adversarial review: challenge '?' grades — they may be false negatives.
    # Compare the *unquoted* grade: the scorer emits "?" quoted (it is a YAML indicator
    # character), so a bare `grade == "?"` test silently matched nothing and this warning
    # never fired once across 600 pages. N/A is excluded — it is a deliberate verdict
    # that the axis does not apply, not a measurement that failed.
    for axis_name, grade in zip(HEALTH_AXES, [g.strip("\"'") for g in grades]):
        if grade == "?":
            rep.warn(path, f"health: axis '{axis_name}' is '?' — verify this is genuinely unmeasurable, not a machine false-negative")

    check_adoption_evidence(path, fmtext, block, rep)

    card = health_card_stem(path, root, base, duplicate_bases) + (".zh.svg" if zh else ".svg")
    if not (root / "assets" / "health" / card).exists():
        rep.error(path, f"health: card missing: assets/health/{card} (run tools/health_card.py)")
    card_ref = f"assets/health/{card}"
    if card_ref not in text[end:]:
        rep.error(path, f"health: block present but card not embedded in body (assets/health/{card})")
        return

    close_end = text.find("\n", end + 4)
    body = text[close_end + 1 :] if close_end != -1 else text[end + 4 :]
    lines = body.splitlines()
    h1_idx = next((i for i, line in enumerate(lines) if re.match(r"^#[ \t]+\S", line)), None)
    card_idx = next((i for i, line in enumerate(lines) if card_ref in line), None)
    first_h2_idx = next((i for i, line in enumerate(lines) if re.match(r"^##[ \t]+\S", line)), None)
    if h1_idx is None or card_idx is None:
        return

    tldr_start = next((i for i in range(h1_idx + 1, len(lines)) if lines[i].strip()), None)
    if tldr_start is None:
        rep.error(path, "health: card must appear after the H1 and one-line TL;DR, before any notice or section")
        return
    tldr_end = next((i for i in range(tldr_start + 1, len(lines)) if not lines[i].strip()), len(lines))
    intervening = [line.strip() for line in lines[tldr_end + 1 : card_idx] if line.strip()]
    if card_idx <= tldr_end or intervening:
        rep.error(path, "health: card must be the first block after the opening TL;DR (before notices/body text)")
    if first_h2_idx is not None and card_idx > first_h2_idx:
        rep.error(path, "health: card must appear before the first H2 section")


def flow_required(last_verified: object) -> bool:
    """A page is on the hook for How it works once it was (re)verified under the contract."""
    if REQUIRE_FLOW:
        return True
    try:
        return dt.date.fromisoformat(str(last_verified)) >= dt.date.fromisoformat(FLOW_REQUIRED_FROM)
    except ValueError:
        return False


def check_flow_section(path: Path, text: str, zh: bool, root: Path, duplicate_bases: set[str],
                       rep: Report, last_verified: object = "") -> None:
    """How it works / 怎么用起来: mechanism prose + backbone flow card + generated text twin."""
    lang = "zh" if zh else "en"
    stem = flow_card.flow_stem(path, root, duplicate_bases)
    rep.flow_stems.add(stem)
    spec_path = root / "flows" / f"{stem}.json"
    span = flow_card.section_bounds(text, lang)
    if span is None:
        if spec_path.exists():
            rep.error(path, f"flows/{stem}.json exists but the page has no '{flow_card.SECTION[lang]}' section")
        elif flow_required(last_verified):
            rep.error(path, f"missing required section: {flow_card.SECTION[lang]} "
                            f"(required for pages with last_verified >= {FLOW_REQUIRED_FROM}; see tools/schema.md)")
        else:
            rep.flow_missing.append(path)
        return

    # position: after When to use (or Q&A if present), right before When NOT to use
    h2 = [m.group(0).strip() for m in re.finditer(r"(?m)^##[ \t]+\S.*$", text)]
    want_when, want_next = ("## 何时使用", "## 何时不用") if zh else ("## When to use", "## When NOT to use")
    callouts = "## 快问快答" if zh else "## Q&A"
    want_prev = callouts if callouts in h2 else want_when
    i = h2.index(flow_card.SECTION[lang])
    if not (i > 0 and h2[i - 1] == want_prev and i + 1 < len(h2) and h2[i + 1] == want_next):
        rep.error(path, f"{flow_card.SECTION[lang]} must sit between '{want_prev}' and '{want_next}'")

    body = text[span[0]:span[1]]
    card_ref = flow_card.card_rel(path, root, stem, lang)
    img_at = body.find(f"]({card_ref})")
    if img_at == -1:
        rep.error(path, f"flow card not embedded in {flow_card.SECTION[lang]}: {card_ref}")
    else:
        prose = body[: body.rfind("![", 0, img_at)] if "![" in body[:img_at] else body[:img_at]
        if not prose.strip():
            rep.error(path, f"{flow_card.SECTION[lang]}: plain-language mechanism paragraph missing before the flow card")

    if not spec_path.exists():
        rep.error(path, f"{flow_card.SECTION[lang]} present but flows/{stem}.json is missing")
        return
    try:
        spec = flow_card.load_spec(spec_path)
    except (ValueError, OSError) as exc:
        rep.error(spec_path, f"unreadable flow spec: {exc}")
        return
    problems = flow_card.validate_spec(spec)
    if problems:
        for prob in problems:
            rep.error(spec_path, prob)
        return
    if lang == "en":  # one spec, two pages — report the editorial smell once
        for note in flow_card.advisories(spec):
            rep.warn(spec_path, note)
    card = root / "assets" / "flow" / flow_card.card_name(stem, lang)
    if not card.exists():
        rep.error(path, f"flow card missing: assets/flow/{card.name} (run tools/flow_card.py)")
    elif card.read_text(encoding="utf-8") != flow_card.render(spec, lang):
        rep.error(path, f"flow card stale vs flows/{stem}.json: assets/flow/{card.name} (run tools/flow_card.py)")
    m = flow_card.BLOCK_RE.search(body)
    want = flow_card.steps_block(spec, lang, stem, flow_card.page_name(text, stem))
    if not m:
        rep.error(path, "flow text list (<!-- flow-steps:begin … end -->) missing (run tools/flow_card.py)")
    elif m.group(0) != want:
        rep.error(path, f"flow text list drifted from flows/{stem}.json — never hand-edit it (run tools/flow_card.py)")


def check_upstream_block(path: Path, text: str, rep: Report) -> None:
    if not text.startswith("---"):
        return
    end = text.find("\n---", 3)
    if end == -1:
        return
    fmtext = text[3:end]
    if not re.search(r"(?m)^upstream:\s*$", fmtext):
        rep.error(path, "upstream: missing required frontmatter block")
        return
    block_m = re.search(r"(?ms)^upstream:\n(.*?)(?=^[A-Za-z_][A-Za-z0-9_-]*:\s*$|\Z)", fmtext)
    block = block_m.group(1) if block_m else ""
    for key in UPSTREAM_KEYS:
        if not re.search(r"(?m)^\s{2}" + key + r":\s*\S+", block):
            rep.error(path, f"upstream: missing '{key}'")
    archived = re.search(r"(?m)^\s{2}archived:\s*(\S+)", block)
    if archived and archived.group(1) not in {"true", "false"}:
        rep.error(path, "upstream: archived must be true or false")
    pushed_at = re.search(r"(?m)^\s{2}pushed_at:\s*(\S+)", block)
    if pushed_at and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$", pushed_at.group(1)):
        rep.error(path, "upstream: pushed_at must be an ISO UTC timestamp")
    sha = re.search(r"(?m)^\s{2}default_branch_sha:\s*(\S+)", block)
    if sha and not re.match(r"^[0-9a-f]{40}$", sha.group(1)):
        rep.error(path, "upstream: default_branch_sha must be a 40-char git SHA")


def section_after_heading(text: str, match: re.Match[str]) -> str:
    start = match.end()
    nxt = re.search(r"(?m)^##\s+", text[start:])
    end = start + nxt.start() if nxt else len(text)
    return text[start:end].strip()


def check_qa(
    path: Path,
    text: str,
    zh: bool,
    sibling_text: str | None,
    rep: Report,
) -> None:
    own = QA_RE_ZH if zh else QA_RE_EN
    found = own.search(text)
    if found:
        if not section_after_heading(text, found):
            rep.error(path, "Q&A / 快问快答 is empty — drop the heading; if there is genuinely nothing, record `no leftover Q&A` in the change summary")
        h2 = [m.group(0).strip() for m in re.finditer(r"(?m)^##[ \t]+\S.*$", text)]
        heading = "## 快问快答" if zh else "## Q&A"
        want_prev = "## 何时使用" if zh else "## When to use"
        want_flow = "## 怎么用起来" if zh else "## How it works"
        want_not = "## 何时不用" if zh else "## When NOT to use"
        want_next = want_flow if want_flow in h2 else want_not
        i = h2.index(heading) if heading in h2 else -1
        if not (i > 0 and h2[i - 1] == want_prev and i + 1 < len(h2) and h2[i + 1] == want_next):
            rep.error(
                path,
                "Q&A / 快问快答 must sit between When to use and How it works "
                "(or When NOT to use, if How it works is absent)",
            )
    if sibling_text is not None and not zh:
        if bool(QA_RE_EN.search(text)) != bool(QA_RE_ZH.search(sibling_text)):
            rep.error(path, "Q&A / 快问快答 presence must match the bilingual sibling")


def check_page(path: Path, category_dir: Path, root: Path, duplicate_bases: set[str], rep: Report, today: dt.date) -> None:
    name = path.name
    zh = name.endswith(ZH_SUFFIX)
    base = base_slug(name)
    text = path.read_text(encoding="utf-8")

    fm = parse_frontmatter(text)
    if fm is None:
        rep.error(path, "missing or malformed YAML frontmatter (must start with '---')")
        return

    for key in REQUIRED_KEYS:
        if key not in fm or fm[key] in ("", None, []):
            rep.error(path, f"frontmatter missing required key: {key}")

    if fm.get("slug") and fm["slug"] != base:
        rep.error(path, f"slug '{fm['slug']}' != base filename '{base}'")
    if fm.get("category") and fm["category"] != category_dir.name:
        rep.error(path, f"category '{fm['category']}' != parent dir '{category_dir.name}'")
    if "tags" in fm and not isinstance(fm["tags"], list):
        rep.error(path, "tags must be an inline list: tags: [a, b]")

    ptype = fm.get("type", "")
    if ptype and ptype not in ALLOWED_TYPES:
        rep.error(path, f"type '{ptype}' not in {sorted(ALLOWED_TYPES)}")

    lv = fm.get("last_verified", "")
    if lv:
        try:
            d = dt.date.fromisoformat(str(lv))
            age = (today - d).days
            if age > STALE_DAYS:
                rep.warn(path, f"stale: last_verified {lv} is {age}d old (> {STALE_DAYS}); run sync-entry")
            if d > today:
                rep.error(path, f"last_verified {lv} is in the future (UTC today is {today}); "
                                f"write the UTC date, not a local date ahead of it")
        except ValueError:
            rep.error(path, f"last_verified '{lv}' is not a valid YYYY-MM-DD date")

    # H1 title: schema requires every page to open with `# <name>` (then a one-line TL;DR).
    if not re.search(r"(?m)^#[ \t]+\S", text):
        rep.error(path, "missing H1 title (`# <name>`) at the top of the page")

    for section in required_sections(ptype if ptype in ALLOWED_TYPES else "tool", zh):
        if not re.search(r"(?m)^" + re.escape(section) + r"\s*$", text):
            rep.error(path, f"missing required section: {section}")

    unresearched = text.count(UNRESEARCHED_MARKER)
    if unresearched:
        rep.error(path, f"{unresearched} section(s) still carry {UNRESEARCHED_MARKER}: the page was "
                        f"scaffolded but not researched. Read the upstream sources and write those "
                        f"sections (sync-entry), or drop the page — do not delete the marker alone.")
    check_comparison_table(path, text, zh, rep)

    # skill-pack pages must OMIT the extra sections, not pad them — forbid, don't just not-require.
    if ptype in NO_EXTRA_TYPES:
        for section in (EXTRA_ZH if zh else EXTRA_EN):
            if re.search(r"(?m)^" + re.escape(section) + r"\s*$", text):
                rep.error(path, f"skill-pack must omit (not include) section: {section}")

    # Caveats ledger (all types): the uncertainty list lives here, not sprinkled across the prose.
    cav_re = CAVEATS_RE_ZH if zh else CAVEATS_RE_EN
    cav = cav_re.search(text)
    if cav is None:
        rep.error(path, "missing required section: ## 存疑（未验证） / ## Caveats (unverified)")
    # Prose-region label density: keep only load-bearing [未验证]/[推断] inline; converge the rest.
    # The "narrative prose" region ends at Health & viability OR Caveats (whichever comes first) —
    # both are labeled-judgment/ledger sections where labels are expected, not sprinkled prose.
    health = (HEALTH_RE_ZH if zh else HEALTH_RE_EN).search(text)
    bounds = [m.start() for m in (health, cav) if m]
    prose = text[: min(bounds)] if bounds else text
    callouts = (QA_RE_ZH if zh else QA_RE_EN).search(text)
    if callouts:
        nxt = re.search(r"(?m)^##\s+", text[callouts.end():])
        end = callouts.end() + nxt.start() if nxt else len(text)
        prose = prose[: callouts.start()] + prose[end:]
    n_inline = len(LABEL_RE.findall(prose))
    if n_inline > PROSE_LABEL_MAX:
        rep.warn(path, f"{n_inline} inline [未验证]/[推断] before the Health/Caveats sections (> {PROSE_LABEL_MAX}); "
                       f"keep load-bearing ones, move the rest into the Caveats ledger")

    sibling = category_dir / (base + (".md" if zh else ZH_SUFFIX))
    sibling_text = None
    if not sibling.exists():
        rep.error(path, f"missing {'English' if zh else 'Chinese'} sibling: {sibling.name}")
    elif not zh:
        # Frontmatter is facts (language-neutral) -> must be identical across the bilingual pair.
        # Compare normalized raw frontmatter so nested health/upstream facts cannot silently drift.
        sibling_text = sibling.read_text(encoding="utf-8")
        if normalized_frontmatter(text) != normalized_frontmatter(sibling_text):
            rep.error(path, f"frontmatter drift vs {sibling.name} (must be identical)")
    check_qa(path, text, zh, sibling_text, rep)

    check_health_block(path, text, base, zh, root, duplicate_bases, rep, today)
    check_upstream_block(path, text, rep)
    check_flow_section(path, text, zh, root, duplicate_bases, rep, fm.get("last_verified", ""))

    for link in md_links(text):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (path.parent / link.split("#", 1)[0]).resolve().exists():
            rep.error(path, f"broken internal link: {link}")


def walk_category(catdir: Path, root: Path, duplicate_bases: set[str], rep: Report, today: dt.date) -> None:
    en_index, zh_index = catdir / INDEX_EN, catdir / INDEX_ZH
    if not en_index.exists():
        rep.error(catdir, f"category node has no {INDEX_EN}")
    if not zh_index.exists():
        rep.error(catdir, f"category node has no {INDEX_ZH}")
    en_linked, zh_linked = linked_targets(en_index), linked_targets(zh_index)

    pages = sorted(p for p in catdir.glob("*.md") if is_page(p.name))
    n_en_pages = 0
    for page in pages:
        check_page(page, catdir, root, duplicate_bases, rep, today)
        zh = page.name.endswith(ZH_SUFFIX)
        if not zh:
            n_en_pages += 1
        idx_linked = zh_linked if zh else en_linked
        idx_name = INDEX_ZH if zh else INDEX_EN
        if (zh_index if zh else en_index).exists() and page.resolve() not in idx_linked:
            rep.error(page, f"orphan: not linked from {idx_name}")
    if n_en_pages > MAX_FANOUT:
        rep.warn(catdir, f"overflow: {n_en_pages} pages > MAX_FANOUT={MAX_FANOUT}; split into sub-categories (refactor-index)")

    # Treat EVERY non-hidden subdirectory as a category node — do NOT gate on INDEX.md existing,
    # or a dir missing its INDEX (e.g. only INDEX.zh.md, or just pages) would be silently skipped.
    # walk_category() reports the missing INDEX, so the subtree is inspected instead of dropped.
    subcats = sorted(d for d in catdir.iterdir() if d.is_dir() and not d.name.startswith("."))
    for sub in subcats:
        if en_index.exists() and (sub / INDEX_EN).resolve() not in en_linked and sub.resolve() not in en_linked:
            rep.error(en_index, f"sub-category '{sub.name}' not linked from {INDEX_EN}")
        if zh_index.exists() and (sub / INDEX_ZH).resolve() not in zh_linked and sub.resolve() not in zh_linked:
            rep.error(zh_index, f"sub-category '{sub.name}' not linked from {INDEX_ZH}")
        walk_category(sub, root, duplicate_bases, rep, today)

    # INDEX internal links resolve
    for idx in (en_index, zh_index):
        if not idx.exists():
            continue
        for link in md_links(idx.read_text(encoding="utf-8")):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            if not (idx.parent / link.split("#", 1)[0]).resolve().exists():
                rep.error(idx, f"broken internal link: {link}")


def check_root_index(root: Path, index_name: str, cat_index_name: str,
                     top_categories: list[Path], rep: Report) -> None:
    root_index = root / index_name
    if not root_index.exists():
        rep.error(root, f"missing root {index_name}")
        return
    linked = linked_targets(root_index)
    for cat in top_categories:
        if (cat / cat_index_name).resolve() not in linked and cat.resolve() not in linked:
            rep.error(root_index, f"top category '{cat.name}' not linked (expected {cat.name}/{cat_index_name})")
    for link in md_links(root_index.read_text(encoding="utf-8")):
        if link.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if not (root / link.split("#", 1)[0]).resolve().exists():
            rep.error(root_index, f"broken internal link: {link}")


def count_pages(catdir: Path) -> tuple[int, int]:
    en = zh = 0
    for p in catdir.rglob("*.md"):
        if not is_page(p.name):
            continue
        if p.name.endswith(ZH_SUFFIX):
            zh += 1
        else:
            en += 1
    return en, zh


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    rep = Report()
    today = today_utc()

    categories_dir = root / "categories"
    if not categories_dir.is_dir():
        rep.error(root, "no categories/ directory")
        print("\n".join(rep.errors))
        return 1
    duplicate_bases = duplicate_slugs(root)

    # Every non-hidden dir under categories/ is a top-level category node (not gated on INDEX.md;
    # see walk_category — a node missing its INDEX is reported, never skipped).
    top_categories = sorted(d for d in categories_dir.iterdir() if d.is_dir() and not d.name.startswith("."))
    for cat in top_categories:
        walk_category(cat, root, duplicate_bases, rep, today)

    check_root_index(root, INDEX_EN, INDEX_EN, top_categories, rep)
    check_root_index(root, INDEX_ZH, INDEX_ZH, top_categories, rep)

    for summary in [root / "README.md", root / "README.zh.md", *sorted(categories_dir.rglob("INDEX.md")), *sorted(categories_dir.rglob("INDEX.zh.md"))]:
        if summary.exists():
            check_summary_health_columns(summary, rep)
            drifts, malformed = health_parity_rows(summary, root)
            for line_no, got, want, page in drifts:
                rep.error(f"{summary}:{line_no}",
                          f"health column drift: {page.name} frontmatter says '{want}', row says '{got}' "
                          f"(run tools/sync_index_health.py --apply)")
            for line_no, n_row, n_head, snippet in malformed:
                rep.error(f"{summary}:{line_no}",
                          f"summary table row has {n_row} columns, header has {n_head}: {snippet}…")

    # Chinese punctuation: fullwidth in CJK context across every .zh.md (pages, INDEX, README).
    for zh in sorted(root.rglob("*.zh.md")):
        if any(part.startswith(".") for part in zh.relative_to(root).parts):
            continue
        v = zh_punct_violations(zh.read_text(encoding="utf-8"))
        if v:
            rep.error(zh, f"{v} ASCII , ; ! ? : ( ) \" adjacent to CJK — use fullwidth 中文标点 （，；：！？（）“”）")

    # README master listing must stay in parity with the indexed pages (guards silent drift):
    # README.md lists every EN page, README.zh.md lists every ZH page.
    en_pages = [p for p in categories_dir.rglob("*.md")
                if is_page(p.name) and not p.name.endswith(ZH_SUFFIX)]
    for readme_name, want_zh in (("README.md", False), ("README.zh.md", True)):
        rp = root / readme_name
        if not rp.exists():
            rep.error(root, f"missing {readme_name}")
            continue
        body = rp.read_text(encoding="utf-8")
        for en in sorted(en_pages):
            rel = en.relative_to(root).as_posix()
            target = (rel[: -len(".md")] + ZH_SUFFIX) if want_zh else rel
            if target not in body:
                rep.error(rp, f"indexed page not listed in {readme_name}: {target}")

    # flows/: every spec must belong to a page (no orphans); backfill progress is ONE line, not 1000.
    flows_dir = root / "flows"
    if flows_dir.is_dir():
        for spec in sorted(flows_dir.glob("*.json")):
            if spec.stem not in rep.flow_stems:
                rep.error(spec, "orphan flow spec: no page resolves to this stem")
    if rep.flow_missing:
        total = len([p for p in categories_dir.rglob("*.md") if is_page(p.name)])
        rep.warn("how-it-works", f"{len(rep.flow_missing)}/{total} pages still lack "
                                 f"'## How it works' / '## 怎么用起来' (backfill backlog; pages with "
                                 f"last_verified >= {FLOW_REQUIRED_FROM} already ERROR, and "
                                 f"OSS_ATLAS_REQUIRE_FLOW=1 makes every one an ERROR)")

    for w in rep.warnings:
        print(w)
    for e in rep.errors:
        print(e)

    n_en, n_zh = count_pages(categories_dir)
    n_nodes = sum(1 for d in categories_dir.rglob("*") if d.is_dir() and (d / INDEX_EN).exists())
    print(f"\n{n_nodes} category nodes, {n_en} EN + {n_zh} ZH pages, "
          f"{len(rep.errors)} errors, {len(rep.warnings)} warnings.")
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
