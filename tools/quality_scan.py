#!/usr/bin/env python3
"""Report-only quality scanner for oss-atlas project pages.

This tool is intentionally separate from tools/lint.py. It catches deterministic
weak-model artifacts and audit signals, but it does not claim semantic approval.

Env: OSS_ATLAS_STUB_BLOCKED_FROM (default 2026-09-22) — a page carrying batch-intake
placeholder prose, duplicated judgment prose, or an untranslated lead line fails the gate
once its last_verified reaches this date.
"""
from __future__ import annotations

import argparse
import os
import re
import zlib
import subprocess
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


ZH_SUFFIX = ".zh.md"
ZERO_SHA = "0000000000000000000000000000000000000000"
GENERIC_TEMPLATES = ["Use this page for its stated niche", "当前页用于它的主场景"]
TRUNCATION_FRAGMENTS = ["trac.", "(Node.", "and.", "per-har.", "before co."]
# Verbatim prose emitted by the batch intake generators (tools/intake_queue_apply.py,
# tools/agent_skills_intake.py). Those scripts mass-create pages from a backlog of names with
# machine-read facts and placeholder judgment: `When to use` describes choosing software in
# general rather than this project's trigger, and Dependencies / Ops difficulty / Health say only
# that nobody has looked yet. lint.py passes them (the sections exist) and a reader cannot tell
# them apart from a researched page, so they are detected here and carried as backlog until
# sync-entry rewrites them.
INTAKE_STUB_MARKERS = [
    "This first-pass page exists because",
    "when its upstream description matches the job",
    "an untracked name from a backlog",
    "not exhaustively verified in this intake pass",
    "Unknown to medium until the upstream docs are reread",
    "Unknown to medium until deeper review",
    "这个首版页面存在，是因为",
    "首版 intake 页面",
    "本首版页面尚未穷尽读取所有依赖清单",
    "本次 intake 未穷尽核验",
    "本次 intake 未完整复核",
    "在重读上游文档前，按未知到中等处理",
]
# A page may keep stub prose (backlog, report-only) but must not also claim a fresh verification
# date: re-verifying a page is exactly when the placeholder prose has to be replaced. Pages whose
# last_verified is on or after this date fail the gate. Mirrors lint.py's FLOW_REQUIRED_FROM.
STUB_BLOCKED_FROM = os.environ.get("OSS_ATLAS_STUB_BLOCKED_FROM", "2026-09-22")
# Sections whose whole job is judgment: a generator or a copy-paste has no way to fill these
# without reading the sources, so they are where boilerplate lands. Compared per language.
# Thresholds are per section and per language, each set above what researched pages actually reach.
# `When to use` / `When NOT to use` state why *this* project and not another, so overlap there is a
# defect: across the current index the most similar researched pair reaches 21% / 28%, while
# batch-generated pages start at 72%. `Dependencies` / `Ops difficulty` describe facts that can
# legitimately coincide (python-docx and python-pptx really do both just need lxml), so only
# near-verbatim reuse counts — at 0.65 the survivors are real copy-paste, e.g. driver-js and
# intro-js sharing a word-for-word ops paragraph.
DUP_SECTIONS = {
    "When to use": 0.40, "When NOT to use": 0.40,
    # Chinese runs higher for the same semantic distance: a 9-character shingle spans roughly a
    # clause of CJK but only a word or two of English, so two zh pages that are genuinely different
    # yet structurally parallel share far more shingles than their en counterparts. Measured: the
    # most similar researched pair reaches 28% in `When NOT to use` and 48% in `何时不用` — same two
    # projects, prose written separately (itchat/wxpy, both killed by the same WeChat protocol
    # shutdown). Thresholds sit above each language's observed ceiling.
    "何时使用": 0.55, "何时不用": 0.55,
    "Dependencies": 0.65, "Ops difficulty": 0.65, "依赖": 0.65, "运维难度": 0.65,
}
# Phrase blacklists only ever catch boilerplate someone already wrote. What makes boilerplate
# boilerplate is not its wording but that it repeats: prose written without reading THIS project
# says the same thing about every project. Measured over the current index, a page's `When to use`
# overlaps the most similar other page by at most 14% when it was researched and by at least 73%
# when it came from the batch generators — so any threshold in between separates them without
# knowing a single phrase in advance. 0.40 sits in that gap.
# Scales every threshold above, for tightening or loosening the whole check at once.
DUP_THRESHOLD_SCALE = float(os.environ.get("OSS_ATLAS_DUP_THRESHOLD_SCALE", "1.0"))
DUP_MIN_CHARS = 120          # shorter sections are too small for the ratio to mean anything
# The line under the H1 is the one sentence every reader reads (schema.md, "The lead line is the
# problem, not the definition"). On a `.zh.md` page it must be authored in Chinese; the cheapest
# thing a generator can put there instead is the upstream README tagline, which arrives in English
# with its marketing adjectives and emoji intact ("🐢 Open-Source Evaluation & Testing library for
# LLM Agents"). That is detectable without judging prose: measure how much of the lead is CJK.
# Fullwidth punctuation counts as Chinese: it is what a real ZH lead uses (schema.md requires it)
# and what an English tagline never has, so including it pushes the two clusters further apart.
# A 2026-09-22 census of all 588 ZH pages found them cleanly separated: the 102 untranslated
# upstream taglines top out at 7.7%, while the most English-heavy *real* Chinese lead — a skill
# page whose name and subject are both English — sits at 16.4%, and ordinary leads run 40–60%.
# 0.12 is the midpoint of that empty band, so no borderline page is being adjudicated. (Counting
# CJK ideographs alone put that real floor at 11%, inside the gate — hence the punctuation range.)
ZH_LEAD_MIN_CJK_RATIO = 0.12
# Below this length a lead is too short for the ratio to mean anything (a bare command, a name).
# Defensive only — no page in the 2026-09-22 census has a lead this short.
ZH_LEAD_MIN_LENGTH = 12
SHINGLE_K = 9
SHINGLE_STEP = 3
SHINGLE_SAMPLE = 4           # keep ~1/4 of shingles: same ratios, a quarter of the postings
LAST_VERIFIED_RE = re.compile(r"^last_verified:\s*['\"]?(\d{4}-\d{2}-\d{2})", re.MULTILINE)
KNOWN_CATEGORIES = [
    "composite-alternative-partly-indexed",
    "generic-comparison-template",
    "health-prose-grade-drift",
    "health-prose-raw-drift",
    "indexed-page-marked-non-repo",
    "indexed-page-marked-not-indexed",
    "duplicated-section-prose",
    "duplicated-section-prose-reverified",
    "intake-stub-page",
    "intake-stub-page-reverified",
    "non-repo-status-legacy-form",
    "truncation-fragment",
    "zero-placeholder-upstream-sha",
    "zh-lead-not-chinese",
    "zh-lead-not-chinese-reverified",
    "zh-link-to-english-sibling",
]
GATED_DETERMINISTIC_CATEGORIES = {
    "composite-alternative-partly-indexed",
    "generic-comparison-template",
    "duplicated-section-prose-reverified",
    "indexed-page-marked-non-repo",
    "indexed-page-marked-not-indexed",
    "intake-stub-page-reverified",
    "truncation-fragment",
    "zh-lead-not-chinese-reverified",
    "zh-link-to-english-sibling",
}
NOT_INDEXED_MARKERS = ["not indexed", "未收录"]
INDEXED_MARKERS = ["✅", "已收录"]
PARTIALLY_INDEXED_MARKERS = ["partly indexed", "partially indexed", "部分已收录"]
# `非仓库` / `not a repo` is a STATUS, not a flavour of `未收录` (schema §2): `未收录` claims the
# alternative is a real repository we have not added yet (backlog debt); `非仓库` claims it is not
# a repository at all (hosted SaaS, closed app, paid service, article) and therefore out of scope.
# Writers had been hand-rolling the difference as `未收录（非仓库）`; 22 files still carry that
# combined form, which is detected here only so the sweep can normalize it (report-only).
NON_REPO_MARKERS = ["非仓库", "not a repository", "not a repo", "non-repo"]
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MIN_GLOBAL_PLAIN_SLUG_LENGTH = 7
HEALTH_AXES = ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]
AXIS_LABELS = {
    "maintenance": ["Maintenance", "维护活跃度"],
    "responsiveness": ["Responsiveness", "响应速度", "响应性"],
    "adoption": ["Adoption", "采用广度", "采用度"],
    "longevity": ["Longevity", "长青度"],
    "governance": ["Governance", "Bus factor", "Bus Factor", "治理集中度", "维护者分散度"],
    "risk_license": ["Risk", "License", "Risk/License", "许可宽松度", "许可证风险"],
}
RAW_NUMERIC_FIELDS = {
    "responsiveness": ["median_ttfr_hours", "qualifying_issues"],
    "adoption": ["downloads_last_month", "dependent_repos_count"],
    "longevity": ["repo_age_days", "last_commit_age_days"],
    "governance": ["top3_share", "top1_share", "active_maintainers_12mo"],
}
RAW_FIELD_TRIGGERS = {
    "median_ttfr_hours": ["median", "first-response", "首次响应", "中位"],
    "qualifying_issues": ["qualifying", "issues/PRs", "issue/PR"],
    "downloads_last_month": ["download", "downloads", "下载量"],
    "dependent_repos_count": ["dependent repos", "dependent repositories", "dependents", "依赖仓库"],
    "repo_age_days": ["days old", "repo age", "created", "创建", "已创建"],
    "last_commit_age_days": ["last commit", "last pushed", "最后提交", "最后 push", "最近推送"],
    "top3_share": ["top-3", "top3", "前三"],
    "top1_share": ["top-1", "top1", "第一贡献者"],
    "active_maintainers_12mo": ["active maintainer", "active maintainers", "活跃维护者"],
}


