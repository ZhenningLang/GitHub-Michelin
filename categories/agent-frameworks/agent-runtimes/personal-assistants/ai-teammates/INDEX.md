# ai-teammates

> Category node. You want a standing roster of several named bots — each with its own role, model, memory and often its own computer — that you message one by one or put in group chats.
> ← back to [personal-assistants](../INDEX.md) · root: [category route](../../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Rakazo** | Use it when you want self-hosted AI teammates — persistent bots, each with its own thread, routines and a Linux computer with a browser you can take over, on your Docker host or a sandbox provider and any model — but it is a 7-week-old beta tracking the `edge` image, and shell/browser actions inside the computer skip approval. | B (6/6) | [→](rakazo.md) |
| **OpenMausBot** | Use it when you already pay for Claude Code, Codex or the Grok CLI and want them as a roster of named bots in one chat app — each with its own model, computer and connected apps, permission prompts as Allow/Deny cards — but approvals are the CLIs' own modes, analytics are on by default, `enterprise/` is source-available, and it is 8 weeks old with near-daily releases. | B (6/6) | [→](openmausbot.md) |
| **OpenDots** | Use it when you want a few named AI coworkers you host and fork — each with its own role, tools, document Spaces and optional container computer, reachable by chat, voice call or Slack, asking before saves and MCP writes — but every conversation lives in CopilotKit Intelligence, the model path is OpenAI-compatible only, and it is a 9-day-old alpha template. | B (4/6) | [→](opendots.md) |
| **DS Bot** | Use it when you want a standing team of DeepSeek Harness bots — each with its own memory, model, folder and permissions, a Main Bot that sets up the rest, and group chats where an admin routes the work — but it is a six-week-old DSH plugin pinned to a release candidate, with unsigned installers and a full-access Docker edition. | C (5/6) | [→](ds-bot.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Rakazo](rakazo.md) | ✅ | B (6/6) | Elie Steinbock's open alternative to xAI's Grok Bot: Pi agent loop plus a checkpointed Docker/E2B/Daytona/Box computer per bot, web/Electron/Expo clients; buys durable graphical computers with no hosted dependency at the price of heavy ops and container-only isolation. |
| [OpenMausBot](openmausbot.md) | ✅ | B (6/6) | Milind Soni's open Grok Bot alternative that drives the agent CLIs you already log into (claude, codex, grok) from a Telegram-style app, with Boat/Local VM/your-own-Mac computers and Composio apps; buys BYO-agent with light ops at the price of passthrough approvals, default-on analytics and an open-core `enterprise/` layer. |
| [OpenDots](opendots.md) | ✅ | B (4/6) | CopilotKit's MIT clone-and-edit workspace of role-scoped specialist agents with pages, Slack, calls and OpenBot computers; boots offline but cannot chat without the vendor's Intelligence service. |
| [DS Bot](ds-bot.md) | ✅ | C (5/6) | Fei2411's DSH plugin and desktop app that turns DeepSeek Harness sessions into long-lived bots with reviewed memory, a context steward and admin-first group chats; buys persistent roles on API-billed models at the price of DSH release-candidate coupling and extra model calls per turn. |

## What belongs here

Products whose unit is a roster of several named, long-lived bots: each bot has its own identity (role, model or personality), memory and often its own computer or connected apps, and you reach them individually or in group/channel chats. One owner's single assistant — a desktop coworker, an errand-runner, a phone agent, or a host agent that splits one brief across specialists ([Raven](../raven.md)) — stays in [personal-assistants](../INDEX.md); assistants whose primary entry point is an existing messaging channel go in [messaging-daemons](../messaging-daemons/INDEX.md).
