# pdf-transform-signing

> Category node. Rewrite existing PDFs in place — structural transforms, an added OCR text layer, or digital signatures that preserve revisions.
> ← back to [pdf-tools](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **qpdf** | Use it when a script must merge, split, reorder, encrypt, linearize or repair PDFs without re-rendering pages, fonts or form fields — but it does not render, extract text, draw new content or sign. | A (6/6) | [→](qpdf.md) |
| **OCRmyPDF** | Use it when a scanner keeps dropping image-only PDFs into a folder and you want the same files, optionally PDF/A, made searchable and copyable by an unattended job — but it outputs a PDF with a hidden text layer, not Markdown for RAG. | B (6/6) | [→](ocrmypdf.md) |
| **SAPP** | Use it when a PHP application must append PKCS#12 signatures while preserving an existing PDF's revisions and object graph; not for encrypted PDFs, broad repair, or independently validated PAdES/LTV compliance. | B (5/6) | [→](sapp.md) |
| **pyHanko** | Use it when Python must create or validate PDF signatures with documented PAdES/LTV workflows — upstream still labels the project beta. | A (6/6) | [→](pyhanko.md) |
| **PdfCraft** | Use it when people on macOS, Windows or Linux need an offline, account-free desktop app to organize, comment on, fill, redact and password-protect PDFs (or an agent needs the same through MCP) — but it is nine days old and pre-1.0, with a borrowed renderer and unmeasured Acrobat fidelity. | C (5/6) | [→](pdfcraft.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [qpdf](qpdf.md) | ✅ | A (6/6) | Byte-for-byte content preservation from a ~20-year-old CLI callable from any language, in exchange for structural operations only and a two-person core team. |
| [OCRmyPDF](ocrmypdf.md) | ✅ | B (6/6) | Original page images kept intact with an aligned OCR layer and validated output, at the cost of Tesseract's weakness on handwriting and photos, and a roadmap that depends on one maintainer. |
| [SAPP](sapp.md) | ✅ | B (5/6) | PHP-native incremental PDF signing and object manipulation that preserves revisions; narrower specification coverage than qpdf and no independently validated PAdES/LTV evidence. |
| [pyHanko](pyhanko.md) | ✅ | A (6/6) | Python PDF signing, timestamping and validation with documented PAdES/LTV workflows; upstream still labels itself beta. |
| [PdfCraft](pdfcraft.md) | ✅ | C (5/6) | A free, native Acrobat-style desktop workbench with append-only saves and an MCP tool surface, in exchange for a nine-day track record, borrowed rendering and a single-vendor, agent-written codebase. |
| OpenPDFSign | 未收录 | — | Standalone Java signing CLI named by the pages. |

## What belongs here

Tools, libraries and desktop workbenches whose input *and* output is an **existing PDF**: content-preserving structural transforms, adding an OCR text layer to scans, and incremental-update signing/validation (PAdES, PKCS#12, timestamps). Not generating new documents (see `pdf-generation`), not standalone OCR engines (see `ocr`).
