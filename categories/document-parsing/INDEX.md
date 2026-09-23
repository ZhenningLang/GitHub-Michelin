# document-parsing

> Category node. Parse/convert documents (PDF/DOCX/…) into structured Markdown/JSON for gen-AI ingestion.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Docling** | Use it when you must parse messy PDF/DOCX/PPTX into clean structured Markdown/JSON for RAG ingestion — a parser, not a DMS. | A (6/6) | [→](docling.md) |
| **MarkItDown** | Use it when you need a lightweight Python library to convert various office documents and files to Markdown for LLM ingestion — simpler than Docling but less layout-aware. | B (6/6) | [→](markitdown.md) |
| **olmOCR** | Use it when you must convert complex PDFs with equations, tables, handwriting, and multi-column layouts into clean Markdown for LLM training datasets — requires a GPU. | C (5/6) | [→](olmocr.md) |
| **Marker** | Convert PDF to markdown + JSON quickly with high accuracy | B (5/6) | [→](marker.md) |
| **unstructured** | Convert documents to structured data effortlessly. Unstructured is open-source ETL solution for transforming complex documents into clean, structured formats for language models.  Visit our website to learn more about our enterprise grade Platform product for production grade workflows, partitioning, enrichments, chunking and embedding. | A (6/6) | [→](unstructured.md) |
| **any2html** | Use it when you need any2html in this category. | D (5/6) | [→](any2html.md) |
| **Dedoc** | Use it when an on-premises Python pipeline needs multi-format documents recovered as logical trees with tables, annotations, and attachments; expect a heavy Linux/system-package stack and limits on difficult scans. | B (5/6) | [→](dedoc.md) |
| **Bella Domify** | Use it when Chinese RAG ingestion needs detailed PDF/Office DOM trees plus FastAPI/Kafka/S3 service integration; license ambiguity, optional remote OCR, and heavy infrastructure are decisive constraints. | C (5/6) | [→](bella-domify.md) |
| **MinerU Skill** | Use it when a coding agent needs one-command cloud document-to-Markdown through CLI/MCP, with batch, resume, or content-tool delivery; files cross a service boundary and remain subject to quotas and API changes. | C (5/6) | [→](mineru-skill.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Docling](docling.md) | ✅ | A (6/6) | Rich-document parsing (layout + tables) to structured Markdown/JSON; heavier model deps than plain text extraction. |
| [MarkItDown](markitdown.md) | ✅ | B (6/6) | Lightweight Python library converting office documents and files to Markdown for LLM ingestion; simpler than Docling but less layout-aware. |
| [olmOCR](olmocr.md) | ✅ | C (5/6) | VLM-based PDF linearization for LLM datasets; handles equations, tables, and handwriting but requires GPU. |
| [PageIndex](../rag-retrieval/pageindex.md) | ✅ | B (6/6) | Builds a retrieval index over long structured docs — downstream of parsing, not a parser. |
| [any2html](any2html.md) | ✅ | D (5/6) | Use it when you need any2html in this category. |
| [Dedoc](dedoc.md) | ✅ | B (5/6) | Multi-format logical-tree parsing with tables, annotations, and attachments; deeper than lightweight Markdown conversion, but heavier on Linux dependencies and limited on difficult scans. |
| [Bella Domify](bella-domify.md) | ✅ | C (5/6) | Detailed pdf2docx-derived DOM trees and service hooks; rich layout objects, but heavy infrastructure, optional outbound OCR, and an unresolved GPL v2/v3 declaration conflict. |
| [MinerU Skill](mineru-skill.md) | ✅ | C (5/6) | Agent-facing CLI/MCP over MinerU's cloud API with batch, resume, and delivery; avoids local model deployment but adds upload, quota, and third-party API risk. |
| LlamaParse / self-hosted MinerU | 未收录 | — | Cloud and self-hosted document-parsing routes named across the pages. |


## What belongs here

Libraries whose primary job is **parsing/converting documents into structured representations** for gen-AI/RAG. Not retrieval/indexing itself (see `rag-retrieval`), not document archiving/search (see `document-management`), not raw OCR (see `ocr`).
