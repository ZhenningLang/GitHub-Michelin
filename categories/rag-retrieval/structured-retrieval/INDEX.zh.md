# structured-retrieval

> 分类节点。沿结构检索、而不只看向量相近：做 GraphRAG 遍历的图数据库，以及由 LLM 按章节逐层导航的文档树索引。
> ← 返回[rag-retrieval](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **FalkorDB** | 当 GraphRAG 需要在一个低延迟、嵌入 Redis 的引擎里把向量相似与多跳图遍历结合时使用。 | D（5/6） | [→](falkordb.zh.md) |
| **PageIndex** | 当向量 RAG 在少量长而有结构的文档上召回相似但不相关的块、且你需要可溯源引用时使用。 | B（6/6） | [→](pageindex.zh.md) |
| **HelixDB** | 当你的 RAG 语料本身就是一张图，你想把向量检索、BM25 和图遍历放进同一个采用 Apache-2.0、由对象存储托底的引擎时用它——但 v3 引擎 2026-07 才开源，且没有可自建的 HA。 | B（6/6） | [→](helix-db.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [FalkorDB](falkordb.zh.md) | ✅ | D（5/6） | 当 GraphRAG 需要在一个低延迟、嵌入 Redis 的引擎里把向量相似与多跳图遍历结合时使用。 |
| [PageIndex](pageindex.zh.md) | ✅ | B（6/6） | 当向量 RAG 在少量长而有结构的文档上召回相似但不相关的块、且你需要可溯源引用时使用。 |
| [HelixDB](helix-db.zh.md) | ✅ | B（6/6） | 当你的 RAG 语料本身就是一张图，你想把向量检索、BM25 和图遍历放进同一个采用 Apache-2.0、由对象存储托底的引擎时用它——但 v3 引擎 2026-07 才开源，且没有可自建的 HA。 |
| Neo4j / LightRAG | 未收录 | — | 各页对比里点到的其他图／GraphRAG 检索方案。 |

## 什么该放这里

检索时**沿结构走**的引擎与索引——实体／关系图（常在同一引擎里叠加向量与全文索引），或文档自身的章节层级——让答案能引出一条路径或一页出处。不含单纯的 embedding 检索（见 `vector-search`），不含代码图（见 `code-intelligence`），不含 agent 记忆存储（见 `agent-memory`）。
