# office-automation

> Category node. Programmatically create, read, and edit **native** Office documents (`.docx` / `.xlsx` / `.pptx`) — the authoring side of the pipe, for scripts and for agents.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OfficeCLI** | Use it when an agent must read, edit, and create all three Office formats on a machine with no Python and no Office, and needs to *see* the rendered result — but it is 6 months old, 98% single-author, has no public test suite, and auto-updates plus rewrites your agent skill dirs by default. | B (6/6) | [→](officecli.md) |
| **python-docx** | Use it when a Python service must create or edit Word `.docx` in place, with a pinnable MIT dependency that has survived 13 years — but there is no rendering, and footnotes/endnotes have been unimplemented since 2014. | B (5/6) | [→](python-docx.md) |
| **python-pptx** | Use it when you must generate or edit native `.pptx` from Python and the deliverable has to open in PowerPoint — but it has not shipped since 2024-08-07, and animations (2017) and SmartArt (2014) were never implemented. | C (4/6) | [→](python-pptx.md) |
| **XlsxWriter** | Use it when a Python service generates new `.xlsx` files from data and you want zero dependencies plus 13 years of stability — but it is write-only, cannot open an existing workbook, and does not calculate formulas. | B (6/6) | [→](xlsxwriter.md) |
| **Office-Word-MCP-Server** | Use it only when an existing LLM integration is already bound to its ~55 Word tool schemas — the repo was archived 2025-12-31 and its author mass-archived ~15 MCP servers; for new work use OfficeCLI or wrap python-docx yourself. | C (6/6) | [→](office-word-mcp-server.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OfficeCLI](officecli.md) | ✅ | B (6/6) | All three formats + a render-back loop in one dependency-free binary; paid for with a 6-month solo-authored codebase, no public tests, and default-on auto-update that rewrites agent skill dirs. |
| [python-docx](python-docx.md) | ✅ | B (5/6) | The stable, pinnable Word layer most agent skills wrap; Word-only, no rendering, decade-old feature gaps. |
| [python-pptx](python-pptx.md) | ✅ | C (4/6) | The only mature MIT `.pptx` authoring library; coasting since 2024-08 with no animation or SmartArt API. |
| [XlsxWriter](xlsxwriter.md) | ✅ | B (6/6) | Zero-dependency, production-stable, actively maintained spreadsheet generation; write-only and does not evaluate formulas. |
| [Office-Word-MCP-Server](office-word-mcp-server.md) | ✅ | C (6/6) | MCP-native Word editing with the footnote support python-docx lacks; archived, Word-only, and its PDF tool needs a real MS Word install. |
| [Pandoc](../markdown-tools/pandoc.md) | ✅ | B (6/6) | One-call Markdown → `.docx`/`.pptx` export with a reference doc for styling; cannot edit an existing Office file in place. |
| [MarkItDown](../document-parsing/markitdown.md) | ✅ | A (6/6) | The opposite direction: Office → Markdown for LLM ingestion, read-only and deliberately lossy on formatting. |
| openpyxl | 未收录 | — | The read+write `.xlsx` counterpart to XlsxWriter; not indexed because its canonical repo is on Heptapod (Mercurial), not GitHub, and this index's health/upstream tooling is GitHub-only. |
| Office-PowerPoint-MCP-Server | 未收录 | — | The `.pptx` sibling of the Word MCP server (1,852 stars); archived by the same author on 2025-12-31, so it adds no selection value beyond that note. |
| LibreOffice headless / Aspose / Apache POI | 未收录 | — | Conversion-engine, commercial, and JVM routes named across these pages; different abstraction level from an agent-facing OOXML editor. |


## What belongs here

Tools and libraries whose primary job is **producing or modifying native Office files** (`.docx` / `.xlsx` / `.pptx`) — whether called from a script, a CLI, or an agent over MCP. Not document → Markdown ingestion (see [document-parsing](../document-parsing/INDEX.md)), not OCR (see [ocr](../ocr/INDEX.md)), not archiving and full-text search over paperwork (see [document-management](../document-management/INDEX.md)), and not HTML/visual deck generation where the artifact is not an Office file (see [ai-design-generation](../ai-design-generation/INDEX.md) and [agent-skills/slides-ppt](../agent-skills/slides-ppt/INDEX.md)). One-way converters such as Pandoc live in their own format categories and are cross-linked here.
