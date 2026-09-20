---
name: Claude Octopus
slug: claude-octopus
repo: https://github.com/nyldn/claude-octopus
category: orchestration-and-review
tags: [claude-code, plugin, multi-model, orchestration, slash-commands, blindspot, mcp]
language: Shell
license: MIT
maturity: v9.45.0, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-25T02:50:04Z
  default_branch: main
  default_branch_sha: 239263db9db25590b0386dbdbb38d0a6fface5c6
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:25:37Z
  overall: B
  overall_score: 2.8
  scored_axes: 5
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
        median_ttfr_hours: 0.3
        qualifying_issues: 47
        band: default
        window_offset_days: 3
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 169
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 14
        top1_share: 0.94
        top3_share: 0.968
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
    adoption: { reason: registry_no_counts }
---

# Claude Octopus

A Claude Code plugin that fans a single task out to up to ~8 other AI models (Codex, Gemini, Perplexity, Ollama, OpenRouter, etc.) and uses their disagreement as a blindspot/consensus gate, all driven by `/octo:*` slash commands.

![claude-octopus — health radar](../../../../assets/health/claude-octopus.svg)

## When to use

You're already living inside Claude Code as your primary agent, and you've been burned by a confident-but-wrong answer that shipped — a security hole Claude waved through, a dependency choice no one cross-checked, a design Claude liked but a second model would have flagged. You don't want to leave your harness and paste prompts into five other tools by hand; you want a second (and third, and eighth) opinion *in the same session*. Claude Octopus installs as a plugin and gives you commands like `/octo:research`, `/octo:security`, and `/octo:council` that dispatch the same task to whichever provider CLIs you have installed (Codex, Gemini, Copilot, Perplexity, Ollama, OpenRouter, Qwen, Antigravity), then has Claude synthesize the results and apply a consensus gate so split decisions surface before you merge rather than after.

It fits best when you treat the extra models as a *review/research panel* layered on top of Claude's orchestration: structured workflows like the Double Diamond (`/octo:embrace`) for end-to-end feature work, adversarial multi-provider review for code and security, and parallel research with per-model attribution. If you already pay for OpenAI/Gemini/Copilot subscriptions or run Ollama locally, you get those extra perspectives without standing up new infrastructure — Claude is the only required provider; everything else is auto-detected and optional.

## When NOT to use

