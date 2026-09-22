# video-production

> Category node. AI-orchestrated end-to-end video production — research, scripting, asset generation, composition, and rendering driven by an agent inside a coding assistant.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenMontage** | Use it when you want an AI coding assistant to produce full videos — explainers, trailers, animations, or documentary montages — from a plain-language prompt through research, scripting, asset generation, and render. | C (6/6) | [→](open-montage.md) |
| **HyperFrames** | Use it when you need deterministic, code-form video — HTML compositions rendered to MP4 in CI — with agent skills covering the production loop; it is a rendering engine, not a generative video model. | B (6/6) | [→](hyperframes.md) |
| **anything2explainer** | Use it when you want a Claude Code / Codex skill to turn a topic into a narrated motion-graphics explainer video (Chinese or English) through a governed 9-stage multi-agent pipeline with human checkpoints and quantitative QC — fixed black-canvas style, PolyForm noncommercial license. | C (3/6) | [→](anything2explainer.md) |
| **Hypit** | Use it when your agent should clone a specific viral video into an editable, word-anchored SVML workflow and ship batch variants by swapping face/words/B-roll — agent-first, non-OSI license, very young. | B (3/6) | [→](hypit.md) |
| **Remotion** | Use it when a React-first team needs proven programmatic video — compositions as React components with a mature Lambda cloud renderer — under a source-available license free for ≤3-employee companies. | A (4/6) | [→](remotion.md) |
| **MoneyPrinterTurbo** | Use it when you need a self-hosted MIT appliance (WebUI + API) that turns topics into narrated stock-footage shorts at near-zero marginal cost — no cloning, no agent required. | A (4/6) | [→](moneyprinter-turbo.md) |
| **video-shotcraft** | Use it when a coding agent should turn your product or webpage into a cinematic promo — 150+ shot recipe cards, a validated 36.2s Remotion template, real page captures, 2.5D camera moves and beat-synced SFX — rendered locally; ~2 months old, no tagged releases, and it targets Remotion's eligibility-gated license. | B (4/6) | [→](video-shotcraft.md) |
| **OpenCreator** | Use it when a bilingual channel or localization desk needs one local desktop for subtitling, dubbing, and recutting *this* video — plus writing and generation in the same project — and you already have a Codex login; not a from-scratch film pipeline and not Linux Desktop. | A (5/6) | [→](open-creator.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenMontage](open-montage.md) | ✅ | C (6/6) | Use it when you want an AI coding assistant to produce full videos — explainers, trailers, animations, or documentary montages — from a plain-language prompt through research, scripting, asset generation, and render. |
| [HyperFrames](hyperframes.md) | ✅ | B (6/6) | Deterministic HTML-to-MP4 rendering with 20 agent skills and Apache-2.0 licensing; the engine layer, not a governed pipeline and not generative footage. |
| [anything2explainer](anything2explainer.md) | ✅ | C (3/6) | A Claude Code / Codex skill-pack with a full explainer-film method (research → narration → storyboard → parallel build → QC) and a reference film as the quality bar; fixed MG style, 8 days old, PolyForm noncommercial. |
| [video-shotcraft](video-shotcraft.md) | ✅ | B (4/6) | Pick it when the film is a product promo built from real UI captures with a shot library supplying the taste — but it ships Remotion compositions, so the engine's ≤3-employee licence gate travels with your deliverable, and nothing is tagged. |
| [Remotion](remotion.md) | ✅ | A (4/6) | React-component authoring and a mature Lambda renderer, under a source-available license with a company-size threshold; OpenMontage embeds engines of this class. |
| [Hypit](hypit.md) | ✅ | B (3/6) | Agent-first viral-video cloning into word-anchored SVML workflows with pluggable generation providers; non-OSI license, 7 weeks old at verification, generation runs bill to paid model APIs. |
| [MoneyPrinterTurbo](moneyprinter-turbo.md) | ✅ | A (4/6) | Topic → narrated stock-footage shorts as a MIT WebUI/API appliance; near-zero marginal cost, generic output, single-maintainer bus factor. |
| [OpenCreator](open-creator.md) | ✅ | A (5/6) | Local Codex-native creator desktop whose shipped strength is translation/dubbing/portrait recut of an existing video; generation and writing share the same project. Codex login required, no Linux Desktop, nested GPL KrillinAI core. |
| Runway / Pika / HeyGen | 未收录 | — | Closed-source SaaS — faster one-click generation but no pipeline customization, no agent approval gates, no open-source extensibility. |
| DaVinci Resolve / Premiere Pro | 未收录 | — | Professional NLEs — human editors, not agent-driven; the right tool when you need frame-level manual control and a traditional post-production team. |


## What belongs here

Tools and frameworks whose primary job is **agent-driven or AI-orchestrated video production** — end-to-end pipelines that go from prompt/idea to finished video through research, scripting, asset generation, composition, and rendering. Includes multi-pipeline systems with quality gates, provider selection, and budget governance. Not traditional media processing frameworks (see `media-processing`), not standalone video-generation SaaS landing pages, and not general design/HTML generators (see `ai-design-generation`).
