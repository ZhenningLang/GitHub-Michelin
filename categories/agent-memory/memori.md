---
name: Memori
slug: memori
repo: https://github.com/MemoriLabs/Memori
category: agent-memory
tags: [agent-memory, persistent-memory, llm-agnostic, mcp, state-management, entity-extraction]
language: Python
license: Apache-2.0
maturity: v3.3.6, active (2026-06)
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-15T23:18:56Z
  default_branch: main
  default_branch_sha: 56600c525ba3046354c17a7663dca06a813a0bb5
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T10:42:45Z
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
        last_commit_age_days: 17
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 14.8
        qualifying_issues: 14
        band: default
        window_offset_days: 7
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: memori
        dependent_repos_count: 1
        downloads_last_month: 33978
        graph_tier: D
        volume_tier: C
        cross_check_divergence: null
    longevity:
      grade: D
      raw:
        repo_age_days: 344
        last_commit_age_days: 17
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 45
        top1_share: 0.223
        top3_share: 0.588
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Memori

An LLM-agnostic memory layer that turns agent execution and conversation into structured, persistent state — captured by wrapping your existing LLM client, recalled automatically, no `search()` calls in your hot path.

![memori — health radar](../../assets/health/memori.svg)

## When to use

You're building a production support agent on top of OpenAI or Anthropic, and you keep re-solving the same problem: the model forgets everything between sessions, so each conversation starts cold. You don't want to hand-roll a vector store, write retrieval glue, or design a memory schema — you want the agent to *remember the user* (their entities, preferences, past decisions) the way a human teammate would. Memori sits between your code and the LLM: you register your existing client (`Memori().llm.register(client)`), tag a call with an `entity_id` and `process_id`, and conversations are persisted and recalled automatically in the background — so the next session, the relevant facts, people, preferences, and rules are already in context without you writing a retrieval pipeline.

It's a fit when you want memory that's keyed on *what agents do*, not just chat transcripts — the augmentation layer extracts attributes, events, facts, people, preferences, relationships, rules, and skills at entity / process / session levels in the background, claiming "no latency" on the hot path. Because it's pitched as LLM-, datastore-, and framework-agnostic (Anthropic, OpenAI, Bedrock, DeepSeek, Gemini, Grok; Agno, LangChain, Pydantic AI), and ships an MCP server, you can also wire it into Claude Code, Cursor, Codex, or Warp with no SDK code at all.

## When NOT to use

- **You need a fully air-gapped, self-contained library.** The default SDK path calls **Memori Cloud** and requires a `MEMORI_API_KEY` (sign-up at app.memorilabs.ai). Self-hosting exists via **BYODB** (Bring Your Own Database), but the only datastore the docs name explicitly is **TiDB** — Postgres/SQLite support is not documented in the README. [未验证] If you require local-only, this is a real constraint to verify before adopting.
- **You're avoiding vendor lock-in / SaaS dependency.** "Advanced Augmentation" (the entity/fact/relationship extraction that is the product's main draw) is described as available without an account but **rate-limited**, with the full capability behind paid cloud accounts. The open-source code and the commercial cloud are intertwined; the most valuable behavior may degrade off-cloud.
- **You want a battle-tested, stable API.** It's young (v3.3.6, releases moving fast in 2026); the API surface and the cloud/BYODB split are still shifting. Pin versions and expect churn.
- **You only need a thin vector-recall RAG.** If all you want is "embed chunks, top-k retrieve," a plain vector DB or [Mem0](mem0.md) is lighter than Memori's structured-state + augmentation model.
- **You need transparent, auditable retrieval.** Memory is injected by automatic background interception of the wrapped client — there are no explicit `search()` calls in the quickstart. If you need to see and control exactly what gets pulled into each prompt, the implicit model fights you.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Mem0](mem0.md) | ✅ | Choose Mem0 when explicit add/search APIs and broad self-hosting matter more. | The most-cited agent-memory layer; add/search API over a vector store, broad self-host story. Memori leans on automatic client interception + structured entity/process state and an opinionated cloud, vs Mem0's more explicit, datastore-flexible retrieval. |
| [claude-subconscious](claude-subconscious.md) | ✅ | Choose claude-subconscious when you specifically want a Claude/Letta background-memory experiment. | A Claude-specific background-memory experiment (Letta lineage); narrower scope than Memori's multi-provider, multi-framework infrastructure. |
| [Letta (MemGPT)](letta.md) | ✅ | Choose Letta when you need a memory-management OS inside a stateful agent runtime. | Agent runtime with a memory-management OS (tiered context, self-editing memory); a heavier stateful-agent server, not a drop-in client wrapper. |
| [Zep](zep.md) | ✅ | Choose Zep when temporal knowledge-graph memory is the main architecture bet. | Temporal knowledge-graph memory service with a strong self-host/OSS core; comparable structured-memory ambition, different graph-first model. |
| [LangMem (LangChain)](langmem.md) | ✅ | Choose LangMem when your memory utilities should stay tied to LangGraph/LangChain. | Memory utilities tied to the LangGraph/LangChain stack; less standalone than Memori's framework-agnostic pitch. |
| plain vector DB (pgvector / Chroma) | 未收录 | Choose a plain vector DB when owning schema and retrieval outweighs augmentation features. | You own the schema and retrieval; no augmentation, no entity model, no cloud — maximum control, maximum wiring. |

