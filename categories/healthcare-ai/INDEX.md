# healthcare-ai

> Category node. Clinical text intelligence you run yourself — medical entity extraction and PHI/PII de-identification on your own hardware, for data that cannot leave the network.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenMed** | Use it when clinical notes must yield typed entities and a redacted copy without patient data ever leaving your network — accepting per-model validation on your own corpus and a single-maintainer release cadence. | B (5/6) | [→](openmed.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenMed](openmed.md) | ✅ | B (5/6) | Local-first clinical NER + PHI de-identification SDK with a 2,266-row model registry spanning CPU/CUDA/MLX/ONNX/mobile; validate every model yourself, and pin versions against a one-person release cadence. |

## What belongs here

Software whose subject is **clinical/medical text and health data**: entity extraction from notes, PHI/PII de-identification, FHIR/HL7 interop, phenotyping and coding pipelines you can run on your own hardware. Not general PII frameworks with no medical models (Presidio-class), not document OCR or PDF parsing (see [ocr](../ocr/INDEX.md) and [document-parsing](../document-parsing/INDEX.md)), not general inference runtimes (see [on-device-ml](../on-device-ml/INDEX.md)), and not hosted medical NLP APIs (not repositories).
