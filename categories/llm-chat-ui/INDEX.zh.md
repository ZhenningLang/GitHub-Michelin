# llm-chat-ui

> 分类节点。可自部署、跨多 LLM provider 的 AI 聊天客户端前端（单用户 / BYOK）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **NextChat** | 当你想要一个私有、可自部署、跨 web/桌面/移动 的多 provider AI 聊天前端时用它——不是多用户 RBAC 团队平台。 | B（6/6） | [→](nextchat.zh.md) |
| **Open WebUI** | 当你用 Ollama 跑本地模型，想要一个带账号、分组权限和文档问答的 ChatGPT 式网页界面，甚至完全离线运行时用它——但许可证不是 OSI 认可的，超过 50 个用户的部署未经许可不得换品牌。 | B（5/6） | [→](open-webui.zh.md) |
| **LibreChat** | 当一个组织想要一套挂在 SSO 后面的自托管聊天应用，让员工在同一个菜单里选 OpenAI、Anthropic、Bedrock、Azure 或本地模型，聊天记录留在自己的数据库里时用它——但必须用 MongoDB，且自 2025 年起归 ClickHouse 所有。 | B（5/6） | [→](librechat.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [NextChat](nextchat.zh.md) | ✅ | B（6/6） | 轻量、跨平台、一键部署的聊天前端；偏单用户，不做 RBAC/配额团队管理。 |
| [Open WebUI](open-webui.zh.md) | ✅ | B（5/6） | 从本地模型到多人共享聊天工作台的最短路径，代价是带品牌条款的自定义许可、CLA 和创始人主导的路线图。 |
| [HiveChat](../team-chat/hivechat.zh.md) | ✅ | D（3/6） | 管理员统管的多用户团队聊天，带分组模型权限和 token 配额。 |
| Lobe Chat | 未收录 | — | 各页对比里点到的其他自托管聊天前端（部分带多用户/RBAC）。 |

## 什么该放这里

单用户（或小团队）指向自己的 LLM provider key 的**可自部署聊天客户端前端**。需要管理员统管、带配额的多用户团队聊天见 `team-chat`;agent 框架见 `agent-frameworks`。
