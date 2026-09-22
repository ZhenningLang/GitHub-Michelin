#!/usr/bin/env python3
"""oss-atlas intake sweep — drain the `未收录` backlog one item at a time.

The repo already has discovery (`tools/harvest.py`) and a per-item authoring contract
(`.claude/skills/add-project/SKILL.md`), but nothing that walks the backlog and hands one
item at a time to a worker. This is that missing hand-off executor.

Division of labour — the program is deterministic and the judgment is not:

  build     read the scope (default: the category comparison matrices) and write a queue
  classify  ask GitHub whether each name is a real repository, and store the evidence
  next      print the next actionable item plus its worker brief (what a subagent receives)
  record    write one item's outcome (done / non-repo / alias / failed) into the ledger
  status    progress summary for the wave

The ledger (`intake/<wave>/ledger.jsonl`) is the resume state: a re-run never repeats a
terminal item, so a sweep can stop and continue across sessions.

Vocabulary is `tools/schema.md` §2: 未收录 = a real repository we have not added yet (debt);
非仓库 / not a repo = not a repository at all (out of scope by shape, no debt).

Usage:
  python3 tools/intake_sweep.py build --wave 1
  python3 tools/intake_sweep.py classify --wave 1 [--limit 40]
  python3 tools/intake_sweep.py next --wave 1
  python3 tools/intake_sweep.py record --wave 1 --id gsap --status done --evidence "…"
  python3 tools/intake_sweep.py status --wave 1

Requires: Python 3.9+ (stdlib only). GitHub auth via GITHUB_TOKEN or GH_TOKEN.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MATRIX_HEADINGS = ("## Comparison matrix", "## 对比矩阵")
NOT_INDEXED_MARKERS = ("未收录", "not indexed")
NON_REPO_MARKERS = ("非仓库", "not a repository", "not a repo", "non-repo")
INDEXED_MARKERS = ("✅", "已收录")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
# Rows that are placeholders rather than named alternatives: "Other downloaders", "各页点到的替代品".
PLACEHOLDER_RE = re.compile(
    r"named across the pages|各页对比里点到的|各页里点到的|other\b|其他|more-active forks|更活跃的分叉|"
    r"alternatives named|替代品\)|\(alternatives",
    re.IGNORECASE,
)
SEARCH_URL = "https://api.github.com/search/repositories"
THROTTLE_SECONDS = float(os.environ.get("OSS_ATLAS_SWEEP_THROTTLE", "2.0"))

TERMINAL_STATUSES = {"done", "non_repo", "alias", "failed", "skipped_placeholder"}


@dataclass
class Item:
    id: str
    name: str
    row: str
    target_category: str
    sources: list[str]
    status: str = "todo"
    reason: str = ""
    repo: str = ""
    stars: int = 0
    license: str = ""
    pushed_at: str = ""
    archived: bool = False
    html_url: str = ""
    confidence: str = ""
    evidence: list[str] = field(default_factory=list)
    worker: str = ""
    detail: str = ""


def slugify(text: str) -> str:
    plain = re.sub(r"`([^`]+)`", r"\1", text).strip()
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain).strip()
    plain = re.sub(r"\([^)]*\)|（[^）]*）", "", plain).strip()
    plain = plain.split(":", 1)[0]
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")


def indexed_slugs(root: Path) -> set[str]:
    return {p.name[: -len(".zh.md")] if p.name.endswith(".zh.md") else p.stem
            for p in (root / "categories").rglob("*.md")
            if p.name not in {"INDEX.md", "INDEX.zh.md"}}


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


def split_names(cell: str) -> list[str]:
    """Alternative cell -> candidate names. Composite rows list several, separated by / or 、."""
    plain = re.sub(r"`([^`]+)`", r"\1", cell)
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain)
    parts: list[str] = []
    for chunk in re.split(r"\s*[/、]\s*", plain):
        chunk = chunk.strip(" 　·-—")
        if chunk:
            parts.append(chunk)
    return parts


def scope_rows(root: Path, scope: str) -> list[tuple[Path, int, str]]:
    """Rows to sweep. `matrix` = comparison matrices in category INDEX files (wave 1 default)."""
    rows: list[tuple[Path, int, str]] = []
    if scope == "matrix":
        for index in sorted(root.glob("categories/**/INDEX.md")):
            lines = index.read_text(encoding="utf-8").splitlines()
            headings = [i for i, line in enumerate(lines) if line.strip() in MATRIX_HEADINGS]
            for start in headings:
                for i in range(start + 1, len(lines)):
                    if re.match(r"^##[ \t]+\S", lines[i]):
                        break
                    line = lines[i].strip()
                    if not line.startswith("|") or is_table_separator(line):
                        continue
                    cells = table_cells(line)
                    if len(cells) < 2 or not any(m in cells[1] for m in NOT_INDEXED_MARKERS):
                        continue
                    rows.append((index, i + 1, line))
    elif scope == "pages":
        for page in sorted(root.glob("categories/**/*.md")):
            if page.name in {"INDEX.md", "INDEX.zh.md"} or page.name.endswith(".zh.md"):
                continue
            lines = page.read_text(encoding="utf-8").splitlines()
            for i, line in enumerate(lines):
                stripped = line.strip()
                if not stripped.startswith("|") or is_table_separator(stripped):
                    continue
                cells = table_cells(stripped)
                if len(cells) < 2 or not any(m in cells[1] for m in NOT_INDEXED_MARKERS):
                    continue
                rows.append((page, i + 1, stripped))
    else:
        raise ValueError(f"unknown scope: {scope}")
    return rows


def build_items(root: Path, scope: str) -> tuple[list[Item], list[str]]:
    slugs = indexed_slugs(root)
    items: dict[str, Item] = {}
    notes: list[str] = []
    for path, line_no, row in scope_rows(root, scope):
        cells = table_cells(row)
        status = cells[1]
        names = split_names(cells[0])
        if not names or PLACEHOLDER_RE.search(cells[0]):
            notes.append(f"placeholder row skipped: {path.relative_to(root)}:{line_no}")
            continue
        non_repo_row = any(m in status for m in NON_REPO_MARKERS)
        for name in names:
            slug = slugify(name)
            if not slug:
                continue
            if slug in slugs:
                notes.append(f"alias of an indexed page, fix the row status instead: {name} ({path.relative_to(root)}:{line_no})")
                continue
            item = items.get(slug)
            source = f"{path.relative_to(root).as_posix()}:{line_no}"
            if item is None:
                item = Item(
                    id=slug,
                    name=name,
                    row=row,
                    target_category=path.parent.name,
                    sources=[source],
                    status="non_repo" if non_repo_row else "todo",
                    reason="row already marked 非仓库" if non_repo_row else "",
                )
                items[slug] = item
            elif source not in item.sources:
                item.sources.append(source)
    return sorted(items.values(), key=lambda item: item.id), notes


def ledger_path(root: Path, wave: str) -> Path:
    return root / "intake" / f"wave-{wave}" / "ledger.jsonl"


def load_ledger(root: Path, wave: str) -> dict[str, Item]:
    path = ledger_path(root, wave)
    if not path.exists():
        return {}
    items: dict[str, Item] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        record = json.loads(line)
        record["sources"] = list(record.get("sources") or [])
        record["evidence"] = list(record.get("evidence") or [])
        items[record["id"]] = Item(**record)
    return items


def save_ledger(root: Path, wave: str, items: dict[str, Item]) -> None:
    path = ledger_path(root, wave)
    path.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(items.values(), key=lambda item: item.id)
    path.write_text(
        "".join(json.dumps(asdict(item), ensure_ascii=False, sort_keys=True) + "\n" for item in ordered),
        encoding="utf-8",
    )


def github_json(url: str, token: str, *, attempts: int = 3) -> dict:
    request = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "oss-atlas-intake-sweep",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code in (403, 429) and attempt < attempts - 1:
                time.sleep(20 * (attempt + 1))
                continue
            raise
    raise RuntimeError("unreachable")


def search_match(name: str, payload: dict) -> tuple[dict | None, str]:
    """Best candidate for a name plus how strong the match is.

    Returns (repo, confidence) where confidence is:
      `exact`  — the slugified name equals the slugified repo name (rq -> rq/rq)
      `likely` — the name appears inside owner/name (Nextcloud -> nextcloud/server,
                 PaddleOCR -> PaddlePaddle/PaddleOCR)
      `weak`   — some repo merely starts with the name; a name search is not an identity check
      `none`   — nothing plausible

    The worker still confirms: `kepano/obsidian-skills` matching "Obsidian" is a `likely` hit for a
    *closed* note app, and a name-level search cannot tell the difference. That is why the brief
    requires the worker to verify before authoring.
    """
    want = slugify(name)
    if not want:
        return None, "none"
    weak: dict | None = None
    for repo in payload.get("items") or []:
        name_slug = slugify(repo.get("name", ""))
        owner_slug = slugify((repo.get("full_name") or "/").split("/")[0])
        if name_slug == want:
            return repo, "exact"
        if owner_slug == want:
            return repo, "likely"
        if name_slug.startswith(f"{want}-") or want.startswith(f"{name_slug}-"):
            weak = weak or repo
    if weak is not None:
        return weak, "weak"
    return None, "none"


def classify_items(root: Path, wave: str, limit: int | None, offline: bool = False, refresh: bool = False) -> int:
    items = load_ledger(root, wave)
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or ""
    if not token and not offline:
        print("WARN no GITHUB_TOKEN/GH_TOKEN: running against the unauthenticated limit", file=sys.stderr)
    if refresh:
        for item in items.values():
            item.repo = item.detail = item.confidence = ""
            item.stars = 0
            item.license = item.pushed_at = item.html_url = ""
            item.archived = False
    pending = [item for item in items.values() if item.status == "todo" and not item.repo and not item.detail]
    if limit is not None:
        pending = pending[:limit]
    for index, item in enumerate(pending):
        if offline:
            break
        query = urllib.parse.urlencode({"q": f"{item.name} in:name", "sort": "stars", "per_page": 5})
        try:
            payload = github_json(f"{SEARCH_URL}?{query}", token)
        except Exception as error:  # noqa: BLE001 — the sweep records the failure and continues
            item.detail = f"search failed: {error}"
            item.evidence.append(item.detail)
            continue
        match, confidence = search_match(item.name, payload)
        item.confidence = confidence
        if match is None:
            item.detail = "no repository matched the name"
            item.evidence.append(f"GitHub search for {item.name!r}: no plausible match")
        else:
            item.repo = match.get("full_name", "")
            item.stars = int(match.get("stargazers_count") or 0)
            item.license = ((match.get("license") or {}).get("spdx_id") or "") or ""
            item.pushed_at = (match.get("pushed_at") or "")[:10]
            item.archived = bool(match.get("archived"))
            item.html_url = match.get("html_url", "")
            item.detail = f"repository candidate ({confidence} name match)"
            item.evidence.append(
                f"GitHub search: {item.repo} stars={item.stars} pushed={item.pushed_at} match={confidence}"
            )
        save_ledger(root, wave, items)
        if index + 1 < len(pending):
            time.sleep(THROTTLE_SECONDS)
    save_ledger(root, wave, items)
    return len(pending)


def worker_brief(item: Item, root: Path) -> str:
    state = "REAL REPOSITORY (candidate for 收录)" if item.repo else "NO REPOSITORY FOUND (likely 非仓库)"
    return f"""# intake sweep — item {item.id}

