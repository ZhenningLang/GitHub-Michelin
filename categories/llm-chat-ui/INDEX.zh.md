# llm-chat-ui

> 分类节点。可自部署、跨多 LLM provider 的 AI 聊天客户端前端（单用户 / BYOK）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **NextChat** | 当你想要一个私有、可自部署、跨 web/桌面/移动 的多 provider AI 聊天前端时用它——不是多用户 RBAC 团队平台。 | A（5/6） | [→](nextchat.zh.md) |
| **Open WebUI** | 当你想要一个自托管 AI 聊天平台，内置 RAG、支持 Ollama、可完全离线运行时用它——但默认偏单用户。 | B（6/6） | [→](open-webui.zh.md) |
| **LibreChat** | Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini, Artifacts, AI model switching, message search, Code Interpreter, langchain, DALL-E-3, OpenAPI Actions, Functions, Secure Multi-User Auth, Presets, open-source for self-hosting. Active | B（6/6） | [→](librechat.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [NextChat](nextchat.zh.md) | ✅ | A（5/6） | 轻量、跨平台、一键部署的聊天前端；偏单用户，不做 RBAC/配额团队管理。 |
| [Open WebUI](open-webui.zh.md) | ✅ | B（6/6） | 自托管 AI 聊天平台，内置 RAG 且支持 Ollama；可离线运行，但默认偏单用户。 |
| [HiveChat](../team-chat/hivechat.zh.md) | ✅ | B（4/6） | 管理员统管的多用户团队聊天，带分组模型权限和 token 配额。 |
| LibreChat / Lobe Chat | 未收录 | — | 各页对比里点到的其他自托管聊天前端（部分带多用户/RBAC）。 |

## 什么该放这里

单用户（或小团队）指向自己的 LLM provider key 的**可自部署聊天客户端前端**。需要管理员统管、带配额的多用户团队聊天见 `team-chat`;agent 框架见 `agent-frameworks`。
