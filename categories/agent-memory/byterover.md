---
name: ByteRover CLI
slug: byterover
repo: https://github.com/campfirein/byterover-cli
homepage: https://docs.byterover.dev/
category: agent-memory
tags: [agent-memory, context-tree, coding-agent, mcp, cloud-sync, repl]
language: TypeScript
license: NOASSERTION
maturity: v0.x, active; ~4.9k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-06-25T17:00:57Z
  default_branch: main
  default_branch_sha: 1052ac1a5dd0fde4da8693d4712064f7876c269c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:39:04Z
  overall: D
  overall_score: 1.83
  scored_axes: 6
  applicable_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NOASSERTION"
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 89
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: D
      raw:
        median_ttfr_hours: 1089.6
        qualifying_issues: 3
        band: default
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: byterover-cli
        dependent_repos_count: 0
        downloads_last_month: 57394
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 460
        last_commit_age_days: 89
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 17
        top1_share: 0.288
        top3_share: 0.634
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: NOASSERTION
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
---

# ByteRover CLI

A portable memory layer for autonomous coding agents (formerly Cipher) — structured context trees with git-like versioning, cloud sync, and MCP integration.

![ByteRover CLI — health radar](../../assets/health/byterover.svg)

## When to use

You're a developer who runs AI coding agents across multiple sessions and keeps losing context. You've tried relying on the agent's built-in memory, but it forgets project conventions, architectural decisions, and your personal coding style between sessions. You've looked at [Mem0](mem0.md) for a hosted memory API, but you want a local-first CLI tool with git-like versioning and a context tree you can control directly. You install ByteRover CLI (`brv`) in your project directory, and it builds an interactive REPL that understands your codebase through an agentic map, reads and writes files, executes code, and stores knowledge in a persistent context tree. You can version-control that context tree with git-like commands (branch, commit, merge, push/pull), sync it to the cloud for access across machines, and share it with teammates. It works with 20+ LLM providers and integrates with 22+ AI coding agents via MCP. Pick ByteRover over [Mem0](mem0.md) when you want a local CLI with git-like versioning rather than a hosted API-first service; pick it over [Memori](memori.md) when you want a structured context tree rather than a lightweight wrapper around your existing LLM client; pick it over [claude-mem](claude-mem.md) when you need a general-purpose cross-agent memory layer rather than a Claude Code-specific hook.


## When NOT to use

- **You want a simple, well-established memory solution.** If you need battle-tested agent memory with a proven track record, use [Mem0](mem0.md) or [Memori](memori.md) instead of ByteRover, because ByteRover is extremely young (created 2025-06) and pre-1.0, and the context-tree abstraction, git-like versioning, and cloud sync are novel but unproven at scale. [推断]
- **You don't want to add another dependency layer.** If you want minimal overhead between your coding agent and your project, use [claude-mem](claude-mem.md) or direct prompt engineering instead of ByteRover, because ByteRover sits between your agent and your project, adding a CLI tool, a web dashboard, and optionally a cloud backend.
- **You need a library you can embed in your own application.** If you need to add memory to a custom agent framework with a clean embeddable API, use [Mem0](mem0.md) or MemGPT instead of ByteRover, because ByteRover is primarily a CLI tool and REPL (`brv`), not a clean embeddable library with a simple API. [推断]
- **You are sensitive to license ambiguity.** If you need a clearly licensed library for commercial use, use [Mem0](mem0.md) (MIT) or [Memori](memori.md) (MIT) instead of ByteRover, because the GitHub metadata reports `NOASSERTION` (no recognized license), while the README shows an "Elastic 2.0" badge — the license situation needs clarification before commercial use. [未验证]
- **You don't want cloud sync or external dependencies.** If you want fully offline, air-gapped memory without any cloud-centric design, use [claude-mem](claude-mem.md) or a simple local file-based memory wrapper instead of ByteRover, because while local-only use is possible, the product's value proposition includes cloud sync and a hub ecosystem.
- **You need enterprise-grade security or compliance.** If you need an independently audited security model for memory and cloud sync, use [Mem0](mem0.md) or a vendor-backed commercial solution instead of ByteRover, because the project is young and small, and the security model of the cloud sync and MCP integration has not been independently audited.


## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Mem0](mem0.md) | ✅ | Mature, LLM-agnostic memory API with strong adoption and cloud service. | A hosted API-first memory service with broader ecosystem support; less focus on local CLI and git-like versioning than ByteRover. |
| [Memori](memori.md) | ✅ | Lightweight wrapper for adding persistent memory to existing LLM clients. | Simpler to adopt — wraps your existing client without a new CLI or context tree; less structured than ByteRover's approach. |
| [claude-mem](claude-mem.md) | ✅ | Hook/MCP memory wired into Claude Code's session lifecycle. | Tightly coupled to Claude Code; not a general-purpose cross-agent memory layer like ByteRover. |
| [Letta (MemGPT)](letta.md) | ✅ | Academic research project turned commercial for LLM memory management. | Deep research roots in memory management for LLMs; commercial service with a different pricing and integration model. |
| [Cognee](cognee.md) | ✅ | Open-source memory layer for AI agents with graph-based recall. | Graph-based memory with a different abstraction; younger and less proven than Mem0. |

## Tech stack

- **TypeScript** — primary implementation language.
- **Node.js** — runtime for the CLI and web dashboard.
- **React / Ink** — the interactive TUI REPL interface.
- **MCP (Model Context Protocol)** — integration with coding agents.
- **Cloud backend** — sync and hub services (optional, for push/pull).

## Dependencies

- **Node.js runtime** for the CLI and dashboard.
- **LLM provider** — one of 20+ supported providers (Anthropic, OpenAI, Google, Groq, Mistral, xAI, DeepSeek, etc.).
- **Optional: cloud account** — for sync, push/pull, and the hub ecosystem.
- **Project workspace** — ByteRover operates within a project directory, building an agentic map of the codebase.

## Ops difficulty

**Low to medium.** Installation is via npm (`npm install -g byterover-cli`). The CLI is self-contained, and local-only use requires no server setup. The medium difficulty comes from integrating it into your agent workflow: configuring the MCP integration, deciding what belongs in the context tree, and managing cloud sync if you use it. Because the project is young and pre-1.0, expect breaking changes and evolving configuration.

## Health & viability
- **Maintenance**: Grade A — 10/13 active weeks in trailing 13; last commit 7 days ago.
- **Responsiveness**: Grade A — median first-response time 3.6 hours across 23 qualifying issues/PRs.
- **Adoption**: Grade D — 6,431 monthly downloads via npmjs.org (package: byterover-cli).
- **Longevity**: Grade C — 379 days old.
- **Governance**: Grade A — top-3 contributor share 63.4% (?).
- **Risk / License**: Grade E — NOASSERTION license.
## Caveats (unverified)

- [未验证] Repo facts as of 2026-07-01 via GitHub API: created 2025-06-19, last push 2026-06-25, not archived, ~4.9k stars, ~453 forks, NOASSERTION license in metadata, language reported as TypeScript, owner type Organization.
- [未验证] The README shows an "Elastic 2.0" license badge, but GitHub metadata reports `NOASSERTION`. The actual license file and terms need verification before any commercial use.
- [未验证] The "20+ LLM providers", "24 built-in agent tools", "22+ AI coding agents" compatibility claims, and the cloud sync features are from the README; exact coverage and stability are not independently verified.
- [推断] The project was formerly named "Cipher" (as noted in the GitHub description: "formerly Cipher"); the rebrand timeline and any breaking changes from the old name are not documented here.
- [未验证] The "agentic map" of the codebase, context-tree versioning, and the web dashboard features are described in the README but not independently tested or verified.
- [推断] With ~4.9k stars on a repo created in mid-2025, the star count may reflect marketing or early hype rather than sustained production adoption.
- [推断] The security model of ByteRover's cloud sync and MCP integration has not been independently audited; enterprise users should verify before adoption.
