# graph-memory

> Category node. Memory engines whose store is a knowledge graph — temporal fact graphs with explicit invalidation, and document-derived graph pipelines — that you run as a service or library, rather than a vector store or file tree.
> ← back to [agent-memory](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Zep** | Zep \| Examples, Integrations, & More | A (4/6) | [→](zep.md) |
| **Graphiti** | Build Real-Time Knowledge Graphs for AI Agents | B (6/6) | [→](graphiti.md) |
| **Cognee** | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | A (6/6) | [→](cognee.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Zep](zep.md) | ✅ | A (4/6) | Temporal knowledge-graph memory for facts about users that expire or get superseded; a backend for app memory rather than a coding-agent hook layer. |
| [Graphiti](graphiti.md) | ✅ | B (6/6) | Real-time knowledge-graph library for AI agents; you build the graph pipeline, it maintains the edges. |
| [Cognee](cognee.md) | ✅ | A (6/6) | Self-hosted knowledge-graph memory engine for document-shaped agent memory; heavier to run than a file or SQLite store. |

## What belongs here

Memory engines whose storage model is a **knowledge graph**: temporal fact graphs with bi-temporal edges and explicit invalidation (Zep, and the Graphiti library it is built on), and document-to-graph ingestion pipelines (Cognee). You run them as a service or embed them as a library — the graph shape is the deciding trait. Not hook layers for coding agents (see `coding-agent-memory`), not vector-store or compression memory APIs (see `app-memory`).
