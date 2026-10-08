# vector-search

> Category node. The embedding-similarity path of RAG: sentence encoders that turn text into vectors, and ANN indexes / vector databases that return nearest neighbours.
> ← back to [rag-retrieval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FAISS** | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. | A (6/6) | [→](faiss.md) |
| **text2vec** | Use it when you need Chinese-first sentence embeddings or CoSENT/SBERT fine-tuning for FAQ matching or semantic search from one pip install — but it is only the encoder (bring FAISS or Milvus), and the single maintainer last released in 2023-09. | C (5/6) | [→](text2vec.md) |
| **Milvus** | Use it when vectors outgrow one machine's RAM and you need filtered nearest-neighbor search, live writes, replicas, and horizontal scale-out as a network service — but you then operate a distributed cluster with etcd and object storage; small corpora fit FAISS or pgvector. | A (6/6) | [→](milvus.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FAISS](faiss.md) | ✅ | A (6/6) | Use it when you need a fast in-process ANN vector index for embeddings — a library, not a managed vector DB. |
| [text2vec](text2vec.md) | ✅ | C (5/6) | Gets curated Chinese embedding checkpoints and training scripts benchmarked on Chinese STS sets; costs a bus factor of one, lag behind newer embedding models, and an extra layer over sentence-transformers. |
| [Milvus](milvus.md) | ✅ | A (6/6) | Compute and storage that scale out separately for filtered vector search, at the cost of cluster operations and a roadmap steered by Zilliz, which also sells the hosted Zilliz Cloud. |
| Weaviate | 未收录 | — | Another vector database named across the pages. |

## What belongs here

Components of **embedding-based retrieval**: encoders that produce vectors, in-process ANN libraries, and vector-database services that store and search them at scale. Not graph or document-structure retrieval (see `structured-retrieval`), not code indexes (see `code-intelligence`).
