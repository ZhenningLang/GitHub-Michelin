# vector-search

> 分类节点。RAG 的向量相似检索这条路：把文本编码成向量的句向量模型，以及返回最近邻的 ANN 索引／向量数据库。
> ← 返回[rag-retrieval](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **FAISS** | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 | A（6/6） | [→](faiss.zh.md) |
| **text2vec** | 当你要一行 pip 拿到偏中文的句向量、或用 CoSENT/SBERT 在自己的样本对上微调，做 FAQ 匹配或语义检索时用它——但它只是编码器（索引要配 FAISS 或 Milvus），单一维护者最后一次发版在 2023-09。 | C（5/6） | [→](text2vec.zh.md) |
| **Milvus** | 当向量塞不进一台机器的内存，又要元数据过滤、实时增删、副本和横向扩容的检索服务时用它——但你得运维一个带 etcd 和对象存储的分布式集群；几百万条以内用 FAISS，已有 Postgres 就用 pgvector。 | A（6/6） | [→](milvus.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [FAISS](faiss.zh.md) | ✅ | A（6/6） | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 |
| [text2vec](text2vec.zh.md) | ✅ | C（5/6） | 换来经过筛选的中文 embedding 检查点和训练脚本，带中文 STS 基准成绩；代价是 bus factor 为一、落后于更新的 embedding 模型，还在 sentence-transformers 之上多套一层。 |
| [Milvus](milvus.zh.md) | ✅ | A（6/6） | 计算与存储分离、能横向扩容的过滤向量检索，代价是要运维集群，路线图由同时卖托管 Zilliz Cloud 的 Zilliz 主导。 |
| Weaviate | 未收录 | — | 各页对比里点到的另一个向量数据库。 |

## 什么该放这里

**基于 embedding 检索**的组件：产出向量的编码器、进程内 ANN 库，以及规模化存储与搜索向量的向量数据库服务。不含图检索或文档结构检索（见 `structured-retrieval`），不含代码索引（见 `code-intelligence`）。
