# messaging-daemons

> Category node. You want a long-lived assistant on your own host or board, reached mainly through existing messaging channels and scheduled jobs.
> ← back to [personal-assistants](../INDEX.md) · root: [category route](../../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Octop** | Use it when a household or small team needs isolated agents on Feishu/WeCom with chats on your disk — not when you want finished office skills, and the LangGraph core is still a private wheel. | B (5/6) | [→](octop.md) |
| **PicoClaw** | Run a chat-driven assistant on a small ARM, MIPS or RISC-V Linux board without a Python/Node.js core runtime; model inference stays separate, remote exec defaults on and process isolation off. | B (6/6) | [→](picoclaw.md) |
| **Hermes Agent** | Use it when you want one long-lived assistant on your own VPS that runs shell commands and scheduled jobs, remembers your environment and answers on Telegram or Slack — but its behaviour drifts as skills and memory change, and it is about 15 months old. | A (4/6) | [→](hermes-agent.md) |
| **OpenClaw** | Use it when you want one personal assistant on your own computer answering across WhatsApp, iMessage, Slack, Telegram and 20+ more channels with shared memory — but one Gateway is one trust domain, so users who do not trust each other must not share it. | B (5/6) | [→](openclaw.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Octop](octop.md) | ✅ | B (5/6) | TencentCloud's self-hosted multi-user assistant for Feishu/WeCom on one Python process; two months old, and the agent runtime is a PyPI wheel whose GitHub repo 404s. |
| [PicoClaw](picoclaw.md) | ✅ | B (6/6) | Cross-compiled Go core with chat adapters, tools and local state; buys deployability on small boards, not local model inference or an enabled-by-default OS sandbox. |
| [Hermes Agent](hermes-agent.md) | ✅ | A (4/6) | Buys persistence under your control — bounded memory, self-written skills, session search and a scheduler; costs determinism, enterprise governance (no SSO, RBAC or audit) and any Lindy track record. |
| [OpenClaw](openclaw.md) | ✅ | B (5/6) | Buys the widest chat-channel coverage plus phone and desktop companion apps; costs tenant isolation, SSO and audit logs, on a project less than a year old. |

## What belongs here

Self-hosted, long-lived assistants whose primary entry points are existing messaging channels and scheduled jobs. Companion clients or dashboards do not exclude them. Chat or scheduling alone does not qualify a desktop artifact layer, ingestion-first memory interface or task-graph workspace; those remain in [personal-assistants](../INDEX.md).
