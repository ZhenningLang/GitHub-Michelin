---
name: ripgrep
slug: ripgrep
repo: https://github.com/BurntSushi/ripgrep
category: data-tools
tags: [search, grep, regex, cli, rust, gitignore]
language: Rust
license: Unlicense
maturity: v14.x, active, 66k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T12:07:43Z
  default_branch: master
  default_branch_sha: 48b0c795f4feb37343b2832d991c5c6a3900c08a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T03:03:17Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 50
        active_weeks_13: 6
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 13.2
        qualifying_issues: 22
        band: relaxed_solo
        window_offset_days: 8
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: crates.io
        canonical_package: ripgrep
        dependent_repos_count: 1
        downloads_last_month: 1575197
        graph_tier: D
        volume_tier: A
        cross_check_divergence: 13.39
        homebrew_installs_90d: 213088
        homebrew_tier: A
        release_downloads: 53737933
        release_assets: 678
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3848
        last_commit_age_days: 50
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 6
        top1_share: 0.842
        top3_share: 0.95
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Unlicense
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# ripgrep

A line-oriented search tool that recursively searches directories for a regex pattern while automatically respecting gitignore rules and skipping hidden files and binary files by default.

![ripgrep — health radar](../../../assets/health/ripgrep.svg)

## When to use

You're choosing a code search tool for daily use across large codebases and speed and smart defaults matter. You pick ripgrep over `grep` because you want a tool that automatically respects `.gitignore`, skips hidden files and binary files, and works identically on Windows, macOS, and Linux with prebuilt binaries for every release. You pick ripgrep over The Silver Searcher (ag) because ripgrep is generally faster, has better Unicode support, and more active maintenance. You need Unicode-aware regex search, optional multiline matching, and the ability to search specific file types — all fast enough to run interactively without waiting.

## When NOT to use

- If you need to search across lines with complex multiline patterns, use `pcregrep` or `ack` instead of ripgrep, because ripgrep is line-oriented by design and its multiline mode (`-U`) is not as natural for complex cross-line matching.
- If you need to search within binary files, use `grep` or `strings` instead of ripgrep, because ripgrep skips binary files by default.
- If you are on a system where you cannot install a new binary, use `grep` instead of ripgrep, because ripgrep is not universally preinstalled like `grep` and on minimal containers or restricted systems `grep` may be your only option.
- If you need a tool that is part of the POSIX standard and guaranteed on every Unix system, use `grep` instead of ripgrep, because ripgrep is a modern replacement but not a portable standard.
- If you need to search compressed files (`.gz`, `.zip`, `.tar`), use `zgrep` or `ag` with appropriate plugins instead of ripgrep, because ripgrep does not search inside archives by default.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| grep | 未收录 | The standard POSIX search utility, available everywhere. | grep is universal and standard but slower and noisier; ripgrep is faster, smarter, and respects gitignore by default. |
| The Silver Searcher (ag) | 未收录 | Fast grep replacement with gitignore support, written in C. | ag is mature and fast; ripgrep is generally faster, has better Unicode support, and more active maintenance. |
| ack | 未收录 | Perl-based search tool optimized for programmers. | ack is slower and requires Perl; ripgrep is faster, Rust-native, and has broader platform support. |
| git grep | 未收录 | Search within tracked files using git's own index. | git grep is fast for tracked files but only works inside Git repos; ripgrep works anywhere and searches untracked files too. |

## Tech stack

- **Rust** — primary implementation language for performance and safety
- **regex crate** — Rust's standard regex engine with SIMD optimizations
- **Memory-mapped I/O** — for efficient file reading on supported platforms

## Dependencies

- A supported platform (Windows, macOS, Linux; x86_64, ARM64, and others)
- No runtime dependencies — self-contained static binary
- Optional: PCRE2 support for advanced regex features (requires PCRE2 library if compiled with it)

## Ops difficulty

**None**. ripgrep is a single static binary. Install via package manager, download from releases, or `cargo install`. No configuration, no daemon, no maintenance.

## Health & viability
- **Maintenance**: Grade B — 5/13 active weeks in trailing 13; last commit 1 days ago.
- **Responsiveness**: Grade A — median first-response time 54.5 hours across 16 qualifying issues/PRs.
- **Adoption**: Grade D — 13,080,989 monthly downloads via conda-forge.org (package: ripgrep).
- **Longevity**: Grade A — 3,767 days old.
- **Governance**: Grade D — top-3 contributor share 93.1% (?).
- **Risk / License**: Grade A — Unlicense license.
## Caveats (unverified)

- [未验证] The exact performance comparison against grep and ag depends on the specific query, filesystem, and hardware; benchmarks vary.
- [未验证] The PCRE2 support is an optional compile-time feature; the prebuilt binaries may or may not include it depending on the release.
