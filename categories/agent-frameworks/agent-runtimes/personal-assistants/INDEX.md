# personal-assistants

> Category node. Packaged assistants aimed at one person: install it, connect it to your accounts/model, and talk to it.
> ← back to [agent-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenClaw** | Use it when you want a personal AI assistant that runs on your own devices and answers you across 20+ messaging channels — but it's extremely young with no Lindy track record. | B (4/6) | [→](openclaw.md) |
| **Hermes Agent** | Use it when you want a self-improving AI agent with a learning loop that creates skills from experience and runs on a $5 VPS — but it's under a year old and the learning-loop stability is unproven. | B (5/6) | [→](hermes-agent.md) |
| **OpenHuman** | Use it when you want a local-first personal assistant that ingests your mail, calendar and repos into Markdown memory on a 20-minute loop and can be forced offline in its Rust core — but it's 7 months old, one author holds most commits, and it's GPL-3.0-only. | B (6/6) | [→](openhuman.md) |
| **Octop** | Use it when a household or small team needs isolated agents on Feishu/WeCom with chats on your disk — not when you want finished office skills, and the LangGraph core is still a private wheel. | B (5/6) | [→](octop.md) |
| **OpenMuse** | Use it when you want a self-hosted personal agent with a working computer — persistent browser you can take over, sandboxed Linux terminal, durable approval-gated tasks — but it refuses to start without a CopilotKit cloud key, and the alpha is 12 days old with zero releases. | B (4/6) | [→](openmuse.md) |
| **OpenWorker** | Use it when you want a desktop AI coworker that finishes real tasks with your own model key behind approval gates and a per-call audit trail — but the command sandbox is opt-in, one-click connectors use a closed OAuth broker, and it is a 71-day-old beta. | B (6/6) | [→](openworker.md) |
| **Raven** | Use it when you want one surface that splits a big brief into a task graph and hands the nodes to built-in research/code/design/on-call agents or to Claude Code and Codex — but it's a 4-month-old pre-alpha, the sandbox is off by default, and DAG nodes can bypass it (#796). | B (6/6) | [→](raven.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenClaw](openclaw.md) | ✅ | B (4/6) | Use it when you want a personal AI assistant that runs on your own devices and answers you across 20+ messaging channels — but it's extremely young with no Lindy track record. |
| [Hermes Agent](hermes-agent.md) | ✅ | B (5/6) | Use it when you want a self-improving AI agent with a learning loop that creates skills from experience and runs on a $5 VPS — but it's under a year old and the learning-loop stability is unproven. |
| [OpenHuman](openhuman.md) | ✅ | B (6/6) | Local-first desktop assistant that buys context by ingesting your accounts on a 20-minute loop instead of waiting for a learning loop; GPL-3.0-only, heavy build, vendor account by default. |
| [Octop](octop.md) | ✅ | B (5/6) | TencentCloud's self-hosted multi-user assistant for Feishu/WeCom on one Python process; two months old, and the agent runtime is a PyPI wheel whose GitHub repo 404s. |
| [OpenMuse](openmuse.md) | ✅ | B (4/6) | CopilotKit's MIT personal-agent app with a persistent browser and bounded Linux computer; buys that working surface at the price of a mandatory Intelligence (hosted) project key. |
| [OpenWorker](openworker.md) | ✅ | B (6/6) | Desktop cowork app by Andrew Ng's team: human-only floors, standing-approval ladder and audit provenance, ~15 model providers signed-out; sandbox off by default, two-person core, weak issue response. |
| [Raven](raven.md) | ✅ | B (6/6) | EverMind's host agent (nanobot fork) that orchestrates its own specialists and 13 third-party agents as a DAG, with EverOS memory; buys breadth at the price of pre-alpha churn and a sandbox you must enable and verify. |

## What belongs here

Packaged assistants aimed at one person: install it, connect it to your accounts/model, and talk to it.