@dataclass(frozen=True)
class Finding:
    category: str
    severity: str
    path: str
    line: int
    message: str
    evidence: str


@dataclass
class ScanResult:
    findings: list[Finding]
    health_unknowns: Counter[tuple[str, str]]
    project_page_count: int
    english_canonical_page_count: int
    indexed_project_page_count: int
    scan_mode: str = "all"
    scope_paths: tuple[str, ...] = ()
    changed_candidate_count: int = 0


def section_body(text: str, name: str) -> str:
    match = re.search(rf"##\s+{re.escape(name)}\s*\n(.*?)(\n##\s|\Z)", text, re.S)
    return match.group(1).strip() if match else ""


def shingles(body: str) -> set[str]:
    flat = re.sub(r"\W+", " ", body.lower()).strip()
    return {
        flat[i : i + SHINGLE_K]
        for i in range(0, max(0, len(flat) - SHINGLE_K), SHINGLE_STEP)
        if zlib.crc32(flat[i : i + SHINGLE_K].encode()) % SHINGLE_SAMPLE == 0
    }


def detect_duplicated_sections(pages: list[Path], universe: list[Path], root: Path) -> list[Finding]:
    """Flag a judgment section that is near-identical to the same section on another page.

    Compared against the whole index (`universe`), not just the scanned scope, so a scoped run
    still sees a match against a page it did not scan.
    """
    findings: list[Finding] = []
    scoped = {page.resolve() for page in pages}
    for section, base_threshold in DUP_SECTIONS.items():
        threshold = min(1.0, base_threshold * DUP_THRESHOLD_SCALE)
        bodies: dict[Path, set[str]] = {}
        texts: dict[Path, str] = {}
        for page in universe:
            text = page.read_text(encoding="utf-8")
            body = section_body(text, section)
            if len(body) < DUP_MIN_CHARS:
                continue
            grams = shingles(body)
            if grams:
                bodies[page] = grams
                texts[page] = text
        if len(bodies) < 2:
            continue
        posting: dict[str, list[Path]] = {}
        for page, grams in bodies.items():
            for gram in grams:
                posting.setdefault(gram, []).append(page)
        for page, grams in bodies.items():
            if page.resolve() not in scoped:
                continue
            shared: Counter[Path] = Counter()
            for gram in grams:
                for other in posting[gram]:
                    if other != page:
                        shared[other] += 1
            if not shared:
                continue
            twin, hits = shared.most_common(1)[0]
            ratio = hits / len(grams)
            if ratio < threshold:
                continue
            text = texts[page]
            offset = text.find(f"## {section}")
            verified = last_verified_of(text)
            message = (f"`{section}` is {ratio:.0%} the same text as {relpath(twin, root)} — prose "
                       f"that says the same thing about two projects describes neither.")
            if verified and verified >= STUB_BLOCKED_FROM:
                findings.append(Finding("duplicated-section-prose-reverified", "high", relpath(page, root),
                                        line_number(text, max(offset, 0)),
                                        message + f" The page claims last_verified {verified} >= "
                                                  f"{STUB_BLOCKED_FROM}; write it from the sources.", f"{ratio:.0%}"))
            else:
                findings.append(Finding("duplicated-section-prose", "medium", relpath(page, root),
                                        line_number(text, max(offset, 0)), message, f"{ratio:.0%}"))
    return findings


