#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import contextlib
import io
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mechanism_card as mc


SPEC = {
    "schema": 1, "direction": "right",
    "nodes": [
        {"id": "input", "en": "Input", "zh": "输入", "kind": "input"},
        {"id": "parse", "en": "Parse", "zh": "解析", "technique": [1]},
        {"id": "save", "en": "Save", "zh": "保存", "kind": "output", "technique": [2]},
    ],
    "edges": [{"from": "input", "to": "parse"},
              {"from": "parse", "to": "save", "en": "valid", "zh": "有效", "style": "dashed"}],
    "sources": ["https://example.org/design"],
}


def technique_body(zh=False, count=2):
    labels = ("解决：", "做法：", "边界：", "源码：") if zh else ("Problem:", "How:", "Limits:", "Source:")
    return "\n\n".join(f"### {n}. {'拆招' if zh else 'Technique'} {n}\n\n" + "\n".join(
        f"- **{label}** " + ("[design](https://example.org/design)" if i == 3 else f"Value {n}-{i}.")
        for i, label in enumerate(labels)) for n in range(1, count + 1))


def fake_d2(root):
    """External process stub; no real d2 dependency, including when PATH is empty."""
    path = root / "fake-d2"
    path.write_text(f"#!{sys.executable}\n" + '''import json, pathlib, sys
args = sys.argv[1:]
data = sys.stdin.read()
with open(str(pathlib.Path(__file__)) + '.calls', 'a') as f:
    f.write(json.dumps({'args': args, 'data': data}) + '\\n')
if 'FAIL_RENDER' in data:
    sys.stderr.write('deliberate renderer failure')
    sys.exit(7)
print('<?xml version="1.0" encoding="UTF-8"?><svg xmlns="http://www.w3.org/2000/svg"><text>stub</text></svg>')
''', encoding="utf-8")
    path.chmod(0o755)
    return str(path)


