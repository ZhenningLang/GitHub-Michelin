#!/usr/bin/env python3
from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import tab_intake
from tab_intake import Ledger, RepoInfo, Row


class RepoKeyTest(unittest.TestCase):
    def test_strips_subpaths_query_and_case(self):
        self.assertEqual(tab_intake.repo_key("https://github.com/TanStack/Query/tree/main/docs?x=1"), "tanstack/query")
        self.assertEqual(tab_intake.repo_key("https://www.github.com/a/b.git"), "a/b")
        self.assertEqual(tab_intake.repo_key("https://github.com/a/b#readme"), "a/b")

    def test_non_repo_pages(self):
        for url in ("https://github.com/TanStack", "https://github.com/orgs/x/repos", "https://github.com/topics/llm",
                    "https://gist.github.com/a/b", "https://x.com/a/b", "https://github.com/trending/python"):
            self.assertIsNone(tab_intake.repo_key(url), url)

    def test_owner_page(self):
        self.assertEqual(tab_intake.owner_key("https://github.com/TanStack"), "TanStack")
        self.assertIsNone(tab_intake.owner_key("https://github.com/TanStack/query"))
        self.assertIsNone(tab_intake.owner_key("https://github.com/explore"))


class UserChromeTest(unittest.TestCase):
    APP = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    def test_picks_the_default_profile_process(self):
        ps = "\n".join([
            f"101 {self.APP}",
            f"102 {self.APP} --remote-debugging-port=9222 --user-data-dir=/tmp/x",
            f"103 {self.APP} --user-data-dir=/var/folders/tmp-profile",
            f"104 {self.APP[:-len('Google Chrome')]}../Frameworks/Google Chrome Helper (Renderer).app/x --type=renderer",
        ])
        self.assertEqual(tab_intake.user_chrome_pid(ps), "101")

    def test_explicit_default_profile_with_space_in_path(self):
        # the real command line after a Chrome self-restart (2026-09-30)
        ps = (f"31822 {self.APP} --origin-trial-disabled-features=CanvasTextNg|X "
              f"--user-data-dir={tab_intake.DEFAULT_PROFILE} --restart\n"
              f"9 {self.APP} --user-data-dir=/tmp/other profile --no-first-run")
        self.assertEqual(tab_intake.user_chrome_pid(ps), "31822")

    def test_defers_when_ambiguous_or_absent(self):
        with self.assertRaises(SystemExit):
            tab_intake.user_chrome_pid(f"1 {self.APP}\n2 {self.APP}")
        with self.assertRaises(SystemExit):
            tab_intake.user_chrome_pid("")


class LedgerTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "tabs-2026-09-30" / "ledger.md"

    def tearDown(self):
        self.tmp.cleanup()

    def test_roundtrip_keeps_preamble_and_rows(self):
        led = Ledger(self.path)
        self.assertTrue(led.add(Row("Foo/Bar", "add", "pending", "", "note|pipe", "foo/bar")))
        self.assertFalse(led.add(Row("foo/bar", "add", "pending")))  # case-insensitive dedupe
        led.save()
        text = self.path.read_text(encoding="utf-8")
        self.assertIn("2026-09-30 (UTC)", text)
        self.assertIn("note／pipe", text)  # a pipe in a note must not add a column
        again = Ledger(self.path)
        self.assertEqual([r.repo for r in again.rows], ["Foo/Bar"])
        self.assertEqual(again.find("FOO/BAR").note, "note／pipe")

    def test_reads_existing_ledger_format(self):
        self.path.parent.mkdir(parents=True)
        self.path.write_text(
            "# Tab intake ledger — 2026-09-30 (UTC)\n\ncustom preamble\n\n"
            "| 规范名 | 动作 | 结果 | 页面路径 | 备注 | 标签里的写法 |\n|:---|:---|:---|:---|:---|:---|\n"
            "| OpenBMB/VoxCPM | add | done | categories/speech/voxcpm.md |  | openbmb/voxcpm |\n",
            encoding="utf-8",
        )
        led = Ledger(self.path)
        self.assertEqual(led.find("openbmb/voxcpm").result, "done")
        led.save()
        self.assertIn("custom preamble", self.path.read_text(encoding="utf-8"))


