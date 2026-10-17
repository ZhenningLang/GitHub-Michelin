#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import json
import re
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
                "## Q&A\n\n## When NOT to use",
            )
            zh = page_text(zh=True).replace(
                "## 何时不用",
                "## 快问快答\n\n## 何时不用",
            )
            page = self._write_pair(root, en, zh)
            rep = lint.Report()
            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))
            self.assertTrue(any("Q&A / 快问快答 is empty" in e for e in rep.errors))

    def test_one_sided_callouts_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            en = page_text().replace(
                "## When NOT to use",
                "## Q&A\n\nA leftover judgment.\n\n## When NOT to use",
            )
            zh = page_text(zh=True)
            page = self._write_pair(root, en, zh)
            rep = lint.Report()
            lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 6, 29))
            self.assertTrue(any("presence must match the bilingual sibling" in e for e in rep.errors))

    def test_callouts_after_caveats_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            en = page_text() + "\n## Q&A\n\nA leftover judgment.\n"
            zh = page_text(zh=True) + "\n## 快问快答\n\n一条剩下的判断。\n"
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


def section_chunks(text: str) -> tuple[str, dict[str, str]]:
    parts = re.split(r"(?m)(^##[^\n]*\n)", text)
    return parts[0], {parts[i].strip(): parts[i + 1] for i in range(1, len(parts), 2)}


def contract_page(zh: bool = False, *, v2: bool = True, qa: bool = True,
                  flow: bool = True, ptype: str = "tool") -> str:
    """Independent complete fixture; legacy page_text remains unchanged."""
    prefix, chunks = section_chunks(page_text(zh=zh))
    date = "2026-10-13" if v2 else "2026-06-29"
    prefix = prefix.replace("last_verified: 2026-06-29", f"last_verified: {date}").replace("type: tool", f"type: {ptype}")
    when, negative, comparison = ("何时使用", "何时不用", "横向对比") if zh else ("When to use", "When NOT to use", "Comparison")
    q = "快问快答" if zh else "Q&A"
    quick = ("快速上手" if v2 else "怎么用起来") if zh else ("Quick start" if v2 else "How it works")
    key = "技术要点" if zh else "Key techniques"
    chunks[f"## {q}"] = "\nA leftover judgment.\n\n"
    chunks[f"## {quick}"] = f"\n{'安装后调用接口。' if zh else 'Install it and call its API.'}\n\n![Demo](../../assets/flow/demo{'.zh' if zh else ''}.svg)\n\n"
    chunks[f"## {key}"] = "\nA source-backed implementation technique.\n\n"
    order = [when, negative, comparison] if v2 else [when]
    if qa:
        order.append(q)
    if flow:
        order.append(quick)
    order += [key] if v2 else [negative, comparison]
    if ptype != "skill-pack":
        order += ["技术栈", "依赖", "运维难度"] if zh else ["Tech stack", "Dependencies", "Ops difficulty"]
    order += ["健康度与可持续性", "存疑（未验证）"] if zh else ["Health & viability", "Caveats (unverified)"]
    return prefix + "".join(f"## {heading}\n" + chunks[f"## {heading}"] for heading in order)


