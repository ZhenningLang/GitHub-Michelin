#!/usr/bin/env python3
"""Refresh the generated one-line-per-axis health bullets in place.

Scoring a page rewrites its `health:` frontmatter but not its body, so every rescore
leaves the generated bullets quoting yesterday's numbers. `quality_scan.py` reports that
as `health-prose-grade-drift` / `health-prose-raw-drift`.

Why not `sync-health-to-body.py`: that script regenerates the whole `Health & viability`
section, so it overwrites hand-written analysis. Running it across the corpus once cost
548 pages of prose. This one replaces ONLY lines that are already the generated bullet —
lines a machine wrote in the first place, where regenerating loses nothing — and leaves
every other line untouched, including hand-written bullets in the same section.

    python3 tools/refresh_health_bullets.py            # dry run, prints what would change
    python3 tools/refresh_health_bullets.py --apply
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
AXES = ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]
# The generated bullet, both languages:
#   - **Responsiveness**: Grade C — median first-response time 4.2 hours across 2 ...
#   - **响应速度**：Grade C——中位首次响应时间 4.2 小时，基于 2 个 ...
GENERATED_BULLET = re.compile(r"^(\s*-\s+\*\*)([^*]+)(\*\*[:：]\s*)Grade\s+[A-E?]\s*[—–-]")
# Label -> axis, for both languages. Longest first so `维护活跃度` is not read as `维护`.
LABEL_TO_AXIS = {
    "Maintenance": "maintenance", "维护活跃度": "maintenance", "维护": "maintenance",
    "Responsiveness": "responsiveness", "响应速度": "responsiveness", "响应性": "responsiveness",
    "Adoption": "adoption", "采用广度": "adoption", "采用度": "adoption",
    "Longevity": "longevity", "长青度": "longevity",
    "Governance": "governance", "治理集中度": "governance", "维护者分散度": "governance",
    "治理": "governance",
    "Risk / License": "risk_license", "Risk/License": "risk_license",
    "许可宽松度": "risk_license", "许可证风险": "risk_license", "许可与风险": "risk_license",
}


def load_sync_module():
    """The bullet generators live in a module whose name has dashes."""
    spec = importlib.util.spec_from_file_location(
        "sync_health_to_body", ROOT / "tools" / "sync-health-to-body.py")
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(ROOT / "tools"))
    spec.loader.exec_module(mod)
    return mod


def refresh(path: Path, sync) -> tuple[int, list[str], str | None]:
    """Rewrite generated bullets on this page.

    Returns (count, sample diffs, new text) without touching disk, so a dry run and a
    real run take exactly the same code path.
    """
    text = path.read_text(encoding="utf-8")
    fm, body = sync.parse_frontmatter(text)
    if not fm or "health" not in fm:
        return 0, [], None
    axes = (fm["health"] or {}).get("axes") or {}
    is_zh = path.name.endswith(".zh.md")
    make = sync.axis_bullet_zh if is_zh else sync.axis_bullet_en

    changed, diffs = 0, []
    out = []
    for line in body.splitlines():
        m = GENERATED_BULLET.match(line)
        if not m:
            out.append(line)
            continue
        axis = LABEL_TO_AXIS.get(m.group(2).strip().rstrip("：:"))
        if axis is None or axis not in axes:
            out.append(line)
            continue
        fresh = make(axis, axes.get(axis) or {})
        if fresh.strip() == line.strip():
            out.append(line)
            continue
        # Keep the original indentation; only the bullet's text is regenerated.
        indent = line[:len(line) - len(line.lstrip())]
        out.append(indent + fresh.strip())
        changed += 1
        if len(diffs) < 2:
            diffs.append(f"    - {line.strip()[:100]}\n    + {fresh.strip()[:100]}")

    if not changed:
        return 0, [], None
    new_body = "\n".join(out) + ("\n" if body.endswith("\n") else "")
    new_text = text[: len(text) - len(body)] + new_body
    # A line rewrite must not change the page's structure.
    if re.findall(r"(?m)^## .*$", body) != re.findall(r"(?m)^## .*$", new_body):
        raise SystemExit(f"{path}: refusing to write — H2 set changed")
    if len(body.splitlines()) != len(new_body.splitlines()):
        raise SystemExit(f"{path}: refusing to write — line count changed")
    return changed, diffs, new_text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write the changes")
    args = ap.parse_args()

    sync = load_sync_module()
    total_lines = total_pages = 0
    for p in sorted((ROOT / "categories").rglob("*.md")):
        if p.name.endswith("INDEX.md"):
            continue
        count, diffs, new_text = refresh(p, sync)
        if not count:
            continue
        total_lines += count
        total_pages += 1
        print(f"{p.relative_to(ROOT)}: {count} bullet(s)")
        for d in diffs:
            print(d)
        if args.apply:
            p.write_text(new_text, encoding="utf-8")
    verb = "refreshed" if args.apply else "would refresh"
    print(f"\n{verb} {total_lines} generated bullet(s) across {total_pages} page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
