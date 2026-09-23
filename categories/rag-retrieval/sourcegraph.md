---
name: Sourcegraph
slug: sourcegraph
repo: https://github.com/sourcegraph/sourcegraph-public-snapshot
category: rag-retrieval
tags: [rag, retrieval, sourcegraph, app]
language: Go
license: NOASSERTION
maturity: archived, ~10,291 stars (as of 2026-07)
last_verified: 2026-07-07
type: app
upstream:
  pushed_at: 2024-09-02T11:52:13Z
  default_branch: main
  default_branch_sha: c864f15af264f0f456a6d8a83290b5c940715349
  archived: true
health:
  schema: 1
  computed_at: 2026-09-22T16:58:11Z
  overall: D
  overall_score: 0.75
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 761
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: relaxed_solo
        window_offset_days: 6
    adoption:
      grade: B
      raw:
        registry: proxy.golang.org
        canonical_package: github.com/sourcegraph/sourcegraph-public-snapshot
        dependent_repos_count: 1200
        downloads_last_month: null
        graph_tier: B
        volume_tier: "?"
        cross_check_divergence: null
        release_downloads: 40919
        release_assets: 146
        release_tier: D
        signal_basis: releases
        tier_source: registry
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 4047
        last_commit_age_days: 761
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    governance: { reason: unattributable }
    risk_license: { reason: license_unparsed }
---
# Sourcegraph

Code AI platform with Code Search & Cody It is archived on GitHub, so treat it as a legacy or pattern-source option rather than a default for new production work.

![Sourcegraph — health radar](../../assets/health/sourcegraph.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `rag-retrieval` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for Sourcegraph when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because Sourcegraph was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on Sourcegraph.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [code-review-graph](code-review-graph.md) | ✅ | When you need the established in-index option for this category, compare it against Sourcegraph before switching. | Sourcegraph is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Sourcegraph only after verifying the repo-specific caveats below. |
| [FAISS](faiss.md) | ✅ | When you need the established in-index option for this category, compare it against Sourcegraph before switching. | Sourcegraph is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Sourcegraph only after verifying the repo-specific caveats below. |
| [FalkorDB](falkordb.md) | ✅ | When you need the established in-index option for this category, compare it against Sourcegraph before switching. | Sourcegraph is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Sourcegraph only after verifying the repo-specific caveats below. |
| [graphify](graphify.md) | ✅ | When you need the established in-index option for this category, compare it against Sourcegraph before switching. | Sourcegraph is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose Sourcegraph only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** Go per GitHub metadata.
- **Repository:** `sourcegraph/sourcegraph-public-snapshot`.
- **Project shape:** categorized as `app` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `main`, last pushed `2024-09-02T11:52:13Z`, archived `true`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=true` and `pushed_at=2024-09-02T11:52:13Z` as of 2026-07-07.
- **Adoption snapshot:** ~10,291 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `NOASSERTION` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** archived repository; license needs manual verification; first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [未验证] GitHub API returned no SPDX license or NOASSERTION; inspect the repository license files before commercial or redistribution use.
- [未验证] GitHub marks this repository archived; treat it as a pattern or legacy option unless a maintained successor is confirmed.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
