#!/usr/bin/env python3
"""oss-atlas tab intake — the deterministic half of `.claude/skills/intake-tabs/`.

The skill turns the GitHub repositories open in the maintainer's Chrome into selection pages,
one repo at a time, closing each repo's tabs once its page is committed. Judgment (is this
repo includable, where does it go, what does the page say) stays with the agent; this file
owns the parts that must not vary between runs:

  tabs      list the owner/repo keys open in the USER's Chrome (never an automation Chrome)
  scan      read the tabs, canonicalize each repo via `gh api`, classify it, append new rows
            to the ledger. Re-run it any time: rows already in the ledger are left alone, so
            tabs opened mid-batch are picked up and nothing is repeated.
  pending   print the rows still waiting (`<repo> <action> <page>`)
  set       update one row's result / action / page / note
  close     close every tab of the given repos — refuses repos whose ledger row is not `done`
  union-resolve   settle INDEX/README merge conflicts where both sides appended rows

Ledger (`intake/tabs-<UTC date>/ledger.md`) columns, in order:
  规范名 | 动作 | 结果 | 页面路径 | 备注 | 标签里的写法
  action: add | sync | skip | propose      (propose = the agent judged it unfit; the user decides)
  result: pending | running | done | failed | skipped | proposed

Why Chrome is addressed by pid: AppleScript's `tell application "Google Chrome"` binds to the
first instance with that bundle id, and on this machine another session's automation Chrome is
often running — the 2026-09-28 batch read the wrong browser's tabs that way. The user's Chrome is
the one main process with no `--remote-debugging-*` flag and the default profile directory; the
Swift helper (`tools/chrome_tabs.swift`, compiled on demand) talks to that pid only.

Requires: macOS, Python 3.9+, `gh` authenticated, `swiftc` (Xcode command line tools).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable

ROOT = Path(__file__).resolve().parent.parent
SWIFT_SRC = ROOT / "tools" / "chrome_tabs.swift"
HELPER = Path(os.environ.get("OSS_ATLAS_CHROME_TABS_BIN", Path.home() / ".cache" / "oss-atlas" / "chrome_tabs"))
DEFAULT_PROFILE = str(Path.home() / "Library" / "Application Support" / "Google" / "Chrome")
DEFAULT_SKIP_OWNER = "ZhenningLang"  # the maintainer's own repos are not selection candidates

HEADER = ["规范名", "动作", "结果", "页面路径", "备注", "标签里的写法"]
LEDGER_PREAMBLE = """# Tab intake ledger — {date} (UTC)

来源：用户本人 Chrome 的标签（按进程号定位，不碰自动化实例）。动作 add/sync/skip/propose；结果 pending/running/done/failed/skipped/proposed。
propose = 读过之后判断不适合收录，标签保留，等用户定。

