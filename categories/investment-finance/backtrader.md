---
name: backtrader
slug: backtrader
repo: https://github.com/mementum/backtrader
category: investment-finance
tags: [investment-finance, backtrader, library]
language: Python
license: NOASSERTION
maturity: active, ~22,458 stars (as of 2026-07)
last_verified: 2026-07-16
type: library
upstream:
  pushed_at: 2024-08-19T17:47:36Z
  default_branch: master
  default_branch_sha: b853d7c90b6721476eb5a5ea3135224e33db1f14
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:23:07Z
  overall: D
  overall_score: 1.0
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1252
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: backtrader
        dependent_repos_count: 231
        downloads_last_month: 293691
        graph_tier: C
        volume_tier: B
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 4273
        last_commit_age_days: 1252
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: issues_disabled }
    governance: { reason: unattributable }
---
# backtrader

Python Backtesting library for trading strategies

![backtrader — health radar](../../assets/health/backtrader.svg)

## When to use

You're evaluating a task in the `investment-finance` area and want a real repository in the GitHub-Michelin shortlist rather than an untracked name from a backlog. Reach for backtrader when the upstream description matches the job, when its license and maintenance profile are acceptable after verification, and when adopting a public project is preferable to writing a local one-off.

This is a first-pass intake page for a user-requested backlog item. Use it to route selection and compare nearby options, then reread the upstream README, license, examples, and release history before relying on it for high-stakes work.

## When NOT to use

- **You need a deeply reviewed atlas page today.** Prefer an older in-index page from the comparison table until this entry has had a full semantic review.
- **License is a hard constraint.** GitHub reported `NOASSERTION`; inspect the repository license files before commercial use, redistribution, or vendoring.
- **Maintenance risk is unacceptable.** If the project is young, single-maintainer, low-star, unversioned, or quiet, choose a more established substitute in the same category.
- **Your task needs a narrower substitute.** If another page's `When NOT to use` section names your exact constraint, prefer that page over this first-pass entry.
- **You cannot verify the upstream workflow.** Do not install, run, or vendor this repo before checking its README, scripts, dependencies, and any external API requirements.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Existing projects in this category | ✅ | Prefer a mature in-index page when it covers the same job with clearer dependencies and when-not guidance. | This page adds a backlog candidate; existing pages may be safer until deeper review is complete. |
| Custom implementation | 未收录 | Build custom only when the needed scope is tiny and ongoing maintenance is cheaper than adopting a repo. | Avoids dependency risk but loses upstream fixes, docs, and ecosystem signals. |


## Tech stack

- **Primary language:** Python per GitHub metadata.
- **Repository shape:** `mementum/backtrader`; this first-pass page has not exhaustively read every dependency manifest.
- **Default branch snapshot:** last pushed `2024-08-19T17:47:36Z`; archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect upstream manifests and docs before production use.
- **External services:** not exhaustively verified; check whether it needs API keys, data vendors, browsers, model providers, GPUs, databases, or queues.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until deeper review.** Treat this page as an intake-backed starting point, not a full runbook. Library-style projects may be easy to try but still need version pinning, while apps/frameworks can hide data, service, and deployment requirements.


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2024-08-19T17:47:36Z`.
- **Adoption snapshot:** ~22,458 GitHub stars as of 2026-07; this is a noisy signal and low-star projects are still included when the repository is real and relevant.
- **License snapshot:** `NOASSERTION` from GitHub metadata; manual license-file review remains required when license matters.
- **Lindy / governance:** not fully reviewed in this intake pass. Check age, owner type, contributor concentration, releases, and issue response before long-term adoption.
- **Risk flags:** first-pass page generated from the 2026-07-16 backlog; semantic comparison and dependency review are intentionally conservative.

## Caveats (unverified)

- [未验证] This page is generated from public GitHub metadata plus the user-provided intake list; upstream README, docs, examples, releases, and dependency manifests still need deeper review.
- [未验证] License, install commands, supported harnesses, and runtime requirements may differ from GitHub metadata; verify them in the repository before use.
- [推断] The comparison table starts from nearby atlas categories rather than a complete substitute survey; refine it after reading the full upstream project and adjacent alternatives.
