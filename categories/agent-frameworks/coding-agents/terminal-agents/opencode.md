---
name: OpenCode
slug: opencode
repo: https://github.com/anomalyco/opencode
category: terminal-agents
tags: [coding-agent, ai-agent, terminal, cli, typescript]
language: TypeScript
license: MIT
maturity: v0.x, active, 181k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-04T12:37:42Z
  default_branch: dev
  default_branch_sha: 7a8e7c88f495acf5af3e7584e8ec1dbab2fe04ec
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:36:41Z
  overall: A
  overall_score: 3.6
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
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@opencode-ai/cli-linux-x64"
        dependent_repos_count: 0
        downloads_last_month: 554339
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.09
        homebrew_installs_90d: 94934
        homebrew_tier: A
        release_downloads: 84114151
        release_assets: 3624
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: C
      raw:
        repo_age_days: 510
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 429
        top1_share: 0.146
        top3_share: 0.417
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

# OpenCode

An open-source AI coding agent that runs in your terminal, edits files, executes commands, and works with your existing codebase. Install it via npm as `opencode-ai`.

![OpenCode — health radar](../../../../assets/health/opencode.svg)

## When to use

You are a developer who wants AI-assisted coding but refuses to be locked into a single LLM vendor. You have tried Claude Code (Anthropic-only) and Codex (OpenAI-only), and you realize that if model prices spike or capabilities regress, you are trapped with no escape. You need a model-agnostic coding agent — the same tool running GPT-4 today, Claude 3.5 tomorrow, and a local Llama model next week, entirely under your control. You choose OpenCode over Claude Code because OpenCode lets you switch models at will, while Claude Code is vendor-locked to Anthropic. You choose it over Open Interpreter because OpenCode is TypeScript/npm-based and targets the same fast-iterating JavaScript ecosystem you already work in. OpenCode is MIT-licensed, source-auditable, and extensible — you can fork it to fit your team's workflow. Install with `npm install opencode-ai`, connect an API key, point it at a repo, and it becomes a model-agnostic pair-programmer living in your shell.

## When NOT to use

- **You are already satisfied with Claude Code and trust Anthropic's roadmap** — If you only use Claude, have a fixed budget, and are confident in the vendor's direction, Claude Code is the more polished choice with Claude-specific context optimization and Artifacts integration. Switching to OpenCode adds configuration burden with no extra benefit. Stick with Claude Code instead of OpenCode, because the vendor-locked experience is superior when you do not need model freedom.
- **Your team needs seamless IDE integration** — OpenCode is a CLI tool, not a VS Code plugin. If you want to click a button in your editor to let AI rewrite code, use Kilo Code or GitHub Copilot instead of OpenCode, because their IDE-native integrations provide a smoother editing experience.
- **Non-technical users or terminal-averse team members** — Pure command-line interaction with no GUI. If someone on your team cannot use a terminal, OpenCode is a hard barrier. Use Claude web or ChatGPT instead of OpenCode, because they provide a familiar chat interface with no technical setup.
- **You need enterprise-grade governance** — No RBAC, no audit logs, no admin panel. It is a personal or small-team development tool, not an enterprise platform. If you need organizational governance, use Dify or GitHub Copilot for Business instead of OpenCode, because those platforms offer admin controls, audit trails, and team management.
- **You are 100% committed to a single model and will never switch** — OpenCode's core value is model freedom. If you know you will only ever use Claude (or only GPT-4), model-agnosticism delivers zero value. Use Claude Code or Codex CLI instead of OpenCode, because a single-vendor tool is simpler and more tightly optimized for that one model.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Open Interpreter](open-interpreter.md) | ✅ | Pick Open Interpreter when OS sandbox execution and open-model harness swapping are the priorities. | Open Interpreter is a Rust rewrite with OS sandbox execution; OpenCode is TypeScript/npm-based and integrates more naturally into JS/TS workflows. |
| [Hermes Agent](../../agent-runtimes/personal-assistants/hermes-agent.md) | ✅ | Pick Hermes when a cross-session learning loop and skill creation matter more than a focused coding agent. | Hermes focuses on skill creation and personal growth across sessions; OpenCode is a focused coding agent without a learning loop. |
| [AutoGPT](../../workflow-builders/autogpt.md) | ✅ | Pick AutoGPT for complex multi-step autonomous workflow automation rather than terminal pair-programming. | AutoGPT targets complex multi-step autonomous tasks; OpenCode is a terminal pair-programmer for code. |
| Claude Code | 未收录 | Pick Claude Code when you accept a proprietary subscription-bound terminal agent for Anthropic's managed experience. | Proprietary, no source access, subscription-bound; OpenCode is open-source and BYOK. |
| [Gemini CLI](gemini-cli.md) | ✅ | Pick Gemini CLI when Google backing and Apache-2.0 matter more than OpenCode's MIT/community model. | Apache-2.0, backed by Google; OpenCode is MIT and community-driven. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — runtime environment
- **npm** — distribution via `npm install opencode-ai`
- **Monorepo** — packages for console app and core logic

## Dependencies

- **Node.js** runtime (check package requirements for version)
- **LLM API key** — OpenAI, Anthropic, or compatible provider
- **Terminal / shell** — primary interaction surface
- **Git** — for working with repositories

## Ops difficulty

**Low**. Installation is `npm install -g opencode-ai` or similar; the agent runs as a local process with no persistent service to manage. The ongoing burden is API key rotation and keeping the npm package updated.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 1 days ago.
- **Responsiveness**: Cannot be scored — no_traffic.
- **Adoption**: Grade A — 554,339 monthly downloads via npmjs.org (package: @opencode-ai/cli-linux-x64).
- **Longevity**: Grade C — 510 days old.
- **Governance**: Grade A — top-3 contributor share 41.7% (429 active maintainers in the trailing 12 months).
- **Risk / License**: Grade A — MIT license.
## Caveats (unverified)

- [推断] 181k GitHub stars on a repo created in April 2025 may be inflated by hype rather than organic production adoption.
- [未验证] The exact npm package name and installation path may change as the project is still in v0.x.
- [未验证] Multi-language README support (18+ languages listed) suggests global ambition, but the depth of non-English documentation quality is unverified.
- [未验证] The relationship between `anomalyco` and any commercial entity or monetization plan is not publicly documented.
