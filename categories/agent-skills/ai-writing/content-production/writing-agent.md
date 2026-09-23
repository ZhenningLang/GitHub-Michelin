---
name: writing-agent
slug: writing-agent
repo: https://github.com/dongbeixiaohuo/writing-agent
category: content-production
tags: [agent-skill, writing, writing-agent, skill-pack]
language: JavaScript
license: MIT
maturity: active, ~319 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-07-05T06:13:28Z
  default_branch: main
  default_branch_sha: 91177b9c0a07bb731a2e3dac3d57ac1b45de8678
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:41:02Z
  overall: B
  overall_score: 2.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 15
        active_weeks_13: 6
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 725
        release_assets: 1
        release_tier: D
        signal_basis: releases
    longevity:
      grade: B
      raw:
        repo_age_days: 275
        last_commit_age_days: 15
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
---
# writing-agent

🚀 一个基于 Claude Code (Skills + Subagents) 的“去AI味”全栈写作系统。不仅防套路，更通过专属规则强制注入人类观点与细节，搭配读者测试评估与自动图文排版。全面支持 DeepSeek / 智谱GLM / MiniMax 等国产低成本大模型，提供从选题、风格建模到审稿发布的高维全自动写作工作流。

![writing-agent — health radar](../../../../assets/health/writing-agent.svg)

## When to use

You write Chinese long-form opinion pieces, WeChat posts, or content-marketing essays and want a staged production line instead of “generate the full article in one prompt”. Choose writing-agent when you need topic/positioning, evidence ledger, scar-tissue material mining, outline, opening tournament, drafting, editorial review, reader simulation, de-AI pass, fact-check gate, and final `_clean.txt` output.

It fits users willing to run a full Claude Code project workflow, inspect intermediate artifacts, and use compatible model endpoints such as DeepSeek, GLM, or MiniMax. The repo also includes a Windows desktop preview, but the documented full workflow depends on project files, `.claude/`, workflows, agents, and scripts.

## When NOT to use

- **You want a short, one-shot draft.** This project is intentionally heavy; a simple prompt or smaller writing skill is cheaper.
- **You cannot keep intermediate files or evidence ledgers.** The value comes from artifacts such as theme files, evidence ledger, drafts, reviews, fact-check reports, and final clean output.
- **You do not use Claude Code or a compatible project workflow.** The full path depends on project runtime structure, agents, workflows, and scripts.
- **You need English marketing/copy workflows.** [marketingskills](../marketing-seo/marketingskills.md) is broader for SaaS marketing, CRO, SEO, and lifecycle execution.
- **You are unwilling to provide real material.** Upstream emphasizes true experiences/evidence and blocks unsupported facts; generic inputs weaken the pipeline.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [huashu-skills](huashu-skills.md) | ✅ | Choose huashu-skills for a broader Chinese creator toolkit: topics, research, editing, video outlines, and images. | huashu-skills is a toolkit collection; writing-agent is a stricter end-to-end writing production line. |
| [Baoyu Skills](baoyu-skills.md) | ✅ | Choose Baoyu Skills for general translation, formatting, transcript, webpage capture, and media utilities. | Broader utilities, less opinionated long-form writing pipeline. |
| [marketingskills](../marketing-seo/marketingskills.md) | ✅ | Choose marketingskills for marketing/CRO/SEO/growth tasks. | Marketing execution versus Chinese long-form article production. |
| Custom editorial workflow | 未收录 | Choose custom when your publication has fixed stages, reviewers, or compliance rules. | More exact to one org, but more maintenance work. |


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2026-07-05T06:13:28Z`; health scores maintenance as B.
- **Adoption snapshot:** ~319 GitHub stars as of 2026-07; niche but relevant for Chinese writing workflows.
- **License snapshot:** MIT verified from upstream README badge and root `LICENSE` in the read-only upstream check.
- **Lindy / governance:** health longevity is B and governance is D because the repo is young and single-maintainer concentrated.
- **Risk flags:** pipeline complexity, model/provider setup, and user-supplied evidence quality decide whether outputs are actually publishable.

## Caveats (unverified)

- [未验证] Demo quality and desktop preview were read from upstream docs but not executed locally.
- [未验证] Model recommendations and pricing notes can change; verify current provider docs before adopting.
- [推断] Best fit is disciplined Chinese long-form writing, not lightweight copyediting.
