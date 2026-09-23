---
name: jq
slug: jq
repo: https://github.com/jqlang/jq
category: data-tools
tags: [data-tools, jq, tool]
language: C
license: NOASSERTION
maturity: active, ~35,118 stars (as of 2026-07)
last_verified: 2026-07-07
type: tool
upstream:
  pushed_at: 2026-07-02T05:45:10Z
  default_branch: master
  default_branch_sha: 579e6f76cffd7643ba4002a2c3618a5ea710589a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:09:46Z
  overall: A
  overall_score: 3.6
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
        last_commit_age_days: 3
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 12.9
        qualifying_issues: 16
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: conda-forge.org
        canonical_package: jq
        dependent_repos_count: 52
        downloads_last_month: 7573273
        graph_tier: D
        volume_tier: A
        cross_check_divergence: null
        homebrew_installs_90d: 216465
        homebrew_tier: A
        release_downloads: 295514014
        release_assets: 229
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5179
        last_commit_age_days: 3
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 20
        top1_share: 0.623
        top3_share: 0.696
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---
# jq

Command-line JSON processor

![jq — health radar](../../../assets/health/jq.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `data-tools` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for jq when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because jq was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on jq.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [CyberChef](cyberchef.md) | ✅ | When you need the established in-index option for this category, compare it against jq before switching. | jq is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose jq only after verifying the repo-specific caveats below. |
| [DevToys](devtoys.md) | ✅ | When you need the established in-index option for this category, compare it against jq before switching. | jq is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose jq only after verifying the repo-specific caveats below. |
| [Faker (faker-js)](faker-js.md) | ✅ | When you need the established in-index option for this category, compare it against jq before switching. | jq is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose jq only after verifying the repo-specific caveats below. |
| [Flashlight](flashlight.md) | ✅ | When you need the established in-index option for this category, compare it against jq before switching. | jq is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose jq only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** C per GitHub metadata.
- **Repository:** `jqlang/jq`.
- **Project shape:** categorized as `tool` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `master`, last pushed `2026-07-02T05:45:10Z`, archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=false` and `pushed_at=2026-07-02T05:45:10Z` as of 2026-07-07.
- **Adoption snapshot:** ~35,118 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `NOASSERTION` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** license needs manual verification; first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [未验证] GitHub API returned no SPDX license or NOASSERTION; inspect the repository license files before commercial or redistribution use.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
