---
name: Claude Code Router
slug: claude-code-router
repo: https://github.com/musistudio/claude-code-router
category: api-gateway
tags: [claude-code, coding-agent, llm-router, model-routing, local-proxy]
language: TypeScript
license: MIT
maturity: v3.1.1, active, 37k stars, created 2025-02 (as of 2026-09)
last_verified: 2026-09-19
type: tool
upstream:
  pushed_at: 2026-09-18T02:27:33Z
  default_branch: main
  default_branch_sha: a034b0c51cdd1b5628bbff545821f5540d30c6c5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T11:26:30Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 38.0
        qualifying_issues: 19
        band: relaxed_solo
        window_offset_days: 10
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: "@musistudio/claude-code-router"
        dependent_repos_count: 0
        downloads_last_month: 398338
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
    longevity:
      grade: B
      raw:
        repo_age_days: 571
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 37
        top1_share: 0.782
        top3_share: 0.846
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

# Claude Code Router

A local control plane and proxy that points Claude Code — and other coding agents — at whichever model provider you choose, adding conditional routing, protocol adaption, retries and fallback behind a desktop-or-CLI UI.

![Claude Code Router — health radar](../../assets/health/claude-code-router.svg)

## When to use

You're a developer who wants to keep using Claude Code's own workflow — slash commands, tools, sessions — but not be locked to one provider: you want the cheap model for routine edits and a strong model for hard reasoning, switchable per task or per rule, without changing clients. You reach for Claude Code Router because it is purpose-built for that client: it runs a local gateway (default `127.0.0.1:3456`) that understands the coding-agent protocol and stores its configuration in a desktop UI (SQLite at `~/.claude-code-router/config.sqlite`), so you are not operating a general gateway as a service.

The deciding tradeoff against the nearest substitutes is *scope of the layer*. Choose it over [LiteLLM](litellm.md) or [CLIProxyAPI](cliproxyapi.md) when you are redirecting one developer's coding agent and do not want to run a multi-tenant gateway with databases, virtual keys and budgets; choose it over [HarnessRouter](harnessrouter.md) when you only need model routing inside an existing client, not harness execution as a product API; choose it over [Funtool](funtool.md) when you need cross-platform, configuration-driven routing rather than one vendor's Windows proxy path.

## When NOT to use

- **One provider already meets your needs.** Use Anthropic's own Claude Code directly; a proxy adds a process, a port, credentials and an upgrade path to reach the same model.
- **You need an LLM gateway for product backends, with keys, budgets and per-team isolation.** Use [LiteLLM](litellm.md) or Portkey Gateway; Router is a local agent control plane, not a governance gateway.
- **You need to run agent tasks as a service (sessions, files, cancellation) for your app.** Use [HarnessRouter](harnessrouter.md); Router redirects a client's model calls and does not execute or host tasks.
- **You are re-exposing consumer subscription or OAuth logins to other tools.** Use provider API keys, [CLIProxyAPI](cliproxyapi.md) if you accept that risk, or a hosted gateway; whether subscription proxying is permitted by each vendor is not established here. [未验证]
- **You cannot tolerate protocol-conversion loss.** Use the provider's native API; open issues report images silently dropped on cross-protocol routes and fallback chains that fail to switch provider.
- **You do not want a local proxy with a CA/MITM path and a SQLite config file.** Use a hosted router such as OpenRouter; the local setup is what gives you control and what you must maintain.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [LiteLLM](litellm.md) | ✅ | When one gateway must serve many applications with virtual keys, budgets and spend tracking, choose LiteLLM; choose Router when the job is one developer's coding agent and the overhead of a governed server is not wanted. | LiteLLM brings PostgreSQL/Redis and a heavier feature surface but real multi-user controls; Router stays local and simple, and offers none of that governance. |
| [CLIProxyAPI](cliproxyapi.md) | ✅ | When you want to reuse several CLI/OAuth accounts as a broad multi-protocol API, choose CLIProxyAPI; choose Router when you want configuration-driven model routing inside Claude Code itself. | CLIProxyAPI covers more upstream CLI products and API shapes; Router is narrower but keeps the routing decision inside the coding-agent workflow. |
| [HarnessRouter](harnessrouter.md) | ✅ | When your product must run whole agent tasks behind an API, choose HarnessRouter; Router is for redirecting a client you already run. | HarnessRouter owns sessions, files and workspaces and therefore has far more operational surface; Router is a request path only. |
| [Funtool](funtool.md) | ✅ | When the exact Windows + Claude Code + vendor-endpoint path is all you need and a prebuilt binary is acceptable, choose Funtool; choose Router for cross-platform, configuration-driven routing. | Funtool is a narrow opaque binary; Router is inspectable TypeScript with a UI, at the cost of a Node/Electron stack and a larger config surface. |
| OpenRouter | not indexed | When you would rather not run any local router and accept a hosted broker, choose OpenRouter; choose Router when provider credentials and routing must stay on your machine. | OpenRouter removes local ops and adds a third party in the request path plus per-token margin; Router keeps credentials local but makes you the operator. |

