---
name: Alacritty
slug: alacritty
repo: https://github.com/alacritty/alacritty
category: terminal-ui
tags: [terminal, terminal-emulator, opengl, gpu, rust, cross-platform]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 65k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-06-22T14:16:02Z
  default_branch: master
  default_branch_sha: bdb72b32eeb074e3a0b8559d8ccac458237474a3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:06:20Z
  overall: A
  overall_score: 3.67
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
        last_commit_age_days: 22
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 2.0
        qualifying_issues: 38
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: crates.io
        canonical_package: alacritty_terminal
        dependent_repos_count: 335
        downloads_last_month: 1616311
        graph_tier: C
        volume_tier: A
        cross_check_divergence: 1.74
        homebrew_installs_90d: 3807
        homebrew_tier: A
        release_downloads: 2841517
        release_assets: 1144
        release_tier: B
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3870
        last_commit_age_days: 22
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.56
        top3_share: 0.92
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

# Alacritty

A fast, cross-platform, OpenGL terminal emulator with sensible defaults and extensive configuration, designed to integrate with other applications rather than reimplement their functionality.

![Alacritty — health radar](../../assets/health/alacritty.svg)

## When to use

You're a developer who spends hours in the terminal every day and wants the fastest, most responsive terminal emulator available. You pick Alacritty over WezTerm or Kitty because you want a terminal that does one thing exceptionally well — GPU-accelerated rendering — and delegates everything else to tools you already use. You pick it over iTerm2 because you need a cross-platform terminal that works identically on macOS, Linux, BSD, and Windows with the same configuration file, not a macOS-only app. You pick it over Warp because you value open-source transparency and minimalism over AI features and cloud integration. You are frustrated with terminal emulators that lag when scrolling through large log files or running `cat` on multi-megabyte outputs. You want a terminal that uses your GPU for rendering, offloading work from the CPU, and you already use tmux or screen for multiplexing.

## When NOT to use

- If you need a built-in terminal multiplexer with tabs and splits, use WezTerm, iTerm2, or Zellij instead of Alacritty, because Alacritty explicitly does not include tabs, splits, or session management.
- If you need font ligature support, use WezTerm or Kitty instead of Alacritty, because Alacritty does not support combining `!=` into a single glyph.
- If you are on a system without OpenGL 3.3+ support, use Windows Terminal or a CPU-based terminal instead of Alacritty, because Alacritty requires a modern GPU and graphics driver, and older systems or some VMs may not work.
- If you want a terminal with built-in AI or shell integration, use Warp instead of Alacritty, because Alacritty is a plain terminal emulator with no AI features, shell suggestions, or smart completions.
- If you need a fully stable, 1.0 product, use iTerm2 or Windows Terminal instead of Alacritty, because Alacritty is self-described as beta-level software, and while widely used as a daily driver, there are known missing features and bugs.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| WezTerm | 未收录 | Use Alacritty for minimal, raw-performance GPU terminal emulation; choose WezTerm when you want a modern GPU-accelerated terminal with tabs, splits, and ligatures built in. | WezTerm has more built-in features (tabs, ligatures, multiplexing); Alacritty is faster and more minimal. |
| Kitty | 未收录 | Use Alacritty for minimal, raw-performance GPU terminal emulation; choose Kitty when you want a GPU-based terminal with advanced features like kittens (plugins) and image support. | Kitty has more features and a plugin system; Alacritty is simpler and more focused on raw performance. |
| iTerm2 | 未收录 | Use Alacritty for cross-platform, minimal GPU terminal emulation; choose iTerm2 when you want the most popular macOS terminal with deep macOS integration and extensive features. | iTerm2 is macOS-only and feature-rich; Alacritty is cross-platform and minimal. |
| Windows Terminal | 未收录 | Use Alacritty for cross-platform, minimal GPU terminal emulation; choose Windows Terminal when you want Microsoft's modern terminal for Windows with tabs and GPU acceleration. | Windows Terminal is Windows-only and integrates with WSL; Alacritty is cross-platform and simpler. |
| [Warp](warp.md) | ✅ | Use Alacritty for fully open-source, minimal, local terminal emulation; choose Warp when you want an AI-powered modern terminal with cloud features and IDE-like blocks. | Warp has AI features and modern UI; Alacritty is plain, fast, and fully local. |

## Tech stack

- **Rust** — primary implementation language
- **OpenGL** — GPU-accelerated rendering for smooth scrolling and large output
- **FreeType/FontConfig** — font rendering and configuration (platform-dependent)

## Dependencies

- A modern desktop OS (macOS, Linux, BSD, Windows)
- A GPU with OpenGL 3.3+ support and up-to-date graphics drivers
- A shell of your choice (Alacritty does not bundle one)

## Ops difficulty

**None.** Alacritty is a single binary. Install via package manager or download from releases. Configuration is a single YAML file. No daemon, no background service.

## Health & viability
- **Maintenance**: Grade A — 7/13 active weeks in trailing 13; last commit 10 days ago.
- **Responsiveness**: Grade A — median first-response time 1.5 hours across 55 qualifying issues/PRs.
- **Adoption**: Grade B — 520,819 monthly downloads via crates.io (package: alacritty_terminal).
- **Longevity**: Grade A — 3,788 days old.
- **Governance**: Grade C — top-3 contributor share 93.3% (?).
- **Risk / License**: Grade A — Apache-2.0 license.
## Caveats (unverified)

- [未验证] The exact OpenGL version requirement and compatibility with specific GPU drivers on Linux vary by distribution and hardware.
- [未验证] The beta-level readiness claim is self-assessed by the project; many users report stable daily use.
- [推断] As the terminal emulator landscape evolves, Alacritty's minimalism may cause it to lose users to feature-richer alternatives like WezTerm or Warp unless it finds a way to maintain its performance edge.
