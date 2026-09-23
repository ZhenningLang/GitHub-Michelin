---
name: MarkItDown
slug: markitdown
repo: https://github.com/microsoft/markitdown
category: document-parsing
tags: [document-conversion, markdown, pdf, office, llm-ingestion, python]
language: Python
license: MIT
maturity: v0.x, active, 162k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-06-24T15:32:46Z
  default_branch: main
  default_branch_sha: e144e0a2be95b34df17433bac904e635f2c5e551
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:18:04Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 66.6
        qualifying_issues: 36
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: markitdown
        dependent_repos_count: 0
        downloads_last_month: 14692950
        graph_tier: E
        volume_tier: A
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 678
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 54
        top1_share: 0.445
        top3_share: 0.533
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# MarkItDown

A lightweight Python library for converting various files and office documents to Markdown, designed for LLM ingestion and text-analysis pipelines rather than high-fidelity human consumption.

![MarkItDown — health radar](../../assets/health/markitdown.svg)

## When to use

You're building a RAG pipeline, a document QA system, or an agent that needs to consume PDFs, Word documents, PowerPoint slides, Excel sheets, images, audio files, and HTML pages as structured text. You pick MarkItDown over [Docling](docling.md) when you want a lightweight, pip-installable library with zero ML model dependencies and a simple `convert()` API, whereas Docling pulls in heavier dependencies for structured layout analysis. You pick it over unstructured.io when you need a local, free, MIT-licensed solution without enterprise licensing tiers or cloud dependencies. You pick it over Marker or LlamaParse when you need breadth across formats — not just PDF, but Office, audio, images, and HTML — in a single library. You install via pip, call `convert()` on a file path, and get back clean Markdown with headings, lists, tables, and links preserved so your LLM can process them without being overwhelmed by binary noise or proprietary formatting.

## When NOT to use

- **If you need high-fidelity document conversion for human reading** — use [Docling](docling.md) or a dedicated PDF-to-Word converter instead of MarkItDown, because MarkItDown flattens complex layouts and optimizes output for LLM consumption, which can make results less presentable for human readers.
- **If you need document editing or round-tripping** — use python-docx, PyMuPDF, or a document manipulation library directly instead of MarkItDown, because MarkItDown is one-way conversion (file → Markdown) and cannot write back to the original format.
- **If you need precise layout, merged cells, and nested table preservation** — use Docling instead of MarkItDown, because Docling models document structure and layout with higher fidelity, whereas MarkItDown simplifies tables and flattens layouts for Markdown output. [未验证]
- **If you process untrusted inputs in a multi-tenant environment** — use a sandboxed conversion service or an LLM parsing API instead of MarkItDown, because MarkItDown performs I/O with the privileges of the current process and can access any resource the process can reach. [未验证]
- **If OCR is your primary use case** — use Tesseract, PaddleOCR, or a dedicated OCR pipeline instead of MarkItDown, because MarkItDown's image OCR is convenience-level and not as mature or configurable as specialized OCR libraries.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Docling](docling.md) | ✅ | Rich-document parsing with layout + tables to structured Markdown/JSON. | Docling is heavier with model dependencies and focuses on structured output; MarkItDown is lighter and simpler, built for LLM ingestion. |
| unstructured.io | 未收录 | Enterprise-grade document parsing with chunking and embedding pipelines. | More mature ecosystem and cloud offerings; heavier dependencies and potential licensing costs for enterprise features. |
| LlamaParse | 未收录 | Parsing service from LlamaIndex with a hosted API. | Cloud-based, API-key required, good for complex PDFs; MarkItDown is local, free, and open-source. |
| [Marker](marker.md) | ✅ | Fast PDF-to-Markdown converter optimized for academic papers. | Specializes in PDF and claims high accuracy on research papers; MarkItDown covers more formats (Office, audio, HTML, etc.). |
| [PyMuPDF](../pdf-tools/pymupdf.md) | ✅ | Low-level Python PDF library for extraction and manipulation. | A library for direct PDF page manipulation, not a high-level Markdown converter; more powerful but requires more code. |
| textract | 未收录 | Python library for extracting text from many formats. | Older project with broader format support but less focus on Markdown structure preservation for LLMs. |

## Tech stack

- **Python** — primary implementation language
- **Modular converter architecture** — separate converters per format (PDF, DOCX, PPTX, XLSX, images, audio, HTML, etc.)
- **Markdown output** — unified target format for all conversions

## Dependencies

- **Python 3.9+** — runtime environment
- **Optional format-specific dependencies** — some converters require additional packages (e.g., for OCR, audio transcription, or advanced PDF parsing)
- **No service or database** — pure library; runs in-process

## Ops difficulty

**Low.** `pip install markitdown` and import. The library is stateless and runs in-process; there is no service to deploy, no database to manage, and no persistent infrastructure. The main operational concern is keeping the Python environment and optional dependencies current, plus the input-sanitization discipline mentioned in the security notes.

## Health & viability
- **Maintenance**: Grade B — 3/13 active weeks in trailing 13; last commit 37 days ago.
- **Responsiveness**: Grade A — median first-response time 37.3 hours across 32 qualifying issues/PRs.
- **Adoption**: Grade A — 10,869,537 monthly downloads via pypi.org (package: markitdown).
- **Longevity**: Grade C — 597 days old.
- **Governance**: Grade A — top-3 contributor share 53.6% (?).
- **Risk / License**: Grade A — MIT license.
## Caveats (unverified)

- [未验证] The Microsoft AutoGen team authorship is stated in the README badge; the exact team structure and long-term maintenance commitment are not publicly documented.
- [未验证] Output quality varies significantly by format and document complexity; the "Markdown is optimized for LLMs" disclaimer means human readability is explicitly a secondary goal.
- [未验证] The security note about I/O privileges and input sanitization should be treated as a real operational concern in multi-tenant or untrusted-input environments.
- [推断] The 162k star count on an 8-month-old project is likely amplified by the Microsoft brand and the 2024–2025 LLM-tooling hype cycle.
- [未验证] Support for audio transcription and image OCR may require additional external dependencies (e.g., Whisper, Tesseract) that are not bundled by default.
