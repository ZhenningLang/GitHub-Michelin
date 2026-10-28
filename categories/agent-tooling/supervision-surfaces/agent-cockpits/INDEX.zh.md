# agent-cockpits

> 分类节点。人要查看和引导任务、会话、团队或业务工作；不表示这些项目共享同一种执行运行时。
> ← 返回 [supervision-surfaces](../INDEX.zh.md) · 根路由：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Kandev** | 用服务端浏览器工作台评审并行编程任务，配置流程关口和执行器；须收窄默认监听并核对归档清理。 | B（6/6） | [→](kandev.zh.md) |
| **Nezha** | 在本地用终端、会话与 Git 视图监管 Claude Code／Codex；须主动选工作树，并接受启动时的 hook 改动。 | C（6/6） | [→](nezha.zh.md) |
| **FounderOS** | 在本地单人界面汇总收入、收件箱与 agent 工作；真实服务和执行后端另接，首次启动的数据是虚构的。 | B（4/6） | [→](founderos.zh.md) |
| **dsh-TUI** | DeepSeek Harness 的工具、审批和后台任务散在文字里。dsh-TUI 把这些状态投影成终端卡片、面板和会话浏览器。 | B（5/6） | [→](dsh-tui.zh.md) |
| **Agor** | 用实时分支看板协作混合编程助手；接受 BSL，并自行运营数据库与执行安全。 | D（6/6） | [→](agor.zh.md) |
| **Agent Orchestrator** | 当你要监管多个跑在真实分支上的并行编码 agent、想要一个桌面控制面把每个隔离进 git worktree 并自动路由 CI/review/冲突反馈时用它——但它约 4.5 个月大、尚未到 1.0、单一 User 所有，且 daemon 是 loopback 无鉴权。 | B（6/6） | [→](agent-orchestrator.zh.md) |
| **Hermes Workspace** | 当你跑的是 Nous 的 hermes-agent、想把它的状态当 Web 驾驶舱用——聊天、memory、skills、终端、tmux swarm 派发、手机经 PWA/Tailscale 可达——但它的增强面板锚定 Hermes gateway/dashboard API、且问世仅约 6 个月时用它。 | B（5/6） | [→](hermes-workspace.zh.md) |
| **Ekko Studio** | 当你同时跑 Hermes Agent **和** Claude Code／Codex 等编码 agent、想要一个本地控制台——单聊、@ 多 agent 的群聊房间、带审批关口的工作流画布、文件与终端——时用它——但它是 BSL-1.1（2029 年前禁止商用）、建仓一个月就从 MIT 改许可、约 5.5 个月大且基本一人编写。 | D（6/6） | [→](ekko-studio.zh.md) |
| **CloudCLI (Claude Code UI)** | 当你的大脑是 Claude Code / Codex / Cursor CLI、想要这些会话的浏览器/移动驾驶舱（文件、终端、git）时用它——但它是 AGPL-3.0-or-later、单人操作形态。 | B（6/6） | [→](claudecodeui.zh.md) |
| **Pi Web** | 当你的编码 agent 是 pi、想要在它自己的磁盘会话、模型与项目文件之上加一层浏览器工作台——恢复／分支会话、查 diff 和 worktree——时用它——但它约 6 个月大、pre-1.0、单人维护，且锚定 pi 的数据目录。 | B（6/6） | [→](pi-web.zh.md) |
| **Paperclip** | 当你手上已有一支常驻 agent 团队（Claude Code、Codex、OpenClaw、shell／HTTP 机器人），需要一个自托管看板按心跳唤醒它们、一张工单只许一个 agent 领、超预算自动暂停时用它——但它约 7 个月大、已公开 12 条安全公告，且 Windows 上本地运行不可用。 | B（5/6） | [→](paperclip.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Kandev](kandev.zh.md) | 已收录 | B（6/6） | 原生服务器整合任务流程、工作树与远程执行；AGPL、可选身份验证及破坏性归档生命周期须主动配置。 |
| [Nezha](nezha.zh.md) | ✅ | C（6/6） | 聚焦两种助手任务与 Git 流程的 Tauri 桌面；工作树可选，会改 Codex 全局 hook，退出应用不保活。 |
| [FounderOS](founderos.zh.md) | ✅ | B（4/6） | SQLite 与外部服务上的 MIT 经营操控界面，不是开箱即用的自治公司，也不是多人工作区。 |
| [dsh-TUI](dsh-tui.zh.md) | ✅ | B（5/6） | DeepSeek Harness 的工具、审批和后台任务散在文字里。dsh-TUI 把这些状态投影成终端卡片、面板和会话浏览器。 |
| [Agor](agor.zh.md) | ✅ | D（6/6） | 用实时分支看板协作混合编程助手；接受 BSL，并自行运营数据库与执行安全。 |
| [Agent Orchestrator](agent-orchestrator.zh.md) | ✅ | B（6/6） | 桌面控制面把活铺给多个 agent 各自 worktree，再把 CI/评审反馈路由回来——广度优先，不聚焦单个产物。 |
| [Hermes Workspace](hermes-workspace.zh.md) | ✅ | B（5/6） | 为单一 agent 的全状态做的厂商向 Web 控制台——视图最全，也最绑它宿主的 API。 |
| [Ekko Studio](ekko-studio.zh.md) | ✅ | D（6/6） | 一个本地总机接管 Hermes 加六种编码 agent CLI——含群聊房间与工作流画布——代价是非商业的源码可用许可证。 |
| [CloudCLI (Claude Code UI)](claudecodeui.zh.md) | ✅ | B（6/6） | 从浏览器或手机操办会话（文件、终端、git）——是驾驶，不是评审。 |
| [Pi Web](pi-web.zh.md) | ✅ | B（6/6） | 在 pi 自己的磁盘状态上加浏览器工作台——会话、模型、文件——只服务一个大脑的 MIT 驾驶舱。 |
| [Paperclip](paperclip.zh.md) | ✅ | B（5/6） | 在你现有 agent 之上加一层组织与预算控制面——心跳、原子领取、花费上限、审批——不是 diff 评审闭环；项目年轻，审过安全历史前只放在回环地址或 tailnet 里。 |

## 什么该放这里

按任务、会话、分支、团队或业务组织持续监管界面。这里包括经营工作台，不要求各项目都是执行运行时。需要审查单个产物或检查行为理解时，转到 [human-review-gates](../human-review-gates/INDEX.zh.md)。
