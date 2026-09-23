---
name: uv
slug: uv
repo: https://github.com/astral-sh/uv
category: python-tooling
tags: [python, packaging, dependency-manager, rust, cli]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 87k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T08:47:56Z
  default_branch: main
  default_branch_sha: 648f5a3bd2be7c6e8465863693d4e625462fcbc1
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:56:35Z
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
      grade: A
      raw:
        median_ttfr_hours: 3.3
        qualifying_issues: 53
        band: relaxed_solo
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: uv
        dependent_repos_count: 2
        downloads_last_month: 128564586
        graph_tier: D
        volume_tier: A
        cross_check_divergence: 1.04
        homebrew_installs_90d: 523657
        homebrew_tier: A
        release_downloads: 630576062
        release_assets: 4180
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1086
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 152
        top1_share: 0.36
        top3_share: 0.632
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

# uv

An extremely fast Python package and project manager written in Rust, designed to replace pip, pip-tools, pipx, poetry, pyenv, and more with a single tool and a universal lockfile.

![uv — health radar](../../assets/health/uv.svg)

## When to use

You're a Python developer tired of waiting for `pip install` to resolve dependencies or juggling multiple tools — pip for installing, pip-tools for locking, pipx for CLI tools, pyenv for Python versions, poetry for project management. You've looked at Poetry for its mature project management and publish workflows, but you want a faster, more unified experience with a single tool and a universal lockfile. You reach for uv because it replaces the entire stack with one Rust-based CLI that installs packages 10–100x faster than pip, manages Python versions, runs scripts with inline dependency metadata, and produces a lockfile you can check into Git. Pick uv over pip when you want a modern resolver and lockfile instead of the legacy dependency algorithm; pick it over Poetry when you prioritize installation speed and a unified CLI over mature publish workflows; pick it over Conda when you are managing pure Python packages rather than scientific binary stacks that need precompiled distributions. You're starting a new Python project or modernizing an existing one and want the fastest, most reliable packaging experience available.


## When NOT to use

- **If you need a mature, battle-tested ecosystem.** If you need a packaging tool with 20+ years of stability and edge-case coverage, use pip with virtualenv instead of uv, because uv is relatively new (created 2023) and some edge cases in dependency resolution or platform-specific builds may still be rougher than pip or poetry.
- **If you rely on poetry-specific features.** If you need Poetry's `pyproject.toml` extras, plugins, and build-backend ecosystem, use Poetry instead of uv, because migrating existing poetry projects may require manual adjustment and full feature parity has not been achieved. [未验证]
- **If you need conda-forge or binary-scientific packages.** If you need precompiled binary distributions for scientific stacks (NumPy, PyTorch with CUDA), use Conda or Mamba instead of uv, because uv is a pip-replacement, not a Conda-replacement, and does not handle binary scientific distributions.
- **If you are on an exotic platform with no Rust toolchain.** If you need a package manager for a niche architecture without prebuilt binaries, use pip with source builds instead of uv, because uv provides prebuilt binaries for common platforms but niche architectures may require building from source.
- **If your team is not ready to change workflows.** If you have a stable legacy project with entrenched pip/virtualenv workflows and no migration budget, use pip with pip-tools instead of uv, because uv introduces new commands (`uv pip`, `uv run`, `uv lock`) and the learning curve may not be worth the speed gain for a team that values stability over velocity.


## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| pip | 未收录 | Python's default package installer. | pip is universal and stable but slow; uv is 10–100x faster with a modern resolver and lockfile. |
| Poetry | 未收录 | Python dependency management and packaging. | Poetry has mature project management and publish workflows; uv is faster but newer and still building feature parity. |
| pdm | 未收录 | Python package manager with PEP 582 support. | pdm is modern and spec-compliant; uv is faster but may lack some pdm-specific workflow features. |
| Conda | 未收录 | Cross-platform package manager for any language, especially scientific Python. | Conda handles binary scientific distributions; uv is Python-only and does not replace Conda's binary packaging. |

## Tech stack

- **Rust** — primary implementation language for performance and memory safety
- **PubGrub** — the dependency resolution algorithm (also used by cargo and dart)
- **PEP 517/518/621/660** — modern Python packaging standards support

## Dependencies

- A supported platform (macOS, Linux, Windows; x86_64 and ARM64)
- No Python runtime required for installation (self-contained Rust binary)
- A Python interpreter to manage (uv can install one for you)

## Ops difficulty

**Low**. A single static binary — install via `curl`, Homebrew, or PyPI. No daemon, no background service. For teams, the main cost is workflow migration and training.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 0 days ago.
- **Responsiveness**: Grade A — median first-response time 3.3 hours across 53 qualifying issues/PRs.
- **Adoption**: Grade A — 128,564,586 monthly downloads via pypi.org (package: uv).
- **Longevity**: Grade B — 1086 days old.
- **Governance**: Grade A — top-3 contributor share 63.2% (?).
- **Risk / License**: Grade A — Apache-2.0 license.
## Caveats (unverified)

- [未验证] The exact speedup factor varies by platform, cache state, and network conditions; 10–100x is the project's own benchmark claim.
- [未验证] Full feature parity with Poetry's build and publish workflows has not been achieved as of the verification date.
- [推断] Astral may introduce commercial tiers or feature-gating as the product matures, given the company's funding model.