def last_verified_of(text: str) -> str | None:
    match = LAST_VERIFIED_RE.search(text)
    return match.group(1) if match else None


def detect_intake_stub(text: str, rel: str) -> list[Finding]:
    """One finding per page, not per marker: the whole page is the stub, not each sentence."""
    hits = [marker for marker in INTAKE_STUB_MARKERS if marker in text]
    if not hits:
        return []
    offset = min(text.find(marker) for marker in hits)
    verified = last_verified_of(text)
    evidence = f"{hits[0]} (+{len(hits) - 1} more)" if len(hits) > 1 else hits[0]
    if verified and verified >= STUB_BLOCKED_FROM:
        return [Finding("intake-stub-page-reverified", "high", rel, line_number(text, offset),
                        f"Page carries first-pass intake prose but claims last_verified {verified} "
                        f">= {STUB_BLOCKED_FROM}; rewrite the placeholder sections (sync-entry).", evidence)]
    return [Finding("intake-stub-page", "medium", rel, line_number(text, offset),
                    "First-pass intake page: facts are machine-read, judgment sections are placeholders.", evidence)]


def is_chinese_char(ch: str) -> bool:
    """A CJK ideograph, or the fullwidth punctuation a Chinese body is required to use."""
    code = ord(ch)
    return (0x4E00 <= code <= 0x9FFF) or (0x3000 <= code <= 0x303F) or (0xFF01 <= code <= 0xFF60)


def lead_line(text: str) -> tuple[str, int] | None:
    """The first non-empty, non-image line after the H1 — the page's lead. None if there is none."""
    offset = 0
    seen_h1 = False
    for raw in text.split("\n"):
        line = raw.strip()
        if seen_h1 and line and not line.startswith("!["):
            return line, offset
        if raw.startswith("# "):
            seen_h1 = True
        offset += len(raw) + 1
    return None


def detect_zh_lead_not_chinese(text: str, rel: str) -> list[Finding]:
    """A ZH page whose lead line was never translated — almost always the upstream README tagline."""
    found = lead_line(text)
    if found is None:
        return []
    lead, offset = found
    if len(lead) < ZH_LEAD_MIN_LENGTH:
        return []
    ratio = sum(1 for ch in lead if is_chinese_char(ch)) / len(lead)
    if ratio >= ZH_LEAD_MIN_CJK_RATIO:
        return []
    evidence = lead if len(lead) <= 70 else lead[:70] + "…"
    verified = last_verified_of(text)
    line = line_number(text, offset)
    if verified and verified >= STUB_BLOCKED_FROM:
        return [Finding("zh-lead-not-chinese-reverified", "high", rel, line,
                        f"Chinese page opens with a {ratio:.0%}-CJK lead but claims last_verified "
                        f"{verified} >= {STUB_BLOCKED_FROM}; write the lead in Chinese, as the "
                        "problem it solves rather than the upstream tagline (schema.md).", evidence)]
    return [Finding("zh-lead-not-chinese", "medium", rel, line,
                    f"Chinese page opens with a {ratio:.0%}-CJK lead — the upstream English tagline "
                    "was left in place instead of a Chinese lead stating the problem.", evidence)]


def is_project_page(path: Path) -> bool:
    return path.suffix == ".md" and path.name not in {"INDEX.md", "INDEX.zh.md"}


def project_pages(root: Path) -> list[Path]:
    categories = root / "categories"
    if not categories.exists():
        return []
    return sorted(path for path in categories.rglob("*.md") if is_project_page(path))


def is_project_page_under_root(path: Path, root: Path) -> bool:
    categories = root / "categories"
    try:
        path.relative_to(categories)
    except ValueError:
        return False
    return path.exists() and path.is_file() and is_project_page(path)


def normalize_scope_path(root: Path, scope: Path | str) -> Path:
    path = Path(scope)
    if not path.is_absolute():
        path = root / path
    return path.resolve()


