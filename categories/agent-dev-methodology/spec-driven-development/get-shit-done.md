---
name: Get Shit Done (GSD)
slug: get-shit-done
repo: https://github.com/gsd-build/get-shit-done
category: spec-driven-development
tags: [spec-driven, context-engineering, meta-prompting, claude-code, subagents, phase-workflow, multi-runtime]
language: JavaScript
license: MIT
maturity: GitHub release v1.42.3 (2026-05); main README now redirects to open-gsd/gsd-core (as of 2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-05-31T17:46:54Z
  default_branch: main
  default_branch_sha: bdcaab2c752d9a33a1a1ca9acf3a3c81fb991815
  archived: true
health:
  schema: 1
  computed_at: 2026-07-03T08:18:09Z
  overall: C
  overall_score: 1.5
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 33
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: default
        window_offset_days: 10
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: get-shit-done-cc
        dependent_repos_count: 0
        downloads_last_month: 194520
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 201
        last_commit_age_days: 33
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 97
        top1_share: 0.454
        top3_share: 0.871
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

# Get Shit Done (GSD)

A spec-driven, context-engineering workflow for coding agents: it turns a vague idea into PROJECT/ROADMAP/CONTEXT/PLAN docs, then executes each phase in a fresh context window with orchestrated subagents to fight context rot.

![get-shit-done — health radar](../../../assets/health/get-shit-done.svg)

## When to use

You're a solo builder or small team who codes *through* an agent (Claude Code, OpenCode, Codex, Gemini, Cursor, and others) rather than by hand. You've felt the classic failure: you describe a feature, the agent one-shots a wall of code, quality holds for the first few turns, then degrades as the context window fills with history — by the end it's confidently producing slop that falls apart at scale. You don't want BMAD/SpecKit-style enterprise ceremony (sprints, story points, Jira), you just want the model to actually understand what you're building and ship it reliably. GSD installs a handful of slash commands (`/gsd-new-project`, `/gsd-discuss-phase`, `/gsd-plan-phase`, `/gsd-execute-phase`, `/gsd-verify-work`, `/gsd-ship`) that walk you from interview → research → roadmap → per-phase context → atomic plans → wave-parallel execution, persisting state in markdown (`PROJECT.md`, `ROADMAP.md`, `STATE.md`, `{phase}-CONTEXT.md`, `{phase}-PLAN.md`).

The core bet is structural: each atomic plan is small enough to run in its own clean 200k-token window, so implementation never inherits a degraded conversation, and each task gets its own commit so git history stays auditable. It's a good fit when you want a repeatable build loop with checkpoints you approve (you review the roadmap, you shape each phase's CONTEXT before any code is written, you do a guided UAT pass), and when you run the agent in skip-permissions / autonomous mode and want guardrails baked into the prompts rather than improvised per-task.

## When NOT to use

- **You want a thin, fully-owned prompt setup.** GSD is a large, fast-moving system (dozens of subagents in `agents/`, a built TypeScript SDK, install logic across ~13 runtimes). If you want to read and own every prompt, a small hand-rolled `CLAUDE.md` + a few commands is more legible.
- **You distrust the project's governance/continuity.** The canonical `main` README is now just a redirect notice pointing to a *different* org's repo (`open-gsd/gsd-core`), while GitHub still reports the repo as not archived and `package.json` sits on a canary version ahead of the last tagged release — a confusing split-brain that signals an in-flight relocation/fork. [推断] Pin a version and watch where development actually lands before depending on it.
- **You need deterministic, non-LLM build orchestration.** GSD's "verification" and "wave execution" are agent-driven prompt workflows, not a CI/build engine. [未验证] Behavior is model- and runtime-dependent and not guaranteed reproducible run-to-run.
- **You're on a non-supported or older runtime / tiny context budget.** It targets specific agent CLIs; the default install carries a multi-thousand-token system-prompt overhead (there is a `--minimal` profile, but full power assumes a capable, large-context agent run in skip-permissions mode).
- **Crypto-adjacency is a dealbreaker.** The README prominently features a `$GSD` Solana token. The framework itself is MIT and usable without it, but if a memecoin association is disqualifying for your org, factor that in.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [SuperClaude Framework](../coding-agent-harnesses/superclaude.md) | ✅ | Choose SuperClaude Framework when you need a persona/command/MCP framework that reshapes one agent's behavior. | Persona/command/MCP framework that reshapes one agent's behavior; GSD is more of a linear phase pipeline (discuss→plan→execute→verify) with heavy subagent fan-out and persisted spec docs. |
| [Superpowers](../coding-agent-harnesses/superpowers.md) | ✅ | Choose Superpowers when you need a broad skills/plugin library you compose à la carte. | A broad skills/plugin library you compose à la carte; GSD is an opinionated end-to-end project loop rather than a grab-bag of capabilities. |
| [Compound Engineering](../coding-agent-harnesses/compound-engineering.md) | ✅ | Choose Compound Engineering when you need a plugin encoding a compounding "agents improve the system" philosophy. | Plugin encoding a compounding "agents improve the system" philosophy; overlapping spec-driven goals, lighter surface than GSD's full toolchain. |
| [12-Factor Agents](12-factor-agents.md) | ✅ | Choose 12-Factor Agents when you need principles for building reliable agents, not an installable command set. | Principles/methodology doc for building reliable agents, not an installable command set; read it for the *why*, use GSD for an executable *how*. |
| [ECC](../coding-agent-harnesses/ecc.md) | ✅ | Choose ECC when you need a sibling agent-dev methodology with a different orchestration model. | Sibling agent-dev methodology with a different orchestration model; compare phase/context handling directly. |
| [Spec Kit](spec-kit.md) | ✅ | Choose Spec Kit when you need a vendor-backed spec-driven toolkit (`/specify`, `/plan`, `/tasks`). | Vendor-backed spec-driven toolkit (`/specify`, `/plan`, `/tasks`); GSD positions itself as lighter and more context-engineering-focused, less ceremony. |
| [BMAD-METHOD](bmad-method.md) | ✅ | Choose BMAD-METHOD when you need an agile-agent framework with explicit PM/architect/dev/QA roles. | Agile-agent framework with explicit roles (PM/architect/dev/QA); heavier "run a software org" framing GSD deliberately rejects. |

