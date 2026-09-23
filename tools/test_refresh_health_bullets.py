#!/usr/bin/env python3
"""Tests for tools/refresh_health_bullets.py.

The dangerous version of this job is `sync-health-to-body.py --all`, which regenerates
the whole section and once destroyed hand-written analysis on 548 pages. These tests pin
the property that makes this tool safe instead: it only ever rewrites lines that are
already the generated bullet, and never changes the shape of the page.
"""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "refresh_health_bullets", Path(__file__).resolve().parent / "refresh_health_bullets.py")
refresher = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(refresher)
sync = refresher.load_sync_module()


FRONTMATTER = """---
name: Demo
slug: demo
health:
  schema: 1
  overall: B
  axes:
    maintenance:
      grade: A
      raw:
        last_commit_age_days: 3
        active_weeks_13: 12
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 10.0
        qualifying_issues: 4
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: demo
        downloads_last_month: 900000
    longevity:
      grade: A
      raw:
        repo_age_days: 2000
    governance:
      grade: B
      raw:
        top3_share: 0.5
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
---
"""


def page(body: str) -> str:
    return FRONTMATTER + body


class RefreshBulletsTest(unittest.TestCase):
    def run_on(self, text: str) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "demo.md"
            p.write_text(text, encoding="utf-8")
            count, _, new_text = refresher.refresh(p, sync)
            return count, (new_text if new_text is not None else text)

    def test_stale_generated_bullet_is_refreshed(self) -> None:
        count, out = self.run_on(page(
            "\n# Demo\n\n## Health & viability\n\n"
            "- **Longevity**: Grade C — 111 days old.\n"))
        self.assertEqual(count, 1)
        self.assertIn("Grade A — 2000 days old.", out)

    def test_hand_written_analysis_is_left_alone(self) -> None:
        """The whole point: a human's paragraph in the same section must survive."""
        hand = ("- **Backing & longevity.** Google has sunset other projects, but this one "
                "is a lighter successor and has gained broad adoption; longevity is A.\n")
        count, out = self.run_on(page(
            "\n# Demo\n\n## Health & viability\n\n"
            "- **Longevity**: Grade C — 111 days old.\n" + hand))
        self.assertEqual(count, 1)
        self.assertIn(hand.strip(), out)

    def test_a_correct_bullet_is_not_rewritten(self) -> None:
        count, _ = self.run_on(page(
            "\n# Demo\n\n## Health & viability\n\n"
            "- **Longevity**: Grade A — 2000 days old.\n"))
        self.assertEqual(count, 0)

    def test_bullets_outside_the_health_section_are_refreshed_too(self) -> None:
        """A generated bullet is generated wherever it sits; Caveats quotes them as well."""
        count, out = self.run_on(page(
            "\n# Demo\n\n## Health & viability\n\n- nothing\n\n"
            "## Caveats (unverified)\n\n"
            "- **Adoption**: Grade E — 1 monthly downloads via npmjs.org (package: demo).\n"))
        self.assertEqual(count, 1)
        self.assertIn("Grade A — 900,000 monthly downloads", out)

    def test_chinese_bullet_is_refreshed_with_chinese_text(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "demo.zh.md"
            p.write_text(page("\n# Demo\n\n## 健康度与可持续性\n\n"
                              "- **长青度**：Grade C——仓库已创建 111 天。\n"), encoding="utf-8")
            count, _, out = refresher.refresh(p, sync)
        self.assertEqual(count, 1)
        self.assertIn("Grade A——仓库已创建 2000 天。", out)

    def test_section_count_and_line_count_are_preserved(self) -> None:
        before = page("\n# Demo\n\n## Health & viability\n\n"
                      "- **Longevity**: Grade C — 111 days old.\n\n"
                      "## Tech stack\n\n- Python.\n\n## Caveats (unverified)\n\n- None.\n")
        count, out = self.run_on(before)
        self.assertEqual(count, 1)
        self.assertEqual([l for l in before.splitlines() if l.startswith("## ")],
                         [l for l in out.splitlines() if l.startswith("## ")])
        self.assertEqual(len(before.splitlines()), len(out.splitlines()))

    def test_a_page_without_a_health_block_is_untouched(self) -> None:
        count, out = self.run_on("---\nname: Demo\nslug: demo\n---\n\n# Demo\n\ntext\n")
        self.assertEqual(count, 0)
        self.assertIn("text", out)


if __name__ == "__main__":
    unittest.main()
