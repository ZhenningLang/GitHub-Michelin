---
name: oh-my-claudecode
slug: oh-my-claudecode
repo: https://github.com/Yeachan-Heo/oh-my-claudecode
category: orchestration-and-review
tags: [claude-code, multi-agent, orchestration, plugin, tmux, parallel-execution]
language: TypeScript
license: MIT
maturity: v4.15.0, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-29T11:19:35Z
  default_branch: main
  default_branch_sha: 6c59219cced3ddd857334d2a7fb78099f2d67e71
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T03:10:49Z
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.6
        qualifying_issues: 38
        band: default
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 257
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 99
        top1_share: 0.792
        top3_share: 0.84
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
    adoption: { reason: ambiguous }
---

# oh-my-claudecode

A multi-agent orchestration layer for Anthropic's Claude Code CLI: it stages teams of specialized agents (plan → prd → exec → verify → fix), routes each subtask to a cheaper or stronger model, and runs parallel workers under tmux — installed as a Claude Code plugin or via the `oh-my-claude-sisyphus` npm package.

![oh-my-claudecode — health radar](../../../../assets/health/oh-my-claudecode.svg)

## When to use

You're a developer who lives in Claude Code and keeps hitting the ceiling of a single agent on bigger work: a multi-file feature where you want one pass to plan, another to write the PRD, parallel workers to implement, and a separate reviewer/tester to verify — all without hand-copying context between chat sessions or babysitting each step. You also notice you're burning Opus tokens on trivial edits that Haiku could handle. oh-my-claudecode (OMC) sits on top of Claude Code and gives you a canonical "team" pipeline (`team-plan → team-prd → team-exec → team-verify → team-fix`) plus model routing that pushes simple work to cheaper tiers and reserves the expensive model for hard reasoning, with a HUD statusline so you can watch what each agent is doing.

You reach for it specifically when you want orchestration *inside the Claude Code ecosystem you already pay for* — your Max/Pro subscription or API key — rather than standing up a separate Python agent framework with its own runtime. You install it as a plugin (`/plugin install`) or `npm i -g`, run `/setup`, and from then on drive it in natural language or via slash commands (`/team`, `/autopilot`, `/ralph`); for the tmux-backed parallel CLI workers you use `omc team`. It's a good fit when your bottleneck is *coordinating Claude agents*, not building a general-purpose multi-LLM application.

## When NOT to use

- **You're not on Claude Code.** OMC is a Claude Code plugin / companion CLI. If you orchestrate agents with arbitrary LLM providers in your own app, you want a general framework ([DSPy](../../workflow-builders/dspy.md), [AgentScope](../../agent-runtimes/agent-sdks/agentscope.md)), not a Claude-Code-bound layer. There is no provider-agnostic core here.
- **You can't run tmux.** The parallel `omc team` workers and rate-limit detection lean on tmux; on constrained CI, locked-down corporate shells, or pure-Windows setups, expect friction. Recent releases are still hardening Windows/tmux paths, so treat cross-platform parallelism as not-yet-settled.
- **You need a stable, slow-moving API to build a product on.** The project ships aggressively (multiple releases a month, many "N features / many fixes" patches) and exposes a wide, fast-evolving surface — 19 agent roles, multiple execution modes (Autopilot, Ralph, Ultrawork, UltraQA), keyword triggers. That velocity is great for a power user but is churn you'd be coupling to.
- **You want one auditable, deterministic agent loop.** A staged multi-agent pipeline with automatic model routing and parallel workers is inherently harder to reason about and reproduce than a single-agent script; debugging "which agent did what at which tier" adds surface area.
- **You're a single-author, single-maintainer risk-averse shop.** This is effectively a one-person project [推断]; bus-factor and long-term support are real considerations for anything load-bearing.
- **Cost is fully predictable already.** The "saves 30-50% on tokens" claim is the project's own framing and depends entirely on your workload; if you already control model selection by hand, the routing buys you less.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [DSPy](../../workflow-builders/dspy.md) | ✅ | Choose DSPy when you need a provider-agnostic Python framework for programming/optimizing LLM pipelines. | Provider-agnostic Python framework for programming/optimizing LLM pipelines; you build the app yourself. OMC is narrower: orchestration *inside Claude Code*, no model-program compilation. |
| [AgentScope](../../agent-runtimes/agent-sdks/agentscope.md) | ✅ | Choose AgentScope when you need a general multi-agent platform you host yourself. | General multi-agent platform (any model, message-passing, visual studio); a full framework you host. OMC rides on Claude Code instead of being a standalone runtime. |
| [claude-octopus](claude-octopus.md) | ✅ | Choose claude-octopus when you need Claude-Code-centric parallel/multi-agent tooling. | Also Claude-Code-centric parallel/multi-agent tooling; closest sibling. Differs in surface and orchestration model — compare the two directly if you're already on Claude Code. |
| [Symphony](../../agent-runtimes/agent-services/symphony.md) | ✅ | Choose Symphony when you need tracker-driven coding-agent orchestration outside Claude Code. | OpenAI-authored orchestration; tied to a different vendor ecosystem than Claude Code. |
| [openfang](../../agent-runtimes/agent-services/openfang.md) | ✅ | Choose openfang when you need a separate agent-framework take with an OS-shaped model. | Separate agent-framework take; see its page for its model. |
| claude-flow | 未收录 | Choose claude-flow when you need another Claude-Code multi-agent/swarm orchestration layer. | Another popular Claude-Code multi-agent / swarm orchestration layer; overlapping problem space, different abstractions and maturity. |
| Claude Code subagents (built-in) | 未收录 | Choose built-in Claude Code subagents when native parallel/subagent features are enough and you want no third-party dependency. | Anthropic's native subagent/parallel features cover part of OMC's value without a third-party dependency; OMC adds team pipelines, routing, modes, and HUD on top. |

