# pdf-tools

> Category node. Render, read, and manipulate PDF files.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **PDF.js** | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. | A (6/6) | [→](pdfjs.md) |
| **pdf-lib** | Use it when you need to create or modify PDFs in JS/TS — in the browser, Node, Deno, or React Native — without native dependencies. | C (4/6) | [→](pdf-lib.md) |
| **jsPDF** | Use it when you need client-side PDF generation from HTML, text, and graphics in the browser — it's creation-only, not for editing existing PDFs. | B (5/6) | [→](jspdf.md) |
| **PyMuPDF** | PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents. | B (6/6) | [→](pymupdf.md) |
| **pdfplumber** | Plumb a PDF for detailed information about each char, rectangle, line, et cetera — and easily extract text and tables. | B (6/6) | [→](pdfplumber.md) |
| **OCRmyPDF** | OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be searched | B (6/6) | [→](ocrmypdf.md) |
| **qpdf** | qpdf: A content-preserving PDF document transformer | A (6/6) | [→](qpdf.md) |
| **SAPP** | Use it when a PHP application must append PKCS#12 signatures while preserving an existing PDF's revisions and object graph; not for encrypted PDFs, broad repair, or independently validated PAdES/LTV compliance. | B (5/6) | [→](sapp.md) |
| **FPDI** | Use it when a PHP app built on FPDF/TCPDF/tFPDF must import pages from an existing PDF as templates — the free parser rejects encrypted files and compressed cross-reference streams. | A (5/6) | [→](fpdi.md) |
| **pyHanko** | Use it when Python must create or validate PDF signatures with documented PAdES/LTV workflows — upstream still labels the project beta. | A (6/6) | [→](pyhanko.md) |
| **PDFMathTranslate** | Use it when a scientific PDF must be translated without losing formulas and columns — CLI/GUI/Docker, many translators; AGPL, and 1.x pins an old BabelDOC. | C (5/6) | [→](pdfmathtranslate.md) |
| **BabelDOC** | Use it when you need the layout-preserving PDF translation engine (current 0.6) to embed or debug — not an end-user app; AGPL, OpenAI-only, API unsupported. | C (6/6) | [→](babeldoc.md) |
| **PDFMathTranslate-next** | Use it when you want BabelDOC 0.6 as a CLI/WebUI with SiliconFlowFree by default — AGPL, Google/Bing gone, last push 2026-05. | D (4/6) | [→](pdfmathtranslate-next.md) |
| **pdfcn** | Use it when themed React PDF components and whole document blocks (invoices, reports, labels) should be copy-pasted in via the shadcn CLI on Takumi or Forme — it generates new PDFs only. | B (6/6) | [→](pdfcn.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [PDF.js](pdfjs.md) | ✅ | A (6/6) | Use it when you need to render or read PDFs in the browser/Node (Firefox's engine) — it doesn't create or edit PDFs. |
| [pdf-lib](pdf-lib.md) | ✅ | C (4/6) | Use it when you need to create or modify PDFs in JS/TS — in the browser, Node, Deno, or React Native — without native dependencies. |
| [jsPDF](jspdf.md) | ✅ | B (5/6) | Use it when you need client-side PDF generation from HTML, text, and graphics in the browser — it's creation-only, not for editing existing PDFs. |
| [pdfcn](pdfcn.md) | ✅ | B (6/6) | Copy-paste React PDF components and themed document blocks over Takumi/Forme WASM engines; no releases to pin, generation-only. |
| [SAPP](sapp.md) | ✅ | B (5/6) | PHP-native incremental PDF signing and object manipulation that preserves revisions; narrower specification coverage than qpdf and no independently validated PAdES/LTV evidence. |
| [FPDI](fpdi.md) | ✅ | A (5/6) | Import pages from existing PDFs as templates in PHP writers; the free parser rejects encrypted PDFs and compressed cross-reference streams. |
| [pyHanko](pyhanko.md) | ✅ | A (6/6) | Python PDF signing, timestamping and validation with documented PAdES/LTV workflows; upstream still labels itself beta. |
| [PDFMathTranslate](pdfmathtranslate.md) | ✅ | C (5/6) | End-user PDF paper translation that keeps layout; many translators, but AGPL and the 1.x tree pins BabelDOC `<0.3`. |
| [BabelDOC](babeldoc.md) | ✅ | C (6/6) | The layout-preserving translation engine Immersive Translate ships; OpenAI-only, API declared internal, current 0.6 is not what pdf2zh 1.x installs. |
| [PDFMathTranslate-next](pdfmathtranslate-next.md) | ✅ | D (4/6) | Official BabelDOC 0.6 product wrapper; SiliconFlowFree default, Google/Bing deprecated, quiet since 2026-05. |
| OpenPDFSign | 未收录 | — | Standalone Java signing CLI named by the pages. |

## What belongs here

Tools whose primary job is to **render, read, or manipulate PDF files** — viewers, parsers, generators, editors, and layout-preserving PDF translators. Not parsing documents into structured Markdown/JSON for gen-AI (see `document-parsing`), not OCR engines (see `ocr`), not bilingual ebook CLIs that flatten PDFs to text (see `reading-tools`).
