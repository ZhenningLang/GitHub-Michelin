# document-parsing

> Category node. Parse/convert documents (PDF/DOCX/…) into structured Markdown/JSON for gen-AI ingestion.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | A (5/6) | [→](docling.md) |
| **MarkItDown** | Use it when an agent or RAG pipeline must turn mixed Office files, HTML, EPUB and simple PDFs into Markdown with one lightweight Python call — but scanned or complex-layout PDFs need Marker or Docling, since it has no OCR or layout model. | B (6/6) | [→](markitdown.md) |
| **olmOCR** | Use it when you are turning thousands to millions of PDFs with equations, tables and multi-column layouts into clean reading-order Markdown for an LLM corpus — but local runs need a 12 GB+ NVIDIA GPU, and upstream has been quiet since 2026-03. | C (5/6) | [→](olmocr.md) |
| **Marker** | Use it when converting thousands of PDFs (papers, textbooks, scans) into Markdown with real tables, LaTeX math and selective OCR on your own hardware — but the model weights are free only below a $5M funding or revenue threshold. | B (6/6) | [→](marker.md) |
| **unstructured** | Use it when a RAG pipeline over mixed PDFs, emails and Office files needs typed elements with page metadata and section-aware chunking rather than one Markdown string — but its open-source PDF table accuracy trails Docling and Marker, and analytics pings are on by default. | A (6/6) | [→](unstructured.md) |
| **any2html** | Use it when you need any2html in this category. | D (5/6) | [→](any2html.md) |
| **Dedoc** | Use it when an on-premises Python pipeline needs multi-format documents recovered as logical trees with tables, annotations, and attachments; expect a heavy Linux/system-package stack and limits on difficult scans. | B (5/6) | [→](dedoc.md) |
| **Bella Domify** | Use it when Chinese RAG ingestion needs detailed PDF/Office DOM trees plus FastAPI/Kafka/S3 service integration; license ambiguity, optional remote OCR, and heavy infrastructure are decisive constraints. | C (5/6) | [→](bella-domify.md) |
| **MinerU Skill** | Use it when a coding agent needs one-command cloud document-to-Markdown through CLI/MCP, with batch, resume, or content-tool delivery; files cross a service boundary and remain subject to quotas and API changes. | C (5/6) | [→](mineru-skill.md) |
| **anydoc** | Use it when a pipeline gets a mixed pile of Office (incl. legacy .doc/.ppt/.xls), OpenDocument, RTF, EPUB and text-PDF files and needs one consistent Markdown in milliseconds with no LibreOffice or models; no OCR — scanned pages fail. | B (6/6) | [→](anydoc.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Docling](docling.md) | ✅ | A (5/6) | Rich-document parsing (layout + tables) to structured Markdown/JSON; heavier model deps than plain text extraction. |
| [MarkItDown](markitdown.md) | ✅ | B (6/6) | Broad format coverage with no GPU or model download, at the cost of layout fidelity and optional features that send files to external LLMs or Azure. |
| [olmOCR](olmocr.md) | ✅ | C (5/6) | Buys VLM-grade fidelity on equations and messy scans; costs GPU inference per page, versus cheaper CPU-only Docling or PyMuPDF when layout fidelity matters less. |
| [PageIndex](../rag-retrieval/structured-retrieval/pageindex.md) | ✅ | B (6/6) | Builds a retrieval index over long structured docs — downstream of parsing, not a parser. |
| [any2html](any2html.md) | ✅ | D (5/6) | Use it when you need any2html in this category. |
| [Dedoc](dedoc.md) | ✅ | B (5/6) | Multi-format logical-tree parsing with tables, annotations, and attachments; deeper than lightweight Markdown conversion, but heavier on Linux dependencies and limited on difficult scans. |
| [Bella Domify](bella-domify.md) | ✅ | C (5/6) | Detailed pdf2docx-derived DOM trees and service hooks; rich layout objects, but heavy infrastructure, optional outbound OCR, and an unresolved GPL v2/v3 declaration conflict. |
| [MinerU Skill](mineru-skill.md) | ✅ | C (5/6) | Agent-facing CLI/MCP over MinerU's cloud API with batch, resume, and delivery; avoids local model deployment but adds upload, quota, and third-party API risk. |
| [anydoc](anydoc.md) | ✅ | B (6/6) | Pure-Rust converter for 20+ office/ebook/PDF extensions with Node/Python/WASM bindings; fast and dependency-free, but no OCR, heuristic PDF tables, and a young single-author 0.x project. |
| LlamaParse / self-hosted MinerU | 未收录 | — | Cloud and self-hosted document-parsing routes named across the pages. |


## What belongs here

Libraries whose primary job is **parsing/converting documents into structured representations** for gen-AI/RAG. Not retrieval/indexing itself (see `rag-retrieval`), not document archiving/search (see `document-management`), not raw OCR (see `ocr`).
