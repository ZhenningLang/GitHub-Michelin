# computer-vision

> Category node. Detect, recognize and analyze faces, objects and people in images and video — libraries and models you call from your own code.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **DeepFace** | Use it when you want face verification (same person?) and 1:N face search from one Python call with swappable models and pre-tuned thresholds — but wrapped weights inherit their own licences (Buffalo_L is non-commercial), TensorFlow is always installed, and race/emotion analysis is restricted under the EU AI Act. | B (6/6) | [→](deepface.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [DeepFace](deepface.md) | ✅ | B (6/6) | One API over 11 face-recognition models and ~20 detectors with shipped thresholds, a REST/gRPC server and DB-backed search — single maintainer, 0.0.x versioning, inherited weight licences. |
| InsightFace / face_recognition / CompreFace / facenet-pytorch | 未收录 | — | Face-recognition substitutes named on the DeepFace page; not added in this tab-intake batch. |

## What belongs here

**Computer-vision libraries and models** that find, recognize or describe things in images and video — face verification and recognition, face/object detection, pose and attribute analysis — used as building blocks in your own code. Image-to-text is in `ocr`; photo/video-to-3D is in `3d-reconstruction`; single research-model releases such as depth or CLIP sit in `ml-research`.
