# video-editing

> Category node. End-user non-linear video editors (NLE apps) — a GUI timeline for cutting, trimming, composing, and exporting, as opposed to codec toolchains and programmatic rendering libraries.
> ← back to [media-processing](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Concat** | Use when you want a native, offline, scriptable CapCut-style editor you can install and run today — accepting a 25-day-old 0.2.x beta with a single maintainer. | C (5/6) | [→](concat.md) |
| **OpenCut** | Use when you want to track or build on the browser/WASM rewrite architecture — not when you need a working editor, because the repository is mid-rewrite and the shipped version lives in an archived classic repo. | B (5/6) | [→](opencut.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Concat](concat.md) | ✅ | C (5/6) | Pick for a native Rust desktop/mobile editor that bundles FFmpeg and Whisper and exposes an API/CLI/server; the price is beta stability and a one-person bus factor. |
| [OpenCut](opencut.md) | ✅ | B (5/6) | Pick to follow or build on the next-generation browser/WASM architecture; the price is that this repository currently ships nothing while the rewrite is in progress. |
| CapCut (ByteDance) | 未收录 | — | Pick for a free, polished editor with cloud AI features; the price is closed source, account-bound uploads, Pro paywalls, and no self-hosting. |
| DaVinci Resolve | 未收录 | — | Pick for professional colour, masks, and tracking on a one-off edit; the price is a large proprietary application outside a normal desktop. |

## What belongs here

End-user non-linear video editors with a GUI timeline — applications a person cuts in, not libraries that render for them. Codec/transcode toolchains and editing frameworks belong under `video-audio` (FFmpeg, MLT, GStreamer); programmatic rendering engines belong under `video-production` (Remotion, HyperFrames).
