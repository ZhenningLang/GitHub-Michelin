#!/usr/bin/env python3
"""Deterministic reverse index and unindexed-mention backlog for oss-atlas.

The atlas has no repo -> page reverse index: page slugs come from a project's
display name, which does not always match its repository (for example
`funtool.md` points at `cixingguangming55555/wechat-bot`). So "is this repo
indexed?" is a manual grep over every page, and a `未收录` label can silently
outlive the thing it describes.

This tool builds the missing index and a regenerable backlog of alternatives
that pages name but do not index. It is offline and deterministic: no network,
stable sort order, no timestamps in the output, so `--check` can diff exactly.

Scan scope is the English tree, project pages AND category INDEX files. INDEX
files are included on purpose: `tools/quality_scan.py` only reads project pages,
so a stale `未收录` row in a category INDEX is invisible to that gate.

Two severities are reported, because they are different bugs:

* `full`     - every alternative named in the row is already indexed, so the
               whole `未收录` row is false. This fails `--check`.
* `partial`  - a composite "and others" row mixes indexed and unindexed names.
               The indexed names should be removed from the row, but the label
               is not wholly false. Reported and tracked, not a hard failure.

Modes:
  (default)   dry run: print a summary, write nothing
  --write     write reports/repo-page-index.csv,
              reports/unindexed-project-mentions.csv and
              reports/project-intake-backlog.md
  --check     exit non-zero when committed reports are stale, or when a `full`
              mislabel exists
"""
from __future__ import annotations

import argparse
import csv
import io
import re
from dataclasses import dataclass
from pathlib import Path

REPO_INDEX_PATH = "reports/repo-page-index.csv"
UNINDEXED_PATH = "reports/unindexed-project-mentions.csv"
BACKLOG_PATH = "reports/project-intake-backlog.md"
NOT_INDEXED_MARKERS = ("未收录", "not indexed")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MIN_PLAIN_SLUG_LENGTH = 7
BACKLOG_TOP_N = 30


@dataclass(frozen=True)
class Page:
    path: Path
    slug: str
    category: str
    repo: str
    is_index: bool


@dataclass(frozen=True)
class Mention:
    alternative: str
    first_page: str
    indexed_hits: tuple[str, ...]
    all_indexed: bool

    @property
    def partly_indexed(self) -> bool:
        return bool(self.indexed_hits) and not self.all_indexed


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fields: dict[str, str] = {}
    for line in text[3:end].splitlines():
        if not line or line[0] in " \t#":
            continue
        key, sep, value = line.partition(":")
        if not sep:
            continue
        fields[key.strip()] = value.strip().strip('"\'')
    return fields


def slugify(label: str) -> str:
    plain = re.sub(r"`([^`]+)`", r"\1", label).strip()
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain).strip()
    plain = re.sub(r"\([^)]*\)", "", plain).strip()
    plain = re.sub(r"（[^）]*）", "", plain).strip()
    plain = plain.lower().replace("_", "-")
    return re.sub(r"[^a-z0-9]+", "-", plain).strip("-")


def alternative_names(cell: str) -> list[str]:
    plain = re.sub(r"`([^`]+)`", r"\1", cell).strip()
    plain = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", plain).strip()
    names: list[str] = []
    for comma_part in re.split(r"\s*[,，;；]\s*", plain):
        names.extend(piece.strip() for piece in re.split(r"\s+/\s+", comma_part) if piece.strip())
    return names or ([plain] if plain else [])


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


def is_project_page(path: Path) -> bool:
    return path.suffix == ".md" and path.name not in {"INDEX.md", "INDEX.zh.md"}


def english_markdown(root: Path) -> list[Path]:
    categories = root / "categories"
    if not categories.exists():
        return []
    return sorted(path for path in categories.rglob("*.md") if not path.name.endswith(".zh.md"))


def load_pages(root: Path) -> list[Page]:
    pages: list[Page] = []
    for path in english_markdown(root):
        text = path.read_text(encoding="utf-8")
        is_index = path.name == "INDEX.md"
        fields = parse_frontmatter(text)
        pages.append(
            Page(
                path=path,
                slug="" if is_index else path.name[: -len(".md")],
                category=path.parent.name,
                repo=fields.get("repo", ""),
                is_index=is_index,
            )
        )
    return pages


