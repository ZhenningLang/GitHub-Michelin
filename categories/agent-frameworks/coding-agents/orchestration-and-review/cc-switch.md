---
name: CC Switch
slug: cc-switch
repo: https://github.com/farion1231/cc-switch
category: orchestration-and-review
tags: [desktop-app, ai-tools, provider-management, mcp, skills-management]
language: Rust
license: MIT
maturity: v0.x, active, 111.6k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-06T01:11:56Z
  default_branch: main
  default_branch_sha: e606adfae7328acf836292701ad25cb1afe523f6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:34:25Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 32506
        homebrew_tier: A
        release_downloads: 19380551
        release_assets: 719
        release_tier: A
        signal_basis: homebrew+releases
    longevity:
      grade: C
      raw:
        repo_age_days: 414
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 98
        top1_share: 0.82
        top3_share: 0.88
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# CC Switch

A cross-platform desktop All-in-One manager for Claude Code, Claude Desktop, Codex, Gemini CLI, OpenCode, OpenClaw, and Hermes Agent — built with Rust and Tauri 2.

![CC Switch — health radar](../../../../assets/health/cc-switch.svg)

## When to use

You're a developer who juggles multiple AI coding agents and assistants across your daily workflow. You switch between Claude Code for deep codebase work, Codex for quick tasks, Gemini CLI for Google-integrated queries, and OpenClaw for personal messaging. You pick CC Switch over managing each tool from its own terminal window because it provides a single desktop control plane that unifies credentials, settings, and model providers with visual provider routing, skill management, and MCP integration. You pick it over a terminal-based workflow when you want to switch agents without memorizing CLI flags or maintaining separate config files for each tool. You install CC Switch, connect your providers once, and manage all your AI tools from one cross-platform GUI instead of context-switching across disparate interfaces.

## When NOT to use

- **If you only use one agent** — use that agent directly (e.g., Claude Code CLI) instead of CC Switch, because CC Switch adds unnecessary GUI overhead and abstraction for a single tool.
- **If you need to run on a headless server or CI pipeline** — use the CLI agents directly via SSH or shell scripts instead of CC Switch, because CC Switch is a Tauri desktop app that requires a GUI environment and will not run in headless environments.
- **If you need team-wide RBAC, audit trails, or policy enforcement** — use a governed platform like [Dify](https://github.com/langgenius/dify) or [n8n](https://github.com/n8n-io/n8n) instead of CC Switch, because CC Switch has no RBAC, admin layer, or enterprise compliance features.
- **If you don't switch between LLM providers or manage custom skills/MCP servers** — use a single agent like Claude Code or Gemini CLI directly instead of CC Switch, because if you don't need provider management, the added abstraction provides no value.
- **If you prefer staying entirely in the terminal** — use a terminal multiplexer like tmux or a shell alias system instead of CC Switch, because CC Switch is a GUI overlay built on Tauri, not a terminal-native solution.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [OpenClaw](../../agent-runtimes/personal-assistants/openclaw.md) | ✅ | Personal multi-channel AI assistant. | OpenClaw is a self-hosted assistant across messaging apps; CC Switch is a desktop manager for coding agents, not a conversational bot. |
| [Hermes Agent](../../agent-runtimes/personal-assistants/hermes-agent.md) | ✅ | Self-improving AI agent with a learning loop. | Hermes Agent is an autonomous agent; CC Switch is a management layer for other agents, not an agent itself. |
| [OpenCode](../terminal-agents/opencode.md) | ✅ | Open-source terminal coding agent. | OpenCode is one of the tools CC Switch manages; they complement rather than compete. |
| Claude Code / Claude Desktop | 未收录 | Official Anthropic desktop IDE integration. | First-party, closed-source; CC Switch adds multi-provider unification but at the cost of a third-party abstraction layer. |
| Cursor / Windsurf | 未收录 | AI-native IDEs with built-in multi-model support. | These are full editors with agent features; CC Switch is a meta-manager, not a code editor. |

## Tech stack

- **Rust** — core backend logic and Tauri 2 integration
- **TypeScript** — frontend UI layer
- **Tauri 2** — cross-platform desktop application framework
- **MCP (Model Context Protocol)** — for connecting custom skills and integrations

## Dependencies

- A supported desktop OS (Windows, macOS, or Linux)
- The AI tools you want to manage (Claude Code, Codex, Gemini CLI, etc.) installed separately
- API keys / credentials for each LLM provider you configure
- System webview (provided by the OS; Tauri 2 uses the native webview engine)

## Ops difficulty

**Low**. CC Switch is a desktop GUI application distributed via standard installer packages. The operational burden is limited to configuring your agent credentials and keeping the app updated. There is no server or database to maintain. However, you must still manage each underlying agent's credentials and updates independently.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 0 days ago.
- **Responsiveness**: Cannot be scored — no_traffic.
- **Adoption**: Cannot be scored — unknown.
- **Longevity**: Grade C — 414 days old.
- **Governance**: Grade D — top-3 contributor share 88.0% (?).
- **Risk / License**: Grade A — MIT license.
## Caveats (unverified)

- [未验证] The `111.6k` star count on a repo created in 2025-08 may be inflated by hype or bot activity rather than organic adoption.
- [未验证] `farion1231` is a personal GitHub account; there may be no team or backup maintainers.
- [未验证] The "official website" claim (`ccswitch.io`) has not been verified for authenticity or ongoing operation.
- [推断] As a meta-manager, CC Switch's value depends on the continued compatibility of the agents it manages; upstream API changes could break integrations quickly.
