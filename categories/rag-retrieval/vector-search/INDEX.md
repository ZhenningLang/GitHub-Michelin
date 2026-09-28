# vector-search

> Category node. The embedding-similarity path of RAG: sentence encoders that turn text into vectors, and ANN indexes / vector databases that return nearest neighbours.
> ← back to [rag-retrieval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FAISS** | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. | A (6/6) | [→](faiss.md) |
| **text2vec** | Use it when you need Chinese-first sentence embeddings for semantic search or FAQ matching from a single pip install — it's only the encoder, so bring your own vector index (FAISS/Milvus). | C (5/6) | [→](text2vec.md) |
| **Milvus** | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search | A (5/6) | [→](milvus.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FAISS](faiss.md) | ✅ | A (6/6) | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. |
| [text2vec](text2vec.md) | ✅ | C (5/6) | Use it when you need Chinese-first sentence embeddings for semantic search or FAQ matching from a single pip install — it's only the encoder, so bring your own vector index (FAISS/Milvus). |
| [Milvus](milvus.md) | ✅ | A (5/6) | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search |
| Weaviate | 未收录 | — | Another vector database named across the pages. |

## What belongs here

Components of **embedding-based retrieval**: encoders that produce vectors, in-process ANN libraries, and vector-database services that store and search them at scale. Not graph or document-structure retrieval (see `structured-retrieval`), not code indexes (see `code-intelligence`).
