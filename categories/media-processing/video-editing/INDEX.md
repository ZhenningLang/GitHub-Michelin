# video-editing

> Category node. End-user non-linear video editors (NLE apps) — a GUI timeline for cutting, trimming, composing, and exporting, as opposed to codec toolchains and programmatic rendering libraries.
> ← back to [media-processing](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Concat** | Use when you want a native, offline, scriptable CapCut-style editor you can install and run today — accepting a 25-day-old 0.2.x beta with a single maintainer. | C (6/6) | [→](concat.md) |
| **OpenCut** | Use when you want to track or build on the browser/WASM rewrite architecture — not when you need a working editor, because the repository is mid-rewrite and the shipped version lives in an archived classic repo. | B (5/6) | [→](opencut.md) |
| **Palmier Pro** | Use when an agent (Claude Code, Codex, Cursor) should edit the timeline you have open on a macOS 26 Apple Silicon Mac through a local MCP server — knowing only the source through v0.7.6 is GPL and later builds are proprietary. | C (6/6) | [→](palmier-pro.md) |
| **OpenScreen** | Use when you want the Screen-Studio-style demo for free — record the screen and get cursor-following zooms, smoothed cursor, backgrounds, on-device captions, MP4/GIF export — accepting that the upstream was archived in 2026-06 and maintenance moved to a community fork. | C (6/6) | [→](openscreen.md) |
| **EffectCraft** | Use when you want After Effects-style motion graphics (layers, keyframes, expressions, 306 named effects, Lottie export) for free or driven by an agent over MCP — accepting an 8-day-old, mostly agent-written app that cannot open `.aep` and whose fidelity to After Effects is unmeasured. | B (5/6) | [→](effectcraft.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Concat](concat.md) | ✅ | C (6/6) | Pick for a native Rust desktop/mobile editor that bundles FFmpeg and Whisper and exposes an API/CLI/server; the price is beta stability and a one-person bus factor. |
| [OpenCut](opencut.md) | ✅ | B (5/6) | Pick to follow or build on the next-generation browser/WASM architecture; the price is that this repository currently ships nothing while the rewrite is in progress. |
| [Palmier Pro](palmier-pro.md) | ✅ | C (6/6) | Pick for agent editing over MCP on a real Mac timeline plus built-in generation; the price is macOS 26 + Apple Silicon only, vendor-backend generation, and an open-source line frozen since 2026-08. |
| [OpenScreen](openscreen.md) | ✅ | C (6/6) | Pick for the free, local, auto-polished screen-demo pipeline (record → cursor-following zooms → MP4/GIF); the price is an archived upstream — fixes now depend on the community fork. |
| [EffectCraft](effectcraft.md) | ✅ | B (5/6) | Pick for an After Effects-style motion-graphics compositor with Lottie export, readable JSON projects and an MCP/CLI surface, with no FFmpeg; the price is a week-old codebase, no `.aep` import and unmeasured parity. |
| CapCut (ByteDance) | 未收录 | — | Pick for a free, polished editor with cloud AI features; the price is closed source, account-bound uploads, Pro paywalls, and no self-hosting. |
| DaVinci Resolve | 未收录 | — | Pick for professional colour, masks, and tracking on a one-off edit; the price is a large proprietary application outside a normal desktop. |

## What belongs here

End-user non-linear video editors with a GUI timeline — applications a person cuts in, not libraries that render for them. Timeline-based motion-graphics compositors in the After Effects mould (EffectCraft) live here too. Codec/transcode toolchains and editing frameworks belong under `video-audio` (FFmpeg, MLT, GStreamer); programmatic rendering engines belong under `video-production` (Remotion, HyperFrames).
