# rag-retrieval

> Category node. Document indexing, code-intelligence graphs, and graph DBs for retrieval-augmented generation.
> Split into sub-categories by **what is being retrieved and how**: a codebase indexed for an agent, text found by embedding similarity, or a graph / document structure walked hop by hop.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Code Intelligence** | The corpus is a code repository and an agent must answer structural questions — callers, blast radius, ownership — without grepping the whole tree. | [→](code-intelligence/INDEX.md) |
| **Vector Search** | You need the embedding path of RAG: an encoder that turns text into vectors, or an ANN index / vector database that returns nearest neighbours. | [→](vector-search/INDEX.md) |
| **Structured Retrieval** | Similarity alone is not enough: retrieval should traverse an entity graph (GraphRAG) or navigate a document's own section tree, with citable paths. | [→](structured-retrieval/INDEX.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [Code Intelligence](code-intelligence/INDEX.md) | Sub-category | graphify, code-review-graph, Understand-Anything, Ix, Repowise, SCIP, Sourcegraph — code graphs and code-search indexes that hand an agent a structural slice instead of raw files. |
| [Vector Search](vector-search/INDEX.md) | Sub-category | FAISS, Milvus, text2vec — encoder, in-process ANN library, and vector-database service; fast similarity, no notion of relationships. |
| [Structured Retrieval](structured-retrieval/INDEX.md) | Sub-category | FalkorDB, HelixDB, PageIndex — graph engines that mix traversal with vector/text indexes, and a vectorless document-tree index; more setup or per-query LLM cost than plain vector search. |

## What belongs here

Infrastructure whose primary job is **indexing and retrieving** context for RAG — document indexes, code graphs, graph databases. Not agent memory (see `agent-memory`), not research agents (see `deep-research`). Pick a sub-category by **what you retrieve and how**: a codebase for an agent (`code-intelligence`), embeddings by similarity (`vector-search`), or a graph / document structure by traversal (`structured-retrieval`).
