# pdf-transform-signing

> Category node. Rewrite existing PDFs in place — structural transforms, an added OCR text layer, or digital signatures that preserve revisions.
> ← back to [pdf-tools](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **qpdf** | qpdf: A content-preserving PDF document transformer | A (6/6) | [→](qpdf.md) |
| **OCRmyPDF** | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched | B (6/6) | [→](ocrmypdf.md) |
| **SAPP** | Use it when a PHP application must append PKCS#12 signatures while preserving an existing PDF's revisions and object graph; not for encrypted PDFs, broad repair, or independently validated PAdES/LTV compliance. | B (5/6) | [→](sapp.md) |
| **pyHanko** | Use it when Python must create or validate PDF signatures with documented PAdES/LTV workflows — upstream still labels the project beta. | A (6/6) | [→](pyhanko.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [qpdf](qpdf.md) | ✅ | A (6/6) | qpdf: A content-preserving PDF document transformer |
| [OCRmyPDF](ocrmypdf.md) | ✅ | B (6/6) | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched |
| [SAPP](sapp.md) | ✅ | B (5/6) | PHP-native incremental PDF signing and object manipulation that preserves revisions; narrower specification coverage than qpdf and no independently validated PAdES/LTV evidence. |
| [pyHanko](pyhanko.md) | ✅ | A (6/6) | Python PDF signing, timestamping and validation with documented PAdES/LTV workflows; upstream still labels itself beta. |
| OpenPDFSign | 未收录 | — | Standalone Java signing CLI named by the pages. |

## What belongs here

Tools and libraries whose input *and* output is an **existing PDF**: content-preserving structural transforms, adding an OCR text layer to scans, and incremental-update signing/validation (PAdES, PKCS#12, timestamps). Not generating new documents (see `pdf-generation`), not standalone OCR engines (see `ocr`).
