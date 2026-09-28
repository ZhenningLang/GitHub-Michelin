# app-memory

> 分类节点。你**自己开发的** agent 或产品里内嵌的记忆——记忆库、SDK、客户端包裹器，以及接管 agent 循环的有状态 agent 平台——面向应用数据（用户、实体、长期对话），不面向编码 agent 的会话。
> ← 返回 [agent-memory](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Mem0** | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 | A（6/6） | [→](mem0.zh.md) |
| **Memori** | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 | B（5/6） | [→](memori.zh.md) |
| **Letta (MemGPT)** | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. | B（6/6） | [→](letta.zh.md) |
| **LangMem** | 当你需要在 `agent-memory` 分类中评估 LangMem 时用它。 | B（5/6） | [→](langmem.zh.md) |
| **SimpleMem** | 当你的 LLM 智能体要回答关于长期对话的问题、又不想把原始历史重放进上下文时用它——写入时压缩、有 LoCoMo 公开数字，但仓库年轻学术、PyPI 停在 0.1.0、音视频支持没有基准验证。 | B（5/6） | [→](simplemem.zh.md) |
| **Supermemory** | 当你想把整叠上下文管线——事实抽取、矛盾取代、自动到期、按用户画像、RAG 加记忆混合检索——收到一个 API 或一个自托管二进制后面，并接受引擎只发二进制、许可证翻转过一次时用它。 | A（6/6） | [→](supermemory.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Mem0](mem0.zh.md) | ✅ | A（6/6） | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 |
| [Memori](memori.zh.md) | ✅ | B（5/6） | SQL 优先、包裹客户端的应用记忆，带一个有主张的云与 BYODB 之分。 |
| [Letta (MemGPT)](letta.zh.md) | ✅ | B（6/6） | 有状态 agent 平台，记忆 OS 由运行时自己掌管；适合让 Letta 接管 agent 循环，不适合只想给现有 harness 加上下文。 |
| [LangMem](langmem.zh.md) | ✅ | B（5/6） | 绑在 LangChain／LangGraph 生态上的记忆工具，留在该栈内使用。 |
| [SimpleMem](simplemem.zh.md) | ✅ | B（5/6） | 写入时压缩的记忆库，带 LoCoMo 公开证据；PyPI 冻在 0.1.0（只能源码安装）、存储 bug 未修、音视频支持无基准。 |
| [Supermemory](supermemory.zh.md) | ✅ | A（6/6） | API 优先的记忆＋画像＋混合 RAG，形态是托管服务或单个自托管二进制；引擎源码不公开、基准由厂商自跑、server 通道 v0.0.x，许可证走过 MIT → CC BY-NC-SA → MIT。 |

## 什么该放这里

作为**组件嵌进你自己的 agent 或产品**的记忆：即插即用的记忆 API 与库（Mem0、Memori、SimpleMem）、绑定生态的记忆 SDK（LangMem）、运行时自掌管记忆的有状态 agent 平台（Letta）。记忆的主体是应用数据——用户、实体、长期对话。不含你只是运行着的编码 agent harness 的记忆（见 `coding-agent-memory`），不含作为基础设施单独部署的图形态引擎（见 `graph-memory`）。
