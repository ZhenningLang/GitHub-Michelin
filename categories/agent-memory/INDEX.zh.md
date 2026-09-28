# agent-memory

> 分类节点。面向 agent、与 LLM 无关的跨会话持久记忆基础设施。
> 按**记忆属于谁、怎么接进来**拆分子类：自己产品里的记忆组件、挂在你已在跑的编码 agent harness 上的记忆层，或单独部署的图形态引擎。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **应用记忆** | 你自己在做 agent／产品，想要把记忆当组件——一个 API、SDK、客户端包裹器，或接管 agent 循环的平台。 | [→](app-memory/INDEX.zh.md) |
| **编码 agent 记忆** | agent 是你已在跑的编码 harness（Claude Code、Codex、Cursor……），记忆要挂进它们的会话——本地或共享服务端。 | [→](coding-agent-memory/INDEX.zh.md) |
| **图记忆** | 记忆存储该是知识图谱——时间事实图、文档派生的图管线——作为服务或库来跑。 | [→](graph-memory/INDEX.zh.md) |

## 对比矩阵

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [应用记忆](app-memory/INDEX.zh.md) | 子分类 | Mem0、Memori、Letta、LangMem、SimpleMem、Hindsight——面向应用数据（用户、实体、对话）的记忆，在构建期嵌入。 |
| [编码 agent 记忆](coding-agent-memory/INDEX.zh.md) | 子分类 | claude-mem、Claude Subconscious、ByteRover、OpenViking、Beacon——通过 hook／插件／MCP 在你的机器或团队服务端上捕获编码会话。 |
| [图记忆](graph-memory/INDEX.zh.md) | 子分类 | Zep、Graphiti、Cognee——带时间失效或文档到图管线的知识图谱引擎；比文件或向量存储更重。 |

## 什么该放这里

主要职责是**跨会话存取** agent 记忆、且与具体模型无关的基础设施。不含任务/issue 跟踪（见 `agent-tooling`），不含 RAG 文档检索（见 `rag-retrieval`）。按**谁的记忆、怎么接**选子类：自己产品里的组件（`app-memory`）、挂在你运行的编码 agent 上的层（`coding-agent-memory`）、图形态引擎（`graph-memory`）。
