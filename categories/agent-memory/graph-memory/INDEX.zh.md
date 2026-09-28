# graph-memory

> 分类节点。存储模型是知识图谱的记忆引擎——带显式失效的时间事实图，以及从文档派生的图管线——作为服务或库来跑，而不是向量库或文件树。
> ← 返回 [agent-memory](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Zep** | Zep \| Examples, Integrations, & More | A（4/6） | [→](zep.zh.md) |
| **Graphiti** | Build Real-Time Knowledge Graphs for AI Agents | B（6/6） | [→](graphiti.zh.md) |
| **Cognee** | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | A（6/6） | [→](cognee.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Zep](zep.zh.md) | ✅ | A（4/6） | 面向用户事实的时间知识图谱记忆，事实会过期或被取代；是应用记忆的后端，不是编码 agent 的钩子层。 |
| [Graphiti](graphiti.zh.md) | ✅ | B（6/6） | 面向 AI agent 的实时知识图谱库；图管线你来搭，边由它维护。 |
| [Cognee](cognee.zh.md) | ✅ | A（6/6） | 自托管的知识图谱记忆引擎，面向文档形态的 agent 记忆；比文件或 SQLite 存储更重。 |

## 什么该放这里

存储模型是**知识图谱**的记忆引擎：带双时态边和显式失效的时间事实图（Zep，以及它底层的 Graphiti 库），以及文档到图的摄取管线（Cognee）。作为服务跑或作为库嵌入都可以——图形态是决定性特征。不含编码 agent 的钩子层（见 `coding-agent-memory`），不含向量库或压缩式记忆 API（见 `app-memory`）。
