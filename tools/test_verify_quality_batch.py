#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import quality_scan
import verify_quality_batch
from test_quality_scan import commit_all, init_git_repo, write_page


def documented_gated_categories() -> set[str]:
    """The gated list as AGENTS.md documents it.

    The set used to be hand-copied here as a third literal, which drifted twice in one session
    when a new gate was added to the scanner and to AGENTS.md but not to this file. Reading the
    documented list instead makes the contract in AGENTS.md the single source of truth and turns
    any divergence between doc and code into a test failure.
    """
    agents_md = Path(__file__).resolve().parents[1] / "AGENTS.md"
    match = re.search(r"deterministic categories\s*\(([^)]*)\)", agents_md.read_text(encoding="utf-8"))
    assert match, "AGENTS.md no longer documents the gated deterministic categories"
    return set(re.findall(r"`([^`]+)`", match.group(1)))


def run_verifier(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(Path(verify_quality_batch.__file__).resolve()), "--root", str(root), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


class VerifyQualityBatchTest(unittest.TestCase):
    def test_cli_writes_report_and_prints_pass_summary(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            write_page(root, "categories/clean/clean.md", "## Comparison\n")
            commit_all(root)
            report = root / "reports" / "batch.md"

            completed = run_verifier(root, "--scope", "categories/clean", "--report", str(report))

            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertTrue(report.exists())
            self.assertIn(f"Report: {report}", completed.stdout)
            self.assertIn("Final: PASS", completed.stdout)
            self.assertIn("Scan gated findings: PASS", completed.stdout)
            self.assertIn("Diff check: PASS", completed.stdout)

    def test_scoped_gated_finding_fails_but_out_of_scope_finding_does_not(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            write_page(root, "categories/scoped/bad.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/outside/bad.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/clean/clean.md", "## Comparison\n")
            commit_all(root)

            scoped_report = root / "scoped.md"
            scoped = run_verifier(root, "--scope", "categories/scoped", "--report", str(scoped_report))
            self.assertNotEqual(scoped.returncode, 0, scoped.stdout + scoped.stderr)
            self.assertIn("Final: FAIL", scoped.stdout)
            self.assertIn("generic-comparison-template=1", scoped.stdout)
            self.assertIn("categories/scoped/bad.md", scoped_report.read_text(encoding="utf-8"))
            self.assertNotIn("categories/outside/bad.md", scoped_report.read_text(encoding="utf-8"))

            clean_report = root / "clean.md"
            clean = run_verifier(root, "--scope", "categories/clean", "--report", str(clean_report))
            self.assertEqual(clean.returncode, 0, clean.stdout + clean.stderr)
            self.assertIn("Final: PASS", clean.stdout)
            self.assertNotIn("categories/outside/bad.md", clean_report.read_text(encoding="utf-8"))

    def test_non_project_scope_fails_instead_of_passing_empty_scan(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            write_page(root, "categories/clean/clean.md", "## Comparison\n")
            (root / "README.md").write_text("# Not a project page\n", encoding="utf-8")
            (root / "categories" / "clean" / "INDEX.md").write_text("# Index\n", encoding="utf-8")
            commit_all(root)

            for scope in ("README.md", "categories/clean/INDEX.md"):
                report = root / f"{scope.replace('/', '-')}.md"
                completed = run_verifier(root, "--scope", scope, "--report", str(report))

                self.assertNotEqual(completed.returncode, 0, completed.stdout + completed.stderr)
                self.assertTrue(report.exists())
                self.assertIn("Scan gated findings: FAIL", completed.stdout)
                self.assertIn("0 project pages scanned", completed.stdout)
                self.assertIn("Final: FAIL", completed.stdout)

    def test_gated_categories_match_documented_contract(self) -> None:
        self.assertEqual(quality_scan.GATED_DETERMINISTIC_CATEGORIES, documented_gated_categories())
        self.assertEqual(verify_quality_batch.GATED_CATEGORIES, documented_gated_categories())

    def test_diff_check_failure_under_scope_fails_verifier(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            page = write_page(root, "categories/clean/clean.md", "## Comparison\n")
            commit_all(root)
            page.write_text(page.read_text(encoding="utf-8") + "trailing whitespace   \n", encoding="utf-8")

            completed = run_verifier(root, "--scope", "categories/clean", "--report", str(root / "report.md"))

            self.assertNotEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertIn("Diff check: FAIL", completed.stdout)
            self.assertIn("trailing whitespace", completed.stdout)

    def test_full_runs_make_test_and_lint_and_propagates_failure(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            write_page(root, "categories/clean/clean.md", "## Comparison\n")
            (root / "Makefile").write_text(
                "test:\n\t@printf test >> make.log\n\t@exit 0\n\n"
                "lint:\n\t@printf lint >> make.log\n\t@exit 7\n",
                encoding="utf-8",
            )
            commit_all(root)
            subprocess.run(["git", "-C", str(root), "add", "Makefile"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            subprocess.run(
                ["git", "-C", str(root), "commit", "-m", "add makefile"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            without_full = run_verifier(root, "--scope", "categories/clean", "--report", str(root / "without.md"))
            self.assertEqual(without_full.returncode, 0, without_full.stdout + without_full.stderr)
            self.assertFalse((root / "make.log").exists())

            with_full = run_verifier(root, "--scope", "categories/clean", "--report", str(root / "with.md"), "--full")
            self.assertNotEqual(with_full.returncode, 0, with_full.stdout + with_full.stderr)
            self.assertEqual((root / "make.log").read_text(encoding="utf-8"), "testlint")
            self.assertIn("make test: PASS", with_full.stdout)
            self.assertIn("make lint: FAIL", with_full.stdout)


if __name__ == "__main__":
    unittest.main()
