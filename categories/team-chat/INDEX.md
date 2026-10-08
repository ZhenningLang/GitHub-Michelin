# team-chat

> Category node. Self-hostable team chat and collaboration platforms — Slack/Teams
> substitutes, agent-augmented workspaces, and admin-managed multi-LLM chat.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Mattermost** | Self-hosted Slack-style collaboration (chat, calling, screen share) on a single Go binary over PostgreSQL, with enterprise SSO/compliance in a separately licensed tier. | A (5/6) | [→](mattermost.md) |
| **Zulip** | Self-hosted, topic-threaded team chat (Apache-2.0) for async-first teams — a dedicated Ubuntu/Debian host, with voice/video delegated to integrations. | A (6/6) | [→](zulip.md) |
| **Rocket.Chat** | Self-hosted communications platform (MIT CE) with an app marketplace, omnichannel customer support, and native federation — but MongoDB + NATS + microservices ops. | A (5/6) | [→](rocket-chat.md) |
| **Buzz** | Self-hosted Nostr workspace where humans and AI agents are signed, co-equal members over one event log — agent-first, pre-1.0, heavy infrastructure. | B (4/6) | [→](buzz.md) |
| **Macro** | One workspace replacing Slack + Linear + Notion + a CRM + a Gmail client, with everything @-linked in one database and exposed to agents over MCP — AGPL, hosted-first, self-host is still a developer stack. | B (6/6) | [→](macro.md) |
| **HiveChat** | Use it when a 5–50 person team needs a self-hosted chat front-end where an admin holds API keys for many LLM providers and sets per-group model access and token quotas — but it has had no commit since 2025-09 and is still v0.1.0. | D (3/6) | [→](hivechat.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Mattermost](mattermost.md) | ✅ | A (5/6) | Mature single-binary platform with the deepest enterprise controls, but source is AGPL/commercial (only vendor-built binaries are MIT) and features are open-core gated. |
| [Zulip](zulip.md) | ✅ | A (6/6) | Best-organized long-form conversation and a clean Apache-2.0 license, but no native calling and it wants a dedicated host on a supported OS. |
| [Rocket.Chat](rocket-chat.md) | ✅ | A (5/6) | Richest extension surface (marketplace, omnichannel, federation), at the cost of MongoDB + NATS + microservices operations and an EE feature split. |
| [Buzz](buzz.md) | ✅ | B (4/6) | Only option where agents are key-holding members in the same signed log as humans, but it is ~6 months old, pre-1.0, and needs Postgres + Redis + S3. |
| [Macro](macro.md) | ✅ | B (6/6) | Links chat, Gmail, tasks, docs and CRM in one graph agents can read, but it is a young vendor's hosted-first product with a ~40-service, build-from-source self-host. |
| [HiveChat](hivechat.md) | ✅ | D (3/6) | Gets central key custody, group quotas and Feishu/DingTalk/WeCom login in one deployment; costs a mandatory Postgres, a dormant v0.1.0 with no releases, and a license that restricts distributing derivatives. |
| Lobe Chat | 未收录 | — | Other self-hosted chat UIs named on the pages. |
| Slack / Discord / Microsoft Teams | 未收录 | — | Hosted SaaS team chat named across the pages. |

## What belongs here

Self-hostable **team communication and collaboration applications** — chat platforms and Slack/Teams substitutes, agent-augmented workspaces, and admin-managed multi-LLM chat front-ends. Not agent runtimes (see `agent-frameworks`), not memory infra (see `agent-memory`), not single-user desktop chat clients (see `llm-chat-ui`).
