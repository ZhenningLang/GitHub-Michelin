#!/usr/bin/env python3
from __future__ import annotations

import sys
import subprocess
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import quality_scan


ZERO_SHA = "0000000000000000000000000000000000000000"


def write_page(root: Path, rel: str, body: str, *, sha: str = "0123456789abcdef0123456789abcdef01234567") -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    slug = path.name.removesuffix(".zh.md").removesuffix(".md")
    path.write_text(
        f"""---
name: {slug}
slug: {slug}
repo: https://github.com/example/{slug}
category: {path.parent.name}
tags: [demo]
language: Python
license: MIT
maturity: active
last_verified: 2026-07-04
type: tool
upstream:
  pushed_at: 2026-07-04T00:00:00Z
  default_branch: main
  default_branch_sha: {sha}
  archived: false
health:
  schema: 1
  axes:
    maintenance:
      grade: ?
      reason: missing releases
    responsiveness:
      grade: B
---

# {slug}

{body}
""",
        encoding="utf-8",
    )
    return path


def write_page_with_health(root: Path, rel: str, body: str, health_axes: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    slug = path.name.removesuffix(".zh.md").removesuffix(".md")
    path.write_text(
        f"""---
name: {slug}
slug: {slug}
repo: https://github.com/example/{slug}
category: {path.parent.name}
tags: [demo]
language: Python
license: MIT
maturity: active
last_verified: 2026-07-04
type: tool
upstream:
  pushed_at: 2026-07-04T00:00:00Z
  default_branch: main
  default_branch_sha: 0123456789abcdef0123456789abcdef01234567
  archived: false
health:
  schema: 1
  axes:
{health_axes}---

# {slug}

{body}
""",
        encoding="utf-8",
    )
    return path


def git(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def init_git_repo(root: Path) -> None:
    git(root, "init")
    git(root, "config", "user.email", "test@example.com")
    git(root, "config", "user.name", "Quality Scan Test")


def commit_all(root: Path, message: str = "initial") -> None:
    git(root, "add", "categories")
    git(root, "commit", "-m", message)


def run_quality_scan_cli(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(Path(quality_scan.__file__).resolve()), "--root", str(root), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


class QualityScanTest(unittest.TestCase):
    def test_scope_file_limits_findings_to_scoped_page(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            scoped = write_page(root, "categories/demo/scoped.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/demo/out-of-scope.md", "Use this page for its stated niche.\n")

            result = quality_scan.scan(root, scope_paths=[scoped])

            self.assertEqual({finding.path for finding in result.findings}, {"categories/demo/scoped.md"})
            self.assertEqual(result.project_page_count, 1)
            self.assertEqual(result.indexed_project_page_count, 2)

    def test_scope_directory_limits_findings_to_directory_pages(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/selected/one.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/selected/two.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/sibling/other.md", "Use this page for its stated niche.\n")

            result = quality_scan.scan(root, scope_paths=[root / "categories" / "selected"])

            self.assertEqual(
                {finding.path for finding in result.findings},
                {"categories/selected/one.md", "categories/selected/two.md"},
            )
            self.assertEqual(result.project_page_count, 2)
            self.assertEqual(result.indexed_project_page_count, 3)

    def test_repeatable_scope_scans_union_of_selected_pages(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            first = write_page(root, "categories/first/one.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/second/two.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/third/three.md", "Use this page for its stated niche.\n")

            result = quality_scan.scan(root, scope_paths=[first, root / "categories" / "second"])

            self.assertEqual(
                {finding.path for finding in result.findings},
                {"categories/first/one.md", "categories/second/two.md"},
            )
            self.assertEqual(result.project_page_count, 2)
            self.assertEqual(result.indexed_project_page_count, 3)

    def test_scoped_scan_uses_all_pages_as_indexed_universe(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/target/long-target.md", "## Comparison\n")
            source = write_page(
                root,
                "categories/source/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Long Target | not indexed | Long Target is outside this scan scope but still indexed. |
""",
            )

            result = quality_scan.scan(root, scope_paths=[source])

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" for f in result.findings))
            self.assertEqual({finding.path for finding in result.findings}, {"categories/source/source.md"})

    def test_changed_only_clean_worktree_scans_no_pages(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            write_page(root, "categories/demo/demo.md", "Use this page for its stated niche.\n")
            commit_all(root)

            result = quality_scan.scan(root, changed_only=True)

            self.assertEqual(result.project_page_count, 0)
            self.assertEqual(result.findings, [])
            self.assertEqual(result.indexed_project_page_count, 1)

    def test_changed_only_includes_staged_unstaged_and_untracked_project_pages(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            staged = write_page(root, "categories/demo/staged.md", "## Comparison\n")
            unstaged = write_page(root, "categories/demo/unstaged.md", "## Comparison\n")
            write_page(root, "categories/demo/unchanged.md", "Use this page for its stated niche.\n")
            commit_all(root)

            staged.write_text(staged.read_text(encoding="utf-8") + "Use this page for its stated niche.\n", encoding="utf-8")
            git(root, "add", "categories/demo/staged.md")
            unstaged.write_text(unstaged.read_text(encoding="utf-8") + "Use this page for its stated niche.\n", encoding="utf-8")
            write_page(root, "categories/demo/untracked.md", "Use this page for its stated niche.\n")
            (root / "notes.md").write_text("Use this page for its stated niche.\n", encoding="utf-8")

            result = quality_scan.scan(root, changed_only=True)

            self.assertEqual(
                {finding.path for finding in result.findings if finding.category == "generic-comparison-template"},
                {"categories/demo/staged.md", "categories/demo/unstaged.md", "categories/demo/untracked.md"},
            )
            self.assertEqual(result.project_page_count, 3)

    def test_changed_only_excludes_deleted_markdown_project_pages(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            deleted = write_page(root, "categories/demo/deleted.md", "Use this page for its stated niche.\n")
            commit_all(root)
            deleted.unlink()

            result = quality_scan.scan(root, changed_only=True)

            self.assertEqual(result.project_page_count, 0)
            self.assertEqual(result.findings, [])

    def test_changed_only_scans_rename_destination_not_deleted_source(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            write_page(root, "categories/demo/old.md", "Use this page for its stated niche.\n")
            commit_all(root)

            git(root, "mv", "categories/demo/old.md", "categories/demo/new.md")
            result = quality_scan.scan(root, changed_only=True)

            self.assertEqual({finding.path for finding in result.findings}, {"categories/demo/new.md"})

    def test_changed_only_gate_exits_nonzero_for_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            page = write_page(root, "categories/demo/demo.md", "## Comparison\n")
            commit_all(root)
            page.write_text(page.read_text(encoding="utf-8") + "Use this page for its stated niche.\n", encoding="utf-8")

            result = run_quality_scan_cli(root, "--changed-only", "--fail-on-any-scoped")

            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("generic-comparison-template", result.stdout)

    def test_changed_only_gate_exits_zero_without_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            page = write_page(root, "categories/demo/demo.md", "## Comparison\n")
            commit_all(root)
            page.write_text(page.read_text(encoding="utf-8") + "\nAdditional non-gated prose.\n", encoding="utf-8")

            result = run_quality_scan_cli(root, "--changed-only", "--fail-on-any-scoped")

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_changed_only_gate_exits_zero_for_non_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            init_git_repo(root)
            page = write_page(root, "categories/demo/demo.md", "## Comparison\n")
            commit_all(root)
            page.write_text(page.read_text(encoding="utf-8").replace("default_branch_sha: 0123456789abcdef0123456789abcdef01234567", f"default_branch_sha: {ZERO_SHA}"), encoding="utf-8")

            result = run_quality_scan_cli(root, "--changed-only", "--fail-on-any-scoped")

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("zero-placeholder-upstream-sha", result.stdout)

    def test_scoped_gate_exits_nonzero_for_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            scoped = write_page(root, "categories/demo/scoped.md", "Use this page for its stated niche.\n")
            write_page(root, "categories/demo/out-of-scope.md", "Use this page for its stated niche.\n")

            result = run_quality_scan_cli(root, "--scope", str(scoped), "--fail-on-any-scoped")

            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("categories/demo/scoped.md", result.stdout)
            self.assertNotIn("categories/demo/out-of-scope.md", result.stdout)

    def test_scoped_gate_exits_zero_without_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            scoped = write_page(root, "categories/demo/scoped.md", "## Comparison\n")
            write_page(root, "categories/demo/out-of-scope.md", "Use this page for its stated niche.\n")

            result = run_quality_scan_cli(root, "--scope", str(scoped), "--fail-on-any-scoped")

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertNotIn("categories/demo/out-of-scope.md", result.stdout)

    def test_default_cli_remains_report_only_when_findings_exist(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.md", "Use this page for its stated niche.\n")

            result = run_quality_scan_cli(root)

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("generic-comparison-template", result.stdout)

    def test_repo_wide_gate_exits_nonzero_for_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.md", "Use this page for its stated niche.\n")

            result = run_quality_scan_cli(root, "--fail-on-gated")

            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("generic-comparison-template", result.stdout)

    def test_repo_wide_gate_exits_zero_without_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.md", "## Comparison\n")

            result = run_quality_scan_cli(root, "--fail-on-gated")

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_repo_wide_gate_ignores_non_gated_finding(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(
                root,
                "categories/demo/demo.md",
                "## Comparison\n",
                sha="0000000000000000000000000000000000000000",
            )

            result = run_quality_scan_cli(root, "--fail-on-gated")

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("zero-placeholder-upstream-sha", result.stdout)

    def test_detects_generic_templates_truncation_and_zero_sha(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(
                root,
                "categories/demo/demo.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Other | not indexed | Use this page for its stated niche before co. |
""",
                sha=ZERO_SHA,
            )

            result = quality_scan.scan(root)
            categories = {finding.category for finding in result.findings}

            self.assertIn("generic-comparison-template", categories)
            self.assertIn("truncation-fragment", categories)
            self.assertIn("zero-placeholder-upstream-sha", categories)

    def test_detects_chinese_generic_template(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.zh.md", "当前页用于它的主场景；如果更看重别的能力，再选 Other。")

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "generic-comparison-template" and f.evidence == "当前页用于它的主场景" for f in result.findings))

    def test_truncation_detection_skips_common_word_endings_and_node_js(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(
                root,
                "categories/demo/demo.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Other | not indexed | Configure by hand. Run the command. Track demand. Avoid land. Do not rebrand. Uses zustand. Runtime (Node.js) is supported. |
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "truncation-fragment" for f in result.findings))

    def test_truncation_detection_keeps_sampled_row_end_fragments(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(
                root,
                "categories/demo/demo.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Selenium | not indexed | Browser automation with trac. |
| Node option | not indexed | JavaScript library (Node. |
| Karpathy | not indexed | Use before co. |
| Partial | not indexed | Needs per-har. |
| Flowchart | not indexed | Actively developed and. |
""",
            )

            result = quality_scan.scan(root)
            evidence = {f.evidence for f in result.findings if f.category == "truncation-fragment"}

            self.assertEqual(evidence, {"trac.", "(Node.", "before co.", "per-har.", "and."})

    def test_detects_zh_links_to_english_when_sibling_exists(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/target.md", "## Comparison\n")
            write_page(root, "categories/demo/target.zh.md", "## 横向对比\n")
            write_page(root, "categories/demo/source.zh.md", "See [Target](target.md).")

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "zh-link-to-english-sibling" and "target.zh.md" in f.message for f in result.findings))

    def test_detects_indexed_link_marked_not_indexed_in_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/target.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| [Target](target.md) | not indexed | Target is already indexed. |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" for f in result.findings))

    def test_detects_chinese_indexed_link_marked_unindexed_in_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/target.zh.md", "## 横向对比\n")
            write_page(root, "categories/demo/target.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.zh.md",
                """## 横向对比

| 替代品 | 是否收录 | 我们的评价 |
|---|---|---|
| [Target](target.zh.md) | 未收录 | Target 已经收录。 |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" and "未收录" in f.evidence for f in result.findings))

    def test_detects_plain_text_indexed_slug_marked_not_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/yt-dlp.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/youtube-dl.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| yt-dlp | 未收录 | Pick it by default. |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" and "yt-dlp" in f.evidence for f in result.findings))

    def test_detects_plain_text_indexed_alias_marked_not_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/antfu-skills.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| antfu/skills | 未收录 | Personal skill collection. |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" and "antfu/skills" in f.evidence for f in result.findings))

    def test_detects_aggregate_plain_text_indexed_alternatives_marked_not_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/dimillian-skills.md", "## Comparison\n")
            write_page(root, "categories/demo/gstack.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Dimillian/Skills, gstack (other personal collections) | 未收录 | Same genre. |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(
                any(f.category == "indexed-page-marked-not-indexed" and "Dimillian/Skills" in f.evidence for f in result.findings)
            )

    def test_does_not_flag_short_global_plain_text_slug_collision(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/web-ui/react.md", "## Comparison\n")
            write_page(
                root,
                "categories/ai-code-review/react-doctor.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| eslint-plugin-react-hooks / react | 未收录 | Canonical linting rules for React hooks. |
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(
                any(f.category == "indexed-page-marked-not-indexed" and "eslint-plugin-react-hooks" in f.evidence for f in result.findings)
            )

    def test_mixed_comparison_status_row_does_not_mark_indexed_link_unindexed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/dimillian-skills.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| External / [dimillian-skills](dimillian-skills.md) | 未收录 / ✅ | Mixed row. |
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "indexed-page-marked-not-indexed" for f in result.findings))
            self.assertFalse(any(f.category == "composite-alternative-partly-indexed" for f in result.findings))

    def test_detects_composite_alternative_partly_marked_indexed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/svelte.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| [Svelte / SvelteKit](svelte.md) | ✅ | Composite row marks both indexed. |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "composite-alternative-partly-indexed" for f in result.findings))

    def test_partially_indexed_status_does_not_report_composite(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/mlt.md", "## Comparison\n")
            write_page(
                root,
                "categories/demo/source.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| [MLT](mlt.md) / Shotcut | 部分已收录 | Mixed row. |
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "composite-alternative-partly-indexed" for f in result.findings))

    def test_detects_cross_category_composite_plain_slug_marked_unindexed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/llm-training/unsloth.md", "## Comparison\n")
            write_page(
                root,
                "categories/on-device-ml/bitnet.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Unsloth / GPTQ-AWQ stacks | 未收录 | Mixed row. |
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "indexed-page-marked-not-indexed" and "Unsloth" in f.evidence for f in result.findings))

    def test_partially_indexed_status_allows_cross_category_composite_plain_slug(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/llm-training/unsloth.md", "## Comparison\n")
            write_page(
                root,
                "categories/on-device-ml/bitnet.md",
                """## Comparison

| Alternative | In index | Our verdict |
|---|---|---|
| Unsloth / GPTQ-AWQ stacks | 部分已收录 | Mixed row. |
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "indexed-page-marked-not-indexed" for f in result.findings))

    def test_counts_health_unknown_axes_by_axis_and_reason(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.md", "## Comparison\n")

            result = quality_scan.scan(root)

            self.assertEqual(result.health_unknowns[("maintenance", "missing releases")], 1)

    def test_counts_quoted_health_unknowns_from_unknowns_block(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = write_page(root, "categories/demo/demo.md", "## Comparison\n")
            page.write_text(
                page.read_text(encoding="utf-8")
                .replace("grade: ?", 'grade: "?"')
                .replace("      reason: missing releases\n", "")
                .replace("    responsiveness:\n      grade: B", "  unknowns:\n    maintenance: { reason: no_traffic }\n    responsiveness:\n      grade: B"),
                encoding="utf-8",
            )

            result = quality_scan.scan(root)

            self.assertEqual(result.health_unknowns[("maintenance", "no_traffic")], 1)

    def test_detects_health_prose_grade_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Responsiveness**: Grade C — median first-response time 4.2 hours across 2 qualifying issues/PRs.
""",
                """    responsiveness:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "health-prose-grade-drift" and "Responsiveness" in f.evidence for f in result.findings))

    def test_detects_chinese_health_prose_grade_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **响应速度**：Grade C，样本不足。
""",
                """    responsiveness:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "health-prose-grade-drift" and "响应速度" in f.evidence for f in result.findings))

    def test_chinese_governance_line_with_maintainer_word_is_not_maintenance_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **治理集中度**：Grade B，若核心维护者退出，项目仍有多人维护。
""",
                """    maintenance:
      grade: A
      raw: {}
    governance:
      grade: B
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift" for f in result.findings))

    def _raw_drift(self, body: str, axes: str, *, zh: bool = False) -> list:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            name = "demo.zh.md" if zh else "demo.md"
            write_page_with_health(root, f"categories/demo/{name}", body, axes)
            result = quality_scan.scan(root)
        return [f for f in result.findings if f.category == "health-prose-raw-drift"]

    def test_age_off_by_a_day_is_not_drift(self) -> None:
        """`repo_age_days` advances on its own, so prose is exact only the day it is written.

        Demanding equality made this check a clock: it reported 15 pages whose prose was
        1-4 days behind and would report them again the next day.
        """
        drift = self._raw_drift(
            "## Health & viability\n\n- **Longevity**: the repository was 432 days old.\n",
            "    longevity:\n      grade: A\n      raw:\n        repo_age_days: 433\n")
        self.assertEqual(drift, [])

    def test_a_genuinely_stale_age_is_still_drift(self) -> None:
        """The tolerance must not hide a page whose prose predates a real gap."""
        drift = self._raw_drift(
            "## Health & viability\n\n- **Longevity**: the repository was 432 days old.\n",
            "    longevity:\n      grade: A\n      raw:\n        repo_age_days: 2000\n")
        self.assertEqual(len(drift), 1, f"expected the stale age to be reported, got {drift}")

    def test_a_hundred_day_gap_on_a_young_repo_is_still_drift(self) -> None:
        """5% of 400 is 20 days; 100 days behind must not slip through."""
        drift = self._raw_drift(
            "## Health & viability\n\n- **Longevity**: the repository was 300 days old.\n",
            "    longevity:\n      grade: A\n      raw:\n        repo_age_days: 400\n")
        self.assertEqual(len(drift), 1)

    def test_a_share_rounded_to_two_decimals_is_not_drift(self) -> None:
        """Frontmatter stores 0.772; prose writes 0.77. That is how people write numbers."""
        drift = self._raw_drift(
            "## Health & viability\n\n- **Governance**: top-3 contributor share is 0.77.\n",
            "    governance:\n      grade: B\n      raw:\n        top3_share: 0.772\n")
        self.assertEqual(drift, [])

    def test_a_share_written_as_a_percentage_is_not_drift(self) -> None:
        drift = self._raw_drift(
            "## Health & viability\n\n- **Governance**: the top 3 hold 77.2% of commits.\n",
            "    governance:\n      grade: B\n      raw:\n        top3_share: 0.772\n")
        self.assertEqual(drift, [])

    def test_a_wrong_share_is_still_drift(self) -> None:
        drift = self._raw_drift(
            "## Health & viability\n\n- **Governance**: top-3 contributor share is 0.41.\n",
            "    governance:\n      grade: B\n      raw:\n        top3_share: 0.772\n")
        self.assertEqual(len(drift), 1)

    def test_a_zero_stated_in_words_is_not_drift(self) -> None:
        """"there are no registry packages" states 0 more clearly than the digit would."""
        drift = self._raw_drift(
            "## Health & viability\n\n- **Adoption**: there are no registry packages to "
            "measure dependents against, so the only signal is attention.\n",
            "    adoption:\n      grade: E\n      raw:\n        dependent_repos_count: 0\n")
        self.assertEqual(drift, [])

    def test_a_chinese_zero_stated_in_words_is_not_drift(self) -> None:
        drift = self._raw_drift(
            "## 健康度与可持续性\n\n- **采用广度**：没有可测的 registry 包，依赖数无从统计。\n",
            "    adoption:\n      grade: E\n      raw:\n        dependent_repos_count: 0\n",
            zh=True)
        self.assertEqual(drift, [])

    def test_a_nonzero_count_is_not_excused_by_the_word_no(self) -> None:
        """The words-for-zero escape applies only when the value really is zero.

        The line has to carry a number of its own, because a line with no numbers is
        never compared at all — that is pre-existing behaviour, not part of this change.
        """
        drift = self._raw_drift(
            "## Health & viability\n\n- **Adoption**: there are no dependent repos worth "
            "reporting; dependent_repos_count sits at 7.\n",
            "    adoption:\n      grade: D\n      raw:\n        dependent_repos_count: 4200\n")
        self.assertEqual(len(drift), 1)

    def test_detects_grade_drift_outside_the_health_section(self) -> None:
        """A page explains its grades wherever the explanation belongs.

        apache-poi's stale paragraph — "overall D, capped, risk/license E" — sat in
        Caveats, so scanning only `Health & viability` never saw it.
        """
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- Nothing to declare here.

## Caveats (unverified)

- **Radar note.** Governance is D because contribution is concentrated.
""",
                """    governance:
      grade: B
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "health-prose-grade-drift"
                                and "Governance is D" in f.evidence
                                for f in result.findings))

    def test_detects_hand_written_grade_claim_without_the_word_grade(self) -> None:
        """The generated template says "Grade B"; a human writes "longevity is C"."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Lindy / governance:** health longevity is C and governance is D.
""",
                """    longevity:
      grade: B
      raw: {}
    governance:
      grade: D
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            drift = [f for f in result.findings if f.category == "health-prose-grade-drift"]
            self.assertEqual(len(drift), 1, f"expected only the longevity claim, got {drift}")
            self.assertIn("longevity grade B", drift[0].message)

    def test_chinese_hand_written_claim_is_attributed_to_the_nearest_axis(self) -> None:
        """`longevity 为 C；维护者集中，governance 为 D` states two grades, both correct.

        Taking the first axis word in the line instead of the nearest one reads it as
        governance=C and maintenance=D — two findings, both wrong, on a clean line.
        """
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **Lindy / 治理：** 项目年轻，health 中 longevity 为 C；维护者集中，governance 为 D。
""",
                """    maintenance:
      grade: A
      raw: {}
    longevity:
      grade: C
      raw: {}
    governance:
      grade: D
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift"
                                 for f in result.findings))

    def test_a_contrast_is_not_read_as_a_claim(self) -> None:
        """"so this axis is B rather than A" states B, not A.

        Three of the first four corpus hits were this shape, including one on this repo's
        own apache-poi page.
        """
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Governance**: single-vendor, so this axis is B rather than A.
""",
                """    governance:
      grade: B
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift"
                                 for f in result.findings))

    def test_a_history_is_not_read_as_a_claim(self) -> None:
        """"it used to grade E" describes the past, not the current grade."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Caveats (unverified)

- The scorer used to read that null as no license and grade E; that was a bug, fixed.
""",
                """    risk_license:
      grade: A
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift"
                                 for f in result.findings))

    def test_a_contrast_does_not_hide_a_real_claim_elsewhere_on_the_line(self) -> None:
        """Suppressing contrasts must not suppress a genuine claim in the same sentence."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Longevity** is C, so the axis is B rather than A.
""",
                """    longevity:
      grade: A
      raw: {}
    governance:
      grade: B
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            drift = [f for f in result.findings if f.category == "health-prose-grade-drift"]
            self.assertEqual(len(drift), 1, f"expected the longevity claim only, got {drift}")
            self.assertIn("longevity grade A", drift[0].message)

    def test_license_identifiers_are_not_read_as_grades(self) -> None:
        """`CC BY-SA 4.0` and `BSD-3-Clause` contain letters that are not grades."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Risk / License**: content is CC BY-SA 4.0 and the code is BSD-3-Clause.
""",
                """    risk_license:
      grade: A
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift"
                                 for f in result.findings))

    def test_frontmatter_grades_are_not_read_as_prose(self) -> None:
        """Scanning the whole file instead of the body would match the health block itself."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- Nothing to declare.
""",
                """    maintenance:
      grade: A
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift"
                                 for f in result.findings))

    def test_matching_chinese_health_prose_grade_is_not_reported(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **维护活跃度**：Grade A，提交活跃。
""",
                """    maintenance:
      grade: A
      raw: {}
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-grade-drift" for f in result.findings))

    def test_detects_health_prose_raw_drift_for_ttfr(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Responsiveness**: Grade A — median first-response time 8.7 hours across 38 qualifying issues/PRs.
""",
                """    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 12.6
        qualifying_issues: 38
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "health-prose-raw-drift" and "median_ttfr_hours=12.6" in f.message for f in result.findings))

    def test_detects_chinese_health_prose_raw_drift_for_repo_age(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **长青度**：Grade A——仓库已创建 2567 天。
""",
                # Was 2568 — a one-day gap. That is no longer drift: `repo_age_days`
                # advances by one every day a page is not rescored, so equality made the
                # check a clock (15 real pages, 1-4 days behind, reported daily). The gap
                # here is now large enough to be real staleness, which is what this test
                # was protecting: that a Chinese line gets scanned for raw drift at all.
                """    longevity:
      grade: A
      raw:
        repo_age_days: 3600
""",
            )

            result = quality_scan.scan(root)

            self.assertTrue(any(f.category == "health-prose-raw-drift" and "repo_age_days=3600" in f.message for f in result.findings))

    def test_matching_health_prose_raw_value_is_not_reported(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Longevity**: Grade A — 2,568 days old.
""",
                """    longevity:
      grade: A
      raw:
        repo_age_days: 2568
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-raw-drift" for f in result.findings))

    def test_health_prose_raw_drift_ignores_unrelated_numbers(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Adoption**: Grade A — ~53k stars plus de-facto ecosystem status.
""",
                """    adoption:
      grade: A
      raw:
        downloads_last_month: 80749282
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-raw-drift" for f in result.findings))

    def test_health_raw_values_parse_numeric_field_names(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = write_page_with_health(
                root,
                "categories/demo/demo.md",
                "## Health & viability\n",
                """    governance:
      grade: A
      raw:
        top3_share: 0.149
        top1_share: 0.062
        active_maintainers_12mo: 177
""",
            )

            values = quality_scan.health_axis_raw_values(page.read_text(encoding="utf-8"))

            self.assertEqual(values[("governance", "top3_share")], "0.149")
            self.assertEqual(values[("governance", "top1_share")], "0.062")
            self.assertEqual(values[("governance", "active_maintainers_12mo")], "177")

    def test_dependent_substring_does_not_trigger_dependents_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Adoption**: Grade D — not independently confirmed by this pass.
""",
                """    adoption:
      grade: D
      raw:
        dependent_repos_count: 1
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-raw-drift" for f in result.findings))

    def test_ratio_raw_value_matches_percent_prose(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.md",
                """## Health & viability

- **Governance**: Grade A — top-3 contributor share 14.9%.
""",
                """    governance:
      grade: A
      raw:
        top3_share: 0.149
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-raw-drift" for f in result.findings))

    def test_chinese_ratio_raw_value_matches_percent_prose(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page_with_health(
                root,
                "categories/demo/demo.zh.md",
                """## 健康度与可持续性

- **治理集中度**：Grade A——前三贡献者占比 14.9%。
""",
                """    governance:
      grade: A
      raw:
        top3_share: 0.149
""",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.category == "health-prose-raw-drift" for f in result.findings))

    def test_report_labels_reviewer_only_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/demo.md", "## Comparison\n")

            report = quality_scan.render_report(quality_scan.scan(root), root)

            self.assertIn("## Reviewer-only dimensions", report)
            self.assertIn("not hard failures", report)
            self.assertIn("weak or non-second-person `When to use` signals", report)


    def test_summary_matrix_row_marking_indexed_page_not_indexed_is_found(self) -> None:
        """INDEX matrices are user-visible claims; the page scan skips them (it only reads pages).

        Regression: `Letta (MemGPT) / Zep / Cognee | 未收录` in categories/agent-memory/INDEX.md sat
        stale while all three had their own pages, because is_project_page() excludes INDEX files.
        """
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.md", "## Comparison\n")
            write_page(root, "categories/demo/beta.md", "## Comparison\n")
            (root / "categories" / "demo" / "INDEX.md").write_text(
                "## Comparison matrix\n\n"
                "| Option | Indexed | Health | One-line tradeoff |\n"
                "| --- | --- | --- | --- |\n"
                "| alpha / beta | 未收录 | — | Both are named in the pages. |\n"
                "| [alpha](alpha.md) | ✅ | — | Fine: it points at a page. |\n"
                "| Other / alpha | partly indexed | — | Fine: the status says partly. |\n",
                encoding="utf-8",
            )

            result = quality_scan.scan(root)

            stale = [f for f in result.findings if f.category == "indexed-page-marked-not-indexed"]
            self.assertEqual(len(stale), 1)
            self.assertEqual(stale[0].path, "categories/demo/INDEX.md")
            self.assertEqual(stale[0].severity, "high")
            self.assertIn("alpha / beta", stale[0].evidence)

    def test_summary_matrix_row_without_pages_is_not_flagged(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.md", "## Comparison\n")
            (root / "categories" / "demo" / "INDEX.md").write_text(
                "## Comparison matrix\n\n"
                "| Option | Indexed | Health | One-line tradeoff |\n"
                "| --- | --- | --- | --- |\n"
                "| Kibana / Datadog | 未收录 | — | Not repositories, so out of scope. |\n",
                encoding="utf-8",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.path.endswith("INDEX.md") for f in result.findings))


    def test_indexed_page_marked_non_repo_is_gated(self) -> None:
        """`非仓库` claims the alternative is not a repository; a page proves otherwise."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.md", "## Comparison\n")
            (root / "categories" / "demo" / "INDEX.md").write_text(
                "## Comparison matrix\n\n"
                "| Option | Indexed | Health | One-line tradeoff |\n"
                "| --- | --- | --- | --- |\n"
                "| [alpha](alpha.md) | 非仓库 | — | Wrong: it has a page. |\n",
                encoding="utf-8",
            )

            result = quality_scan.scan(root)

            contradictions = [f for f in result.findings if f.category == "indexed-page-marked-non-repo"]
            self.assertEqual(len(contradictions), 1)
            self.assertEqual(contradictions[0].severity, "high")

    def test_non_repo_row_without_a_page_is_not_flagged(self) -> None:
        """A hosted service marked `非仓库` is the correct status — out of scope, not debt."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.md", "## Comparison\n")
            (root / "categories" / "demo" / "INDEX.md").write_text(
                "## Comparison matrix\n\n"
                "| Option | Indexed | Health | One-line tradeoff |\n"
                "| --- | --- | --- | --- |\n"
                "| Kibana / Datadog | 非仓库 | — | Hosted dashboards, not repositories. |\n",
                encoding="utf-8",
            )

            result = quality_scan.scan(root)

            self.assertFalse(any(f.path.endswith("INDEX.md") for f in result.findings))

    def test_legacy_combined_non_repo_status_is_report_only(self) -> None:
        """`未收录（非仓库）` still reads correctly; it is normalized by the sweep, not gated."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.md", "## Comparison\n")
            (root / "categories" / "demo" / "INDEX.md").write_text(
                "## Comparison matrix\n\n"
                "| Option | Indexed | Health | One-line tradeoff |\n"
                "| --- | --- | --- | --- |\n"
                "| Conductor | 未收录（非仓库） | — | Closed macOS app. |\n",
                encoding="utf-8",
            )

            result = quality_scan.scan(root)

            legacy = [f for f in result.findings if f.category == "non-repo-status-legacy-form"]
            self.assertEqual(len(legacy), 1)
            self.assertEqual(legacy[0].severity, "low")
            self.assertNotIn("non-repo-status-legacy-form", quality_scan.GATED_DETERMINISTIC_CATEGORIES)

    def test_zh_lead_left_as_english_tagline_is_reported(self) -> None:
        """The cheapest thing a generator puts under the H1 is the upstream README tagline."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.zh.md",
                       "\U0001F422 Open-Source Evaluation & Testing library for LLM Agents\n\n## 横向对比\n")

            result = quality_scan.scan(root)

            leads = [f for f in result.findings if f.category == "zh-lead-not-chinese"]
            self.assertEqual(len(leads), 1)
            self.assertEqual(leads[0].severity, "medium")
            self.assertNotIn("zh-lead-not-chinese", quality_scan.GATED_DETERMINISTIC_CATEGORIES)

    def test_zh_lead_with_english_proper_nouns_is_not_flagged(self) -> None:
        """An ordinary Chinese lead is held under 100% CJK by names it cannot translate."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.zh.md",
                       "JetBrains \u7cfb IDE\uff08IntelliJ IDEA\u3001PyCharm\u3001GoLand\u3001WebStorm\uff09"
                       "\u7684 Vim \u6a21\u62df\u63d2\u4ef6\u3002\n\n## \u6a2a\u5411\u5bf9\u6bd4\n")

            result = quality_scan.scan(root)

            self.assertEqual([f for f in result.findings if f.category.startswith("zh-lead-not-chinese")], [])

    def test_english_page_lead_is_never_flagged(self) -> None:
        """The rule is about an untranslated mirror, so it only applies to `.zh.md`."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.md",
                       "The grammar-constrained decoding engine most stacks already run.\n\n## Comparison\n")

            result = quality_scan.scan(root)

            self.assertEqual([f for f in result.findings if f.category.startswith("zh-lead-not-chinese")], [])

    def test_zh_lead_not_chinese_is_gated_once_reverified(self) -> None:
        """Re-verifying a page is when the untranslated lead has to be written."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = write_page(root, "categories/demo/alpha.zh.md",
                              "Download market data from Yahoo! Finance's API\n\n## \u6a2a\u5411\u5bf9\u6bd4\n")
            page.write_text(page.read_text(encoding="utf-8").replace(
                "last_verified: 2026-07-04", f"last_verified: {quality_scan.STUB_BLOCKED_FROM}"), encoding="utf-8")

            result = quality_scan.scan(root)

            gated = [f for f in result.findings if f.category == "zh-lead-not-chinese-reverified"]
            self.assertEqual(len(gated), 1)
            self.assertEqual(gated[0].severity, "high")
            self.assertIn("zh-lead-not-chinese-reverified", quality_scan.GATED_DETERMINISTIC_CATEGORIES)

    def test_short_zh_lead_is_not_flagged(self) -> None:
        """Too short for the ratio to mean anything — do not adjudicate it."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            write_page(root, "categories/demo/alpha.zh.md", "`qpdf`\n\n## \u6a2a\u5411\u5bf9\u6bd4\n")

            result = quality_scan.scan(root)

            self.assertEqual([f for f in result.findings if f.category.startswith("zh-lead-not-chinese")], [])


if __name__ == "__main__":
    unittest.main()
