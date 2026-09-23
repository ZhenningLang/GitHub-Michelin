---
name: ECC
slug: ecc
repo: https://github.com/affaan-m/ECC
category: coding-agent-harnesses
tags: [claude-code, skills, agents, hooks, memory, security-scan, cross-harness, mcp]
language: JavaScript
license: MIT
maturity: v2.0.0, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-29T04:55:36Z
  default_branch: main
  default_branch_sha: 2bc924faf2f8e893bfe0af86b1931283693c30ae
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T03:10:49Z
  overall: B
  overall_score: 2.67
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 46.8
        qualifying_issues: 31
        band: default
        window_offset_days: 4
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 77679
        release_assets: 10
        release_tier: D
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 248
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 92
        top1_share: 0.651
        top3_share: 0.748
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

# ECC

A cross-harness "agent operating system" that installs hundreds of skills, agents, rules, hooks, memory/instinct learning, and a security scanner into Claude Code (and Codex/OpenCode/Cursor) from one repo.

![ecc — health radar](../../../assets/health/ecc.svg)

## When to use

You're running Claude Code (or several harnesses — Codex, OpenCode, Cursor) day to day, and you've outgrown a hand-rolled `~/.claude` directory. You keep re-writing the same TDD / code-review / security-review workflows per project, your context gets blown out at session start, and nothing carries learnings forward. ECC resolves this by shipping an opinionated, batteries-included substrate as a Claude Code plugin: you run `/plugin install ecc@ecc`, and you get a large library of skills, specialized subagents (planner, architect, code-reviewer, language-specific reviewers), always-on rules, and Node-backed hooks that auto-save/load session context and extract "instincts" with confidence scoring. It's the right reach when you want a maintained, versioned harness stack instead of curating one yourself.

You're also a fit if you work across more than one agent runtime and want *one* source of truth: ECC ships harness-neutral session adapters and an MCP inventory so the same skills/rules/AGENTS.md conventions apply whether you're in Claude Code, Codex CLI, OpenCode, or Cursor, plus a `/security-scan` (AgentShield) pass that audits your agent config for injection risks, leaked secrets, and misconfigurations before you trust it.

## When NOT to use

- **You want a small, auditable, self-owned config.** ECC installs hundreds of skills/agents/rules and a hook runtime into `~/.claude`; if you prefer a handful of files you fully understand and version yourself, this is a large surface to inherit and reason about.
- **You're not on Claude Code / a supported harness.** The primary target is Claude Code; non-Claude harnesses use adapters of varying completeness. If your runtime isn't on the list, most value evaporates.
- **You distrust auto-loaded hooks / memory.** Hooks run Node on session events and persist data locally; the v2.0.0 notes themselves flag that "plugin hooks were silently no-ops on Node 21+" was a shipped bug — a reminder this is moving, behavior-bearing automation, not inert prompts.
- **You only need one workflow.** If you just want, say, a TDD loop or a security gate, lifting one pattern (or a single-purpose tool) beats adopting a whole operating-system layer and its update cadence.
- **Single-author velocity / lock-in risk.** Development is fast-moving and centered on one maintainer's repo; coupling your whole agent harness to its release rhythm and conventions is real lock-in. Maturity/abandonment is a bet you're making on one project.
- **You need provider-neutral methodology, not Claude-centric config.** ECC is heavily Claude-Code-shaped; for vendor-agnostic *principles* rather than installed config, a doc-only methodology fits better.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [SuperClaude Framework](superclaude.md) | ✅ | Choose SuperClaude Framework when you want a lighter Claude-focused config framework for personas, commands, and MCP. | Also a Claude-focused config framework (personas, commands, MCP); narrower and lighter than ECC's hundreds-of-skills + hooks + security-scan + cross-harness substrate. |
| [Superpowers](superpowers.md) | ✅ | Choose Superpowers when you need a curated Claude Code skills/plugin collection without ECC's hook and memory substrate. | A curated skills/plugin collection for Claude Code; overlapping skill-library idea but without ECC's memory/instinct hooks, security scanner, and multi-harness adapters. |
| [Compound Engineering](compound-engineering.md) | ✅ | Choose Compound Engineering when you need a smaller plugin encoding a specific compounding-workflow methodology. | A plugin encoding a specific compounding-workflow methodology; far more opinionated-and-small vs ECC's broad OS-style bundle. |
| [get-shit-done](../spec-driven-development/get-shit-done.md) | ✅ | Choose get-shit-done when you need a lightweight task-execution workflow pack. | Lightweight task-execution workflow pack; single-philosophy vs ECC's everything-included surface. |
| [12-Factor Agents](../spec-driven-development/12-factor-agents.md) | ✅ | Choose 12-Factor Agents when you need provider-neutral *principles* for building agents, not installed config. | Provider-neutral *principles* for building agents (docs, not installed config); different layer than ECC's concrete Claude-Code harness. |
| dotfiles / hand-rolled `~/.claude` | 未收录 | Choose hand-rolled dotfiles when you need full control and a minimal surface you maintain yourself. | Full control and minimal surface; you maintain every skill/hook/rule yourself instead of inheriting and updating a curated stack. |

