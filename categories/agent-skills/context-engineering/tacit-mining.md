---
name: tacit-mining
slug: tacit-mining
repo: https://github.com/xiaohuailabs/tacit-mining
category: context-engineering
tags: [agent-skill, context-engineering, tacit-mining, skill-pack]
language: Unknown
license: NOASSERTION
maturity: active, ~68 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-04-08T10:52:37Z
  default_branch: main
  default_branch_sha: d8e0347d7854db024b0828f1102b5d638ad50d0f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T07:32:36Z
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
        last_commit_age_days: 168
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
        repo_age_days: 168
        last_commit_age_days: 168
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
# tacit-mining

Let AI truly understand you. A Claude Code skill that extracts tacit knowledge through structured dialogue. 隐性知识挖掘技能。

![tacit-mining — health radar](../../../assets/health/tacit-mining.svg)

## When to use

You want an agent to understand the user's tacit judgment rules through structured dialogue: writing taste, topic instinct, product judgment, aesthetics, and audience sense. Use tacit-mining when the target is **the current user's own implicit decision standards**, not a public persona or generic memory store.

The upstream skill is based on Polanyi's tacit knowledge theory plus CDM, Laddering, and Repertory Grid methods. It asks about concrete events and choices, performs teachback, stores confirmed or fuzzy rules under `memory/tacit/`, and updates a tacit knowledge map.

## When NOT to use

- **License clarity matters.** The README says MIT, but the verified root tree has no `LICENSE` file; keep reuse conservative until the upstream adds one.
- **You need a persona or expert imitation.** Use [nuwa-skill](nuwa-skill.md) or [soul.md](soul-md.md); tacit-mining is about extracting the user's own tacit rules.
- **You cannot store personal memory files.** The workflow writes `memory/tacit/` fragments and updates maps; that is sensitive user preference data.
- **You need quick prompt tuning.** Tacit mining is an interview loop, not a one-shot prompt optimizer.
- **The user does not want introspective questioning.** The method depends on 5-8 rounds of concrete-event probing and correction.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [nuwa-skill](nuwa-skill.md) | ✅ | Choose nuwa when you want to distill a public figure or theme into a reusable perspective skill. | nuwa targets public-source persona/thinking extraction; tacit-mining targets the current user's hidden criteria. |
| [soul.md](soul-md.md) | ✅ | Choose soul.md when you already have identity/source files and want a persistent persona package. | soul.md packages identity; tacit-mining elicits user rules through dialogue. |
| [NotebookLM Claude Code Skill](notebooklm-skill.md) | ✅ | Choose NotebookLM when the issue is source-grounded retrieval from uploaded documents. | NotebookLM retrieves; tacit-mining interviews and writes memory fragments. |
| Manual interview notes | 未收录 | Use manual notes when data sensitivity blocks automated memory writes. | Safer and easier to review, but loses agent automation and map updates. |


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2026-04-08T10:52:37Z`; health scores maintenance as C.
- **Adoption snapshot:** ~68 GitHub stars as of 2026-07; low adoption is acceptable for inclusion but should be treated as a risk signal.
- **License snapshot:** `NOASSERTION`; README says MIT, but the verified root tree contains only `README.md`, `SKILL.md`, and `banner.jpg`, with no root `LICENSE`.
- **Lindy / governance:** health longevity is C and governance is D due to a young, single-maintainer repo.
- **Risk flags:** stores sensitive user judgment data and can overfit from a small number of interview rounds.

## Caveats (unverified)

- [未验证] README says MIT, but no root `LICENSE` file was found in the verified tree.
- [未验证] The interview method was read from README/SKILL.md but not run with a user in this pass.
- [推断] Best fit is preference/tacit-rule extraction for a consenting user, not persona cloning or general knowledge retrieval.
