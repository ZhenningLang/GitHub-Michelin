# design-tokens

> Category node. Get, check and gate design tokens — the colours, type scale, spacing, radii and shadows a UI is built from — when the source of truth is a live site rather than a file you author.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Dembrandt** | Use it when the only source of a design system is a live URL and you need its real colours, type and spacing as DTCG/Tailwind/DESIGN.md tokens — or a CI gate that fails when they drift — not when you already author the tokens or fear layout regressions. | C (5/6) | [→](dembrandt.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Dembrandt](dembrandt.md) | ✅ | C (5/6) | MIT CLI + MCP server + GitHub Action that reads computed styles from a real browser and exports tokens or a drift verdict; single-maintainer, pre-1.0, and its heuristics move baselines almost weekly. |
| Style Dictionary · Project Wallace css-analyzer · BackstopJS | 未收录 | — | The opposite direction (author tokens → platforms), static CSS-source auditing, and pixel-diff visual regression — named and weighed in Dembrandt's comparison, not yet indexed. |

## What belongs here

Repositories whose primary job is **design tokens as data**: extracting them from a rendered site or stylesheet, validating or transforming them, and gating changes to them in CI. Not design editors (see `design-editors`); not agent skills that carry a named site's look into code (see `agent-skills/design/design-to-code`); not general web scraping (see `web-scraping`).