## Tech stack

- **Language/shape:** TypeScript monorepo; Node.js 22+ CLI, plus an Electron 42 desktop application with a React 18 / Base Web / Tailwind 4 UI.
- **Local gateway:** listens on `127.0.0.1:3456` by default (management UI `3458`); handles conditional routing, model chains and fallback, and can run in MITM-proxy mode with a CA certificate for clients that need interception.
- **State/config:** a SQLite database at `~/.claude-code-router/config.sqlite` written by the UI; the legacy `config.json` is migration-only. Runtime deps include `better-sqlite3`, `undici` and `node-forge`.
- **Distribution:** release binaries, `npm install -g @musistudio/claude-code-router`, or Docker.

## Dependencies

- **Node.js 22+** for the CLI path, or the packaged desktop binary.
- **Provider credentials** for every model you intend to route to; Router stores and forwards them.
- **Local ports** `3456` (gateway) and `3458` (management), and a CA certificate install if you enable MITM interception.
- **A local SQLite file and its backups** — the configuration lives there, so losing it means rebuilding routing rules.

## Ops difficulty

**Low to medium.** For a single developer it is a local process with a UI: start it, pick providers, run Claude Code through it. The ongoing costs are upgrade churn (25 releases in the last 90 days), keeping the SQLite config backed up, and watching the route semantics — recent issues report fallback not switching provider (#1804), cross-protocol images being silently dropped (#1678), and global agent configuration being taken over (#1575). Treat the local gateway as credential-bearing infrastructure: a past advisory (GHSA-8hmm-4crw-vm2c) let a CORS misconfiguration expose API keys before 1.0.34, which is the class of risk that comes with a loopback proxy holding provider secrets. [未验证] whether the three issues above are fixed in v3.1.1.

## Health & viability

- **Maintenance, as of 2026-09:** latest release v3.1.1 (2026-09-16) with about 25 releases in the previous 90 days — very active, not coasting.
- **Governance and bus factor:** 58 named contributors, but the top contributor holds roughly 76.7% of commits (next two at 3.1% and 2.0%). Effectively a single-maintainer project; continuity depends on one person. [推断]
- **Backing and longevity:** an independent maintainer project (homepage `ccrdesk.top`), not a foundation or a funded vendor; started 2025-02, so roughly 1.6 years old and active — a moderate Lindy position, neither young-and-unproven nor long-established.
- **Adoption:** about 37k stars and 3.1k forks against 140 watchers. Forks and stars indicate real use, but the watcher ratio is low, so part of the attention is likely promotional. [推断]
- **Risk flags:** MIT with no `enterprise/` directory or CLA found in-tree; a low-severity advisory (CVE-2025-57755 / GHSA-8hmm-4crw-vm2c, CORS could expose API keys, fixed in 1.0.34); a large open-issue backlog (1,132).

## Caveats (unverified)

- [未验证] Whether forwarding consumer subscription/OAuth credentials is permitted by each upstream vendor; the README does not claim provider authorization, and ban rates are not established.
- [未验证] Whether issues #1804 (fallback not switching provider), #1678 (silent image loss across protocols) and #1575 (agent config takeover) are resolved in v3.1.1; they were open at research time.
- [推断] Single-maintainer concentration (~77% of commits) is a continuity risk if that maintainer steps away.
- [推断] The low watcher-to-star ratio (140 watchers vs ~37k stars) suggests a meaningful share of stars came from promotion rather than sustained use.
- [未验证] Whether an external or private CLA exists; only the in-tree MIT LICENSE was confirmed.
- [未验证] This page did not install or run Router, so runtime behaviour and the practical severity of the issues above are taken from the repository and issue tracker, not from a reproduction.
