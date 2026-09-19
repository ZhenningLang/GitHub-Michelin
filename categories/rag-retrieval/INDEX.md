# rag-retrieval

> Category node. Document indexing, code-intelligence graphs, and graph DBs for retrieval-augmented generation.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FalkorDB** | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. | A (4/6) | [→](falkordb.md) |
| **graphify** | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. | B (6/6) | [→](graphify.md) |
| **code-review-graph** | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. | B (6/6) | [→](code-review-graph.md) |
| **PageIndex** | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. | B (5/6) | [→](pageindex.md) |
| **Understand-Anything** | Use it when you want any codebase turned into an explorable, queryable knowledge graph for an agent — younger and less proven than graphify. | B (6/6) | [→](understand-anything.md) |
| **FAISS** | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. | A (6/6) | [→](faiss.md) |
| **text2vec** | Use it when you need Chinese-first sentence embeddings for semantic search or FAQ matching from a single pip install — it's only the encoder, so bring your own vector index (FAISS/Milvus). | C (5/6) | [→](text2vec.md) |
| **SCIP** | SCIP Code Intelligence Protocol | A (6/6) | [→](scip.md) |
| **Milvus** | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search | A (4/6) | [→](milvus.md) |
| **Sourcegraph** | Code AI platform with Code Search & Cody | E (3/6) | [→](sourcegraph.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FalkorDB](falkordb.md) | ✅ | A (4/6) | Use it when GraphRAG needs vector similarity plus multi-hop graph traversal in one low-latency Redis-embedded engine. |
| [graphify](graphify.md) | ✅ | B (6/6) | Use it when an agent needs to query a whole repo's code, schemas and docs as a knowledge graph instead of grepping. |
| [code-review-graph](code-review-graph.md) | ✅ | B (6/6) | Use it when an AI reviewer keeps burning context on a large repo and you want only the blast-radius files. |
| [PageIndex](pageindex.md) | ✅ | B (5/6) | Use it when vector RAG returns similar-but-irrelevant chunks over a few long, structured documents needing auditable citations. |
| [Understand-Anything](understand-anything.md) | ✅ | B (6/6) | Code → explorable knowledge graph an agent can query; younger than graphify, with an unverified star count and egress boundary. |
| [FAISS](faiss.md) | ✅ | A (6/6) | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. |
| [text2vec](text2vec.md) | ✅ | C (5/6) | Use it when you need Chinese-first sentence embeddings for semantic search or FAQ matching from a single pip install — it's only the encoder, so bring your own vector index (FAISS/Milvus). |
| Neo4j / LlamaIndex / LightRAG / Weaviate | 未收录 | — | Other graph/RAG retrieval stacks named across the pages. |

## What belongs here

Infrastructure whose primary job is **indexing and retrieving** context for RAG — document indexes, code graphs, graph databases. Not agent memory (see `agent-memory`), not research agents (see `deep-research`).
