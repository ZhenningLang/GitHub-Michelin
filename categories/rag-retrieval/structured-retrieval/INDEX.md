# structured-retrieval

> Category node. Retrieval that follows structure rather than only vector nearness: graph databases for GraphRAG traversal, and document-tree indexes an LLM navigates section by section.
> ← back to [rag-retrieval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FalkorDB** | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. | D (5/6) | [→](falkordb.md) |
| **PageIndex** | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. | B (6/6) | [→](pageindex.md) |
| **HelixDB** | Use it when your RAG corpus is a genuine graph and you want vector search, BM25 and traversal in one Apache-2.0 engine backed by object storage — but its v3 engine was open-sourced in 2026-07 and self-hosted HA does not exist yet. | B (6/6) | [→](helix-db.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FalkorDB](falkordb.md) | ✅ | D (5/6) | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. |
| [PageIndex](pageindex.md) | ✅ | B (6/6) | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. |
| [HelixDB](helix-db.md) | ✅ | B (6/6) | Use it when your RAG corpus is a genuine graph and you want vector search, BM25 and traversal in one Apache-2.0 engine backed by object storage — but its v3 engine was open-sourced in 2026-07 and self-hosted HA does not exist yet. |
| Neo4j / LightRAG | 未收录 | — | Other graph / GraphRAG retrieval stacks named across the pages. |

## What belongs here

Engines and indexes whose retrieval **walks a structure** — entity/relationship graphs (often combined with vector and full-text indexes in one engine) or a document's own section hierarchy — so answers can cite a path or a page. Not plain embedding search (see `vector-search`), not code graphs (see `code-intelligence`), not agent memory stores (see `agent-memory`).
