# agent-services

> Category node. Deployable runtimes and services for agent workloads — durable sessions, scheduled agents, on-rails customer agents, backlog orchestrators.
> ← back to [agent-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **JiuwenSwarm** | Ready-made leader/team workbench with chat channels; distributed operation adds registry and session constraints. | B (5/6) | [→](jiuwenswarm.md) |
| **Agnes Harness** | Shared local sessions and reviewed business plugins with custom panels; source-only pre-alpha, trusted in-process plugins. | C (6/6) | [→](agnes-harness.md) |
| **Claude Commerce Agents** | You are building the assistant inside a product that sells something and want the shopping/merchant agent layer — prompt, guardrails, UI fill-in, approval — already decided, as a blueprint you read and vendor. | C (5/6) | [→](commerce-agents.md) |
| **eve** | Your agent must wait days for a human or a webhook, survive redeploys, and answer on Slack/Discord/Teams — as one deployable TypeScript service. | A (6/6) | [→](eve.md) |
| **Open Executive** | Use it when a small company needs one self-hosted executive voice over specialist agents, company docs, and Slack — not a framework you assemble, and not a personal pager. | B (4/6) | [→](open-executive.md) |
| **OpenAgentCore** | Use it when your app should drive Codex, Claude Code or MiniMax Code in per-Session sandboxes on your own infrastructure through the OpenAI Agents API — but it is a ten-day-old v0.0.x with no compatibility promises, partial feature parity across harnesses, and no per-Session network isolation. | C (5/6) | [→](openagentcore.md) |
| **OpenBot** | Use it when a company wants governed AI coworkers — each with its own browser-and-shell container, every action policy-checked and audited, any AG-UI agent plugged in — but it's a 6-week-old alpha template that won't boot without CopilotKit's Intelligence service. | B (6/6) | [→](openbot.md) |
| **Open Dots (Anil-matcha)** | Use it when you want to send Claude Code tasks from Telegram or a web page into a throwaway cloud VM and approve each risky action with a button — but it is a ~10-day-old prototype in a repurposed 5.5k-star repo, its API has no auth, it runs only on paid Boat VMs, and it has no LICENSE file. | D (4/6) | [→](open-dots.md) |
| **OpenFang** | You want autonomous agents that run on a schedule from one self-hosted Rust binary. | C (5/6) | [→](openfang.md) |
| **Parlant** | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. | C (5/6) | [→](parlant.md) |
| **Symphony** | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. | C (5/6) | [→](symphony.md) |
| **FastClaw** | Run multiple assistant identities through one Go service with scoped configuration and durable sessions; source-available, host execution by default. | C (4/6) | [→](fastclaw.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [JiuwenSwarm](jiuwenswarm.md) | ✅ | B (5/6) | Packaged multi-agent application, tool approvals and opt-in skill evolution; heavy dependencies and beta version drift. |
| [Agnes Harness](agnes-harness.md) | ✅ | C (6/6) | Workbench, approval records and plugin lifecycle included; customer deployment, hostile-code isolation and cross-platform acceptance remain yours. |
| [Claude Commerce Agents](commerce-agents.md) | ✅ | C (5/6) | Anthropic's reference blueprint for a shopping agent plus a merchant agent over three runtimes; read and vendor it — it is unmaintained and not on any package index. |
| [eve](eve.md) | ✅ | A (6/6) | Your agent must wait days for a human or a webhook, survive redeploys, and answer on Slack/Discord/Teams — as one deployable TypeScript service. |
| [Open Executive](open-executive.md) | ✅ | B (4/6) | Use it when a small company needs one self-hosted executive voice over specialist agents, company docs, and Slack — not a framework you assemble, and not a personal pager. |
| [OpenAgentCore](openagentcore.md) | ✅ | C (5/6) | Self-hosted OpenAI-Agents-API server that runs vendor-native coding harnesses in sandboxes with durable Session state — you operate Core, PostgreSQL and sandbox capacity, on a pre-release with uneven per-harness features. |
| [OpenBot](openbot.md) | ✅ | B (6/6) | Governance-first company agent platform (deny-first CEL policy + audit gateway, per-bot computers, SSO); a clone-and-own alpha that requires CopilotKit's separately licensed Intelligence service. |
| [Open Dots (Anil-matcha)](open-dots.md) | ✅ | D (4/6) | Telegram/web relay that runs `claude -p` in Boat VMs behind a PermissionRequest approval gate, plus cron schedules; buys a phone-first approval loop at the price of no API auth, no license, one agent and one paid sandbox vendor. |
| [OpenFang](openfang.md) | ✅ | C (5/6) | You want autonomous agents that run on a schedule from one self-hosted Rust binary. |
| [Parlant](parlant.md) | ✅ | C (5/6) | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. |
| [Symphony](symphony.md) | ✅ | C (5/6) | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. |
| [FastClaw](fastclaw.md) | ✅ | C (4/6) | Run multiple assistant identities through one Go service with scoped configuration and durable sessions; source-available, host execution by default. |

## What belongs here

Deployable runtimes and services for agent workloads — durable sessions, scheduled agents, on-rails customer agents, backlog orchestrators.
