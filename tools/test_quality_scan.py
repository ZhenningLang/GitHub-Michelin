#!/usr/bin/env python3
from __future__ import annotations

import sys
import subprocess
import tempfile
import unittest
import re
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import quality_scan


ZERO_SHA = "0000000000000000000000000000000000000000"

# FINAL_REVIEW_B synthetic input, not a factual description of Bella Domify.
LINK_NOISE_REGRESSION = (
    "它不靠版面模型猜结构，而是先用 PyMuPDF 取出每个字符的坐标与字号，再按行距和缩进把字符聚成段落；"
    "表格单独走一条路：先找横竖线围出的格子，再把落在格子里的文字归位，没有线的表格只能退回按列对齐猜测，所以无框表常被拆散。"
    "标题层级不是读目录，而是按字号从大到小排名后映射到一到六级，字号相同就看是否加粗，这一步在扫描件上完全失效，因为扫描件没有文字层。"
    "见 [layout.py](https://github.com/acme/domify/blob/main/domify/layout.py#L40) 与 "
    "[table.py](https://github.com/acme/domify/blob/main/domify/table.py#L12)。"
)
# Frozen pure-agentic.zh technical section at 52128061: self-contained regression twin.
LINK_NOISE_TWIN = """- **将复用规则与项目上下文预算分开。** [scripts/context-check.sh:71–103](https://github.com/JonB32/pure-agentic/blob/ddadf731f1f6cff5c9761cd4c09408c0a5b82d22/scripts/context-check.sh#L71-L103) 统计标记项目上下文块以外的行数，脚本其它部分执行角色与上下文 80 行、规格 50 行预算。它让复用骨架短小，但排除块仍能变大；行数不衡量相关性或真实模型词元。
- **检查存储结构，但明确依赖缺口。** [scripts/context-check.sh:167–243](https://github.com/JonB32/pure-agentic/blob/ddadf731f1f6cff5c9761cd4c09408c0a5b82d22/scripts/context-check.sh#L167-L243) 解析 YAML 意图与知识块，应用 JSON Schema 校验器并汇集文件级错误。缺 Python 包会跳过校验，缺 schema 文件会返回空 schema；退出 0 不能解释为所有 schema 或门都查过。
- **对规格点名文件检测漂移。** [scripts/freshness-check.sh:32–104](https://github.com/JonB32/pure-agentic/blob/ddadf731f1f6cff5c9761cd4c09408c0a5b82d22/scripts/freshness-check.sh#L32-L104) 从 UNIFY 知识块读 base SHA、找规格、提取 Impact Zones，并将这些路径与当前 HEAD 比较。它能发现规划后的已提交改动；解析不到影响文件只警告并退出 0，比较也不查未暂存编辑或证明语义仍新鲜。"""


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


