---
name: video-shotcraft
slug: video-shotcraft
repo: https://github.com/Vincentwei1021/video-shotcraft
category: video-production
tags: [agent-skill, claude-code, codex, remotion, product-video, promo-video, motion-graphics, sound-design, jianying]
language: TypeScript
license: Apache-2.0
maturity: no versioned releases, created 2026-07-19, ~9.1k stars / 826 forks, active (as of 2026-09)
last_verified: 2026-09-21
type: skill-pack
upstream:
  pushed_at: 2026-09-09T05:46:40Z
  default_branch: main
  default_branch_sha: 5e71af35a2daee492dd3ea93e5e8903f32dcd13c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-21T02:30:34Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 12
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 64
        last_commit_age_days: 12
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 7
        top1_share: 0.659
        top3_share: 0.854
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
    adoption: { reason: no_package_structural }
---

# video-shotcraft

An agent skill for cinematic product films: a library of ~157 shot recipe cards with Remotion reference implementations, a validated 36-second promo template, sound-design assets, and a post-delivery workbench — so a coding agent can storyboard, animate and sound-design a launch video from your product's own screenshots.

![video-shotcraft — health radar](../../assets/health/video-shotcraft.svg)

## When to use

You are shipping a web or desktop product and you need a 30–60 second launch, demo or feature film. You have real screenshots and copy, a coding agent (Claude Code or Codex), and no motion designer — and the alternatives you have tried are unconvincing: a screen recording with a music bed, or a generative-video SaaS that invents footage that looks nothing like your product.

Reach for video-shotcraft because it supplies the part that usually requires taste rather than code: a **vocabulary of shots** (card deal-ins, row embeds, spotlight hero cards, 2.5D page-camera moves), each with the actual easing and timing parameters in a runnable TSX demo, plus a pinned SFX/BGM library and a written methodology for beat-syncing cuts and sound. It hands you a validated template to swap branding into, or lets the agent compose from the cards. The deciding tradeoff against its nearest neighbours: [Remotion Agent Skills](../agent-skills/vendor-collections/remotion-skills.md) teach the *API* and leave the visual and audio design to you, and [anything2explainer](anything2explainer.md) is an already-worked-out pipeline for one genre (narrated MG explainers) under a noncommercial licence — this pack is genre-focused, permissively licensed (Apache-2.0), and leaves the film editable after delivery, both in its own browser workbench and as an editable 剪映 draft.

## How it works

