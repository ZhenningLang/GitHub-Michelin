---
name: Mem0
slug: mem0
repo: https://github.com/mem0ai/mem0
category: agent-memory
tags: [agent-memory, long-term-memory, llm-agnostic, vector-store, rag, personalization]
language: Python
license: Apache-2.0
maturity: Python mem0ai v2.0.8, Node ts-v3.0.10; active (2026-06)
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-29T10:19:26Z
  default_branch: main
  default_branch_sha: 31cec11a790868f88c9acafb8b70eb25071f2150
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:40:04Z
  overall: A
  overall_score: 3.67
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 12.8
        qualifying_issues: 37
        band: default
        window_offset_days: 3
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: mem0ai
        dependent_repos_count: 0
        downloads_last_month: 2100304
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.02
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1190
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 55
        top1_share: 0.404
        top3_share: 0.558
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

# Mem0

An LLM-agnostic memory layer that runs an LLM extraction pass over conversations, stores the distilled facts in a vector store, and retrieves them on later turns so your agent remembers users across sessions.

![mem0 — health radar](../../assets/health/mem0.svg)

## When to use

You're building a chatbot, support agent, or personal assistant on top of an LLM, and you've hit the obvious wall: every new session starts from zero. Stuffing the whole prior conversation back into the prompt blows your context window and your token bill, and a raw RAG-over-transcripts setup retrieves noisy chunks instead of the few durable facts ("user is vegetarian", "prefers terse answers", "works in EU timezone") that actually personalize the next reply. You want a drop-in layer that watches the conversation, extracts the salient facts, and hands back only the relevant ones at retrieval time — without you hand-rolling the extraction prompts, the embedding pipeline, and the store.

Mem0 is built for exactly this. You call `m.add(messages, user_id=...)` after a turn and it runs an LLM pass to pull out memory-worthy facts, embeds them, and writes them to a vector store; you call `m.search(query, user_id=...)` before the next turn and get back the top relevant memories to inject into the prompt. It's LLM- and store-agnostic (OpenAI is the default LLM/embedder, but litellm, Groq, Gemini, Ollama and others are wired in; Qdrant is the default vector backend), ships Python (`pip install mem0ai`) and Node (`npm install mem0ai`) SDKs, and runs fully self-hosted from the OSS package — so you can prototype against the library and keep the data on your own infra.

## When NOT to use

- **You need memories to be corrected or forgotten in-place.** The current extraction algorithm is documented as **single-pass ADD-only — one LLM call, no UPDATE/DELETE; memories accumulate and nothing is overwritten** `[未验证]` (per README, April 2026). If a user says "actually I moved to Berlin", the old fact isn't superseded automatically — stale and contradictory memories pile up and you must prune them yourself. For mutable, authoritative user state, a plain database row is more honest than a memory layer.
- **You want a zero-LLM, deterministic store.** Every `add` costs an extra LLM call (latency + tokens on top of your main generation). If your "memory" is structured profile data or you can't afford the per-write inference, a key-value store or [Memori](memori.md)'s SQL-first approach fits better.
- **You're avoiding a hosted-platform upsell.** The OSS library is real and Apache-2.0, but the project also sells a managed **Mem0 Platform** (paid SaaS) with features beyond the library; the README's three-tier framing (Library → Self-Hosted → Cloud) means some capabilities are positioned as platform-only. Read which features you actually need before assuming OSS parity.
- **You need a mature, frozen API.** Memory extraction logic has changed materially across releases (the ADD-only algorithm replaced an earlier UPDATE/DELETE one), and Python vs Node SDKs version independently. If you need long-term API stability, pin hard and expect churn.
- **Graph relationships are central to your use case.** Whether a graph-memory backend (e.g. Neo4j) is available in the current OSS package is unclear `[未验证]`; don't pick Mem0 *for* graph memory without verifying the current release supports it.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Memori](memori.md) | ✅ | Choose Memori when database-native auditability matters more than drop-in vector memory. | SQL-first / database-native memory (queryable, auditable, no vector store required); Mem0 leans vector + LLM extraction and is more "drop-in" but less inspectable. |
| [claude-subconscious](claude-subconscious.md) | ✅ | Choose claude-subconscious when you want a Claude-specific hook memory experiment. | A Claude-specific subconscious/reflection memory experiment; Mem0 is general-purpose and LLM-agnostic across many providers. |
| [Zep](zep.md) / [Graphiti](graphiti.md) | ✅ | Choose Zep or Graphiti when temporal graph memory and explicit invalidation are central. | Temporal knowledge-graph memory with bi-temporal edges and explicit invalidation; stronger at evolving/contradicting facts where Mem0's ADD-only model accumulates. |
| [Letta (MemGPT)](letta.md) | ✅ | Choose Letta when you need a stateful agent runtime, not just a memory library. | Agent runtime with self-editing memory + a stateful server, not just a library; heavier, owns the agent loop rather than slotting under yours. |
| [LangMem (LangChain)](langmem.md) | ✅ | Choose LangMem when your memory layer should stay inside LangChain/LangGraph. | Memory utilities tied to the LangChain/LangGraph ecosystem; Mem0 is framework-neutral. |
| Plain pgvector + your own extraction | 未收录 | Choose plain pgvector when full schema and retrieval control outweigh Mem0's packaged layer. | Full control, no extra dependency or platform; you build and maintain the extraction prompts, schema, and retrieval that Mem0 gives you out of the box. |

