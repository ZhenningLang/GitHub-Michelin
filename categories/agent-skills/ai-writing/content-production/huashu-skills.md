---
name: huashu-skills
slug: huashu-skills
repo: https://github.com/alchaincyf/huashu-skills
category: content-production
tags: [agent-skill, writing, huashu-skills, skill-pack]
language: Python
license: NOASSERTION
maturity: active, ~1,205 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-04-21T05:28:31Z
  default_branch: master
  default_branch_sha: 35e7cf31328f6de07e5d125bfd094791f84b2352
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:40:57Z
  overall: B
  overall_score: 2.5
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
        last_commit_age_days: 0
        active_weeks_13: 4
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
        repo_age_days: 242
        last_commit_age_days: 0
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
# huashu-skills

花叔的内容创作 Skills 合集 - AI审校、选题生成、视频大纲、素材搜索等 11 个实用技能

![huashu-skills — health radar](../../../../assets/health/huashu-skills.svg)

## When to use

You want a Chinese creator-oriented Claude Code skill collection for article editing, topic generation, research, video outlines, scripts, social conversion, images, PDF export, speech coaching, and prompt saving. Choose huashu-skills when you want a broad content-creation toolbox rather than a single writing pipeline.

The upstream README describes 21 practical skills, including end-to-end workflows such as slides, data reports, Douyin scripts, and design advice, plus writing/proofreading, material search, article editing, topic generation, video checks, image generation/upload, and Markdown-to-PDF. It installs individual skills via `/install-skill https://github.com/alchaincyf/huashu-skills/tree/master/{skill名}`.

## When NOT to use

- **License clarity is required.** The README did not expose a license section in this pass and `LICENSE` returned 404; keep reuse conservative.
- **You need one strict end-to-end article production line.** [writing-agent](writing-agent.md) is more process-heavy and evidence-gated.
- **You need English SaaS marketing or growth execution.** [marketingskills](../marketing-seo/marketingskills.md) is more specialized for CRO, SEO, analytics, and sales enablement.
- **You cannot install individual subskills.** The README's installation model is per skill path, not one clearly versioned package contract.
- **You require audited output quality claims.** Claims such as AI-detection reduction, image pipelines, or report quality still require local validation.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [writing-agent](writing-agent.md) | ✅ | Choose writing-agent when one article must move through a strict staged production and fact-check workflow. | writing-agent is deeper and heavier; huashu-skills is broader and modular. |
| [Baoyu Skills](baoyu-skills.md) | ✅ | Choose Baoyu Skills for broad coding-agent utilities across translation, formatting, capture, and media. | Baoyu is more utility-oriented; huashu-skills targets Chinese creator workflows. |
| [marketingskills](../marketing-seo/marketingskills.md) | ✅ | Choose marketingskills for SaaS/growth marketing. | marketingskills is marketing-specialized; huashu-skills is creator-content oriented. |
| Custom creator toolkit | 未收录 | Choose custom when your content channels, image hosts, and editorial style are fixed. | Better local fit, but you must maintain every skill yourself. |


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2026-04-21T05:28:31Z`; health scores maintenance as C.
- **Adoption snapshot:** ~1,205 GitHub stars as of 2026-07; useful attention signal for a creator toolkit but not a quality proof for every subskill.
- **License snapshot:** `NOASSERTION`; root `LICENSE` returned 404 during this pass and health marks the repo as source-available/no-license.
- **Lindy / governance:** health longevity is C and governance is D due to a young, single-maintainer-centered repo.
- **Risk flags:** broad surface area, unclear license, per-skill install paths, and channel-specific dependencies such as image hosts or model APIs.

## Caveats (unverified)

- [未验证] No root `LICENSE` file was found during this pass; do not assume permissive reuse.
- [未验证] Individual subskill behavior and external dependencies were not executed locally.
- [推断] Best fit is Chinese content-creator workflow support, not a single audited writing pipeline.
