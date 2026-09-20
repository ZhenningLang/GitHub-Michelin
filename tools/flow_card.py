#!/usr/bin/env python3
"""Render a page's BACKBONE USER-STORY flow (the `How it works` / `怎么用起来` section).

PURE / OFFLINE. The SSOT is a structured spec, one per project, language-neutral structure
with per-step bilingual text:

  flows/<stem>.json   (stem = page slug; category-prefixed when the slug is duplicated,
                       exactly like assets/health/ cards)

  {
    "schema": 1,
    "them":  {"en": "XXL-JOB does", "zh": "XXL-JOB 做的"},
    "steps": [
      {"lane": "you",  "en": "…", "zh": "…", "code": "@XxlJob(\"demoJobHandler\")"},
      {"lane": "them", "en": "…", "zh": "…"}
    ],
    "value": {"en": "…", "zh": "…"},
    "sources": ["https://github.com/…/SampleXxlJob.java", "README#quick-start"]
  }

Two lanes only — "you" (what the developer does) and "them" (what the project does for you).
Steps are LINEAR (the backbone, no branches); a lane change is a handoff. `code` is optional and
language-neutral (a command / annotation / API that the step touches) and must be traceable to
`sources`.

Outputs (one per LANGUAGE, like health cards):
  assets/flow/<stem>.svg      English card
  assets/flow/<stem>.zh.svg   Chinese card
  plus a generated, agent-readable text list inside the page section, between
  <!-- flow-steps:begin … --> and <!-- flow-steps:end --> (images are opaque to agents).

Usage:
  python3 tools/flow_card.py categories/<cat>/<slug>.md [more pages…]   # render + sync those pages
  python3 tools/flow_card.py --all                                   # every page that has a flow
  python3 tools/flow_card.py --check-spec flows/<stem>.json          # validate one spec, no writes
"""
from __future__ import annotations

import json
import os
import re
import sys
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FLOWS = ROOT / "flows"
ASSETS = ROOT / "assets" / "flow"
ZH_SUFFIX = ".zh.md"

LANES = ("you", "them")
LANGS = ("en", "zh")
MIN_STEPS, MAX_STEPS = 3, 9
MAX_LEN = {"en": 110, "zh": 40, "code": 80, "value_en": 160, "value_zh": 60, "them_en": 40, "them_zh": 24}

SECTION = {"en": "## How it works", "zh": "## 怎么用起来"}
YOU_LABEL = {"en": "You do", "zh": "你做的"}
VALUE_LABEL = {"en": "VALUE", "zh": "价值"}
ALT = {"en": "backbone user story", "zh": "主干用户故事"}
STEPS_SUMMARY = {"en": "Text version of the flow", "zh": "流程文字版"}
YOU_WORD = {"en": "You", "zh": "你"}
BEGIN = "<!-- flow-steps:begin (generated from flows/{stem}.json by tools/flow_card.py — do not edit) -->"
END = "<!-- flow-steps:end -->"
BLOCK_RE = re.compile(r"<!-- flow-steps:begin[^\n]*-->\n.*?\n<!-- flow-steps:end -->", re.S)

# ---------------------------------------------------------------- layout constants
W = 880
PAD = 28
GAP = 40
LANE_W = (W - 2 * PAD - GAP) // 2
CARD_PX, CARD_PY = 18, 14
FS_T, FS_C = 15, 12.5
LH_T, LH_C = 22, 19
ROW_GAP = 26
FONT = {
    "zh": "'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Helvetica Neue',Arial,sans-serif",
    "en": "-apple-system,'Segoe UI','Helvetica Neue',Arial,sans-serif",
}
MONO = "'SF Mono',Menlo,Consolas,monospace"

