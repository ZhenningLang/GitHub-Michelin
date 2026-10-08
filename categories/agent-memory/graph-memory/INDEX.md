# graph-memory

> Category node. Memory engines whose store is a knowledge graph — temporal fact graphs with explicit invalidation, and document-derived graph pipelines — that you run as a service or library, rather than a vector store or file tree.
> ← back to [agent-memory](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Zep** | Use it when you want temporal user memory as a hosted service with ready adapters for LangGraph, CrewAI, ADK or Pydantic AI — but this repo holds only examples and clients; the engine is closed, paid Zep Cloud, and the self-hosted Community Edition is deprecated. | A (4/6) | [→](zep.md) |
| **Graphiti** | Use it when users change preferences, jobs or addresses over time and the agent must know which fact is still true and when it held — but it needs Neo4j, FalkorDB or Neptune from day one, and every message costs several LLM calls to ingest. | B (6/6) | [→](graphiti.md) |
| **Cognee** | Use it when agent memory spans connected material (docs, tickets, meeting notes, code) and plain RAG keeps failing multi-hop questions — but every ingest costs LLM graph extraction, and Postgres-as-graph-store is a demo, not a production path. | A (5/6) | [→](cognee.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Zep](zep.md) | ✅ | A (4/6) | Buys temporal-graph memory with no graph database or user and thread plumbing to run; costs dependence on a closed SaaS's pricing and terms, with GitHub issues disabled on the repo. |
| [Graphiti](graphiti.md) | ✅ | B (6/6) | Buys a temporal graph where new facts invalidate old ones, with provenance back to source messages; costs running a graph database, slow per-message ingest, and a pre-1.0 library steered by one vendor. |
| [Cognee](cognee.md) | ✅ | A (5/6) | Buys a knowledge graph plus embeddings behind four calls, on a three-year-old, very active project; costs a heavy dependency tree, extraction cost per document, and a young 1.x API. |

## What belongs here

Memory engines whose storage model is a **knowledge graph**: temporal fact graphs with bi-temporal edges and explicit invalidation (Zep, and the Graphiti library it is built on), and document-to-graph ingestion pipelines (Cognee). You run them as a service or embed them as a library — the graph shape is the deciding trait. Not hook layers for coding agents (see `coding-agent-memory`), not vector-store or compression memory APIs (see `app-memory`).
