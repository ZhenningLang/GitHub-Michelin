#!/usr/bin/env python3
"""Batch audit of `?` health-radar axes across the index (offline, no network).

`?` is first-class (docs/health-rubric.md §1.2) — but at index scale nobody re-reads 300
pages to check whether each `?` is genuinely structural or a machine false-negative.
This tool scans every EN page's frontmatter `health:` block (the `.zh.md` sibling is
identical by lint contract) and reports:

  - the axis x reason distribution of all `?` grades,
  - each reason classified per docs/health-rubric.md §5.2:
      structural   — expected N/A; leave `?` (e.g. adoption for a repo that ships no package)
      transient    — a network/API failure; re-run the scorer on these pages
      needs_review — a human should look: ambiguous attribution, unparsed license, or a code
                     that doubles as the scorer's exception fallback (it can mask a crash)
  - reasons NOT in the §5.2 enums (enum drift between scorer and rubric),
  - `?` axes with no recorded reason at all (malformed block).

Read-only; exits 0 unless --fail-on-flags is given and transient/drift/missing items exist.

Usage:
  python3 tools/health_audit.py [--root DIR] [--json] [--fail-on-flags]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# §5.2 reason-code enums (SSOT: docs/health-rubric.md). Keep in sync with the rubric.
RUBRIC_ENUMS: dict[str, set[str]] = {
    "maintenance": {"repo_404_or_private", "empty_repo", "recency_unreadable"},
    "responsiveness": {"issues_disabled", "no_traffic", "no_window_signal", "too_young",
                       "type_na", "github_unavailable", "mirror", "vendor_support_elsewhere"},
    "adoption": {"no_package_structural", "registry_lookup_failed", "registry_no_counts",
                 "ambiguous", "no_install_channel"},
    "longevity": {"not_found", "no_activity_signal", "not_a_repo"},
    "governance": {"fork", "unattributable", "empty_or_gated"},
    "risk_license": {"repo_unreachable", "license_unparsed"},
}
AXES = list(RUBRIC_ENUMS)

# Expected N/A — a persistent `?` with one of these is correct; leave it.
STRUCTURAL = {"empty_repo", "issues_disabled", "no_traffic", "no_window_signal", "too_young",
              "type_na", "mirror", "vendor_support_elsewhere", "no_package_structural",
              "not_a_repo", "fork", "unattributable"}
# API/network failure at score time — re-running the scorer usually resolves these.
TRANSIENT = {"recency_unreadable", "github_unavailable", "registry_lookup_failed",
             "no_activity_signal", "repo_unreachable"}
# Human judgment needed: ambiguous attribution, an unparsed/custom license, a moved repo —
# or a code that doubles as a `_safe()` exception fallback in tools/health.py (score_repo),
# which can mask a scorer crash as a structural-looking `?` (adoption->registry_no_counts,
# longevity->not_found, governance->empty_or_gated). The remaining fallbacks map to codes
# classified above: maintenance->recency_unreadable + risk_license->repo_unreachable are
# transient (a re-run resolves or re-flags them); responsiveness->no_traffic is structural
# and too common to flag wholesale — a masked crash there stays invisible [推断].
NEEDS_REVIEW = {"repo_404_or_private", "registry_no_counts", "ambiguous", "not_found",
                "empty_or_gated", "license_unparsed"}


def classify(reason: str) -> str:
    if reason in NEEDS_REVIEW:
        return "needs_review"
    if reason in TRANSIENT:
        return "transient"
    if reason in STRUCTURAL:
        return "structural"
    return "enum_drift"


def parse_page(text: str) -> tuple[dict[str, str], dict[str, str]] | None:
    """Return ({axis: grade}, {axis: reason}) from a page's health block, or None."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    m = re.search(r"(?ms)^health:\n(.*)\Z", text[3:end])
    if not m:
        return None
    block = m.group(0)
    grades: dict[str, str] = {}
    for axis in AXES:
        gm = re.search(r"(?m)^\s{4}" + axis + r":\n\s{6}grade:\s*(\S+)", block)
        if gm:
            grades[axis] = gm.group(1).strip("\"'")
    reasons: dict[str, str] = {}
    for key in ("unknowns", "not_applicable"):
        um = re.search(r"(?ms)^  " + key + r":\n(.*?)(?=^\S|\Z)", block)
        if um:
            for rm in re.finditer(r"(?m)^\s{4}(\w+):\s*\{\s*reason:\s*([\w-]+)\s*\}", um.group(1)):
                reasons[rm.group(1)] = rm.group(2)
    return grades, reasons