CSS = """
.bg{fill:#ffffff}.lane{fill:#f6f8fa}.laneT{fill:#fbf7ec}
.hdr{font:600 13px %(f)s;letter-spacing:.08em}
.hY{fill:#0969da}.hT{fill:#9a6700}
.pillY{fill:#ddf4ff}.pillT{fill:#fff1c2}
.card{fill:#ffffff;stroke:#d0d7de;stroke-width:1}
.cardT{fill:#ffffff;stroke:#e3c46a;stroke-width:1}
.accY{fill:#0969da}.accT{fill:#bf8700}
.t{font:500 %(ft)spx %(f)s;fill:#1f2328}
.c{font:%(fc)spx %(m)s;fill:#57606a}
.num{font:700 11px %(m)s;fill:#ffffff}
.edge{stroke:#8c959f;stroke-width:1.5;fill:none}
.hand{stroke:#8c959f;stroke-width:1.5;fill:none;stroke-dasharray:5 4}
.ah{fill:#8c959f}
.val{fill:#dafbe1;stroke:#4ac26b;stroke-width:1}
.valK{font:700 12px %(f)s;fill:#1a7f37;letter-spacing:.08em}
.valT{font:600 15px %(f)s;fill:#1a7f37}
@media (prefers-color-scheme: dark){
.bg{fill:#0d1117}.lane{fill:#161b22}.laneT{fill:#1c1a14}
.hY{fill:#58a6ff}.hT{fill:#d4a72c}.pillY{fill:#0c2d6b}.pillT{fill:#3b2e0a}
.card{fill:#0d1117;stroke:#30363d}.cardT{fill:#0d1117;stroke:#6e5a1f}
.accY{fill:#1f6feb}.accT{fill:#9e6a03}
.t{fill:#e6edf3}.c{fill:#8b949e}
.edge,.hand{stroke:#6e7681}.ah{fill:#6e7681}
.val{fill:#0f2d1a;stroke:#2ea043}.valK,.valT{fill:#3fb950}
}
"""


# ---------------------------------------------------------------- stems / paths
def base_slug(page: Path) -> str:
    n = page.name
    return n[: -len(ZH_SUFFIX)] if n.endswith(ZH_SUFFIX) else n[: -len(".md")]


def duplicate_slugs(root: Path) -> set[str]:
    counts: dict[str, int] = {}
    for page in (root / "categories").rglob("*.md"):
        if page.name.startswith("INDEX") or page.name.endswith(ZH_SUFFIX):
            continue
        counts[page.stem] = counts.get(page.stem, 0) + 1
    return {slug for slug, count in counts.items() if count > 1}


def flow_stem(page: Path, root: Path, duplicates: set[str]) -> str:
    """Same naming rule as the health card stem (category-prefixed only for duplicated slugs)."""
    slug = base_slug(page)
    if slug not in duplicates:
        return slug
    try:
        rel_parent = page.parent.relative_to(root / "categories")
    except ValueError:
        return slug
    return f"{'-'.join(rel_parent.parts)}-{slug}"


def card_name(stem: str, lang: str) -> str:
    return stem + (".zh.svg" if lang == "zh" else ".svg")


def card_rel(page: Path, root: Path, stem: str, lang: str) -> str:
    return os.path.relpath(root / "assets" / "flow" / card_name(stem, lang), page.parent).replace(os.sep, "/")


# ---------------------------------------------------------------- spec validation
def validate_spec(spec: object) -> list[str]:
    """Return a list of human-readable problems (empty = valid)."""
    errs: list[str] = []
    if not isinstance(spec, dict):
        return ["spec must be a JSON object"]
    if spec.get("schema") != 1:
        errs.append("schema must be 1")

    def bilingual(key: str, obj: object, lim_prefix: str | None) -> None:
        if not isinstance(obj, dict):
            errs.append(f"{key} must be an object with 'en' and 'zh'")
            return
        for lang in LANGS:
            v = obj.get(lang)
            if not isinstance(v, str) or not v.strip():
                errs.append(f"{key}.{lang} must be a non-empty string")
            elif lim_prefix and len(v) > MAX_LEN[f"{lim_prefix}_{lang}"]:
                errs.append(f"{key}.{lang} is {len(v)} chars (> {MAX_LEN[f'{lim_prefix}_{lang}']})")

    bilingual("them", spec.get("them"), "them")
    bilingual("value", spec.get("value"), "value")

    steps = spec.get("steps")
    if not isinstance(steps, list):
        errs.append("steps must be a list")
        steps = []
    elif not MIN_STEPS <= len(steps) <= MAX_STEPS:
        errs.append(f"steps must have {MIN_STEPS}–{MAX_STEPS} items (backbone only), found {len(steps)}")
    lanes_seen = set()
    for i, st in enumerate(steps, 1):
        if not isinstance(st, dict):
            errs.append(f"steps[{i}] must be an object")
            continue
        extra = set(st) - {"lane", "en", "zh", "code"}
        if extra:
            errs.append(f"steps[{i}] has unknown key(s): {sorted(extra)}")
        lane = st.get("lane")
        if lane not in LANES:
            errs.append(f"steps[{i}].lane must be 'you' or 'them'")
        else:
            lanes_seen.add(lane)
        for lang in LANGS:
            v = st.get(lang)
            if not isinstance(v, str) or not v.strip():
                errs.append(f"steps[{i}].{lang} must be a non-empty string")
            elif len(v) > MAX_LEN[lang]:
                errs.append(f"steps[{i}].{lang} is {len(v)} chars (> {MAX_LEN[lang]}); one short sentence per step")
        code = st.get("code")
        if code is not None and (not isinstance(code, str) or not code.strip()):
            errs.append(f"steps[{i}].code must be a non-empty string when present")
        elif isinstance(code, str) and len(code) > MAX_LEN["code"]:
            errs.append(f"steps[{i}].code is {len(code)} chars (> {MAX_LEN['code']})")
    if steps and lanes_seen != set(LANES):
        errs.append("steps must use both lanes ('you' and 'them') — the flow shows the handoff")

    sources = spec.get("sources")
    if not isinstance(sources, list) or not sources or not all(isinstance(s, str) and s.strip() for s in sources):
        errs.append("sources must be a non-empty list of strings (where each command/API was verified)")
    extra_top = set(spec) - {"schema", "them", "steps", "value", "sources"}
    if extra_top:
        errs.append(f"unknown top-level key(s): {sorted(extra_top)}")
    return errs


