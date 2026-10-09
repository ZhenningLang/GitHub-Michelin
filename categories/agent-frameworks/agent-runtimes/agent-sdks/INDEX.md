# agent-sdks

> Category node. Code-first libraries and frameworks you build an agent (or a team of them) with, inside your own program.
> ← back to [agent-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **AgentScope** | Shipping a production multi-agent LLM service needing sandboxed tools, permissions, tracing, and human-in-the-loop. | B (6/6) | [→](agentscope.md) |
| **AutoGen** | Use it when you already ship a Python or .NET multi-agent system on AutoGen's AgentChat or Core runtime and rewriting is the bigger risk — but it is in maintenance mode; start new projects on Microsoft Agent Framework. | B (5/6) | [→](autogen.md) |
| **CrewAI** | Use it when a knowledge-work job splits naturally into roles (researcher, analyst, writer) and you would rather declare agents and tasks than wire a graph — but hand-offs are decided by prompts, and the core package pulls in a heavy dependency set. | A (6/6) | [→](crewai.md) |
| **LangGraph** | Use it when an agent runs for minutes or days and must pause for human approval or survive a restart mid-run — but you assemble the loop node by node, and the official self-hosted production server needs a LangSmith license. | A (6/6) | [→](langgraph.md) |
| **Microsoft Agent Framework** | You want Microsoft's successor to AutoGen + Semantic Kernel: self-looping agents first, typed graph workflows and .NET parity when production needs them. | A (6/6) | [→](agent-framework.md) |
| **OpenAI Agents SDK** | Use it when your product already runs on OpenAI models and you want a tool loop, agent hand-offs and traces from a few primitives — but runs do not survive crashes without Temporal-style infrastructure, and non-OpenAI providers go through beta adapters. | A (6/6) | [→](openai-agents-sdk.md) |
| **Pydantic AI** | Use it when a Python service needs an LLM step that returns a validated Pydantic type and you want to swap model providers with a string — but it is Python-only, and its API already moved from V1 to V2 in nine months. | A (6/6) | [→](pydantic-ai.md) |
| **smolagents** | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. | B (6/6) | [→](smolagents.md) |
| **Harness SDK** | Use it when you want a working agent from one call — tuned prompt, shell/file/web tools, a code sandbox, a subagent, memory and sessions — in Python and TypeScript alike, with every default overridable. | A (6/6) | [→](harness-sdk.md) |
| **TanStack AI** | Building the AI surface of a TypeScript app — streaming chat, typed tools, media, agents across seven front-end frameworks — under one provider-agnostic typed contract with no platform layer. | B (6/6) | [→](tanstack-ai.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [AgentScope](agentscope.md) | ✅ | B (6/6) | Shipping a production multi-agent LLM service needing sandboxed tools, permissions, tracing, and human-in-the-loop. |
| [smolagents](smolagents.md) | ✅ | B (6/6) | Use it when you want a tiny, transparent code-acting agent loop from Hugging Face — not a heavy production agent OS. |
| [Harness SDK](harness-sdk.md) | ✅ | A (6/6) | A tuned default agent from one call, in Python and TypeScript; the price is model-owned control flow and a 0.x assembled layer. |

## What belongs here

Code-first libraries and frameworks you build an agent (or a team of them) with, inside your own program.
