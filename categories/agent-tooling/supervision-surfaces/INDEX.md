# supervision-surfaces

> Category node. The screen a human looks at: review and approval gates over what the agent produced, browser/mobile cockpits for its sessions, and desktop control planes over several agents at once.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Agent Orchestrator** | Use it when you supervise several parallel coding agents on real branches and want a desktop control plane that isolates each in a git worktree and auto-routes CI/review/conflict feedback — but it's ~4.5 months old, pre-1.0, single-User-owned, with a loopback-no-auth daemon. | B (6/6) | [→](agent-orchestrator.md) |
| **Hermes Workspace** | Use it when you run Nous's hermes-agent and want its state as a web console — chat, memory, skills, terminal, tmux swarm dispatch, phone via PWA/Tailscale — but its enhanced panes are keyed to the Hermes gateway/dashboard APIs and it's ~6 months old. | B (5/6) | [→](hermes-workspace.md) |
| **CloudCLI (Claude Code UI)** | Use it when your brain is Claude Code / Codex / Cursor CLI and you want a browser/mobile cockpit for those sessions (files, terminal, git) — but it's AGPL-3.0-or-later and single-operator shaped. | B (6/6) | [→](claudecodeui.md) |
| **Plannotator** | Use it when a human must annotate or approve what the agent produced — a plan, a diff, an HTML artifact — and send that markup back as the agent's next instruction. | B (6/6) | [→](plannotator.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Agent Orchestrator](agent-orchestrator.md) | ✅ | B (6/6) | A desktop control plane that fans work out to many agents in worktrees and routes CI/review feedback back — breadth over one artifact. |
| [Hermes Workspace](hermes-workspace.md) | ✅ | B (5/6) | Vendor-shaped web console for one agent's whole state; the richest view, the most coupled to its host's APIs. |
| [CloudCLI (Claude Code UI)](claudecodeui.md) | ✅ | B (6/6) | Operate sessions from a browser or phone (files, terminal, git) — steering, not review. |
| [Plannotator](plannotator.md) | ✅ | B (6/6) | A human gate inside the agent loop: annotate the plan or diff, and the decision returns through the hook protocol — at the cost of a very young, single-maintainer project. |
| Harness built-in plan approval (Claude Code / Codex) | not a repo | — | Zero install, but no annotations, no rendered document, no record of what you approved. |

## What belongs here

Interfaces whose primary job is the **human's view and decision** over agent work: review/approval gates, session cockpits, multi-agent control planes. Not LLM-authored review findings (see `ai-code-review`), not the task/plan state the agent runs on (see `work-state`), and not post-hoc transcript analytics (see `session-history`).
