# local-identities

> Local login-state snapshots and browser-profile coordination for coding-agent clients. This is not task orchestration, provider routing or an account-permission service.
> ← back to [agent-tooling](../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CCBaga** | Inspect selected local Claude-state snapshots and linked browser directories; unresolved UI rights and an open restore defect make this information-only, not installation approval. | B (6/6) | [→](ccbaga.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [CCBaga](ccbaga.md) | ✅ | B (6/6) | Local credential/file recovery rather than provider editing; the reviewed version does not guarantee successful round trips or clear copied-UI rights. |
| [CC Switch](../../agent-frameworks/coding-agents/orchestration-and-review/cc-switch.md) | ✅ | B (5/6) | Choose provider/MCP/configuration editing when endpoint settings, not login-state restoration, are the actual problem; it remains indexed in its existing category. |

## What belongs here

Tools whose primary task is capturing, selecting or restoring authorized local client identities and coordinating their browser data. Provider catalogs belong with their existing configuration tools; task dispatch and agent execution belong in agent-frameworks. Each new entry needs its own permission, credential-storage and recovery review.
