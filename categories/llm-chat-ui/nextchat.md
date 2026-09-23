---
name: NextChat
slug: nextchat
repo: https://github.com/ChatGPTNextWeb/NextChat
category: llm-chat-ui
tags: [llm-chat-ui, self-hosted, multi-provider, byok, cross-platform, nextjs, vercel, mcp]
language: TypeScript
license: MIT
maturity: v2.16.1, active (2026-05), ~88.3k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2026-05-15T01:19:01Z
  default_branch: main
  default_branch_sha: 89b8f26ff8f03a0c5b98fc3026d980721495227e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:45:49Z
  overall: B
  overall_score: 3.0
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 43
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 339.8
        qualifying_issues: 5
        band: relaxed_solo
        window_offset_days: 5
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: null
        canonical_package: null
        release_downloads: 694015
        release_assets: 642
        release_tier: C
        signal_basis: releases
    longevity:
      grade: A
      raw:
        repo_age_days: 1292
        last_commit_age_days: 43
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.944
        top3_share: 1.0
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

# NextChat

A light, cross-platform (Web/iOS/macOS/Android/Linux/Windows) self-deployable AI chat client that fronts many providers (OpenAI/Claude/Gemini/DeepSeek/Ollama/…) with one-click Vercel deploy and bring-your-own-key.

![nextchat — health radar](../../assets/health/nextchat.svg)

## When to use

