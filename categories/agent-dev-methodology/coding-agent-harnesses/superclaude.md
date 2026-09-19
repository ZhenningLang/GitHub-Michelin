---
name: SuperClaude Framework
slug: superclaude
repo: https://github.com/SuperClaude-Org/SuperClaude_Framework
category: coding-agent-harnesses
tags: [claude-code, slash-commands, agents, personas, behavioral-modes, mcp, config-framework]
language: Python
license: MIT
maturity: v4.3.0, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-13T16:40:33Z
  default_branch: master
  default_branch_sha: 226c45cc93b865108843a669c6545d421784b68c
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:18:03Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 67
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 376
        last_commit_age_days: 67
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 41
        top1_share: 0.409
        top3_share: 0.812
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
    responsiveness: { reason: no_traffic }
    adoption: { reason: registry_no_counts }
---

# SuperClaude Framework

A Python-installed configuration layer that bolts 30 `/sc:` slash commands, 20 specialized agents, 7 behavioral modes, and MCP wiring onto Claude Code via behavioral-instruction injection.

![superclaude — health radar](../../../assets/health/superclaude.svg)

## When to use

You're a developer who lives in Claude Code and keeps re-typing the same long prompts — "act as a security reviewer," "brainstorm before you implement," "be token-efficient" — and you want that structure to be a one-word command instead of a paragraph you paste every session. You run `pipx install superclaude && superclaude install`, and now you have `/sc:brainstorm`, `/sc:implement`, `/sc:troubleshoot`, `/sc:document` and ~26 more as first-class commands, plus 20 domain agents (security engineer, frontend architect, deep-research agent, PM agent) that the framework routes to based on context. The point is that you don't want to invent your own persona/command scaffolding from scratch — SuperClaude gives you an opinionated, ready-made one and an installer that drops the agent/command markdown into `~/.claude/`.

It also fits when you want behavioral *modes* layered on top of the raw model: a Brainstorming mode that interrogates requirements before coding, a Token-Efficiency mode for long sessions, an Introspection/Task-Management mode for multi-step work. You install once, get the whole battery of commands+agents+modes, and optionally bolt on 8 MCP servers (Context7, Serena, Playwright, Magic, Sequential-Thinking, etc.) through `superclaude mcp`. If your team standardizes on Claude Code and wants a shared command vocabulary, this is a packaged starting point rather than a DIY config repo.

## When NOT to use

- **You don't use Claude Code.** It targets Claude Code *only* — there is no Cursor / Codex / opencode / Droid / generic-agent path. If your harness is anything else, almost none of it applies. [推断]
- **You want a minimal, fully-owned config.** It injects a large surface (30 commands + 20 agents + 7 modes) into `~/.claude/`; if you prefer a handful of hand-written commands you fully understand, this is a lot of opaque scaffolding to audit and trim.
- **You distrust auto-routing / "automatic agent coordination."** Behavior is driven by the framework's own dispatch and behavioral-instruction injection; debugging *why* a given agent or mode fired means reading SuperClaude's markdown layer on top of Claude Code's native mechanics.
- **You want guaranteed performance wins.** Marketing cites "2-3x faster" and "30-50% fewer tokens" from optional MCPs — these are project claims, config-dependent, and not independently benchmarked here.
- **Churn / version coupling.** v4 is a recent rewrite and a v5 TypeScript plugin system is announced; command names, agent rosters, and the `~/.claude/` install layout can shift release-to-release, and a TS rewrite may change the install model entirely.
- **You only need one capability.** If you just want, say, structured brainstorming or a research mode, installing the whole battery (and its MCP setup) is heavier than copying a single command.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Superpowers](superpowers.md) | ✅ | Choose Superpowers when you need a Claude Code skill/plugin collection emphasizing reusable skills. | Claude Code skill/plugin collection emphasizing reusable "skills"; overlapping "battery of capabilities for Claude Code" goal, different packaging (plugin/skills vs installed command+persona framework). |
| [get-shit-done](../spec-driven-development/get-shit-done.md) | ✅ | Choose get-shit-done when you need an opinionated workflow/command pack for agent development. | Opinionated workflow/command pack for agent dev; narrower, workflow-first vs SuperClaude's broad command+agent+mode surface. |
| [Compound Engineering](compound-engineering.md) | ✅ | Choose Compound Engineering when you need methodology-plus-plugin tooling for compounding agent work. | Methodology-plus-plugin for compounding agent work; a development *philosophy* with tooling, vs SuperClaude's config-injection framework. |
| [ECC](ecc.md) | ✅ | Choose ECC when you need context-engineering methodology rather than an installable command suite. | Context-engineering methodology for agents; conceptual/process framing rather than an installable command suite. |
| [12-Factor Agents](../spec-driven-development/12-factor-agents.md) | ✅ | Choose 12-Factor Agents when you need principles for building reliable LLM agents. | Principles for building reliable LLM agents — a spec/manifesto you read, not software you install into Claude Code. |
| claude-code-templates / awesome-claude-code | 未收录 | Choose community template collections when you want lighter, à-la-carte Claude Code config snippets. | Community config/template collections for Claude Code; lighter, à-la-carte copy-paste vs SuperClaude's installed, coordinated framework. |