"""

REPO_URL_RE = re.compile(
    r"^https?://(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:\.git)?(?:[/?#]|$)", re.I
)
OWNER_URL_RE = re.compile(r"^https?://(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/?(?:[?#]|$)", re.I)
# First path segments that are GitHub's own pages, not an owner.
RESERVED = {
    "orgs", "settings", "notifications", "marketplace", "topics", "collections", "sponsors", "apps",
    "features", "login", "logout", "signup", "explore", "trending", "search", "pulls", "issues", "new",
    "organizations", "enterprise", "pricing", "about", "codespaces", "copilot", "dashboard", "users",
    "security", "site", "readme", "customer-stories", "events", "watching", "stars",
}


def repo_key(url: str) -> str | None:
    """`https://github.com/Foo/bar/tree/main?x` → `foo/bar`; non-repo GitHub pages → None."""
    m = REPO_URL_RE.match(url)
    if not m or m.group(1).lower() in RESERVED:
        return None
    return f"{m.group(1)}/{m.group(2)}".lower()


def owner_key(url: str) -> str | None:
    """`https://github.com/TanStack` → `TanStack` (an org/user page, not a repo)."""
    m = OWNER_URL_RE.match(url)
    return m.group(1) if m and m.group(1).lower() not in RESERVED else None


# ---------------------------------------------------------------- Chrome

def user_chrome_pid(ps_output: str | None = None) -> str:
    if ps_output is None:
        ps_output = subprocess.run(["ps", "-axo", "pid=,command="], capture_output=True, text=True).stdout
    mine = []
    for line in ps_output.splitlines():
        pid, _, cmd = line.strip().partition(" ")
        if not cmd.startswith("/") or "/Contents/MacOS/Google Chrome" not in cmd or "Helper" in cmd:
            continue
        if "--remote-debugging" in cmd:
            continue
        m = re.search(r"--user-data-dir=(.+?)(?= --|$)", cmd)  # the default path contains a space
        if m and m.group(1).rstrip("/") != DEFAULT_PROFILE:
            continue
        mine.append(pid)
    if len(mine) != 1:
        raise SystemExit(f"DEFER: expected exactly one user Chrome process, found {mine or 'none'}")
    return mine[0]


def ensure_helper() -> Path:
    if HELPER.exists() and HELPER.stat().st_mtime >= SWIFT_SRC.stat().st_mtime:
        return HELPER
    HELPER.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["swiftc", "-O", "-o", str(HELPER), str(SWIFT_SRC)], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(f"swiftc failed building {HELPER}: {r.stderr.strip()}")
    return HELPER


def run_helper(*args: str) -> str:
    try:
        r = subprocess.run([str(ensure_helper()), user_chrome_pid(), *args], capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired:
        raise SystemExit("chrome_tabs timed out (Chrome busy or an Automation permission prompt is open)")
    if r.returncode:
        raise SystemExit(f"chrome_tabs failed rc={r.returncode}: {r.stderr.strip()}")
    return r.stdout


def chrome_urls() -> list[str]:
    return [line.split("\t", 2)[2] for line in run_helper("list").splitlines() if line.count("\t") >= 2]


# ---------------------------------------------------------------- ledger

@dataclass
class Row:
    repo: str
    action: str
    result: str
    page: str = ""
    note: str = ""
    tab: str = ""

    def cells(self) -> list[str]:
        return [self.repo, self.action, self.result, self.page, self.note.replace("|", "／"), self.tab]


class Ledger:
    def __init__(self, path: Path):
        self.path = path
        self.pre: list[str] = []
        self.rows: list[Row] = []
        self.post: list[str] = []
        if path.exists():
            self._parse(path.read_text(encoding="utf-8").split("\n"))

    def _parse(self, lines: list[str]) -> None:
        seen = False
        for line in lines:
            if line.startswith("|"):
                seen = True
                c = [x.strip() for x in line.strip().strip("|").split("|")]
                if c[0] == HEADER[0] or set(line) <= set("|:- "):
                    continue
                c += [""] * (6 - len(c))
                self.rows.append(Row(*c[:6]))
            elif not seen:
                self.pre.append(line)
            else:
                self.post.append(line)

    def find(self, name: str) -> Row | None:
        n = name.lower()
        return next((r for r in self.rows if n in (r.repo.lower(), r.tab.lower())), None)

    def add(self, row: Row) -> bool:
        if self.find(row.repo) or (row.tab and self.find(row.tab)):
            return False
        self.rows.append(row)
        return True

    def render(self, date: str) -> str:
        pre = "\n".join(self.pre).rstrip("\n") + "\n\n" if self.pre else LEDGER_PREAMBLE.format(date=date)
        table = ["| " + " | ".join(HEADER) + " |", "|" + ":---|" * len(HEADER)]
        table += ["| " + " | ".join(r.cells()) + " |" for r in self.rows]
        post = "\n".join(self.post).strip("\n")
        return pre + "\n".join(table) + "\n" + ("\n" + post + "\n" if post else "")

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        date = self.path.parent.name.removeprefix("tabs-")
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(self.render(date), encoding="utf-8")
        os.replace(tmp, self.path)


# ---------------------------------------------------------------- classify

@dataclass
class RepoInfo:
    full_name: str
    fork: bool = False
    archived: bool = False
    size: int = 1
    parent: str = ""


def gh_resolve(key: str) -> RepoInfo | None:
    """Canonical name + shape flags. None = GitHub says 404; other failures raise."""
    r = subprocess.run(
        ["gh", "api", f"repos/{key}", "--jq", '[.full_name,.fork,.archived,.size,(.parent.full_name // "")]|@tsv'],
        capture_output=True, text=True,
    )
    if r.returncode:
        if "404" in r.stderr or "Not Found" in r.stderr:
            return None
        raise RuntimeError(r.stderr.strip() or f"gh exit {r.returncode}")
    name, fork, archived, size, parent = (r.stdout.rstrip("\n").split("\t") + [""] * 5)[:5]
    return RepoInfo(name, fork == "true", archived == "true", int(size or 0), parent)


def indexed_page(full_name: str, categories: Path) -> str:
    pat = re.compile(rf"^repo:\s*https?://github\.com/{re.escape(full_name)}/?\s*$", re.I | re.M)
    for p in sorted(categories.rglob("*.md")):
        if p.name.endswith(".zh.md") or p.name.startswith("INDEX"):
            continue
        head = p.read_text(encoding="utf-8", errors="replace")[:4000]
        if pat.search(head):
            return str(p.relative_to(categories.parent))
    return ""


def classify(key: str, info: RepoInfo | None, skip_owner: str, find_page: Callable[[str], str]) -> Row:
    if info is None:
        return Row(key, "skip", "skipped", "", "GitHub API 404（私有、已删或拼错），标签不动", key)
    if info.full_name.split("/")[0].lower() == skip_owner.lower():
        return Row(info.full_name, "skip", "skipped", "", f"owner 是 {skip_owner}，标签不动", key)
    if info.size == 0:
        return Row(info.full_name, "skip", "skipped", "", "空仓库（size=0），标签不动", key)
    notes = []
    if info.full_name.lower() != key:
        notes.append(f"标签写法已重定向到 {info.full_name}")
    if info.fork:
        notes.append(f"fork 自 {info.parent or '?'}：先判是否与上游重复")
    if info.archived:
        notes.append("已归档：照收，风险写进健康度")
    page = find_page(info.full_name)
    return Row(info.full_name, "sync" if page else "add", "pending", page, "；".join(notes), key)


def scan(ledger: Ledger, urls: Iterable[str], skip_owner: str,
         resolve: Callable[[str], RepoInfo | None], find_page: Callable[[str], str]) -> tuple[list[Row], list[str], list[str]]:
    """Returns (new rows, owner pages seen, keys that failed to resolve)."""
    urls = list(urls)
    keys = sorted({k for k in map(repo_key, urls) if k})
    owners = sorted({o for o in map(owner_key, urls) if o})
    new, errors = [], []
    for key in keys:
        if ledger.find(key):
            continue
        try:
            info = resolve(key)
        except RuntimeError as e:  # rate limit, network: leave it out so the next scan retries
            errors.append(f"{key}: {e}")
            continue
        row = classify(key, info, skip_owner, find_page)
        if ledger.add(row):
            new.append(row)
    return new, owners, errors


# ---------------------------------------------------------------- union-resolve

CONFLICT_RE = re.compile(r"<<<<<<< [^\n]*\n(.*?)=======\n(.*?)>>>>>>> [^\n]*\n", re.S)
UNIONABLE_RE = re.compile(r"(^|/)(INDEX|README)(\.zh)?\.md$")


def union_text(text: str, is_index: bool) -> str:
    """Keep both sides of each conflict (ours first). Only safe where both sides appended rows."""
    def join(m: re.Match) -> str:
        a, b = m.group(1).rstrip("\n"), m.group(2).rstrip("\n")
        table_seam = a.split("\n")[-1].startswith("|") and b.lstrip("\n").startswith("|")
        sep = "\n" if table_seam or is_index else "\n\n"  # a blank line inside a table splits it
        return a + sep + (b.lstrip("\n") if table_seam else b) + "\n"
    return CONFLICT_RE.sub(join, text)


def union_resolve() -> int:
    files = subprocess.run(["git", "diff", "--name-only", "--diff-filter=U"], capture_output=True, text=True).stdout.split()
    bad = []
    for f in files:
        if not UNIONABLE_RE.search(f):
            bad.append(f)
            continue
        text = union_text(Path(f).read_text(encoding="utf-8"), "INDEX" in f)
        if "<<<<<<<" in text or ">>>>>>>" in text:
            bad.append(f)
            continue
        Path(f).write_text(text, encoding="utf-8")
        subprocess.run(["git", "add", f], check=True)
        print("union-resolved", f)
    if bad:
        print("UNRESOLVED (resolve by hand):", *bad)
    return 1 if bad else 0


# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("tabs", help="list owner/repo keys in the user's Chrome")
    for name in ("scan", "pending", "set", "close"):
        p = sub.add_parser(name)
        p.add_argument("--ledger", required=True, type=Path)
        if name == "scan":
            p.add_argument("--skip-owner", default=DEFAULT_SKIP_OWNER)
        if name == "set":
            p.add_argument("repo")
            p.add_argument("result", choices=["pending", "running", "done", "failed", "skipped", "proposed"])
            p.add_argument("--action", choices=["add", "sync", "skip", "propose"])
            p.add_argument("--page")
            p.add_argument("--note")
        if name == "close":
            p.add_argument("repos", nargs="+")
    sub.add_parser("union-resolve", help="resolve INDEX/README append-append conflicts in the current repo")
    a = ap.parse_args(argv)

    if a.cmd == "tabs":
        for k in sorted({k for k in map(repo_key, chrome_urls()) if k}):
            print(k)
        return 0
    if a.cmd == "union-resolve":
        return union_resolve()

    ledger = Ledger(a.ledger)
    if a.cmd == "scan":
        cats = ROOT / "categories"
        new, owners, errors = scan(ledger, chrome_urls(), a.skip_owner, gh_resolve, lambda n: indexed_page(n, cats))
        ledger.save()
        for r in new:
            print(f"NEW {r.action:5} {r.repo}  {r.page}  {r.note}".rstrip())
        for o in owners:
            print(f"OWNER-PAGE {o}  (org/user page, not a repo — ask before expanding it)")
        for e in errors:
            print(f"RETRY {e}")
        print(f"{len(new)} new, {sum(r.result == 'pending' for r in ledger.rows)} pending, {len(ledger.rows)} rows")
        return 0
    if a.cmd == "pending":
        for r in ledger.rows:
            if r.result == "pending":
                print(r.repo, r.action, r.page)
        return 0
    if a.cmd == "set":
        row = ledger.find(a.repo)
        if not row:
            raise SystemExit(f"not in ledger: {a.repo}")
        row.result = a.result
        row.action = a.action or row.action
        row.page = a.page if a.page is not None else row.page
        row.note = a.note if a.note is not None else row.note
        ledger.save()
        print("| " + " | ".join(row.cells()) + " |")
        return 0
    if a.cmd == "close":
        rows = [(n, ledger.find(n)) for n in a.repos]
        refused = [n for n, r in rows if not r or r.result != "done"]
        if refused:
            raise SystemExit(f"refusing to close tabs of repos not `done` in the ledger: {refused}")
        names = {r.repo.lower() for _, r in rows} | {r.tab.lower() for _, r in rows if r.tab}
        urls = sorted({u for u in chrome_urls() if repo_key(u) in names})
        if urls:
            print(run_helper("close", *urls), end="")
        print(f"{len(urls)} tab(s) matched")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
