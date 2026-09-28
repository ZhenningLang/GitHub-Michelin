# agent-runtimes

> Category node. Reusable frameworks and runtimes for autonomous agents, multi-agent execution, or on-rails agent behavior.
> ← back to [agent-frameworks](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Agent SDKs** | You are writing the agent yourself and need the loop, orchestration and tool plumbing in your own code. | [→](agent-sdks/INDEX.md) |
| **Personal Assistants** | You want a ready assistant for yourself rather than a library to program against. | [→](personal-assistants/INDEX.md) |
| **Agent Services** | An agent workload must run as infrastructure you deploy and operate, not as a chat window. | [→](agent-services/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Docker Agent** | Use it when the deliverable is a shareable YAML — model, instruction, toolsets, teammates — that `docker agent run` executes locally, like an image; not when the agent loop must live inside your program. | B (6/6) | [→](docker-agent.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [Agent SDKs](agent-sdks/INDEX.md) | Sub-category | Code-first libraries and frameworks you build an agent (or a team of them) with, inside your own program. |
| [Personal Assistants](personal-assistants/INDEX.md) | Sub-category | Packaged assistants aimed at one person: install it, connect it to your accounts/model, and talk to it. |
| [Agent Services](agent-services/INDEX.md) | Sub-category | Deployable runtimes and services for agent workloads — durable sessions, scheduled agents, on-rails customer agents, backlog orchestrators. |
| [Docker Agent](docker-agent.md) | Project page | Build and run agents from one declarative YAML — MCP tools, multi-agent delegation, approval-gated execution, OCI sharing — as a local CLI, not a hosted platform. |

## What belongs here

Navigate by how you intend to use the agent: a code-first SDK, a packaged personal assistant, or a deployable agent service.
