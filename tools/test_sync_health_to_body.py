#!/usr/bin/env python3
"""Regression tests for tools/sync-health-to-body.py.

This script rewrites a page's `Health & viability` section in place. It once scanned
forward to a hardcoded "## Caveats (unverified)" header, which meant it swallowed any
section in between (it deleted `## Tech stack` / `## Dependencies` / `## Ops difficulty`
from pyav and lit) and, on a page with no Caveats section, replaced the whole tail of
the file. These tests pin the section boundary and the H2-set invariant.
"""
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

# The module name has dashes, so it cannot be imported by name.
_SPEC = importlib.util.spec_from_file_location(
    "sync_health_to_body", Path(__file__).resolve().parent / "sync-health-to-body.py")
sync = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(sync)


FRONTMATTER = """---
name: Demo
slug: demo
health:
  schema: 1
  overall: B
  axes:
    maintenance:
      grade: B
      raw:
        last_commit_age_days: 5
        active_weeks_13: 7
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

HAND_WRITTEN = ("- **Maintenance (2026-07).** A long hand-written paragraph that carries "
                "analysis the frontmatter does not contain, such as why the vendor's "
                "strategic priorities matter here.\n")


def page(sections: list[tuple[str, str]]) -> str:
    body = "\n# Demo\n\nOne-line summary.\n\n"
    for head, text in sections:
        body += f"## {head}\n{text}\n"
    return FRONTMATTER + body


class SectionBoundaryTest(unittest.TestCase):
    def sync(self, text: str) -> str:
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "demo.md"
            p.write_text(text, encoding="utf-8")
            sync.sync_page(p)
            return p.read_text(encoding="utf-8")

    def heads(self, text: str) -> list[str]:
        return [l for l in text.splitlines() if l.startswith("## ")]

    def test_sections_between_health_and_caveats_survive(self) -> None:
        """The exact shape that cost pyav and lit three sections each."""
        before = page([
            ("Health & viability", HAND_WRITTEN),
            ("Tech stack", "- Python.\n"),
            ("Dependencies", "- None.\n"),
            ("Ops difficulty", "Low.\n"),
            ("Caveats (unverified)", "- None.\n"),
        ])
        after = self.sync(before)
        self.assertEqual(self.heads(before), self.heads(after))
        for kept in ("- Python.", "- None.", "Low."):
            self.assertIn(kept, after)

    def test_page_without_a_caveats_section_keeps_its_tail(self) -> None:
        """No Caveats header used to mean the rewrite ran to end of file."""
        before = page([
            ("Health & viability", HAND_WRITTEN),
            ("Tech stack", "- Rust.\n"),
        ])
        after = self.sync(before)
        self.assertEqual(self.heads(before), self.heads(after))
        self.assertIn("- Rust.", after)

    def test_the_health_section_is_actually_rewritten(self) -> None:
        """Guard against 'preserves everything' passing because it changed nothing."""
        before = page([
            ("Health & viability", HAND_WRITTEN),
            ("Caveats (unverified)", "- None.\n"),
        ])
        after = self.sync(before)
        self.assertNotIn("strategic priorities", after)
        self.assertIn("**Adoption**", after)

    def test_a_rewrite_that_would_drop_a_section_raises(self) -> None:
        """The output-side invariant, exercised by forcing the generator to emit an H2."""
        before = page([
            ("Health & viability", HAND_WRITTEN),
            ("Tech stack", "- Go.\n"),
            ("Caveats (unverified)", "- None.\n"),
        ])
        original = sync.axis_bullet_en
        sync.axis_bullet_en = lambda name, axis: "## Tech stack"
        try:
            with self.assertRaises(SystemExit) as ctx:
                self.sync(before)
            self.assertIn("changed the H2 set", str(ctx.exception))
        finally:
            sync.axis_bullet_en = original


class FrontmatterCoercionTest(unittest.TestCase):
    """The script reads frontmatter with the repo's stdlib mapping parser, not PyYAML.

    That parser returns every scalar as a string, but the bullets format with `{n:,}` and
    `{share:.1%}` and branch on `is not None` — so the coercion layer is load-bearing.
    Dropping PyYAML was necessary because CI installs no third-party packages and this
    was the only tool in the repo that imported it.
    """

    def test_null_becomes_none(self) -> None:
        self.assertIsNone(sync._coerce("null"))

    def test_integers_and_floats_are_numbers(self) -> None:
        self.assertEqual(sync._coerce("362917"), 362917)
        self.assertEqual(sync._coerce("0.876"), 0.876)
        self.assertEqual(sync._coerce("-3"), -3)

    def test_booleans(self) -> None:
        self.assertIs(sync._coerce("true"), True)
        self.assertIs(sync._coerce("false"), False)

    def test_version_like_strings_stay_strings(self) -> None:
        """`Apache-2.0` and `1.2.3` must not be mangled into numbers."""
        self.assertEqual(sync._coerce("Apache-2.0"), "Apache-2.0")
        self.assertEqual(sync._coerce("1.2.3"), "1.2.3")

    def test_empty_flow_mapping(self) -> None:
        """The scorer writes `raw: {}` for an axis with no evidence.

        The mapping parser hands that back as the string "{}", and a caller doing
        `raw.get(...)` then fails on a str — which it did, on android-skills.
        """
        self.assertEqual(sync._coerce("{}"), {})

    def test_inline_flow_mapping(self) -> None:
        self.assertEqual(sync._coerce("{ reason: no_package_structural }"),
                         {"reason": "no_package_structural"})

    def test_bullets_render_for_an_axis_with_no_evidence(self) -> None:
        """End to end: an axis whose raw is the `{}` literal must not raise."""
        fm, _ = sync.parse_frontmatter(page([("Health & viability", "x\n")]).replace(
            "    longevity:\n      grade: A\n      raw:\n        repo_age_days: 2000\n",
            "    longevity:\n      grade: \"?\"\n      raw: {}\n"))
        axis = fm["health"]["axes"]["longevity"]
        self.assertIn("Cannot be scored", sync.axis_bullet_en("longevity", axis))


class AllFlagGuardTest(unittest.TestCase):
    def test_all_refuses_without_the_acknowledgement_flag(self) -> None:
        """`--all` overwrites hand-written prose on every page, so it must be opt-in."""
        import contextlib
        import io
        import sys

        argv = sys.argv
        sys.argv = ["sync-health-to-body.py", "--all"]
        out = io.StringIO()
        try:
            with contextlib.redirect_stdout(out):
                rc = sync.main()
        finally:
            sys.argv = argv
        self.assertEqual(rc, 2)
        self.assertIn("--overwrite-prose", out.getvalue())


if __name__ == "__main__":
    unittest.main()
