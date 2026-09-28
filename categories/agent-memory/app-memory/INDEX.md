# app-memory

> Category node. Memory you embed in **your own** agent or product — memory libraries, SDKs, client wrappers, and stateful-agent platforms that own the agent loop — keyed on application data (users, entities, dialogues), not on a coding-agent session.
> ← back to [agent-memory](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Mem0** | Use it when your LLM agent must remember users across sessions without bloating the prompt context. | A (6/6) | [→](mem0.md) |
| **Memori** | Use it when you want LLM-agnostic persistent agent memory captured by wrapping your existing client. | B (5/6) | [→](memori.md) |
| **Letta (MemGPT)** | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. | B (6/6) | [→](letta.md) |
| **LangMem** | Use it when you need LangMem for the agent-memory category. | B (5/6) | [→](langmem.md) |
| **SimpleMem** | Use it when your LLM agent must recall long-horizon dialogues without replaying raw history — write-time compression with published LoCoMo numbers, but a young academic repo, a stale PyPI package, and audio/video support that is not benchmark-validated. | B (5/6) | [→](simplemem.md) |
| **Supermemory** | Use it when you want the whole context stack — fact extraction, contradiction supersession, auto-expiry, per-user profiles, hybrid RAG+memory — behind one API or one self-hosted binary, accepting that the engine itself ships binary-only and the license has flip-flopped once. | A (6/6) | [→](supermemory.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Mem0](mem0.md) | ✅ | A (6/6) | Use it when your LLM agent must remember users across sessions without bloating the prompt context. |
| [Memori](memori.md) | ✅ | B (5/6) | SQL-first client-wrapper memory for application code; an opinionated cloud vs the BYODB split. |
| [Letta (MemGPT)](letta.md) | ✅ | B (6/6) | Stateful-agent platform whose memory OS the runtime owns; pick it when Letta should own the agent loop, not when you only want context under an existing harness. |
| [LangMem](langmem.md) | ✅ | B (5/6) | Memory utilities tied to the LangChain/LangGraph ecosystem; stays inside that stack. |
| [SimpleMem](simplemem.md) | ✅ | B (5/6) | Write-time compression memory library with published LoCoMo evidence; PyPI frozen at 0.1.0 (source-only install), open storage bugs, audio/video support unbenchmarked. |
| [Supermemory](supermemory.md) | ✅ | A (6/6) | API-first memory + profiles + hybrid RAG as a hosted service or a single self-hosted binary; the engine source is not public, benchmarks are vendor-run, server channel is v0.0.x, and the license went MIT → CC BY-NC-SA → MIT. |

## What belongs here

Memory as a **component you build into your own agent or product**: drop-in memory APIs and libraries (Mem0, Memori, SimpleMem), ecosystem-bound memory SDKs (LangMem), and stateful-agent platforms whose runtime owns the memory (Letta). The memory's subject is application data — users, entities, long-horizon dialogues. Not memory for coding-agent harnesses you merely run (see `coding-agent-memory`), not graph-shaped engines you stand up as infrastructure (see `graph-memory`).
