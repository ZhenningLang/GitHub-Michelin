# coding-agent-memory

> 分类节点。挂在你已经在跑的编码 agent harness 上的记忆——Claude Code、Codex、Cursor、OpenCode——通过 hook、插件、MCP，或一段由 agent 自己遵守的提示块驱动命令行接入：开发者机器上的会话捕获、压缩与注入，以及给一组 agent 共用的共享上下文存储。
> ← 返回 [agent-memory](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Claude Subconscious** | 当你想让一个后台 Letta agent 通过 hook 给 Claude Code 加上跨会话记忆时使用（仅 demo，非生产）。 | C（5/6） | [→](claude-subconscious.zh.md) |
| **claude-mem** | 当你的编码 agent 跨会话丢失上下文、你想要本地 hook/MCP 捕获并压缩后再注入的记忆时用它（star 数存疑）。 | B（6/6） | [→](claude-mem.zh.md) |
| **ByteRover CLI** | 当你想要一款可移植的、带 git 式版本控制和云同步的结构化编码 agent 记忆层时用它——但它极其年轻（2025-06 创建），且许可情况模糊。 | D（6/6） | [→](byterover.zh.md) |
| **OpenViking** | 当多个编码 agent 或一个团队需要共用同一份既装文档又装长期记忆的存储、且你能跑一个服务端时用它——但主仓是 AGPL-3.0，仓库自标 alpha。 | B（6/6） | [→](openviking.zh.md) |
| **Beacon** | 当你各家的 agent 经验互相隔绝、想要一份覆盖所有编码会话的本地轨迹加人工把关的经验沉淀时用它。 | B（6/6） | [→](agent-beacon.zh.md) |
| **Engram** | 当你同时用好几个编码 agent、想让它们共用一份由 agent 自己通过 MCP 写入和检索的本地记忆时用它——一个 Go 程序加一个 SQLite 文件，关键词搜索，不做后台采集。 | B（5/6） | [→](engram.zh.md) |
| **backpass** | 当你的 `AGENTS.md`／`CLAUDE.md` 跟编码 agent 实际犯的错对不上了，想从磁盘上已有的会话记录里挖出改动——每条有两个会话的原话作证、在 token 预算内逐条由你接受——时用它。 | B（6/6） | [→](backpass.zh.md) |
| **OptMem** | 当你想要零活动部件的编码 agent 记忆——一段贴进去的提示块、一个零依赖的 Python 脚本、一份由 agent 自己经营的只追加日志——且能接受自愿捕获、仅正则的检索和没有许可证时用它。 | D（5/6） | [→](optmem.zh.md) |
| **deja-vu** | 当你的各家 agent 反复重排你在另一家 agent 里早已修好的问题，而你想直接用 35 家 harness 已经写进磁盘的会话记录建记忆、不要“保存”环节也不要模型账单时用它。 | B（6/6） | [→](deja-vu.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Claude Subconscious](claude-subconscious.zh.md) | ✅ | C（5/6） | 后台 Letta agent 通过 hook 向 Claude Code 低语记忆；探索性 demo，不用于生产。 |
| [claude-mem](claude-mem.zh.md) | ✅ | B（6/6） | 接进编码 agent 会话生命周期的 hook/MCP 记忆（非与模型无关的应用内记忆 API）；所报 star 数存疑。 |
| [ByteRover CLI](byterover.zh.md) | ✅ | D（6/6） | 面向编码 agent 的可移植结构化记忆，带 git 式版本控制和云同步；极其年轻（2025-06 创建），许可模糊（NOASSERTION 与 Elastic 2.0）。 |
| [OpenViking](openviking.zh.md) | ✅ | B（6/6） | 自托管上下文数据库，把文档 RAG 与会话记忆统一在一个 `viking://` 目录树下并做账号级隔离；代价是一个服务端、两个模型依赖，以及 AGPL-3.0。 |
| [Beacon](agent-beacon.zh.md) | ✅ | B（6/6） | 跨工具会话采集加人工审核的经验沉淀；仓库年轻、厂商驱动、带托管商业层。 |
| [Engram](engram.zh.md) | ✅ | B（5/6） | 不挑 agent 的 MCP 记忆，一个 Go 程序加 SQLite FTS5；没有额外运行时和 LLM 账单，但召回取决于 agent 肯不肯存，且项目年轻、发版极其频繁。 |
| [backpass](backpass.zh.md) | ✅ | B（6/6） | 离线批处理，从 7 家 agent 已有的会话记录里给记忆文件提出有证据门槛的改动；自己不跑常驻进程、不持有密钥，但记录会发给你已登录的模型，且项目才五周大、只有一位维护者。 |
| [OptMem](optmem.zh.md) | ✅ | D（5/6） | 一段提示块加一个只依赖标准库的 Python 单文件：agent 自己往只追加日志里写单行记忆，wake 时读摘要树；什么都不自动化、只有正则检索，而且没有许可证。 |
| [deja-vu](deja-vu.zh.md) | ✅ | B（6/6） | 把 35 家受支持 harness 写在磁盘上的会话记录做成一份词法索引——装上第一天就能搜安装前的历史，一个 Go 单文件、召回不过模型；项目年轻、一人维护、跑分为作者自测。 |

## 什么该放这里

挂在**你正在运行的编码 agent harness**（Claude Code、Codex、Cursor、OpenCode……）上的记忆层——通过 hook、插件、MCP、端点采集，或一段 agent 自己遵守的提示块接入：本地每开发者一份的存储（claude-mem、claude-subconscious、ByteRover、Beacon、Engram、OptMem）、从会话记录里挖改动直接修记忆文件本身的工具（backpass）与多 agent 共享的上下文服务端（OpenViking）。主体是编码会话：决策、约定、轨迹、经验。不含嵌进你自己产品的记忆 API（见 `app-memory`），不含图形态引擎（见 `graph-memory`）。
