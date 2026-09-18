#!/usr/bin/env python3
"""Sync the Health / 健康度 column in INDEX + README summary tables from page frontmatter.

The page `health:` block (written by tools/health.py) is the SSOT; the index rows are a
projection of it and must never be hand-graded. lint.py ERRORs on any drift; this tool fixes it.

Usage:
    python3 tools/sync_index_health.py             # dry-run: print every row it would change
    python3 tools/sync_index_health.py --apply     # rewrite the rows in place
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint import ZH_SUFFIX, health_parity_rows, is_table_separator, table_cells  # noqa: E402


def apply_file(path: Path, root: Path, apply: bool) -> int:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    drifts, _malformed = health_parity_rows(path, root)
    zh = path.name.endswith(ZH_SUFFIX)
    required = "健康度" if zh else "Health"
    # Map each drift line back to its table's health-column index by re-finding the header.
    fixed = 0
    for line_no, got, want, page in drifts:
        idx = line_no - 1
        header_i = next((k for k in range(idx - 1, -1, -1)
                         if is_table_separator(lines[k + 1].strip() if k + 1 < len(lines) else "")), None)
        if header_i is None:
            print(f"SKIP {path}:{line_no}: header not found")
            continue
        hcol = table_cells(lines[header_i].strip()).index(required)
        raw = lines[idx]
        parts = re.split(r"(?<!\\)\|", raw.rstrip("\n"))
        # Positional cell must match the lint parser (which unescapes \|) before we rewrite it.
        if len(parts) <= hcol + 1 or parts[hcol + 1].strip().replace("\\|", "|") != got:
            print(f"SKIP {path}:{line_no}: positional mismatch (fix by hand)")
            continue
        parts[hcol + 1] = f" {want} "
        if apply:
            lines[idx] = "|".join(parts) + ("\n" if raw.endswith("\n") else "")
        print(f"{'FIX ' if apply else 'WOULD'} {path}:{line_no} {page.name}: '{got}' -> '{want}'")
        fixed += 1
    if apply and fixed:
        path.write_text("".join(lines), encoding="utf-8")
    return fixed


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--apply", action="store_true", help="rewrite rows (default: dry-run)")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    targets = [root / "README.md", root / "README.zh.md",
               *sorted((root / "categories").rglob("INDEX.md")),
               *sorted((root / "categories").rglob("INDEX.zh.md"))]
    total = 0
    for t in targets:
        if t.exists():
            total += apply_file(t, root, args.apply)
    verb = "fixed" if args.apply else "would fix"
    print(f"\n{verb} {total} row(s) across {len(targets)} summary files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
