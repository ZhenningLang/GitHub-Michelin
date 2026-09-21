# agent-memory

> 分类节点。面向 agent、与 LLM 无关的跨会话持久记忆基础设施。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Mem0** | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 | A（6/6） | [→](mem0.zh.md) |
| **Memori** | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 | B（5/6） | [→](memori.zh.md) |
| **Claude Subconscious** | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用（仅 demo，非生产）。 | C（6/6） | [→](claude-subconscious.zh.md) |
| **claude-mem** | 当你的编码 agent 跨会话丢失上下文、你想要本地 hook/MCP 捕获并压缩后再注入的记忆时用它（star 数存疑）。 | B（6/6） | [→](claude-mem.zh.md) |
| **ByteRover CLI** | 当你想要一款可移植的、带 git 式版本控制和云同步的结构化编码 agent 记忆层时用它——但它极其年轻（2025-06 创建），且许可情况模糊。 | D（6/6） | [→](byterover.zh.md) |
| **Letta (MemGPT)** | Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. | B（5/6） | [→](letta.zh.md) |
| **Zep** | Zep \| Examples, Integrations, & More | A（4/6） | [→](zep.zh.md) |
| **Graphiti** | Build Real-Time Knowledge Graphs for AI Agents | B（6/6） | [→](graphiti.zh.md) |
| **LangMem** | 当你需要在 `agent-memory` 分类中评估 LangMem 时用它。 | B（5/6） | [→](langmem.zh.md) |
| **Cognee** | Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory across sessions with a self-hosted knowledge graph engine. | A（6/6） | [→](cognee.zh.md) |
| **OpenViking** | 当多个编码 agent 或一个团队需要共用同一份既装文档又装长期记忆的存储、且你能跑一个服务端时用它——但主仓是 AGPL-3.0，仓库自标 alpha。 | B（6/6） | [→](openviking.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Mem0](mem0.zh.md) | ✅ | A（6/6） | 当你的 LLM agent 需要跨会话记住用户、又不想撑爆 prompt 上下文时用它。 |
| [Memori](memori.zh.md) | ✅ | B（5/6） | 当你想要 LLM 无关、通过包裹现有客户端自动捕获并召回的持久化 agent 记忆时使用。 |
| [Claude Subconscious](claude-subconscious.zh.md) | ✅ | C（6/6） | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用（仅 demo，非生产）。 |
| [claude-mem](claude-mem.zh.md) | ✅ | B（6/6） | 接进编码 agent 会话生命周期的 hook/MCP 记忆（非与模型无关的应用内记忆 API）；所报 star 数存疑。 |
| [ByteRover CLI](byterover.zh.md) | ✅ | D（6/6） | 面向编码 agent 的可移植结构化记忆，带 git 式版本控制和云同步；极其年轻（2025-06 创建），许可模糊（NOASSERTION 与 Elastic 2.0）。 |
| [Letta (MemGPT)](letta.zh.md) | ✅ | B（5/6） | 有状态 agent 平台，记忆 OS 由运行时自己掌管；适合让 Letta 接管 agent 循环，不适合只想给现有 harness 加上下文。 |
| [Zep](zep.zh.md) | ✅ | A（4/6） | 面向用户事实的时间知识图谱记忆，事实会过期或被取代；是应用记忆的后端，不是编码 agent 的钩子层。 |
| [Cognee](cognee.zh.md) | ✅ | A（6/6） | 自托管的知识图谱记忆引擎，面向文档形态的 agent 记忆；比文件或 SQLite 存储更重。 |
| [OpenViking](openviking.zh.md) | ✅ | B（6/6） | 自托管上下文数据库，把文档 RAG 与会话记忆统一在一个 `viking://` 目录树下并做账号级隔离；代价是一个服务端、两个模型依赖，以及 AGPL-3.0。 |

## 什么该放这里

主要职责是**跨会话存取** agent 记忆、且与具体模型无关的基础设施。不含任务/issue 跟踪（见 `agent-tooling`），不含 RAG 文档检索（见 `rag-retrieval`）。
