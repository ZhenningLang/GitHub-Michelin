# media-processing

> Category node. Decode, encode, transcode, filter, and score images, audio, and video.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Category | Use when | Route |
|---|---|---|
| **video-audio** | Audio/video tooling below the application layer — codec/transcode pipelines, programmatic editing and cutting, speech/subtitles (three leaves). | [→](video-audio/INDEX.md) |
| **video-editing** | End-user non-linear video editors (NLE apps) — GUI timeline editing, the application layer above the codec toolchain. | [→](video-editing/INDEX.md) |
| **nle-automation** | Programmatic control of an existing video editor — generate, mutate, and headlessly export its native project/draft files through the editor's own engine. | [→](nle-automation/INDEX.md) |
| **image-processing** | Image processing, conversion, resizing, and format tooling. | [→](image-processing/INDEX.md) |
| **quality-metrics** | Perceptual media quality metrics and benchmarking tools. | [→](quality-metrics/INDEX.md) |

## Projects

- [Jasna](jasna.md) — Restore tracked mosaic regions in local videos; free public BasicVSR++ path, with private supporter components in official packages.

## Comparison matrix

| Project | Use when | Main constraint | Health |
|---|---|---|---|
| [Jasna](jasna.md) | Moving mosaic regions need detection, tracking and temporal restoration together. | GPU-specific setup; mixed component terms and opaque supporter runtime. | C (6/6) |

## What belongs here

Decode, encode, transcode, filter, and score images, audio, and video.
