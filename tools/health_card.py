#!/usr/bin/env python3
"""Generate a JoJo Stand-stats HEALTH radar card (SVG) from a page's `health:` block.

PURE / OFFLINE: reads the SSOT `health:` block already present in a page's YAML
frontmatter and renders an SVG. Never hits the network (scoring lives in
tools/health.py). Safe to run in a pre-commit hook.

One card per LANGUAGE (no mixed scripts on a card):
  <slug>.md     -> assets/health/<slug>.svg     (English)
  <slug>.zh.md  -> assets/health/<slug>.zh.svg  (Chinese)
If the same slug appears in multiple categories, the category path is prefixed:
  categories/<cat>/<slug>.md -> assets/health/<cat>-<slug>.svg

Usage:
  python3 tools/health_card.py categories/<cat>/<slug>.md [more pages...]
  python3 tools/health_card.py --all          # every page (both languages) with a health: block
"""
from __future__ import annotations
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets" / "health"

# grade -> (radius fraction, color)
TIER = {
    "A": (1.00, "#F2C200"),  # gold
    "B": (0.80, "#3FB950"),  # green
    "C": (0.60, "#D4C20A"),  # yellow
    "D": (0.40, "#E8702A"),  # orange
    "E": (0.20, "#E5484D"),  # red
    "?": (0.50, "#8B949E"),  # gray, dashed (measured failed — excluded from area)
    "N/A": (0.50, "#4B5563"), # dim gray, solid (axis does not apply — excluded from area)
}
# Unscored states share a radius but must never share a treatment: a dashed ghost says
# "we could not measure this, go look"; a flat dim spoke says "this axis asks a question
# this artifact type cannot answer". Rendering both as the same gray hid which one a
# reader was looking at.
UNSCORED = ("?", "N/A")
AXIS_KEYS = ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]

# Per-language axis labels = the real axis meaning (order = top, then clockwise).
# JoJo is the *visual* influence only — no Stand-stat vocabulary in the text.
LANG = {
    "en": {
        "axes": ["Maintenance", "Responsiveness", "Adoption", "Longevity", "Bus Factor", "Permissiveness"],
        "tag": "HEALTH RADAR",
        "overall": "OVERALL",
        "axes_scored": "AXES",
        "archived": "ARCHIVED",
        "ext": ".svg",
        "label_font": "'Arial Black','Helvetica Neue',Arial,sans-serif",
        "axis_fs": 12,
    },
    "zh": {
        "axes": ["维护活跃度", "响应速度", "采用广度", "长青度", "维护者分散度", "许可宽松度"],
        "tag": "健康度雷达",
        "overall": "总评",
        "axes_scored": "已评分",
        "archived": "已归档",
        "ext": ".zh.svg",
        "label_font": "'PingFang SC','Hiragino Sans GB','Heiti SC','Microsoft YaHei',sans-serif",
        "axis_fs": 16,
    },
}
DISP = "'Georgia','Times New Roman',serif"          # dramatic serif for name + overall
LOUD = "'Arial Black','Helvetica Neue',Arial,sans-serif"

W, H = 820, 500
CX, CY, R = 260, 268, 115
GOLD = "#E8C45A"
GOLD_DK = "#9c7d2a"
PARCH = "#f3e7c8"


def _v(i: int, frac: float) -> tuple[float, float]:
    a = math.radians(-90 + 60 * i)
    return CX + R * frac * math.cos(a), CY + R * frac * math.sin(a)


def _esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def base_slug(page: Path) -> str:
    return page.name[: -len(".zh.md")] if page.name.endswith(".zh.md") else page.stem


def duplicate_slugs(root: Path) -> set[str]:
    counts: dict[str, int] = {}
    for page in (root / "categories").rglob("*.md"):
        if page.name.startswith("INDEX") or page.name.endswith(".zh.md"):
            continue
        counts[page.stem] = counts.get(page.stem, 0) + 1
    return {slug for slug, count in counts.items() if count > 1}


