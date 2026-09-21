#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import flow_card
import lint
from test_lint import page_text

SPEC = {
    "schema": 1,
    "them": {"en": "Demo does", "zh": "Demo 做的"},
    "steps": [
        {"lane": "you", "en": "Install it", "zh": "安装", "code": "pip install demo"},
        {"lane": "them", "en": "Registers a hook", "zh": "注册钩子"},
        {"lane": "you", "en": "Call the API", "zh": "调用接口", "code": "demo.run()"},
        {"lane": "them", "en": "Does the work", "zh": "完成工作"},
    ],
    "value": {"en": "Less code to write", "zh": "少写代码"},
    "sources": ["README#usage"],
}


def with_flow_section(text: str, zh: bool, section: str | None = None) -> str:
    heading = "## 怎么用起来" if zh else "## How it works"
    para = "它会替你完成工作。" if zh else "It does the work for you."
    img = f"![demo — {'主干用户故事' if zh else 'backbone user story'}](../../assets/flow/demo{'.zh' if zh else ''}.svg)"
    block = section if section is not None else f"{heading}\n\n{para}\n\n{img}\n\n"
    nxt = "## 何时不用" if zh else "## When NOT to use"
    return text.replace(nxt, block + nxt, 1)


class FlowSpecTest(unittest.TestCase):
    def test_valid_spec_passes(self) -> None:
        self.assertEqual(flow_card.validate_spec(SPEC), [])

    def test_rejects_bad_lane_step_count_single_lane_and_missing_sources(self) -> None:
        bad = copy.deepcopy(SPEC)
        bad["steps"][0]["lane"] = "platform"
        self.assertTrue(any("lane must be" in e for e in flow_card.validate_spec(bad)))

        short = copy.deepcopy(SPEC)
        short["steps"] = short["steps"][:2]
        self.assertTrue(any("3–9 items" in e for e in flow_card.validate_spec(short)))

        one_lane = copy.deepcopy(SPEC)
        for st in one_lane["steps"]:
            st["lane"] = "you"
        self.assertTrue(any("both lanes" in e for e in flow_card.validate_spec(one_lane)))

        nosrc = copy.deepcopy(SPEC)
        nosrc["sources"] = []
        self.assertTrue(any("sources" in e for e in flow_card.validate_spec(nosrc)))

    def test_rejects_missing_translation_and_overlong_step(self) -> None:
        bad = copy.deepcopy(SPEC)
        del bad["steps"][1]["zh"]
        bad["steps"][2]["en"] = "x" * 200
        errs = flow_card.validate_spec(bad)
        self.assertTrue(any("steps[2].zh" in e for e in errs))
        self.assertTrue(any("steps[3].en is 200 chars" in e for e in errs))

    def test_render_is_deterministic_and_escapes(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["steps"][2]["code"] = '@Hook("<x>")'
        a, b = flow_card.render(spec, "en"), flow_card.render(spec, "en")
        self.assertEqual(a, b)
        self.assertIn("&lt;x&gt;", a)
        self.assertNotIn('("<x>")', a)
        self.assertIn("prefers-color-scheme: dark", a)

    def test_wrap_keeps_cjk_lines_within_width_and_avoids_orphans(self) -> None:
        lines = flow_card.wrap("按顺序跑这条路由上的插件，任一不放行就直接拒绝", 15, 300)
        self.assertGreater(len(lines), 1)
        self.assertGreater(len(lines[-1]), 2)
        self.assertTrue(all(flow_card.text_w(ln, 15) <= 300 + 15 * 3 for ln in lines))

    def test_wrap_never_starts_a_line_with_cjk_trailing_punctuation(self) -> None:
        lines = flow_card.wrap("给你的机器做硬件画像，按估算的 tok/s、精度、内存给模型排名", 15, 300)
        self.assertGreater(len(lines), 1)
        self.assertFalse(any(ln[0] in "、，。；：！？）" for ln in lines[1:]), lines)

    def test_component_is_optional_and_validated(self) -> None:
        self.assertEqual(flow_card.validate_spec(copy.deepcopy(SPEC)), [])

        with_component = copy.deepcopy(SPEC)
        with_component["steps"][0]["component"] = {"en": "executor", "zh": "执行器"}
        self.assertEqual(flow_card.validate_spec(with_component), [])

        bad = copy.deepcopy(with_component)
        del bad["steps"][0]["component"]["zh"]
        self.assertTrue(any("steps[1].component.zh" in e for e in flow_card.validate_spec(bad)))

        overlong = copy.deepcopy(with_component)
        overlong["steps"][0]["component"]["en"] = "x" * 200
        self.assertTrue(any("steps[1].component.en is 200 chars" in e
                            for e in flow_card.validate_spec(overlong)))

        empty = copy.deepcopy(with_component)
        empty["steps"][0]["component"]["zh"] = "   "
        self.assertTrue(any("steps[1].component.zh" in e for e in flow_card.validate_spec(empty)))

    def test_render_and_steps_block_carry_component(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["steps"][0]["component"] = {"en": "executor", "zh": "执行器"}
        spec["steps"][1]["component"] = {"en": 'a<b>', "zh": "被<a>转义"}

        en_svg = flow_card.render(spec, "en")
        self.assertIn("component: executor", en_svg)
        self.assertIn("component: a&lt;b&gt;", en_svg)
        self.assertNotIn("component: a<b>", en_svg)

        zh_svg = flow_card.render(spec, "zh")
        self.assertIn("组件：执行器", zh_svg)
        self.assertIn("组件：被&lt;a&gt;转义", zh_svg)

        block = flow_card.steps_block(spec, "zh", "demo", "Demo")
        self.assertIn("1. **你**：安装 — `pip install demo` — 组件：`执行器`", block)
        # angle brackets must sit inside a code span so GitHub does not parse them as HTML
        self.assertIn("2. **Demo**：注册钩子 — 组件：`被<a>转义`", block)
        self.assertNotIn("组件：被<a>", block)

    def test_steps_without_component_render_unchanged(self) -> None:
        svg = flow_card.render(SPEC, "en")
        self.assertNotIn("component:", svg)
        self.assertNotIn(".comp", svg)
        self.assertNotIn("component:", flow_card.steps_block(SPEC, "en", "demo", "Demo"))

    def test_steps_block_uses_page_name_as_actor(self) -> None:
        block = flow_card.steps_block(SPEC, "zh", "demo", "Demo")
        self.assertIn("2. **Demo**：注册钩子", block)
        self.assertIn("1. **你**：安装 — `pip install demo`", block)
        self.assertIn("**价值**：少写代码", block)


class FlowLintTest(unittest.TestCase):
    def _setup(self, root: Path, zh: bool = False, section: str | None = None, spec: dict | None = SPEC) -> Path:
        page = root / "categories" / "demo" / ("demo.zh.md" if zh else "demo.md")
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(with_flow_section(page_text(zh=zh), zh, section), encoding="utf-8")
        (root / "assets" / "health").mkdir(parents=True, exist_ok=True)
        (root / "assets" / "health" / ("demo.zh.svg" if zh else "demo.svg")).write_text("<svg />", encoding="utf-8")
        if spec is not None:
            (root / "flows").mkdir(exist_ok=True)
            (root / "flows" / "demo.json").write_text(json.dumps(spec, ensure_ascii=False), encoding="utf-8")
            lang = "zh" if zh else "en"
            (root / "assets" / "flow").mkdir(parents=True, exist_ok=True)
            (root / "assets" / "flow" / flow_card.card_name("demo", lang)).write_text(
                flow_card.render(spec, lang), encoding="utf-8")
            flow_card.sync_page(page, root, spec, "demo")
        return page

    def _lint(self, page: Path, root: Path) -> lint.Report:
        rep = lint.Report()
        lint.check_flow_section(page, page.read_text(encoding="utf-8"), page.name.endswith(".zh.md"), root, set(), rep)
        return rep

    def test_complete_section_is_clean_in_both_languages(self) -> None:
        for zh in (False, True):
            with tempfile.TemporaryDirectory() as td:
                root = Path(td)
                page = self._setup(root, zh=zh)
                rep = self._lint(page, root)
                self.assertEqual(rep.errors, [], rep.errors)
                self.assertIn("<!-- flow-steps:begin", page.read_text(encoding="utf-8"))

    def test_missing_section_is_only_tallied_during_backfill(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(), encoding="utf-8")
            rep = self._lint(page, root)
            self.assertEqual(rep.errors, [])
            self.assertEqual(rep.flow_missing, [page])

    def test_missing_section_is_an_error_for_a_freshly_verified_page(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(), encoding="utf-8")
            rep = lint.Report()
            lint.check_flow_section(page, page.read_text(encoding="utf-8"), False, root, set(), rep,
                                    lint.FLOW_REQUIRED_FROM)
            self.assertTrue(any("missing required section: ## How it works" in e for e in rep.errors))

            older = lint.Report()
            lint.check_flow_section(page, page.read_text(encoding="utf-8"), False, root, set(), older, "2026-06-29")
            self.assertEqual(older.errors, [])
            self.assertEqual(older.flow_missing, [page])

    def test_spec_without_section_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = root / "categories" / "demo" / "demo.md"
            page.parent.mkdir(parents=True)
            page.write_text(page_text(), encoding="utf-8")
            (root / "flows").mkdir()
            (root / "flows" / "demo.json").write_text(json.dumps(SPEC), encoding="utf-8")
            rep = self._lint(page, root)
            self.assertTrue(any("has no '## How it works' section" in e for e in rep.errors))

    def test_hand_edited_step_list_is_drift(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = self._setup(root)
            page.write_text(page.read_text(encoding="utf-8").replace("Registers a hook", "Registers two hooks"),
                            encoding="utf-8")
            rep = self._lint(page, root)
            self.assertTrue(any("drifted from flows/demo.json" in e for e in rep.errors))

    def test_stale_card_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = self._setup(root)
            (root / "assets" / "flow" / "demo.svg").write_text("<svg />", encoding="utf-8")
            rep = self._lint(page, root)
            self.assertTrue(any("flow card stale" in e for e in rep.errors))

    def test_section_in_wrong_position_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = self._setup(root)
            text = page.read_text(encoding="utf-8")
            start = text.index("## How it works")
            end = text.index("## When NOT to use")
            section = text[start:end]
            text = text[:start] + text[end:]
            text = text.replace("## Comparison", section + "## Comparison", 1)
            page.write_text(text, encoding="utf-8")
            rep = self._lint(page, root)
            self.assertTrue(any("must sit between" in e for e in rep.errors))

    def test_missing_mechanism_prose_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            img = "![demo — backbone user story](../../assets/flow/demo.svg)"
            page = self._setup(root, section=f"## How it works\n\n{img}\n\n")
            rep = self._lint(page, root)
            self.assertTrue(any("mechanism paragraph missing" in e for e in rep.errors))

    def test_invalid_spec_is_reported_on_the_spec_file(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            page = self._setup(root)
            bad = copy.deepcopy(SPEC)
            bad["sources"] = []
            (root / "flows" / "demo.json").write_text(json.dumps(bad), encoding="utf-8")
            rep = self._lint(page, root)
            self.assertTrue(any("demo.json" in e and "sources" in e for e in rep.errors))


class FlowPhaseTest(unittest.TestCase):
    """`phase` labels a lifecycle stage; it must never read as a branch or as extra lanes."""

    def _phased(self) -> dict:
        spec = copy.deepcopy(SPEC)
        spec["steps"][0]["phase"] = {"en": "Build", "zh": "搭建"}
        spec["steps"][2]["phase"] = {"en": "Every turn", "zh": "每轮运行"}
        return spec

    def test_valid_phases_pass_and_inherit_until_the_next_marker(self) -> None:
        spec = self._phased()
        self.assertEqual(flow_card.validate_spec(spec), [])
        self.assertEqual([p["en"] if p else None for p in flow_card.phases_of(spec)],
                         ["Build", "Build", "Every turn", "Every turn"])

    def test_a_marker_off_the_first_step_is_rejected(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["steps"][1]["phase"] = {"en": "Run", "zh": "运行"}
        self.assertTrue(any("first stage would be unlabeled" in e for e in flow_card.validate_spec(spec)))

    def test_repeating_the_open_stage_is_rejected(self) -> None:
        spec = copy.deepcopy(SPEC)
        spec["steps"][0]["phase"] = {"en": "Build", "zh": "搭建"}
        spec["steps"][1]["phase"] = {"en": "Build", "zh": "搭建"}
        self.assertTrue(any("repeats the stage already open" in e for e in flow_card.validate_spec(spec)))

    def test_more_than_three_stages_and_bad_labels_are_rejected(self) -> None:
        spec = copy.deepcopy(SPEC)
        for st, label in zip(spec["steps"], ("A", "B", "C", "D")):
            st["phase"] = {"en": label, "zh": label}
        self.assertTrue(any("at most 3 phases" in e for e in flow_card.validate_spec(spec)))

        long_en = self._phased()
        long_en["steps"][0]["phase"] = {"en": "x" * 25, "zh": "搭建"}
        self.assertTrue(any("phase.en is 25 chars" in e for e in flow_card.validate_spec(long_en)))

        not_bilingual = self._phased()
        not_bilingual["steps"][0]["phase"] = "Build"
        self.assertTrue(any("phase must be an object" in e for e in flow_card.validate_spec(not_bilingual)))

    def test_a_phase_less_spec_renders_byte_identical_to_the_pre_phase_renderer(self) -> None:
        # Backward compatibility: 53 specs predate the field, so adding it must not touch them.
        for lang in ("en", "zh"):
            svg = flow_card.render(SPEC, lang)
            self.assertNotIn(".ph{", svg)
            self.assertNotIn('class="ph"', svg)

    def test_phased_render_labels_every_card_of_the_stage(self) -> None:
        svg = flow_card.render(self._phased(), "en")
        self.assertEqual(svg.count('class="ph"'), len(SPEC["steps"]))
        self.assertEqual(svg.count(">Build<"), 2)
        self.assertEqual(svg.count(">Every turn<"), 2)
        self.assertIn(".ph{", svg)

    def test_steps_block_carries_the_stage_on_every_step(self) -> None:
        block = flow_card.steps_block(self._phased(), "zh", "demo", "Demo")
        self.assertIn("1. **你**（搭建）：安装", block)
        self.assertIn("2. **Demo**（搭建）：注册钩子", block)
        self.assertIn("4. **Demo**（每轮运行）：完成工作", block)


if __name__ == "__main__":
    unittest.main()
