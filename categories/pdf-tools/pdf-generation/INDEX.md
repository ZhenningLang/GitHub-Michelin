# pdf-generation

> Category node. Create new PDFs in code — from scratch, from HTML or components, or by composing imported pages.
> ← back to [pdf-tools](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **pdf-lib** | Use it when you must create, fill or merge PDFs from the same TypeScript code in the browser, Node, Deno or React Native with no native deps — but upstream has been frozen since 2021-11, so new work should take the maintained @cantoo/pdf-lib fork. | C (4/6) | [→](pdf-lib.md) |
| **jsPDF** | Use it when a web app needs a Download PDF button for receipts, labels, tickets or certificates built in the browser by placing text and images at coordinates — but it cannot edit existing PDFs, and its html() output drifts on modern CSS. | B (5/6) | [→](jspdf.md) |
| **pdfcn** | Use it when themed React PDF components and whole document blocks (invoices, reports, labels) should be copy-pasted in via the shadcn CLI on Takumi or Forme — it generates new PDFs only. | B (6/6) | [→](pdfcn.md) |
| **FPDI** | Use it when a PHP app built on FPDF/TCPDF/tFPDF must import pages from an existing PDF as templates — the free parser rejects encrypted files and compressed cross-reference streams. | A (5/6) | [→](fpdi.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [pdf-lib](pdf-lib.md) | ✅ | C (4/6) | Gets a typed, pure-JS PDF writer with tens of millions of monthly npm downloads; costs no rendering, no HTML-to-PDF, a ~500KB browser bundle, and bugs that will never be fixed upstream. |
| [jsPDF](jspdf.md) | ✅ | B (5/6) | No backend, offline-capable PDF creation with the longest track record among JS options; you hand-place every coordinate, get no automatic page flow, and rely on a few maintainers shipping mostly security fixes. |
| [pdfcn](pdfcn.md) | ✅ | B (6/6) | Copy-paste React PDF components and themed document blocks over Takumi/Forme WASM engines; no releases to pin, generation-only. |
| [FPDI](fpdi.md) | ✅ | A (5/6) | Import pages from existing PDFs as templates in PHP writers; the free parser rejects encrypted PDFs and compressed cross-reference streams. |

## What belongs here

Libraries whose primary job is to **produce a new PDF** from application code: drawing APIs, HTML/component-to-PDF, and page import into a new composition. pdf-lib also edits existing files, but its center of gravity is creation. Not in-place rewriting or signing of an existing file (see `pdf-transform-signing`).