## Tech stack

- **Language:** JavaScript (~73%) + TypeScript (~26%) + Shell (repo language stats, 2026-06).
- **Distribution:** npm package `get-shit-done-cc`; installer CLI `bin/install.js` (also exposes `gsd-sdk` / `gsd-tools` bins).
- **SDK:** a TypeScript `sdk/` package (built via `npm run build:sdk`) providing query/state tooling and freshness checks; hooks are generated via `scripts/build-hooks.js`.
- **Installed artifacts:** slash commands / skills (`commands/`, emitted as `skills/gsd-*/SKILL.md` on newer Claude Code & Codex), subagents (`agents/gsd-*.md`), hooks, and runtime-specific config (e.g. `.clinerules` for Cline).
- **Targets:** Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, Antigravity, Augment, Trae, CodeBuddy, Cline (per README install matrix).
- **State model:** plain-markdown SSOT docs (`PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, per-phase `CONTEXT/RESEARCH/PLAN/SUMMARY/VERIFICATION/UAT`) under a `.planning/` tree.

## Dependencies

- **Runtime:** Node.js ≥ 22 (per `package.json` `engines`) to run the installer and SDK; Mac/Windows/Linux.
- **An agent CLI:** one of the supported coding agents above is required at run time — GSD is the prompt/orchestration layer, the agent does the work.
- **npm deps:** `@anthropic-ai/claude-agent-sdk`, `ws`; optional `fallow`; dev/test via `c8`/`vitest`.
- **Install:** `npx get-shit-done-cc@latest` (interactive runtime + global/local prompts), or non-interactive flags like `npx get-shit-done-cc --claude --global`.
- **Recommended mode:** the docs intend Claude Code run with `--dangerously-skip-permissions` (or a curated `allow` list) for friction-free autonomy.

## Ops difficulty

**Low to medium.** Day-one install is a single `npx` command and the artifacts are just files dropped into your agent's config dir — no servers, no datastore. The medium comes from operating it well: running an agent in skip-permissions mode (a real blast-radius decision), the per-phase discipline (you must actually fill `CONTEXT.md` to get good output, not just defaults), keeping up with a fast release cadence, and — most acutely right now — tracking the repo relocation so you're installing from the maintained source. [未验证] Token/system-prompt overhead and exact runtime behavior vary by agent and version.

## Health & viability

- **Responsiveness**: Grade E.
- **Maintenance (2026-06):** facts row reports the `gsd-build/get-shit-done` repo as **archived (true)** as of this verification, with last push 2026-05 — and the `main` README is now a redirect to a *different* org (`open-gsd/gsd-core`). Read this repo as **frozen/relocated**: development appears to have moved (or forked) elsewhere, so the live source of truth is likely no longer this URL — confirm before installing.
- **Governance & continuity:** Organization-owned (gsd-build), but the redirect-plus-archive split signals an in-flight org migration/fork rather than stable stewardship. This is a **continuity red flag**: who owns the roadmap and where releases land is currently ambiguous.
- **Age & Lindy (2026-06):** created 2025-12, ~6 months old — and the canonical repo is already archived. Lindy verdict: **fails the prior on this URL** — young *and* abandoned-here is the worst quadrant; any viability now lives entirely in the successor repo (`open-gsd/gsd-core`), which must be assessed on its own.
- **Risk flags:** the archived/redirect split-brain is the dominant risk (install from a dead source). Secondary: the README's `$GSD` Solana token branding — MIT software is usable without it, but the memecoin association is a governance/optics flag for some orgs. No CVEs were reviewed.

## Caveats (unverified)

- [未验证] GitHub stargazer count (~64.5k as of 2026-06) — star counts are unreliable and date-sensitive; treat as indicative only.
- [未验证] Latest tagged GitHub release is v1.42.3 (2026-05-16) while `package.json` shows `1.50.0-canary.0`; the published npm "latest" may differ from both — verify the actual installed version before relying on a feature.
- [推断] The `main` README being a redirect-to-`open-gsd/gsd-core` stub while GitHub reports the repo as not archived indicates an in-progress relocation or fork; which org/repo is the live source of truth is not fully clear from the metadata alone.
- [未验证] The supported-runtime list, command names, and subagent roster are taken from the repo's own README/tree and shift release-to-release; confirm against the current source for your runtime.
- [未验证] Claims that the fresh-context-per-plan design "fights context rot" and yields better results are the project's own framing plus third-party testimonials; no independent benchmark verified here. LLM behavior is not guaranteed.
- [未验证] The `$GSD` Solana token referenced in the README is associated with the project's branding; its relationship to the MIT-licensed software (governance, funding) is not detailed in the material reviewed.
