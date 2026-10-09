#!/usr/bin/env python3
"""Find indexed repos that were renamed, transferred or deleted, and follow the moves.

A renamed or transferred GitHub repo keeps answering under its old name through a
redirect, so nothing else in the toolchain notices: `gh api repos/<old>` returns 200 with
the new `full_name`. The page keeps pointing at the old name until someone claims it —
then the page silently describes a stranger's repo, or 404s. 2026-10-09 scan of all
pages: facebook/react -> react/react, danny-avila/LibreChat -> LibreChat-AI/LibreChat,
OpenBB-finance/OpenBB -> openbq-org/OpenBB, Untrivial-ai/agent-orchestrator ->
OrchestratorInc/agent-orchestrator, two case-only changes, one 404 (HiThink-Tech).

Statuses:
  same   — the recorded name is current.
  case   — same repo, owner/name case changed.
  moved  — GitHub redirects the recorded name to another repo. GitHub only redirects a
           real rename or transfer, so `--apply` follows it.
  gone   — 404. Candidates with the same repo name are listed, each with whether it
           contains the page's recorded `default_branch_sha`. That is evidence, not proof:
           a fork or a re-upload carries the same history (financial-api has exactly such
           a personal re-upload), so a `gone` page is never rewritten automatically.

A full scan resolves the names in GraphQL batches of 100 first (GraphQL follows the same
redirects, and a batch costs one point where per-repo REST calls would spend most of a
`GITHUB_TOKEN`'s 1000 requests an hour); only names the batch did not resolve go through
REST. `.github/workflows/repo-moves.yml` runs it monthly and files the result as an issue
(`tools/repo_moves_issue.py`).

`--apply --yes` for `moved` / `case` rewrites the `repo:` field and every
`github.com/<old>` link (case-insensitive, whole path segment only, so `facebook/react`
never touches `facebook/react-native`) in pages, flows, INDEX/README and the health
package-override keys. Bare `owner/repo` mentions in prose are reported, not rewritten:
a sentence like "still under facebook/react" has to be re-judged, not substituted.
Afterwards run `tools/upstream_snapshot.py --page <P> --apply --yes` and
`tools/reverse_index.py --write`.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent
OVERRIDES = Path("tools/health_package_overrides.json")
REWRITE_GLOBS = ("categories/**/*.md", "flows/*.json", "README.md", "README.zh.md", "INDEX.md", "INDEX.zh.md")

GitHub = Callable[[str], object]


def gh_api(path: str) -> object:
    """`gh api <path>` as parsed JSON; None when the thing does not exist. Other failures raise.

    "Does not exist" is a 404, or the 422 GitHub returns for a commit SHA the repo lacks."""
    for attempt in range(3):
        proc = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=60)
        if proc.returncode == 0:
            return json.loads(proc.stdout or "null")
        if "404" in proc.stderr or "Not Found" in proc.stderr or "No commit found for SHA" in proc.stderr:
            return None
        if not re.search(r"HTTP 5\d\d", proc.stderr) or attempt == 2:
            break
        time.sleep(5 * (attempt + 1))  # transient GitHub 5xx (a 502 ended a full scan, 2026-10-09)
    raise RuntimeError(proc.stderr.strip() or f"gh api {path} failed")


def gh_graphql(query: str) -> dict:
    """`gh api graphql` data. gh exits non-zero when any alias is NOT_FOUND but still prints
    the partial data, so stdout is parsed before the exit code is looked at."""
    proc = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"],
                          capture_output=True, text=True, timeout=120)
    try:
        data = json.loads(proc.stdout or "null")
    except json.JSONDecodeError:
        data = None
    if isinstance(data, dict) and isinstance(data.get("data"), dict):
        return data["data"]
    raise RuntimeError(proc.stderr.strip() or "gh api graphql failed")


def prefetch(names: list[str], gql: Callable[[str], dict] = gh_graphql, batch: int = 100) -> dict[str, str]:
    """Recorded name -> current `owner/name`, for every name GraphQL resolves.

    Unresolved names (NOT_FOUND, any other error, a failed batch) are simply absent, so they
    fall through to the REST path in `classify`, which owns the 404 / candidate logic."""
    resolved: dict[str, str] = {}
    unique = sorted(set(names))
    for start in range(0, len(unique), batch):
        chunk = unique[start:start + batch]
        fields = []
        for i, name in enumerate(chunk):
            owner, repo = name.split("/", 1)
            fields.append(f"r{i}: repository(owner: {json.dumps(owner)}, name: {json.dumps(repo)}) {{ nameWithOwner }}")
        try:
            data = gql("{ " + " ".join(fields) + " }")
        except RuntimeError as exc:
            print(f"note: GraphQL batch {start // batch} failed, falling back to REST: {exc}")
            continue
        for i, name in enumerate(chunk):
            node = data.get(f"r{i}")
            if isinstance(node, dict) and node.get("nameWithOwner"):
                resolved[name] = node["nameWithOwner"]
    return resolved


def repo_from_page(text: str) -> str | None:
    m = re.search(r"^repo:\s*https?://github\.com/([^/\s]+/[^/\s#?]+?)(?:\.git)?/?\s*$", text, re.M)
    return m.group(1) if m else None


def snapshot_sha(text: str) -> str | None:
    m = re.search(r"^\s+default_branch_sha:\s*([0-9a-f]{7,40})\s*$", text, re.M)
    return m.group(1) if m else None


def classify(full_name: str, sha: str | None, gh: GitHub = gh_api) -> tuple[str, str | None, list[dict]]:
    data = gh(f"repos/{full_name}")
    if isinstance(data, dict) and data.get("full_name"):
        now = data["full_name"]
        if now == full_name:
            return "same", now, []
        return ("case" if now.lower() == full_name.lower() else "moved"), now, []
    name = full_name.split("/", 1)[1]
    found = gh(f"search/repositories?q={name}+in:name&per_page=10") or {}
    candidates = []
    for item in found.get("items", []) if isinstance(found, dict) else []:
        cand = item.get("full_name", "")
        if cand.split("/", 1)[-1].lower() != name.lower() or cand.lower() == full_name.lower():
            continue
        has = bool(sha) and gh(f"repos/{cand}/commits/{sha}") is not None
        candidates.append({"full_name": cand, "fork": bool(item.get("fork")), "has_snapshot_commit": has})
    return "gone", None, candidates


def _link_pattern(old: str) -> re.Pattern[str]:
    # The old path must end the segment: `/`, `#`, `?`, `.git`, quote, bracket, space, `|`
    # or end of text. `facebook/react` never matches inside `facebook/react-native`.
    return re.compile(r"(github\.com/)" + re.escape(old) + r"(?=\.git\b|[/#?\s)\]\"'`|>,;]|$)", re.I)


def _bare_pattern(old: str) -> re.Pattern[str]:
    return re.compile(r"(?<![\w./-])" + re.escape(old) + r"(?![\w-])", re.I)


def apply_move(root: Path, old: str, new: str) -> dict:
    link = _link_pattern(old)
    bare = _bare_pattern(old)
    changed: list[str] = []
    bare_mentions: list[dict] = []
    paths = sorted({p for pattern in REWRITE_GLOBS for p in root.glob(pattern) if p.is_file()})
    for path in paths:
        text = path.read_text(encoding="utf-8")
        new_text = link.sub(lambda m: m.group(1) + new, text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            changed.append(str(path.relative_to(root)))
        for number, line in enumerate(new_text.splitlines(), 1):
            if bare.search(line):
                bare_mentions.append({"path": str(path.relative_to(root)), "line": number, "text": line.strip()[:200]})
    overrides = root / OVERRIDES
    if overrides.is_file():
        table = json.loads(overrides.read_text(encoding="utf-8"))
        if old.lower() in {k.lower() for k in table}:
            table = {(new.lower() if k.lower() == old.lower() else k): v for k, v in table.items()}
            overrides.write_text(json.dumps(dict(sorted(table.items())), indent=2, ensure_ascii=False) + "\n",
                                 encoding="utf-8")
            changed.append(str(OVERRIDES))
    return {"old": old, "new": new, "changed": changed, "bare_mentions": bare_mentions}


def discover(root: Path, pages: list[str]) -> list[Path]:
    if pages:
        return [root / p for p in pages]
    return sorted(p for p in root.glob("categories/**/*.md")
                  if not p.name.endswith(".zh.md") and p.name != "INDEX.md")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--page", action="append", default=[], help="EN page; repeatable; default all pages")
    ap.add_argument("--apply", action="store_true", help="follow `moved` / `case` (needs --yes)")
    ap.add_argument("--yes", action="store_true")
    ap.add_argument("--json", help="write the full report here")
    args = ap.parse_args()
    if args.apply and not args.yes:
        sys.exit("refusing to write without --yes")
    root = Path(args.root).resolve()
    pages = [(page, page.read_text(encoding="utf-8")) for page in discover(root, args.page)]
    resolved = prefetch([n for _, text in pages if (n := repo_from_page(text))])

    def gh(path: str) -> object:
        name = path.removeprefix("repos/")
        if name in resolved:
            return {"full_name": resolved[name]}
        return gh_api(path)

    report = []
    for page, text in pages:
        full_name = repo_from_page(text)
        if full_name is None:
            continue
        try:
            status, now, candidates = classify(full_name, snapshot_sha(text), gh)
        except RuntimeError as exc:
            status, now, candidates = "error", None, []
            print(f"error {page.relative_to(root)} {full_name}: {exc}")
        row = {"page": str(page.relative_to(root)), "repo": full_name, "status": status, "now": now}
        if candidates:
            row["candidates"] = candidates
        if args.apply and status in {"moved", "case"}:
            row["applied"] = apply_move(root, full_name, now)
        report.append(row)
        if status not in {"same", "error"}:
            print(f"{status:5} {row['page']} {full_name}" + (f" -> {now}" if now else ""))
            for cand in candidates:
                print(f"      candidate {cand['full_name']} fork={cand['fork']} "
                      f"has_snapshot_commit={cand['has_snapshot_commit']}")
            for hit in row.get("applied", {}).get("bare_mentions", []):
                print(f"      review {hit['path']}:{hit['line']}: {hit['text']}")
    if args.json:
        Path(args.json).write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    pending = [r for r in report if r["status"] in {"gone", "error"}
               or (r["status"] in {"moved", "case"} and not args.apply)]
    return 1 if pending else 0


if __name__ == "__main__":
    raise SystemExit(main())
