# workflow-builders

> Category node. Prompt optimizers and visual/code-first platforms for building LLM workflows and agentic applications.
> ← back to [agent-frameworks](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **DSPy** | You have eval data and a metric and want optimizers to compile prompts instead of hand-tuning them. | A (6/6) | [→](dspy.md) |
| **SkillOpt** | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. | B (6/6) | [→](skillopt.md) |
| **AutoGPT** | Use it when a recurring multi-app chore (Gmail, CRM lookup, LLM draft, Slack post) should become a scheduled agent built on a canvas or from a plain-English description — but the platform is PolyForm Shield, not OSI open source, and self-hosting is heavy. | B (5/6) | [→](autogpt.md) |
| **Dify** | Use it when a team needs several LLM apps — a docs Q&A bot, a ticket-triage workflow — built on a canvas over knowledge bases, each with a web UI and API on publish — but its license forbids unapproved multi-tenant hosting and logo removal. | B (5/6) | [→](dify.md) |
| **LangChain** | Use it when a Python assistant must call your tools across OpenAI, Claude and local models without rewriting schemas and the tool loop per provider — but skip it for single-prompt apps, and go straight to LangGraph for hand-designed control flow. | A (6/6) | [→](langchain.md) |
| **Langflow** | Use it when you want to wire prompts, retrievers and tools on a canvas, test them in a chat panel, then call the flow as an HTTP API or MCP tool — but its advisories include unauthenticated RCE, so expose it only with weekly patching. | B (6/6) | [→](langflow.md) |
| **LlamaIndex** | Use it when a Python app must answer from your own PDFs, wikis or tickets and you want the load, chunk, embed and retrieve pipeline in a few lines — but the company now focuses on paid LlamaParse, making the open framework a side line. | A (6/6) | [→](llamaindex.md) |
| **Flowise** | Use it only when you already run Flowise chatflows and need to plan a fork or a migration — but the repo was archived on 2026-08-13 and support ended on 2026-08-31, so new projects belong on Langflow or Dify. | D (5/6) | [→](flowise.md) |
| **Agent-Native** | You want the agent inside your product to actually perform its tasks, and you'll let one TypeScript app own the UI, server and Postgres so the button and the tool share one implementation. | C (4/6) | [→](agent-native.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [DSPy](dspy.md) | ✅ | A (6/6) | You have eval data and a metric and want optimizers to compile prompts instead of hand-tuning them. |
| [SkillOpt](skillopt.md) | ✅ | B (6/6) | Use it when you must optimize an agent's natural-language skill doc for a frozen LLM against a scorable benchmark — but without a reliable eval to gate edits the method has no signal, and it's a brand-new v0.1.0. |
| [AutoGPT](autogpt.md) | ✅ | B (5/6) | Buys LLM-native automation with schedules, webhooks and app blocks in one platform; costs a competition-restricted license plus CLA, a still-beta version line, and Postgres, Redis, RabbitMQ and more to host. |
| [Dify](dify.md) | ✅ | B (5/6) | Buys one self-hosted workspace for RAG apps, workflows and their APIs; costs a custom Apache-plus-conditions license the vendor may tighten, with SSO and RBAC held back for paid Enterprise. |
| [LangChain](langchain.md) | ✅ | A (6/6) | Buys one interface over hundreds of model and tool integrations plus a prebuilt `create_agent` loop; costs abstraction weight, reorganisations at each major version, and a pull toward paid LangSmith. |
| [Langflow](langflow.md) | ✅ | B (6/6) | Buys fast visual iteration with editable Python behind every node under a plain MIT license; costs a server-side code-execution surface for anyone who can edit flows, and flows that are harder to review than code. |
| [Agent-Native](agent-native.md) | ✅ | C (4/6) | One action powers the button and the agent tool plus a full app (auth, SQL state, chat) — the price is letting the framework own your stack, and it is a six-month-old, fast-moving v0.x. |

## What belongs here

Prompt optimizers and visual/code-first platforms for building LLM workflows and agentic applications.