The skill is markdown methodology plus a working Remotion project, not a service. `SKILL.md` routes the agent into one of three modes — reproduce the bundled **Ink Press** template by swapping your screenshots and copy, compose freely from the shot cards, or co-create with you approving product brief, visual direction and storyboard — and each mode points at the matching reference document. From there the agent runs the repo's capture scripts against your product's pages, maps shot cards to a storyboard, writes the compositions as TSX (each card's demo is parameterised by normalised progress `t`, so timing stays deterministic), lays SFX and BGM on the beat, and renders through the template's own Remotion scripts. The delivery is not a dead file: a bundled workbench opens the finished film decomposed into shot / transition / caption / SFX tracks for retiming and copy edits, then re-renders through Remotion. What stays your job: replacing demo screenshots and branding, choosing the mode, and settling the Remotion licence question for your organisation.

![video-shotcraft — backbone user story](../../assets/flow/video-shotcraft.svg)

<!-- flow-steps:begin (generated from flows/video-shotcraft.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the skill into your coding agent — `npx skills add Vincentwei1021/video-shotcraft`
2. **You**: Point it at your product and say what the film is for — `Use video-shotcraft to create a promo for my desktop product.`
3. **video-shotcraft**: Checks the product read-only, maps shot cards, and storyboards the promo
4. **video-shotcraft**: Writes Remotion compositions: 2.5D camera moves, captions, SFX on the beat
5. **You**: Render the film from the bundled template — `npm run render`
6. **video-shotcraft**: Opens a workbench where shots can still be retimed and copy edited — `node workbench/scripts/open.mjs <project>`

**Value**: A cinematic product film from screenshots and one brief, with the shots still editable afterwards

</details>
<!-- flow-steps:end -->

## When NOT to use

- **The video needs a human narrator or word-locked voiceover.** This is a motion-design pack, not a narration pipeline; there is no TTS or forced-alignment stage. For a narrated motion-graphics explainer with human checkpoints use [anything2explainer](anything2explainer.md), and for stock-footage shorts with synthetic voice use [MoneyPrinterTurbo](moneyprinter-turbo.md).
- **You only need the agent to stop writing bad Remotion code.** Install [Remotion Agent Skills](../agent-skills/vendor-collections/remotion-skills.md) instead — they are the vendor's version-locked best practices, where this pack is one author's library plus a template.
- **Your motion stack is HTML, not React.** Take [HyperFrames](hyperframes.md) (Apache-2.0) and its skills; video-shotcraft's demos, template and workbench are all Remotion/React and do not port.
- **You want an end-to-end pipeline that researches, scripts and produces many genres behind approval gates.** Use [OpenMontage](open-montage.md); video-shotcraft assumes you already know what the film is and that you will supply the product material.
- **Nobody on the team can own the Remotion licence question.** Remotion is source-available and free for individuals and small companies, but larger organisations may need a paid licence — the README says so itself. If that is a blocker, use [HyperFrames](hyperframes.md), which is Apache-2.0, or author with [Remotion](remotion.md) directly and settle the terms yourself.
- **You need photoreal footage, a presenter or b-roll you don't own.** Everything here is composed from your screenshots and code-drawn motion; for generative footage or avatars use a closed SaaS (Runway, HeyGen — 未收录), accepting that it cannot reproduce your actual UI.
- **You need a dependency with a maintenance track record.** The repository is roughly two months old, has no versioned releases, and its numbers move weekly — see Health & viability before standardising a launch workflow on it.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Remotion Agent Skills](../agent-skills/vendor-collections/remotion-skills.md) | ✅ | When the agent already writes acceptable Remotion and you only need framework correctness, use the vendor skills; pick video-shotcraft when the missing layer is *design* — which shot, what easing, which SFX on which beat — because the vendor bundle ships no shot library, template or audio assets. | Vendor skills: canonical, version-locked, no opinions about your film. video-shotcraft: opinionated shot/SFX library and a template, maintained by one author and pinned to its own Remotion version. |
| [Remotion](remotion.md) | ✅ | When you want full control and your own visual identity, author Remotion directly; pick video-shotcraft when you want a launching point with the motion decisions already made, because the pack is a fixed-shot library and a template rather than a general framework. | Remotion: maximum freedom, no design help, you own composition and sound. video-shotcraft: faster first cut, but you inherit a style vocabulary and the pack's own version pins. |
| [anything2explainer](anything2explainer.md) | ✅ | Pick anything2explainer when the deliverable is a narrated explainer with research, voiceover and QC gates; pick video-shotcraft when it is a product promo with real UI, cinematic camera moves and sound design, because the two target different genres and only this one is Apache-2.0. | anything2explainer: fixed style, governed pipeline, noncommercial licence. video-shotcraft: permissive licence and product-specific material, with no narration or fact-checking stage. |
| [OpenMontage](open-montage.md) | ✅ | Pick OpenMontage when the whole production — research, scripting, assets, render — should be orchestrated with approvals across genres; pick video-shotcraft when the brief is a product film and you want the shot-level craft layer, because OpenMontage orchestrates engines while this pack supplies the motion vocabulary and audio. | OpenMontage: broader scope, AGPL-3.0, heavier toolchain. video-shotcraft: narrow and craft-dense, Apache-2.0, no approval-gate machinery. |
| [HyperFrames](hyperframes.md) | ✅ | Pick HyperFrames when the stack is HTML and the licence must be permissive without a company-size threshold; pick video-shotcraft when you are a React shop and want the shot library, because HyperFrames is a rendering engine with skills, not a curated motion and sound library. | HyperFrames: engine-first, Apache-2.0, you build the design system. video-shotcraft: design-first on Remotion, whose own licence may require a commercial agreement. |

## Health & viability

- **Maintenance (radar A, 2026-09-21):** very active for its age — created 2026-07-19, 96 commits, last push 2026-09-09, CI running `pr-checks.yml` alongside gallery and showcase deploy workflows. No versioned releases: the only tags are media-sync tags (`showcase-media`, `gallery-media`), so there is no stable pin to adopt.
- **Governance / bus factor (radar C):** the healthiest community signal in this batch — 7 contributors with the top author at ~69% of commits, ~54 merged pull requests, and open issues that are mostly localisation and workbench feature requests rather than breakage reports. There is still no organisation or foundation behind it, and the roadmap is one practitioner's. [推断]
- **Backing & Lindy (radar D):** two months old with ~9.1k stars and ~826 forks is attention, not a track record, and the repo carries Trendshift badges and a star-history chart — treat the velocity as marketing-amplified. The content is a distillation of publicly documented motion work (the README credits official films from ClickUp, Perplexity, Slack, Notion, Figma and others as study material, with no assets copied), so the *technique* is durable even though this repository has no history.
- **Adoption & ecosystem (radar ?):** distribution is through `npx skills add` and the agent's own skill loader, plus a public gallery of motion previews; there is no package on npm, so usage cannot be measured by downloads and the axis is structurally unscorable. The author maintains sibling packs for other video genres that are not indexed here, which means this page covers one entry in a family rather than a whole product line. [推断]
- **Risk flags (radar A):** the repo is Apache-2.0 but its core dependency **Remotion is source-available with a company-size threshold** — the licence question belongs to whoever ships the film; the clone is ~189 MB because the gallery and audio assets are committed; the README's own counts drift (its changelog says 152 cards / 209 previews while the header and contents table say 157 / 214); bundled template screenshots are demo assets that must be replaced before publishing; and the 剪映 export is documented as macOS-verified with Windows untested.

## Caveats (unverified)

- [未验证] Nothing here was executed: shot counts, template specs, audio inventory, headless notes and the workbench contract come from the README, `SKILL.md`, `template/package.json` and a GitHub tree listing read on 2026-09-21.
- [未验证] Star / fork / issue / commit counts are point-in-time GitHub API values (2026-09-21) on a two-month-old repo; they move fast.
- [未验证] The quality of the films this pack produces was not judged independently — the Gallery and YouTube examples are the project's own output, and no third-party reproduction report was found.
- [推断] README number drift (152 vs 157 shot cards, 209 vs 214 previews) looks like documentation lag rather than missing content: the tree contains 158 files under `references/shots/` including one attribution file.
- [未验证] The claim that 剪映 export was "verified on JianYing Pro 11.2 for macOS" is ambiguous in the README (another table cell reads "verified on macOS 11.2"); the repo's own tree comment marks Windows untested. Assume macOS-only until you reproduce it.
- [未验证] Headless rendering notes (`--concurrency=1`, chrome-headless-shell, `--browser-executable` fallback) are author-reported from one 2-core Linux box.
- [未验证] Remotion's licensing implication for a company above the free threshold was not reviewed with anyone qualified; the README merely acknowledges that a paid licence may be required.
- [推断] The shot-attribution list (official films studied as references, no assets copied) is taken at the project's word; no provenance audit of the TSX demos was performed.
