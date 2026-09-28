# rag-retrieval

> 分类节点。面向 RAG 的文档索引、代码智能图与图数据库。
> 按**检索什么、怎么检索**拆分子类：给 agent 索引的代码库、按 embedding 相似度找的文本，或逐跳遍历的图／文档结构。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **代码智能** | 语料是一个代码仓库，agent 要回答结构性问题——谁调用它、影响面、归属——而不想把整棵树 grep 一遍。 | [→](code-intelligence/INDEX.zh.md) |
| **向量检索** | 你要的是 RAG 的 embedding 这条路：把文本编码成向量的编码器，或返回最近邻的 ANN 索引／向量数据库。 | [→](vector-search/INDEX.zh.md) |
| **结构化检索** | 光靠相似度不够：检索要遍历实体图（GraphRAG），或沿文档自身的章节树导航，并给出可引用的路径。 | [→](structured-retrieval/INDEX.zh.md) |

## 对比矩阵

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [代码智能](code-intelligence/INDEX.zh.md) | 子分类 | graphify、code-review-graph、Understand-Anything、Ix、Repowise、SCIP、Sourcegraph——代码图与代码搜索索引，交给 agent 一片结构切片而不是原始文件。 |
| [向量检索](vector-search/INDEX.zh.md) | 子分类 | FAISS、Milvus、text2vec——编码器、进程内 ANN 库与向量数据库服务；相似度检索快，但不懂关系。 |
| [结构化检索](structured-retrieval/INDEX.zh.md) | 子分类 | FalkorDB、HelixDB、PageIndex——把遍历与向量／全文索引合在一起的图引擎，以及无向量的文档树索引；比单纯向量检索更费部署或每次查询的 LLM 成本。 |

## 什么该放这里

主要职责是为 RAG **索引与检索**上下文的基础设施——文档索引、代码图、图数据库。不含 agent 记忆（见 `agent-memory`），不含研究 agent（见 `deep-research`）。按**检索什么、怎么检索**选子类：给 agent 用的代码库（`code-intelligence`）、按相似度找 embedding（`vector-search`）、按遍历走图／文档结构（`structured-retrieval`）。
