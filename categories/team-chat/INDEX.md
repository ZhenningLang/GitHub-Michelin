# team-chat

> Category node. Self-hostable team chat and collaboration platforms — Slack/Teams
> substitutes, agent-augmented workspaces, and admin-managed multi-LLM chat.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Mattermost** | Self-hosted Slack-style collaboration (chat, calling, screen share) on a single Go binary over PostgreSQL, with enterprise SSO/compliance in a separately licensed tier. | A (5/6) | [→](mattermost.md) |
| **Zulip** | Self-hosted, topic-threaded team chat (Apache-2.0) for async-first teams — a dedicated Ubuntu/Debian host, with voice/video delegated to integrations. | A (5/6) | [→](zulip.md) |
| **Rocket.Chat** | Self-hosted communications platform (MIT CE) with an app marketplace, omnichannel customer support, and native federation — but MongoDB + NATS + microservices ops. | A (5/6) | [→](rocket-chat.md) |
| **Buzz** | Self-hosted Nostr workspace where humans and AI agents are signed, co-equal members over one event log — agent-first, pre-1.0, heavy infrastructure. | B (3/6) | [→](buzz.md) |
| **HiveChat** | Self-hostable, admin-managed AI chat for small/medium teams: one admin wires many LLM providers; the team chats with per-group model access and token quotas. | C (3/6) | [→](hivechat.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Mattermost](mattermost.md) | ✅ | A (5/6) | Mature single-binary platform with the deepest enterprise controls, but source is AGPL/commercial (only vendor-built binaries are MIT) and features are open-core gated. |
| [Zulip](zulip.md) | ✅ | A (5/6) | Best-organized long-form conversation and a clean Apache-2.0 license, but no native calling and it wants a dedicated host on a supported OS. |
| [Rocket.Chat](rocket-chat.md) | ✅ | A (5/6) | Richest extension surface (marketplace, omnichannel, federation), at the cost of MongoDB + NATS + microservices operations and an EE feature split. |
| [Buzz](buzz.md) | ✅ | B (3/6) | Only option where agents are key-holding members in the same signed log as humans, but it is ~6 months old, pre-1.0, and needs Postgres + Redis + S3. |
| [HiveChat](hivechat.md) | ✅ | C (3/6) | Admin-managed multi-LLM team chat with quotas; different job from the comms platforms above. |
| LibreChat / Lobe Chat / Open WebUI | 未收录 | — | Other self-hosted chat UIs named on the pages. |
| Slack / Discord / Microsoft Teams | 未收录 | — | Hosted SaaS team chat named across the pages. |

## What belongs here

Self-hostable **team communication and collaboration applications** — chat platforms and Slack/Teams substitutes, agent-augmented workspaces, and admin-managed multi-LLM chat front-ends. Not agent runtimes (see `agent-frameworks`), not memory infra (see `agent-memory`), not single-user desktop chat clients (see `llm-chat-ui`).
