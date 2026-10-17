#!/usr/bin/env python3
"""Bilingual mechanism JSON → local d2 SVGs and generated page text.

Usage: python3 tools/mechanism_card.py <page>… | --all | --check-spec <json>…
Rendering requires local d2; validation and text/hash checks are pure Python.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

import flow_card
from flow_card import card_name

ROOT = Path(__file__).resolve().parent.parent
RENDER_VERSION = "2"
LANGS = ("en", "zh")
SECTION = {"en": "## Key techniques", "zh": "## 技术要点"}
BEGIN = "<!-- mechanism:begin (generated from mechanisms/{stem}.json by tools/mechanism_card.py; do not edit) -->"
END = "<!-- mechanism:end -->"
# Root, complete blocks only; a truncated opener must not swallow subsequent prose.
BLOCK_RE = re.compile(r"^<!-- mechanism:begin[^\r\n]*-->\n(?:(?!^<!-- mechanism:begin|^##).)*?^<!-- mechanism:end -->$", re.M | re.S)


def validate_spec(spec: object, technique_count: int | None = None) -> list[str]:
    """Validate graph shape, optionally cross-checking the page's actual technique count."""
    if not isinstance(spec, dict):
        return ["spec must be a JSON object"]
    errors = []
    if type(spec.get("schema")) is not int or spec["schema"] != 1:
        errors.append("schema must be 1")
    if spec.get("direction") not in ("right", "down"):
        errors.append("direction must be right or down")

    def bilingual(obj: dict, where: str) -> None:
        for lang in LANGS:
            if not isinstance(obj.get(lang), str) or not obj[lang].strip():
                errors.append(f"{where}.{lang} must be a non-empty string")

    nodes = spec.get("nodes")
    if not isinstance(nodes, list):
        errors.append("nodes must be a list")
        nodes = []
    if not 3 <= len(nodes) <= 12:
        errors.append("nodes must have 3–12 items")
    ids = set()
    covered = set()
    for i, node in enumerate(nodes, 1):
        where = f"nodes[{i}]"
        if not isinstance(node, dict):
            errors.append(f"{where} must be an object")
            continue
        ident = node.get("id")
        if not isinstance(ident, str) or not ident.strip():
            errors.append(f"{where}.id must be a non-empty string")
        elif ident in ids:
            errors.append(f"{where}.id must be unique: {ident}")
        else:
            ids.add(ident)
        bilingual(node, where)
        if node.get("kind", "step") not in ("input", "step", "output", "external"):
            errors.append(f"{where}.kind must be input, step, output or external")
        numbers = node.get("technique", [])
        if not isinstance(numbers, list) or any(type(n) is not int or n < 1 for n in numbers):
            errors.append(f"{where}.technique must be a list of positive integers")
        else:
            covered.update(numbers)
            if technique_count is not None and any(n > technique_count for n in numbers):
                errors.append(f"{where}.technique outside page range 1..{technique_count}")
    if technique_count is not None:
        for n in range(1, technique_count + 1):
            if n not in covered:
                errors.append(f"technique {n} has no node")
    edges = spec.get("edges")
    if not isinstance(edges, list):
        errors.append("edges must be a list")
        edges = []
    for i, edge in enumerate(edges, 1):
        where = f"edges[{i}]"
        if not isinstance(edge, dict):
            errors.append(f"{where} must be an object")
            continue
        for endpoint in ("from", "to"):
            if not isinstance(edge.get(endpoint), str) or edge[endpoint] not in ids:
                errors.append(f"{where}.{endpoint} endpoint must name an existing node")
        if "en" in edge or "zh" in edge:
            bilingual(edge, where)
        if "style" in edge and edge["style"] != "dashed":
            errors.append(f"{where}.style must be dashed when present")
    sources = spec.get("sources", [])
    if not isinstance(sources, list) or any(not isinstance(s, str) or not s.strip() for s in sources):
        errors.append("sources, when present, must be a list of non-empty strings")
    return errors


