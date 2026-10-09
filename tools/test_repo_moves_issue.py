#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import repo_moves_issue as rmi

MOVED = {"page": "categories/a/react.md", "repo": "facebook/react", "status": "moved", "now": "react/react"}
GONE = {"page": "categories/f/financial-api.md", "repo": "HiThink-Tech/financial-api", "status": "gone", "now": None,
        "candidates": [{"full_name": "tekteku/financial-api", "fork": False, "has_snapshot_commit": False}]}
SAME = {"page": "categories/a/vue.md", "repo": "vuejs/core", "status": "same", "now": "vuejs/core"}


class FakeGh:
    def __init__(self, open_issues: list[dict]):
        self.open_issues = open_issues
        self.calls: list[list[str]] = []

    def __call__(self, args: list[str]) -> str:
        self.calls.append(args)
        if args[:2] == ["issue", "list"]:
            return json.dumps(self.open_issues)
        if args[:2] == ["issue", "create"]:
            return "https://github.com/o/r/issues/9\n"
        return ""

    def verbs(self) -> list[str]:
        return [" ".join(c[:2]) for c in self.calls]


class RepoMovesIssueTest(unittest.TestCase):
    def test_acknowledged_gone_is_quiet_but_other_statuses_are_not(self):
        acked = {"hithink-tech/FINANCIAL-API": "kept"}
        self.assertEqual(rmi.actionable([MOVED, GONE, SAME], acked), [MOVED])
        self.assertEqual(rmi.actionable([MOVED, GONE, SAME], {}), [MOVED, GONE])
        # An acknowledged repo that comes back as a move is news again.
        back = dict(GONE, status="moved", now="HiThink-Tech/fin-api")
        self.assertEqual(rmi.actionable([back], acked), [back])

    def test_clean_scan_with_no_issue_does_nothing(self):
        gh = FakeGh([])
        self.assertEqual(rmi.sync_issue([], gh, "o/r"), "clean")
        self.assertEqual(gh.verbs(), ["issue list"])

    def test_first_finding_creates_labelled_issue(self):
        gh = FakeGh([])
        self.assertEqual(rmi.sync_issue([MOVED, GONE], gh, "o/r", "https://run"), "created https://github.com/o/r/issues/9")
        self.assertEqual(gh.verbs(), ["issue list", "label create", "issue create"])
        body = gh.calls[-1][gh.calls[-1].index("--body") + 1]
        self.assertIn("| `categories/a/react.md` | `facebook/react` | moved | `react/react` |", body)
        self.assertIn("`HiThink-Tech/financial-api` → `tekteku/financial-api` fork=False has_snapshot_commit=False", body)

    def test_repeat_scan_edits_silently_and_comments_only_on_change(self):
        same_body = rmi.render([MOVED], "")
        gh = FakeGh([{"number": 4, "body": same_body}])
        self.assertEqual(rmi.sync_issue([MOVED], gh, "o/r", "https://run2"), "updated #4")
        self.assertEqual(gh.verbs(), ["issue list", "issue edit"])
        gh = FakeGh([{"number": 4, "body": same_body}])
        self.assertEqual(rmi.sync_issue([MOVED, GONE], gh, "o/r"), "updated #4 (findings changed)")
        self.assertEqual(gh.verbs(), ["issue list", "issue edit", "issue comment"])

    def test_clean_scan_closes_open_issue(self):
        gh = FakeGh([{"number": 4, "body": ""}])
        self.assertEqual(rmi.sync_issue([], gh, "o/r"), "closed #4")
        self.assertEqual(gh.verbs(), ["issue list", "issue close"])

    def test_dry_run_writes_nothing(self):
        gh = FakeGh([])
        self.assertEqual(rmi.sync_issue([MOVED], gh, "o/r", dry_run=True), "dry-run")
        self.assertEqual(gh.verbs(), ["issue list"])

    def test_committed_acknowledged_file_parses(self):
        self.assertTrue(json.loads(rmi.ACKNOWLEDGED.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
