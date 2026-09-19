# knowledge-base

> 分类节点。个人知识库与「第二大脑」应用——积累、互链并查询你自己的文档语料，可选由 LLM 维护。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LLM Wiki** | 当你希望自己的文档被一次性编译成一份本地互链维基、由 LLM 持续保鲜，而不是每次查询都用 RAG 重新推导时用它。 | B（4/6） | [→](llm-wiki.zh.md) |
| **Logseq** | 当你想要一个本地优先、由你自己撰写并用 Datalog 查询的大纲笔记工具、且 LLM 能力交给插件时用它。 | B（5/6） | [→](logseq.zh.md) |
| **SiYuan** | 当你想要一个自托管、块级引用的知识工作空间、让人与 AI 智能体共同编辑时用它——但部分功能需付费（open-core）。 | B（5/6） | [→](siyuan.zh.md) |
| **Khoj** | 当你想要一个可自托管的 AI 第二大脑、从你的文档与网络取答案、并覆盖浏览器／桌面／Obsidian、模型可选本地或在线时用它。 | C（6/6） | [→](khoj.zh.md) |
| **Reor** | 当你需要一份「本地优先 AI 笔记」的模式参考时用它；它已归档（2025-05），不要把生产押在它上面。 | E（4/6） | [→](reor.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LLM Wiki](llm-wiki.zh.md) | ✅ | B（4/6） | 把资料编译成一份受共同演化 schema 约束、持续维护的维基——但项目年轻（2026-04）、单人维护，且预编译的错误日后会被信任。 |
| [Logseq](logseq.zh.md) | ✅ | B（5/6） | 成熟、本地优先的大纲工具，支持 Datalog 查询、社区庞大——但互链靠人肉，且 DB 重写仍是 beta 并带数据丢失警告。 |
| [SiYuan](siyuan.zh.md) | ✅ | B（5/6） | 块级引用、Go 内核、支持 Docker 自托管——但有 open-core 付费墙和单一厂商生态。 |
| [Khoj](khoj.zh.md) | ✅ | C（6/6） | 第二大脑触面最广（网页／桌面／Obsidian／WhatsApp）、支持多种 LLM——但 Python + pgvector 运维更重，发布线停滞。 |
| [Reor](reor.zh.md) | ✅ | E（4/6） | 与 LLM Wiki 最直接的同型竞品（本地 embedding + Ollama + LanceDB）——但已归档，只能当模式参考。 |
| NotebookLM / Obsidian | 未收录 | — | 各页点到的托管 SaaS 与专有免费软件：不是可收录的仓库。 |

## 什么该放这里

让人**积累自己的知识语料并查询它**的面向用户的系统——个人维基、大纲笔记、AI「第二大脑」应用。不含其底层的检索基础设施（见 `rag-retrieval`），不含 agent 读写你的记忆（见 `agent-memory`），也不含团队协作（见 `team-chat`）。
