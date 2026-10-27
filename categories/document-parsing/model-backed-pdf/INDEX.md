# model-backed-pdf

> Category node. PDF/image-focused parsing paths that use models for layout, OCR or page recognition.
> ← back to [document parsing](../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OXR** | Parse scientific PDF/images with a replaceable layout detector and typed Markdown/JSON output; requires a GPU stack and custom commercial-license clearance. | C (3/6) | [→](oxr.md) |
| **olmOCR** | Use it when you are turning thousands to millions of PDFs with equations, tables and multi-column layouts into clean reading-order Markdown for an LLM corpus — but local runs need a 12 GB+ NVIDIA GPU, and upstream has been quiet since 2026-03. | C (5/6) | [→](olmocr.md) |
| **Marker** | Use it when converting thousands of PDFs (papers, textbooks, scans) into Markdown with real tables, LaTeX math and selective OCR on your own hardware — but the model weights are free only below a $5M funding or revenue threshold. | B (6/6) | [→](marker.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OXR](oxr.md) | ✅ | C (3/6) | Separate layout detection plus OXR recognition/reading order; Linux/NVIDIA, executable model plugin, in-memory jobs, and commercial restrictions. |
| [olmOCR](olmocr.md) | ✅ | C (5/6) | Buys VLM-grade fidelity on equations and messy scans; costs GPU inference per page, versus cheaper CPU-only Docling or PyMuPDF when layout fidelity matters less. |

## What belongs here

PDF/image-focused model-backed layout, OCR and page-recognition pipelines. A model may process every page or only the regions that need recognition. Mixed-format converters, broader document trees and cloud-facing agent wrappers remain in the [parent category](../INDEX.md); raw OCR engines remain under [OCR](../../ocr/INDEX.md).