def card_stem_for_page(page: Path, duplicates: set[str]) -> str:
    slug = base_slug(page)
    if slug not in duplicates:
        return slug
    try:
        rel_parent = page.parent.relative_to(ROOT / "categories")
    except ValueError:
        return slug
    return f"{'-'.join(rel_parent.parts)}-{slug}"


# ---------------------------------------------------------------- frontmatter
def parse_frontmatter(text: str) -> dict:
    """Minimal indent-based YAML subset parser (mappings + scalars)."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]
    for line in text[3:end].strip("\n").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, val = line.strip().partition(":")
        key, val = key.strip(), val.strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if val == "":
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = val.strip().strip('"').strip("'")
    return root


# ---------------------------------------------------------------- renderer
def render(lang: str, name: str, grades: list[str], overall: str, note: str, flags: list[str],
           scored_axes: str, applicable_axes: str | None = None) -> str:
    cfg = LANG[lang]
    oc = TIER.get(overall, TIER["?"])[1]
    lf = cfg["label_font"]
    s: list[str] = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')

    # ---- defs ----
    s.append("<defs>")
    s.append('<radialGradient id="bg" cx="30%" cy="34%" r="90%">'
             '<stop offset="0%" stop-color="#2a2010"/><stop offset="48%" stop-color="#181206"/>'
             '<stop offset="100%" stop-color="#05030a"/></radialGradient>')
    s.append('<radialGradient id="vig" cx="50%" cy="50%" r="72%">'
             '<stop offset="62%" stop-color="#000000" stop-opacity="0"/>'
             '<stop offset="100%" stop-color="#000000" stop-opacity="0.72"/></radialGradient>')
    s.append(f'<linearGradient id="frame" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0%" stop-color="#f6dd92"/><stop offset="45%" stop-color="{GOLD}"/>'
             f'<stop offset="55%" stop-color="{GOLD_DK}"/><stop offset="100%" stop-color="#f6dd92"/></linearGradient>')
    s.append(f'<linearGradient id="poly" x1="0" y1="0" x2="0.7" y2="1">'
             f'<stop offset="0%" stop-color="{oc}" stop-opacity="0.92"/>'
             f'<stop offset="100%" stop-color="{oc}" stop-opacity="0.34"/></linearGradient>')
    s.append(f'<radialGradient id="halo" cx="50%" cy="50%" r="50%">'
             f'<stop offset="0%" stop-color="{oc}" stop-opacity="0.34"/>'
             f'<stop offset="68%" stop-color="{oc}" stop-opacity="0.04"/>'
             f'<stop offset="100%" stop-color="{oc}" stop-opacity="0"/></radialGradient>')
    s.append('<filter id="glow" x="-60%" y="-60%" width="220%" height="220%">'
             '<feGaussianBlur stdDeviation="5" result="b"/><feMerge>'
             '<feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    s.append('<filter id="soft" x="-30%" y="-30%" width="160%" height="160%">'
             '<feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity="0.7"/></filter>')
    s.append('<pattern id="halftone" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(18)">'
             f'<circle cx="2" cy="2" r="1" fill="{GOLD}" fill-opacity="0.06"/></pattern>')
    s.append("</defs>")

    # ---- background plates ----
    s.append(f'<rect width="{W}" height="{H}" rx="17" fill="url(#bg)"/>')
    s.append(f'<rect width="{W}" height="{H}" rx="17" fill="url(#halftone)"/>')

    # ---- aura sunburst behind the hexagon (JoJo menace) ----
    s.append(f'<g opacity="0.5" filter="url(#glow)">')
    for k in range(12):
        a0 = math.radians(k * 30 - 8)
        a1 = math.radians(k * 30 + 8)
        rr = 235
        x0, y0 = CX + rr * math.cos(a0), CY + rr * math.sin(a0)
        x1, y1 = CX + rr * math.cos(a1), CY + rr * math.sin(a1)
        col = GOLD if k % 2 == 0 else oc
        s.append(f'<path d="M{CX},{CY} L{x0:.0f},{y0:.0f} L{x1:.0f},{y1:.0f} Z" fill="{col}" fill-opacity="0.10"/>')
    s.append("</g>")
    s.append(f'<circle cx="{CX}" cy="{CY}" r="{R+46}" fill="url(#halo)"/>')

    # ---- ornate double frame + corner ticks ----
    s.append(f'<rect x="6" y="6" width="{W-12}" height="{H-12}" rx="14" fill="none" stroke="url(#frame)" stroke-width="3.5"/>')
    s.append(f'<rect x="13" y="13" width="{W-26}" height="{H-26}" rx="9" fill="none" stroke="{GOLD_DK}" stroke-width="1" stroke-opacity="0.8"/>')
    for cx0, cy0, sx, sy in [(6, 6, 1, 1), (W - 6, 6, -1, 1), (6, H - 6, 1, -1), (W - 6, H - 6, -1, -1)]:
        s.append(f'<path d="M{cx0+sx*8},{cy0+sy*22} L{cx0+sx*8},{cy0+sy*8} L{cx0+sx*22},{cy0+sy*8}" '
                 f'fill="none" stroke="{GOLD}" stroke-width="2.4"/>')
    s.append(f'<rect width="{W}" height="{H}" rx="17" fill="url(#vig)"/>')

    # ---- hexagon rings + spokes + A..E ladder ----
    for frac in (1.0, 0.8, 0.6, 0.4, 0.2):
        pts = " ".join(f"{_v(i, frac)[0]:.1f},{_v(i, frac)[1]:.1f}" for i in range(6))
        s.append(f'<polygon points="{pts}" fill="none" stroke="{GOLD_DK}" stroke-opacity="0.55" stroke-width="1"/>')
    for i in range(6):
        x, y = _v(i, 1.0)
        s.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="{GOLD_DK}" stroke-opacity="0.5" stroke-width="1"/>')
    for j, g in enumerate("ABCDE"):
        ly = CY - R * (1.0 - j * 0.2) + 4
        s.append(f'<text x="{CX+8}" y="{ly:.1f}" font-size="11" font-style="italic" fill="{GOLD}" '
                 f'fill-opacity="0.55" font-family="{DISP}">{g}</text>')

    if applicable_axes is None:
        applicable_axes = str(sum(1 for g in grades if g != "N/A"))

    # ---- data polygon ----
    pts = [_v(i, TIER.get(grades[i], TIER["?"])[0]) for i in range(6)]
    s.append(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="url(#poly)" filter="url(#glow)"/>')
    for i in range(6):
        a, b = pts[i], pts[(i + 1) % 6]
        if grades[i] in UNSCORED or grades[(i + 1) % 6] in UNSCORED:
            na_edge = "N/A" in (grades[i], grades[(i + 1) % 6]) and "?" not in (grades[i], grades[(i + 1) % 6])
            col_e, dash = ("#4B5563", "1 5") if na_edge else ("#8B949E", "4 4")
            s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
                     f'stroke="{col_e}" stroke-width="2" stroke-dasharray="{dash}" stroke-opacity="0.92"/>')
        else:
            s.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{oc}" stroke-width="3"/>')
    for i in range(6):
        x, y = pts[i]
        g = grades[i]
        if g == "?":
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="#10100b" stroke="#8B949E" stroke-width="2" stroke-dasharray="2 2"/>')
        elif g == "N/A":
            s.append(f'<rect x="{x-4.5:.1f}" y="{y-4.5:.1f}" width="9" height="9" fill="#10100b" stroke="#4B5563" stroke-width="2"/>')
        else:
            s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5.5" fill="{TIER[g][1]}" stroke="#1a1306" stroke-width="1.2"/>')

    # ---- axis labels: the real axis name + grade (no JoJo vocabulary) ----
    afs = cfg["axis_fs"]
    for i, label in enumerate(cfg["axes"]):
        lx, ly = _v(i, 1.0)
        a = math.radians(-90 + 60 * i)
        ox, oy = lx + 13 * math.cos(a), ly + 22 * math.sin(a)
        anchor = "middle"
        if math.cos(a) > 0.3:
            anchor = "start"
        elif math.cos(a) < -0.3:
            anchor = "end"
        g = grades[i]
        col = TIER.get(g, TIER["?"])[1]
        s.append(f'<text x="{ox:.1f}" y="{oy+4:.1f}" font-size="{afs}" font-weight="900" fill="{PARCH}" '
                 f'text-anchor="{anchor}" font-family="{lf}" letter-spacing="0.4" filter="url(#soft)">{label} '
                 f'<tspan fill="{col}" font-family="{DISP}" font-style="italic" font-size="{afs+5}">{g}</tspan></text>')

    # ---- right panel ----
    px = 498
    # banner tag
    s.append(f'<text x="{px}" y="60" font-size="13" letter-spacing="5" fill="{GOLD}" font-weight="900" '
             f'font-family="{lf}" filter="url(#soft)">◆ {cfg["tag"]}</text>')
    # name — bold italic, skewed (JoJo logo energy)
    s.append(f'<g transform="translate({px},112) skewX(-9)">'
             f'<text x="2" y="2" font-size="30" font-weight="900" font-style="italic" fill="#000" fill-opacity="0.6" '
             f'font-family="{DISP}">{_esc(name)}</text>'
             f'<text x="0" y="0" font-size="30" font-weight="900" font-style="italic" fill="#fff7e2" '
             f'font-family="{DISP}">{_esc(name)}</text></g>')
    s.append(f'<line x1="{px}" y1="124" x2="{px+150}" y2="124" stroke="url(#frame)" stroke-width="2"/>')
    # overall — starburst + huge outlined italic letter
    ocx, ocy = px + 52, 200
    s.append(f'<g opacity="0.85" filter="url(#glow)">')
    for k in range(16):
        a = math.radians(k * 22.5)
        x1, y1 = ocx + 18 * math.cos(a), ocy - 18 + 18 * math.sin(a)
        x2, y2 = ocx + 62 * math.cos(a), ocy - 18 + 62 * math.sin(a)
        s.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{oc}" stroke-opacity="0.16" stroke-width="3"/>')
    s.append("</g>")
    s.append(f'<text x="{ocx}" y="226" font-size="104" font-weight="900" font-style="italic" text-anchor="middle" '
             f'fill="{oc}" stroke="#000" stroke-width="2" paint-order="stroke" font-family="{DISP}" filter="url(#glow)">{overall}</text>')
    nt = f"   {_esc(note)}" if note else ""
    s.append(f'<text x="{px}" y="252" font-size="11" letter-spacing="3" fill="{GOLD}" font-family="{lf}" font-weight="900">'
             f'{cfg["overall"]}{nt}</text>')
    s.append(f'<text x="{px+150}" y="252" font-size="11" letter-spacing="2" fill="#8B949E" '
             f'font-family="{lf}" font-weight="900" text-anchor="end">{cfg["axes_scored"]} {scored_axes}/{applicable_axes}</text>')
    # axis rows
    y0 = 288
    for i, label in enumerate(cfg["axes"]):
        yy = y0 + i * 29
        g = grades[i]
        col = TIER.get(g, TIER["?"])[1]
        lfs = 14 if lang == "zh" else 11
        s.append(f'<text x="{px}" y="{yy}" font-size="{lfs}" font-weight="900" fill="{PARCH}" font-family="{lf}" letter-spacing="0.4">{label}</text>')
        bx, bw = px + 150, 118
        s.append(f'<rect x="{bx}" y="{yy-11}" width="{bw}" height="9" rx="2" fill="#241d0e" stroke="{GOLD_DK}" stroke-opacity="0.5"/>')
        if g not in UNSCORED:
            s.append(f'<rect x="{bx}" y="{yy-11}" width="{bw*TIER[g][0]:.0f}" height="9" rx="2" fill="{col}"/>')
        elif g == "?":
            s.append(f'<rect x="{bx}" y="{yy-11}" width="{bw}" height="9" rx="2" fill="none" stroke="#8B949E" stroke-dasharray="3 3"/>')
        else:
            s.append(f'<line x1="{bx}" y1="{yy-6.5}" x2="{bx+bw}" y2="{yy-6.5}" stroke="#4B5563" stroke-width="2"/>')
        gfs = 11 if g == "N/A" else 16
        s.append(f'<text x="{bx+bw+13}" y="{yy}" font-size="{gfs}" font-weight="900" font-style="italic" fill="{col}" '
                 f'font-family="{DISP}" text-anchor="middle">{_esc(g)}</text>')
    # flags
    fy = y0 + 6 * 29 + 6
    fx = px
    for fl in flags:
        bw = (9 if fl.isascii() else 13) * len(fl) + 20
        s.append(f'<rect x="{fx}" y="{fy-13}" width="{bw}" height="21" rx="3" fill="#1b1408" stroke="{GOLD}" stroke-opacity="0.5"/>')
        s.append(f'<text x="{fx+bw/2}" y="{fy+2}" font-size="11" font-weight="700" fill="{PARCH}" text-anchor="middle" font-family="{lf}">{_esc(fl)}</text>')
        fx += bw + 8
    s.append("</svg>")
    return "\n".join(s)


# ---------------------------------------------------------------- page -> card
def card_for_page(page: Path, duplicates: set[str]) -> Path | None:
    fm = parse_frontmatter(page.read_text(encoding="utf-8"))
    health = fm.get("health")
    if not isinstance(health, dict):
        return None
    lang = "zh" if page.name.endswith(".zh.md") else "en"
    axes = health.get("axes", {})
    grades = [str(axes.get(k, {}).get("grade", "?")) for k in AXIS_KEYS]
    overall = str(health.get("overall", "?"))
    scored_axes = str(health.get("scored_axes", sum(1 for g in grades if g not in UNSCORED)))
    applicable_axes = str(health.get("applicable_axes", sum(1 for g in grades if g != "N/A")))
    name = str(fm.get("name", page.stem))

    flags: list[str] = []
    maint = axes.get("maintenance", {}).get("raw", {})
    if isinstance(maint, dict) and str(maint.get("archived", "")).lower() == "true":
        flags.append(LANG[lang]["archived"])
    risk = axes.get("risk_license", {}).get("raw", {})
    if isinstance(risk, dict) and risk.get("spdx_id"):
        flags.append(str(risk["spdx_id"]))
    note = ""
    if str(health.get("capped", "")).lower() == "true":
        note = str(health.get("cap_reason") or "")

    svg = render(lang, name, grades, overall, note, flags[:3], scored_axes, applicable_axes)
    ASSETS.mkdir(parents=True, exist_ok=True)
    out = ASSETS / (card_stem_for_page(page, duplicates) + LANG[lang]["ext"])
    out.write_text(svg, encoding="utf-8")
    return out


def main(argv: list[str]) -> int:
    if not argv:
        sys.stderr.write(__doc__ or "")
        return 2
    if argv[0] == "--all":
        pages = [p for p in (ROOT / "categories").rglob("*.md") if not p.name.startswith("INDEX")]
    else:
        pages = [Path(a) if Path(a).is_absolute() else ROOT / a for a in argv]
    duplicates = duplicate_slugs(ROOT)
    n = 0
    for page in pages:
        out = card_for_page(page, duplicates)
        if out:
            print(f"wrote {out.relative_to(ROOT)}")
            n += 1
    print(f"{n} card(s) generated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
