---
name: ian-xiaohei-illustrations
slug: ian-illustrations
repo: https://github.com/helloianneo/ian-xiaohei-illustrations
category: visual-content
tags: [skill, illustration, hand-drawn, chinese, codex-skill, image-generation, prompt-pack]
language: Markdown
license: MIT
maturity: v1.0.0 release 2026-05-27, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-03T11:35:43Z
  default_branch: main
  default_branch_sha: 91b560849e8f883922cc2fa8a358a668caa94105
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:41:04Z
  overall: C
  overall_score: 2.25
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 111
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 118
        last_commit_age_days: 111
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# ian-xiaohei-illustrations

An agent skill that turns a Chinese article into 4–8 hand-drawn 16:9 explanatory illustrations starring the "小黑" (Xiaohei) ink character — your host agent's own image model does the rendering.

![ian-illustrations — health radar](../../../assets/health/ian-illustrations.svg)

## When to use

You're writing a Chinese long-form piece — a 公众号 post, a Notion methodology doc, a blog — and the prose is carrying ideas that *want* a picture: a two-breakpoint judgment, an input→output loop, a before/after, a "one fish, many dishes" reuse. You don't want a stock-photo banner or a tidy corporate infographic; you want something that looks like the author sketched it by hand and is a little weird but lands the point. You drop the article into your coding agent (Codex), invoke this skill, and it first reads the text to find the *cognitive anchors* worth illustrating, proposes a shot list (which paragraph, the core meaning, the structure type, what 小黑 is doing, suggested Chinese annotations), and then — using the agent's built-in `image_gen` — renders each shot as a separate white-background line drawing with sparse red/orange/blue handwritten notes.

Reach for it specifically when consistency of *one* visual voice matters across a whole article and you'd rather steer with a persona ("小黑 pulling the rope", "小黑 stamping the toolbox") than hand-write a fresh prompt per image. The skill is a set of reference docs — style DNA, the IP's action library, composition patterns, a prompt template, a QA checklist — that constrain the model toward a coherent, repeatable look rather than letting each call drift.

## When NOT to use

- **You need editable vector/structured artifacts.** It outputs PNGs only — it explicitly refuses PPTX/PDF/Keynote and SVG/HTML/Canvas editable graphics. If you need an editable deck or a card you can re-template, use [guizang-ppt](../slides-ppt/guizang-ppt.md) or [guizang-social-card](guizang-social-card.md) / [html-anything](../../ai-design-generation/html-anything.md).
- **Your content isn't Chinese (or isn't prose).** The whole skill is tuned for Chinese articles and Chinese handwritten annotations; English decks, data dashboards, or UI mockups are out of scope.
- **You want commercial illustration, cute cartoons, or dense infographics.** The skill deliberately steers *away* from polished commercial art and text-heavy infographics — that's a non-goal, not a limitation to work around.
- **Your host agent has no image-generation tool.** This is a prompt/skill pack, not a renderer: it assumes an agent with a built-in `image_gen` (the repo is packaged as a Codex skill). Without that, you get shot lists but no pictures.
- **You need brand/style lock-in or guaranteed reproducibility.** Output quality and adherence track whatever image model your agent calls; the skill biases the look but cannot pin exact results, and the 小黑 IP is one specific aesthetic you may not want.
- **Maturity:** small single-author skill at v1.0.0; treat longevity and ongoing maintenance as unproven.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [guizang-social-card](guizang-social-card.md) | ✅ | Choose guizang-social-card when you need polished social/quote cards rather than hand-drawn article sketches. | Generates polished social/quote cards (often via editable templates), not hand-drawn in-article explanatory sketches; different visual register. |
| [guizang-ppt](../slides-ppt/guizang-ppt.md) | ✅ | Choose guizang-ppt when you need structured multi-page slide decks. | Builds slide decks (structured, multi-page); this skill makes single-concept inline illustrations and refuses decks. |
| [html-anything](../../ai-design-generation/html-anything.md) | ✅ | Choose html-anything when you need editable/hostable HTML/CSS artifacts. | Produces HTML/CSS artifacts you can edit and host; this produces flat PNGs in one fixed art style. |
| [open-design](../../ai-design-generation/open-design.md) | ✅ | Choose open-design when you need reusable UI/design-system artifacts. | Toward reusable UI/design-system artifacts; orthogonal to a hand-drawn article-illustration persona. |
| [impeccable](../../ai-design-generation/impeccable.md) | ✅ | Choose impeccable when your target is general design artifacts rather than a fixed Chinese illustration voice. | Different generation target (design artifacts) rather than a fixed-IP Chinese illustration voice. |
| nano-banana / gpt-image prompt packs | 未收录 | Choose generic image-prompt packs when raw model access is enough. | Generic image-prompt collections give you raw model access with no article-analysis, shot-list, or consistent-IP layer this skill adds. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance (as of 2026-06):** last pushed 2026-06, not archived — active in absolute terms, but the repo was *created in 2026-05*, so there is barely a month of history to judge cadence on. [推断]
- **Governance & bus factor:** a `User`-owned, single-author skill (helloianneo) at v1.0.0; one person owns the 小黑 IP, the style DNA and the prompt templates. Classic single-maintainer bus-factor risk — if the author stops, nothing carries it. [推断]
- **Age & Lindy verdict:** age < 1 year and ~6k stars on a fresh repo make this **young + lightly-hyped, longevity unproven**; it has not survived long enough for Lindy to say anything. Bet on the *idea* (a consistent illustration persona), not on this repo being here in two years. [未验证]
- **Risk flags:** it is a thin prompt/style layer with no renderer of its own (depends on the host agent's `image_gen`), and the Codex-vs-Claude-Code packaging ambiguity (see Caveats) means host compatibility can shift under you. Low lock-in (MIT, plain markdown) offsets this — you can fork and keep the prompts. [推断]

## Caveats (unverified)

- [未验证] Release v1.0.0 dated 2026-05-27, last pushed 2026-06-03, license MIT — per `gh repo view` on 2026-06-26.
- [未验证] Star count ~6.2k as of 2026-06; GitHub stars are unreliable and date-sensitive — indicative only.
- [推断] The skill is packaged for Codex (install path `${CODEX_HOME:-$HOME/.codex}/skills/`, frontmatter + `agents/openai.yaml`); the README also frames it loosely as a "Claude Code Skill", so the exact set of compatible hosts is ambiguous — verify against your own agent before relying on it.
- [推断] Actual rendering depends on the host agent's built-in `image_gen` tool; the repo ships no model, API key, or rendering code of its own, so output fidelity is model-dependent and not controlled by the skill.
- [未验证] "4–8 illustrations per article" and the refused-output list (PPTX/SVG/etc.) come from SKILL.md's own instructions, not from independent testing.
