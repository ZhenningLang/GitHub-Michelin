---
name: HiveChat
slug: hivechat
repo: https://github.com/HiveNexus/HiveChat
category: team-chat
tags: [team-chat, multi-llm, self-hosted, nextjs, chatbot, admin-managed]
language: TypeScript
license: Apache-2.0
maturity: v0.1.0, active, ~1.2k stars (as of 2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2025-09-16T16:08:49Z
  default_branch: main
  default_branch_sha: 9d1e8ed614923dcf74414357e0fe53f66b016c0a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:17:53Z
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
        last_commit_age_days: 290
        active_weeks_13: 0
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
        repo_age_days: 499
        last_commit_age_days: 290
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.409
        top3_share: 1.0
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
    responsiveness: { reason: no_traffic }
    adoption: { reason: no_package_structural }
---

# HiveChat

A self-hostable, admin-managed AI chat app for small-to-medium teams: one admin wires up many LLM providers (OpenAI, Claude, Gemini, DeepSeek, Ollama, OpenAI-compatible), and the whole team chats through them with per-group model access and token quotas.

![hivechat — health radar](../../assets/health/hivechat.svg)

## When to use

You're the technical lead or IT admin at a 5–50 person company, and your team keeps asking for ChatGPT/Claude access. You don't want to buy a seat of every vendor's product, hand out raw API keys, or let usage run unbounded — and you'd rather not send internal conversations through a third-party SaaS you can't audit. You want one place where *you* hold the API keys, decide which models the sales team versus the engineers can see, cap monthly tokens per group, and onboard people by Feishu/DingTalk/WeWork login instead of yet another password.

HiveChat is built for exactly this shape. You deploy it once (Docker Compose with a bundled Postgres, or one-click on Vercel), hit `/setup` to create the admin account with an `ADMIN_CODE`, then add your providers and models in the admin console. Users sign in, pick from the models you've allowed their group, and chat with image understanding, LaTeX/Markdown rendering, DeepSeek reasoning-chain display, and MCP tool servers — while you watch quotas from the admin side. It's the "self-hosted team front-end over many model APIs" niche, not a personal single-user playground and not a from-scratch chat framework.

## When NOT to use

- **You're a single user wanting a local/personal chat client.** The whole model is admin-over-team (Postgres, user groups, quotas, a `/setup` admin flow). For one person, a desktop client like Cherry Studio, Chatbox, or LibreChat-as-personal is lighter.
- **You need an on-device, no-server, offline setup.** HiveChat mandates a PostgreSQL backend and a running Node/Next.js server; there is no SQLite or fully-local single-binary mode.
- **You want a mature, battle-tested platform with a long release history.** It is at `v0.1.0` with no published git tags/releases, and the default branch was last pushed 2025-09 — early-stage, single-vendor pace.
- **You need a custom license-clean fork or to resell a derivative.** The license is Apache-2.0 *with added commercial conditions*: building and distributing a derivative work requires a separate commercial license from the author. This is not vanilla Apache-2.0.
- **You want pluggable enterprise SSO beyond the built-ins (SAML/OIDC/LDAP).** Auth is email/password plus Feishu, DingTalk, and WeChat Work; generic enterprise IdP integration is not advertised.
- **You need a self-hosted RAG / document-knowledge platform.** It's a chat front-end over model APIs (plus MCP tools), not a document-ingestion / vector-search knowledge base.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [LibreChat](../llm-chat-ui/librechat.md) | ✅ | Choose LibreChat when you need a more mature, larger feature surface with RAG, assistants, code interpreter, and many auth backends. | MIT-licensed and broader, but heavier to operate and less opinionated toward HiveChat's small-team admin-quota flow. |
| [Open WebUI](../llm-chat-ui/open-webui.md) | ✅ | Choose Open WebUI when local-model serving, RBAC, and pipelines matter more than multi-cloud provider quotas. | Broader and more active, but its sweet spot is Ollama/local-model serving rather than HiveChat's per-group quota framing. |
| Lobe Chat | 未收录 | Choose Lobe Chat when you need a polished multi-provider UI with plugins and self-hosting for personal/prosumer use. | Less centered on centralized admin-managed team governance with token quotas. |
| Chatbox / Cherry Studio | 未收录 | Choose desktop clients when each person brings their own key and central governance is unnecessary. | No central admin, groups, quotas, or shared server. |
| ChatGPT Team / Claude Team (SaaS) | 未收录 | Choose managed SaaS teams when zero-ops and a single model family are acceptable. | HiveChat trades that convenience for self-hosting, multi-provider choice, and key/data control. |

## Tech stack

- **Language:** TypeScript (~99% of the repo), with small CSS/JS/Dockerfile.
- **Framework:** Next.js 14 (App Router) + React 18; Ant Design 5 + Tailwind CSS for UI.
- **Auth:** NextAuth (next-auth 5 beta) with the Drizzle adapter; email/password plus Feishu/DingTalk/WeChat Work.
- **Data:** PostgreSQL via Drizzle ORM (`postgres` / `@neondatabase/serverless` drivers); `drizzle-kit` for schema push and seed scripts.
- **Model SDKs:** `@anthropic-ai/sdk`, `openai`, `@google/generative-ai`, plus OpenAI-compatible HTTP for the long tail (DeepSeek, Moonshot, Volcano, Qianfan, Hunyuan, Zhipu, OpenRouter, Grok, Ollama, SiliconFlow, custom).
- **Extras:** `@modelcontextprotocol/sdk` (MCP, SSE mode), KaTeX + react-markdown/rehype for math/Markdown, `@agentic/tavily` for web search, `sharp` for images, Zustand for state.

## Dependencies

- **Runtime:** Node.js (Next.js 14 server) — must run a persistent server process; not a static site.
- **Database:** PostgreSQL is mandatory. Self-host with bundled Postgres via Docker Compose, or use Neon serverless Postgres on the Vercel one-click path. Schema must be initialized/migrated with `npm run initdb` (also re-run on version upgrades).
- **Config:** environment variables including `ADMIN_CODE` for first-run admin creation via the `/setup` route; provider API keys are entered/stored through the admin console.
- **Optional:** Ollama or any OpenAI-compatible endpoint for local/extra models; MCP servers (SSE) for tools; Tavily key for web search.

## Ops difficulty

**Low-to-medium.** The happy path — `docker compose up -d` (app + Postgres), set `ADMIN_CODE`, run `initdb`, visit `/setup` — is genuinely simple for a single small deployment, and the Vercel + Neon route removes server management entirely. It rises toward **medium** once you self-host the database for real: you own Postgres backups, migrations on each upgrade (`initdb` must be re-run, and there are no versioned releases to pin, so you track a moving `main`), TLS/reverse-proxy, secret storage for many provider keys, and the enterprise-login (Feishu/DingTalk/WeWork) callback configuration. As an early-stage `v0.1.0` single-vendor project, expect to read source and follow the repo for breaking changes.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance — coasting, not clearly active.** Last pushed **2025-09**, ~9 months stale as of 2026-06; not archived, but a multi-quarter gap with no commits is a coasting/dormancy signal, not "active". There are **no git tags or GitHub releases** at all — version is `0.1.0` from `package.json`, so you track a moving (and idle) `main` with no semver to pin. `[未验证]`
- **Governance / bus factor — single-vendor, tiny.** **Organization**-owned (`HiveNexus/HiveChat`) but ~1.2k stars [未验证] and early-stage single-vendor pace; the roadmap is one small team's. Low adoption + dormancy is a real abandonment-risk combination here.
- **Age & Lindy — young (created 2025-02, ~1.3 years) and now quiet.** Not old enough for a Lindy prior, and the recent quiet erodes even that — a young project that stops pushing trends toward the "fails Lindy" quadrant, not the "strong Lindy" one. Verify the repo is still moving before betting a team deployment on it.
- **Risk flags — non-vanilla license.** Stated Apache-2.0 **with added commercial conditions**: building/distributing a derivative requires a separate commercial license from the author [未验证]. This is *not* plain Apache-2.0 — read `LICENSE` before any commercial or fork/resell use. Self-hosting for internal use appears unaffected, but confirm.

## Caveats (unverified)

- [未验证] Star count ~1.2k and `pushedAt` 2025-09-16 are from the GitHub API on 2026-06-26; GitHub stars are unreliable and dates drift — re-verify against the live repo.
- [未验证] Version is `0.1.0` from `package.json`; the repo publishes **no** git tags or GitHub releases, so there is no semver release history to anchor maturity — treat "active" cautiously given the last push predates this verification.
- [未验证] License is Apache-2.0 **with additional commercial conditions** (the `LICENSE` file restricts building/distributing derivative works without a separate commercial license); the SPDX frontmatter says `Apache-2.0` for tooling, but the real terms are not plain Apache-2.0 — read `LICENSE` before any commercial/derivative use.
- [未验证] The exact list of supported model providers, auth integrations (Feishu/DingTalk/WeWork), and capabilities (MCP SSE, image understanding, web search) is taken from the README; verify each against the current code/admin UI before relying on it.
- [推断] Comparison verdicts (LibreChat/Open WebUI/Lobe Chat being broader or more mature, desktop clients lacking central admin) reflect general project positioning, not a benchmarked head-to-head; Open WebUI is indexed here, while LibreChat, Lobe Chat, desktop clients, and SaaS team products are not.
- [推断] "Small-to-medium team" sizing (≈5–50 people) is illustrative framing, not a documented hard limit; no published scale/load numbers were found.
