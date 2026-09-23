#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import tempfile
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint


HEALTH_BLOCK = """health:
  schema: 1
  computed_at: 2026-06-29T00:00:00Z
  overall: A
  overall_score: 4.0
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw: {}
    responsiveness:
      grade: A
      raw: {}
    adoption:
      grade: A
      raw: {}
    longevity:
      grade: A
      raw: {}
    governance:
      grade: A
      raw: {}
    risk_license:
      grade: A
      raw: {}
"""

UPSTREAM_BLOCK = """upstream:
  pushed_at: 2026-06-29T00:00:00Z
  default_branch: main
  default_branch_sha: 0123456789abcdef0123456789abcdef01234567
  archived: false
"""


def page_text(*, slug: str = "demo", zh: bool = False, health: bool = True, verdict: bool = True) -> str:
    title = "Demo"
    comparison = "横向对比" if zh else "Comparison"
    if zh:
        header = "| 替代品 | 是否收录 | 我们的评价 | 取舍 |" if verdict else "| 替代品 | 是否收录 | 取舍 |"
        row = "| Other | 未收录 | 优先用 Demo。 | Other is broader. |" if verdict else "| Other | 未收录 | Other is broader. |"
    else:
        header = "| Alternative | In index | Our verdict | Tradeoff |" if verdict else "| Alternative | In index | Tradeoff |"
        row = "| Other | not indexed | Prefer Demo for this case. | Other is broader. |" if verdict else "| Other | not indexed | Other is broader. |"
    separator = "|---|---|---|---|" if verdict else "|---|---|---|"
    health_block = HEALTH_BLOCK if health else ""
    card = f"![{slug} — {'健康度雷达' if zh else 'health radar'}](../../assets/health/{slug}{'.zh' if zh else ''}.svg)"
    return f"""---
name: Demo
slug: {slug}
repo: https://github.com/example/{slug}
category: demo
tags: [demo]
language: Python
license: MIT
maturity: active, 1 star (as of 2026-06)
last_verified: 2026-06-29
type: tool
{UPSTREAM_BLOCK}{health_block}---

# {title}

One-line summary.

{card if health else ''}

## {'何时使用' if zh else 'When to use'}

You use it.

## {'何时不用' if zh else 'When NOT to use'}

- Do not use it otherwise.

## {comparison}

{header}
{separator}
{row}

## {'技术栈' if zh else 'Tech stack'}

- Python.

## {'依赖' if zh else 'Dependencies'}

- None.

## {'运维难度' if zh else 'Ops difficulty'}

Low.

## {'健康度与可持续性' if zh else 'Health & viability'}

- Active.

## {'存疑（未验证）' if zh else 'Caveats (unverified)'}

- None.
"""


