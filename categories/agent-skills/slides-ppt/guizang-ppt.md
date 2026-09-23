---
name: Guizang PPT Skill
slug: guizang-ppt
repo: https://github.com/op7418/guizang-ppt-skill
category: slides-ppt
tags: [skill, html-deck, presentation, slides, swiss-design, claude-code, codex]
language: HTML
license: AGPL-3.0-only
maturity: v1.1.0, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-02T09:53:57Z
  default_branch: main
  default_branch_sha: 82fe5ae129e8c2a12e1155fcabed6703342749d6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:40:22Z
  overall: C
  overall_score: 2.0
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 47
        active_weeks_13: 2
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
        repo_age_days: 152
        last_commit_age_days: 47
        cohort: skill-pack
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.5
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: true
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# Guizang PPT Skill

An agent skill that turns an article or outline into a single-file HTML horizontal-swipe slide deck — plus matching deck images and multi-platform covers — using two locked visual systems (editorial-magazine and Swiss international).

![guizang-ppt — health radar](../../../assets/health/guizang-ppt.svg)

## When to use

You're a founder, indie maker, or domain expert prepping a talk for an offline meetup, a private salon, or a product demo day, and you want a deck that looks designed rather than templated. You have an article or a pile of Markdown notes, you live in Claude Code or Codex, and you don't want to fight slide software or hand-place every box. You drop the skill in, say "make me a 7-page Swiss-style deck with 2–3 images," and the agent walks a fixed workflow — pick a style, answer a 7-question brief, copy the template, fill named layouts, optionally generate images, self-check against a checklist, open the result in a browser. Because the output is one self-contained `.html` file, you can present it, send it, or screenshot it with no build step and no server.

It fits best when you want a strong personal aesthetic baked in: Style A (electronic-magazine × e-ink) leans narrative and opinionated; Style B (Swiss international) enforces a 16-column grid, a single high-saturation anchor color, hairline rules, and 22 named layouts (`S01`–`S22`) with a validator script that rejects centered titles, improvised page structures, and text baked into SVG. You get a constrained, agent-legible design system instead of a blank canvas.

## When NOT to use

- **You need editable, collaborative slides.** Output is static single-file HTML; there's no PowerPoint/Google Slides export and no multi-author co-editing. If colleagues must edit in a familiar tool, this is the wrong artifact.
- **Dense data, tables, or training material.** The README explicitly calls out big tables and high-density courseware as a poor fit — the layouts optimize for sparse, statement-driven slides, not spreadsheets.
- **You're not in a file-system + browser agent.** It assumes an agent that can read/write files and run shell (Claude Code, Codex, Cursor). A plain chatbot with no filesystem or preview can't reliably produce a full deck.
- **You want provider-neutral image generation.** The optional image pipeline is described around Codex + GPT-Image / GPT-M models; if you can't use those, you lose the integrated image step and must source visuals yourself. [推断]
- **AGPL-3.0 matters to you.** The skill (and its templates/scripts) is AGPL-3.0-licensed; if you embed parts into a service or product you ship, the copyleft terms apply — read them before vendoring.
- **You need a stable, long-stable contract.** It's a young, fast-moving single-maintainer skill (latest release 2026-05); layout names, theme presets, and the brief flow can shift between versions.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [guizang-social-card](../visual-content/guizang-social-card.md) | ✅ | Choose guizang-social-card when you need single social cards/covers instead of full decks. | Same author's sibling skill, but scoped to single social cards / covers rather than full multi-page decks; overlapping visual rules, narrower output. |
| [html-anything](../../ai-design-generation/html-anything.md) | ✅ | Choose html-anything when you need general agent-driven HTML artifact generation. | General agent-driven HTML artifact generation; broader and unopinionated, so it lacks the locked deck layouts, Swiss validator, and cover/image workflow this skill ships. |
| [open-design](../../ai-design-generation/open-design.md) | ✅ | Choose open-design when you need broader UI/design generation rather than deck-specific output. | Aimed at broader UI/design generation; not a presentation-deck specialist with horizontal-swipe runtime and named slide layouts. |
| [Impeccable](../../ai-design-generation/impeccable.md) | ✅ | Choose Impeccable when you need a design-quality harness layer rather than deck generation. | Design-quality oriented generation; different surface — not a single-file HTML deck workflow. |
| Slidev | 未收录 | Choose Slidev when you need a developer-grade Markdown-to-HTML deck framework. | Developer-grade Markdown→HTML deck framework with build tooling, themes, and a dev server; more powerful/long-stable but not agent-driven and not opinionated about Swiss/editorial aesthetics. |
| Marp | 未收录 | Choose Marp when you need Markdown-to-slides with HTML/PDF/PPTX exports. | Markdown→slides (HTML/PDF/PPTX) with a clean ecosystem and exports this skill lacks; far less visual flexibility per slide. |
| Gamma / Tome | 未收录 | Choose Gamma or Tome when hosted AI deck SaaS is acceptable. | Hosted AI deck SaaS, not a repo — easier for non-agents, but closed, no single-file HTML artifact, no local agent control. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance (2026-06):** [推断] active — last push 2026-06-02, latest release v1.1.0 (2026-05-15), low open-issue count (~23). For a prompt/skill pack "maintenance" mostly means the author keeps tuning layouts and the brief flow; cadence looks healthy but is recent and could pause.
- **Governance & bus factor:** [推断] **single-maintainer, `User`-owned repo (`op7418`) with ~19k stars — a classic bus-factor flag.** A skill-pack this popular but driven by one person inherits that person's availability; there's no org or co-maintainer backstop. Mitigant: the output is a self-contained `.html` file you fully own, so an abandoned upstream doesn't strand the decks you already generated — only future updates stop.
- **Age & Lindy:** [推断] created 2026-04, ~2 months old as of 2026-06 — **young and hyped (high stars, low age); Lindy prior is essentially zero.** Layout names (`S01`–`S22`), theme presets, and the brief flow can shift release-to-release; don't treat the contract as stable.
- **Risk flags:** [未验证] **AGPL-3.0-only** — if you vendor templates/scripts into a product or network service you ship, copyleft applies; read the terms before embedding. Optional image pipeline is tied to specific Codex/GPT-Image models (provider lock for that step). No CVEs relevant to a static-HTML generator.

## Caveats (unverified)

- [未验证] License read as AGPL-3.0-only from the GitHub `licenseInfo` API and the `LICENSE` file (2026-06-26); confirm the exact SPDX/edition against the repo before relying on copyleft scope.
- [未验证] Latest release v1.1.0 (published 2026-05-15) and last push 2026-06-02 per the GitHub API on 2026-06-26; star count ~19k — GitHub stars are unreliable and date-sensitive, treat as indicative only.
- [推断] The optional image-generation step is tied to Codex + GPT-Image 2.0 / GPT-M 2.0 in the README; whether equivalent generation works on other agents/providers is not stated — verify before relying on it.
- [推断] "22 named Swiss layouts (S01–S22)" and "Style A 10 layouts" are the project's own framing from the README; the precise counts and names may shift release-to-release.
- [未验证] The Swiss validator (`scripts/validate-swiss-deck.mjs`) is a Node script; its exact rule coverage was read from the README description, not by running it.