class KeyTechniquesTest(unittest.TestCase):
    def test_structured_cleanup_preserves_phase01_gating_policy(self):
        self.assertEqual(quality_scan.DUP_SECTIONS["Key techniques"], 0.15)
        self.assertEqual(quality_scan.DUP_SECTIONS["技术要点"], 0.15)
        self.assertEqual(quality_scan.DUP_MIN_CHARS, 120)
        self.assertEqual(quality_scan.GATED_DETERMINISTIC_CATEGORIES, {
            "generic-comparison-template", "indexed-page-marked-non-repo",
            "indexed-page-marked-not-indexed", "composite-alternative-partly-indexed",
            "truncation-fragment", "zh-link-to-english-sibling", "intake-stub-page-reverified",
            "duplicated-section-prose-reverified", "zh-lead-not-chinese-reverified",
        })

    @staticmethod
    def structured(body, zh=False, title="Shared title", image="same.svg"):
        labels = ("解决：", "做法：", "边界：", "源码：") if zh else ("Problem:", "How:", "Limits:", "Source:")
        block = "<!-- mechanism:begin (generated) -->\n" + ("Shared generated node → edge " * 80) + "\n<!-- mechanism:end -->"
        return f"![mechanism]({image})\n\n{block}\n\n### 1. {title}\n\n" + "\n".join(
            f"- **{label}** {body if i < 3 else '[reference](https://example.org/design)'}" for i, label in enumerate(labels))

    def test_structured_template_removed_values_and_continuations_retained(self):
        for zh in (False, True):
            text = self.structured("Distinct prose\n  continued", zh)
            normalized = quality_scan.technique_prose(text)
            self.assertNotIn("Shared generated", normalized)
            self.assertNotIn("Shared title", normalized)
            self.assertNotIn("mechanism]", normalized)
            self.assertNotIn("**", normalized)
            self.assertEqual(normalized.count("Distinct prose\n  continued"), 3)
            self.assertIn("reference", normalized)

    def test_structured_different_prose_not_duplicate_full_scoped_cli(self):
        for title, suffix, first, second in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                bodies = tuple(self.structured(body, suffix == ".zh.md") for body in (first, second))
                pages = self.technique_pair(root, title, suffix, bodies, fresh=True)
                for scope in (None, [pages[0]]):
                    result = quality_scan.scan(root, scope_paths=scope)
                    self.assertFalse([f for f in result.findings if f.category.startswith("duplicated-section-prose")])
                result = run_quality_scan_cli(root, "--fail-on-gated")
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_structured_copy_still_gated_with_different_titles_and_images(self):
        for title, suffix, first, _ in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                bodies = (self.structured(first, suffix == ".zh.md"), self.structured(first, suffix == ".zh.md", "Other title", "other.svg"))
                pages = self.technique_pair(root, title, suffix, bodies, fresh=True)
                result = quality_scan.scan(root, scope_paths=[pages[0]])
                self.assertEqual(len([f for f in result.findings if f.category == "duplicated-section-prose-reverified"]), 1)
                cli = run_quality_scan_cli(root, "--fail-on-gated")
                self.assertEqual(cli.returncode, 1, cli.stdout + cli.stderr)

    def test_malformed_generated_blocks_do_not_swallow_prose(self):
        for seed in ("<!-- mechanism:begin -->\nkept正文", '<!-- mechanism:begin "\nkept正文',
                     "<!-- mechanism:begin -->\n" * 1000 + "kept正文", "\ufffd<!-- mechanism:begin -->\nkept正文"):
            normalized = quality_scan.technique_prose(seed)
            self.assertIn("kept正文", normalized)
            self.assertLessEqual(len(normalized), len(seed))

    def test_conservative_title_escape_cannot_skip_line_breaks(self) -> None:
        # Multiline titles are deliberately unsupported here: retaining raw prose is conservative.
        for visible in ("visible prose", "可见正文（备注）"):
            for newline in ("\n", "\r", "\r\n"):
                raw = '[src](https://x/a.py "outer\\' + newline + visible + '")'
                expected = '[src]( "outer\\' + newline + visible + '")'
                with self.subTest(visible=visible, newline=repr(newline)):
                    self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_unescaped_angle_opener_keeps_literal_destination_prose(self) -> None:
        for visible in ("visible prose", "可见正文（备注）"):
            raw = "[src](<https://x/<" + visible + ">)"
            expected = "[src](<<" + visible + ">)"
            with self.subTest(visible=visible):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_unescaped_nested_parentheses_keep_literal_title_prose(self) -> None:
        for visible in ("visible prose", "可见正文（备注）"):
            raw = "[src](https://x/a.py (outer (" + visible + ")))"
            expected = "[src]( (outer (" + visible + ")))"
            with self.subTest(visible=visible):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_blank_line_in_title_keeps_literal_prose(self) -> None:
        for visible in ("visible prose", "可见正文（备注）"):
            raw = '[src](https://x/a.py "outer\n\n' + visible + '")'
            expected = '[src]( "outer\n\n' + visible + '")'
            with self.subTest(visible=visible):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_bare_destinations_reject_ascii_controls(self) -> None:
        for control in ("\x01", "\x07", "\x7f"):
            for visible in ("visible_prose", "可见正文（备注）"):
                raw = "[src](https://x/a" + control + visible + ")"
                expected = "[src](" + control + visible + ")"
                with self.subTest(control=repr(control), visible=visible):
                    self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_nonpunctuation_escape_cannot_hide_bare_whitespace(self) -> None:
        for whitespace in (" ", "\t"):
            for visible in ("visible prose", "可见正文（备注）"):
                escaped = visible.replace(" ", "\\ ")
                raw = "[src](https://x/a\\" + whitespace + escaped + ")"
                expected = "[src](\\" + whitespace + escaped + ")"
                with self.subTest(whitespace=repr(whitespace), visible=visible):
                    self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_legitimate_separated_titles_keep_existing_label_policy(self) -> None:
        for label in ("src", "来源"):
            for destination, separator, tooltip in (
                ("<https://x/a>", " ", '"tip"'),
                ("<https://x/a>", "\t", "'tip'"),
                ("https://x/a", " ", "(tip)"),
                (r"https://x/a\(b\)", " ", r'"tip \"quoted\""'),
            ):
                with self.subTest(label=label, tooltip=tooltip):
                    self.assertEqual(quality_scan.technique_prose(f"[{label}]({destination}{separator}{tooltip})"), label)

    def test_titles_without_destination_separator_remain_visible(self) -> None:
        for visible in ("visible prose", "可见正文（备注）"):
            for left, right in (("\"", "\""), ("'", "'"), ("(", ")")):
                raw = "[src](<https://x/a>" + left + visible + right + ")"
                expected = "[src](" + left + visible + right + ")"
                with self.subTest(visible=visible, delimiter=left):
                    self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_copied_prose_without_title_separator_is_gated(self) -> None:
        for title, suffix, first, other in self.cases():
            for left, right in (("\"", "\""), ("'", "'"), ("(", ")")):
                wrapper = "[src](<https://x/a.py>" + left + first + right + ")"
                visible = other + "[src](" + left + first + right + ")"
                flat = re.sub(r"\W+", " ", visible.lower()).strip()
                copied = re.sub(r"\W+", " ", first.lower()).strip()
                padding = "x" * (-flat.index(copied) % quality_scan.SHINGLE_STEP)
                with self.subTest(title=title, delimiter=left), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    self.technique_pair(root, title, suffix, (first, padding + other + wrapper), fresh=True)
                    result = quality_scan.scan(root)
                    self.assertEqual(len([f for f in result.findings if f.category == "duplicated-section-prose-reverified"]), 2)

    def test_angle_destinations_never_escape_line_endings(self) -> None:
        for visible in ("visible prose (note)", "可见正文（备注）"):
            for newline in ("\n", "\r", "\r\n"):
                raw = "[src](<https://x/a" + "\\" + newline + visible + ">)"
                expected = "[src](<\\" + newline + visible + ">)"
                with self.subTest(newline=repr(newline), visible=visible):
                    self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_copied_prose_after_escaped_angle_newline_is_gated(self) -> None:
        for title, suffix, first, other in self.cases():
            for newline in ("\n", "\r", "\r\n"):
                uri = "https://x/a.py"
                wrapper = "[src](<" + uri + "\\" + newline + first + ">)"
                visible = other + "[src](<\\" + newline + first + ">)"
                flat = re.sub(r"\W+", " ", visible.lower()).strip()
                copied = re.sub(r"\W+", " ", first.lower()).strip()
                padding = "x" * (-flat.index(copied) % quality_scan.SHINGLE_STEP)
                with self.subTest(title=title, newline=repr(newline)), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    self.technique_pair(root, title, suffix, (first, padding + other + wrapper), fresh=True)
                    result = quality_scan.scan(root)
                    self.assertEqual(len([f for f in result.findings if f.category == "duplicated-section-prose-reverified"]), 2)

    def test_parenthesized_link_targets_are_fully_removed(self) -> None:
        for raw, expected in (
            ("Keep [cursor](https://example.org/a(b(c))d), done (ordinary text).", "Keep cursor, done (ordinary text)."),
            ("先看[游标](https://example.org/a(b(c))d)，再保留（普通正文）。", "先看游标，再保留（普通正文）。"),
        ):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_bare_parenthesized_urls_keep_sentence_parentheses(self) -> None:
        for raw, expected in (
            ("See https://example.org/a(b)c, next (ordinary text).", "See , next (ordinary text)."),
            ("(see https://example.org/a(b(c))d) keep (ordinary text).", "(see ) keep (ordinary text)."),
            ("（见https://example.org/a(b)c）保留正文。", "（见）保留正文。"),
        ):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_malformed_links_keep_visible_prose(self) -> None:
        for raw, expected in (
            ("[src](https://x/a.py <visible paragraph (note)>)", "[src]( <visible paragraph (note)>)"),
            ("[open](https://x/a.py\nvisible paragraph (note) tail", "[open](\nvisible paragraph (note) tail"),
            ("[来源](https://x/a.py <必须保留的正文（备注）>)", "[来源]( <必须保留的正文（备注）>)"),
            ("[未闭合](https://x/a.py\n必须保留的正文 (备注) 后文", "[未闭合](\n必须保留的正文 (备注) 后文"),
        ):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_copied_prose_inside_malformed_links_remains_gated(self) -> None:
        for title, suffix, first, other in self.cases():
            for malformed in (f"See [src](https://github.com/o/r/blob/main/a.py <{first}>)",
                              f"Typo [b.py](https://github.com/o/r/blob/main/b.py\n{first} (end)"):
                with self.subTest(title=title, malformed=malformed[:40]), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    uri = "https://github.com/o/r/blob/main/" + ("a.py" if malformed.startswith("See") else "b.py")
                    visible = other + malformed.replace(uri, "")
                    flat = re.sub(r"\W+", " ", visible.lower()).strip()
                    copied = re.sub(r"\W+", " ", first.lower()).strip()
                    # The unchanged sampler visits every third start; align this positive fixture.
                    padding = "x" * (-flat.index(copied) % quality_scan.SHINGLE_STEP)
                    second = padding + other + malformed
                    self.assertEqual(quality_scan.technique_prose(second), padding + visible)
                    self.technique_pair(root, title, suffix, (first, second), fresh=True)
                    result = run_quality_scan_cli(root, "--fail-on-gated")
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_code_literals_keep_non_url_parameters(self) -> None:
        for raw, expected in (
            ('`cache[key](fallback)` and `f[x](durable_cursor="checkpoint", retry_policy="bounded")`',
             '`cache[key](fallback)` and `f[x](durable_cursor="checkpoint", retry_policy="bounded")`'),
            ('``[src](https://example.org/a(b)c)`` then `cache[key](fallback)`',
             '``[src]()`` then `cache[key](fallback)`'),
        ):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_escaped_link_openers_keep_literal_parentheses(self) -> None:
        for raw in (r"keep \[cursor](fallback(note)) and (ordinary text)", r"保留\[游标](fallback(note)) 与（普通正文）"):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), raw)

    def test_parenthesized_citations_do_not_make_original_prose_duplicate(self) -> None:
        first = LINK_NOISE_REGRESSION.split("见 [layout.py]")[0]
        second = "甲" + self.cases()[1][3][:200]
        target = "https://example.org/reference(foo)/distributed-cursor-checkpoint-recovery-and-leases"
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.technique_pair(root, "技术要点", ".zh.md", (first + f"见 [来源]({target})。", second + f"见 [来源]({target})。"), fresh=True)
            result = quality_scan.scan(root)
            self.assertEqual([f for f in result.findings if f.category.startswith("duplicated-section-prose")], [])

    def test_scan_removes_link_noise_before_comparing_both_sides(self) -> None:
        for title, suffix, first, other in self.cases():
            citations = " ".join(f"[{{label}}](https://github.com/acme/research/blob/0123456789abcdef/source/dispatch-{i}.py#L120-L240)" for i in range(4))
            # Equal-width, different labels keep the raw shared URLs in the same sampling phase.
            bodies = (citations.format(label="scheduler") + " " + first[:200], citations.format(label="fontglyph") + " " + other[:200])
            raw_grams = [quality_scan.shingles(body) for body in bodies]
            raw_ratio = len(raw_grams[0] & raw_grams[1]) / len(raw_grams[0])
            self.assertGreaterEqual(raw_ratio, quality_scan.DUP_SECTIONS[title])
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                pages = self.technique_pair(root, title, suffix, bodies, fresh=True)
                result = quality_scan.scan(root, scope_paths=[pages[0]])
                self.assertEqual([f for f in result.findings if f.category.startswith("duplicated-section-prose")], [])

    def test_scoped_copy_requires_normalizing_the_unscanned_twin(self) -> None:
        for title, suffix, first, _ in self.cases():
            visible = "citation " + first[:200]
            source = quality_scan.shingles(visible)
            # The raw twin deliberately has a different sampling phase; the visible copy does not.
            candidates = [f"[citation](https://example.org/{'z' * length}) " + first[:200] for length in (90, 91, 92)]
            raw = next((candidate for candidate in candidates if len(source & quality_scan.shingles(candidate)) / len(source) < quality_scan.DUP_SECTIONS[title]), None)
            self.assertIsNotNone(raw)
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                pages = self.technique_pair(root, title, suffix, (visible, raw), fresh=True)
                result = quality_scan.scan(root, scope_paths=[pages[0]])
                self.assertEqual(len([f for f in result.findings if f.category == "duplicated-section-prose-reverified"]), 1)

    def test_calibrated_thresholds_use_minimal_grid_with_margin(self) -> None:
        # Independently measured from the frozen 21-pair corpus at 52128061, after URL removal.
        for title, maximum in (("Key techniques", Fraction(3, 82)), ("技术要点", Fraction(1, 21))):
            with self.subTest(title=title):
                threshold = Fraction(str(quality_scan.DUP_SECTIONS[title]))
                self.assertGreaterEqual(threshold, maximum + Fraction(1, 10))
                self.assertLess(threshold - Fraction(1, 20), maximum + Fraction(1, 10))
                self.assertEqual((threshold * 20).denominator, 1)

    def test_inline_links_preserve_labels_in_both_languages(self) -> None:
        for raw, expected in (
            ("Keep [cursor](https://example.org/src.py#L40) and [lease](http://example.net/t.py?x=1&y=2). "
             "Keep the nearby words.", "Keep cursor and lease. Keep the nearby words."),
            ("先看[游标](https://example.org/src.py#L40)，再看[租约](http://example.net/t.py?x=1&y=2)。", "先看游标，再看租约。"),
        ):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_autolinks_removed_in_both_languages(self) -> None:
        for raw, expected in (
            ("See <https://example.org/a#part>, then <http://example.net/b>.", "See , then ."),
            ("见<https://example.org/a#part>；再看<http://example.net/b>。", "见；再看。"),
        ):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_bare_urls_preserve_adjacent_prose_in_both_languages(self) -> None:
        for raw, expected in (
            ("See http://example.net/b#L1,continue safely;https://example.org/a?x=1&y=2. End!", "See ,continue safely;. End!"),
            ("裸链https://example.net/b#L1之后保留中文。再看http://example.org/a?x=1&y=2；结束！", "裸链之后保留中文。再看；结束！"),
        ):
            with self.subTest(raw=raw):
                self.assertEqual(quality_scan.technique_prose(raw), expected)

    def test_original_short_chinese_link_noise_is_not_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.technique_pair(root, "技术要点", ".zh.md", (LINK_NOISE_REGRESSION, LINK_NOISE_TWIN), fresh=True)
            result = quality_scan.scan(root)
            self.assertEqual([f for f in result.findings if f.category.startswith("duplicated-section-prose")], [])

    def test_regression_normalized_shingles_are_prose_only(self) -> None:
        expected = (
            "它不靠版面模型猜结构，而是先用 PyMuPDF 取出每个字符的坐标与字号，再按行距和缩进把字符聚成段落；"
            "表格单独走一条路：先找横竖线围出的格子，再把落在格子里的文字归位，没有线的表格只能退回按列对齐猜测，所以无框表常被拆散。"
            "标题层级不是读目录，而是按字号从大到小排名后映射到一到六级，字号相同就看是否加粗，这一步在扫描件上完全失效，因为扫描件没有文字层。"
            "见 layout.py 与 table.py。"
        )
        self.assertEqual(quality_scan.shingles(quality_scan.technique_prose(LINK_NOISE_REGRESSION)), quality_scan.shingles(expected))

    def test_copied_labels_with_different_targets_remain_gated(self) -> None:
        for title, suffix, first, _ in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                bodies = (f"[{first}](https://example.org/a#L1)", f"[{first}](http://elsewhere.net/b#L2)")
                pages = self.technique_pair(root, title, suffix, bodies, fresh=True)
                result = quality_scan.scan(root, scope_paths=[pages[0]])
                duplicates = [f for f in result.findings if f.category == "duplicated-section-prose-reverified"]
                self.assertEqual([f.path for f in duplicates], [pages[0].relative_to(root).as_posix()])
                self.assertIn(pages[1].relative_to(root).as_posix(), duplicates[0].message)

    def test_linked_copies_cli_fresh_and_old_in_both_languages(self) -> None:
        for title, suffix, first, _ in self.cases():
            for fresh, expected_code, category in ((True, 1, "duplicated-section-prose-reverified"), (False, 0, "duplicated-section-prose")):
                with self.subTest(title=title, fresh=fresh), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    self.technique_pair(root, title, suffix, (f"[{first}](https://example.org/a)", f"[{first}](https://other.org/b)"), fresh=fresh)
                    result = run_quality_scan_cli(root, "--fail-on-gated")
                    self.assertEqual(result.returncode, expected_code, result.stdout + result.stderr)
                    self.assertIn(f"`{category}`", result.stdout)

    def test_original_length_gate_precedes_link_removal(self) -> None:
        for title, suffix, _, _ in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                body = f"[{'c' * 110}](https://example.org/a/very/long/target)"
                self.technique_pair(root, title, suffix, (body, body), fresh=True)
                result = quality_scan.scan(root)
                self.assertEqual(len([f for f in result.findings if f.category == "duplicated-section-prose-reverified"]), 2)

    def test_nontechnical_sections_keep_link_targets(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            target = "https://example.org/" + "durable-shared-source-cursor-retry-boundary/" * 20
            self.technique_pair(root, "When to use", ".md", ("c" * 150 + f" [source]({target})", "f" * 150 + f" [source]({target})"), fresh=True)
            result = quality_scan.scan(root)
            self.assertEqual(len([f for f in result.findings if f.category == "duplicated-section-prose-reverified"]), 2)

    def test_malformed_link_inputs_are_bounded(self) -> None:
        # No fuzz framework in this repo: truncated, mismatched, repeated and invalid-byte seeds.
        for raw in ("[open](https://example.org/a", '[x]("https://example.org/a)>',
                    "[x](https://example.org/a)" * 1000, b"\xffhttps://example.org/a\xfe".decode("utf-8", "replace")):
            with self.subTest(raw=raw[:40]):
                self.assertLessEqual(len(quality_scan.technique_prose(raw)), len(raw))

    def test_fresh_identical_techniques_are_gated_in_both_languages(self) -> None:
        for suffix, title, body in (
            (".md", "Key techniques", "The event dispatcher records a durable cursor before releasing the worker. Separate leases constrain retries and each consumer validates its own acknowledgment boundary. " * 4),
            (".zh.md", "技术要点", "事件调度器先保存持久游标，再释放工作线程。独立租约约束重试，各消费端检查自己的确认边界。重启恢复依赖游标记录，不把接收成功当作所有操作已经执行。" * 4),
        ):
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                self.technique_pair(root, title, suffix, (body, body), fresh=True)
                result = quality_scan.scan(root)
                duplicates = [finding for finding in result.findings if finding.category == "duplicated-section-prose-reverified"]
                self.assertEqual(len(duplicates), 2)
                self.assertTrue(all(f"`{title}`" in finding.message for finding in duplicates))

    def technique_pair(self, root: Path, title: str, suffix: str, bodies: tuple[str, str], *, fresh: bool = False) -> list[Path]:
        pages = []
        for slug, body in zip(("first", "second"), bodies):
            page = write_page(root, f"categories/demo/{slug}{suffix}", f"## {title}\n\n{body}\n")
            if fresh:
                page.write_text(page.read_text().replace("last_verified: 2026-07-04", "last_verified: 2026-10-14"))
            pages.append(page)
        return pages

    def cases(self) -> tuple[tuple[str, str, str, str], ...]:
        return (
            ("Key techniques", ".md",
             "Astronomical catalog alignment projects stellar coordinates onto a calibrated celestial sphere. Observatory clocks anchor the exposure timestamps; orbital ephemerides compensate apparent motion before linking detections. " * 4,
             "Font shaping traverses Unicode grapheme clusters and selects glyph substitutions from typographic tables. Kerning adjusts adjacent outlines while rasterization fills pixel coverage. Ligature boundaries preserve the original cursor positions. " * 4),
            ("技术要点", ".zh.md",
             "天文观测先校准恒星坐标，再投影到球面星图。观测站时钟记录曝光时间，轨道星历补偿视运动，最后关联不同夜晚的探测结果。云层遮挡会减少可用观测，不能补出没有收到的光子。" * 4,
             "字体排版先拆分字符簇，再查字形替换表。相邻轮廓通过字距调整，栅格化计算像素覆盖，连字仍保留原始光标位置。缺少目标字体时必须回退，不能把替代字形当作原始设计。" * 4),
        )

    def test_different_techniques_are_not_reported_in_both_languages(self) -> None:
        for title, suffix, first, second in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                self.technique_pair(root, title, suffix, (first, second), fresh=True)
                result = quality_scan.scan(root)
                self.assertFalse([f for f in result.findings if f.category.startswith("duplicated-section-prose")])

    def test_old_near_duplicate_is_report_only_in_both_languages(self) -> None:
        for title, suffix, first, second in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                self.technique_pair(root, title, suffix, (first, first + second[:80]))
                result = quality_scan.scan(root)
                duplicates = [f for f in result.findings if f.category.startswith("duplicated-section-prose")]
                self.assertEqual(len(duplicates), 2)
                self.assertEqual({f.category for f in duplicates}, {"duplicated-section-prose"})

    def test_scoped_technique_scan_finds_an_unscanned_twin(self) -> None:
        for title, suffix, first, _ in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                pages = self.technique_pair(root, title, suffix, (first, first), fresh=True)
                result = quality_scan.scan(root, scope_paths=[pages[0]])
                duplicates = [f for f in result.findings if f.category == "duplicated-section-prose-reverified"]
                self.assertEqual([f.path for f in duplicates], [pages[0].relative_to(root).as_posix()])
                self.assertIn(pages[1].relative_to(root).as_posix(), duplicates[0].message)

    def test_technique_minimum_length_boundary_is_unchanged(self) -> None:
        for title, suffix, _, _ in self.cases():
            for length, count in ((119, 0), (120, 2)):
                with self.subTest(title=title, length=length), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    self.technique_pair(root, title, suffix, ("c" * length, "c" * length), fresh=True)
                    result = quality_scan.scan(root)
                    self.assertEqual(len([f for f in result.findings if f.category == "duplicated-section-prose-reverified"]), count)

    def test_real_cli_fresh_old_and_different_techniques(self) -> None:
        for title, suffix, first, second in self.cases():
            for scenario, fresh, bodies, exit_code, category in (
                ("fresh", True, (first, first), 1, "duplicated-section-prose-reverified"),
                ("old", False, (first, first), 0, "duplicated-section-prose"),
                ("different", True, (first, second), 0, None),
            ):
                with self.subTest(title=title, scenario=scenario), tempfile.TemporaryDirectory() as td:
                    root = Path(td)
                    self.technique_pair(root, title, suffix, bodies, fresh=fresh)
                    result = run_quality_scan_cli(root, "--fail-on-gated")
                    self.assertEqual(result.returncode, exit_code, result.stdout + result.stderr)
                    if category:
                        self.assertIn(f"`{category}`", result.stdout)
                        self.assertIn(f"`{title}`", result.stdout)
                    else:
                        self.assertNotIn("is 100% the same text", result.stdout)

    def test_real_cli_threshold_scale_still_clamps_at_one(self) -> None:
        import os
        for title, suffix, first, second in self.cases():
            with self.subTest(title=title), tempfile.TemporaryDirectory() as td:
                root = Path(td)
                pages = self.technique_pair(root, title, suffix, (first, first + second), fresh=True)
                normal = run_quality_scan_cli(root, "--scope", str(pages[1]), "--fail-on-gated")
                self.assertEqual(normal.returncode, 1, normal.stdout + normal.stderr)
                scaled = subprocess.run(
                    [sys.executable, str(Path(quality_scan.__file__).resolve()), "--root", str(root), "--scope", str(pages[1]), "--fail-on-gated"],
                    env=dict(os.environ, OSS_ATLAS_DUP_THRESHOLD_SCALE="20"), text=True, capture_output=True,
                )
                self.assertEqual(scaled.returncode, 0, scaled.stdout + scaled.stderr)
                self.assertNotIn(f"`duplicated-section-prose-reverified`", scaled.stdout)


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