class SectionsV2Test(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.page = LintContractTest()._write_pair(self.root, contract_page(), contract_page(True))
        from test_flow_card import SPEC
        self.spec = SPEC
        (self.root / "flows").mkdir()
        (self.root / "flows/demo.json").write_text(json.dumps(SPEC), encoding="utf-8")
        (self.root / "assets/flow").mkdir()
        for lang in ("en", "zh"):
            (self.root / f"assets/flow/demo{'.zh' if lang == 'zh' else ''}.svg").write_text(lint.flow_card.render(SPEC, lang), encoding="utf-8")
        # Explicit dates make the contract tests independent of the wall clock / runner env.
        for key, value in {"SECTIONS_V2_FROM": "2026-10-13", "FLOW_REQUIRED_FROM": "2026-09-20", "REQUIRE_FLOW": False}.items():
            patcher = mock.patch.object(lint, key, value, create=True)
            patcher.start()
            self.addCleanup(patcher.stop)

    def check(self, en: str, zh: str) -> tuple[lint.Report, lint.Report]:
        reports = []
        for is_zh, text in ((False, en), (True, zh)):
            path = self.page.with_name("demo.zh.md") if is_zh else self.page
            path.write_text(text, encoding="utf-8")
            lint.flow_card.sync_page(path, self.root, self.spec, "demo")
        for path in (self.page, self.page.with_name("demo.zh.md")):
            rep = lint.Report()
            lint.check_page(path, path.parent, self.root, set(), rep, lint.dt.date(2026, 10, 13))
            reports.append(rep)
        return tuple(reports)

    def assert_errors(self, texts: tuple[str, str], needle: str) -> None:
        for zh, rep in enumerate(self.check(*texts)):
            with self.subTest(zh=zh):
                self.assertTrue(any(needle in e for e in rep.errors), rep.errors)

    def assert_clean(self, **kwargs) -> None:
        for zh, rep in enumerate(self.check(contract_page(**kwargs), contract_page(True, **kwargs))):
            with self.subTest(zh=zh):
                self.assertEqual(rep.errors, [])

    def test_v2_acc2_01_missing_key_techniques(self) -> None:
        texts = []
        for zh in (False, True):
            prefix, chunks = section_chunks(contract_page(zh))
            del chunks["## 技术要点" if zh else "## Key techniques"]
            texts.append(prefix + "".join(k + "\n" + v for k, v in chunks.items()))
        self.assert_errors(tuple(texts), "missing required section: ##")
        for zh, rep in enumerate(self.check(*texts)):
            heading = "## 技术要点" if zh else "## Key techniques"
            self.assertTrue(any(f"missing required section: {heading}" in e for e in rep.errors), rep.errors)

    def test_v2_acc2_02_empty_key_techniques(self) -> None:
        self.assert_errors(tuple(contract_page(zh).replace("A source-backed implementation technique.", " \t ") for zh in (False, True)), "Key techniques / 技术要点 is empty")

    def test_v2_acc2_07_bilingual_key_presence_both_directions(self) -> None:
        for missing_zh in (False, True):
            texts = [contract_page(), contract_page(True)]
            key = "## 技术要点" if missing_zh else "## Key techniques"
            prefix, chunks = section_chunks(texts[int(missing_zh)])
            del chunks[key]
            texts[int(missing_zh)] = prefix + "".join(k + "\n" + v for k, v in chunks.items())
            en, zh = self.check(*texts)
            self.assertTrue(any("Key techniques / 技术要点 presence must match the bilingual sibling" in e for e in en.errors), en.errors)
            self.assertTrue(any(f"missing required section: {key}" in e for e in (zh if missing_zh else en).errors))

    def test_v2_acc2_03_comparison_after_quick_start_first_misplacement(self) -> None:
        for zh in (False, True):
            prefix, chunks = section_chunks(contract_page(zh))
            headings = list(chunks)
            comparison = "## 横向对比" if zh else "## Comparison"
            quick = "## 快速上手" if zh else "## Quick start"
            headings.remove(comparison)
            headings.insert(headings.index(quick) + 1, comparison)
            text = prefix + "".join(k + "\n" + chunks[k] for k in headings)
            texts = [contract_page(), contract_page(True)]
            texts[int(zh)] = text
            rep = self.check(*texts)[int(zh)]
            self.assertTrue(any(f"first misplaced heading: {comparison}" in e for e in rep.errors), rep.errors)

    def test_v2_acc2_04_legacy_title_needs_rename(self) -> None:
        self.assert_errors(tuple(contract_page(zh).replace("## 快速上手" if zh else "## Quick start", "## 怎么用起来" if zh else "## How it works") for zh in (False, True)), "rename")

    def test_v2_acc2_05_new_titles_on_v1_need_date_update(self) -> None:
        for key in (False, True):
            texts = []
            for zh in (False, True):
                text = contract_page(zh, v2=False)
                title = ("技术要点" if key else "快速上手") if zh else ("Key techniques" if key else "Quick start")
                texts.append(text + f"\n## {title}\n\nContent.\n")
            self.assert_errors(tuple(texts), "update last_verified")

    def test_v2_acc2_06_complete_v1_remains_clean(self) -> None:
        self.assert_clean(v2=False)

    def test_v2_acc2_08a_qa_after_when_is_wrong(self) -> None:
        texts = []
        for zh in (False, True):
            prefix, chunks = section_chunks(contract_page(zh))
            headings = list(chunks)
            q = "## 快问快答" if zh else "## Q&A"
            headings.remove(q)
            headings.insert(1, q)
            texts.append(prefix + "".join(k + "\n" + chunks[k] for k in headings))
        self.assert_errors(tuple(texts), "must sit between Comparison and Quick start")

    def test_v2_acc2_08b_qa_after_comparison_is_clean(self) -> None:
        self.assert_clean()

    def test_v2_acc2_09_skill_pack_without_extra_sections(self) -> None:
        self.assert_clean(ptype="skill-pack")

    def test_v2_h2_unknown_duplicate_caveats_last_and_h3(self) -> None:
        for zh in (False, True):
            text = contract_page(zh)
            extra = "## 安装" if zh else "## Install"
            first = "## 何时使用" if zh else "## When to use"
            for broken, needle in ((text + f"\n{extra}\n", "unknown v2 heading"),
                                   (text + f"\n{first}\n", "duplicate v2 heading")):
                texts = [contract_page(), contract_page(True)]
                texts[int(zh)] = broken
                self.assertTrue(any(needle in e for e in self.check(*texts)[int(zh)].errors))
            text = text.replace("## 存疑（未验证）" if zh else "## Caveats (unverified)", "## 存疑（待核）" if zh else "## Caveats (pending review)")
            texts = [contract_page(), contract_page(True)]
            texts[int(zh)] = text + "\n### Notes\n\nBody ## Install is not an H2.\n"
            self.assertEqual(self.check(*texts)[int(zh)].errors, [])
        self.assert_clean(qa=False)

    def test_v2_skill_pack_forbids_each_extra_section(self) -> None:
        for zh in (False, True):
            for heading in (["技术栈", "依赖", "运维难度"] if zh else ["Tech stack", "Dependencies", "Ops difficulty"]):
                texts = [contract_page(ptype="skill-pack"), contract_page(True, ptype="skill-pack")]
                texts[int(zh)] += f"\n## {heading}\n\nContent.\n"
                self.assertTrue(any("skill-pack must omit" in e for e in self.check(*texts)[int(zh)].errors))

    def test_v2_date_boundary_invalid_and_environment_override(self) -> None:
        self.assertEqual(lint.SECTIONS_V2_FROM, "2026-10-13")
        for value, expected in (("2026-10-12", False), ("2026-10-13", True), ("2026-10-14", True), ("bad", False), (None, False), ("", False)):
            self.assertEqual(lint.sections_v2(value), expected)
        import subprocess
        import os
        default_env = dict(os.environ)
        default_env.pop("OSS_ATLAS_SECTIONS_V2_FROM", None)
        default = subprocess.run([sys.executable, "-c", "import lint; print(lint.SECTIONS_V2_FROM)"], cwd=Path(lint.__file__).parent, env=default_env, capture_output=True, text=True, check=True)
        self.assertEqual(default.stdout.strip(), "2026-10-13")
        env = dict(os.environ, OSS_ATLAS_SECTIONS_V2_FROM="2026-10-14")
        result = subprocess.run([sys.executable, "-c", "import lint; print(lint.sections_v2('2026-10-13'), lint.sections_v2('2026-10-14'))"], cwd=Path(lint.__file__).parent, env=env, capture_output=True, text=True, check=True)
        self.assertEqual(result.stdout.strip(), "False True")
        self.assert_errors(tuple(contract_page(zh).replace("last_verified: 2026-10-13", "last_verified: bad") for zh in (False, True)), "not a valid YYYY-MM-DD")

    def test_v2_v1_unknown_h2_tolerance_and_v2_caveats_last(self) -> None:
        for zh in (False, True):
            texts = [contract_page(v2=False), contract_page(True, v2=False)]
            texts[int(zh)] += "\n## Notes\n\nLegacy notes.\n"
            self.assertEqual(self.check(*texts)[int(zh)].errors, [])
            prefix, chunks = section_chunks(contract_page(zh))
            heading = "## 运维难度" if zh else "## Ops difficulty"
            body = chunks.pop(heading)
            text = prefix + "".join(k + "\n" + v for k, v in chunks.items()) + heading + "\n" + body
            texts = [contract_page(), contract_page(True)]
            texts[int(zh)] = text
            self.assertTrue(any(f"first misplaced heading: {heading}" in e for e in self.check(*texts)[int(zh)].errors))

    def test_v2_flow_required_and_optional_quick_start(self) -> None:
        texts = tuple(contract_page(zh, flow=False) for zh in (False, True))
        self.assert_errors(texts, "has no '##")
        (self.root / "flows/demo.json").unlink()
        self.assert_errors(texts, "missing required section: ##")
        with mock.patch.object(lint, "FLOW_REQUIRED_FROM", "2099-01-01"):
            self.assert_clean(flow=False)
            with mock.patch.object(lint, "REQUIRE_FLOW", True):
                self.assert_errors(texts, "missing required section: ##")

    def test_v2_new_and_old_flow_titles_cannot_coexist(self) -> None:
        self.assert_errors(tuple(contract_page(zh) + ("\n## 怎么用起来\n" if zh else "\n## How it works\n") for zh in (False, True)), "rename")

    def test_v2_regression_future_utc(self) -> None:
        self.assert_errors(tuple(contract_page(zh).replace("last_verified: 2026-10-13", "last_verified: 2026-10-14") for zh in (False, True)), "in the future (UTC today is 2026-10-13)")

    def test_v2_regression_empty_qa(self) -> None:
        self.assert_errors(tuple(contract_page(zh).replace("A leftover judgment.", "") for zh in (False, True)), "Q&A / 快问快答 is empty")

    def test_v2_regression_one_sided_qa(self) -> None:
        for missing_zh in (False, True):
            texts = [contract_page(qa=missing_zh), contract_page(True, qa=not missing_zh)]
            self.assertTrue(any("Q&A / 快问快答 presence must match" in e for e in self.check(*texts)[0].errors))

    def test_v2_regression_nested_frontmatter_parity(self) -> None:
        en, _ = self.check(contract_page(), contract_page(True).replace("maintenance:\n      grade: A", "maintenance:\n      grade: E"))
        self.assertTrue(any("frontmatter drift" in e for e in en.errors))

    def run_main(self) -> tuple[int, str]:
        # Real main path, including routing and punctuation (not just the punctuation helper).
        for zh in (False, True):
            suffix = ".zh.md" if zh else ".md"
            (self.page.parent / f"INDEX{suffix}").write_text(f"[Demo](demo{suffix})\n", encoding="utf-8")
            (self.root / f"INDEX{suffix}").write_text(f"[Demo](categories/demo/INDEX{suffix})\n", encoding="utf-8")
            (self.root / f"README{suffix}").write_text(f"[Demo](categories/demo/demo{suffix})\n", encoding="utf-8")
        out = io.StringIO()
        with mock.patch.object(lint, "today_utc", return_value=lint.dt.date(2026, 10, 13)), mock.patch.object(sys, "argv", ["lint.py", "--root", str(self.root)]), contextlib.redirect_stdout(out):
            code = lint.main()
        return code, out.getvalue()

    def test_v2_regression_chinese_new_section_punctuation_via_main(self) -> None:
        for heading in ("快速上手", "技术要点"):
            with self.subTest(heading=heading):
                self.check(contract_page(), contract_page(True))
                path = self.page.with_name("demo.zh.md")
                text = path.read_text(encoding="utf-8")
                path.write_text(text.replace(f"## {heading}\n", f"## {heading}\n\n汉字,错误。\n"), encoding="utf-8")
                code, output = self.run_main()
                self.assertEqual(code, 1)
                self.assertIn("ASCII , ; ! ?", output)
        self.check(contract_page(), contract_page(True))
        path.write_text(path.read_text(encoding="utf-8").replace("## 技术要点\n", "## 技术要点\n\n`汉字,` https://example.com/汉字,\n\n```text\n汉字,\n```\n"), encoding="utf-8")
        code, output = self.run_main()
        self.assertEqual(code, 0, output)

    def test_v2_malformed_heading_inputs_are_bounded(self) -> None:
        # No property/fuzz dependency: truncated, malformed quotes, repetition and NUL table.
        for fragment in ("##", '## "Install', "## Q&A\n" * 50, "## \x00"):
            texts = [contract_page() + "\n" + fragment, contract_page(True)]
            rep = self.check(*texts)[0]
            self.assertLess(len(rep.errors), 110)

    def test_v2_real_indented_unknown_and_duplicate_headings_are_rejected(self) -> None:
        for zh in (False, True):
            for indent in (" ", "  ", "   "):
                for heading, needle in (("## 安装" if zh else "## Install", "unknown v2 heading"),
                                        ("## 何时使用" if zh else "## When to use", "duplicate v2 heading")):
                    with self.subTest(zh=zh, indent=len(indent), heading=heading):
                        texts = [contract_page(), contract_page(True)]
                        texts[int(zh)] += f"\n{indent}{heading}\n\nContent.\n"
                        rep = self.check(*texts)[int(zh)]
                        self.assertTrue(any(needle in e for e in rep.errors), rep.errors)

    def test_v2_key_only_inside_fence_is_missing_and_presence_mismatches(self) -> None:
        for missing_zh in (False, True):
            for fence in ("```", "~~~~"):
                with self.subTest(missing_zh=missing_zh, fence=fence):
                    texts = [contract_page(), contract_page(True)]
                    heading = "## 技术要点" if missing_zh else "## Key techniques"
                    text = texts[int(missing_zh)]
                    text = text.replace(heading + "\n\nA source-backed implementation technique.\n",
                                        f"{fence}markdown\n{heading}\n\nA source-backed implementation technique.\n{fence}\n")
                    texts[int(missing_zh)] = text
                    en, zh = self.check(*texts)
                    self.assertTrue(any(f"missing required section: {heading}" in e for e in (zh if missing_zh else en).errors), (en.errors, zh.errors))
                    self.assertTrue(any("Key techniques / 技术要点 presence must match" in e for e in en.errors), en.errors)

    def test_v2_fenced_h2_examples_do_not_change_sections_or_flow(self) -> None:
        for fence in ("```", "~~~~", "````"):
            texts = []
            for zh in (False, True):
                quick = "## 快速上手" if zh else "## Quick start"
                example = "## 安装\n## 怎么用起来\n## 技术要点" if zh else "## Install\n## How it works\n## Key techniques"
                close = fence.strip()
                texts.append(contract_page(zh).replace(quick + "\n", f"{quick}\n\n{fence}markdown\n{example}\n{close}\n"))
            with self.subTest(fence=fence):
                for rep in self.check(*texts):
                    self.assertEqual(rep.errors, [])

    def test_v2_setext_unknown_h2_is_rejected(self) -> None:
        texts = tuple(contract_page(zh) + ("\n安装\n---\n" if zh else "\nInstall\n---\n") for zh in (False, True))
        self.assert_errors(texts, "unknown v2 heading")

    def test_v2_indented_code_and_fence_delimiters_are_literal(self) -> None:
        for zh in (False, True):
            texts = [contract_page(), contract_page(True)]
            key = "## 技术要点" if zh else "## Key techniques"
            example = ("\n````markdown\n## Install\n```\n## Install\n````\n"
                       "\n~~~text\n## Install\n~~~\n")
            texts[int(zh)] = texts[int(zh)].replace(key + "\n", key + "\n" + example)
            self.assertEqual(self.check(*texts)[int(zh)].errors, [])

    def test_v2_every_required_heading_must_be_outside_fences(self) -> None:
        for zh in (False, True):
            required = ["何时使用", "何时不用", "横向对比", "健康度与可持续性", "存疑（未验证）"] if zh else ["When to use", "When NOT to use", "Comparison", "Health & viability", "Caveats (unverified)"]
            for title in required:
                with self.subTest(zh=zh, title=title):
                    prefix, chunks = section_chunks(contract_page(zh))
                    heading = "## " + title
                    text = prefix + "".join(("```markdown\n" + k + "\n" + v + "```\n\n") if k == heading else k + "\n" + v for k, v in chunks.items())
                    texts = [contract_page(), contract_page(True)]
                    texts[int(zh)] = text
                    rep = self.check(*texts)[int(zh)]
                    self.assertTrue(any(f"missing required section: {heading}" in e or (title.startswith(("Caveats", "存疑")) and "missing required section: ## 存疑" in e) for e in rep.errors), rep.errors)

    def test_v2_qa_and_comparison_use_real_section_boundaries(self) -> None:
        texts = []
        for zh in (False, True):
            prefix, chunks = section_chunks(contract_page(zh))
            q = "## 快问快答" if zh else "## Q&A"
            comparison = "## 横向对比" if zh else "## Comparison"
            chunks[comparison] = "\n```markdown\n## Install\n```\n" + chunks[comparison]
            texts.append(prefix + "".join(("```markdown\n" + k + "\n" + v + "```\n\n") if k == q else k + "\n" + v for k, v in chunks.items()))
        for rep in self.check(*texts):
            self.assertEqual(rep.errors, [])
        en, _ = self.check(texts[0], contract_page(True))
        self.assertTrue(any("Q&A / 快问快答 presence must match" in e for e in en.errors), en.errors)

    def test_v2_scan_offsets_are_bounded_on_malformed_blocks(self) -> None:
        import random
        rng = random.Random(7)
        tokens = ["## Install", "   ## Key techniques", "    ## Code", "```", "````", "~~~", "~~~~",
                  "<!--", "-->", "Install", "---", "### Subheading", "", "\x00"]
        for _ in range(60):
            text = "\n".join(rng.choice(tokens) for _ in range(80))
            chapters = lint.flow_card.scan_h2_sections(text)
            self.assertLessEqual(len(chapters), 80)
            self.assertEqual([h.start for h in chapters], sorted(h.start for h in chapters))
            for h in chapters:
                self.assertTrue(0 <= h.start < h.body_start <= h.end <= len(text), h)

    def test_v2_optional_missing_flow_warning_names_quick_start(self) -> None:
        (self.root / "flows/demo.json").unlink()
        with mock.patch.object(lint, "FLOW_REQUIRED_FROM", "2099-01-01"):
            self.check(contract_page(flow=False), contract_page(True, flow=False))
            code, output = self.run_main()
        self.assertEqual(code, 0, output)
        warning = next(line for line in output.splitlines() if "backfill backlog" in line)
        self.assertIn("## Quick start", warning)
        self.assertIn("## 快速上手", warning)

    def test_v2_nested_h2_is_not_a_way_to_hide_unknown_sections(self) -> None:
        for prefix in ("> ", "- ", "1. ", "> - "):
            self.assert_errors(tuple(contract_page(zh) + "\n" + prefix + ("## 安装\n" if zh else "## Install\n") for zh in (False, True)), "unknown v2 heading")

    def round2_container_case(self, suffix: str) -> None:
        # Round-3 ruling supersedes lexical-container closing: all such delimiters are forbidden.
        needle = "comments must open/close at column zero" if "<!--" in suffix else "fences must open/close at column zero"
        self.assert_errors(tuple(contract_page(zh) + suffix.replace("## Install", "## 安装" if zh else "## Install").replace("## When to use", "## 何时使用" if zh else "## When to use") for zh in (False, True)), needle)

    def test_v2_round2_a_quote_eof(self) -> None:
        self.round2_container_case("\n> ```markdown\n> literal\n\n## Install\n")

    def test_v2_round2_a_list_eof(self) -> None:
        self.round2_container_case("\n- ```markdown\n  literal\n\n## Install\n")

    def test_v2_round2_a_root_false_close(self) -> None:
        for rep in self.check(*(contract_page(zh) + "\n```markdown\n> ```\n## Install\n```\n" for zh in (False, True))):
            self.assertTrue(any("fences must open/close at column zero" in e for e in rep.errors), rep.errors)
            self.assertFalse(any("unknown v2 heading: ## Install" in e for e in rep.errors))

    def round2_key_in_literal(self, hidden_zh: bool, opener: str, closer: str, first_line: str = "") -> None:
        texts = [contract_page(), contract_page(True)]
        heading = "## 技术要点" if hidden_zh else "## Key techniques"
        old = heading + "\n\nA source-backed implementation technique.\n"
        new = opener + "\n" + first_line + old + closer + "\n"
        texts[int(hidden_zh)] = texts[int(hidden_zh)].replace(old, new)
        en, zh = self.check(*texts)
        self.assertTrue(any(f"missing required section: {heading}" in e for e in (zh if hidden_zh else en).errors), (en.errors, zh.errors))
        self.assertTrue(any("Key techniques / 技术要点 presence must match" in e for e in en.errors), en.errors)

    def test_v2_round2_a_pre_only_key_en(self) -> None:
        self.round2_key_in_literal(False, "<pre>", "</pre>")

    def test_v2_round2_a_pre_only_key_zh(self) -> None:
        self.round2_key_in_literal(True, "<pre>", "</pre>")

    def test_v2_round2_b_quote_fence_unknown_h2(self) -> None:
        self.round2_container_case("\n> ```\n## Install\nText.\n\n> ```\n")

    def test_v2_round2_b_list_fence_duplicate_h2(self) -> None:
        self.round2_container_case("\n- ```\n## When to use\nText.\n- ```\n")

    def test_v2_round2_b_quote_comment_unknown_h2(self) -> None:
        self.round2_container_case("\n> <!--\n## Install\n-->\n")

    def test_v2_round2_list_comment_leak(self) -> None:
        self.round2_container_case("\n- <!--\n  literal\n\n## Install\n-->\n")

    def test_v2_round2_b_key_only_in_code(self) -> None:
        for zh in (False, True):
            with self.subTest(zh=zh):
                self.round2_key_in_literal(zh, "```text", "```", "> ```\n")

    def test_v2_round2_b_quote_fence_closed_at_root(self) -> None:
        self.round2_container_case("\n> ```bash\n> npm i\n```\n## Install\n")

    def test_v2_round2_container_literal_must_close_even_at_eof(self) -> None:
        for suffix in ("\n> ```\n> literal\n", "\n- <!--\n  literal\n"):
            self.round2_container_case(suffix)

    def test_v2_round2_closed_container_literals_now_require_root_syntax(self) -> None:
        for block in ("> ```markdown\n> ## Install\n> ```", "- ```markdown\n  ## Install\n  ```",
                      "> <!--\n> ## Install\n> -->", "- <!--\n  ## Install\n  -->"):
            with self.subTest(block=block):
                for rep in self.check(*(contract_page(zh) + "\n" + block + "\n" for zh in (False, True))):
                    self.assertTrue(any("must open/close at column zero" in e for e in rep.errors), rep.errors)

    def test_v2_round2_list_item_then_thematic_break(self) -> None:
        for rep in self.check(*(contract_page(zh) + "\n- item\n---\n" for zh in (False, True))):
            self.assertEqual(rep.errors, [])

    def test_v2_round2_ordered_item_then_thematic_break(self) -> None:
        for rep in self.check(*(contract_page(zh) + "\n1. item\n---\n" for zh in (False, True))):
            self.assertEqual(rep.errors, [])

    def test_v2_round2_quote_then_thematic_break(self) -> None:
        for rep in self.check(*(contract_page(zh) + "\n> quote\n---\n" for zh in (False, True))):
            self.assertEqual(rep.errors, [])

    def test_v2_round2_table_row_then_thematic_break(self) -> None:
        for rep in self.check(*(contract_page(zh) + "\n| a | b |\n|---|---|\n| 1 | 2 |\n---\n" for zh in (False, True))):
            self.assertEqual(rep.errors, [])

    def test_v2_round2_noncanonical_key_cannot_satisfy_presence(self) -> None:
        for zh in (False, True):
            heading = "## 技术要点" if zh else "## Key techniques"
            for replacement in (" " + heading, "> " + heading, heading[3:] + "\n---"):
                with self.subTest(zh=zh, replacement=replacement):
                    texts = [contract_page(), contract_page(True)]
                    texts[int(zh)] = texts[int(zh)].replace(heading, replacement)
                    en, other = self.check(*texts)
                    self.assertTrue(any(f"missing required section: {heading}" in e for e in (other if zh else en).errors))
                    self.assertTrue(any("presence must match the bilingual sibling" in e for e in en.errors))

    def round3_rejected_fragment(self, fragment: str, needle: str) -> None:
        self.assert_errors(tuple(contract_page(zh) + "\n" + fragment.replace("## Install", "## 安装" if zh else "## Install") for zh in (False, True)), needle)

    def test_v2_round3_a_list_cont_fence(self) -> None:
        self.round3_rejected_fragment("- example\n\n  ```markdown\n  literal\n\n## Install\n", "fences must open/close at column zero")

    def test_v2_round3_a_list_cont_comment(self) -> None:
        self.round3_rejected_fragment("- example\n\n  <!--\n  literal\n\n## Install\n", "comments must open/close at column zero")

    def test_v2_round3_a_list_cont_fence_closed(self) -> None:
        self.round3_rejected_fragment("- example\n\n  ```markdown\n  literal\n\n## Install\n  ```\n", "fences must open/close at column zero")

    def round3_non_lf_key(self, char: str) -> None:
        for zh in (False, True):
            with self.subTest(zh=zh, char=repr(char)):
                texts = [contract_page(), contract_page(True)]
                heading = "## 技术要点" if zh else "## Key techniques"
                original = heading + "\n\nA source-backed implementation technique.\n"
                replacement = "```text\nliteral" + char + "```\n" + original + "<!--\n```\n-->\n\n"
                texts[int(zh)] = texts[int(zh)].replace(original, replacement)
                en, other = self.check(*texts)
                self.assertTrue(any(f"missing required section: {heading}" in e for e in (other if zh else en).errors), (en.errors, other.errors))
                self.assertTrue(any("Key techniques / 技术要点 presence must match" in e for e in en.errors), en.errors)

    def test_v2_round3_a_non_lf_vt_false_close(self) -> None:
        self.round3_non_lf_key("\x0b")

    def test_v2_round3_a_non_lf_u2028_false_close(self) -> None:
        self.round3_non_lf_key("\u2028")

    def test_v2_round3_a_non_lf_nel_false_close(self) -> None:
        self.round3_non_lf_key("\x85")

    def test_v2_round3_b_list_indent4_h2(self) -> None:
        self.round3_rejected_fragment("- foo\n\n    ## Install\n", "rewrite as column-zero ATX")

    def test_v2_round3_b_ordered_indent4_h2(self) -> None:
        self.round3_rejected_fragment("1. foo\n\n    ## Install\n", "rewrite as column-zero ATX")

    def test_v2_round3_b_setext_inline_html(self) -> None:
        self.round3_rejected_fragment("<b>Install</b>\n---\n", "setext underline")

    def test_v2_round3_b_setext_autolink(self) -> None:
        self.round3_rejected_fragment("<https://example.com>\n---\n", "setext underline")

    def test_v2_round3_b_pre_mismatched_end(self) -> None:
        self.round3_rejected_fragment("<pre>\n</script>\n\n## Install\n", "unknown v2 heading")

    def test_v2_round3_conform_list_no_blank_indent4(self) -> None:
        self.round3_rejected_fragment("- item\n    ## Install\n", "rewrite as column-zero ATX")

    def test_v2_round3_conform_tab_heading(self) -> None:
        self.round3_rejected_fragment("- item\n\n\t## Install\n", "rewrite as column-zero ATX")

    def test_v2_round3_conform_quote_list_indent4(self) -> None:
        self.round3_rejected_fragment("> - item\n>\n>     ## Install\n", "rewrite as column-zero ATX")

    def test_v2_round3_raw_html_key_requires_blank_boundary(self) -> None:
        for tag in ("div", "span", "details"):
            for zh in (False, True):
                with self.subTest(tag=tag, zh=zh):
                    texts = [contract_page(), contract_page(True)]
                    heading = "## 技术要点" if zh else "## Key techniques"
                    body = heading + "\n\nA source-backed implementation technique.\n"
                    texts[int(zh)] = texts[int(zh)].replace(body, f"<{tag}>\n{body}</{tag}>\n")
                    en, other = self.check(*texts)
                    self.assertTrue(any(f"missing required section: {heading}" in e for e in (other if zh else en).errors))
                    self.assertTrue(any("presence must match" in e for e in en.errors))

    def test_v2_round3_php_only_key(self) -> None:
        for zh in (False, True):
            self.round2_key_in_literal(zh, "<?php", "?>")

    def test_v2_round3_cdata_only_key(self) -> None:
        for zh in (False, True):
            self.round2_key_in_literal(zh, "<![CDATA[", "]]>")

    def test_v2_round3_doctype_only_key(self) -> None:
        for zh in (False, True):
            self.round2_key_in_literal(zh, "<!DOCTYPE", ">")

    def test_v2_round3_no_secondary_missing_quick_start_error(self) -> None:
        en, zh = self.check(*(contract_page(is_zh) + "\n> ```\n> text\n" for is_zh in (False, True)))
        for rep in (en, zh):
            self.assertTrue(rep.errors)
            self.assertFalse(any("page has no '## Quick start'" in e or "page has no '## 快速上手'" in e for e in rep.errors), rep.errors)

    def test_v2_round3_root_fence_content_stays_literal(self) -> None:
        for newline in ("\n", "\r\n"):
            texts = tuple((contract_page(zh) + "\n```markdown\n## Install\n```\n").replace("\n", newline) for zh in (False, True))
            for rep in self.check(*texts):
                self.assertEqual(rep.errors, [])

    def test_v2_round3_c0_controls_rejected(self) -> None:
        for value in [*range(9), 11, 12, *range(14, 32)]:
            with self.subTest(value=value):
                self.round3_rejected_fragment("text" + chr(value) + "text\n", "C0 control character")
        for rep in self.check(*(contract_page(zh) + "\ntext\ttext\n" for zh in (False, True))):
            self.assertEqual(rep.errors, [])

    def test_v2_round3_deep_quote_does_not_compile_dynamic_regex(self) -> None:
        # Bound hostile-input testing itself; a timeout is a failure, not a skipped case.
        import subprocess
        script = "import flow_card; text=('> '*1000)+'```\\n'+('> '*999)+'```\\n'; result=flow_card.scan_h2_sections(text); print('rejected' if any('fences must open/close at column zero' in e for e in result.errors) else 'accepted')"
        try:
            result = subprocess.run([sys.executable, "-B", "-c", script], cwd=Path(lint.__file__).parent,
                                    capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=2)
        except subprocess.TimeoutExpired:
            self.fail("scanner exceeded the 2-second hostile-input deadline")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "rejected")

    def test_v2_round3_all_nonroot_hash_levels_rejected(self) -> None:
        for level in range(1, 7):
            for prefix in (" ", "    ", "\t", "> ", "- ", "* ", "+ ", "1. ", "> - "):
                with self.subTest(level=level, prefix=prefix):
                    self.round3_rejected_fragment(prefix + "#" * level + " Heading\n", "rewrite as column-zero ATX")

    def test_v2_round3_setext_equal_rejected(self) -> None:
        self.round3_rejected_fragment("Heading\n===\n", "setext underline")