## Tech stack

- **Language:** JavaScript / Node.js (per repo primary language) for hooks, scripts, and the install path; large amounts of Markdown (skills/agents/rules with YAML frontmatter) as the actual payload.
- **Tooling:** `install.sh` / `install.ps1` installers; npm packages `ecc-universal` (main) and `ecc-agentshield` (security auditor); Node's built-in test runner for the internal test suite.
- **Optional GUI:** a Python (Tkinter) dashboard (`ecc_dashboard.py`).
- **Integration surface:** Claude Code plugin format (`/plugin install`), `hooks.json` + Node hook scripts, `mcp-servers.json` for MCP wiring, and per-harness adapters (Codex `AGENTS.md`, OpenCode plugin hooks, Cursor, GitHub Copilot instruction files).

## Dependencies

- **Runtime:** Node.js (for hook execution and setup scripts). README states Claude Code CLI v2.1.0+ as the primary target [未验证]. v2.0.0 notes call out a Node 21+ hook regression that was fixed — version sensitivity is real.
- **Optional:** Python 3 for the dashboard GUI; PM2 for multi-agent orchestration; MCP servers (GitHub, Supabase, Vercel, Context7, Exa, Playwright, etc.) for the MCP features — each its own external dependency/credential.
- **Storage:** local only — memory/metrics persist under `~/.claude/session-data/`, `~/.claude/skills/learned/`, `~/.claude/metrics/`; no external backend.
- **Install:** `/plugin install ecc@ecc` (plugin path), or `npm install && ./install.sh --profile full` for manual setup.

## Ops difficulty

**Low to medium.** The plugin install path is one command and the system is purely client-side (no server to run), so getting started is easy. Difficulty rises because what you've installed is large and *active*: hundreds of skills/agents/rules plus Node hooks that fire on session events and mutate local memory. You inherit its update cadence, env-var tuning (`ECC_HOOK_PROFILE`, `ECC_SESSION_START_MAX_CHARS`, `ECC_AGENT_DATA_HOME`), Node-version sensitivity (the v2.0.0 Node 21+ hook fix), and cross-harness adapter quirks. Debugging an unexpected behavior means tracing through hook scripts and a big config tree rather than a few files you wrote.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 59.7 hours across 33 qualifying issues/PRs.
- **Maintenance (2026-06):** actively (fast) maintained — last pushed 2026-06, on a v2.0.0 line, not archived. The high open-issue count (~100) plus a self-disclosed "hooks were silent no-ops on Node 21+" regression in the v2.0.0 notes signals real velocity but also that behavior-bearing automation is still stabilizing.
- **Governance & bus factor:** the repo is **User-owned** (affaan-m), i.e. a single-maintainer project — and the ~222k-star headline against a one-person backing is a **bus-factor red flag**, not a safety signal. The "When NOT to use" section already calls out "single-author velocity / lock-in risk"; you are betting your whole agent harness on one person's release rhythm. [未验证] No foundation, company, or co-maintainer governance published.
- **Age & Lindy (2026-06):** created 2026-01, ~5 months old. Extremely young for something positioning itself as an "agent operating system" you install into `~/.claude`. Lindy verdict: **fails the longevity prior** — no track record, breaking change cadence likely; treat as early-adopter tooling, pin versions, expect churn.
- **Risk flags:** MIT-licensed (no relicense seen). Real risks are **Node-version sensitivity** (the shipped Node 21+ hook bug), **auto-loaded hooks that mutate local state**, and abandonment exposure from the single-maintainer structure. The bundled `/security-scan` (AgentShield) audits *your* config, but does not de-risk ECC's own surface.

## Caveats (unverified)

- [未验证] v2.0.0 publish date per GitHub release API is 2026-06-10; one secondary source rendered it as 2024 — treat the 2026-06 maturity line as the authoritative one and re-verify on the release page.
- [未验证] Skill/agent/command/rule counts vary by source and release (README cites ~271 skills / 67 agents; the v2.0.0 notes cite 261 skills / 64 agents / 84 commands). Counts shift release-to-release; verify against the current repo.
- [未验证] GitHub stars (~211.9k–221.9k as of 2026-06) — star counts in this ecosystem are unreliable and date-sensitive; indicative only.
- [未验证] npm package names (`ecc-universal`, `ecc-agentshield`), the Tkinter dashboard, PM2 orchestration, and AgentShield's "1,282 tests / 102 rules" come from the README and were not independently confirmed against published packages.
- [未验证] Claude Code CLI v2.1.0+ minimum and the exact set of supported non-Claude harnesses / adapter completeness are from project docs, not independently tested.
- [推断] Typed as `framework` (not `skill-pack`) because, beyond its prompt/skill payload, it ships real runtime tooling (Node hooks, installers, version-gated behavior, env-var config, local state) — i.e. it has genuine tech-stack/deps/ops. A reader who only wants the markdown payload may reasonably regard the prompt collection alone as skill-pack-like.
