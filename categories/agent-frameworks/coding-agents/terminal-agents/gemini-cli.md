---
name: Gemini CLI
slug: gemini-cli
repo: https://github.com/google-gemini/gemini-cli
category: terminal-agents
tags: [ai-agent, cli, gemini, mcp-client, mcp-server, terminal]
language: TypeScript
license: Apache-2.0
maturity: v0.x, active, 105.7k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-06T01:31:22Z
  default_branch: main
  default_branch_sha: f7af4e5180cf92eea8190e383fd5daeeb2578c2d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:36:05Z
  overall: B
  overall_score: 3.4
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
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: "@google/gemini-cli"
        dependent_repos_count: 0
        downloads_last_month: 1331337
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.02
        release_downloads: 10558
        release_assets: 290
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 523
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 79
        top1_share: 0.085
        top3_share: 0.205
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# Gemini CLI

An open-source AI agent that brings the power of Gemini directly into your terminal. Provides lightweight access to Gemini models with built-in tools, MCP support, and a free tier for personal Google accounts.

![Gemini CLI — health radar](../../../../assets/health/gemini-cli.svg)

## When to use

You're a developer who lives in the terminal and wants an AI assistant that can reason about your codebase, run shell commands, search the web, and read files — all without leaving your command line. You pick Gemini CLI over [OpenCode](opencode.md) because its generous free tier (60 req/min, 1,000 req/day with a personal Google account) eliminates the need to bring and pay for your own API keys across every model provider. You pick it over Claude Code (Anthropic's closed-source terminal agent) because Gemini CLI is open-source under Apache-2.0 and free-tier accessible, whereas Claude Code requires an Anthropic subscription. You pick it over [Open Interpreter](open-interpreter.md) when you want deep Gemini integration — especially the 1M token context window and built-in Google Search grounding — rather than a model-agnostic harness where you must configure every provider yourself. You install via npm, authenticate with your Google account, and delegate tasks: refactoring code, explaining APIs, generating tests, or fetching documentation. The MCP extensibility means you can wire it into your existing tool ecosystem without switching to a different agent framework.

## When NOT to use

- **If you need to switch between OpenAI, Anthropic, or local models** — use [OpenCode](opencode.md) or [Open Interpreter](open-interpreter.md) instead of Gemini CLI, because Gemini CLI is tightly coupled to Google's Gemini API and does not support other providers.
- **If your organization blocks Google authentication or requires enterprise SSO** — use a self-hosted platform like [Dify](https://github.com/langgenius/dify) or [n8n](https://github.com/n8n-io/n8n) instead of Gemini CLI, because the free tier requires a personal Google account and there is no RBAC or admin layer.
- **If you work in an offline or air-gapped environment** — use Ollama with a local chat UI like [Open WebUI](../../../llm-chat-ui/open-webui.md) instead of Gemini CLI, because Gemini CLI requires internet access to reach the Gemini API and does not support local model inference.
- **If you need complex multi-agent orchestration** — use LangChain or AutoGPT instead of Gemini CLI, because Gemini CLI is a single-agent CLI tool without built-in workflows for multiple collaborating agents.
- **If you need enterprise audit logging, RBAC, or compliance guarantees** — use a governed platform like Dify or n8n instead of Gemini CLI, because it is a personal developer tool with no built-in audit logging or admin controls.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [OpenCode](opencode.md) | ✅ | Open-source terminal coding agent. | OpenCode is model-agnostic and self-hostable; Gemini CLI is Google-only but offers a generous free tier and deep Gemini integration. |
| [Open Interpreter](open-interpreter.md) | ✅ | Terminal coding agent with swappable harnesses for open models. | Open Interpreter supports multiple model providers and local models; Gemini CLI is Gemini-only but has stronger Google ecosystem integration. |
| Claude Code | 未收录 | Official Anthropic terminal coding agent. | Closed-source, Anthropic-only; Gemini CLI is open-source and free-tier friendly but locked to Google models. |
| [CC Switch](../orchestration-and-review/cc-switch.md) | ✅ | Desktop manager for multiple coding agents. | CC Switch can manage Gemini CLI alongside other agents; they are complementary, not competing. |
| GitHub Copilot CLI | 未收录 | AI-powered CLI from GitHub/Microsoft. | Copilot CLI is Copilot-subscription based and IDE-integrated; Gemini CLI is standalone and free-tier accessible. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — runtime environment
- **Gemini API** — backend LLM provider (Google)
- **MCP (Model Context Protocol)** — extensibility layer for custom integrations
- **Google Search** — built-in grounding tool

## Dependencies

- Node.js runtime (npm-installable)
- A Google account (for the free tier API access)
- Internet connectivity (to reach Gemini API endpoints)
- Terminal / shell environment

## Ops difficulty

**Low**. Gemini CLI is installed via npm and runs as a local Node.js process. There is no server to maintain. The operational burden is limited to keeping the CLI updated and managing your Google API credentials. The free tier has rate limits that may require upgrading for heavy usage, but there is no infrastructure to operate.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 1 days ago.
- **Responsiveness**: Cannot be scored — no_traffic.
- **Adoption**: Grade B — 1,331,337 monthly downloads via npmjs.org (package: @google/gemini-cli).
- **Longevity**: Grade C — 523 days old.
- **Governance**: Grade A — top-3 contributor share 20.5% (?).
- **Risk / License**: Grade A — Apache-2.0 license.
## Caveats (unverified)

- [未验证] The exact relationship between `google-gemini` and the broader Google DeepMind / Gemini product organization has not been verified.
- [推断] Google has a track record of launching and later deprecating open-source and consumer projects; the long-term commitment to Gemini CLI is unproven.
- [未验证] The free tier rate limits (60 req/min, 1,000 req/day) may be reduced or changed as the product matures.
- [未验证] The MCP server ecosystem and third-party integration quality are new and unverified.
