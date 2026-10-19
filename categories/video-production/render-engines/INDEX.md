# render-engines

> Category node. You already own the script, assets and production method, and need code-defined compositions rendered into video.
> ← back to [video-production](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **fframes** | Use it when code- or agent-authored motion graphics must render fast on your own GPU with no browser in the loop — Rust + SVG frames, linked libav, a per-project CLI that checks frames and loudness for an author that cannot watch — MIT, but a native toolchain, 1.0 only since 2026-09-28 and a single maintainer. | B (4/6) | [→](fframes.md) |
| **Remotion** | Use it when a React-first team needs proven programmatic video — compositions as React components with a mature Lambda cloud renderer — under a source-available license free for ≤3-employee companies. | A (4/6) | [→](remotion.md) |
| **HyperFrames** | Use it when you need deterministic, code-form video — HTML compositions rendered to MP4 in CI — with agent skills covering the production loop; it is a rendering engine, not a generative video model. | B (6/6) | [→](hyperframes.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [fframes](fframes.md) | ✅ | B (4/6) | Rust + SVG frames drawn by Skia on the GPU and encoded through linked libav, with inspect/strip/audio-analyze commands for agents; MIT and ~1.5× faster than Remotion's best in its own benchmark, paid for in a native build toolchain, no cloud renderer, 1.0 two days old, bus factor 1. |
| [Remotion](remotion.md) | ✅ | A (4/6) | React-component authoring and a mature Lambda renderer, under a source-available license with a company-size threshold; OpenMontage embeds engines of this class. |
| [HyperFrames](hyperframes.md) | ✅ | B (6/6) | Deterministic HTML-to-MP4 rendering with 20 agent skills and Apache-2.0 licensing; the engine layer, not a governed pipeline and not generative footage. |

## What belongs here

Code-defined composition and frame-rendering engines, including HTML, React and Rust/SVG routes. Directing skills, production pipelines and finished creator apps stay in [video-production](../INDEX.md). Traditional codecs and NLE automation belong in [media-processing](../../media-processing/INDEX.md).
