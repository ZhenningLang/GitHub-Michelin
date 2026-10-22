# video-production

> Category node. Agent-driven video directing methods, production pipelines and creator apps; code-defined composition engines have their own child category.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **render-engines** | You already own the script, assets and production method, and need code-defined compositions rendered into video. | [→](render-engines/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **We-Video** | Reuse a narration/audio/visual review workbench and checked MP4 renderer; first complete missing job API handlers and account inputs. | C (4/6) | [→](we-video.md) |
| **Stickman Video Director** | Approve a stick-figure storyboard and get standalone continuity prompts; generation and editing stay external. | C (4/5) | [→](stickman-video-director.md) |
| **huashu-art-motion** | Agent-directed art animation with shot rules, Canvas scenes and measured film gates. | C (5/6) | [→](huashu-art-motion.md) |
| **shuohao-skills** | Your generated drama keeps changing who sits where between shots; this collection turns a novel into shared character, art, script, staging and storyboard records before production. | C (5/6) | [→](shuohao-skills.md) |
| **OpenMontage** | Use it when you want an AI coding assistant to produce full videos — explainers, trailers, animations, or documentary montages — from a plain-language prompt through research, scripting, asset generation, and render. | B (5/6) | [→](open-montage.md) |
| **anything2explainer** | Use it when you want a Claude Code / Codex skill to turn a topic into a narrated motion-graphics explainer video (Chinese or English) through a governed 9-stage multi-agent pipeline with human checkpoints and quantitative QC — fixed black-canvas style, PolyForm noncommercial license. | C (3/5) | [→](anything2explainer.md) |
| **Hypit** | Use it when your agent should clone a specific viral video into an editable, word-anchored SVML workflow and ship batch variants by swapping face/words/B-roll — agent-first, non-OSI license, very young. | C (4/6) | [→](hypit.md) |
| **MoneyPrinterTurbo** | Use it when you need a self-hosted MIT appliance (WebUI + API) that turns topics into narrated stock-footage shorts at near-zero marginal cost — no cloning, no agent required. | B (6/6) | [→](moneyprinter-turbo.md) |
| **video-shotcraft** | Use it when a coding agent should turn your product or webpage into a cinematic promo — 150+ shot recipe cards, a validated 36.2s Remotion template, real page captures, 2.5D camera moves and beat-synced SFX — rendered locally; ~2 months old, no tagged releases, and it targets Remotion's eligibility-gated license. | B (5/6) | [→](video-shotcraft.md) |
| **OpenCreator** | Use it when a bilingual channel or localization desk needs one local desktop for subtitling, dubbing, and recutting *this* video — plus writing and generation in the same project — and you already have a Codex login; not a from-scratch film pipeline and not Linux Desktop. | B (6/6) | [→](open-creator.md) |
| **video-use** | Use it when a coding agent should cut a folder of raw takes from a packed transcript — confirm the plan, then ffmpeg — not generate footage; needs ElevenLabs Scribe, 22 commits under 27k stars. | B (4/5) | [→](video-use.md) |
| **SeeCut** | Use it when a coding agent should polish your talking-head or AI-avatar A-roll into a high-energy motion short — real evidence screenshots on screen, every version gated by a video-native judge (Gemini via Antigravity CLI) — delivered as MP4 plus an editable JianYing layered draft; PolyForm noncommercial, 4 days old at verification. | D (4/6) | [→](seecut.md) |
| **Lemo-Opuscar** | Have a coding agent direct style-led films with deterministic browser frames, sound and reading-time checks; code MIT, gallery media CC BY. | C (4/6) | [→](lemo-opuscar.md) |
| **ArtCraft** | Stage a camera and character pose before cloud image/video generation; permissive desktop code, separately restricted backend and excluded demo assets. | A (6/6) | [→](artcraft.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [We-Video](we-video.md) | ✅ | C (4/6) | Human-reviewed article-to-video implementation, not a turnkey checkout: missing API handlers, private prompts and Remotion's separate license remain your responsibility. |
| [Render engines](render-engines/INDEX.md) | Sub-category | — | HTML, React or Rust/SVG compositions to rendered frames; choose a production method or creator app below when the engine alone is not enough. |
| [Stickman Video Director](stickman-video-director.md) | ✅ | C (4/5) | Prompt-only directing and voice locks, not a renderer or a guarantee of generated continuity. |
| [huashu-art-motion](huashu-art-motion.md) | ✅ | C (5/6) | Art recipes and local Canvas rendering; mostly Chinese instructions, young single-author project. |
| [shuohao-skills](shuohao-skills.md) | ✅ | C (5/6) | Your generated drama keeps changing who sits where between shots; this collection turns a novel into shared character, art, script, staging and storyboard records before production. |
| [OpenMontage](open-montage.md) | ✅ | B (5/6) | Use it when you want an AI coding assistant to produce full videos — explainers, trailers, animations, or documentary montages — from a plain-language prompt through research, scripting, asset generation, and render. |
| [anything2explainer](anything2explainer.md) | ✅ | C (3/5) | A Claude Code / Codex skill-pack with a full explainer-film method (research → narration → storyboard → parallel build → QC) and a reference film as the quality bar; fixed MG style, 8 days old, PolyForm noncommercial. |
| [video-shotcraft](video-shotcraft.md) | ✅ | B (5/6) | Pick it when the film is a product promo built from real UI captures with a shot library supplying the taste — but it ships Remotion compositions, so the engine's ≤3-employee licence gate travels with your deliverable, and nothing is tagged. |
| [Hypit](hypit.md) | ✅ | C (4/6) | Agent-first viral-video cloning into word-anchored SVML workflows with pluggable generation providers; non-OSI license, 7 weeks old at verification, generation runs bill to paid model APIs. |
| [MoneyPrinterTurbo](moneyprinter-turbo.md) | ✅ | B (6/6) | Topic → narrated stock-footage shorts as a MIT WebUI/API appliance; near-zero marginal cost, generic output, single-maintainer bus factor. |
| [OpenCreator](open-creator.md) | ✅ | B (6/6) | Local Codex-native creator desktop whose shipped strength is translation/dubbing/portrait recut of an existing video; generation and writing share the same project. Codex login required, no Linux Desktop, nested GPL KrillinAI core. |
| [video-use](video-use.md) | ✅ | B (4/5) | Coding-agent editor for existing takes: packed Scribe transcript, strategy gate, ffmpeg render. MIT skill-pack, hard ElevenLabs dep, 22 commits / ~27k stars. |
| [SeeCut](seecut.md) | ✅ | D (4/6) | Edits existing A-roll with a video-watching AI judge loop on HyperFrames render; hard agy/Google-account dependency, PolyForm noncommercial, 4 days old — vs video-use's transcript-only MIT cut or HyperFrames' engine-only Apache. |
| Runway / Pika / HeyGen | 未收录 | — | Closed-source SaaS — faster one-click generation but no pipeline customization, no agent approval gates, no open-source extensibility. |
| DaVinci Resolve / Premiere Pro | 未收录 | — | Professional NLEs — human editors, not agent-driven; the right tool when you need frame-level manual control and a traditional post-production team. |
| [Lemo-Opuscar](lemo-opuscar.md) | ✅ | C (4/6) | Have a coding agent direct style-led films with deterministic browser frames, sound and reading-time checks; code MIT, gallery media CC BY. |
| [ArtCraft](artcraft.md) | ✅ | A (6/6) | Visual 2D/3D composition instead of inference-graph authoring; cloud jobs and auto-uploaded captures, not local inference or a wholly permissive service stack. |


## What belongs here

Tools and frameworks whose primary job is **agent-driven or AI-orchestrated video production** — directing methods, end-to-end pipelines and creator apps with quality gates, provider selection or budget governance. Pure code-defined composition and rendering engines go in [render-engines](render-engines/INDEX.md). Not traditional media processing frameworks (see `media-processing`), not standalone video-generation SaaS landing pages, and not general design/HTML generators (see `ai-design-generation`).