def resolve_scope_paths(root: Path, scopes: list[Path | str] | tuple[Path | str, ...]) -> list[Path]:
    selected: set[Path] = set()
    for scope in scopes:
        scope_path = normalize_scope_path(root, scope)
        if not scope_path.exists():
            raise FileNotFoundError(f"Scope path does not exist: {scope}")
        if scope_path.is_file():
            if is_project_page_under_root(scope_path, root):
                selected.add(scope_path)
            continue
        if scope_path.is_dir():
            selected.update(path for path in scope_path.rglob("*.md") if is_project_page_under_root(path, root))
            continue
        raise ValueError(f"Scope path is not a file or directory: {scope}")
    return sorted(selected)


def git_changed_markdown_candidates(root: Path) -> list[Path]:
    commands = [
        ["git", "-C", str(root), "diff", "--name-only", "--diff-filter=ACMRTUXB", "HEAD", "--", "*.md"],
        ["git", "-C", str(root), "ls-files", "--others", "--exclude-standard", "--", "*.md"],
    ]
    candidates: set[Path] = set()
    for command in commands:
        completed = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in completed.stdout.splitlines():
            if line.strip():
                candidates.add((root / line.strip()).resolve())
    return sorted(candidates)


def changed_project_pages(root: Path) -> list[Path]:
    return sorted(path for path in git_changed_markdown_candidates(root) if is_project_page_under_root(path, root))


def relpath(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def body_start(text: str) -> int:
    if not text.startswith("---"):
        return 0
    end = text.find("\n---", 3)
    return end + 4 if end != -1 else 0


def base_slug(name: str) -> str:
    return name[: -len(ZH_SUFFIX)] if name.endswith(ZH_SUFFIX) else name[: -len(".md")]


def canonical_target(path: Path) -> Path:
    if path.name.endswith(ZH_SUFFIX):
        return path.with_name(f"{base_slug(path.name)}.md").resolve()
    return path.resolve()


def indexed_slugs(pages: list[Path]) -> set[str]:
    return {base_slug(page.name) for page in pages}


def slugify_label(label: str) -> str:
    plain = re.sub(r"`([^`]+)`", r"\1", label).strip()
    plain = re.sub(r"\[[^\]]+\]\([^)]+\)", "", plain).strip()
    plain = plain.split("/", 1)[0].strip()
    plain = re.sub(r"\([^)]*\)", "", plain).strip()
    plain = plain.replace("（", " ").replace("）", " ")
    plain = plain.lower().replace("_", "-")
    plain = re.sub(r"[^a-z0-9]+", "-", plain).strip("-")
    return plain


def slugify_candidate_label(label: str) -> str:
    plain = re.sub(r"`([^`]+)`", r"\1", label).strip()
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain).strip()
    plain = re.sub(r"\([^)]*\)", "", plain).strip()
    plain = re.sub(r"（[^）]*）", "", plain).strip()
    plain = plain.lower().replace("_", "-")
    plain = re.sub(r"[^a-z0-9]+", "-", plain).strip("-")
    return plain


def alternative_candidate_slugs(label: str) -> set[str]:
    plain = re.sub(r"`([^`]+)`", r"\1", label).strip()
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain).strip()
    chunks = [plain]
    for comma_part in re.split(r"\s*[,，;；]\s*", plain):
        chunks.append(comma_part)
        chunks.extend(part.strip() for part in re.split(r"\s+/\s+", comma_part) if part.strip())
    return {slug for chunk in chunks if (slug := slugify_candidate_label(chunk))}


def is_indexed_plain_candidate(source: Path, candidate_slug: str, indexed_targets: set[Path], indexed_slug_set: set[str]) -> bool:
    sibling = source.with_name(f"{candidate_slug}.md").resolve()
    if sibling in indexed_targets:
        return True
    return len(candidate_slug) >= MIN_GLOBAL_PLAIN_SLUG_LENGTH and candidate_slug in indexed_slug_set


def non_repo_status(status: str) -> bool:
    """True when the status cell claims the alternative is not a repository at all.

    `非仓库` / `not a repo` is out-of-scope-by-shape (hosted SaaS, closed app, paid service,
    article), which is a different claim from `未收录` = a real repository we have not added yet.
    """
    return any(marker in status for marker in NON_REPO_MARKERS)


def legacy_non_repo_status(status: str) -> bool:
    """`未收录（非仓库）` / `not indexed (non-repo)`: the hand-rolled combined form.

    Writers used it before the standalone status existed (22 files as of 2026-09-22). It still
    reads correctly, so this is report-only: the sweep normalizes it to `非仓库` / `not a repo`.
    """
    return non_repo_status(status) and any(marker in status for marker in NOT_INDEXED_MARKERS)


def row_resolves_to_indexed(source: Path, line: str, cells: list[str], indexed_targets: set[Path], indexed_slug_set: set[str]) -> bool:
    """True when a comparison row's alternative column resolves to a page already in the index.

    Links win anywhere in the row; a plain-text alternative is resolved by same-directory sibling
    first, then by a global slug long enough to be unambiguous.
    """
    if any(
        (target := resolve_markdown_target(source, href)) and canonical_target(target) in indexed_targets
        for _label, href in LINK_RE.findall(line)
    ):
        return True
    if len(cells) >= 2 and LINK_RE.search(cells[0]):
        return False
    return any(
        is_indexed_plain_candidate(source, slug, indexed_targets, indexed_slug_set)
        for slug in alternative_candidate_slugs(cells[0])
    )


def split_composite_label(label: str) -> list[str]:
    plain = re.sub(r"`([^`]+)`", r"\1", label).strip()
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain).strip()
    parts = [part.strip() for part in re.split(r"\s+/\s+", plain) if part.strip()]
    return parts if len(parts) > 1 else []



