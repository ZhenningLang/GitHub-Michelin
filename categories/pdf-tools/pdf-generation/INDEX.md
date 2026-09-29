# pdf-generation

> Category node. Create new PDFs in code — from scratch, from HTML or components, or by composing imported pages.
> ← back to [pdf-tools](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **pdf-lib** | Use it when you need to create or modify PDFs in JS/TS — in the browser, Node, Deno, or React Native — without native dependencies. | C (4/6) | [→](pdf-lib.md) |
| **jsPDF** | Use it when you need client-side PDF generation from HTML, text, and graphics in the browser — it's creation-only, not for editing existing PDFs. | B (5/6) | [→](jspdf.md) |
| **pdfcn** | Use it when themed React PDF components and whole document blocks (invoices, reports, labels) should be copy-pasted in via the shadcn CLI on Takumi or Forme — it generates new PDFs only. | B (6/6) | [→](pdfcn.md) |
| **FPDI** | Use it when a PHP app built on FPDF/TCPDF/tFPDF must import pages from an existing PDF as templates — the free parser rejects encrypted files and compressed cross-reference streams. | A (5/6) | [→](fpdi.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [pdf-lib](pdf-lib.md) | ✅ | C (4/6) | Use it when you need to create or modify PDFs in JS/TS — in the browser, Node, Deno, or React Native — without native dependencies. |
| [jsPDF](jspdf.md) | ✅ | B (5/6) | Use it when you need client-side PDF generation from HTML, text, and graphics in the browser — it's creation-only, not for editing existing PDFs. |
| [pdfcn](pdfcn.md) | ✅ | B (6/6) | Copy-paste React PDF components and themed document blocks over Takumi/Forme WASM engines; no releases to pin, generation-only. |
| [FPDI](fpdi.md) | ✅ | A (5/6) | Import pages from existing PDFs as templates in PHP writers; the free parser rejects encrypted PDFs and compressed cross-reference streams. |

## What belongs here

Libraries whose primary job is to **produce a new PDF** from application code: drawing APIs, HTML/component-to-PDF, and page import into a new composition. pdf-lib also edits existing files, but its center of gravity is creation. Not in-place rewriting or signing of an existing file (see `pdf-transform-signing`).
