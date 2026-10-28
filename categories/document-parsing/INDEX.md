# document-parsing

> Category node. Parse/convert documents (PDF/DOCX/…) into structured Markdown/JSON for gen-AI ingestion.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

- [Model-backed PDF parsing](model-backed-pdf/INDEX.md) — PDF/image-focused layout, OCR and page-recognition pipelines, including selective or full-page model processing.

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **ContextGem** | Extract named clauses and typed domain values with optional source-object references; you own model access, evaluation and durable jobs. | C (5/6) | [→](contextgem.md) |
| **OpenDataLoader PDF** | Java PDF extraction with page coordinates, optional Docling triage and Tagged PDF output. | B (6/6) | [→](opendataloader-pdf.md) |
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | A (5/6) | [→](docling.md) |
| **MarkItDown** | Use it when an agent or RAG pipeline must turn mixed Office files, HTML, EPUB and simple PDFs into Markdown with one lightweight Python call — but scanned or complex-layout PDFs need Marker or Docling, since it has no OCR or layout model. | B (6/6) | [→](markitdown.md) |
| **unstructured** | Use it when a RAG pipeline over mixed PDFs, emails and Office files needs typed elements with page metadata and section-aware chunking rather than one Markdown string — but its open-source PDF table accuracy trails Docling and Marker, and analytics pings are on by default. | A (6/6) | [→](unstructured.md) |
| **any2html** | Use it when you need any2html in this category. | D (4/5) | [→](any2html.md) |
| **Dedoc** | Use it when an on-premises Python pipeline needs multi-format documents recovered as logical trees with tables, annotations, and attachments; expect a heavy Linux/system-package stack and limits on difficult scans. | B (5/6) | [→](dedoc.md) |
| **Bella Domify** | Use it when Chinese RAG ingestion needs detailed PDF/Office DOM trees plus FastAPI/Kafka/S3 service integration; license ambiguity, optional remote OCR, and heavy infrastructure are decisive constraints. | C (5/6) | [→](bella-domify.md) |
| **MinerU Skill** | Use it when a coding agent needs one-command cloud document-to-Markdown through CLI/MCP, with batch, resume, or content-tool delivery; files cross a service boundary and remain subject to quotas and API changes. | C (5/6) | [→](mineru-skill.md) |
| **anydoc** | Use it when a pipeline gets a mixed pile of Office (incl. legacy .doc/.ppt/.xls), OpenDocument, RTF, EPUB and text-PDF files and needs one consistent Markdown in milliseconds with no LibreOffice or models; no OCR — scanned pages fail. | B (6/6) | [→](anydoc.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [ContextGem](contextgem.md) | Indexed | C (5/6) | Semantic schema extraction after conversion, not OCR or retrieval; checked types and reference IDs do not prove answer correctness. |
| [OpenDataLoader PDF](opendataloader-pdf.md) | ✅ | B (6/6) | CPU Java baseline and optional model backend; PDF-only, PDF/UA export is enterprise. |
| [Docling](docling.md) | ✅ | A (5/6) | Rich-document parsing (layout + tables) to structured Markdown/JSON; heavier model deps than plain text extraction. |
| [MarkItDown](markitdown.md) | ✅ | B (6/6) | Broad format coverage with no GPU or model download, at the cost of layout fidelity and optional features that send files to external LLMs or Azure. |
| [PageIndex](../rag-retrieval/structured-retrieval/pageindex.md) | ✅ | B (6/6) | Builds a retrieval index over long structured docs — downstream of parsing, not a parser. |
| [any2html](any2html.md) | ✅ | D (4/5) | Use it when you need any2html in this category. |
| [Dedoc](dedoc.md) | ✅ | B (5/6) | Multi-format logical-tree parsing with tables, annotations, and attachments; deeper than lightweight Markdown conversion, but heavier on Linux dependencies and limited on difficult scans. |
| [Bella Domify](bella-domify.md) | ✅ | C (5/6) | Detailed pdf2docx-derived DOM trees and service hooks; rich layout objects, but heavy infrastructure, optional outbound OCR, and an unresolved GPL v2/v3 declaration conflict. |
| [MinerU Skill](mineru-skill.md) | ✅ | C (5/6) | Agent-facing CLI/MCP over MinerU's cloud API with batch, resume, and delivery; avoids local model deployment but adds upload, quota, and third-party API risk. |
| [anydoc](anydoc.md) | ✅ | B (6/6) | Pure-Rust converter for 20+ office/ebook/PDF extensions with Node/Python/WASM bindings; fast and dependency-free, but no OCR, heuristic PDF tables, and a young single-author 0.x project. |
| LlamaParse / self-hosted MinerU | 未收录 | — | Cloud and self-hosted document-parsing routes named across the pages. |


## What belongs here

Libraries whose primary job is **parsing/converting documents into structured representations** for gen-AI/RAG. Not retrieval/indexing itself (see `rag-retrieval`), not document archiving/search (see `document-management`), not raw OCR (see `ocr`).

Keep mixed-format conversion, broader document trees and cloud-facing agent wrappers at this node. Descend into [model-backed PDF parsing](model-backed-pdf/INDEX.md) when the primary route is PDF/image layout and recognition with models; having any optional model path does not by itself require moving a broader converter there.
