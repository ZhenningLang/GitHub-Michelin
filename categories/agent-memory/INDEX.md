# agent-memory

> Category node. Persistent, LLM-agnostic memory an agent reads/writes across sessions.
> Split into sub-categories by **whose memory it is and how you wire it in**: a memory component inside your own product, a layer bolted onto the coding-agent harnesses you already run, or a graph-shaped engine you stand up.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **App Memory** | You are building the agent/product yourself and want memory as a component — an API, SDK, client wrapper, or a platform that owns the agent loop. | [→](app-memory/INDEX.md) |
| **Coding-Agent Memory** | The agents are coding harnesses you already run (Claude Code, Codex, Cursor, …) and memory should hook their sessions — locally or behind a shared server. | [→](coding-agent-memory/INDEX.md) |
| **Graph Memory** | The memory store should be a knowledge graph — temporal fact graphs, document-derived graph pipelines — run as a service or library. | [→](graph-memory/INDEX.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [App Memory](app-memory/INDEX.md) | Sub-category | Mem0, Memori, Letta, LangMem, SimpleMem — memory keyed on application data (users, entities, dialogues), embedded at build time. |
| [Coding-Agent Memory](coding-agent-memory/INDEX.md) | Sub-category | claude-mem, Claude Subconscious, ByteRover, OpenViking, Beacon — hook/plugin/MCP capture of coding sessions on your machine or a team server. |
| [Graph Memory](graph-memory/INDEX.md) | Sub-category | Zep, Graphiti, Cognee — knowledge-graph engines with temporal invalidation or document-to-graph pipelines; heavier than file or vector stores. |

## What belongs here

Infrastructure whose primary job is to **store and recall** agent memory across sessions, independent of the model. Not task/issue tracking (see `agent-tooling`), not RAG document retrieval (see `rag-retrieval`). Pick a sub-category by **whose memory and how it wires in**: a component in your own product (`app-memory`), a layer on the coding agents you run (`coding-agent-memory`), or a graph-shaped engine (`graph-memory`).
