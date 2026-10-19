# supervision-surfaces

> 分类节点。人查看、批准和引导 agent 工作的界面；终端、浏览器、手机与桌面均可。
> ← 返回 [agent-tooling](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Sphinx** | 本地 Git 推送前，按源码回答行为题；可绕过的学习辅助，不是发布授权。 | C（5/6） | [→](sphinx.zh.md) |
| **dsh-TUI** | DeepSeek Harness 的工具、审批和后台任务散在文字里。dsh-TUI 把这些状态投影成终端卡片、面板和会话浏览器。 | B（5/6） | [→](dsh-tui.zh.md) |
| **Agor** | 用实时分支看板协作混合编程助手；接受 BSL，并自行运营数据库与执行安全。 | D（6/6） | [→](agor.zh.md) |
| **Agent Orchestrator** | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI/review/冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 | B（6/6） | [→](agent-orchestrator.zh.md) |
| **Hermes Workspace** | 当你跑的是 Nous 的 hermes-agent、想把它的状态当 Web 驾驶舱用——聊天、memory、skills、终端、tmux swarm 派发、手机经 PWA/Tailscale 可达——但它的增强面板锚定 Hermes gateway/dashboard API、且问世仅约 6 个月时用它。 | B（5/6） | [→](hermes-workspace.zh.md) |
| **Ekko Studio** | 当你同时跑 Hermes Agent **和** Claude Code／Codex 等编码 agent、想要一个本地控制台——单聊、@ 多 agent 的群聊房间、带审批关口的工作流画布、文件与终端——时用它——但它是 BSL-1.1（2029 年前禁止商用）、建仓一个月就从 MIT 改许可、约 5.5 个月大且基本一人编写。 | D（6/6） | [→](ekko-studio.zh.md) |
| **CloudCLI (Claude Code UI)** | 当你的大脑是 Claude Code / Codex / Cursor CLI、想要这些会话的浏览器/移动驾驶舱（文件、终端、git）时用它——但它是 AGPL-3.0-or-later、单人操作形态。 | B（6/6） | [→](claudecodeui.zh.md) |
| **Plannotator** | 当 agent 的产出（计划、diff、HTML 产物）必须由人批注或批准、并把批注当作 agent 下一条指令发回去时用它。 | B（6/6） | [→](plannotator.zh.md) |
| **Pi Web** | 当你的编码 agent 是 pi、想要在它自己的磁盘会话、模型与项目文件之上加一层浏览器工作台——恢复／分支会话、查 diff 和 worktree——时用它——但它约 6 个月大、pre-1.0、单人维护，且锚定 pi 的数据目录。 | B（6/6） | [→](pi-web.zh.md) |
| **Whiteboard** | 当你要 coding agent 亲笔「画」出评审——对钉住的分支生成可交互 RFC，图、引文与代码片段都能点回本地 checkout 的确切行——时用它——但它问世约 6 周、v0.1.x，且评审面只读。 | B（5/6） | [→](whiteboard.zh.md) |
| **Paperclip** | 当你手上已有一支常驻 agent 团队（Claude Code、Codex、OpenClaw、shell／HTTP 机器人），需要一个自托管看板按心跳唤醒它们、一张工单只许一个 agent 领、超预算自动暂停时用它——但它约 7 个月大、已公开 12 条安全公告，且 Windows 上本地运行不可用。 | B（5/6） | [→](paperclip.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Sphinx](sphinx.zh.md) | ✅ | C（5/6） | Git 继续前测试你对已提交行为的预测；增加模型费用与可能误判，不产代码评审意见。 |
| [dsh-TUI](dsh-tui.zh.md) | ✅ | B（5/6） | DeepSeek Harness 的工具、审批和后台任务散在文字里。dsh-TUI 把这些状态投影成终端卡片、面板和会话浏览器。 |
| [Agor](agor.zh.md) | ✅ | D（6/6） | 用实时分支看板协作混合编程助手；接受 BSL，并自行运营数据库与执行安全。 |
| [Agent Orchestrator](agent-orchestrator.zh.md) | ✅ | B（6/6） | 桌面控制面把活铺给多个 agent 各自 worktree，再把 CI/评审反馈路由回来——广度优先，不聚焦单个产物。 |
| [Hermes Workspace](hermes-workspace.zh.md) | ✅ | B（5/6） | 为单一 agent 的全状态做的厂商向 Web 控制台——视图最全，也最绑它宿主的 API。 |
| [Ekko Studio](ekko-studio.zh.md) | ✅ | D（6/6） | 一个本地总机接管 Hermes 加六种编码 agent CLI——含群聊房间与工作流画布——代价是非商业的源码可用许可证。 |
| [CloudCLI (Claude Code UI)](claudecodeui.zh.md) | ✅ | B（6/6） | 从浏览器或手机操办会话（文件、终端、git）——是驾驶，不是评审。 |
| [Plannotator](plannotator.zh.md) | ✅ | B（6/6） | 长在 agent 循环里的人工闸门：批注计划或 diff，决定经 hook 协议回传——代价是极年轻、单人维护。 |
| [Pi Web](pi-web.zh.md) | ✅ | B（6/6） | 在 pi 自己的磁盘状态上加浏览器工作台——会话、模型、文件——只服务一个大脑的 MIT 驾驶舱。 |
| [Whiteboard](whiteboard.zh.md) | ✅ | B（5/6） | agent 亲笔在钉住的分支上画出可交互 RFC——图与引文点回确切代码；评审面只读、问世约 6 周。 |
| [Paperclip](paperclip.zh.md) | ✅ | B（5/6） | 在你现有 agent 之上加一层组织与预算控制面——心跳、原子领取、花费上限、审批——不是 diff 评审闭环；项目年轻，审过安全历史前只放在回环地址或 tailnet 里。 |
| harness 内建的计划批准（Claude Code / Codex） | 非仓库 | — | 零安装，但没有批注、没有渲染后的文档、不留下你批准过什么的记录。 |

## 什么该放这里

主要职责是**人的视图与决定**的界面：评审／批准闸门、会话驾驶舱、共享分支板与多 agent 控制面，不限终端、浏览器或桌面载体。不含以自有执行核心为选型主轴的完整 agent（见 `agent-frameworks`），不含由 LLM 产出评审 finding 的工具（见 `ai-code-review`），不含 agent 运转所依据的任务／计划状态（见 `work-state`），也不是事后的对话记录分析（见 `session-history`）。
