# agent-services

> Category node. Deployable runtimes and services for agent workloads — durable sessions, scheduled agents, on-rails customer agents, backlog orchestrators.
> ← back to [agent-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Claude Commerce Agents** | You are building the assistant inside a product that sells something and want the shopping/merchant agent layer — prompt, guardrails, UI fill-in, approval — already decided, as a blueprint you read and vendor. | C (5/6) | [→](commerce-agents.md) |
| **eve** | Your agent must wait days for a human or a webhook, survive redeploys, and answer on Slack/Discord/Teams — as one deployable TypeScript service. | A (6/6) | [→](eve.md) |
| **Open Executive** | Use it when a small company needs one self-hosted executive voice over specialist agents, company docs, and Slack — not a framework you assemble, and not a personal pager. | B (4/6) | [→](open-executive.md) |
| **OpenAgentCore** | Use it when your app should drive Codex, Claude Code or MiniMax Code in per-Session sandboxes on your own infrastructure through the OpenAI Agents API — but it is a ten-day-old v0.0.x with no compatibility promises, partial feature parity across harnesses, and no per-Session network isolation. | C (5/6) | [→](openagentcore.md) |
| **OpenBot** | Use it when a company wants governed AI coworkers — each with its own browser-and-shell container, every action policy-checked and audited, any AG-UI agent plugged in — but it's a 6-week-old alpha template that won't boot without CopilotKit's Intelligence service. | B (6/6) | [→](openbot.md) |
| **OpenFang** | You want autonomous agents that run on a schedule from one self-hosted Rust binary. | C (5/6) | [→](openfang.md) |
| **Parlant** | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. | C (5/6) | [→](parlant.md) |
| **Symphony** | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. | C (5/6) | [→](symphony.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Claude Commerce Agents](commerce-agents.md) | ✅ | C (5/6) | Anthropic's reference blueprint for a shopping agent plus a merchant agent over three runtimes; read and vendor it — it is unmaintained and not on any package index. |
| [eve](eve.md) | ✅ | A (6/6) | Your agent must wait days for a human or a webhook, survive redeploys, and answer on Slack/Discord/Teams — as one deployable TypeScript service. |
| [Open Executive](open-executive.md) | ✅ | B (4/6) | Use it when a small company needs one self-hosted executive voice over specialist agents, company docs, and Slack — not a framework you assemble, and not a personal pager. |
| [OpenAgentCore](openagentcore.md) | ✅ | C (5/6) | Self-hosted OpenAI-Agents-API server that runs vendor-native coding harnesses in sandboxes with durable Session state — you operate Core, PostgreSQL and sandbox capacity, on a pre-release with uneven per-harness features. |
| [OpenBot](openbot.md) | ✅ | B (6/6) | Governance-first company agent platform (deny-first CEL policy + audit gateway, per-bot computers, SSO); a clone-and-own alpha that requires CopilotKit's separately licensed Intelligence service. |
| [OpenFang](openfang.md) | ✅ | C (5/6) | You want autonomous agents that run on a schedule from one self-hosted Rust binary. |
| [Parlant](parlant.md) | ✅ | C (5/6) | Use it when you build a customer-facing agent that must stay on-rails via behavioral guidelines — overkill for simple or free-form agents. |
| [Symphony](symphony.md) | ✅ | C (5/6) | Your Linear backlog and Codex agent need a self-hosted orchestrator running isolated per-issue autonomous implementation runs. |

## What belongs here

Deployable runtimes and services for agent workloads — durable sessions, scheduled agents, on-rails customer agents, backlog orchestrators.