def audit(root: Path) -> dict:
    pages = sorted(p for p in (root / "categories").rglob("*.md")
                   if not p.name.endswith(".zh.md") and not p.name.startswith("INDEX"))
    dist: dict[tuple[str, str], int] = {}
    flagged: dict[str, list[dict]] = {"transient": [], "needs_review": [],
                                      "enum_drift": [], "missing_reason": []}
    unknown_axes = 0
    na_axes = 0
    unparsed: list[str] = []
    for page in pages:
        parsed = parse_page(page.read_text(encoding="utf-8"))
        if parsed is None:
            # No/malformed health block. lint.py ERRORs on this; report it here too so the
            # audit never silently claims coverage it doesn't have.
            unparsed.append(str(page.relative_to(root)))
            continue
        grades, reasons = parsed
        rel = str(page.relative_to(root))
        for axis, grade in grades.items():
            if grade == "N/A":
                # A deliberate "this axis does not apply to this artifact type" verdict.
                # Counting it as an unknown would inflate the very backlog this audit
                # exists to burn down, and it is not something a re-run can resolve.
                na_axes += 1
                continue
            if grade != "?":
                continue
            unknown_axes += 1
            reason = reasons.get(axis)
            if reason is None:
                flagged["missing_reason"].append({"page": rel, "axis": axis})
                continue
            dist[(axis, reason)] = dist.get((axis, reason), 0) + 1
            bucket = classify(reason)
            if bucket == "enum_drift" or reason not in RUBRIC_ENUMS.get(axis, set()):
                flagged["enum_drift"].append({"page": rel, "axis": axis, "reason": reason})
            if bucket in ("transient", "needs_review"):
                flagged[bucket].append({"page": rel, "axis": axis, "reason": reason})
    return {"pages_scanned": len(pages), "pages_unparsed": unparsed, "unknown_axes": unknown_axes,
            "not_applicable_axes": na_axes,
            "distribution": [{"axis": a, "reason": r, "count": c, "bucket": classify(r)}
                             for (a, r), c in sorted(dist.items(), key=lambda kv: -kv[1])],
            "flagged": flagged}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=".", help="repo root (default: cwd)")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--fail-on-flags", action="store_true",
                    help="exit 1 if transient / enum-drift / missing-reason items exist")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if not (root / "categories").is_dir():
        print(f"error: {root} has no categories/ dir", file=sys.stderr)
        return 2

    result = audit(root)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"pages scanned: {result['pages_scanned']} (EN only; zh siblings are identical)")
        if result["pages_unparsed"]:
            print(f"pages skipped (no parsable health block — lint should ERROR on these): "
                  f"{len(result['pages_unparsed'])}")
            for rel in result["pages_unparsed"]:
                print(f"  {rel}")
        print(f"`?` axes:      {result['unknown_axes']}")
        print(f"N/A axes:     {result.get('not_applicable_axes', 0)}  (axis does not apply to the type; not a gap)")
        print()
        print(f"{'axis':<16} {'reason':<26} {'count':>5}  bucket")
        for row in result["distribution"]:
            print(f"{row['axis']:<16} {row['reason']:<26} {row['count']:>5}  {row['bucket']}")
        fl = result["flagged"]
        for key, hint in (("transient", "re-run: python3 tools/health.py --page <page> --write"),
                          ("needs_review", "human check (may be a masked scorer exception)"),
                          ("enum_drift", "reason not in docs/health-rubric.md §5.2 enums"),
                          ("missing_reason", "`?` grade but no unknowns entry — malformed block")):
            if fl[key]:
                print(f"\n{key} ({len(fl[key])}) — {hint}")
                for item in fl[key]:
                    print(f"  {item['page']}: {item['axis']}" +
                          (f" ({item['reason']})" if "reason" in item else ""))
        if not any(fl.values()):
            print("\nno flags — every `?` is a documented structural reason.")
    has_flags = any(result["flagged"][k] for k in ("transient", "enum_drift", "missing_reason"))
    return 1 if (args.fail_on_flags and has_flags) else 0


if __name__ == "__main__":
    sys.exit(main())
