---
name: deep-research
slug: deep-research
repo: https://github.com/dzhng/deep-research
category: deep-research
tags: [research-agent, firecrawl, vercel-ai-sdk, typescript, iterative-search]
language: TypeScript
license: MIT
maturity: untagged (no GitHub releases), active, last pushed 2026-04 (as of 2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-04-11T23:58:25Z
  default_branch: main
  default_branch_sha: 1f8f3e285bbc23e80b98a66a64effab9069f3ad4
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:18:42Z
  overall: C
  overall_score: 2.25
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 82
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
        repo_age_days: 514
        last_commit_age_days: 82
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
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
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: no_package_structural }
---

# deep-research

A deliberately minimal (~500 LOC) TypeScript deep-research agent that recursively fans out search queries via Firecrawl, scrapes results, extracts learnings, and synthesizes a cited Markdown report — built to be the simplest readable reference implementation, not a product.

![deep-research — health radar](../../assets/health/deep-research.svg)

## When to use

You're an engineer who wants to *understand* how a deep-research loop actually works — the breadth/depth recursion, query generation, learning extraction, follow-up direction synthesis — and you'd rather read 500 lines of TypeScript than reverse-engineer a 50k-line framework. You point it at a topic, answer a couple of CLI prompts (`breadth` 3–10, `depth` 1–5), and it generates SERP queries through Firecrawl, scrapes the pages, distills learnings, and either recurses deeper or writes a `report.md` with sources. Because the whole thing fits in your head, it's an ideal starting point to fork: swap the model, change the prompt, bolt on your own scraper.

You're also a good fit if you already have a Firecrawl key and an OpenAI-compatible endpoint and just want a scriptable agent that turns a question into a sourced report from the command line or a thin Express API — without standing up a database, a vector store, or a UI. The default path uses OpenAI's `o3-mini` reasoning model and auto-switches to DeepSeek R1 if you supply a Fireworks key, and it accepts any OpenAI-compatible base URL (OpenRouter, Gemini-compatible gateways, etc.), so you can keep your own model/provider choice.

## When NOT to use

- **You want a turnkey product or UI.** This is a CLI/script and a minimal Express endpoint, not an app with auth, history, or a frontend. If you want a hosted answer engine, look at [Vane](vane.md) or a SaaS.
- **You need fully local / private / offline research.** It hard-depends on the Firecrawl API for search+scrape and a cloud LLM by default. For air-gapped, encrypted, local-LLM research over private docs, use [local-deep-research](local-deep-research.md).
- **You want to read social platforms (Twitter/Reddit/YouTube/GitHub) without API fees.** That's a different access problem; see [Agent-Reach](agent-reach.md).
- **You need production hardening.** No release tags, version still `0.0.1`, ~500 LOC by design — minimal error handling, no rate-limit/retry/cost-control story, no test coverage to speak of. Treat it as a reference/fork base, not a maintained dependency.
- **You want to avoid per-call cloud cost.** Firecrawl credits + a reasoning model per recursion level can get expensive fast at high breadth/depth; there's no built-in budget cap. [推断]
- **Abandonment/maintenance risk matters.** It's a single-author demo repo; activity is bursty and there is no release/changelog cadence. Don't build a business-critical pipeline directly on top.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Vane](vane.md) | ✅ | Choose Vane when you need a usable TypeScript answering product/UI. | TypeScript AI answering engine aimed at being a usable product/UI; deep-research is a bare ~500-LOC agent you fork, not run as a service. |
| [local-deep-research](local-deep-research.md) | ✅ | Choose local-deep-research when you need a Python local-first encrypted research assistant. | Python, local-first & encrypted, 10+ search backends incl. local docs, runs fully on local LLMs; deep-research is cloud-LLM + Firecrawl by default and far smaller in scope. |
| [Agent-Reach](agent-reach.md) | ✅ | Choose Agent-Reach when you need social/web platform reading rather than synthesis. | Python CLI focused on *reading* social/web platforms (Twitter/Reddit/YouTube/GitHub) with "zero API fees"; not an iterative-synthesis research agent. |
| [GPT Researcher](gpt-researcher.md) | ✅ | Choose GPT Researcher when you need a larger Python feature surface with reports and UI. | Python, much larger feature surface (multiple retrievers, report types, web UI); deep-research trades all that breadth for a readable minimal core. |
| [Open Deep Research (LangChain / HF)](open-deep-research.md) | ✅ | Choose Open Deep Research when framework-backed reference agents and ecosystem matter more. | Framework-backed reference agents with bigger ecosystems and tooling; heavier to read and adapt than this single-file-ish implementation. |

