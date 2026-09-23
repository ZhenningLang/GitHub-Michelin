---
name: MLX / mlx-lm
slug: mlx-mlx-lm
repo: https://github.com/ml-explore/mlx-lm
category: on-device-ml
tags: [on-device-ml, mlx-mlx-lm, library]
language: Python
license: MIT
maturity: active, ~6,204 stars (as of 2026-07)
last_verified: 2026-07-07
type: library
upstream:
  pushed_at: 2026-06-24T23:12:59Z
  default_branch: main
  default_branch_sha: 2ed22318cd6a2fcc5c2e0caa1e1fb0ddeb7cafd5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:49:36Z
  overall: B
  overall_score: 3.33
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
        last_commit_age_days: 1
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 129.3
        qualifying_issues: 36
        band: default
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: mlx-lm
        dependent_repos_count: 0
        downloads_last_month: 935298
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.67
        homebrew_installs_90d: 1280
        homebrew_tier: B
        release_downloads: 1613
        release_assets: 1
        release_tier: D
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 560
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 72
        top1_share: 0.289
        top3_share: 0.506
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
# MLX / mlx-lm

Run LLMs with MLX

![MLX / mlx-lm — health radar](../../assets/health/mlx-mlx-lm.svg)

## When to use

You're choosing open-source infrastructure for a task that falls into `on-device-ml` and you need a real repository to evaluate, not just a product name from a comparison table. You reach for MLX / mlx-lm when its upstream description matches the job and when adopting an existing project is preferable to writing custom glue from scratch.

This first-pass page exists because MLX / mlx-lm was repeatedly useful as a comparison candidate in the atlas backlog. Use it as an intake-backed starting point: verify the upstream README and license, then compare it against the linked neighboring pages before committing to the dependency.

## When NOT to use

- **You need a fully reviewed, deeply researched atlas page today.** Use a more mature in-index page from the comparison table until this intake page has been semantically reviewed with the upstream docs.
- **The GitHub metadata flags a blocker for your environment.** If license, archival status, or maintenance cadence is load-bearing, choose a better-verified alternative in this category instead of relying on MLX / mlx-lm.
- **Your task needs a narrower or more specialized substitute.** Prefer the existing page whose `When NOT to use` section names your exact constraint; this page is a broad first-pass entry.
- **You cannot afford upstream churn or operational unknowns.** Pick an older in-index project with a clearer Lindy record and documented ops profile.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Google AI Edge Gallery](ai-edge-gallery.md) | ✅ | When you need the established in-index option for this category, compare it against MLX / mlx-lm before switching. | MLX / mlx-lm is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose MLX / mlx-lm only after verifying the repo-specific caveats below. |
| [BitNet](bitnet.md) | ✅ | When you need the established in-index option for this category, compare it against MLX / mlx-lm before switching. | MLX / mlx-lm is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose MLX / mlx-lm only after verifying the repo-specific caveats below. |
| [ComfyUI](comfyui.md) | ✅ | When you need the established in-index option for this category, compare it against MLX / mlx-lm before switching. | MLX / mlx-lm is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose MLX / mlx-lm only after verifying the repo-specific caveats below. |
| [LiteRT-LM](litert-lm.md) | ✅ | When you need the established in-index option for this category, compare it against MLX / mlx-lm before switching. | MLX / mlx-lm is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose MLX / mlx-lm only after verifying the repo-specific caveats below. |
| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |

## Tech stack

- **Primary language:** Python per GitHub metadata.
- **Repository:** `ml-explore/mlx-lm`.
- **Project shape:** categorized as `library` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `main`, last pushed `2026-06-24T23:12:59Z`, archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect the upstream dependency manifest before production use.
- **External services:** not exhaustively verified in this intake pass; check whether the project requires databases, queues, cloud APIs, browser runtimes, GPUs, or model-provider credentials.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until the upstream docs are reread.** Library-style entries may be low effort to try but still need version pinning and upgrade review. App/service/framework entries can carry hidden database, worker, storage, auth, browser, GPU, or cloud-provider requirements, so treat this first-pass entry as an intake marker rather than an ops runbook.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived=false` and `pushed_at=2026-06-24T23:12:59Z` as of 2026-07-07.
- **Adoption snapshot:** ~6,204 GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `MIT` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** first-pass page generated from backlog metadata.

## Caveats (unverified)

- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes.
- [推断] The backlog item was mixed; this page records the verified repository URL only, not every adjacent project implied by the original label.
- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.