## Tech stack

- **Language:** Python (primary); first-party TypeScript/Node SDK.
- **Core (Python `mem0ai` v2.0.8):** `pydantic` for models, `httpx`/`openai` for LLM calls, `qdrant-client` as default vector store, `sqlalchemy` for relational history, `posthog` for telemetry.
- **LLM/embedding layer:** OpenAI by default (default LLM `gpt-5-mini`, default embedder `text-embedding-3-small`, per README); pluggable via `litellm`, plus `groq`, `google-genai`/`google-generativeai`, `ollama` through the `llms` extra.
- **Retrieval:** README describes multi-signal retrieval — semantic (vector) search, BM25 keyword matching, and entity linking, with temporal reasoning.
- **Deployment shapes:** in-process library, self-hosted Docker Compose server (with auth/API-key management), and the hosted Mem0 Platform (paid).

## Dependencies

- **Runtime:** Python `>=3.10,<4.0` (per PyPI metadata for v2.0.8); Node for the JS SDK.
- **Required Python deps:** `httpx>=0.28`, `openai>=1.90`, `pydantic>=2.7`, `qdrant-client>=1.12`, `sqlalchemy>=2.0`, `posthog`, `pytz`, `protobuf`.
- **An LLM + embedder:** you must supply credentials/endpoints — an OpenAI key for the defaults, or a self-hosted model via Ollama/litellm. Every `add` makes an LLM call, so a reachable model is a hard dependency, not optional.
- **A vector store:** Qdrant by default; other stores (Elasticsearch, OpenSearch, pgvector, etc.) via the `extras` group.
- **Install:** `pip install mem0ai` or `npm install mem0ai`. Self-hosted server adds a Docker Compose stack.

## Ops difficulty

**Low-to-medium.** As an in-process library pointed at a managed LLM and a single Qdrant instance, it's a few lines and minimal ops — close to "just a dependency". It rises to **medium** when you self-host the server stack (Docker Compose, auth, a vector DB you now operate and back up) and when you account for the LLM call on every write: that's added latency, a per-write token cost, and a new failure mode (LLM/embedder downtime stalls memory writes). Because extraction is ADD-only (see When NOT to use), you also inherit an ongoing *data-hygiene* burden — pruning stale/contradictory memories — that pure storage layers don't impose. The hosted Platform trades this ops for a bill and vendor dependency.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 20.6 hours across 31 qualifying issues/PRs.
- **Maintenance (2026-06):** actively maintained — last pushed 2026-06, not archived, two SDKs (Python `v2.0.8`, Node `ts-v3.0.10`) shipping on independent release trains. ~440 open issues is high in absolute terms but typical of a hot project at this star level, not a stall signal on its own.
- **Governance / bus factor:** owned by the `mem0ai` org (a commercial company), not a foundation. Roadmap is vendor-controlled and steered by the paid **Mem0 Platform** business — a single-vendor open-core structure, not community governance. `[推断]`
- **Age & Lindy verdict:** ~3 years old (created 2023-06) and still active — long enough to have shed at least one major extraction-algorithm rewrite (UPDATE/DELETE → ADD-only), so it clears the basic Lindy bar (old + active), but the churn means *API* longevity is weaker than the project's.
- **Adoption:** the most-cited open-source agent-memory layer; large star base and broad LLM/vector-store integration surface signal real adoption, though stars are a weak proxy.
- **Risk flags:** open-core — an Apache-2.0 library with a paid managed Platform on top; expect some capabilities to be platform-gated and the OSS roadmap to serve the commercial product. ADD-only accumulation is a *data-hygiene* liability, not a licensing one.

## Caveats (unverified)

- `[未验证]` "Single-pass ADD-only extraction — one LLM call, no UPDATE/DELETE; memories accumulate, nothing is overwritten" is taken from the README (dated April 2026 in-doc); confirm against the exact release you install, as extraction logic has changed before.
- `[未验证]` Default models (`gpt-5-mini` LLM, `text-embedding-3-small` embedder) and the multi-signal retrieval description (semantic + BM25 + entity linking + temporal reasoning) are the README's own framing, not independently verified.
- `[未验证]` Benchmark figures the project cites (LoCoMo 91.6, LongMemEval 94.8, BEAM, p50 latency ~0.88–1.09s, ~6.7–7.0K tokens) are first-party, self-reported, and benchmark-specific — not independent results.
- `[未验证]` Availability of a graph-memory backend (e.g. Neo4j) in the current OSS package could not be confirmed from the README fetched; historically Mem0 has offered graph memory, but verify for your release.
- `[未验证]` Star count ~59.5k as of 2026-06 — GitHub stars are unreliable and time-sensitive; indicative only.
- `[推断]` Feature parity between the Apache-2.0 OSS package and the paid Mem0 Platform is partial by design; specific platform-only capabilities should be checked against current pricing/docs before assuming OSS covers them.
- `[推断]` Python (`v2.0.8`) and Node (`ts-v3.0.10`) SDKs version independently; behavior and feature coverage may differ between them at any given time.
