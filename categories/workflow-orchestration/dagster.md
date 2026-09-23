---
name: Dagster
slug: dagster
repo: https://github.com/dagster-io/dagster
category: workflow-orchestration
tags: [workflow, orchestration, dagster, framework]
language: Python
license: Apache-2.0
maturity: active, ~15,793 stars (as of 2026-07)
last_verified: 2026-07-06
type: framework
upstream:
  pushed_at: 2026-07-02T19:00:14Z
  default_branch: master
  default_branch_sha: 7e8a1303f8dea2a7aebd02fb11e9cbd53f7fffe5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:22:31Z
  overall: A
  overall_score: 3.83
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 65.8
        qualifying_issues: 21
        band: default
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: dagster-pipes
        dependent_repos_count: 1
        downloads_last_month: 8497641
        graph_tier: D
        volume_tier: A
        cross_check_divergence: null
        release_downloads: 5717
        release_assets: 576
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3067
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 90
        top1_share: 0.304
        top3_share: 0.502
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---
# Dagster

An orchestration platform for the development, production, and observation of data assets.

![Dagster — health radar](../../assets/health/dagster.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `workflow-orchestration` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for Dagster when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because Dagster was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on Dagster.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Airflow Maintenance DAGs](airflow-maintenance-dags.md) | ✅ | When you need the established in-index option for this category, compare it against Dagster before switching. | Dagster is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Dagster only after verifying the repo-specific caveats below. |
| [Apache Airflow](airflow.md) | ✅ | When you need the established in-index option for this category, compare it against Dagster before switching. | Dagster is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Dagster only after verifying the repo-specific caveats below. |
| [Argo Workflows](argo-workflows.md) | ✅ | When you need the established in-index option for this category, compare it against Dagster before switching. | Dagster is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Dagster only after verifying the repo-specific caveats below. |
| [Gaia](gaia.md) | ✅ | When you need the established in-index option for this category, compare it against Dagster before switching. | Dagster is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Dagster only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** Python per GitHub metadata.
- **Repository:** `dagster-io/dagster`.
- **Project shape:** categorized as `framework` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `master`, last pushed `2026-07-02T19:00:14Z`, archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=false` and `pushed_at=2026-07-02T19:00:14Z` as of 2026-07-06.
- **Adoption snapshot:** ~15,793 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `Apache-2.0` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
