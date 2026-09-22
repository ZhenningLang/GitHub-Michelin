# ocr

> Category node. Optical character recognition engines — image/scan to text.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Tesseract** | Use it when you need offline, embeddable OCR over clean printed text in 100+ languages — not wild photos or handwriting. | A (5/6) | [→](tesseract.md) |
| **LaTeX-OCR (pix2tex)** | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. | C (3/6) | [→](latex-ocr.md) |
| **Laravel OCR** | Use it when an existing Laravel application needs one wrapper for Tesseract and cloud OCR plus template/regex extraction and persistence; not for multi-page scanned PDFs or layout-aware OCR, and the repository lacks a license file. | D (5/6) | [→](laravel-ocr.md) |
| **PaddleOCR** | Use it when messy input needs modern detection-plus-recognition, CJK strength, or layout/table structure — and you can carry PaddleX, inference engines and model downloads. | A (5/6) | [→](paddleocr.md) |
| **EasyOCR** | Use it when a PyTorch OCR stack with good scene-text defaults beats building preprocessing yourself — the project's last real release was 2024-09. | B (5/6) | [→](easyocr.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Tesseract](tesseract.md) | ✅ | A (5/6) | Mature offline OCR engine for clean printed text; weak on layout, handwriting, in-the-wild photos. |
| [LaTeX-OCR (pix2tex)](latex-ocr.md) | ✅ | C (3/6) | Use it when you must convert images of math equations into LaTeX (pix2tex) — equations only, idle/coasting, and VLMs may beat it. |
| [Laravel OCR](laravel-ocr.md) | ✅ | D (5/6) | Laravel-native OCR driver switching plus template/regex business extraction; saves application plumbing but has shallow PDF/layout handling, incomplete workflows, and no repository license text. |
| [PaddleOCR](paddleocr.md) | ✅ | A (5/6) | Deep-learning OCR plus document structure and a VLM path; the widest capability surface here, and the heaviest dependency chain (PaddleX, inference engines, model downloads). |
| [EasyOCR](easyocr.md) | ✅ | B (5/6) | Ready-to-use PyTorch OCR for 80+ languages with good scene-text defaults; the last real release is 2024-09 and ~55 PRs sit unmerged, so read it as drifting rather than stable. |
| TrOCR | 未收录 | — | A recognized research model line for cropped text lines; the name has not been pinned to a canonical repository yet. |
| Cloud Vision / Textract | 非仓库 | — | Hosted commercial OCR APIs (Google, AWS): no source, no self-hosting, per-page billing. |

## What belongs here

Engines/libraries whose primary job is **recognizing text in images/scans**. Not document layout-and-table parsing for gen-AI (see `document-parsing`), not document archiving/search (see `document-management`).
