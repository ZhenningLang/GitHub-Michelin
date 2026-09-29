# pdf-reading

> Category node. Render PDFs for viewing, or read their text, tables, and layout objects out programmatically.
> ← back to [pdf-tools](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **PDF.js** | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. | A (6/6) | [→](pdfjs.md) |
| **PyMuPDF** | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. | B (6/6) | [→](pymupdf.md) |
| **pdfplumber** | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. | B (6/6) | [→](pdfplumber.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [PDF.js](pdfjs.md) | ✅ | A (6/6) | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. |
| [PyMuPDF](pymupdf.md) | ✅ | B (6/6) | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. |
| [pdfplumber](pdfplumber.md) | ✅ | B (6/6) | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. |

## What belongs here

Viewers, renderers, and low-level parsers that **read** PDFs: page rendering, text and table extraction, per-character geometry. Not parsing documents into structured Markdown/JSON for gen-AI (see `document-parsing`), not OCR engines (see `ocr`).