## Tech stack

- **Language:** Python (per repo `primaryLanguage`).
- **CLI / installer:** `click` (command-line interface), `rich` (terminal output), `pytest` (declared as a runtime dependency in `pyproject.toml`, unusual — normally a dev dep). [推断]
- **Distribution:** PyPI package `superclaude` (install via `pipx`); also published to npm as `@bifrost_inc/superclaude`; plus a `./install.sh` git path.
- **Payload:** markdown agent/command/mode definitions installed into `~/.claude/agents/` and related Claude Code config locations; behavioral-instruction injection is the core mechanism (no separate runtime service).
- **Optional integrations:** 8 MCP servers wired via `superclaude mcp` — Context7, Sequential-Thinking, Serena, Playwright, Magic, Morphllm-Fast-Apply, Chrome DevTools, Tavily.

## Dependencies

- **Runtime:** Python ≥ 3.10 (per `pyproject.toml` `requires-python`). A working Claude Code install is the real prerequisite — the framework is inert without it.
- **Python deps (v4.3.0):** `click` ≥ 8.0.0, `rich` ≥ 13.0.0, `pytest` ≥ 7.0.0.
- **Install:** `pipx install superclaude` then `superclaude install`; or clone + `./install.sh`; or `npm i -g @bifrost_inc/superclaude`.
- **Optional:** the 8 MCP servers each bring their own Node/Python runtimes and (some) API keys — installed separately via `superclaude mcp`, not bundled.

## Ops difficulty

**Low.** This is a client-side dev-tool config, not a deployed service: `pipx install` + `superclaude install` writes files into `~/.claude/` and you're done — no server, no datastore, no orchestration to keep alive. Maintenance burden comes from (a) re-running `superclaude install` after upgrades and reconciling changes to your `~/.claude/` config, (b) optional MCP servers, which add their own runtimes/keys and are the most likely thing to break, and (c) coupling to a fast-moving project mid-way through a v4→v5 (TypeScript) transition, which can change the install layout. There's nothing to scale or monitor in production.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06):** actively maintained — repo pushed 2026-06-13, latest release v4.3.0 (2026-03-22), not archived. v4 is a recent rewrite and a v5 (TypeScript plugin) is announced, so it's moving fast, not coasting — but the install layout can shift across the v4→v5 transition.
- **Governance & backing:** Organization-owned (SuperClaude-Org) — a community/org structure rather than a lone account, which is a modestly better bus-factor signal than a single-user repo. No foundation or commercial vendor backing is published; effectively a community-maintained framework.
- **Age & Lindy (2026-06):** created 2025-06, ~1 year old, ~23k stars. Young, and mid-rewrite (v4 fresh, v5 announced) means the contract you adopt today may not survive the next major. Lindy verdict: **unproven by age** — usable now, but pin versions and expect command/agent-roster and install-model churn.
- **Risk flags:** MIT (no relicense). Lock-in is **Claude-Code-only** [推断] — almost nothing transfers to other harnesses. Optional MCP servers are the most likely breakage surface (own runtimes/keys). No CVEs were reviewed.

## Caveats (unverified)

- [未验证] Counts "30 commands / 20 agents / 7 modes / 8 MCP servers" come from the project's README/release notes; the exact rosters shift release-to-release — verify against the installed files for your version.
- [未验证] Latest release v4.3.0 published 2026-03-22; repo `pushedAt` 2026-06-13 (active); star count ~23.4k as of 2026-06 — GitHub stars are unreliable and date-sensitive, treat as indicative only.
- [未验证] Performance claims ("2-3x faster", "30-50% fewer tokens") are the project's own framing for optional MCPs and are config-dependent; no independent benchmark.
- [推断] `pytest` appearing in runtime `dependencies` (vs dev-only) is taken from `pyproject.toml` as fetched; could be intentional (the installer self-tests) or a packaging quirk.
- [推断] "Claude Code only" is inferred from the README's framing and the `~/.claude/` install target; no other-agent support is documented, but absence of mention is not proof.
- [未验证] The announced v5.0 TypeScript plugin system is roadmap, not shipped; timing and whether it preserves the current install model are unconfirmed.