class ClassifyScanTest(unittest.TestCase):
    def classify(self, key, info, page=""):
        return tab_intake.classify(key, info, "ZhenningLang", lambda n: page)

    def test_actions(self):
        self.assertEqual(self.classify("a/b", None).action, "skip")
        self.assertEqual(self.classify("zhenninglang/x", RepoInfo("ZhenningLang/x")).action, "skip")
        self.assertEqual(self.classify("a/b", RepoInfo("a/b", size=0)).action, "skip")
        self.assertEqual(self.classify("a/b", RepoInfo("a/b")).action, "add")
        row = self.classify("a/b", RepoInfo("a/b"), page="categories/x/b.md")
        self.assertEqual((row.action, row.page, row.result), ("sync", "categories/x/b.md", "pending"))

    def test_notes_flag_fork_archive_redirect(self):
        row = self.classify("old/b", RepoInfo("New/b", fork=True, archived=True, parent="up/b"))
        self.assertEqual((row.repo, row.tab, row.action), ("New/b", "old/b", "add"))
        for word in ("重定向", "fork 自 up/b", "已归档"):
            self.assertIn(word, row.note)

    def test_scan_is_idempotent_and_retries_errors(self):
        led = Ledger(Path(tempfile.mkdtemp()) / "tabs-x" / "ledger.md")
        urls = ["https://github.com/a/b/issues/1", "https://github.com/A/B", "https://github.com/c/d",
                "https://github.com/SomeOrg", "https://x.com/y"]
        calls = []

        def resolve(key):
            calls.append(key)
            if key == "c/d":
                raise RuntimeError("rate limited")
            return RepoInfo("A/b")

        new, owners, errors = tab_intake.scan(led, urls, "me", resolve, lambda n: "")
        self.assertEqual([r.repo for r in new], ["A/b"])
        self.assertEqual(owners, ["SomeOrg"])
        self.assertEqual(len(errors), 1)
        new2, _, _ = tab_intake.scan(led, urls, "me", resolve, lambda n: "")
        self.assertEqual(new2, [])
        self.assertEqual(calls.count("a/b"), 1)  # already in the ledger: not re-resolved
        self.assertEqual(calls.count("c/d"), 2)  # failed: retried on the next scan

    def test_indexed_page_matches_frontmatter_repo(self):
        root = Path(tempfile.mkdtemp()) / "categories" / "x"
        root.mkdir(parents=True)
        (root / "b.md").write_text("---\nrepo: https://github.com/A/B\n---\n", encoding="utf-8")
        (root / "b.zh.md").write_text("---\nrepo: https://github.com/A/B\n---\n", encoding="utf-8")
        self.assertEqual(tab_intake.indexed_page("a/b", root.parent), "categories/x/b.md")
        self.assertEqual(tab_intake.indexed_page("a/bc", root.parent), "")


class CloseGuardTest(unittest.TestCase):
    def test_refuses_repos_not_done(self):
        tmp = Path(tempfile.mkdtemp()) / "tabs-x" / "ledger.md"
        led = Ledger(tmp)
        led.add(Row("a/b", "add", "pending"))
        led.save()
        with self.assertRaises(SystemExit) as cm:
            tab_intake.main(["close", "--ledger", str(tmp), "a/b"])
        self.assertIn("not `done`", str(cm.exception))


class UnionTextTest(unittest.TestCase):
    def test_table_rows_join_without_blank_line(self):
        text = "| h |\n|:--|\n<<<<<<< ours\n| a |\n=======\n| b |\n>>>>>>> theirs\ntail\n"
        self.assertEqual(tab_intake.union_text(text, is_index=False), "| h |\n|:--|\n| a |\n| b |\ntail\n")


if __name__ == "__main__":
    unittest.main()