class MechanismCLITest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.page = self.root / "categories/nested/demo/demo.md"
        self.page.parent.mkdir(parents=True)
        for lang in ("en", "zh"):
            page = self.page.with_name("demo.zh.md") if lang == "zh" else self.page
            page.write_text("# Demo\n\n" + mc.SECTION[lang] + "\n\n" + technique_body(lang == "zh") + "\n\n## " + ("存疑（未验证）" if lang == "zh" else "Caveats (unverified)") + "\n\nUnchanged.\n")
        (self.root / "mechanisms").mkdir()
        self.source = self.root / "mechanisms/demo.json"
        self.source.write_text(json.dumps(SPEC, ensure_ascii=False))
        patcher = mock.patch.object(mc, "ROOT", self.root)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.d2 = fake_d2(self.root)

    def run_cli(self, *args, d2=True):
        out = io.StringIO()
        with mock.patch.object(mc.shutil, "which", return_value=self.d2 if d2 else None), contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            code = mc.main(list(args))
        return code, out.getvalue()

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes() for folder in ("categories", "assets") for p in (self.root / folder).rglob("*") if p.is_file()}

    def test_cli_bilingual_idempotent_local_writes_and_elk(self):
        code, output = self.run_cli(str(self.page.with_name("demo.zh.md")), str(self.page))
        self.assertEqual(code, 0, output)
        self.assertIn("4 mechanism artifact(s) updated", output)
        for suffix in ("", ".zh"):
            svg = (self.root / f"assets/mechanism/demo{suffix}.svg").read_text()
            ET.fromstring(svg)
            want_hash = hashlib.sha256((json.dumps(SPEC, sort_keys=True, ensure_ascii=False) + mc.RENDER_VERSION).encode()).hexdigest()
            self.assertIn(f"<!-- mechanism-src sha256={want_hash} -->", svg)
            page = self.page.with_name(f"demo{suffix}.md").read_text()
            self.assertIn(f"../../../assets/mechanism/demo{suffix}.svg", page)
            self.assertIn("## " + ("存疑（未验证）" if suffix else "Caveats (unverified)") + "\n\nUnchanged.", page)
            self.assertIn("mechanism:begin", page)
        self.assertIn("Noto Sans CJK SC", (self.root / "assets/mechanism/demo.zh.svg").read_text())
        calls = [json.loads(line) for line in Path(self.d2 + ".calls").read_text().splitlines()]
        self.assertEqual(len(calls), 2)
        self.assertTrue(all(call["args"][:2] == ["--layout", "elk"] for call in calls))
        self.assertIn("Parse①", calls[0]["data"])
        before = self.snapshot()
        code, output = self.run_cli("--all")
        self.assertEqual(code, 0, output)
        self.assertIn("0 mechanism artifact(s) updated", output)
        self.assertEqual(self.snapshot(), before)

    def test_cli_chinese_argument_alone_updates_both_siblings(self):
        code, output = self.run_cli(str(self.page.with_name("demo.zh.md")))
        self.assertEqual(code, 0, output)
        self.assertIn("4 mechanism artifact(s) updated", output)
        for suffix in ("", ".zh"):
            self.assertIn("mechanism:begin", self.page.with_name(f"demo{suffix}.md").read_text())
            self.assertTrue((self.root / f"assets/mechanism/demo{suffix}.svg").is_file())

    def test_kts_acc2_18_missing_d2_exit_two_without_partial_files(self):
        for existing in (False, True):
            if existing:
                self.assertEqual(self.run_cli(str(self.page))[0], 0)
            before = self.snapshot()
            code, output = self.run_cli(str(self.page), d2=False)
            self.assertEqual(code, 2, output)
            self.assertIn("brew install d2", output)
            self.assertEqual(self.snapshot(), before)

    def test_check_spec_and_empty_all_need_no_d2_and_do_not_write(self):
        before = self.snapshot()
        self.assertEqual(self.run_cli("--check-spec", str(self.source), d2=False)[0], 0)
        self.assertEqual(self.snapshot(), before)
        self.source.write_text("{bad")
        code, output = self.run_cli("--check-spec", str(self.source), d2=False)
        self.assertEqual(code, 1)
        self.assertIn("demo.json", output)
        self.source.unlink()
        code, output = self.run_cli("--all", d2=False)
        self.assertEqual(code, 0, output)
        self.assertIn("0 mechanism artifact(s) updated", output)
        self.assertEqual(self.snapshot(), before)

    def test_render_failure_and_escaping(self):
        spec = copy.deepcopy(SPEC)
        spec["nodes"][1]["en"] = 'quoted "text"\\newline\n -> dangerous: {x}'
        self.source.write_text(json.dumps(spec))
        self.assertEqual(self.run_cli(str(self.page))[0], 0)
        call = json.loads(Path(self.d2 + ".calls").read_text().splitlines()[0])
        self.assertIn(json.dumps(spec["nodes"][1]["en"] + "①", ensure_ascii=False), call["data"])
        spec["nodes"][2]["zh"] = "FAIL_RENDER"
        self.source.write_text(json.dumps(spec))
        before = self.snapshot()
        code, output = self.run_cli(str(self.page))
        self.assertEqual(code, 1)
        self.assertIn("zh", output)
        self.assertIn("deliberate renderer failure", output)
        self.assertEqual(self.snapshot(), before)

    def test_cli_uses_duplicate_slug_stems_and_ignores_literal_image(self):
        other = self.root / "categories/other/demo.md"
        other.parent.mkdir(parents=True)
        other.write_text("# Duplicate slug\n")
        self.source.rename(self.source.with_name("nested-demo-demo.json"))
        # The real stem now has the full category prefix; a fenced image is only an example.
        for page, suffix in ((self.page, ""), (self.page.with_name("demo.zh.md"), ".zh")):
            text = page.read_text()
            example = f"```markdown\n![Example](../../../assets/mechanism/nested-demo-demo{suffix}.svg)\n```\n\n"
            page.write_text(text.replace("### 1.", example + "### 1.", 1))
        code, output = self.run_cli(str(self.page))
        self.assertEqual(code, 0, output)
        for page, suffix in ((self.page, ""), (self.page.with_name("demo.zh.md"), ".zh")):
            self.assertTrue((self.root / f"assets/mechanism/nested-demo-demo{suffix}.svg").exists())
            self.assertIn("```markdown\n![Example]", page.read_text())
            visible, blocks = mc.scan_body(page.read_text())
            self.assertEqual(len([line for _, _, line in visible if line.startswith("![") and "/mechanism/" in line]), 1)
            self.assertEqual(len(blocks), 1)

    def test_invalid_renderer_output_is_not_published(self):
        before = self.snapshot()
        for output in ("not XML", "<html />"):
            response = mc.subprocess.CompletedProcess([], 0, output, "")
            with mock.patch.object(mc.subprocess, "run", return_value=response):
                code, diagnostic = self.run_cli(str(self.page))
            self.assertEqual(code, 1, diagnostic)
            self.assertIn("SVG", diagnostic)
            self.assertEqual(self.snapshot(), before)