class LintContractTest(unittest.TestCase):
    def test_missing_health_block_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(health=False), encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("health: missing required frontmatter block" in e for e in rep.errors))

    def test_stale_health_computed_at_is_a_warning(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(), encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            # HEALTH_BLOCK's computed_at is 2026-06-29; 91 days later crosses STALE_DAYS=90.
            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 9, 28))
            self.assertTrue(any("health: computed_at 2026-06-29 is 91d old" in w for w in rep.warnings))

            fresh = lint.Report()
            lint.check_page(page, page.parent, root, set(), fresh, lint.dt.date(2026, 9, 27))
            self.assertFalse(any("health: computed_at" in w for w in fresh.warnings))

    def test_malformed_health_computed_at_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            broken = page_text().replace("computed_at: 2026-06-29T00:00:00Z", "computed_at: yesterday")
            page.write_text(broken, encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("health: computed_at missing or not an ISO UTC timestamp" in e for e in rep.errors))

    def test_comparison_requires_our_verdict_column(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(verdict=False), encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("Comparison table must include 'Our verdict'" in e for e in rep.errors))

    def test_summary_project_table_requires_health_column(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "INDEX.md"
            path.write_text("""# demo

| Project | Use when | Page |
|---|---|---|
| Demo | Use it. | [→](demo.md) |
""", encoding="utf-8")
            rep = lint.Report()

            lint.check_summary_health_columns(path, rep)

            self.assertTrue(any("summary table must include 'Health' column" in e for e in rep.errors))

    def test_missing_upstream_block_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text().replace(UPSTREAM_BLOCK, ""), encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("upstream: missing required frontmatter block" in e for e in rep.errors))

    def _write_pair(self, root: Path, en: str, zh: str) -> Path:
        page = root / "categories" / "demo" / "demo.md"
        page.parent.mkdir(parents=True)
        page.write_text(en, encoding="utf-8")
        page.with_name("demo.zh.md").write_text(zh, encoding="utf-8")
        (root / "assets" / "health").mkdir(parents=True)
        (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")
        (root / "assets" / "health" / "demo.zh.svg").write_text("<svg />", encoding="utf-8")
        return page

    def test_empty_callouts_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            en = page_text().replace(
                "## When NOT to use",
                "## Callouts\n\n## When NOT to use",
            )
            zh = page_text(zh=True).replace(
                "## 何时不用",
                "## 指指点点\n\n## 何时不用",
            )
            page = self._write_pair(root, en, zh)
            rep = lint.Report()
            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))
            self.assertTrue(any("Callouts / 指指点点 is empty" in e for e in rep.errors))

    def test_one_sided_callouts_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            en = page_text().replace(
                "## When NOT to use",
                "## Callouts\n\nA leftover judgment.\n\n## When NOT to use",
            )
            zh = page_text(zh=True)
            page = self._write_pair(root, en, zh)
            rep = lint.Report()
            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))
            self.assertTrue(any("presence must match the bilingual sibling" in e for e in rep.errors))

    def test_callouts_after_caveats_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            en = page_text() + "\n## Callouts\n\nA leftover judgment.\n"
            zh = page_text(zh=True) + "\n## 指指点点\n\n一条剩下的判断。\n"
            page = self._write_pair(root, en, zh)
            rep = lint.Report()
            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))
            self.assertTrue(any("must sit between When to use and How it works" in e for e in rep.errors))

    def test_frontmatter_parity_detects_nested_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            cat = root / "categories" / "demo"
            cat.mkdir(parents=True)
            page = cat / "demo.md"
            sibling = cat / "demo.zh.md"
            page.write_text(page_text(), encoding="utf-8")
            sibling.write_text(page_text(zh=True).replace("maintenance:\n      grade: A", "maintenance:\n      grade: E"), encoding="utf-8")

            lint.check_page(page, cat, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("frontmatter drift vs demo.zh.md" in e for e in rep.errors))

    def test_comparison_row_width_must_match_header(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            broken = page_text().replace(
                "| Other | not indexed | Prefer Demo for this case. | Other is broader. |",
                "| Other | not indexed | Prefer Demo for this case. |",
            )
            page.write_text(broken, encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("Comparison table row has 3 columns, expected 4" in e for e in rep.errors))


    def test_future_last_verified_is_an_error(self) -> None:
        """A date ahead of the comparison clock is an error, not a warning."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            rep = lint.Report()
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text().replace("last_verified: 2026-06-29", "last_verified: 2026-06-30"), encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("last_verified 2026-06-30 is in the future" in e for e in rep.errors))

    def test_today_utc_is_the_clock_the_gate_uses(self) -> None:
        """main() must read the UTC date, not the runner's local date.

        Regression: a page written at 00:05 UTC+8 carried `last_verified: <local tomorrow>`,
        passed locally and failed CI (`is in the future`). Patching today_utc to one day before
        the page's date must therefore fail the run.
        """
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(), encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg />", encoding="utf-8")

            out = io.StringIO()
            with mock.patch.object(lint, "today_utc", lambda: lint.dt.date(2026, 6, 28)), \
                 mock.patch.object(sys, "argv", ["lint.py", "--root", str(root)]), \
                 contextlib.redirect_stdout(out):
                code = lint.main()

            self.assertEqual(code, 1)
            self.assertIn("last_verified 2026-06-29 is in the future (UTC today is 2026-06-28)", out.getvalue())

    def test_today_utc_ignores_a_local_clock_ahead_of_utc(self) -> None:
        """The helper is UTC-based, so it cannot inherit a local clock ahead of UTC."""
        utc_today = lint.dt.datetime.now(lint.dt.timezone.utc).date()
        self.assertEqual(lint.today_utc(), utc_today)


def adoption_block(grade: str, raw_lines: list[str]) -> str:
    """A full health block whose adoption axis carries `grade` and the given raw keys."""
    raw = "\n".join(f"        {line}" for line in raw_lines) if raw_lines else "        {}"
    body = "raw:\n" + raw if raw_lines else "raw: {}"
    return HEALTH_BLOCK.replace(
        "    adoption:\n      grade: A\n      raw: {}\n",
        f"    adoption:\n      grade: {grade}\n      " + body + "\n",
    )


class AdoptionEvidenceGateTest(unittest.TestCase):
    """An adoption grade must be traceable to evidence on the page itself.

    Both gates close bugs that shipped: 39 pages carried `E` with no package matched at
    all, and the by-name lookup once attached a stranger's package as canonical.
    """

    def check(self, block: str) -> lint.Report:
        rep = lint.Report()
        fmtext = "repo: https://github.com/example/demo\n"
        lint.check_adoption_evidence(Path("categories/demo/demo.md"), fmtext, block, rep)
        return rep

    def errors_for(self, block: str, needle: str) -> list[str]:
        return [e for e in self.check(block).errors if needle in e]

    def test_e_without_any_count_is_an_error(self) -> None:
        block = adoption_block("E", ["registry: null", "canonical_package: null"])
        self.assertTrue(self.errors_for(block, "carries no measured count"))

    def test_e_with_all_counts_null_is_an_error(self) -> None:
        block = adoption_block("E", ["dependent_repos_count: null",
                                     "downloads_last_month: null"])
        self.assertTrue(self.errors_for(block, "carries no measured count"))

    def test_e_with_a_measured_zero_is_allowed(self) -> None:
        """Zero installs is a real measurement; only the absence of a number is a gap."""
        block = adoption_block("E", ["canonical_package: demo",
                                     "dependent_repos_count: 0",
                                     "downloads_last_month: 0"])
        self.assertEqual(self.errors_for(block, "carries no measured count"), [])

    def test_e_backed_by_an_install_channel_is_allowed(self) -> None:
        block = adoption_block("E", ["canonical_package: null", "release_downloads: 12"])
        self.assertEqual(self.errors_for(block, "carries no measured count"), [])

    def test_unrelated_grade_without_counts_is_not_flagged(self) -> None:
        """Only E asserts 'measurably unadopted', so only E owes a number."""
        block = adoption_block("?", ["registry: null", "canonical_package: null"])
        self.assertEqual(self.errors_for(block, "carries no measured count"), [])

    def test_na_contradicted_by_its_own_count_is_an_error(self) -> None:
        """N/A says no install event exists; a real count on the same page refutes that.

        Not hypothetical: `android/skills` is a skill-pack — the type N/A was introduced
        for — yet it ships release assets with 166,633 downloads, so it is graded, not
        excused. The scorer already tries install channels before conceding N/A; this
        gate keeps that ordering from silently regressing.
        """
        block = adoption_block("N/A", ["canonical_package: null",
                                       "release_downloads: 166633"])
        self.assertTrue(self.errors_for(block, "contradicts its own evidence"))

    def test_na_with_no_counts_is_allowed(self) -> None:
        block = adoption_block("N/A", ["canonical_package: null",
                                       "release_downloads: null"])
        self.assertEqual(self.errors_for(block, "contradicts its own evidence"), [])

    def test_canonical_package_unrelated_to_the_repo_is_an_error(self) -> None:
        """jaeger once reported `digitalbanking` (NuGet, 1034 downloads) as its package."""
        block = adoption_block("D", ["canonical_package: digitalbanking",
                                     "downloads_last_month: 1034"])
        self.assertTrue(self.errors_for(block, "matches neither"))

    def test_canonical_package_matching_the_repo_name_is_allowed(self) -> None:
        block = adoption_block("A", ["canonical_package: demo",
                                     "downloads_last_month: 900000"])
        self.assertEqual(self.errors_for(block, "matches neither"), [])

    def test_canonical_package_scoped_to_the_owner_is_allowed(self) -> None:
        """The monorepo case: `@mui/material` for `mui/material-ui`."""
        block = adoption_block("A", ["canonical_package: \"@example/anything\"",
                                     "downloads_last_month: 900000"])
        self.assertEqual(self.errors_for(block, "matches neither"), [])

    def test_absent_canonical_package_is_not_flagged(self) -> None:
        block = adoption_block("B", ["canonical_package: null",
                                     "homebrew_installs_90d: 4000"])
        self.assertEqual(self.errors_for(block, "matches neither"), [])

    def test_gate_runs_from_check_page_on_a_real_page(self) -> None:
        """Wiring check: the gate must be reachable through the normal lint entry point.

        A check that is never called is worse than no check — this repo already shipped a
        '?' warning that silently matched nothing across 600 pages.
        """
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            bad = adoption_block("E", ["registry: null", "canonical_package: null"])
            page.write_text(page_text().replace(HEALTH_BLOCK, bad), encoding="utf-8")
            (root / "assets" / "health").mkdir(parents=True)
            (root / "assets" / "health" / "demo.svg").write_text("<svg/>", encoding="utf-8")

            rep = lint.Report()
            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))

            self.assertTrue(any("carries no measured count" in e for e in rep.errors),
                            f"gate did not fire through check_page; errors={rep.errors}")


if __name__ == "__main__":
    unittest.main()
