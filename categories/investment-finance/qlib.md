---
name: qlib
slug: qlib
repo: https://github.com/microsoft/qlib
category: investment-finance
tags: [investment-finance, qlib, framework]
language: Python
license: NOASSERTION
maturity: active, ~46,281 stars (as of 2026-07)
last_verified: 2026-07-16
type: framework
upstream:
  pushed_at: 2026-04-22T07:08:01Z
  default_branch: main
  default_branch_sha: d5379c520f66a39953bad76234a7019a72796fd0
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:23:43Z
  overall: B
  overall_score: 2.67
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 6
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 189.0
        qualifying_issues: 3
        band: default
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 1410
        release_assets: 36
        release_tier: D
        signal_basis: releases
    longevity:
      grade: A
      raw:
        repo_age_days: 2230
        last_commit_age_days: 6
        cohort: framework
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 9
        top1_share: 0.655
        top3_share: 0.793
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
# qlib

Qlib is an AI-oriented Quant investment platform that aims to use AI tech to empower Quant Research, from exploring ideas to implementing productions. Qlib supports diverse ML modeling paradigms, including supervised learning, market dynamics modeling, and RL, and is now equipped with https://github.com/microsoft/RD-Agent to automate R&D process.

![qlib — health radar](../../assets/health/qlib.svg)

## When to use

You're evaluating a task in the `investment-finance` area and want a real repository in the oss-atlas shortlist rather than an untracked name from a backlog. Reach for qlib when the upstream description matches the job, when its license and maintenance profile are acceptable after verification, and when adopting a public project is preferable to writing a local one-off.

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
- **Repository shape:** `microsoft/qlib`; this first-pass page has not exhaustively read every dependency manifest.
- **Default branch snapshot:** last pushed `2026-04-22T07:08:01Z`; archived `false`.

## Dependencies

- **Runtime dependencies:** not exhaustively verified in this intake pass; inspect upstream manifests and docs before production use.
- **External services:** not exhaustively verified; check whether it needs API keys, data vendors, browsers, model providers, GPUs, databases, or queues.
- **Operational input:** at minimum, you depend on the GitHub repository and its release/update process.

## Ops difficulty

**Unknown to medium until deeper review.** Treat this page as an intake-backed starting point, not a full runbook. Library-style projects may be easy to try but still need version pinning, while apps/frameworks can hide data, service, and deployment requirements.


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2026-04-22T07:08:01Z`.
- **Adoption snapshot:** ~46,281 GitHub stars as of 2026-07; this is a noisy signal and low-star projects are still included when the repository is real and relevant.
- **License snapshot:** `NOASSERTION` from GitHub metadata; manual license-file review remains required when license matters.
- **Lindy / governance:** not fully reviewed in this intake pass. Check age, owner type, contributor concentration, releases, and issue response before long-term adoption.
- **Risk flags:** first-pass page generated from the 2026-07-16 backlog; semantic comparison and dependency review are intentionally conservative.

## Caveats (unverified)

- [未验证] This page is generated from public GitHub metadata plus the user-provided intake list; upstream README, docs, examples, releases, and dependency manifests still need deeper review.
- [未验证] License, install commands, supported harnesses, and runtime requirements may differ from GitHub metadata; verify them in the repository before use.
- [推断] The comparison table starts from nearby atlas categories rather than a complete substitute survey; refine it after reading the full upstream project and adjacent alternatives.
