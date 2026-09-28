# supervision-surfaces

> 分类节点。人看的那块屏：对 agent 产出的评审与批准闸门、会话的浏览器/移动驾驶舱，以及同时盯着多个 agent 的桌面控制面。
> ← 返回 [agent-tooling](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Agent Orchestrator** | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI/review/冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 | B（6/6） | [→](agent-orchestrator.zh.md) |
| **Hermes Workspace** | 当你跑的是 Nous 的 hermes-agent、想把它的状态当 Web 驾驶舱用——聊天、memory、skills、终端、tmux swarm 派发、手机经 PWA/Tailscale 可达——但它的增强面板锚定 Hermes gateway/dashboard API、且问世仅约 6 个月时用它。 | B（5/6） | [→](hermes-workspace.zh.md) |
| **Ekko Studio** | 当你同时跑 Hermes Agent **和** Claude Code／Codex 等编码 agent、想要一个本地控制台——单聊、@ 多 agent 的群聊房间、带审批关口的工作流画布、文件与终端——时用它——但它是 BSL-1.1（2029 年前禁止商用）、建仓一个月就从 MIT 改许可、约 5.5 个月大且基本一人编写。 | D（6/6） | [→](ekko-studio.zh.md) |
| **CloudCLI (Claude Code UI)** | 当你的大脑是 Claude Code / Codex / Cursor CLI、想要这些会话的浏览器/移动驾驶舱（文件、终端、git）时用它——但它是 AGPL-3.0-or-later、单人操作形态。 | B（6/6） | [→](claudecodeui.zh.md) |
| **Plannotator** | 当 agent 的产出（计划、diff、HTML 产物）必须由人批注或批准、并把批注当作 agent 下一条指令发回去时用它。 | B（6/6） | [→](plannotator.zh.md) |
| **Pi Web** | 当你的编码 agent 是 pi、想要在它自己的磁盘会话、模型与项目文件之上加一层浏览器工作台——恢复／分支会话、查 diff 和 worktree——时用它——但它约 6 个月大、pre-1.0、单人维护，且锚定 pi 的数据目录。 | B（6/6） | [→](pi-web.zh.md) |
| **Whiteboard** | 当你要 coding agent 亲笔「画」出评审——对钉住的分支生成可交互 RFC，图、引文与代码片段都能点回本地 checkout 的确切行——时用它——但它问世约 6 周、v0.1.x，且评审面只读。 | B（5/6） | [→](whiteboard.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Agent Orchestrator](agent-orchestrator.zh.md) | ✅ | B（6/6） | 桌面控制面把活铺给多个 agent 各自 worktree，再把 CI/评审反馈路由回来——广度优先，不聚焦单个产物。 |
| [Hermes Workspace](hermes-workspace.zh.md) | ✅ | B（5/6） | 为单一 agent 的全状态做的厂商向 Web 控制台——视图最全，也最绑它宿主的 API。 |
| [Ekko Studio](ekko-studio.zh.md) | ✅ | D（6/6） | 一个本地总机接管 Hermes 加六种编码 agent CLI——含群聊房间与工作流画布——代价是非商业的源码可用许可证。 |
| [CloudCLI (Claude Code UI)](claudecodeui.zh.md) | ✅ | B（6/6） | 从浏览器或手机操办会话（文件、终端、git）——是驾驶，不是评审。 |
| [Plannotator](plannotator.zh.md) | ✅ | B（6/6） | 长在 agent 循环里的人工闸门：批注计划或 diff，决定经 hook 协议回传——代价是极年轻、单人维护。 |
| [Pi Web](pi-web.zh.md) | ✅ | B（6/6） | 在 pi 自己的磁盘状态上加浏览器工作台——会话、模型、文件——只服务一个大脑的 MIT 驾驶舱。 |
| [Whiteboard](whiteboard.zh.md) | ✅ | B（5/6） | agent 亲笔在钉住的分支上画出可交互 RFC——图与引文点回确切代码；评审面只读、问世约 6 周。 |
| harness 内建的计划批准（Claude Code / Codex） | 非仓库 | — | 零安装，但没有批注、没有渲染后的文档、不留下你批准过什么的记录。 |

## 什么该放这里

主要职责是**人的视图与决定**的界面：评审/批准闸门、会话驾驶舱、多 agent 控制面。不含由 LLM 产出评审 finding 的工具（见 `ai-code-review`），不含 agent 运转所依据的任务/计划状态（见 `work-state`），也不是事后的对话记录分析（见 `session-history`）。
