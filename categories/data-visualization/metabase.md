---
name: Metabase
slug: metabase
repo: https://github.com/metabase/metabase
category: data-visualization
tags: [data-visualization, metabase, app]
language: Clojure
license: NOASSERTION
maturity: active, ~48,067 stars (as of 2026-07)
last_verified: 2026-07-07
type: app
upstream:
  pushed_at: 2026-07-06T14:45:57Z
  default_branch: master
  default_branch_sha: eae64a014a6825baa7a0eba0e6c3264f6e51b7de
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:03:24Z
  overall: A
  overall_score: 4.0
  scored_axes: 4
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
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@metabase/embedding-sdk-react"
        dependent_repos_count: 0
        downloads_last_month: 244900
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        docker_pulls: 272820557
        docker_image: metabase/metabase
        docker_tier: A
        signal_basis: docker
        tier_source: docker
    longevity:
      grade: A
      raw:
        repo_age_days: 4250
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 115
        top1_share: 0.058
        top3_share: 0.164
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_window_signal }
    risk_license: { reason: license_unparsed }
---
# Metabase

The easy-to-use open source Business Intelligence and Embedded Analytics tool that lets everyone work with data :bar_chart:

![Metabase — health radar](../../assets/health/metabase.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `data-visualization` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for Metabase when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because Metabase was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on Metabase.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Evidence](evidence.md) | ✅ | When you need the established in-index option for this category, compare it against Metabase before switching. | Metabase is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Metabase only after verifying the repo-specific caveats below. |
| [Apache Superset](superset.md) | ✅ | When you need the established in-index option for this category, compare it against Metabase before switching. | Metabase is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Metabase only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** Clojure per GitHub metadata.
- **Repository:** `metabase/metabase`.
- **Project shape:** categorized as `app` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `master`, last pushed `2026-07-06T14:45:57Z`, archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=false` and `pushed_at=2026-07-06T14:45:57Z` as of 2026-07-07.
- **Adoption snapshot:** ~48,067 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `NOASSERTION` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** license needs manual verification; first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [未验证] GitHub API returned no SPDX license or NOASSERTION; inspect the repository license files before commercial or redistribution use.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