class V2GeneratorTest(unittest.TestCase):
    def test_v2_generators_offline_return_type_adaptive_marked_skeletons(self) -> None:
        import intake_queue_apply
        import agent_skills_intake
        item = {"name": "Demo", "slug": "demo", "repo": "example/Demo",
                "category_path": "categories/demo", "suggested_category": "demo", "reasons": [],
                "github": {"url": "https://github.com/example/Demo", "html_url": "https://github.com/example/Demo", "description": "Demo.", "language": "Python", "license": "MIT",
                           "full_name": "example/demo", "stars": 1, "default_branch": "main",
                           "pushed_at": "2026-10-13T00:00:00Z", "archived": False}}
        for module in (intake_queue_apply, agent_skills_intake):
            for ptype in ("tool", "library", "app", "framework", "service", "model", "skill-pack"):
                item["type"] = ptype
                for zh in (False, True):
                    with self.subTest(generator=module.__name__, ptype=ptype, zh=zh), tempfile.TemporaryDirectory() as td, mock.patch.object(module, "TODAY", "2026-10-13"):
                        args = (item, "0" * 40, Path(td)) if module is intake_queue_apply else (item, "0" * 40)
                        text = (module.page_zh if zh else module.page_en)(*args)
                        self.assertIsInstance(text, str)
                        self.assertIn("# Demo", text)
                        self.assertEqual(lint.parse_frontmatter(text)["last_verified"], "2026-10-13")
                        order = ["何时使用", "何时不用", "横向对比", "快速上手", "技术要点"] if zh else ["When to use", "When NOT to use", "Comparison", "Quick start", "Key techniques"]
                        if ptype != "skill-pack":
                            order += ["技术栈", "依赖", "运维难度"] if zh else ["Tech stack", "Dependencies", "Ops difficulty"]
                        order += ["健康度与可持续性", "存疑（未验证）"] if zh else ["Health & viability", "Caveats (unverified)"]
                        _, chunks = section_chunks(text)
                        self.assertEqual(list(chunks), [f"## {h}" for h in order])
                        for heading in order[3:5]:
                            self.assertIn(lint.UNRESEARCHED_MARKER, chunks[f"## {heading}"])
                        root = Path(td)
                        page = root / "categories/demo" / ("demo.zh.md" if zh else "demo.md")
                        page.parent.mkdir(parents=True)
                        page.write_text(text, encoding="utf-8")
                        rep = lint.Report()
                        lint.check_page(page, page.parent, root, set(), rep, lint.dt.date(2026, 10, 13))
                        self.assertTrue(any("still carry <!-- oss-atlas:unresearched -->" in e for e in rep.errors))