## Tech stack

- **Language:** TypeScript (primary, per repo metadata 2026-06-26).
- **Host:** Anthropic Claude Code CLI — distributed both as a Claude Code marketplace plugin and as an npm package (`oh-my-claude-sisyphus`).
- **Orchestration substrate:** tmux for parallel CLI workers (`omc team`) and rate-limit detection.
- **Model routing:** assigns work across Anthropic model tiers (e.g. Haiku for simple, Opus for hard reasoning) [未验证] exact routing rules.
- **Optional integrations:** other agent CLIs (Antigravity/agy, Gemini CLI, Codex CLI, Grok Build) and notification channels (Telegram, Discord, Slack) per README.

## Dependencies

- **Required:** Claude Code CLI; a Claude Max/Pro subscription **or** an Anthropic API key; Node.js (for the npm install path); **tmux** for `omc team` and rate-limit handling.
- **Install (plugin):** `/plugin marketplace add https://github.com/Yeachan-Heo/oh-my-claudecode` → `/plugin install oh-my-claudecode` → `/setup`.
- **Install (CLI):** `npm i -g oh-my-claude-sisyphus@latest` → `omc setup`.
- **Optional:** Antigravity/Gemini/Codex/Grok CLIs; notification integrations.

## Ops difficulty

**Low to medium.** The happy path is genuinely easy: install the plugin, run `/setup`, and drive it in natural language — "zero configuration" with intelligent defaults is a stated design goal. Difficulty rises to **medium** once you depend on the tmux-backed parallel workers (shell/terminal environment matters, and Windows/tmux support is still being hardened release-to-release), wire up external CLIs or notification channels, or try to pin behavior across the project's fast release cadence. Because it's a thin-ish layer over Claude Code, most "ops" is really Claude Code's auth/rate-limit reality plus keeping the plugin/npm version current.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 0.0 hours across 21 qualifying issues/PRs.
- **Maintenance — very active (as of 2026-06).** Last push 2026-06 with an aggressive release cadence (multiple releases a month, currently v4.15.0); not archived. Actively maintained, but the velocity is itself the churn flagged under "When NOT to use."
- **Governance & bus factor — single-maintainer + huge-star mismatch ⇒ red flag.** A `User`-owned repo (`Yeachan-Heo`) carrying ~37k stars is a classic bus-factor flag: one person owns the roadmap of something with disproportionate visibility. Treat the popularity as decoupled from maintenance depth before making it load-bearing. [推断]
- **Age & Lindy — young, unproven.** Created 2026-01, ~6 months old (as of 2026-06). High activity but no track record; active-but-unproven, not Lindy-safe — longevity and single-author continuity are undemonstrated.
- **Risk flags — fast-moving surface + thin layer.** MIT-licensed, low relicense risk, but it's a thin, fast-evolving layer over Claude Code (19 roles, multiple execution modes); upgrades and cross-platform (Windows/tmux) paths are still settling.

## Caveats (unverified)

- [未验证] Star count ~37k as of 2026-06-26 — GitHub stars in the Claude-Code tooling ecosystem are unreliable and date-sensitive; treat as indicative only.
- [未验证] "Saves 30-50% on tokens," "zero configuration," and "19 specialized agents" are the project's own README framing; actual savings and agent count depend on workload and version and were not independently benchmarked.
- [未验证] Exact model-routing rules (which tier gets which task) come from README descriptions, not verified against code.
- [未验证] The full set of execution modes (Autopilot, Ralph, Ultrawork, UltraQA) and keyword triggers is per README; precise behavior/availability shifts release-to-release.
- [推断] Single primary maintainer / low bus-factor — inferred from the repo owner pattern, not confirmed; verify before depending on it for production.
- [推断] Classifying it as `framework` is a judgment call — it is simultaneously a Claude Code plugin and a CLI; "orchestration framework on top of Claude Code" is the closest fit.