- **You don't use Claude Code.** This is a Claude Code *plugin*, not a standalone orchestrator. It requires Claude Code v2.1.14+ as the host (alt installs for Cursor/OpenCode/Codex CLI exist but are secondary). If your harness is plain LangGraph/AutoGen/DSPy, this gives you nothing — see the comparison below.
- **You want a vendor-neutral multi-agent framework.** Claude is hard-wired as the required orchestrator/synthesizer; the architecture is "Claude conducts, others advise." If you need a framework where any model can be the controller, this is the wrong shape.
- **You aren't willing to install and authenticate a pile of provider CLIs.** The value is proportional to how many of `codex`/`gemini`/`agy`/`qwen`/`ollama` you have working plus API keys for Perplexity/OpenRouter. With only Claude installed, you mostly get prompt scaffolding around a single model.
- **Cost / latency sensitivity.** Fanning one task across many models multiplies token spend and wall-clock time, and pulls in paid providers (Perplexity, OpenRouter; Qwen's free OAuth tier ended Apr 2026). A consensus run is not cheap.
- **You need reproducible, auditable orchestration logic.** Behavior lives across 49+ slash commands, 32 personas, 54 skills, hooks, and an MCP server, mostly in Shell — a large, fast-moving surface (242 releases) you're coupling to. Debugging a bad dispatch means tracing through that plugin layer.
- **Single-vendor / data-egress constraints.** Routing your code and prompts to OpenAI, Google, Perplexity, OpenRouter and others may violate data-handling policy; Ollama-only mode narrows but does not eliminate this.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [oh-my-claudecode](oh-my-claudecode.md) | ✅ | Choose oh-my-claudecode when you need a Claude Code enhancement layer not centered on multi-model review. | Also a Claude Code enhancement layer (config/skills/quality-of-life), but not built around multi-model fan-out + consensus; Octopus's whole premise is *other* models reviewing Claude. |
| [DSPy](../../workflow-builders/dspy.md) | ✅ | Choose DSPy when you need a model-agnostic, library-shaped prompt/pipeline optimization framework. | Programmatic prompt/pipeline optimization framework, model-agnostic and library-shaped; you write Python, not slash commands. Different layer entirely — compilation vs. an in-harness review panel. |
| [AgentScope](../../agent-runtimes/agent-sdks/agentscope.md) | ✅ | Choose AgentScope when you need a general multi-agent runtime/library to build apps on. | General multi-agent runtime/library you build apps on; not a Claude-Code-bound plugin and not opinionated about "blindspot consensus." |
| [Symphony](../../agent-runtimes/agent-services/symphony.md) | ✅ | Choose Symphony when you need tracker-driven orchestration for coding-agent runs. | OpenAI's multi-agent orchestration; vendor-anchored on OpenAI rather than Claude, framework not plugin. |
| [openfang](../../agent-runtimes/agent-services/openfang.md) | ✅ | Choose openfang when you need a sibling agent framework with a different orchestration model. | Sibling agent framework with a different orchestration model; compare scope before picking. |
| crystal / claude-squad | 未收录 | Choose crystal or claude-squad when you need multiple parallel Claude Code sessions/worktrees. | Run multiple parallel Claude Code *sessions/worktrees*; parallelism is across Claude instances, not across *different vendors' models* reviewing one task. |

## Tech stack

- **Language:** Shell (~88% of the repo), with TypeScript (~8%, the MCP server), plus Go templates, JavaScript, and a little Python (per GitHub language stats, 2026-06).
- **Host:** Claude Code plugin — registers `/octo:*` slash commands, lifecycle hooks via `.claude-plugin/hooks.json` (session start/end, prompt submit, tool use, compaction), and an MCP server.
- **Providers (CLI-dispatched):** Claude (required, orchestrator), Codex/OpenAI, Gemini, GitHub Copilot, Perplexity, Ollama (local), Qwen, Antigravity (`agy`), OpenRouter, plus a generic OpenAI-compatible tool-loop agent (added v9.45.0).
- **Concepts:** Double Diamond workflow, 32 personas, 54 skills, a 75% consensus quality gate, a "reaction engine" for CI/review events, and optional `claude-mem` memory integration. [推断] Exact persona/skill/command counts are the project's own framing and shift release-to-release.

## Dependencies

- **Required:** Claude Code v2.1.14+ (v2.1.129+ for Anthropic-compatible gateways), and an Anthropic/Claude entitlement to run the orchestrator.
- **Optional provider CLIs (the actual value):** `codex`, `gemini`, `agy`, `qwen`, `ollama`; plus API keys for Perplexity (`PERPLEXITY_API_KEY`) and OpenRouter (`OPENROUTER_API_KEY`), and `OPENAI_API_KEY`/`GEMINI_API_KEY`/`QWEN_API_KEY` where OAuth isn't used. "Claude is required; all others are optional and auto-detected."
- **For the MCP server (Cursor/standalone):** Node.js + npm (`npm install` in `mcp-server/`).
- **State:** results in `~/.claude-octopus/results/`, logs in `~/.claude-octopus/logs/`, per-project state in `.octo/`.
- **Install:** `claude plugin marketplace add https://github.com/nyldn/plugins.git` then `claude plugin install octo@nyldn-plugins`, then `/octo:setup` inside a session.

## Ops difficulty

**Low to install, medium-to-high to run well.** Getting the plugin in is one marketplace command plus a setup wizard, and with only Claude it works out of the box. Difficulty rises with each provider you actually want contributing: installing and authenticating multiple vendor CLIs, managing several API keys/subscriptions, and reasoning about cost and latency when one command fans out to many models. The large Shell-based surface and fast release cadence (242 releases, last push 2026-06-25) mean you're maintaining against a moving target, and debugging a misfiring dispatch or hook means reading through plugin internals. Data-egress review is on you, since prompts/code leave to third-party providers.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 0.3 hours across 47 qualifying issues/PRs.
- **Maintenance — very active (as of 2026-06).** Last push 2026-06-25 with a high release cadence (242 releases, currently v9.45.0); not archived. This reads as actively, even frantically, maintained — the flip side is the churn called out under "When NOT to use."
- **Governance & bus factor — single-maintainer / personal repo.** Owned by an individual GitHub account (`nyldn`), not an org or foundation; the roadmap is one person's. For a tool you wire into every session, that is a bus-factor-of-one risk. [推断]
- **Age & Lindy — young, unproven.** Created 2026-01, ~6 months old (as of 2026-06). High activity but no track record; by the age × still-active heuristic it is "active but unproven," not a Lindy-safe bet — its longevity is undemonstrated.
- **Risk flags — fan-out surface + data egress.** The value depends on routing prompts/code to third-party providers (OpenAI/Google/Perplexity/OpenRouter), and behavior spans a large fast-moving Shell/TS surface; relicense risk is low (MIT) but operational/coupling risk is real.

## Caveats (unverified)

- [未验证] Star count ~3.7k and ~344 forks as of 2026-06 — GitHub stars in this ecosystem are unreliable and date-sensitive; indicative only.
- [未验证] "117 test suites passing," "75% consensus quality gate," "32 personas / 54 skills / 49+ commands," and "up to 8 models" are the project's own README/badge claims; not independently verified, and counts drift across releases.
- [未验证] v9.45.0 release date 2026-06-15 and the changelog items (Antigravity first-class provider, generic OpenAI-compatible agent, routing overrides) are from the GitHub release page; exact prior-version semantics not audited.
- [未验证] Provider auth details (e.g. Qwen free OAuth tier ending Apr 2026; which providers fall back to OAuth vs. require keys) come from the README and may change.
- [推断] Real-world quality uplift from multi-model "blindspot" consensus is a design claim; whether disagreement reliably catches bugs/security issues is not demonstrated by an independent benchmark here.
- [推断] The "primary language: Shell" framing reflects line counts; the orchestration semantics also live in TypeScript (MCP) and prompt/skill markdown, so language % understates where logic sits.
