# team-chat

> 分类节点。可自托管的团队聊天与协作平台——Slack/Teams 的替代品、agent 增强工作区，以及管理员统管的多 LLM 聊天。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Mattermost** | 自托管的 Slack 式协作（聊天、通话、屏幕共享），以单个 Go 二进制跑在 PostgreSQL 上；企业 SSO/合规能力单独授权。 | A（5/6） | [→](mattermost.zh.md) |
| **Zulip** | 自托管、按话题分线程的团队聊天（Apache-2.0），适合异步优先的团队——需一台专用 Ubuntu/Debian 主机，语音/视频交给集成。 | A（6/6） | [→](zulip.zh.md) |
| **Rocket.Chat** | 自托管通信平台（MIT 社区版），带应用市场、全渠道客服与原生联邦——但要运维 MongoDB + NATS + 微服务。 | A（5/6） | [→](rocket-chat.zh.md) |
| **Buzz** | 自托管 Nostr 工作区，人和 AI agent 是同一条事件日志上的签名同等成员——agent 原生、pre-1.0、基础设施重。 | B（4/6） | [→](buzz.zh.md) |
| **Macro** | 用一个工作区替换 Slack + Linear + Notion + CRM + Gmail 客户端，所有东西在同一个库里互相 @ 链接，并通过 MCP 开放给 agent——AGPL、以托管为主，自托管仍是开发者环境。 | B（6/6） | [→](macro.zh.md) |
| **HiveChat** | 当一个 5–50 人的团队需要自托管聊天前端、由管理员统一握住多家大模型的 API key 并按分组控制可见模型和 token 配额时用它——但它自 2025-09 起再无提交，版本仍是 v0.1.0。 | D（3/6） | [→](hivechat.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Mattermost](mattermost.zh.md) | ✅ | A（5/6） | 最成熟的单二进制平台与企业管控，但源码是 AGPL/商业许可（只有厂商编译版是 MIT），功能受 open-core 门禁切分。 |
| [Zulip](zulip.zh.md) | ✅ | A（6/6） | 长对话组织最好、Apache-2.0 许可干净，但没有原生通话，且要求受支持系统上的专用主机。 |
| [Rocket.Chat](rocket-chat.zh.md) | ✅ | A（5/6） | 扩展面最丰富（市场、全渠道、联邦），代价是 MongoDB + NATS + 微服务运维与 EE 功能切分。 |
| [Buzz](buzz.zh.md) | ✅ | B（4/6） | 唯一让 agent 成为与人同处一条签名日志的持钥成员，但项目仅约 6 个月、pre-1.0，且需要 Postgres + Redis + S3。 |
| [Macro](macro.zh.md) | ✅ | B（6/6） | 把聊天、Gmail、任务、文档和 CRM 连成一张 agent 可读的图，但它是一家年轻厂商以托管为主的产品，自托管要从源码编译约 40 个服务。 |
| [HiveChat](hivechat.zh.md) | ✅ | D（3/6） | 换来集中保管 key、分组配额和飞书/钉钉/企业微信登录，一次部署全有；代价是必须配 Postgres、项目停在没发过版的 v0.1.0 且已休眠，许可证还限制分发衍生作品。 |
| Lobe Chat | 未收录 | — | 各页面点到的其他自托管聊天界面。 |
| Slack / Discord / Microsoft Teams | 未收录 | — | 各页面点到的托管 SaaS 团队聊天。 |

## 什么该放这里

面向团队的可自托管**通信与协作应用**——聊天平台与 Slack/Teams 替代品、agent 增强工作区，以及管理员统管的多 LLM 聊天前端。不含 agent 运行时（见 `agent-frameworks`），不含记忆基础设施（见 `agent-memory`），不含单用户桌面聊天客户端（见 `llm-chat-ui`）。
