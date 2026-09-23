---
name: DuckDB
slug: duckdb
repo: https://github.com/duckdb/duckdb
category: database-engines
tags: [database, data, duckdb, service]
language: C++
license: MIT
maturity: active, ~39,203 stars (as of 2026-07)
last_verified: 2026-07-06
type: service
upstream:
  pushed_at: 2026-07-06T14:49:41Z
  default_branch: main
  default_branch_sha: 36c64ee8b5a9c96276efa983eff6b41a7cc63102
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:05:13Z
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
        median_ttfr_hours: 26.5
        qualifying_issues: 4
        band: default
        window_offset_days: 8
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: duckdb-cli
        dependent_repos_count: 0
        downloads_last_month: 43625
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        homebrew_installs_90d: 12429
        homebrew_tier: A
        release_downloads: 7845529
        release_assets: 1189
        release_tier: B
        docker_pulls: 203207
        docker_image: duckdb/duckdb
        docker_tier: D
        signal_basis: homebrew+releases+docker
        tier_source: homebrew+releases+docker
    longevity:
      grade: A
      raw:
        repo_age_days: 3010
        last_commit_age_days: 0
        cohort: service
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 221
        top1_share: 0.267
        top3_share: 0.41
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
# DuckDB

DuckDB is an analytical in-process SQL database management system

![DuckDB — health radar](../../../assets/health/duckdb.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `databases` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for DuckDB when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because DuckDB was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on DuckDB.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [elasticsearch-dsl-py](../database-clients/elasticsearch-dsl-py.md) | ✅ | When you need the established in-index option for this category, compare it against DuckDB before switching. | DuckDB is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose DuckDB only after verifying the repo-specific caveats below. |
| [elasticsearch-sql](../database-clients/elasticsearch-sql.md) | ✅ | When you need the established in-index option for this category, compare it against DuckDB before switching. | DuckDB is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose DuckDB only after verifying the repo-specific caveats below. |
| [go-mysql-elasticsearch](../data-sync/go-mysql-elasticsearch.md) | ✅ | When you need the established in-index option for this category, compare it against DuckDB before switching. | DuckDB is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose DuckDB only after verifying the repo-specific caveats below. |
| [PikiwiDB](pikiwidb.md) | ✅ | When you need the established in-index option for this category, compare it against DuckDB before switching. | DuckDB is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose DuckDB only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** C++ per GitHub metadata.
- **Repository:** `duckdb/duckdb`.
- **Project shape:** categorized as `service` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `main`, last pushed `2026-07-06T14:49:41Z`, archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=false` and `pushed_at=2026-07-06T14:49:41Z` as of 2026-07-06.
- **Adoption snapshot:** ~39,203 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `MIT` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