## Tech stack

- **Language:** TypeScript (~98% of repo); runs on Node.js 22.x via `tsx`.
- **LLM layer:** Vercel AI SDK (`ai`) with `@ai-sdk/openai` and `@ai-sdk/fireworks` providers; default model `o3-mini`, auto-switch to DeepSeek R1 when a Fireworks key is present; OpenAI-compatible base URLs supported.
- **Search/scrape:** Firecrawl (`@mendable/firecrawl-js`), optionally self-hosted via `FIRECRAWL_BASE_URL`.
- **Structure/validation:** `zod` for typed structured output; `js-tiktoken` for token accounting; `p-limit` for bounded concurrency; `lodash-es`, `uuid` utilities.
- **Surface:** interactive CLI (`npm start`) plus a thin `express` + `cors` HTTP API (`npm run api`); output written as `report.md` / `answer.md`.

## Dependencies

- **Runtime:** Node.js 22.x (`engines` pins 22.x); run via `tsx` (no build step) or the provided Docker image / `docker compose`.
- **External services (required):** a Firecrawl API key (`FIRECRAWL_KEY`) for web search + scraping, and an LLM key — `OPENAI_KEY` (OpenAI / compatible) and/or `FIREWORKS_KEY` for DeepSeek R1. Optional `OPENAI_ENDPOINT` / `FIRECRAWL_BASE_URL` for custom/self-hosted endpoints.
- **No datastore/vector DB/queue** — state is in-process; reports land on the local filesystem.
- **Install:** clone, `npm install`, set `.env` keys, `npm start`. Docker path: `docker compose up -d` then `docker exec -it deep-research npm run docker`.

## Ops difficulty

**Low to run, low-to-medium to operate responsibly.** Getting a single research run going is trivial: clone, add two API keys, `npm start`. There's no infra to manage — no DB, no UI, no orchestration. The operational risk is *cost and reliability*, not deployment: high `breadth`×`depth` multiplies Firecrawl scrapes and reasoning-model calls with no built-in budget cap or robust retry/rate-limit handling, so you'll likely add your own guardrails before any unattended/batch use. As a fork base this is fine; as a standalone always-on service it's underbuilt. [推断]

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06):** last pushed 2026-04; no GitHub releases/tags and `package.json` still at `0.0.1`. Activity is **bursty single-author** — coasting-to-active, not a steadily-maintained dependency. [推断]
- **Governance & bus factor:** `User`-owned solo demo repo with ~19k stars — a classic **bus-factor flag**: high visibility, one person, no org or release cadence behind it. [推断]
- **Age & Lindy (~1yr, created 2025-02):** young and popular. The stars buy it attention, not durability — too new to clear a Lindy bar, and by design it's a reference implementation to fork, not bet on long-term. [推断]
- **Risk flags:** no semver/changelog discipline, minimal error handling, no cost-control story; treat as a fork base, not a maintained upstream you can pin and forget. [推断]

## Caveats (unverified)

- [未验证] Star count ~19.2k as of 2026-06 — GitHub stars are unreliable and date-sensitive; treat as indicative only.
- [未验证] "~500 lines of code" and "simplest implementation" are the project's own framing from the README, not independently measured here.
- [未验证] Default model `o3-mini` and the auto-switch-to-DeepSeek-R1 behavior are from the README; exact current defaults may have changed since last push (2026-04).
- [未验证] No GitHub release/tag exists; `package.json` version is `0.0.1` (read from `main`), so there is no stable versioned artifact to pin.
- [推断] Per-run cloud cost can scale steeply with breadth/depth; no first-party cost-control feature is documented, so the "expensive at high settings" warning is inferred from the architecture.
- [推断] Maintenance is bursty single-author; "active" reflects a 2026-04 push, not a guaranteed ongoing cadence.
- [未验证] The internal `package.json` name is `open-deep-research` while the repo/display name is `deep-research`; the repo URL and common reference name are `dzhng/deep-research`.
