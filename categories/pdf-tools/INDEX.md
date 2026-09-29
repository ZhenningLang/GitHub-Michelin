# pdf-tools

> Category node. Render, read, and manipulate PDF files.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **PDF Generation** | You are building a new PDF (invoice, label, report, composed document) from your app's code. | [→](pdf-generation/INDEX.md) |
| **PDF Reading & Extraction** | You need to display a PDF or pull text/tables/positions out of one. | [→](pdf-reading/INDEX.md) |
| **PDF Transform & Signing** | You already have a PDF and must repair, split/merge, make searchable, or sign it while preserving what is there. | [→](pdf-transform-signing/INDEX.md) |
| **PDF Translation** | A (scientific) PDF must be translated and still look like the original. | [→](pdf-translation/INDEX.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [PDF Generation](pdf-generation/INDEX.md) | Sub-category | Create new PDFs in code — from scratch, from HTML or components, or by composing imported pages. |
| [PDF Reading & Extraction](pdf-reading/INDEX.md) | Sub-category | Render PDFs for viewing, or read their text, tables, and layout objects out programmatically. |
| [PDF Transform & Signing](pdf-transform-signing/INDEX.md) | Sub-category | Rewrite existing PDFs in place — structural transforms, an added OCR text layer, or digital signatures that preserve revisions. |
| [PDF Translation](pdf-translation/INDEX.md) | Sub-category | Translate PDFs while preserving layout, formulas, and columns. |

## What belongs here

Tools whose primary job is to **render, read, or manipulate PDF files** — navigate by what you do to the PDF: generate a new one, read its content, rewrite or sign an existing one, or translate it with layout intact. Not parsing documents into structured Markdown/JSON for gen-AI (see `document-parsing`), not OCR engines (see `ocr`), not bilingual ebook CLIs that flatten PDFs to text (see `reading-tools`).