## Tech stack

- **Language:** Python (~63%) with a TypeScript SDK (~18%); `pip install memori` / `npm install @memorilabs/memori`.
- **Memory model:** multi-level tracking at **entity / process / session** levels; background "Advanced Augmentation" extracting attributes, events, facts, people, preferences, relationships, rules, skills.
- **Integration:** wraps existing LLM clients (OpenAI Chat Completions & Responses API, Anthropic, Bedrock, DeepSeek, Gemini, Grok); framework adapters for Agno, LangChain, Pydantic AI; ships an **MCP server** for Claude Code / Cursor / Codex / Warp / Antigravity with no SDK integration.
- **Datastore:** Memori Cloud (managed, default) or **BYODB** self-host — TiDB named explicitly (TiDB Zero provisioning for disposable dev DBs). [未验证] Other backends not documented in the README.

## Dependencies

- **Runtime:** Python (SDK) and/or Node (TS SDK). A `MEMORI_API_KEY` for the default cloud path.
- **External services:** Memori Cloud by default (account at app.memorilabs.ai). For self-host: a BYODB database (TiDB per docs).
- **LLM provider:** at least one supported provider client (OpenAI, Anthropic, etc.) — Memori is a layer over your existing LLM calls, not an LLM itself.
- **Optional:** MCP-capable client (Claude Code, Cursor, Codex, Warp) to use the no-SDK MCP path.

## Ops difficulty

**Low for the cloud path, medium-to-high for self-host.** The managed-cloud quickstart is "zero config": set an API key, register your client, done — minimal ops. The moment you want to avoid the SaaS dependency, you cross into BYODB territory, where you provision and operate your own database (TiDB per the docs) and absorb whatever augmentation features are cloud-gated or rate-limited off-account. Because the open-source code and the commercial cloud are coupled, the real ops question isn't "can I run the container" but "which capabilities survive when I leave the cloud" — budget time to validate that for your use case before committing.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 14.8 hours across 14 qualifying issues/PRs.
- **Maintenance (2026-06):** active and fast-moving — latest release v3.3.6 (2026-05), last pushed 2026-06, not archived, low open-issue count (~20). Releases are coming quickly, which signals energy but also an unstable surface.
- **Governance / bus factor:** owned by the `MemoriLabs` org (the company behind the commercial Memori Cloud). This is single-vendor, open-core governance — the roadmap follows the SaaS, not a foundation or community. `[推断]`
- **Age & Lindy verdict:** ~1 year old (created 2025-07) — young and unproven on the Lindy axis. There's no long track record to lean on; treat longevity as an open question and pin versions.
- **Risk flags:** open-core / SaaS coupling is the headline risk — the most valuable behavior ("Advanced Augmentation") is rate-limited off-account and the only documented self-host backend is TiDB, so leaving the cloud may degrade capability. Validate the BYODB path before betting on local-only.

## Caveats (unverified)

- [未验证] License is Apache-2.0 per the repo's `LICENSE` file (standard text, no Commons Clause); note `gh repo view` reports `license: other`, likely a detection artifact of the appendix copyright line — verify against the live `LICENSE` if license matters.
- [未验证] Latest release v3.3.6 published 2026-05-28; pushed 2026-06-15; stargazer count ~15.4k as of 2026-06 — GitHub stars are unreliable and date-sensitive; treat as indicative only.
- [未验证] BYODB self-host: only TiDB is named in the README; Postgres/SQLite or other backends are not confirmed and may not be supported.
- [推断] "Advanced Augmentation" (entity/fact/relationship extraction) appears to run in Memori Cloud and is rate-limited without a paid account; the degree to which it works fully self-hosted is not confirmed from the README.
- [推断] The default SDK path calls Memori Cloud and requires `MEMORI_API_KEY`; a fully local-only deployment may require non-default configuration not detailed in the quickstart.
- [推断] "No latency" for background augmentation is the project's own framing; real-world impact depends on workload and was not independently measured.
