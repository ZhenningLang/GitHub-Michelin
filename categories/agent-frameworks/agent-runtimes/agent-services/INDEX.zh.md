# agent-services

> 分类节点。面向 agent 负载的可部署运行时与服务——持久会话、计划任务型 agent、守规的对客 agent、待办编排器。
> ← 返回 [agent-runtimes](../INDEX.zh.md) · 根：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Claude Commerce Agents** | 你要在一个卖东西的产品里做助手，想直接拿到购物/商家 agent 这一层——prompt、护栏、UI 回填、审批——已经定好，作为一份读来 vendor 的蓝图。 | C（5/6） | [→](commerce-agents.zh.md) |
| **eve** | 你的 agent 要为一个人或一个 webhook 等上好几天、要扛住重新部署，还要能在 Slack／Discord／Teams 上应答——并且是一个可部署的 TypeScript 服务。 | A（6/6） | [→](eve.zh.md) |
| **Open Executive** | 小公司要把领导问题收成一个自托管高管声音——背后是专家 agent、公司文档和 Slack——而不是自己组装框架，也不是个人传呼机。 | B（3/6） | [→](open-executive.zh.md) |
| **OpenFang** | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 | B（5/6） | [→](openfang.zh.md) |
| **Parlant** | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 | B（6/6） | [→](parlant.zh.md) |
| **Symphony** | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 | C（5/6） | [→](symphony.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Claude Commerce Agents](commerce-agents.zh.md) | ✅ | C（5/6） | Anthropic 的参考蓝图：一个购物 agent 加一个商家 agent、跑在三条运行时上；读它并 vendor——它不维护，也不在任何包索引里。 |
| [eve](eve.zh.md) | ✅ | A（6/6） | 你的 agent 要为一个人或一个 webhook 等上好几天、要扛住重新部署，还要能在 Slack／Discord／Teams 上应答——并且是一个可部署的 TypeScript 服务。 |
| [Open Executive](open-executive.zh.md) | ✅ | B（3/6） | 小公司要把领导问题收成一个自托管高管声音——背后是专家 agent、公司文档和 Slack——而不是自己组装框架，也不是个人传呼机。 |
| [OpenFang](openfang.zh.md) | ✅ | B（5/6） | 想用单个自托管 Rust 二进制、让自治智能体按计划 7×24 无人值守干活时。 |
| [Parlant](parlant.zh.md) | ✅ | B（6/6） | 当你要构建一个必须靠行为准则严格守规的对客 agent 时用它——简单或自由式 agent 用它过重。 |
| [Symphony](symphony.zh.md) | ✅ | C（5/6） | 你的 Linear 待办和 Codex agent 需要一个自托管编排器、按 issue 跑隔离自治实现运行时。 |

## 什么该放这里

面向 agent 负载的可部署运行时与服务——持久会话、计划任务型 agent、守规的对客 agent、待办编排器。
