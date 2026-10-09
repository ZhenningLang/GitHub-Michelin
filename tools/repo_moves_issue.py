#!/usr/bin/env python3
"""File a `tools/repo_moves.py --json` report as one rolling GitHub issue.

Run monthly by `.github/workflows/repo-moves.yml`. Actionable rows are `moved`, `case`,
`error`, and `gone` unless the repo is in `tools/repo_moves_acknowledged.json` (a 404 the
maintainer already decided to keep, so it would otherwise reopen the issue every month).
An acknowledged repo that stops being `gone` is reported again.

One issue, labelled `repo-moves`: created when there is something to do, its body
replaced on later scans (with a comment only when the findings changed, so a repeat scan
does not notify anyone), and closed when a scan comes back clean.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent
ACKNOWLEDGED = ROOT / "tools" / "repo_moves_acknowledged.json"
LABEL = "repo-moves"
TITLE = "repo_moves: indexed repos renamed, transferred or gone upstream"
MARKER = "<!-- repo-moves:findings "

Gh = Callable[[list[str]], str]


def gh_cli(args: list[str]) -> str:
    proc = subprocess.run(["gh", *args], capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"gh {' '.join(args)} failed")
    return proc.stdout


def actionable(report: list[dict], acknowledged: dict[str, str]) -> list[dict]:
    acked = {k.lower() for k in acknowledged}
    return [r for r in report
            if r["status"] in {"moved", "case", "error"}
            or (r["status"] == "gone" and r["repo"].lower() not in acked)]


def fingerprint(rows: list[dict]) -> str:
    return json.dumps(sorted([r["page"], r["status"], r.get("now") or ""] for r in rows))


def render(rows: list[dict], run_url: str) -> str:
    lines = [f"Monthly `tools/repo_moves.py` scan found {len(rows)} page(s) to act on"
             + (f" ([run]({run_url}))." if run_url else "."), "",
             "| page | recorded repo | status | now |", "|:---|:---|:---|:---|"]
    for r in rows:
        lines.append(f"| `{r['page']}` | `{r['repo']}` | {r['status']} | {('`' + r['now'] + '`') if r.get('now') else ''} |")
    candidates = [(r, c) for r in rows for c in r.get("candidates", [])]
    if candidates:
        lines += ["", "Same-name candidates for `gone` repos (evidence only; a fork or re-upload also carries the history):", ""]
        lines += [f"- `{r['repo']}` → `{c['full_name']}` fork={c['fork']} has_snapshot_commit={c['has_snapshot_commit']}"
                  for r, c in candidates]
    lines += ["", "To follow `moved` / `case` rows:", "", "```bash",
              "python3 tools/repo_moves.py --page <page> --apply --yes   # re-judge the bare mentions it prints",
              "python3 tools/upstream_snapshot.py --page <page> --apply --yes",
              "python3 tools/reverse_index.py --write",
              "```", "",
              "A `gone` repo the page should keep pointing at goes into `tools/repo_moves_acknowledged.json` "
              "with the reason. `error` rows are scan failures; re-run the workflow.", "",
              f"{MARKER}{fingerprint(rows)} -->"]
    return "\n".join(lines) + "\n"


def sync_issue(rows: list[dict], gh: Gh, repo: str, run_url: str = "", dry_run: bool = False) -> str:
    """Create / update / close the rolling issue. Returns what it did."""
    open_issues = json.loads(gh(["issue", "list", "-R", repo, "--label", LABEL, "--state", "open",
                                 "--json", "number,body", "--limit", "5"]) or "[]")
    current = open_issues[0] if open_issues else None
    if not rows:
        if current is None:
            return "clean"
        if not dry_run:
            gh(["issue", "close", str(current["number"]), "-R", repo,
                "--comment", f"Scan came back clean{f' ({run_url})' if run_url else ''}; closing."])
        return f"closed #{current['number']}"
    body = render(rows, run_url)
    if dry_run:
        print(body)
        return "dry-run"
    if current is None:
        gh(["label", "create", LABEL, "-R", repo, "--force", "--color", "c5def5",
            "--description", "Indexed repos renamed, transferred or gone upstream"])
        url = gh(["issue", "create", "-R", repo, "--title", TITLE, "--label", LABEL, "--body", body]).strip()
        return f"created {url}"
    changed = fingerprint(rows) not in (current.get("body") or "")
    gh(["issue", "edit", str(current["number"]), "-R", repo, "--body", body])
    if changed:
        gh(["issue", "comment", str(current["number"]), "-R", repo,
            "--body", f"Findings changed on this scan{f' ({run_url})' if run_url else ''}; body updated."])
    return f"updated #{current['number']}" + (" (findings changed)" if changed else "")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("report", help="JSON written by `tools/repo_moves.py --json`")
    ap.add_argument("--repo", required=True, help="owner/name the issue lives in")
    ap.add_argument("--run-url", default="")
    ap.add_argument("--acknowledged", default=str(ACKNOWLEDGED))
    ap.add_argument("--dry-run", action="store_true", help="print the body, touch nothing")
    args = ap.parse_args()
    report = json.loads(Path(args.report).read_text(encoding="utf-8"))
    acknowledged = json.loads(Path(args.acknowledged).read_text(encoding="utf-8"))
    rows = actionable(report, acknowledged)
    print(sync_issue(rows, gh_cli, args.repo, args.run_url, args.dry_run))
    return 0


if __name__ == "__main__":
    sys.exit(main())
