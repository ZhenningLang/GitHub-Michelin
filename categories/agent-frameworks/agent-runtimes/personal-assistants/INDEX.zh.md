# personal-assistants

> 分类节点。面向个人使用的成品助手；手机、语音、桌面与工作区形态留在这里，消息常驻助手单列子类。
> ← 返回 [agent-runtimes](../INDEX.zh.md) · 根：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **messaging-daemons** | 你要在自有主机或小板上常驻助手，主要通过现有聊天渠道和定时任务使用。 | [→](messaging-daemons/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LobsterAI** | 你想让办公任务处理本地文件，再从聊天渠道回传结果。LobsterAI 在 OpenClaw 运行时外增加桌面会话、产物和审批界面。 | B（6/6） | [→](lobsterai.zh.md) |
| **Atomic Agent** | 用压缩工具提示词驱动本地工作站操作；仍是开发预览，分析外发默认开启。 | B（6/6） | [→](atomic-agent.zh.md) |
| **OpenHuman** | 当你想要一个本地优先、每 20 分钟把邮件、日历、仓库灌成本机 Markdown 记忆、并且能在 Rust 内核里强制断网的个人助手时用它——但它只有 7 个月，绝大多数提交来自一个人，而且许可是 GPL-3.0-only。 | B（6/6） | [→](openhuman.zh.md) |
| **OpenMuse** | 当你想要一个能派活的自托管个人助理——浏览器接管、隔离 Linux 终端、可恢复且逐项审批的任务——时用它；但它每种模式都强制要求 CopilotKit 云 key，而且是个 12 天大、零 release 的 Alpha。 | B（4/6） | [→](openmuse.zh.md) |
| **OpenWorker** | 当你想要一个用自己的模型 key、在审批闸门和逐次审计记录下把真活干完的桌面 AI 同事时用它——但命令沙箱要手动开启，一键连接器走闭源 OAuth 中转，而且它是个 71 天大的公测版。 | B（6/6） | [→](openworker.zh.md) |
| **Raven** | 当你想要一个入口把一大份需求拆成任务图、分给自带的调研/编程/设计/值守 agent 或 Claude Code、Codex 时用它——但它是四个月大的 pre-alpha，沙箱默认关闭，DAG 节点还可能绕过沙箱（#796）。 | B（6/6） | [→](raven.zh.md) |
| **Rakazo** | 当你想自托管“AI 同事”——每个 bot 有自己的长期对话、定时任务和一台带浏览器、可接管的 Linux 电脑，跑在你的 Docker 主机或沙箱服务上、模型任选——时用它；但它是 7 周大的 beta，实际跟的是 `edge` 镜像，而且 bot 在电脑里执行命令和操作浏览器不经审批。 | B（6/6） | [→](rakazo.zh.md) |
| **OpenMinis** | 当你想让 AI agent 直接在手机上办事——iOS / Android 应用里自带 Linux shell，健康、日历、提醒事项、HomeKit 都是它的工具，模型用你自己的云端 key——时用它；但模型不在端侧跑，隐私类工具默认放行，仓库是不收 PR 的镜像、只看得到一个提交者。 | C（6/6） | [→](openminis.zh.md) |
| **OpenMausBot** | 当你已经在为 Claude Code、Codex 或 Grok CLI 付费，想把它们变成一个聊天应用里的一排 bot——各有自己的模型、电脑和连接的应用，权限请求变成“允许 / 拒绝”卡片——时用它；但审批只是各 CLI 自己的模式，统计默认开启，`enterprise/` 是源码可见许可，而且它只有 8 周大、几乎每天发版。 | B（6/6） | [→](openmausbot.zh.md) |
| **OpenDots** | 当你想自己托管、自己改几个有名字的 AI 同事——每个有自己的角色、工具、文档空间和可选的容器电脑，能聊天、打电话或在 Slack 里找到，存页面和调 MCP 写操作前先问你——时用它；但每段对话都存在 CopilotKit Intelligence，模型只走兼容 OpenAI 的接口，而且是个 9 天大的 Alpha 模板。 | B（4/6） | [→](opendots.zh.md) |
| **Jarvis** | 用本地语音模型和短期转写参与房间讨论；代价是非商业许可与桌面音频配置。 | C（5/6） | [→](jarvis.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [消息常驻服务](messaging-daemons/INDEX.zh.md) | 子分类 | — | 主要入口是既有聊天渠道与定时任务；手机、语音、桌面与工作区形态留在下方。 |
| [LobsterAI](lobsterai.zh.md) | ✅ | B（6/6） | 你想让办公任务处理本地文件，再从聊天渠道回传结果。LobsterAI 在 OpenClaw 运行时外增加桌面会话、产物和审批界面。 |
| [Atomic Agent](atomic-agent.zh.md) | ✅ | B（6/6） | 托管 llama.cpp 并按会话审批；模型硬件与外发策略需明确配置。 |
| [OpenHuman](openhuman.zh.md) | ✅ | B（6/6） | 靠每 20 分钟灌入你的账号来买上下文的本地优先桌面助手，而不是等学习循环；代价是 GPL-3.0-only、构建重、默认要厂商账号。 |
| [OpenMuse](openmuse.zh.md) | ✅ | B（4/6） | CopilotKit 的 MIT 个人助理应用，自带持久浏览器和有界的 Linux 计算机；代价是强制绑定托管的 Intelligence 项目 key。 |
| [OpenWorker](openworker.zh.md) | ✅ | B（6/6） | 吴恩达团队的桌面 cowork 应用：人工底线、长期审批阶梯和审计溯源，不登录可用约 15 家模型；沙箱默认关闭，两人核心，issue 响应弱。 |
| [Raven](raven.zh.md) | ✅ | B（6/6） | EverMind 的宿主 agent（nanobot 分叉），把自带专项 agent 和 13 个第三方 agent 按 DAG 调度，带 EverOS 记忆；换来覆盖面，代价是 pre-alpha 的频繁变动和一个要自己开、自己验证的沙箱。 |
| [Rakazo](rakazo.zh.md) | ✅ | B（6/6） | Elie Steinbock 做的 xAI Grok Bot 开源替代：Pi agent 循环加每个 bot 一台会备份的 Docker/E2B/Daytona/Box 电脑，网页、Electron、Expo 三端；换来不依赖托管服务的持久图形电脑，代价是运维重、隔离只靠容器。 |
| [OpenMinis](openminis.zh.md) | ✅ | C（6/6） | 免费、自带 key 的手机 agent：应用内 Alpine 沙箱（iOS 用 iSH，Android 用 PRoot）加通向系统数据的原生桥；换来不要服务器的设备集成，代价是 iOS 后台限制、一次一条命令的沙箱和宽松的默认权限。 |
| [OpenMausBot](openmausbot.zh.md) | ✅ | B（6/6） | Milind Soni 做的 Grok Bot 开源替代：在一个类 Telegram 的应用里驱动你已登录的 agent CLI（claude、codex、grok），电脑可选 Boat、Local VM 或你自己的 Mac，应用接入走 Composio；换来自带 agent、运维轻，代价是审批原样透传、统计默认开启、还有一层开源内核外的 `enterprise/`。 |
| [OpenDots](opendots.zh.md) | ✅ | B（4/6） | CopilotKit 的 MIT 模板：按角色划权限的多个专职 agent，带文档页面、Slack、通话和 OpenBot 电脑；不连云能启动，但不接厂商的 Intelligence 服务就聊不了天。 |
| [Jarvis](jarvis.zh.md) | ✅ | C（5/6） | 用本地语音模型和短期转写参与房间讨论；代价是非商业许可与桌面音频配置。 |

## 什么该放这里

面向个人使用的成品助手，包括手机助手、语音伴侣、桌面同事与工作区。有聊天适配器或定时器并不直接决定分类。主要以常驻服务部署、通过既有消息渠道接活的助手走 [messaging-daemons](messaging-daemons/INDEX.zh.md)。
