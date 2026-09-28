# vector-search

> 分类节点。RAG 的向量相似检索这条路：把文本编码成向量的句向量模型，以及返回最近邻的 ANN 索引／向量数据库。
> ← 返回[rag-retrieval](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **FAISS** | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 | A（6/6） | [→](faiss.zh.md) |
| **text2vec** | 当你要为中文语义检索或 FAQ 匹配快速拿到句向量、只想一行 pip 装好时用它——它只是编码器，向量索引（FAISS／Milvus）得自己配。 | C（5/6） | [→](text2vec.zh.md) |
| **Milvus** | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search | A（5/6） | [→](milvus.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [FAISS](faiss.zh.md) | ✅ | A（6/6） | 当你需要一个快速的进程内 ANN 向量索引来检索 embedding 时用它——是库，不是托管向量数据库。 |
| [text2vec](text2vec.zh.md) | ✅ | C（5/6） | 当你要为中文语义检索或 FAQ 匹配快速拿到句向量、只想一行 pip 装好时用它——它只是编码器，向量索引（FAISS／Milvus）得自己配。 |
| [Milvus](milvus.zh.md) | ✅ | A（5/6） | Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search |
| Weaviate | 未收录 | — | 各页对比里点到的另一个向量数据库。 |

## 什么该放这里

**基于 embedding 检索**的组件：产出向量的编码器、进程内 ANN 库，以及规模化存储与搜索向量的向量数据库服务。不含图检索或文档结构检索（见 `structured-retrieval`），不含代码索引（见 `code-intelligence`）。
