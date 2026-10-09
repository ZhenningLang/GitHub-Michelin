#!/usr/bin/env python3
"""Maintain the cheap upstream-change snapshot used by sync-entry.

Dry-run by default; writes only with --apply --yes. The snapshot is intentionally tiny and
GitHub-specific because every indexed page is a GitHub repo today.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
ZH_SUFFIX = ".zh.md"


def frontmatter_bounds(text: str) -> tuple[int, int] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    return 3, end


def parse_frontmatter(text: str) -> dict[str, str]:
    bounds = frontmatter_bounds(text)
    if bounds is None:
        return {}
    start, end = bounds
    data: dict[str, str] = {}
    for line in text[start:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        key, _, raw = line.partition(":")
        data[key.strip()] = raw.strip().strip('"').strip("'")
    return data


def parse_upstream(text: str) -> dict[str, object] | None:
    bounds = frontmatter_bounds(text)
    if bounds is None:
        return None
    start, end = bounds
    fm = text[start:end]
    m = re.search(r"(?ms)^upstream:\n(.*?)(?=^[A-Za-z_][A-Za-z0-9_-]*:\s*$|\Z)", fm)
    if not m:
        return None
    data: dict[str, object] = {}
    for line in m.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        val = raw.strip().strip('"').strip("'")
        data[key] = (val == "true") if key == "archived" else val
    return data


def repo_url_to_owner_name(url: str) -> str | None:
    m = re.search(r"github\.com[/:]([^/]+)/([^/#?]+?)(?:\.git)?/?$", url.strip())
    if not m:
        return None
    return f"{m.group(1)}/{m.group(2)}"


def discover_pages(root: Path) -> list[Path]:
    return sorted(
        p for p in (root / "categories").rglob("*.md")
        if not p.name.startswith("INDEX") and not p.name.endswith(ZH_SUFFIX)
    )


def zh_sibling(page: Path) -> Path:
    return page.with_name(page.stem + ZH_SUFFIX)


def fetch_snapshot(owner_name: str) -> dict[str, object]:
    cmd = [
        "gh", "api", f"repos/{owner_name}",
        "--jq", "{pushed_at,default_branch,archived}",
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"gh api failed for {owner_name}")
    meta = json.loads(proc.stdout)
    branch = meta.get("default_branch")
    if not branch:
        raise RuntimeError(f"missing default_branch for {owner_name}")
    proc = subprocess.run(
        ["gh", "api", f"repos/{owner_name}/commits/{branch}", "--jq", ".sha"],
        capture_output=True, text=True, timeout=60,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or f"commit lookup failed for {owner_name}")
    sha = proc.stdout.strip().strip('"')
    if not sha:
        raise RuntimeError(f"missing default branch sha for {owner_name}")
    return {
        "pushed_at": meta.get("pushed_at"),
        "default_branch": branch,
        "default_branch_sha": sha,
        "archived": bool(meta.get("archived")),
    }


def render_block(snapshot: dict[str, object]) -> str:
    archived = "true" if snapshot["archived"] else "false"
    return (
        "upstream:\n"
        f"  pushed_at: {snapshot['pushed_at']}\n"
        f"  default_branch: {snapshot['default_branch']}\n"
        f"  default_branch_sha: {snapshot['default_branch_sha']}\n"
        f"  archived: {archived}\n"
    )


def upsert_snapshot(text: str, snapshot: dict[str, object]) -> tuple[str, bool]:
    bounds = frontmatter_bounds(text)
    if bounds is None:
        raise ValueError("missing frontmatter")
    start, end = bounds
    fm = text[start:end].lstrip("\n")
    block = render_block(snapshot)
    pattern = re.compile(r"(?ms)^upstream:\n(?:^  [^\n]*\n?)+")
    if pattern.search(fm):
        new_fm = pattern.sub(block, fm, count=1)
    else:
        marker = re.search(r"(?m)^health:\s*$", fm)
        insert_at = marker.start() if marker else len(fm)
        prefix = fm[:insert_at].rstrip("\n") + "\n"
        suffix = fm[insert_at:].lstrip("\n")
        new_fm = prefix + block + suffix
    new_text = text[:start] + "\n" + new_fm.rstrip("\n") + text[end:]
    return new_text, new_text != text


def compare_snapshot(page: Path, root: Path) -> bool:
    fm = parse_frontmatter(page.read_text(encoding="utf-8"))
    owner_name = repo_url_to_owner_name(fm.get("repo", ""))
    if not owner_name:
        raise RuntimeError(f"could not parse GitHub repo from {page}")
    old = parse_upstream(page.read_text(encoding="utf-8"))
    new = fetch_snapshot(owner_name)
    changed = old != new
    print(f"{'changed_upstream' if changed else 'unchanged_upstream'} {page.relative_to(root)} {owner_name}")
    return changed


def process_page(page: Path, root: Path, apply: bool) -> bool:
    fm = parse_frontmatter(page.read_text(encoding="utf-8"))
    owner_name = repo_url_to_owner_name(fm.get("repo", ""))
    if not owner_name:
        raise RuntimeError(f"could not parse GitHub repo from {page}")
    snapshot = fetch_snapshot(owner_name)
    changed = False
    for target in (page, zh_sibling(page)):
        text = target.read_text(encoding="utf-8")
        new_text, did_change = upsert_snapshot(text, snapshot)
        changed = changed or did_change
        if apply and did_change:
            target.write_text(new_text, encoding="utf-8")
    print(f"{'updated' if changed else 'unchanged'} {page.relative_to(root)} {owner_name}")
    return changed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--page", help="single EN page to snapshot")
    ap.add_argument("--all", action="store_true", help="process all EN pages")
    ap.add_argument("--check", action="store_true", help="compare current upstream block with GitHub without writing")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if args.apply and not args.yes:
        sys.exit("refusing to write without --yes")
    if args.page:
        pages = [root / args.page]
    elif args.all:
        pages = discover_pages(root)
    else:
        sys.exit("provide --page categories/<cat>/<slug>.md or --all")
    any_changed = False
    gone = False
    for page in pages:
        try:
            if args.check:
                changed = compare_snapshot(page, root)
            else:
                changed = process_page(page, root, args.apply)
        except RuntimeError as exc:
            if "404" not in str(exc) and "Not Found" not in str(exc):
                raise
            # A vanished repo used to end the run with a traceback (financial-api, 2026-10-09).
            print(f"gone_upstream {page.relative_to(root)}: GitHub 404 — run "
                  f"tools/repo_moves.py --page {page.relative_to(root)} to probe for a move")
            gone = True
            continue
        any_changed = any_changed or changed
    return 1 if gone or (args.check and any_changed) else 0


if __name__ == "__main__":
    raise SystemExit(main())