class StructuredTechniquesTest(unittest.TestCase):
    def setUp(self):
        import copy
        import mechanism_card as mc
        from test_mechanism_card import SPEC, technique_body, fake_d2
        from test_flow_card import SPEC as FLOW
        self.mc = mc
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        texts = [contract_page(zh).replace("last_verified: 2026-10-13", "last_verified: 2026-10-15").replace("A source-backed implementation technique.", technique_body(zh)) for zh in (False, True)]
        self.page = LintContractTest()._write_pair(self.root, *texts)
        (self.root / "flows").mkdir()
        (self.root / "flows/demo.json").write_text(json.dumps(FLOW))
        (self.root / "assets/flow").mkdir()
        for lang, path in (("en", self.page), ("zh", self.page.with_name("demo.zh.md"))):
            (self.root / f"assets/flow/demo{'.zh' if lang == 'zh' else ''}.svg").write_text(lint.flow_card.render(FLOW, lang))
            lint.flow_card.sync_page(path, self.root, FLOW, "demo")
        self.spec = copy.deepcopy(SPEC)
        (self.root / "mechanisms").mkdir()
        self.source = self.root / "mechanisms/demo.json"
        self.source.write_text(json.dumps(self.spec))
        self.d2 = fake_d2(self.root)
        for key, value in {"SECTIONS_V2_FROM": "2026-10-13", "TECHNIQUES_STRUCTURED_FROM": "2026-10-15", "FLOW_REQUIRED_FROM": "2026-09-20", "REQUIRE_FLOW": False}.items():
            patcher = mock.patch.object(lint, key, value, create=True)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.generate()
        self.originals = [self.page.read_text(), self.page.with_name("demo.zh.md").read_text()]

    def generate(self):
        with mock.patch.object(self.mc, "ROOT", self.root), mock.patch.object(self.mc.shutil, "which", return_value=self.d2), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(self.mc.main([str(self.page)]), 0)

    def check(self, texts=None):
        if texts is not None:
            for path, text in zip((self.page, self.page.with_name("demo.zh.md")), texts):
                path.write_text(text)
        reports = []
        for path in (self.page, self.page.with_name("demo.zh.md")):
            rep = lint.Report()
            lint.check_page(path, path.parent, self.root, set(), rep, lint.dt.date(2026, 10, 15))
            reports.append(rep)
        return reports

    def assert_bad(self, edit, needle):
        baseline = self.check(self.originals)
        self.assertEqual([e for r in baseline for e in r.errors], [])
        for i in (0, 1):
            texts = self.originals.copy()
            texts[i] = edit(texts[i], bool(i))
            rep = self.check(texts)[i]
            self.assertTrue(any(needle in e for e in rep.errors), rep.errors)

    def test_kts_acc2_01_missing_image(self):
        self.assert_bad(lambda text, zh: re.sub(r"(?m)^!\[Demo — (?:mechanism diagram|机制图)\].*\n", "", text), "mechanism image")

    def test_kts_acc2_02_missing_image_file(self):
        for suffix in ("", ".zh"):
            (self.root / f"assets/mechanism/demo{suffix}.svg").unlink()
        for report in self.check():
            self.assertTrue(any("mechanism SVG missing" in e for e in report.errors), report.errors)

    def test_kts_acc2_03_missing_generated_block(self):
        self.assert_bad(lambda text, zh: self.mc.BLOCK_RE.sub("", text), "mechanism text block missing")

    def test_kts_acc2_04_manual_text_edit(self):
        self.assert_bad(lambda text, zh: text.replace("- 输入", "- 手改") if zh else text.replace("- Input", "- Edited"), "mechanism text block drifted")

    def test_kts_acc2_05_stale_svg_hash(self):
        for suffix in ("", ".zh"):
            path = self.root / f"assets/mechanism/demo{suffix}.svg"
            path.write_text(path.read_text().replace(self.mc.spec_hash(self.spec), "0" * 64))
        for report in self.check():
            self.assertTrue(any("mechanism SVG stale" in e and "python3 tools/mechanism_card.py" in e for e in report.errors), report.errors)

    def test_kts_acc2_12_bilingual_technique_count(self):
        text = self.originals[1]
        self.page.with_name("demo.zh.md").write_text(re.sub(r"(?ms)^### 2\..*?(?=^## )", "", text))
        report = self.check()[0]
        self.assertTrue(any("technique counts must match" in e for e in report.errors), report.errors)

    def test_kts_acc2_15_yesterday_prose_v2_is_accepted(self):
        texts = [self.mc.BLOCK_RE.sub("", text).replace("last_verified: 2026-10-15", "last_verified: 2026-10-14") for text in self.originals]
        texts = [re.sub(r"(?ms)^### 1\..*?(?=^## )", "Old researched prose.\n\n", text) for text in texts]
        for report in self.check(texts):
            self.assertEqual(report.errors, [])

    def test_kts_acc2_16_v1_is_unaffected_even_with_earlier_threshold(self):
        from test_flow_card import SPEC as FLOW
        with mock.patch.object(lint, "TECHNIQUES_STRUCTURED_FROM", "2026-01-01"):
            texts = [contract_page(zh, v2=False) for zh in (False, True)]
            for path, text in zip((self.page, self.page.with_name("demo.zh.md")), texts):
                path.write_text(text)
                lint.flow_card.sync_page(path, self.root, FLOW, "demo")
            for report in self.check():
                self.assertEqual(report.errors, [])

    def test_kts_acc2_17_unresearched_only_keeps_marker_error(self):
        texts = []
        for zh, text in enumerate(self.originals):
            span = self.mc.section_bounds(text, "zh" if zh else "en")
            texts.append(text[:span[0]] + "\n" + lint.UNRESEARCHED_MARKER + "\n\n" + text[span[1]:])
        for report in self.check(texts):
            self.assertEqual(len(report.errors), 1, report.errors)
            self.assertIn("still carry", report.errors[0])

    def test_bad_or_absent_source_and_stamp_are_diagnostic(self):
        for invalid in (None, "{bad", "[]"):
            if invalid is None:
                self.source.unlink()
            else:
                self.source.write_text(invalid)
            for report in self.check():
                self.assertTrue(any("mechanism spec" in e for e in report.errors), report.errors)
        self.source.write_text(json.dumps(self.spec))
        for stamp in ("", "<!-- mechanism-src sha256=bad -->"):
            for suffix in ("", ".zh"):
                (self.root / f"assets/mechanism/demo{suffix}.svg").write_text(stamp + "<svg />")
            for report in self.check():
                self.assertTrue(any("mechanism SVG stale" in e for e in report.errors), report.errors)
        (self.root / "assets/mechanism/demo.svg").write_bytes(b"\xff\xfe")
        self.assertTrue(any("unreadable" in e for e in self.check()[0].errors))

    def test_threshold_environment_invalid_date_and_unrelated_marker(self):
        import os
        import subprocess
        default_env = dict(os.environ)
        default_env.pop("OSS_ATLAS_TECHNIQUES_STRUCTURED_FROM", None)
        default = subprocess.run([sys.executable, "-B", "-c", "import lint; print(lint.TECHNIQUES_STRUCTURED_FROM)"], cwd=Path(lint.__file__).parent, env=default_env, capture_output=True, text=True, check=True)
        self.assertEqual(default.stdout.strip(), "2026-10-15")
        for date, expected in (("2026-10-14", False), ("2026-10-15", True), ("bad", False), (None, False)):
            self.assertEqual(lint.techniques_structured(date), expected)
        with mock.patch.object(lint, "TECHNIQUES_STRUCTURED_FROM", "invalid"):
            self.assertFalse(lint.techniques_structured("2026-10-15"))
        env = dict(os.environ, OSS_ATLAS_TECHNIQUES_STRUCTURED_FROM="2026-10-16")
        result = subprocess.run([sys.executable, "-B", "-c", "import lint; print(lint.techniques_structured('2026-10-15'), lint.techniques_structured('2026-10-16'))"], cwd=Path(lint.__file__).parent, env=env, capture_output=True, text=True, check=True)
        self.assertEqual(result.stdout.strip(), "False True")
        texts = [text.replace("You use it.", lint.UNRESEARCHED_MARKER) for text in self.originals]
        texts[0] = self.mc.BLOCK_RE.sub("", texts[0])
        report = self.check(texts)[0]
        self.assertTrue(any("mechanism text block missing" in e for e in report.errors), report.errors)

    def run_main(self):
        for zh in (False, True):
            suffix = ".zh.md" if zh else ".md"
            (self.page.parent / f"INDEX{suffix}").write_text(f"[Demo](demo{suffix})\n")
            (self.root / f"INDEX{suffix}").write_text(f"[Demo](categories/demo/INDEX{suffix})\n")
            (self.root / f"README{suffix}").write_text(f"[Demo](categories/demo/demo{suffix})\n")
        out = io.StringIO()
        with mock.patch.object(lint, "today_utc", return_value=lint.dt.date(2026, 10, 15)), mock.patch.object(sys, "argv", ["lint.py", "--root", str(self.root)]), contextlib.redirect_stdout(out):
            code = lint.main()
        return code, out.getvalue()

    def test_e2e_cli_lint_source_drift_and_recovery_without_d2(self):
        with mock.patch.object(self.mc.shutil, "which", return_value=None), mock.patch.object(self.mc.subprocess, "run", side_effect=AssertionError("lint must not render")):
            code, output = self.run_main()
            self.assertEqual(code, 0, output)
            self.spec["nodes"][1]["en"] = "Parse differently"
            self.source.write_text(json.dumps(self.spec))
            code, output = self.run_main()
            self.assertEqual(code, 1)
            self.assertIn("mechanism SVG stale", output)
            self.assertIn("mechanism text block drifted", output)
        self.generate()
        self.assertEqual(self.run_main()[0], 0)
        before = {p: p.read_bytes() for p in (self.page, self.page.with_name("demo.zh.md"), *sorted((self.root / "assets/mechanism").glob("*.svg")))}
        with mock.patch.object(self.mc, "ROOT", self.root), mock.patch.object(self.mc.shutil, "which", return_value=None), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(self.mc.main([str(self.page)]), 2)
        self.assertEqual({p: p.read_bytes() for p in before}, before)

    def test_chinese_punctuation_main_and_generated_block_boundaries(self):
        # Chinese label values may contain ASCII punctuation in JSON; only the generated block is exempt.
        self.spec["nodes"][0]["zh"] = "输入,可见"
        self.source.write_text(json.dumps(self.spec))
        self.generate()
        code, output = self.run_main()
        self.assertEqual(code, 0, output)
        path = self.page.with_name("demo.zh.md")
        good = path.read_text()
        for bad in (good.replace("**解决：**", "**解决:**", 1),
                    good.replace("Value 1-0.", "汉字,", 1),
                    good.replace(self.mc.END, "<!-- mechanism:broken -->", 1)):
            path.write_text(bad)
            code, output = self.run_main()
            self.assertEqual(code, 1, output)
            self.assertIn("ASCII , ; ! ?", output)
        path.write_text(good + "\n```text\n汉字,\n```\n")
        self.assertEqual(self.run_main()[0], 0)

    def test_punctuation_fake_blocks_in_other_sections_still_fail_main(self):
        fake = "<!-- mechanism:begin (not generated) -->\n汉字,汉字;\n<!-- mechanism:end -->\n"
        self.assertEqual(self.run_main()[0], 0)
        path = self.page.with_name("demo.zh.md")
        good = path.read_text()
        for heading in ("## 何时使用", "## 技术栈", "## 存疑（未验证）"):
            with self.subTest(heading=heading):
                path.write_text(good.replace(heading + "\n", heading + "\n\n" + fake, 1))
                code, output = self.run_main()
                self.assertEqual(code, 1, output)
                self.assertIn("ASCII , ; ! ?", output)
        path.write_text(good)

    def test_punctuation_fake_blocks_in_summary_files_and_old_pages_not_exempt(self):
        fake = "<!-- mechanism:begin (not generated) -->\n汉字,汉字;\n<!-- mechanism:end -->\n"
        self.assertEqual(self.run_main()[0], 0)
        # run_main refreshes fixture routing files, so capture its own main() invocation here.
        for path in (self.root / "README.zh.md", self.page.parent / "INDEX.zh.md"):
            original = path.read_text()
            path.write_text(original + "\n" + fake)
            out = io.StringIO()
            with mock.patch.object(lint, "today_utc", return_value=lint.dt.date(2026, 10, 15)), mock.patch.object(sys, "argv", ["lint.py", "--root", str(self.root)]), contextlib.redirect_stdout(out):
                code = lint.main()
            self.assertEqual(code, 1, out.getvalue())
            self.assertIn("ASCII , ; ! ?", out.getvalue())
            path.write_text(original)
        for date in ("2026-06-29", "2026-10-14"):
            text = f"---\nlast_verified: {date}\n---\n\n## 技术要点\n\n{fake}"
            self.assertEqual(lint.zh_punct_violations(text), 2)

    def test_kts_acc2_06_too_few_techniques(self):
        self.assert_bad(lambda text, zh: re.sub(r"(?ms)^### 2\..*?(?=^## )", "", text), "at least 2")

    def test_kts_acc2_07_non_contiguous_numbering(self):
        self.assert_bad(lambda text, zh: text.replace("### 2.", "### 3."), "continuous")

    def test_kts_acc2_08_missing_label(self):
        self.assert_bad(lambda text, zh: re.sub(r"(?m)^- \*\*(?:How:|做法：)\*\*.*\n", "", text, count=1), "four labels")

    def test_kts_acc2_09_label_order(self):
        self.assert_bad(lambda text, zh: text.replace("**解决：**", "**边界：**", 1) if zh else text.replace("**Problem:**", "**Limits:**", 1), "four labels")

    def test_kts_acc2_10_empty_label_value(self):
        self.assert_bad(lambda text, zh: text.replace("Value 1-0.", " \t ", 1), "empty label")

    def test_kts_acc2_11_source_needs_link(self):
        self.assert_bad(lambda text, zh: text.replace("[design](https://example.org/design)", "design", 1), "Source / 源码")

    def test_source_links_inside_code_or_escaped_are_rejected_en_zh_via_main(self):
        link = "[design](https://example.org/design)"
        for fake in (f"`{link}`", f"``{link}``", "\\" + link, "!" + link):
            for zh in (False, True):
                with self.subTest(fake=fake, zh=zh):
                    texts = self.originals.copy()
                    texts[int(zh)] = texts[int(zh)].replace(link, fake)
                    report = self.check(texts)[int(zh)]
                    errors = [e for e in report.errors if "Source / 源码 must contain" in e]
                    self.assertEqual(len(errors), 2, report.errors)
                    code, output = self.run_main()
                    self.assertEqual(code, 1, output)
                    self.assertIn("Source / 源码 must contain", output)

    def test_source_real_links_with_code_labels_and_continuations_remain_valid(self):
        link = "[design](https://example.org/design)"
        for actual in ("[`src.py:1–4`](https://example.org/src.py#L1-L4)",
                       "`not a link` then " + link,
                       "See the source below.\n  " + link,
                       "\\\\" + link,
                       "\\!" + link):
            with self.subTest(actual=actual):
                texts = [text.replace(link, actual) for text in self.originals]
                self.assertEqual([e for r in self.check(texts) for e in r.errors], [])
                code, output = self.run_main()
                self.assertEqual(code, 0, output)

    def test_source_indented_code_blocks_do_not_count_as_links_en_zh_via_main(self):
        link = "[design](https://example.org/design)"
        for indent in (" " * 6, " " * 8, "\t\t"):
            for zh in (False, True):
                with self.subTest(indent=repr(indent), zh=zh):
                    texts = self.originals.copy()
                    texts[int(zh)] = texts[int(zh)].replace(link, "Example only.\n\n" + indent + link)
                    report = self.check(texts)[int(zh)]
                    self.assertEqual(len([e for e in report.errors if "Source / 源码 must contain" in e]), 2, report.errors)
                    code, output = self.run_main()
                    self.assertEqual(code, 1, output)
                    self.assertIn("Source / 源码 must contain", output)

    def test_source_ordinary_continuations_and_links_after_code_stay_valid(self):
        link = "[design](https://example.org/design)"
        values = (
            "See below.\n  " + link,
            "See below.\n\n  " + link,
            "See below.\n\n    " + link,  # four source spaces = two in the list item
            "See below.\n      " + link,  # no blank: indented line continues the paragraph
            "Example only.\n\n      `[fake](https://example.org/fake)`\n\n  " + link,
            "[`src.py`](https://example.org/src.py)",
        )
        for value in values:
            with self.subTest(value=value):
                texts = [text.replace(link, value) for text in self.originals]
                self.assertEqual([e for r in self.check(texts) for e in r.errors], [])
                code, output = self.run_main()
                self.assertEqual(code, 0, output)

    def test_source_comments_html_and_quotes_do_not_count_en_zh_via_main(self):
        link = "[design](https://example.org/design)"
        probes = (
            ("Example only. <!-- " + link + " -->", "Source / 源码 must contain"),
            ("Example only. <!-- hidden\n  " + link + " -->", "Source / 源码 must contain"),
            ("Example only.\n\n  <div>" + link + "</div>", "Source must be plain prose with inline links"),
            ("Example only.\n\n  >     " + link, "Source must be plain prose with inline links"),
        )
        for value, message in probes:
            for zh in (False, True):
                with self.subTest(value=value, zh=zh):
                    texts = self.originals.copy()
                    texts[int(zh)] = texts[int(zh)].replace(link, value)
                    report = self.check(texts)[int(zh)]
                    self.assertEqual(len(report.errors), 2, report.errors)
                    self.assertTrue(all(message in error for error in report.errors), report.errors)
                    code, output = self.run_main()
                    self.assertEqual(code, 1, output)
                    self.assertIn(message, output)

    def test_source_container_continuations_rejected_even_with_a_real_link(self):
        link = "[design](https://example.org/design)"
        for continuation in ("  <span>extra</span>", "  > quoted prose", "    <div>extra</div>"):
            for zh in (False, True):
                texts = self.originals.copy()
                texts[int(zh)] = texts[int(zh)].replace(link, link + "\n\n" + continuation)
                report = self.check(texts)[int(zh)]
                self.assertTrue(any("Source must be plain prose with inline links" in error for error in report.errors), report.errors)
                code, output = self.run_main()
                self.assertEqual(code, 1, output)
                self.assertIn("Source must be plain prose with inline links", output)

    def test_source_real_links_outside_comments_stay_valid(self):
        link = "[design](https://example.org/design)"
        for value in ("Plain prose. <!-- note --> " + link,
                      "Plain prose. <!-- hidden\n  <div>[fake](https://example.org/fake)</div> -->\n  " + link,
                      "[`src.py`](https://example.org/src.py) <!-- note -->"):
            texts = [text.replace(link, value) for text in self.originals]
            self.assertEqual([e for r in self.check(texts) for e in r.errors], [])
            code, output = self.run_main()
            self.assertEqual(code, 0, output)

    def test_shape_positions_extra_content_and_literal_headings(self):
        edits = [
            (lambda text, zh: re.sub(r"(?m)^(### 1\..*)$", r"\1\n\nUnexpected paragraph.", text), "top-level"),
            (lambda text, zh: text.replace("Value 1-0.", "Value 1-0.\n- **Extra:** value", 1), "four labels"),
            (lambda text, zh: text.replace("### 1.", "### No number", 1), "continuous"),
            (lambda text, zh: text.replace("### 1.", "```markdown\n### 1.", 1).replace("### 2.", "```\n\n### 2.", 1), "at least 2"),
        ]
        for edit, needle in edits:
            with self.subTest(needle=needle):
                self.assert_bad(edit, needle)
        for which in ("image", "block"):
            def move(text, zh):
                pattern = r"(?m)^!\[Demo — (?:mechanism diagram|机制图)\].*\n" if which == "image" else self.mc.BLOCK_RE
                match = re.search(pattern, text) if isinstance(pattern, str) else pattern.search(text)
                value = match[0]
                text = text[:match.start()] + text[match.end():]
                return text.replace("Value 1-3.", "Value 1-3.\n" + value) if "Value 1-3." in text else text.replace("### 2.", value + "\n\n### 2.")
            self.assert_bad(move, "before first technique")

    def test_literal_images_and_blocks_do_not_satisfy_structure(self):
        self.assert_bad(lambda text, zh: re.sub(r"(?m)^(!\[Demo — (?:mechanism diagram|机制图)\].*)$", r"```markdown\n\1\n```", text), "mechanism image")
        self.assert_bad(lambda text, zh: self.mc.BLOCK_RE.sub(lambda m: "```markdown\n" + m[0] + "\n```", text), "mechanism text block missing")

    def test_hostile_heading_number_is_rejected_without_integer_conversion(self):
        self.assert_bad(lambda text, zh: text.replace("### 1.", "### " + "9" * 5000 + ".", 1), "continuous")

    def test_legal_indented_continuations_and_seven_techniques_warning(self):
        from test_mechanism_card import technique_body
        texts = [text.replace("Value 1-0.", "Value 1-0.\n  continued text") for text in self.originals]
        self.assertEqual([e for r in self.check(texts) for e in r.errors], [])
        for path, zh in ((self.page, False), (self.page.with_name("demo.zh.md"), True)):
            text = self.originals[int(zh)]
            span = self.mc.section_bounds(text, "zh" if zh else "en")
            body = text[span[0]:span[1]]
            start = body.index("### 1.")
            path.write_text(text[:span[0]] + body[:start] + technique_body(zh, 7) + "\n\n" + text[span[1]:])
        self.spec["nodes"][1]["technique"] = list(range(1, 8))
        self.source.write_text(json.dumps(self.spec))
        self.generate()
        for report in self.check():
            self.assertEqual(report.errors, [])
            self.assertTrue(any("more than 6" in w for w in report.warnings))


