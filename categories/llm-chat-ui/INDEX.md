# llm-chat-ui

> Category node. Self-deployable AI chat client front-ends over many LLM providers (single-user / BYOK).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **NextChat** | Use it when you want a private, self-deployable multi-provider AI chat UI across web/desktop/mobile — not a multi-user RBAC team platform. | B (6/6) | [→](nextchat.md) |
| **Open WebUI** | Use it when you serve local models through Ollama and want a ChatGPT-style web UI with accounts, group permissions and document RAG, even fully offline — but its license is not OSI-approved and forbids rebranding above 50 users without permission. | B (5/6) | [→](open-webui.md) |
| **LibreChat** | Use it when an organisation wants one self-hosted, SSO-protected chat app where staff pick OpenAI, Anthropic, Bedrock, Azure or local models from one menu, with history in your database — but it requires MongoDB and ClickHouse has owned it since 2025. | B (5/6) | [→](librechat.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [NextChat](nextchat.md) | ✅ | B (6/6) | Light, cross-platform, one-click-deploy chat UI; single-user-shaped, not RBAC/quota team admin. |
| [Open WebUI](open-webui.md) | ✅ | B (5/6) | The shortest path from local models to a shared chat workspace, at the cost of a custom branding license, a CLA and a founder-dominated roadmap. |
| [HiveChat](../team-chat/hivechat.md) | ✅ | D (3/6) | Admin-managed multi-user team chat with per-group model access and token quotas. |
| Lobe Chat | 未收录 | — | Other self-hosted chat UIs named across the pages (some with multi-user/RBAC). |

## What belongs here

Self-deployable **chat client front-ends** a single user (or small group) points at their own LLM provider keys. For admin-managed multi-user team chat with quotas see `team-chat`; for agent frameworks see `agent-frameworks`.