Name: {item.name}
State: {state}
Confidence: {item.confidence or 'unclassified'} — a name search is not an identity check; verify the repo is the thing the row means before authoring.
Evidence: {'; '.join(item.evidence) or 'none yet'}
Repo: {item.repo or '—'} stars={item.stars} license={item.license or '—'} pushed={item.pushed_at or '—'} archived={item.archived}
Named by: {', '.join(item.sources)}
Target category: categories/{item.target_category}/
Row: {item.row}

## Do exactly one of these two things

A. It is a real repository -> author the entry per `.claude/skills/add-project/SKILL.md` and
   `tools/schema.md`: bilingual page pair under `categories/{item.target_category}/`, a
   `flows/<slug>.json` backbone with its card, upstream snapshot + health block, then wire the
   category INDEX.md / INDEX.zh.md and README.md / README.zh.md, then run the gates.

B. It is not a repository (hosted SaaS, closed app, paid service, article, not a project) ->
   do NOT create a page. Change that row's status in the source table(s) to `非仓库` /
   `not a repo` (schema §2) and put the reason in the tradeoff cell. That is a complete item.

Scope limits: fix only the rows named above; the 3-5 direct substitutes you name in a new page
keep `未收录` if they lack pages (they go into the next wave, not this one). Report back with the
files you changed, the evidence for the decision, and the gate output.
"""


def command_build(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    items, notes = build_items(root, args.scope)
    ledger = load_ledger(root, args.wave)
    added = 0
    for item in items:
        if item.id not in ledger:
            ledger[item.id] = item
            added += 1
        else:
            ledger[item.id].sources = sorted(set(ledger[item.id].sources) | set(item.sources))
    save_ledger(root, args.wave, ledger)
    print(f"wave {args.wave}: {len(items)} named candidates in scope ({args.scope}), {added} new, {len(ledger)} in ledger")
    for note in notes:
        print(f"  note: {note}")
    counts: dict[str, int] = {}
    for item in ledger.values():
        counts[item.status] = counts.get(item.status, 0) + 1
    print("  status: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


def command_classify(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    count = classify_items(root, args.wave, args.limit, offline=args.offline, refresh=args.refresh)
    ledger = load_ledger(root, args.wave)
    found = sum(1 for item in ledger.values() if item.repo)
    missing = sum(1 for item in ledger.values() if item.status == "todo" and not item.repo and item.detail)
    print(f"classified {count} item(s); ledger: {len(ledger)} total, {found} with a repository, {missing} with no match")
    return 0


def command_next(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    ledger = load_ledger(root, args.wave)
    pending = [item for item in ledger.values() if item.status == "todo"]
    if args.only:
        pending = [item for item in pending if item.id == args.only]
    if not pending:
        print("no actionable item: queue is empty (run build) or everything reached a terminal status")
        return 0
    print(worker_brief(pending[0], root))
    return 0


def command_record(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    ledger = load_ledger(root, args.wave)
    item = ledger.get(args.id)
    if item is None:
        print(f"unknown item id: {args.id}", file=sys.stderr)
        return 1
    if args.status not in TERMINAL_STATUSES:
        print(f"status must be one of {sorted(TERMINAL_STATUSES)}", file=sys.stderr)
        return 1
    item.status = args.status
    if args.reason:
        item.reason = args.reason
    if args.evidence:
        item.evidence.append(args.evidence)
    if args.worker:
        item.worker = args.worker
    if args.detail:
        item.detail = args.detail
    save_ledger(root, args.wave, ledger)
    print(f"recorded {item.id} -> {item.status}")
    return 0


def command_status(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    ledger = load_ledger(root, args.wave)
    if not ledger:
        print(f"wave {args.wave}: empty ledger (run build)")
        return 0
    counts: dict[str, int] = {}
    for item in ledger.values():
        counts[item.status] = counts.get(item.status, 0) + 1
    print(f"wave {args.wave}: {len(ledger)} items")
    for status, count in sorted(counts.items()):
        print(f"  {status}: {count}")
    actionable = sorted(item.id for item in ledger.values() if item.status == "todo")
    if actionable:
        print(f"  actionable ({len(actionable)}): {', '.join(actionable[:12])}{' …' if len(actionable) > 12 else ''}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=str(ROOT))
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build", help="write the queue from a scope")
    build.add_argument("--wave", default="1")
    build.add_argument("--scope", default="matrix", choices=["matrix", "pages"])
    build.set_defaults(func=command_build)

    classify = sub.add_parser("classify", help="ask GitHub whether each name is a repository")
    classify.add_argument("--wave", default="1")
    classify.add_argument("--limit", type=int, default=None)
    classify.add_argument("--offline", action="store_true", help="do not call the API (dry check of the queue)")
    classify.add_argument("--refresh", action="store_true", help="re-query every todo item (drops cached matches)")
    classify.set_defaults(func=command_classify)

    nxt = sub.add_parser("next", help="print the next actionable item and its worker brief")
    nxt.add_argument("--wave", default="1")
    nxt.add_argument("--only", default=None)
    nxt.set_defaults(func=command_next)

    record = sub.add_parser("record", help="write an item's outcome into the ledger")
    record.add_argument("--wave", default="1")
    record.add_argument("--id", required=True)
    record.add_argument("--status", required=True)
    record.add_argument("--reason", default="")
    record.add_argument("--evidence", default="")
    record.add_argument("--worker", default="")
    record.add_argument("--detail", default="")
    record.set_defaults(func=command_record)

    status = sub.add_parser("status", help="progress summary")
    status.add_argument("--wave", default="1")
    status.set_defaults(func=command_status)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