You want a private ChatGPT-style chat UI that you control, fronting whatever model APIs you already pay for, without sending your conversations through a vendor's SaaS. You have an OpenAI key, an Anthropic key, maybe a local Ollama box, and you'd rather not juggle a different app per provider or keep raw keys in a desktop client. You click "Deploy to Vercel", paste your `OPENAI_API_KEY` (and optionally a `CODE` access password so the public URL isn't open to the world), and within minutes you have a fast PWA chat front-end — markdown, prompt templates, local conversation history in the browser, and a model picker that spans OpenAI, Claude, Gemini, DeepSeek, and more. Data lives in your browser's local storage, not a server you have to back up.

You also reach for it as a shareable team deployment in the cheap-and-cheerful sense: a small group fronting a shared gateway or a single set of provider keys behind one `CODE` password, plus the native desktop and mobile builds when people want an app icon instead of a tab. It's the "deploy in five minutes, point it at my keys" option — the floor of self-hosted chat UIs, not a platform you administer.

## When NOT to use

- **You need a multi-user platform with RBAC, per-user accounts, and token quotas.** The community edition is single-user-shaped: one `CODE` password gates the whole instance, with no user accounts, no per-group model access, no usage caps. For centralized admin-over-team governance, use [HiveChat](../team-chat/hivechat.md) or LibreChat. (NextChat does advertise a separate paid Enterprise Edition for permission control; that is not this open-source repo. [未验证])
- **You're deploying the pure front-end and worried about key exposure.** On a static/Vercel deploy where the browser talks to providers, your API key and proxy config can be reachable client-side; the `CODE` password gates access but is not real per-user auth. Put it behind a server-side proxy or gateway, and never expose an unprotected instance with a real key. [未验证]
- **You want an agent framework or orchestration layer.** It's a chat client, not a place to build tools, multi-step agents, or RAG pipelines. It has MCP client support, but it is not an agent runtime — for that, reach for an agent framework.
- **You need a model server.** NextChat runs *no* models; it calls provider APIs (or your Ollama/OpenAI-compatible endpoint). The inference backend is yours to supply.
- **You need a self-hosted knowledge base / document RAG.** No built-in vector store or document ingestion; it's a conversational front-end, not a retrieval platform.
- **You depend on a heavyweight governance/audit story.** Single-vendor open-source project with a fast-moving `main`; conversation history is client-local by default, so there's no central audit log or server-side retention to govern.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [LibreChat](librechat.md) | ✅ | Choose LibreChat when you need a full multi-user platform rather than a lightweight single-deploy client. | Accounts, many auth backends, RAG, assistants, and code interpreter; far more capable and far heavier to run. NextChat is a lighter client, not a team platform. |
| Lobe Chat | 未收录 | Choose Lobe Chat when you want a polished multi-provider UI with plugins, knowledge base, and optional multi-user modes. | Broader feature surface and heavier once cloud/DB features are enabled. NextChat stays minimal and browser-local. |
| [Open WebUI](open-webui.md) | ✅ | Choose Open WebUI when Ollama/local-model serving, RBAC, users, and pipelines matter more than a static/Vercel-style client. | Strong self-hosted UI for local models, but it needs a server and database. NextChat trades those features for simpler deployment and less backend operation. |
| [HiveChat](../team-chat/hivechat.md) | ✅ | Choose HiveChat when you need admin-managed team chat with per-group model access, token quotas, and Postgres-backed user accounts. | HiveChat is the team-governance answer NextChat's community edition deliberately is not. |
| ChatGPT / Claude.ai (commercial SaaS) | 未收录 | Choose commercial SaaS when zero-ops vendor management is more important than self-hosting and provider choice. | Locked to one model family with the provider holding your data; NextChat trades that convenience for self-hosting, multi-provider choice, and key/data control. |

## Tech stack

- **Language:** TypeScript (~91%), with CSS/JS and platform packaging.
- **Framework:** Next.js + React; ships as a PWA web app and as native desktop/mobile builds (Tauri for desktop).
- **Storage:** conversation history and settings in browser local storage by default — no required server-side database for the community edition.
- **Providers:** OpenAI, Claude (Anthropic), Gemini (Google), DeepSeek, Baidu, ByteDance, Alibaba, ChatGLM, Groq, Ollama, and OpenAI-compatible endpoints.
- **Extras:** prompt templates/masks, markdown rendering, MCP (Model Context Protocol) client support, artifacts/plugins. [未验证]

## Dependencies

- **Runtime:** to self-host beyond Vercel you run a Node/Next.js process (or the published Docker image); the desktop/mobile apps are standalone builds. No database is required for the community edition.
- **Provider keys (yours to supply):** at minimum `OPENAI_API_KEY`, plus keys/base-URLs for any other providers you enable. NextChat calls these APIs; it does not host models.
- **Access control:** an optional `CODE` environment variable sets an access password for a public deployment — this is the only built-in gate, not per-user auth.
- **Install paths:** one-click Vercel deploy, Docker image, and prebuilt desktop/mobile apps; build from source needs a Node toolchain.

## Ops difficulty

**Low.** This is the project's whole point — the Vercel one-click path gives you a running instance with no server to manage, and the Docker image is a single container with no database. Day-2 burden is mostly: rotating provider keys, setting a strong `CODE` password (and ideally fronting it with a gateway so keys aren't client-reachable), and tracking a fast-moving `main`/release cadence on a single-vendor project. Because state is browser-local, there's nothing to back up server-side — which is also why it doesn't scale into multi-user territory: there's no central data layer to govern. The hard part isn't running NextChat; it's recognizing when "shared password over my keys" has outgrown its limits and you need a real team platform instead.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 339.8 hours across 5 qualifying issues/PRs.
- **Maintenance — active but coasting on releases (as of 2026-06).** Repo pushed 2026-05, so the codebase is alive; but the latest tagged release (v2.16.1) is reported 2025-07-29 — roughly a year stale, so you'd be tracking a fast-moving `main` rather than cut releases. Not archived. [未验证]
- **Governance & bus factor — single-vendor, open-core-adjacent.** Organization-owned (the ChatGPTNextWeb / NextChat org), so not literally a single User repo, but it is effectively one vendor's project, and that vendor monetizes a separate paid Enterprise Edition. The OSS community edition's roadmap is theirs to set; treat governance as vendor-controlled, not foundation-style. [推断]
- **Age & Lindy — moderate.** Created 2023-03, ~3 years old and still maintained; old enough to have outlived the first wave of ChatGPT-clone UIs, young enough that this category churns fast. A reasonable but not blue-chip Lindy bet — its durability rests on the vendor's continued interest. [推断]
- **Adoption & ecosystem.** Very high star count (~88k) and broad multi-provider support signal strong mindshare as the "deploy-in-five-minutes" floor of self-hosted chat UIs; but stars overstate active maintenance, and the feature surface is deliberately thin vs. LibreChat/Lobe/Open WebUI.
- **Risk flags — open-core boundary.** The paid Enterprise Edition (permissions/RBAC) is the gated tier; capabilities you might expect (multi-user auth) live behind it, not in this MIT repo. No relicense or CVE history asserted here. The stale-release vs. live-`main` gap is itself a supply-chain/stability flag if you pin to releases.

## Caveats (unverified)

- [未验证] ~88.3k stars, latest release v2.16.1 (2025-07-29), and recent activity (2026-05) are from the GitHub page on 2026-06-28; star counts and dates drift — re-verify against the live repo.
- [未验证] Tauri for the desktop builds, the exact MCP/artifacts/plugins surface, and the precise provider list are taken from the README/repo framing; verify each against the current code before relying on it.
- [未验证] The "key-exposure on pure-frontend deploys" caution reflects how a browser-to-provider static deploy works in general; the exact exposure depends on your deployment topology (server-side proxy vs. direct), so audit your own setup rather than assuming.
- [未验证] A paid Enterprise Edition with permission control is advertised by the project (business@nextchat.dev); it is separate from this MIT open-source repo and its terms were not verified here.
- [推断] "Single-user-shaped community edition" is inferred from the `CODE`-password-only access model and browser-local storage, not from a documented hard limit on concurrent users.
- [推断] Comparison verdicts (LibreChat/Lobe Chat/Open WebUI being broader or heavier) reflect general project positioning, not a benchmarked head-to-head; Open WebUI and HiveChat are indexed here, while LibreChat and Lobe Chat are not.