class SourceCitationTest(unittest.TestCase):
    def test_large_unclosed_link_titles_finish_within_deadline(self):
        import subprocess
        script = "import lint; assert not lint.has_source_link('[a](x y ' * 8000); print('bounded citation PASS bytes=64000')"
        result = subprocess.run([sys.executable, "-B", "-c", script], cwd=Path(lint.__file__).parent,
                                text=True, capture_output=True, stdin=subprocess.DEVNULL, timeout=3)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("bounded citation PASS bytes=64000", result.stdout)

    def test_code_runs_and_escape_parity(self):
        for text, expected in (
            ("", False), ("[x](url)", True), ("[`x.py`](url)", True),
            (r"\[x](url)", False), (r"\\[x](url)", True), (r"\\\[x](url)", False),
            ("`[x](url)`", False), ("``[x](url)``", False),
            ("``code ` [x](url)``", False), ("`unmatched [x](url)", True),
            ("![`x`](url)", False), (r"\![x](url)", True), (r"\`[x](url)", True),
            ("[x]( )", False), ("[x](url 'title')", True),
            ('[x](url "a \\"quote\\"")', True), ("[x](url (title))", True),
            ("[x](url unquoted)", False),
        ):
            with self.subTest(text=text):
                self.assertEqual(lint.has_source_link(text), expected)

    def test_malformed_citation_seeds_terminate(self):
        # No fuzz dependency: truncated, mismatched quotes, repetition and invalid-byte seeds.
        for text in ("[open](", '[x]("unterminated', "[x](" * 1000,
                     "`" * 1000, b"\xff[broken](".decode("utf-8", "replace")):
            with self.subTest(seed=text[:30]):
                self.assertIs(lint.has_source_link(text), False)


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

    def test_canonical_package_named_by_the_override_table_is_allowed(self) -> None:
        """shadcn-ui/ui ships the CLI as `shadcn`: neither the repo name nor the owner
        scope, but a human recorded it in tools/health_package_overrides.json."""
        block = adoption_block("A", ["registry: npmjs.org", "canonical_package: shadcn",
                                     "downloads_last_month: 900000"])
        table = {"example/demo": {"registry": "npmjs.org", "name": "shadcn", "reason": "t"}}
        with mock.patch("lint._load_package_overrides", return_value=table):
            self.assertEqual(self.errors_for(block, "matches neither"), [])
        # The table vouches for one registry + name, not for anything on that repo.
        other = adoption_block("A", ["registry: nuget.org", "canonical_package: shadcn",
                                     "downloads_last_month: 900000"])
        with mock.patch("lint._load_package_overrides", return_value=table):
            self.assertTrue(self.errors_for(other, "matches neither"))

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
