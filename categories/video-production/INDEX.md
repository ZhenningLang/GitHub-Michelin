# video-production

> Category node. AI-orchestrated end-to-end video production — research, scripting, asset generation, composition, and rendering driven by an agent inside a coding assistant.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenMontage** | Use it when you want an AI coding assistant to produce full videos — explainers, trailers, animations, or documentary montages — from a plain-language prompt through research, scripting, asset generation, and render. | C (6/6) | [→](open-montage.md) |
| **HyperFrames** | Use it when you need deterministic, code-form video — HTML compositions rendered to MP4 in CI — with agent skills covering the production loop; it is a rendering engine, not a generative video model. | B (6/6) | [→](hyperframes.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenMontage](open-montage.md) | ✅ | C (6/6) | Use it when you want an AI coding assistant to produce full videos — explainers, trailers, animations, or documentary montages — from a plain-language prompt through research, scripting, asset generation, and render. |
| [HyperFrames](hyperframes.md) | ✅ | B (6/6) | Deterministic HTML-to-MP4 rendering with 20 agent skills and Apache-2.0 licensing; the engine layer, not a governed pipeline and not generative footage. |
| Remotion | 未收录 | — | React-component authoring and a mature Lambda renderer, under a source-available license with a revenue threshold; OpenMontage embeds engines of this class. |
| Runway / Pika / HeyGen | 未收录 | — | Closed-source SaaS — faster one-click generation but no pipeline customization, no agent approval gates, no open-source extensibility. |
| DaVinci Resolve / Premiere Pro | 未收录 | — | Professional NLEs — human editors, not agent-driven; the right tool when you need frame-level manual control and a traditional post-production team. |


## What belongs here

Tools and frameworks whose primary job is **agent-driven or AI-orchestrated video production** — end-to-end pipelines that go from prompt/idea to finished video through research, scripting, asset generation, composition, and rendering. Includes multi-pipeline systems with quality gates, provider selection, and budget governance. Not traditional media processing frameworks (see `media-processing`), not standalone video-generation SaaS landing pages, and not general design/HTML generators (see `ai-design-generation`).
