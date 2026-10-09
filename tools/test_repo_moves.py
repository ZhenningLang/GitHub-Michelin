#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import repo_moves


def page(repo: str, body: str = "", sha: str = "abc123") -> str:
    return f"""---
name: Demo
slug: demo
repo: https://github.com/{repo}
category: demo
type: tool
upstream:
  pushed_at: 2026-10-01T00:00:00Z
  default_branch: main
  default_branch_sha: {sha}
  archived: false
health:
  schema: 1
---

# Demo

{body}
"""


class FakeGitHub:
    """`gh api` stand-in: path -> json payload, or None for a 404."""

    def __init__(self, routes: dict[str, object]):
        self.routes = routes
        self.calls: list[str] = []

    def __call__(self, path: str):
        self.calls.append(path)
        return self.routes.get(path)


class RepoMovesTest(unittest.TestCase):
    def make_tree(self, repo: str, body: str = "", extra: dict[str, str] | None = None) -> Path:
        root = Path(tempfile.mkdtemp())
        cat = root / "categories" / "demo"
        cat.mkdir(parents=True)
        (cat / "demo.md").write_text(page(repo, body), encoding="utf-8")
        (cat / "demo.zh.md").write_text(page(repo, body), encoding="utf-8")
        for rel, text in (extra or {}).items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        return root

    def test_same_repo_is_unchanged(self):
        gh = FakeGitHub({"repos/acme/demo": {"full_name": "acme/demo"}})
        self.assertEqual(repo_moves.classify("acme/demo", "abc123", gh), ("same", "acme/demo", []))

    def test_redirect_is_a_move_and_case_change_is_its_own_status(self):
        gh = FakeGitHub({"repos/facebook/react": {"full_name": "react/react"},
                         "repos/jub0t/Concat": {"full_name": "jub0t/concat"}})
        self.assertEqual(repo_moves.classify("facebook/react", "abc123", gh)[:2], ("moved", "react/react"))
        self.assertEqual(repo_moves.classify("jub0t/Concat", "abc123", gh)[:2], ("case", "jub0t/concat"))

    def test_404_lists_candidates_with_history_proof_but_never_picks_one(self):
        gh = FakeGitHub({
            "search/repositories?q=Financial-API+in:name&per_page=10": {"items": [
                {"full_name": "someone/Financial-API", "fork": False},
                {"full_name": "other/Financial-API", "fork": True},
            ]},
            "repos/someone/Financial-API/commits/abc123": {"sha": "abc123"},
        })
        status, now, candidates = repo_moves.classify("HiThink-Tech/Financial-API", "abc123", gh)
        self.assertEqual((status, now), ("gone", None))
        self.assertEqual(candidates, [
            {"full_name": "someone/Financial-API", "fork": False, "has_snapshot_commit": True},
            {"full_name": "other/Financial-API", "fork": True, "has_snapshot_commit": False},
        ])

    def test_missing_commit_is_absence_not_an_error(self):
        """GitHub answers a commit lookup for a SHA the repo lacks with 422, not 404 (2026-10-09)."""
        from unittest import mock
        done = mock.Mock(returncode=1, stdout="", stderr="gh: No commit found for SHA: abc123 (HTTP 422)")
        with mock.patch.object(repo_moves.subprocess, "run", return_value=done):
            self.assertIsNone(repo_moves.gh_api("repos/x/y/commits/abc123"))
        boom = mock.Mock(returncode=1, stdout="", stderr="gh: Server Error (HTTP 502)")
        with mock.patch.object(repo_moves.subprocess, "run", return_value=boom), \
             mock.patch.object(repo_moves.time, "sleep"):
            with self.assertRaises(RuntimeError):
                repo_moves.gh_api("repos/x/y")

    def test_server_errors_are_retried_then_reported_per_page(self):
        """2026-10-09: one HTTP 502 ended a scan of every page; retry, then mark the page and go on."""
        from unittest import mock
        boom = mock.Mock(returncode=1, stdout="", stderr="gh: Server Error (HTTP 502)")
        ok = mock.Mock(returncode=0, stdout='{"full_name": "acme/demo"}', stderr="")
        with mock.patch.object(repo_moves.subprocess, "run", side_effect=[boom, ok]), \
             mock.patch.object(repo_moves.time, "sleep"):
            self.assertEqual(repo_moves.gh_api("repos/acme/demo"), {"full_name": "acme/demo"})
        root = self.make_tree("acme/demo")
        argv = ["repo_moves.py", "--root", str(root)]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(repo_moves, "classify", side_effect=RuntimeError("gh: Server Error (HTTP 502)")):
            self.assertEqual(repo_moves.main(), 1)

    def test_apply_rewrites_links_repo_field_and_override_key_but_not_lookalikes(self):
        body = ("See [React](https://github.com/facebook/react/blob/main/README.md) and "
                "https://github.com/facebook/react-native; the repo is still under `facebook/react`.")
        overrides = json.dumps({"facebook/react": {"none": True, "reason": "x"}}, indent=2)
        root = self.make_tree("facebook/react", body, {
            "flows/demo.json": '{"sources": ["https://github.com/facebook/react#readme"]}',
            "README.md": "| React | https://github.com/Facebook/React |",
            "tools/health_package_overrides.json": overrides,
        })
        report = repo_moves.apply_move(root, "facebook/react", "react/react")
        en = (root / "categories/demo/demo.md").read_text(encoding="utf-8")
        self.assertIn("repo: https://github.com/react/react\n", en)
        self.assertIn("https://github.com/react/react/blob/main/README.md", en)
        self.assertIn("https://github.com/facebook/react-native", en)
        self.assertIn('"https://github.com/react/react#readme"', (root / "flows/demo.json").read_text())
        self.assertIn("https://github.com/react/react |", (root / "README.md").read_text())
        self.assertEqual(list(json.loads((root / "tools/health_package_overrides.json").read_text())),
                         ["react/react"])
        self.assertEqual((root / "categories/demo/demo.zh.md").read_text(encoding="utf-8"), en)
        # Bare `owner/repo` mentions are prose: reported for a human, never rewritten.
        self.assertIn("`facebook/react`", en)
        self.assertEqual([hit["path"] for hit in report["bare_mentions"]],
                         ["categories/demo/demo.md", "categories/demo/demo.zh.md"])


if __name__ == "__main__":
    unittest.main()