def resolve_markdown_target(source: Path, href: str) -> Path | None:
    target = href.split("#", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    if not target.endswith(".md"):
        return None
    return (source.parent / target).resolve()


def table_cells(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [cell.strip() for cell in body.split("|")]


def is_table_separator(line: str) -> bool:
    cells = table_cells(line)
    return bool(cells) and all(cell and set(cell) <= set("-: ") and cell.count("-") >= 3 for cell in cells)


def detects_partly_indexed_composite(source: Path, cells: list[str], indexed_targets: set[Path], indexed_slug_set: set[str]) -> bool:
    if len(cells) < 2 or not any(marker in cells[1] for marker in INDEXED_MARKERS):
        return False
    if any(marker in cells[1] for marker in NOT_INDEXED_MARKERS):
        return False
    if any(marker in cells[1] for marker in PARTIALLY_INDEXED_MARKERS):
        return False
    parts = split_composite_label(cells[0])
    if not parts:
        return False

    linked_slugs = set()
    for _label, href in LINK_RE.findall(cells[0]):
        target = resolve_markdown_target(source, href)
        if target and canonical_target(target) in indexed_targets:
            linked_slugs.add(base_slug(target.name))

    if not linked_slugs:
        return False

    covered = 0
    uncovered = 0
    for part in parts:
        slug = slugify_label(part)
        if not slug:
            continue
        if slug in linked_slugs:
            covered += 1
        elif source.with_name(f"{slug}.md").resolve() in indexed_targets or slug in indexed_slug_set:
            covered += 1
        else:
            uncovered += 1
    return covered > 0 and uncovered > 0


def section_lines(text: str, heading: str) -> list[tuple[int, str]]:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() != heading:
            continue
        end = next((j for j in range(i + 1, len(lines)) if re.match(r"^##[ \t]+\S", lines[j])), len(lines))
        return [(j + 1, lines[j]) for j in range(i + 1, end)]
    return []


def is_boundary(text: str, index: int) -> bool:
    return index < 0 or index >= len(text) or not text[index].isalnum()


SUMMARY_MATRIX_HEADINGS = ("## Comparison matrix", "## 对比矩阵")


def audit_summary_matrix_rows(root: Path, indexed_targets: set[Path], indexed_slug_set: set[str]) -> list[Finding]:
    """Audit the comparison matrix inside category/root INDEX files.

    The per-page loop never sees these: `is_project_page` skips `INDEX.md`/`INDEX.zh.md`, so a
    matrix row could keep calling an already-indexed project `未收录` indefinitely. That is exactly
    how Letta / Zep / Cognee, Ragas, TRL / verl, Superset and Scylla sat stale until 2026-09-22 —
    the defect class was real, the scan just could not look there. Same two deterministic
    categories as the page scan, so it stays inside the existing gated set.
    """
    findings: list[Finding] = []
    for matrix in sorted(root.glob("categories/**/INDEX*.md")):
        if not matrix.is_file():
            continue
        rel = relpath(matrix, root)
        text = matrix.read_text(encoding="utf-8")
        rows: list[tuple[int, str]] = []
        for heading in SUMMARY_MATRIX_HEADINGS:
            rows.extend(section_lines(text, heading))
        for line_no, line in rows:
            if not line.strip().startswith("|") or is_table_separator(line):
                continue
            cells = table_cells(line)
            if len(cells) < 2:
                continue
            status = cells[1]
            resolves_to_indexed = row_resolves_to_indexed(matrix, line, cells, indexed_targets, indexed_slug_set)
            if non_repo_status(status):
                if resolves_to_indexed:
                    findings.append(
                        Finding(
                            "indexed-page-marked-non-repo",
                            "high",
                            rel,
                            line_no,
                            "Summary matrix row calls an indexed page a non-repo — it has a page, so it is a repository.",
                            line.strip(),
                        )
                    )
                elif legacy_non_repo_status(status):
                    findings.append(
                        Finding(
                            "non-repo-status-legacy-form",
                            "low",
                            rel,
                            line_no,
                            "Combined `未收录（非仓库）` status: use the standalone non-repo status.",
                            line.strip(),
                        )
                    )
            if (
                any(marker in status for marker in NOT_INDEXED_MARKERS)
                and not any(marker in status for marker in INDEXED_MARKERS)
                and not any(marker in status for marker in PARTIALLY_INDEXED_MARKERS)
                and not non_repo_status(status)
                and resolves_to_indexed
            ):
                findings.append(
                    Finding(
                        "indexed-page-marked-not-indexed",
                        "high",
                        rel,
                        line_no,
                        "Summary matrix row marks an existing indexed page as not indexed.",
                        line.strip(),
                    )
                )
            if detects_partly_indexed_composite(matrix, cells, indexed_targets, indexed_slug_set):
                findings.append(
                    Finding(
                        "composite-alternative-partly-indexed",
                        "high",
                        rel,
                        line_no,
                        "Summary matrix row marks an only-partly indexed alternative as indexed.",
                        line.strip(),
                    )
                )
    return findings


def truncation_fragments_in_line(line: str) -> list[str]:
    hits: list[str] = []
    for fragment in TRUNCATION_FRAGMENTS:
        start = 0
        while True:
            offset = line.find(fragment, start)
            if offset == -1:
                break
            before = offset - 1
            after = offset + len(fragment)
            if is_boundary(line, before) and is_boundary(line, after):
                hits.append(fragment)
            start = offset + len(fragment)
    return hits


def unknown_health_axes(text: str) -> Counter[tuple[str, str]]:
    counts: Counter[tuple[str, str]] = Counter()
    lines = text.splitlines()
    unknown_reasons: dict[str, str] = {}
    for i, line in enumerate(lines):
        if line.strip() != "unknowns:":
            continue
        section_end = next((j for j in range(i + 1, len(lines)) if lines[j] and not lines[j].startswith("    ")), len(lines))
        for entry in lines[i + 1 : section_end]:
            stripped = entry.strip()
            match = re.match(r"([a-z_]+):\s*\{\s*reason:\s*([^}]+?)\s*\}", stripped)
            if match:
                unknown_reasons[match.group(1)] = match.group(2).strip().strip('"\'') or "(missing_reason)"
    for i, line in enumerate(lines):
        stripped = line.strip()
        axis = stripped[:-1] if stripped.endswith(":") else ""
        if axis not in HEALTH_AXES:
            continue
        section_end = next(
            (
                j
                for j in range(i + 1, len(lines))
                if lines[j].startswith("    ") and not lines[j].startswith("      ") and lines[j].strip().endswith(":")
            ),
            len(lines),
        )
        block = [line.strip() for line in lines[i + 1 : section_end]]
        if not any(re.fullmatch(r"grade:\s*[\"']?\?[\"']?", entry) for entry in block):
            continue
        reason_line = next((entry for entry in block if entry.startswith("reason:")), "")
        reason = reason_line.partition(":")[2].strip() if reason_line else unknown_reasons.get(axis, "(missing_reason)")
        counts[(axis, reason or "(missing_reason)")] += 1
    return counts


def health_axis_grades(text: str) -> dict[str, str]:
    grades: dict[str, str] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        axis = stripped[:-1] if stripped.endswith(":") else ""
        if axis not in HEALTH_AXES:
            continue
        section_end = next(
            (
                j
                for j in range(i + 1, len(lines))
                if lines[j].startswith("    ") and not lines[j].startswith("      ") and lines[j].strip().endswith(":")
            ),
            len(lines),
        )
        for entry in lines[i + 1 : section_end]:
            match = re.search(r"grade:\s*[\"']?([A-E?])[\"']?", entry.strip())
            if match:
                grades[axis] = match.group(1)
                break
    return grades


def yaml_scalar(raw: str) -> str:
    return raw.strip().strip('"\'')


def health_axis_raw_values(text: str) -> dict[tuple[str, str], str]:
    values: dict[tuple[str, str], str] = {}
    lines = text.splitlines()
    for i, line in enumerate(lines):
        stripped = line.strip()
        axis = stripped[:-1] if stripped.endswith(":") else ""
        if axis not in HEALTH_AXES:
            continue
        section_end = next(
            (
                j
                for j in range(i + 1, len(lines))
                if lines[j].startswith("    ") and not lines[j].startswith("      ") and lines[j].strip().endswith(":")
            ),
            len(lines),
        )
        raw_fields = set(RAW_NUMERIC_FIELDS.get(axis, []))
        for entry in lines[i + 1 : section_end]:
            match = re.match(r"\s*([a-z0-9_]+):\s*([-+]?[0-9][0-9.,]*)\s*$", entry)
            if match and match.group(1) in raw_fields:
                values[(axis, match.group(1))] = yaml_scalar(match.group(2))
    return values


def health_section_heading(page: Path) -> str:
    return "## 健康度与可持续性" if page.name.endswith(ZH_SUFFIX) else "## Health & viability"


def detect_health_prose_grade_drift(page: Path, text: str, root: Path) -> list[Finding]:
    grades = health_axis_grades(text)
    if not grades:
        return []
    findings: list[Finding] = []
    heading = health_section_heading(page)
    for line_no, line in section_lines(text, heading):
        prose_grade = re.search(r"\bGrade\s+([A-E?])\b", line)
        if not prose_grade:
            continue
        for axis, labels in AXIS_LABELS.items():
            if any(label in line for label in labels):
                frontmatter_grade = grades.get(axis)
                if frontmatter_grade and frontmatter_grade != prose_grade.group(1):
                    findings.append(
                        Finding(
                            "health-prose-grade-drift",
                            "high",
                            relpath(page, root),
                            line_no,
                            f"Health prose Grade {prose_grade.group(1)} disagrees with frontmatter {axis} grade {frontmatter_grade}.",
                            line.strip(),
                        )
                    )
                break
    return findings


def numeric_variants(value: str) -> set[str]:
    normalized = value.replace(",", "")
    variants = {value, normalized}
    try:
        number = float(normalized)
    except ValueError:
        return variants
    variants.add(f"{number:.1f}")
    if number.is_integer():
        variants.add(str(int(number)))
        variants.add(f"{int(number):,}")
    if 0 < number < 1:
        percent = number * 100
        variants.add(f"{percent:.1f}")
        variants.add(f"{percent:.1f}%")
        if percent.is_integer():
            variants.add(str(int(percent)))
            variants.add(f"{int(percent)}%")
    return variants


def extract_numbers(line: str) -> set[str]:
    return {match.group(0) for match in re.finditer(r"(?<![A-Za-z])\d[\d,]*(?:\.\d+)?", line)}


def line_mentions_raw_field(line: str, field: str) -> bool:
    lowered = line.lower()
    for trigger in RAW_FIELD_TRIGGERS.get(field, []):
        trigger_lower = trigger.lower()
        if re.search(rf"(?<![a-z0-9]){re.escape(trigger_lower)}(?![a-z0-9])", lowered):
            return True
    return False


def detect_health_prose_raw_drift(page: Path, text: str, root: Path) -> list[Finding]:
    raw_values = health_axis_raw_values(text)
    if not raw_values:
        return []
    findings: list[Finding] = []
    heading = health_section_heading(page)
    for line_no, line in section_lines(text, heading):
        prose_numbers = extract_numbers(line)
        if not prose_numbers:
            continue
        for axis, labels in AXIS_LABELS.items():
            if not any(label in line for label in labels):
                continue
            for field in RAW_NUMERIC_FIELDS.get(axis, []):
                if not line_mentions_raw_field(line, field):
                    continue
                frontmatter_value = raw_values.get((axis, field))
                if not frontmatter_value:
                    continue
                if prose_numbers & numeric_variants(frontmatter_value):
                    continue
                findings.append(
                    Finding(
                        "health-prose-raw-drift",
                        "high",
                        relpath(page, root),
                        line_no,
                        f"Health prose numeric values do not include frontmatter {axis}.{field}={frontmatter_value}.",
                        line.strip(),
                    )
                )
                break
            break
    return findings


def scan(root: Path | str, *, scope_paths: list[Path | str] | tuple[Path | str, ...] | None = None, changed_only: bool = False) -> ScanResult:
    root = Path(root).resolve()
    if scope_paths and changed_only:
        raise ValueError("--scope and --changed-only cannot be combined")
    all_pages = project_pages(root)
    if changed_only:
        pages = changed_project_pages(root)
        scan_mode = "changed-only"
        changed_candidate_count = len(git_changed_markdown_candidates(root))
        rendered_scope_paths: tuple[str, ...] = ()
    elif scope_paths:
        pages = resolve_scope_paths(root, scope_paths)
        scan_mode = "scoped"
        changed_candidate_count = 0
        rendered_scope_paths = tuple(relpath(normalize_scope_path(root, scope), root) for scope in scope_paths)
    else:
        pages = all_pages
        scan_mode = "all"
        changed_candidate_count = 0
        rendered_scope_paths = ()
    findings_dup = detect_duplicated_sections(pages, all_pages, root)
    indexed_targets = {canonical_target(page) for page in all_pages}
    indexed_slug_set = indexed_slugs(all_pages)
    english_canonical_page_count = sum(1 for page in pages if not page.name.endswith(ZH_SUFFIX))
    findings: list[Finding] = list(findings_dup)
    health_unknowns: Counter[tuple[str, str]] = Counter()

    for page in pages:
        text = page.read_text(encoding="utf-8")
        rel = relpath(page, root)
        body = text[body_start(text) :]

        for template in GENERIC_TEMPLATES:
            offset = text.find(template)
            if offset != -1:
                findings.append(
                    Finding("generic-comparison-template", "high", rel, line_number(text, offset), "Generic comparison template prose found.", template)
                )

        offset = text.find(f"default_branch_sha: {ZERO_SHA}")
        if offset != -1:
            findings.append(
                Finding("zero-placeholder-upstream-sha", "medium", rel, line_number(text, offset), "Placeholder zero upstream SHA found.", ZERO_SHA)
            )

        findings.extend(detect_intake_stub(text, rel))
        if page.name.endswith(ZH_SUFFIX):
            findings.extend(detect_zh_lead_not_chinese(text, rel))

        health_unknowns.update(unknown_health_axes(text))
        findings.extend(detect_health_prose_grade_drift(page, text, root))
        findings.extend(detect_health_prose_raw_drift(page, text, root))

        if page.name.endswith(ZH_SUFFIX):
            for match in LINK_RE.finditer(body):
                target = resolve_markdown_target(page, match.group(2))
                if target is None or target.name.endswith(ZH_SUFFIX):
                    continue
                zh_target = target.with_name(f"{base_slug(target.name)}.zh.md")
                if zh_target.exists():
                    findings.append(
                        Finding(
                            "zh-link-to-english-sibling",
                            "medium",
                            rel,
                            line_number(body, match.start()) + line_number(text, body_start(text)) - 1,
                            f"Chinese page links to English target while {zh_target.name} exists.",
                            match.group(0),
                        )
                    )

        heading = "## 横向对比" if page.name.endswith(ZH_SUFFIX) else "## Comparison"
        for line_no, line in section_lines(text, heading):
            if not line.strip().startswith("|") or is_table_separator(line):
                continue
            cells = table_cells(line)
            for fragment in truncation_fragments_in_line(line):
                findings.append(
                    Finding(
                        "truncation-fragment",
                        "high",
                        rel,
                        line_no,
                        "High-confidence truncation fragment found in a comparison row.",
                        fragment,
                    )
                )
            if detects_partly_indexed_composite(page, cells, indexed_targets, indexed_slug_set):
                findings.append(
                    Finding(
                        "composite-alternative-partly-indexed",
                        "high",
                        rel,
                        line_no,
                        "Composite comparison row marks an only-partly indexed alternative as indexed.",
                        line.strip(),
                    )
                )
            status_cell = cells[1] if len(cells) >= 2 else ""
            resolves_to_indexed = row_resolves_to_indexed(page, line, cells, indexed_targets, indexed_slug_set)
            if non_repo_status(status_cell):
                if resolves_to_indexed:
                    findings.append(
                        Finding(
                            "indexed-page-marked-non-repo",
                            "high",
                            rel,
                            line_no,
                            "Comparison row calls an indexed page a non-repo — it has a page, so it is a repository.",
                            line.strip(),
                        )
                    )
                elif legacy_non_repo_status(status_cell):
                    findings.append(
                        Finding(
                            "non-repo-status-legacy-form",
                            "low",
                            rel,
                            line_no,
                            "Combined `未收录（非仓库）` status: use the standalone non-repo status.",
                            line.strip(),
                        )
                    )
            if not any(marker in line for marker in NOT_INDEXED_MARKERS):
                continue
            if (
                resolves_to_indexed
                and any(marker in status_cell for marker in NOT_INDEXED_MARKERS)
                and not any(marker in status_cell for marker in INDEXED_MARKERS)
                and not non_repo_status(status_cell)
            ):
                findings.append(
                    Finding(
                        "indexed-page-marked-not-indexed",
                        "high",
                        rel,
                        line_no,
                        "Comparison row marks an existing indexed page as not indexed.",
                        line.strip(),
                    )
                )

    # Whole-repo mode also audits the category/root INDEX matrices (see audit_summary_matrix_rows).
    # Scoped and changed-only runs stay page-scoped: a scoped run must report only its own pages.
    if scan_mode == "all":
        findings.extend(audit_summary_matrix_rows(root, indexed_targets, indexed_slug_set))

    return ScanResult(
        findings=sorted(findings, key=lambda f: (f.severity, f.category, f.path, f.line, f.evidence)),
        health_unknowns=health_unknowns,
        project_page_count=len(pages),
        english_canonical_page_count=english_canonical_page_count,
        indexed_project_page_count=len(all_pages),
        scan_mode=scan_mode,
        scope_paths=rendered_scope_paths,
        changed_candidate_count=changed_candidate_count,
    )


def render_report(result: ScanResult, root: Path | str) -> str:
    root = Path(root).resolve()
    severity_counts = Counter(f.severity for f in result.findings)
    category_counts = Counter(f.category for f in result.findings)
    zero_sha_count = category_counts.get("zero-placeholder-upstream-sha", 0)
    zero_sha_english_count = sum(1 for f in result.findings if f.category == "zero-placeholder-upstream-sha" and not f.path.endswith(ZH_SUFFIX))
    lines = [
        "# oss-atlas quality scan report",
        "",
        "Mode: report-only. Deterministic findings are triage signals, not full semantic approval.",
        "Count scope: deterministic finding counts are page-level over English canonical pages plus Chinese mirrors unless explicitly labeled otherwise.",
        "Truncation fragments are high-confidence only: comparison-row hits with non-alphanumeric boundaries around the sampled fragment.",
        f"Root: `{root}`",
        f"Scan mode: {result.scan_mode}",
        f"Scope paths: {', '.join(f'`{path}`' for path in result.scope_paths) if result.scope_paths else '(none)' }",
        f"Changed markdown candidates: {result.changed_candidate_count}",
        f"Project pages scanned: {result.project_page_count}",
        f"English canonical pages scanned: {result.english_canonical_page_count}",
        f"Whole-repo indexed project page universe: {result.indexed_project_page_count}",
        "",
        "## Summary counts",
        "",
        "### By severity",
        "",
    ]
    for severity in ("high", "medium", "low"):
        lines.append(f"- {severity}: {severity_counts.get(severity, 0)}")
    lines += ["", "### By category", ""]
    for category in KNOWN_CATEGORIES:
        lines.append(f"- {category}: {category_counts[category]}")
    stub_pages = sum(1 for f in result.findings if f.category.startswith("intake-stub-page") and not f.path.endswith(ZH_SUFFIX))
    lines += [
        "",
        f"Intake-stub backlog: {stub_pages}/{result.english_canonical_page_count} English canonical pages "
        f"still carry batch-intake placeholder judgment (report-only; each becomes an ERROR once its "
        f"last_verified reaches {STUB_BLOCKED_FROM} — re-verifying a page is when the prose must be rewritten).",
        "",
        f"Zero placeholder upstream SHA count (page-level): {zero_sha_count}",
        f"Zero placeholder upstream SHA count (English canonical): {zero_sha_english_count}",
        "",
        "## Deterministic findings",
        "",
    ]
    if not result.findings:
        lines.append("No deterministic findings.")
    else:
        for finding in result.findings:
            lines.append(f"- [{finding.severity}] `{finding.category}` {finding.path}:{finding.line} — {finding.message} Evidence: `{finding.evidence}`")
    lines += [
        "",
        "## Health ? distribution",
        "",
        "Count scope: page-level over English canonical pages plus Chinese mirrors; divide by mirror parity only after confirming frontmatter parity.",
        "",
        "| Axis | Reason | Page-level count |",
        "|---|---|---:|",
    ]
    if result.health_unknowns:
        for (axis, reason), count in sorted(result.health_unknowns.items()):
            lines.append(f"| {axis} | {reason} | {count} |")
    else:
        lines.append("| (none) | (none) | 0 |")
    lines += [
        "",
        "## Reviewer-only dimensions",
        "",
        "These dimensions are not hard failures and are not scanner approval. A reviewer must still inspect them semantically:",
        "",
        "- reviewer-only: weak or non-second-person `When to use` signals.",
        "- reviewer-only: `Comparison` rows lacking an obvious decisive tradeoff.",
        "- reviewer-only: Caveats sections that may be too thin for inferred or unverified prose.",
        "- reviewer-only: Chinese monolingual mirror quality beyond link targets.",
        "",
    ]
    return "\n".join(lines)


def has_gated_findings(result: ScanResult) -> bool:
    return any(finding.category in GATED_DETERMINISTIC_CATEGORIES for finding in result.findings)


def main() -> int:
    parser = argparse.ArgumentParser(description="Report deterministic oss-atlas quality signals.")
    parser.add_argument("--root", default=".", help="Repository root to scan.")
    parser.add_argument("--report", help="Optional Markdown report path to write.")
    parser.add_argument("--scope", action="append", default=[], help="Project page file or directory to scan. Repeatable.")
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Scan existing changed project pages from git HEAD: staged, unstaged, untracked, and rename destinations; deleted paths are excluded.",
    )
    parser.add_argument(
        "--fail-on-any-scoped",
        action="store_true",
        help="Exit non-zero for scoped or changed-only scans with gated deterministic findings.",
    )
    parser.add_argument(
        "--fail-on-gated",
        action="store_true",
        help="Exit non-zero when any gated deterministic category has findings, in any mode "
        "(including a whole-repo scan) — the CI gate.",
    )
    args = parser.parse_args()

    if args.scope and args.changed_only:
        parser.error("--scope and --changed-only cannot be combined")
    if args.fail_on_any_scoped and not (args.scope or args.changed_only):
        parser.error("--fail-on-any-scoped requires --scope or --changed-only")

    root = Path(args.root).resolve()
    result = scan(root, scope_paths=args.scope, changed_only=args.changed_only)
    report = render_report(result, root)
    if args.report:
        report_path = Path(args.report)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(report, encoding="utf-8")
    print(report)
    if (args.fail_on_any_scoped or args.fail_on_gated) and has_gated_findings(result):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