def relpath(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def repo_index_rows(root: Path, pages: list[Page]) -> list[list[str]]:
    rows: list[list[str]] = []
    for page in sorted(pages, key=lambda p: (p.repo, p.slug)):
        if page.is_index or not page.repo:
            continue
        rows.append([page.repo, page.slug, page.category, relpath(page.path, root)])
    return rows


def scan_mentions(root: Path, pages: list[Page], indexed_slugs: set[str]) -> list[Mention]:
    first_seen: dict[str, Mention] = {}
    for page in pages:
        text = page.path.read_text(encoding="utf-8")
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped.startswith("|") or is_table_separator(stripped):
                continue
            cells = table_cells(stripped)
            if len(cells) < 2:
                continue
            if not any(marker in cells[1] for marker in NOT_INDEXED_MARKERS):
                continue
            alternative = cells[0]
            if not alternative:
                continue
            parts = alternative_names(alternative)
            part_slugs = [slugify(name) for name in parts]
            part_slugs = [slug for slug in part_slugs if slug]
            hits = tuple(sorted(slug for slug in set(part_slugs) if len(slug) >= MIN_PLAIN_SLUG_LENGTH and slug in indexed_slugs))
            all_indexed = (
                bool(part_slugs)
                and len(part_slugs) == len(parts)
                and all(len(slug) >= MIN_PLAIN_SLUG_LENGTH and slug in indexed_slugs for slug in part_slugs)
            )
            mention = Mention(
                alternative=alternative,
                first_page=relpath(page.path, root),
                indexed_hits=hits,
                all_indexed=all_indexed,
            )
            existing = first_seen.get(alternative)
            if existing is None or (len(existing.indexed_hits) < len(hits)):
                first_seen[alternative] = mention
    return sorted(first_seen.values(), key=lambda m: (m.alternative.lower(), m.alternative))


def render_repo_index(rows: list[list[str]]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["repo", "slug", "category", "page"])
    writer.writerows(rows)
    return buffer.getvalue()


def render_unindexed(mentions: list[Mention]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(["alternative", "first_page", "indexed_hits", "resolves_to_indexed"])
    for mention in mentions:
        if mention.all_indexed:
            status = "full"
        elif mention.partly_indexed:
            status = "partial"
        else:
            status = "no"
        writer.writerow([mention.alternative, mention.first_page, ";".join(mention.indexed_hits), status])
    return buffer.getvalue()


def render_backlog(mentions: list[Mention]) -> str:
    full = [m for m in mentions if m.all_indexed]
    partial = [m for m in mentions if m.partly_indexed]
    lines = [
        "# Project Intake Backlog",
        "",
        "Generated by `tools/reverse_index.py --write`. Do not edit by hand;",
        "regenerate after comparison tables change and commit the diff.",
        "",
        "This is a maintainer backlog, not a canonical selection page and not a",
        "claim that a candidate is verified. Alternatives here are named by pages",
        "as `未收录`; nothing else about them is asserted.",
        "",
        "## Summary",
        "",
        f"- Named-but-unindexed alternatives: {len(mentions)}",
        f"- `full` mislabels (whole row indexed but marked 未收录, must be 0): {len(full)}",
        f"- `partial` rows (mixed indexed/unindexed, clean up the indexed names): {len(partial)}",
        f"- Raw machine list: `{UNINDEXED_PATH}`",
        f"- Repo -> page reverse index: `{REPO_INDEX_PATH}`",
        "",
    ]
    if full:
        lines += [
            "## Full mislabels",
            "",
            "Every alternative named in these rows already has a page, so the row is false.",
            "",
            "| Alternative | First page |",
            "|---|---|",
        ]
        lines += [f"| {m.alternative} | `{m.first_page}` |" for m in full]
        lines.append("")
    if partial:
        lines += [
            "## Partly-indexed rows",
            "",
            "These composite rows name at least one alternative that already has a page.",
            "Remove the indexed names from the row, or split the row.",
            "",
            "| Alternative | Indexed names | First page |",
            "|---|---|---|",
        ]
        lines += [f"| {m.alternative} | {', '.join(m.indexed_hits)} | `{m.first_page}` |" for m in partial]
        lines.append("")
    lines += [
        f"## Top {BACKLOG_TOP_N} named alternatives",
        "",
        "| Alternative | First page |",
        "|---|---|",
    ]
    lines += [f"| {m.alternative} | `{m.first_page}` |" for m in mentions[:BACKLOG_TOP_N]]
    lines.append("")
    return "\n".join(lines)


def compute(root: Path) -> tuple[list[list[str]], list[Mention], dict[str, str]]:
    pages = load_pages(root)
    indexed_slugs = {page.slug for page in pages if not page.is_index and page.slug}
    mentions = scan_mentions(root, pages, indexed_slugs)
    repo_rows = repo_index_rows(root, pages)
    return repo_rows, mentions, {
        REPO_INDEX_PATH: render_repo_index(repo_rows),
        UNINDEXED_PATH: render_unindexed(mentions),
        BACKLOG_PATH: render_backlog(mentions),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the oss-atlas reverse index and unindexed-mention backlog.")
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--write", action="store_true", help="Write the reports.")
    parser.add_argument("--check", action="store_true", help="Fail if committed reports are stale or a full mislabel exists.")
    args = parser.parse_args()
    if args.write and args.check:
        parser.error("--write and --check cannot be combined")

    root = Path(args.root).resolve()
    repo_rows, mentions, rendered = compute(root)
    full = [m for m in mentions if m.all_indexed]
    partial = [m for m in mentions if m.partly_indexed]

    if args.check:
        problems: list[str] = []
        for relative, content in rendered.items():
            committed = root / relative
            if not committed.exists():
                problems.append(f"missing committed report: {relative}")
            elif committed.read_text(encoding="utf-8") != content:
                problems.append(f"stale committed report: {relative} (run tools/reverse_index.py --write)")
        if full:
            problems.append(
                f"{len(full)} row(s) mark a fully-indexed set of names as not-indexed: "
                + ", ".join(sorted(m.alternative for m in full))
            )
        if problems:
            for problem in problems:
                print(f"FAIL {problem}")
            return 1
        print(
            "reverse_index check: reports are current, no full mislabels"
            f" ({len(partial)} partly-indexed rows tracked in {BACKLOG_PATH})"
        )
        return 0

    print(f"repo -> page entries: {len(repo_rows)}")
    print(f"named-but-unindexed alternatives: {len(mentions)}")
    print(f"full mislabels (blocking, must be 0): {len(full)}")
    print(f"partly-indexed rows (tracked): {len(partial)}")
    for mention in partial:
        print(f"  partial: {mention.first_page} :: {mention.alternative} -> {', '.join(mention.indexed_hits)}")
    if args.write:
        for relative, content in rendered.items():
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            print(f"wrote {relative}")
    else:
        print("dry run: pass --write to update reports, --check to verify them")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
