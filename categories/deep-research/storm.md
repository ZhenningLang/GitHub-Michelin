---
name: STORM
slug: storm
repo: https://github.com/stanford-oval/storm
category: deep-research
tags: [deep-research, storm, app]
language: Python
license: MIT
maturity: active, ~29,864 stars (as of 2026-07)
last_verified: 2026-07-06
type: app
upstream:
  pushed_at: 2025-09-30T18:07:21Z
  default_branch: main
  default_branch_sha: fb951af7744dab086e34962e9bc6fe878e145f83
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:08:26Z
  overall: B
  overall_score: 2.5
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 357
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 3.5
        qualifying_issues: 20
        band: relaxed_solo
        window_offset_days: 2
        source: pr
        inferred: false
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: knowledge-storm
        dependent_repos_count: 0
        downloads_last_month: 2205
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        docker_pulls: 9326098
        docker_image: library/storm
        docker_tier: C
        signal_basis: docker
        tier_source: docker
    longevity:
      grade: C
      raw:
        repo_age_days: 912
        last_commit_age_days: 357
        cohort: app
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
---
# STORM

An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations.

![STORM — health radar](../../assets/health/storm.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `deep-research` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for STORM when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because STORM was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on STORM.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Agent-Reach](agent-reach.md) | ✅ | When you need the established in-index option for this category, compare it against STORM before switching. | STORM is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose STORM only after verifying the repo-specific caveats below. |
| [deep-research](deep-research.md) | ✅ | When you need the established in-index option for this category, compare it against STORM before switching. | STORM is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose STORM only after verifying the repo-specific caveats below. |
| [GPT Researcher](gpt-researcher.md) | ✅ | When you need the established in-index option for this category, compare it against STORM before switching. | STORM is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose STORM only after verifying the repo-specific caveats below. |
| [Local Deep Research](local-deep-research.md) | ✅ | When you need the established in-index option for this category, compare it against STORM before switching. | STORM is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose STORM only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** Python per GitHub metadata.
- **Repository:** `stanford-oval/storm`.
- **Project shape:** categorized as `app` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `main`, last pushed `2025-09-30T18:07:21Z`, archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=false` and `pushed_at=2025-09-30T18:07:21Z` as of 2026-07-06.
- **Adoption snapshot:** ~29,864 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `MIT` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
