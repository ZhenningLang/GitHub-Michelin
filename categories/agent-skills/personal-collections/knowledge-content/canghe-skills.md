---
name: canghe-skills
slug: canghe-skills
repo: https://github.com/freestylefly/canghe-skills
category: knowledge-content
tags: [agent-skill, personal-collection, content-production, browser-automation, skill-pack]
language: TypeScript
license: NOASSERTION
maturity: active, ~407 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-06-08T09:57:52Z
  default_branch: master
  default_branch_sha: dd0bf355955b4c82b764740b4183c86a72ba0e0c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T07:36:15Z
  overall: D
  overall_score: 1.25
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
        last_commit_age_days: 107
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
        repo_age_days: 211
        last_commit_age_days: 107
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
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---
# canghe-skills

Canghe's personal Claude Code skills marketplace: content publishing, image/video generation backends, business intelligence, URL/X/WeChat extraction, Obsidian utilities, Remotion guidance, and document parsing.

![canghe-skills — health radar](../../../../assets/health/canghe-skills.svg)

## When to use

You're a power user of Claude Code who wants one personal marketplace of pragmatic skills for content production and utility automation: Xiaohongshu cards, infographics, covers, slide decks, comics, article illustrations, X/WeChat publishing, image/video generation backends, Tianyancha-style dashboards, URL/X/WeChat extraction, Obsidian helpers, Remotion references, and PaddleOCR document parsing. Pick canghe-skills when breadth and ready-to-install commands matter more than a single narrow engineering discipline.

The decisive tradeoff is convenience versus governance. It is a large personal bundle with many external API surfaces and some explicitly risky browser/web skills; use it as a curated toolbox, then install only the plugin group you need.

## When NOT to use

- **License clarity is mandatory.** GitHub metadata has no SPDX license and `master/LICENSE` returned 404 during verification; use [Khazix Skills](khazix-skills.md) or another MIT-verified collection if redistribution or vendoring matters.
- **You only need engineering discipline.** Use [mattpocock/skills](../../engineering/mattpocock-skills.md), [Waza](../../engineering/waza.md), or [Agent Skills (addyosmani)](../../engineering/addyosmani-agent-skills.md) instead; canghe-skills is a broad personal productivity and content toolbox.
- **You cannot handle credentials or browser-login risk.** Several skills mention API keys, Chrome/CDP login flows, X cookies, WeChat credentials, Gemini Web cookies, or provider tokens; prefer a narrower local-only skill if secrets and accounts cannot be governed.
- **You need vendor-neutral, organization-owned policy.** Build an internal marketplace or fork only the needed skills after review; this repo is an individual's evolving collection with many unrelated surfaces.
- **You need deterministic tests or CI workflows.** Use standard engineering/test tools; canghe-skills is mostly operator-invoked content, extraction, and utility automation.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Khazix Skills](khazix-skills.md) | ✅ | For a smaller Chinese personal skill set with clearer boundaries, choose Khazix Skills; choose canghe-skills when you need its broad content/media/publishing toolbox. | Khazix is easier to audit; canghe-skills covers many more workflows and external services. |
| [ljg-skills](ljg-skills.md) | ✅ | For Chinese reading, concept analysis, rewriting, and visual card rendering, choose ljg-skills; for publishing automation, image/video backends, and utility tools, choose canghe-skills. | ljg-skills is knowledge-work focused; canghe-skills is broader but riskier operationally. |
| [dbskill](dbskill.md) | ✅ | For business-model diagnosis and Chinese content strategy skills, choose dbskill; for concrete media generation and platform posting helpers, choose canghe-skills. | dbskill is more advisory; canghe-skills includes more command-style automation. |
| Internal skill marketplace | 未收录 | For enterprise use with secrets, accounts, and compliance, build or fork an internal marketplace; use canghe-skills as a source of patterns only. | Internal governance costs more, but avoids importing unrelated risky surfaces. |


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false`, default branch `master`, and `pushed_at=2026-06-08T09:57:52Z`; the health scorer grades maintenance `C`.
- **Adoption snapshot:** GitHub API reports ~407 stars as of 2026-07; that is enough to include the repo, but not enough to offset license and governance uncertainty.
- **License snapshot:** GitHub metadata reports no SPDX license and `master/LICENSE` returned 404; the README says `MIT`, but frontmatter stays `NOASSERTION` because no root license file was confirmed.
- **Lindy / governance:** the repo is young and appears single-maintainer in the health scorer, so governance is `D` and longevity is only `C`.
- **Risk flags:** many skills touch external APIs, browser sessions, cookies, social posting, and media generation providers; treat this as a menu, not a default install-all baseline.

## Caveats (unverified)

- [未验证] The README states `MIT`, but no root `LICENSE` file was reachable at `master/LICENSE`; confirm licensing before redistribution or vendoring.
- [未验证] The individual skill commands were not installed or executed by oss-atlas; API-key, browser-login, and provider behavior require local verification.
- [推断] This belongs in personal-collections rather than engineering because the dominant value is one author's broad toolbox, not code-quality discipline.