def load_spec(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- text layout
def text_w(s: str, fs: float, mono: bool = False) -> float:
    return sum(fs if ord(ch) > 0x2E80 else fs * (0.62 if mono else 0.56) for ch in s)


def wrap(s: str, fs: float, maxw: float, mono: bool = False) -> list[str]:
    lines, cur = [], ""
    for ch in s:
        if text_w(cur + ch, fs, mono) > maxw and cur:
            # avoid breaking inside an ASCII word when possible
            if ch.isascii() and ch != " " and " " in cur:
                head, tail = cur.rsplit(" ", 1)
                lines.append(head)
                cur = tail + ch
                continue
            lines.append(cur)
            cur = "" if ch == " " else ch
        else:
            cur += ch
    if cur:
        lines.append(cur)
    # CJK line-breaking: a line may not START with a closing/trailing punctuation mark — push the
    # preceding character down with it (禁则处理).
    hanging = "、，。；：！？）」』》〉”’%"
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in hanging and len(lines[i - 1]) > 1:
            lines[i] = lines[i - 1][-1] + lines[i]
            lines[i - 1] = lines[i - 1][:-1]
    # no orphan: a last line of 1–2 CJK chars pulls a few chars down from the line above
    if len(lines) > 1 and len(lines[-1]) <= 2 and not lines[-1].isascii():
        lines[-2], lines[-1] = lines[-2][:-3], lines[-2][-3:] + lines[-1]
    return lines


# ---------------------------------------------------------------- SVG
def render(spec: dict, lang: str) -> str:
    font = FONT[lang]
    css = CSS % {"f": font, "m": MONO, "ft": FS_T, "fc": FS_C}
    inner = LANE_W - 2 * CARD_PX - 30
    lane_x = {"you": PAD, "them": PAD + LANE_W + GAP}
    out: list[str] = []
    cards = []
    top = PAD + 44
    bottom = {"you": top - ROW_GAP, "them": top - ROW_GAP}   # last card bottom per lane
    prev = None
    for i, st in enumerate(spec["steps"], 1):
        tl = wrap(st[lang], FS_T, inner)
        cl = wrap(st["code"], FS_C, inner, mono=True) if st.get("code") else []
        h = CARD_PY * 2 + len(tl) * LH_T + (len(cl) * LH_C + 4 if cl else 0)
        lane = st["lane"]
        if prev is None:
            y0 = top
        elif prev[0] == lane:
            y0 = prev[1] + prev[2] + ROW_GAP
        else:
            # handoff: stagger half a card below the previous step instead of a full row
            y0 = max(bottom[lane] + ROW_GAP, prev[1] + max(prev[2] // 2, 36))
        cards.append((i, st, tl, cl, lane_x[lane], y0, h))
        bottom[lane] = y0 + h
        prev = (lane, y0, h)
    vl = wrap(spec["value"][lang], 15, W - 2 * PAD - 40)
    val_y = max(bottom.values()) + ROW_GAP + 6
    val_h = 44 + len(vl) * 22
    H = val_y + val_h + PAD

    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">')
    out.append(f"<style>{css}</style>")
    out.append('<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
               'orient="auto-start-reverse"><path class="ah" d="M0,0 L10,5 L0,10 z"/></marker></defs>')
    out.append(f'<rect class="bg" width="{W}" height="{H}" rx="12"/>')
    lane_bottom = val_y - 14
    labels = {"you": YOU_LABEL[lang], "them": spec["them"][lang]}
    for key, cls, pill, hcls in (("you", "lane", "pillY", "hY"), ("them", "laneT", "pillT", "hT")):
        x = lane_x[key]
        out.append(f'<rect class="{cls}" x="{x}" y="{PAD}" width="{LANE_W}" height="{lane_bottom - PAD}" rx="10"/>')
        label = labels[key]
        pw = min(text_w(label, 13) * 1.12 + len(label) * 13 * 0.08 + 28, LANE_W - 28)
        out.append(f'<rect class="{pill}" x="{x + 14}" y="{PAD + 12}" width="{pw:.1f}" height="24" rx="12"/>')
        out.append(f'<text class="hdr {hcls}" x="{x + 28}" y="{PAD + 29}">{escape(label)}</text>')

    # edges first (under the cards)
    for (_, st, _tl, _cl, x, y0, h), (_, st2, _tl2, _cl2, x2, y2, _h2) in zip(cards, cards[1:]):
        if st["lane"] == st2["lane"]:
            cx = x + 34
            out.append(f'<path class="edge" d="M{cx},{y0 + h} L{cx},{y2 - 2}" marker-end="url(#a)"/>')
        else:
            right = x2 > x
            sx = x + LANE_W - 12 if right else x + 12
            ex = (x2 + 10) if right else (x2 + LANE_W - 10)
            sy, ey = y0 + h / 2, y2 + CARD_PY + 10
            mx = (sx + ex) / 2
            out.append(f'<path class="hand" d="M{sx},{sy} C{mx},{sy} {mx},{ey} {ex},{ey}" marker-end="url(#a)"/>')

    for i, st, tl, cl, x, y0, h in cards:
        them = st["lane"] == "them"
        cx0, cw = x + 12, LANE_W - 24
        acc = "accT" if them else "accY"
        out.append(f'<rect class="{"cardT" if them else "card"}" x="{cx0}" y="{y0}" width="{cw}" height="{h}" rx="8"/>')
        out.append(f'<rect class="{acc}" x="{cx0}" y="{y0}" width="4" height="{h}" rx="2"/>')
        out.append(f'<circle class="{acc}" cx="{cx0 + 22}" cy="{y0 + CARD_PY + 10}" r="10"/>')
        out.append(f'<text class="num" x="{cx0 + 22}" y="{y0 + CARD_PY + 14}" text-anchor="middle">{i}</text>')
        tx, ty = cx0 + 42, y0 + CARD_PY + 15
        for ln in tl:
            out.append(f'<text class="t" x="{tx}" y="{ty}">{escape(ln)}</text>')
            ty += LH_T
        ty += 2
        for ln in cl:
            out.append(f'<text class="c" x="{tx}" y="{ty}">{escape(ln)}</text>')
            ty += LH_C

    out.append(f'<rect class="val" x="{PAD}" y="{val_y}" width="{W - 2 * PAD}" height="{val_h}" rx="10"/>')
    out.append(f'<text class="valK" x="{PAD + 20}" y="{val_y + 24}">{escape(VALUE_LABEL[lang])}</text>')
    vy = val_y + 48
    for ln in vl:
        out.append(f'<text class="valT" x="{PAD + 20}" y="{vy}">{escape(ln)}</text>')
        vy += 22
    out.append("</svg>")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- page text block
def steps_block(spec: dict, lang: str, stem: str, name: str) -> str:
    """The agent-readable text twin of the SVG (collapsed on GitHub, plain text in the source).

    `name` is the page's frontmatter display name — the actor of the "them" lane.
    """
    sep = "：" if lang == "zh" else ": "
    lines = [BEGIN.format(stem=stem), "<details>", f"<summary>{STEPS_SUMMARY[lang]}</summary>", ""]
    for i, st in enumerate(spec["steps"], 1):
        who = YOU_WORD[lang] if st["lane"] == "you" else name
        code = f" — `{st['code']}`" if st.get("code") else ""
        lines.append(f"{i}. **{who}**{sep}{st[lang]}{code}")
    lines += ["", f"**{VALUE_LABEL[lang] if lang == 'zh' else 'Value'}**{sep}{spec['value'][lang]}", "", "</details>", END]
    return "\n".join(lines)


def section_bounds(text: str, lang: str) -> tuple[int, int] | None:
    """(start, end) character span of the How-it-works section body, or None."""
    m = re.search(r"(?m)^" + re.escape(SECTION[lang]) + r"\s*$", text)
    if not m:
        return None
    nxt = re.search(r"(?m)^##[ \t]+\S", text[m.end():])
    end = m.end() + nxt.start() if nxt else len(text)
    return m.end(), end


def page_name(text: str, fallback: str) -> str:
    m = re.search(r"(?m)^name:[ \t]*(.+?)[ \t]*$", text.split("\n---", 1)[0])
    return m.group(1).strip("\"'") if m else fallback


def sync_page(page: Path, root: Path, spec: dict, stem: str) -> bool:
    """Rewrite the generated steps block inside an existing section. Returns True if changed.

    Only touches pages that already have the section and the begin/end markers or an embedded card;
    authoring the mechanism paragraph is the writer's job, not this tool's.
    """
    lang = "zh" if page.name.endswith(ZH_SUFFIX) else "en"
    text = page.read_text(encoding="utf-8")
    span = section_bounds(text, lang)
    if span is None:
        return False
    s, e = span
    body = text[s:e]
    block = steps_block(spec, lang, stem, page_name(text, stem))
    if BLOCK_RE.search(body):
        new_body = BLOCK_RE.sub(lambda _m: block, body, count=1)
    else:
        img = card_rel(page, root, stem, lang)
        i = body.find(img)
        if i == -1:
            return False
        line_end = body.find("\n", i)
        line_end = len(body) if line_end == -1 else line_end
        new_body = body[:line_end] + "\n\n" + block + body[line_end:]
    if new_body == body:
        return False
    page.write_text(text[:s] + new_body + text[e:], encoding="utf-8")
    return True


# ---------------------------------------------------------------- CLI
def process_page(page: Path, root: Path, duplicates: set[str]) -> list[str]:
    stem = flow_stem(page, root, duplicates)
    spec_path = root / "flows" / f"{stem}.json"
    if not spec_path.exists():
        return []
    spec = load_spec(spec_path)
    problems = validate_spec(spec)
    if problems:
        raise SystemExit(f"{spec_path.relative_to(root)}: invalid spec:\n  - " + "\n  - ".join(problems))
    lang = "zh" if page.name.endswith(ZH_SUFFIX) else "en"
    out = root / "assets" / "flow" / card_name(stem, lang)
    out.parent.mkdir(parents=True, exist_ok=True)
    svg = render(spec, lang)
    done = []
    if not out.exists() or out.read_text(encoding="utf-8") != svg:
        out.write_text(svg, encoding="utf-8")
        done.append(f"wrote {out.relative_to(root)}")
    if sync_page(page, root, spec, stem):
        done.append(f"synced {page.relative_to(root)}")
    return done


def main(argv: list[str]) -> int:
    if not argv:
        sys.stderr.write(__doc__ or "")
        return 2
    if argv[0] == "--check-spec":
        rc = 0
        for a in argv[1:]:
            problems = validate_spec(load_spec(Path(a)))
            for p in problems:
                print(f"{a}: {p}")
            rc |= bool(problems)
        return rc
    if argv[0] == "--all":
        pages = sorted(p for p in (ROOT / "categories").rglob("*.md") if not p.name.startswith("INDEX"))
    else:
        pages = [Path(a) if Path(a).is_absolute() else ROOT / a for a in argv]
        # a page arg implies its bilingual sibling
        sib = []
        for p in pages:
            s = p.with_name(base_slug(p) + (".md" if p.name.endswith(ZH_SUFFIX) else ZH_SUFFIX))
            if s.exists() and s not in pages:
                sib.append(s)
        pages += sib
    duplicates = duplicate_slugs(ROOT)
    n = 0
    for page in pages:
        if not page.exists() or page.name.startswith("INDEX"):
            continue
        for line in process_page(page, ROOT, duplicates):
            print(line)
            n += 1
    print(f"{n} flow artifact(s) updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
