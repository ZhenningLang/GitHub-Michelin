# agent-services

> 分类节点。面向 agent 负载的可部署运行时与服务——持久会话、计划任务型 agent、守规的对客 agent、待办编排器。
> ← 返回 [agent-runtimes](../INDEX.zh.md) · 根：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Claude Commerce Agents** | 你要在一个卖东西的产品里做助手，想直接拿到购物/商家 agent 这一层——prompt、护栏、UI 回填、审批——已经定好，作为一份读来 vendor 的蓝图。 | C（5/6） | [→](commerce-agents.zh.md) |
| **eve** | 你的 agent 要为一个人或一个 webhook 等上好几天、要扛住重新部署，还要能在 Slack／Discord／Teams 上应答——并且是一个可部署的 TypeScript 服务。 | A（6/6） | [→](eve.zh.md) |
| **Open Executive** | 小公司要把领导问题收成一个自托管高管声音——背后是专家 agent、公司文档和 Slack——而不是自己组装框架，也不是个人传呼机。 | B（4/6） | [→](open-executive.zh.md) |
| **OpenAgentCore** | 你的应用要通过 OpenAI Agents API，在自己的基础设施上按会话开沙箱驱动 Codex、Claude Code 或 MiniMax Code——但它只有十天大、还是不做兼容承诺的 v0.0.x，各 harness 功能不对齐，也没有按会话的网络隔离。 | C（5/6） | [→](openagentcore.zh.md) |
| **OpenBot** | 公司要受治理的 AI 同事——每个有自己的浏览器加 shell 容器、每个动作先过策略再留审计、任意 AG-UI agent 可接入——但它是 6 周大的 alpha 模板，缺了 CopilotKit 的 Intelligence 服务就起不来。 | B（6/6） | [→](openbot.zh.md) |
| **Open Dots (Anil-matcha)** | 想从 Telegram 或网页把 Claude Code 任务派进一次性云虚拟机、每个风险动作点按钮审批——但它是挂在一个换过用途的 5.5k 星仓库里、只有十来天的原型，API 无鉴权，只能跑在付费的 Boat 虚拟机上，也没有 LICENSE 文件。 | D（4/6） | [→](open-dots.zh.md) |
| **OpenFang** | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 | C（5/6） | [→](openfang.zh.md) |
| **Parlant** | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 | C（5/6） | [→](parlant.zh.md) |
| **Symphony** | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 | C（5/6） | [→](symphony.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Claude Commerce Agents](commerce-agents.zh.md) | ✅ | C（5/6） | Anthropic 的参考蓝图：一个购物 agent 加一个商家 agent、跑在三条运行时上；读它并 vendor——它不维护，也不在任何包索引里。 |
| [eve](eve.zh.md) | ✅ | A（6/6） | 你的 agent 要为一个人或一个 webhook 等上好几天、要扛住重新部署，还要能在 Slack／Discord／Teams 上应答——并且是一个可部署的 TypeScript 服务。 |
| [Open Executive](open-executive.zh.md) | ✅ | B（4/6） | 小公司要把领导问题收成一个自托管高管声音——背后是专家 agent、公司文档和 Slack——而不是自己组装框架，也不是个人传呼机。 |
| [OpenAgentCore](openagentcore.zh.md) | ✅ | C（5/6） | 自托管的 OpenAI Agents API 服务，在沙箱里跑厂商原生编码 harness 并持久化会话状态——代价是要运维 Core、PostgreSQL 和沙箱算力，而且是预发布版，各 harness 功能参差。 |
| [OpenBot](openbot.zh.md) | ✅ | B（6/6） | 治理优先的公司级 agent 平台（拒绝优先的 CEL 策略加审计闸门、每机器人一台电脑、SSO）；克隆自改的 alpha，必须依赖 CopilotKit 另行授权的 Intelligence 服务。 |
| [Open Dots (Anil-matcha)](open-dots.zh.md) | ✅ | D（4/6） | Telegram／网页中转，在 Boat 虚拟机里跑 `claude -p`，前面挡一道 PermissionRequest 审批，外加 cron 定时任务；换来手机上的审批闭环，代价是 API 无鉴权、无许可证、只支持一种 agent 和一家付费沙箱。 |
| [OpenFang](openfang.zh.md) | ✅ | C（5/6） | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 |
| [Parlant](parlant.zh.md) | ✅ | C（5/6） | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 |
| [Symphony](symphony.zh.md) | ✅ | C（5/6） | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 |

## 什么该放这里

面向 agent 负载的可部署运行时与服务——持久会话、计划任务型 agent、守规的对客 agent、待办编排器。