class MechanismSpecTest(unittest.TestCase):
    def test_sources_metadata_is_not_an_extra_required_field(self):
        for sources in ("absent", []):
            spec = copy.deepcopy(SPEC)
            if sources == "absent":
                del spec["sources"]
            else:
                spec["sources"] = sources
            self.assertEqual(mc.validate_spec(spec, 2), [])

    def test_d2_labels_keep_placeholders_quotes_and_backslashes_literal(self):
        cases = (
            ('Read ${name}', r'"Read \${name}"'),
            ('Read "${name}"', r'"Read \"\${name}\""'),
            ('Path \\${name}', r'"Path \\\${name}"'),
            ('Cost $5\\tail\nnext', r'"Cost \$5\\tail\nnext"'),
        )
        for value, quoted in cases:
            for lang in ("en", "zh"):
                with self.subTest(value=value, lang=lang):
                    spec = copy.deepcopy(SPEC)
                    spec["nodes"][0][lang] = value
                    spec["edges"][0].update(en=value, zh=value)
                    self.assertEqual(mc.validate_spec(spec, 2), [])
                    source = mc.d2_source(spec, lang)
                    self.assertIn(f"n0: {quoted} {{", source)
                    self.assertIn(f"n0 -> n1: {quoted}", source)

    def test_default_step_down_direction_and_malformed_values(self):
        explicit = copy.deepcopy(SPEC)
        explicit["nodes"][1]["kind"] = "step"
        self.assertEqual(mc.d2_source(SPEC, "en"), mc.d2_source(explicit, "en"))
        explicit["direction"] = "down"
        self.assertEqual(mc.validate_spec(explicit, 2), [])
        self.assertIn("direction: down", mc.d2_source(explicit, "zh"))
        for value in (None, [], {}, True, 17, "bad"):
            for field in ("nodes", "edges", "sources"):
                spec = copy.deepcopy(SPEC)
                spec[field] = value
                # No implicit connectivity or extra mandatory graph-source metadata.
                if field in ("edges", "sources") and value == []:
                    self.assertEqual(mc.validate_spec(spec), [])
                else:
                    self.assertTrue(mc.validate_spec(spec))
        for value in (None, 4, [], "bad"):
            for field in ("nodes", "edges"):
                spec = copy.deepcopy(SPEC)
                spec[field][0] = value
                self.assertTrue(mc.validate_spec(spec))
    def test_json_schema_and_mapping_boundaries(self):
        self.assertEqual(mc.validate_spec(SPEC, 2), [])
        for count, valid in ((2, False), (3, True), (12, True), (13, False)):
            spec = copy.deepcopy(SPEC)
            spec["nodes"] = [{"id": f"n{i}", "en": "Node", "zh": "节点"} for i in range(count)]
            spec["edges"] = []
            self.assertEqual(not mc.validate_spec(spec), valid)
        for key, value, needle in (("schema", 2, "schema"), ("direction", "left", "direction"),
                                   ("nodes", None, "nodes"), ("edges", None, "edges"),
                                   ("sources", [None], "sources")):
            spec = copy.deepcopy(SPEC)
            spec[key] = value
            self.assertTrue(any(needle in e for e in mc.validate_spec(spec)))
        for change, needle in (({"id": "input"}, "unique"), ({"en": " "}, "en"),
                               ({"zh": None}, "zh"), ({"kind": "database"}, "kind"),
                               ({"technique": [True]}, "technique")):
            spec = copy.deepcopy(SPEC)
            spec["nodes"][1].update(change)
            self.assertTrue(any(needle in e for e in mc.validate_spec(spec, 2)), change)
        for change, needle in (({"to": "missing"}, "endpoint"), ({"en": "only"}, "zh"),
                               ({"style": "solid"}, "style")):
            spec = copy.deepcopy(SPEC)
            spec["edges"][0].update(change)
            self.assertTrue(any(needle in e for e in mc.validate_spec(spec)), change)
        self.assertTrue(mc.validate_spec(None))

    def test_kts_acc2_13_node_technique_out_of_range(self):
        spec = copy.deepcopy(SPEC)
        spec["nodes"][1]["technique"] = [3]
        self.assertTrue(any("range 1..2" in e for e in mc.validate_spec(spec, 2)))

    def test_kts_acc2_14_each_technique_needs_a_node(self):
        spec = copy.deepcopy(SPEC)
        del spec["nodes"][2]["technique"]
        self.assertTrue(any("technique 2 has no node" in e for e in mc.validate_spec(spec, 2)))

    def test_text_version_preserves_order_labels_and_numbers(self):
        text = mc.text_block(SPEC, "zh", "demo")
        self.assertIn("输入 → 解析①", text)
        self.assertIn("解析① → 保存②（有效）", text)
        self.assertLess(text.index("- 输入"), text.index("- 解析①"))
        self.assertIn("Parse① → Save② (valid)", mc.text_block(SPEC, "en", "demo"))
        spec = copy.deepcopy(SPEC)
        spec["nodes"][1]["technique"] = list(range(1, 8))
        self.assertIn("⑦", mc.text_block(spec, "en", "demo"))

    def test_generated_labels_cannot_inject_markdown_chapters_or_html(self):
        spec = copy.deepcopy(SPEC)
        spec["nodes"][0]["en"] = "Input\n\n## Injected\n<script>bad</script>"
        block = mc.text_block(spec, "en", "demo")
        self.assertNotIn("\n## Injected", block)
        self.assertNotIn("<script>", block)
        self.assertIn("&lt;script&gt;", block)

    def test_source_hash_has_an_independent_canonical_oracle(self):
        want = hashlib.sha256((json.dumps(SPEC, sort_keys=True, ensure_ascii=False) + mc.RENDER_VERSION).encode()).hexdigest()
        self.assertEqual(mc.spec_hash(SPEC), want)
        reordered = json.loads(json.dumps(SPEC, sort_keys=True))
        self.assertEqual(mc.spec_hash(reordered), want)
        changed = copy.deepcopy(SPEC)
        changed["nodes"][0]["en"] = "Different"
        self.assertNotEqual(mc.spec_hash(changed), want)
        with mock.patch.object(mc, "RENDER_VERSION", "next"):
            self.assertNotEqual(mc.spec_hash(SPEC), want)


if __name__ == "__main__":
    unittest.main()
