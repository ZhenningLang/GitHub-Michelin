# pdf-reading

> Category node. Render PDFs for viewing, or read their text, tables, and layout objects out programmatically.
> ← back to [pdf-tools](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **PDF.js** | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. | A (6/6) | [→](pdfjs.md) |
| **PyMuPDF** | Use it when a high-volume Python pipeline must extract positioned text and tables, render page images, redact and merge PDFs in one fast offline package — but it is AGPL-3.0, so closed-source or SaaS use needs Artifex's commercial license. | B (6/6) | [→](pymupdf.md) |
| **pdfplumber** | Use it when tables in machine-generated PDFs (filings, notices, price lists) extract as smeared text and you need character coordinates plus a visual debugger to tune extraction until rows line up — but it has no OCR for scanned PDFs. | B (6/6) | [→](pdfplumber.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [PDF.js](pdfjs.md) | ✅ | A (6/6) | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. |
| [PyMuPDF](pymupdf.md) | ✅ | B (6/6) | MuPDF's C engine behind one pip install covers reading, rendering and editing, in exchange for AGPL-or-paid licensing, paid Office support, and low-level glyph output rather than document structure. |
| [pdfplumber](pdfplumber.md) | ✅ | B (6/6) | An MIT, pure-Python view of every char, line and rectangle that you can inspect and tune, paid for with speed far below PyMuPDF and a project that rests on one maintainer. |

## What belongs here

Viewers, renderers, and low-level parsers that **read** PDFs: page rendering, text and table extraction, per-character geometry. Not parsing documents into structured Markdown/JSON for gen-AI (see `document-parsing`), not OCR engines (see `ocr`).