def load_spec(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        raise ValueError(f"{path}: unreadable mechanism spec: {exc}") from exc


def node_label(node: dict, lang: str) -> str:
    return node[lang] + "".join(chr(0x2460 + n - 1) if n <= 20 else f"[{n}]" for n in node.get("technique", []))


def text_block(spec: dict, lang: str, stem: str) -> str:
    def inline(value: str) -> str:
        return escape(re.sub(r"[\r\n]+", " ", value), quote=False)

    labels = {node["id"]: inline(node_label(node, lang)) for node in spec["nodes"]}
    summary = "机制文字版" if lang == "zh" else "Text version of the mechanism"
    lines = [BEGIN.format(stem=stem), "<details>", f"<summary>{summary}</summary>", ""]
    lines += [f"- {labels[node['id']]}" for node in spec["nodes"]]
    lines.append("")
    for edge in spec["edges"]:
        label = (f"（{inline(edge[lang])}）" if lang == "zh" else f" ({inline(edge[lang])})") if lang in edge else ""
        dashed = ("〔可选／兜底〕" if lang == "zh" else " [optional/fallback]") if edge.get("style") == "dashed" else ""
        lines.append(f"- {labels[edge['from']]} → {labels[edge['to']]}{label}{dashed}")
    return "\n".join(lines + ["", "</details>", END])


def spec_hash(spec: dict) -> str:
    canonical = json.dumps(spec, sort_keys=True, ensure_ascii=False) + RENDER_VERSION
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def svg_stamp(svg: str) -> str | None:
    stamps = re.findall(r"<!-- mechanism-src sha256=([0-9a-f]{64}) -->", svg)
    return stamps[0] if len(stamps) == 1 else None


def section_bounds(text: str, lang: str) -> tuple[int, int] | None:
    chapters = flow_card.scan_h2_sections(text)
    if chapters.errors:
        return None
    section = next((h for h in chapters if h.exact and h.heading == SECTION[lang]), None)
    return (section.body_start, section.end) if section else None


def scan_body(body: str) -> tuple[list[tuple[int, int, str]], list[re.Match[str]]]:
    """Visible root lines + generated blocks, never examples inside literal blocks.

    Offsets stay in the original source. Each physical line is visited once; a malformed
    mechanism opener cannot consume a later H2 or another mechanism opener.
    """
    visible = []
    blocks = []
    literal = None
    skip_before = 0
    for match in flow_card.PHYSICAL_LINE_RE.finditer(body):
        if match.start() < skip_before:
            continue
        line = match[0].rstrip("\r\n")
        if literal:
            if flow_card.literal_closed(literal, line):
                literal = None
            continue
        if line.startswith("<!-- mechanism:begin"):
            block = BLOCK_RE.match(body, match.start())
            if block:
                blocks.append(block)
                skip_before = block.end()
                continue
        opening = flow_card.FENCE_OPEN_RE.fullmatch(line)
        html = flow_card.HTML_LITERAL_RE.match(line)
        if opening:
            literal = flow_card.LiteralBlock("fence", opening[1][0], len(opening[1]), 0)
        elif line.startswith("<!--") or html:
            block = (flow_card.LiteralBlock("html", html[1].lower(), 0, 0) if html else
                     flow_card.LiteralBlock("comment", "-->", 0, 0))
            literal = None if flow_card.literal_closed(block, line) else block
        else:
            visible.append((match.start(), match.end(), line))
    return visible, blocks


def technique_headings(body: str) -> list[tuple[int, int, str]]:
    visible, _ = scan_body(body)
    return [item for item in visible if re.match(r"^###(?:[ \t]|$)", item[2])]


def card_rel(page: Path, root: Path, stem: str, lang: str) -> str:
    return os.path.relpath(root / "assets/mechanism" / card_name(stem, lang), page.parent).replace(os.sep, "/")


def d2_source(spec: dict, lang: str) -> str:
    # JSON quoting handles newlines/quotes/backslashes; d2 additionally interpolates $.
    # Escape dollars AFTER JSON encoding so existing backslashes keep their meaning.
    # Use generated identifiers, never author-supplied ids as executable d2 syntax.
    quote = lambda value: json.dumps(value, ensure_ascii=False).replace("$", r"\$")
    ids = {node["id"]: f"n{i}" for i, node in enumerate(spec["nodes"])}
    shapes = {"input": "parallelogram", "step": "rectangle", "output": "document", "external": "cloud"}
    lines = [f"direction: {spec['direction']}"]
    for node in spec["nodes"]:
        lines += [f"{ids[node['id']]}: {quote(node_label(node, lang))} {{",
                  f"  shape: {shapes[node.get('kind', 'step')]}", "}"]
    for edge in spec["edges"]:
        line = f"{ids[edge['from']]} -> {ids[edge['to']]}"
        if lang in edge:
            line += f": {quote(edge[lang])}"
        if edge.get("style") == "dashed":
            line += " {style.stroke-dash: 5}"
        lines.append(line)
    return "\n".join(lines) + "\n"


def render(spec: dict, lang: str, d2: str) -> str:
    result = subprocess.run([d2, "--layout", "elk", "-", "-"], input=d2_source(spec, lang),
                            text=True, capture_output=True, check=False)
    if result.returncode:
        raise ValueError(f"d2 lang={lang} exit={result.returncode}: {result.stderr.strip()}")
    svg = result.stdout
    try:
        element = ET.fromstring(svg)
    except ET.ParseError as exc:
        raise ValueError(f"d2 lang={lang} returned invalid SVG: {exc}") from exc
    if element.tag.rsplit("}", 1)[-1] != "svg":
        raise ValueError(f"d2 lang={lang} returned a non-SVG document")
    if lang == "zh":
        # Last stylesheet + !important overrides d2's Latin-only embedded font classes.
        css = "<style>text,tspan{font-family:'PingFang SC','Hiragino Sans GB','Noto Sans CJK SC','Microsoft YaHei',sans-serif!important}</style>"
        closing = svg.rfind("</svg>")
        if closing == -1:
            # A valid empty self-closing SVG still needs a stylesheet for the declared contract.
            svg = svg.rstrip().removesuffix("/>") + ">" + css + "</svg>"
        else:
            svg = svg[:closing] + css + svg[closing:]
    stamp = f"<!-- mechanism-src sha256={spec_hash(spec)} -->\n"
    if svg.startswith("<?xml"):
        end = svg.index("?>") + 2
        return svg[:end] + "\n" + stamp + svg[end:].lstrip("\n")
    return stamp + svg


def updated_page(page: Path, root: Path, spec: dict, stem: str, lang: str) -> str:
    text = page.read_text(encoding="utf-8")
    span = section_bounds(text, lang)
    if span is None:
        raise ValueError(f"{page}: missing or malformed {SECTION[lang]}")
    start, end = span
    body = text[start:end]
    count = len(technique_headings(body))
    problems = validate_spec(spec, count)
    if problems:
        raise ValueError(f"{page}: " + "; ".join(problems))
    _, blocks = scan_body(body)
    if len(blocks) > 1 or body.count("<!-- mechanism:begin") != len(blocks) or body.count(END) != len(blocks):
        raise ValueError(f"{page}: malformed/duplicate mechanism block; repair markers before rendering")
    block = text_block(spec, lang, stem)
    body = BLOCK_RE.sub(lambda _m: block, body)
    ref = card_rel(page, root, stem, lang)
    alt = "机制图" if lang == "zh" else "mechanism diagram"
    image = f"![{flow_card.page_name(text, stem)} — {alt}]({ref})"
    img_re = re.compile(r"!\[[^\r\n]*\]\(" + re.escape(ref) + r"\)[ \t]*")
    visible, _ = scan_body(body)
    existing = next((line for line in visible if img_re.fullmatch(line[2])), None)
    if existing:
        start_image = existing[0]
        # Keep the existing physical newline outside the replacement.
        line_end = start_image + len(existing[2])
        body = body[:start_image] + image + body[line_end:]
    if not blocks:
        if existing:
            at = existing[0] + len(image)
            body = body[:at] + "\n\n" + block + body[at:]
        else:
            body = "\n" + image + "\n\n" + block + "\n\n" + body.lstrip("\n")
    elif not existing:
        body = "\n" + image + "\n\n" + body.lstrip("\n")
    return text[:start] + body + text[end:]


def main(argv: list[str]) -> int:
    if not argv or (argv[0] in ("--check-spec",) and len(argv) == 1):
        print(__doc__, file=sys.stderr)
        return 2
    try:
        if argv[0] == "--check-spec":
            rc = 0
            for arg in argv[1:]:
                problems = validate_spec(load_spec(Path(arg)))
                for problem in problems:
                    print(f"{arg}: {problem}", file=sys.stderr)
                rc |= bool(problems)
            return int(rc)
        duplicates = flow_card.duplicate_slugs(ROOT)
        if argv == ["--all"]:
            pages = sorted(p for p in (ROOT / "categories").rglob("*.md")
                           if not p.name.startswith("INDEX") and not p.name.endswith(flow_card.ZH_SUFFIX))
        else:
            pages = [Path(a) if Path(a).is_absolute() else ROOT / a for a in argv]
        canonical = sorted({p.with_name(flow_card.base_slug(p) + ".md") for p in pages})
        jobs = []
        for page in canonical:
            stem = flow_card.flow_stem(page, ROOT, duplicates)
            source = ROOT / "mechanisms" / f"{stem}.json"
            if not source.exists() and argv == ["--all"]:
                continue
            spec = load_spec(source)
            problems = validate_spec(spec)
            if problems:
                raise ValueError(f"{source}: " + "; ".join(problems))
            targets = [(page if lang == "en" else page.with_name(flow_card.base_slug(page) + ".zh.md"), lang) for lang in LANGS]
            page_results = [(p, updated_page(p, ROOT, spec, stem, lang)) for p, lang in targets]
            jobs.append((source, stem, spec, page_results))
        if jobs:
            d2 = shutil.which("d2")
            if not d2:
                print("d2 not found; install locally with: brew install d2 (no files written)", file=sys.stderr)
                return 2
        changed = 0
        for source, stem, spec, page_results in jobs:
            try:
                results = [(ROOT / "assets/mechanism" / card_name(stem, lang), render(spec, lang, d2)) for lang in LANGS]
            except (ValueError, OSError) as exc:
                raise ValueError(f"{source}: {exc}") from exc
            # Both languages and both page rewrites are ready before publishing this pair.
            for target, content in results + page_results:
                if not target.exists() or target.read_text(encoding="utf-8") != content:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(content, encoding="utf-8")
                    print(f"wrote {target.relative_to(ROOT)}")
                    changed += 1
        print(f"{changed} mechanism artifact(s) updated")
        return 0
    except (ValueError, OSError) as exc:
        print(f"mechanism_card: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
