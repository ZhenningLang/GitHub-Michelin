# pdf-translation

> Category node. Translate PDFs while preserving layout, formulas, and columns.
> ← back to [pdf-tools](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **PDFMathTranslate** | Use it when a scientific PDF must be translated without losing formulas and columns — CLI/GUI/Docker, many translators; AGPL, and 1.x pins an old BabelDOC. | C (5/6) | [→](pdfmathtranslate.md) |
| **BabelDOC** | Use it when you need the layout-preserving PDF translation engine (current 0.6) to embed or debug — not an end-user app; AGPL, OpenAI-only, API unsupported. | C (6/6) | [→](babeldoc.md) |
| **PDFMathTranslate-next** | Use it when you want BabelDOC 0.6 as a CLI/WebUI with SiliconFlowFree by default — AGPL, Google/Bing gone, last push 2026-05. | D (4/6) | [→](pdfmathtranslate-next.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [PDFMathTranslate](pdfmathtranslate.md) | ✅ | C (5/6) | End-user PDF paper translation that keeps layout; many translators, but AGPL and the 1.x tree pins BabelDOC `<0.3`. |
| [BabelDOC](babeldoc.md) | ✅ | C (6/6) | The layout-preserving translation engine Immersive Translate ships; OpenAI-only, API declared internal, current 0.6 is not what pdf2zh 1.x installs. |
| [PDFMathTranslate-next](pdfmathtranslate-next.md) | ✅ | D (4/6) | Official BabelDOC 0.6 product wrapper; SiliconFlowFree default, Google/Bing deprecated, quiet since 2026-05. |

## What belongs here

Layout-preserving PDF translators and the engine behind them (BabelDOC and its PDFMathTranslate front ends). Not bilingual ebook CLIs that flatten PDFs to text (see `reading-tools`).
