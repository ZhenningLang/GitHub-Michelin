# agent-tooling

> Category node. Infrastructure for AI coding agents — task/work tracking, persistent memory, agent state, and the human review/approval surfaces where the agent hands control back to you.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **beads** | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. | B (6/6) | [→](beads.md) |
| **CCPM** | Use it when a feature is too big for one session and you want PRD-to-GitHub-Issues specs plus parallel git-worktree agents. | B (4/6) | [→](ccpm.md) |
| **Entire** | Use it when you want AI agent sessions captured as Git checkpoints alongside commits, searchable and rewindable. | B (5/6) | [→](entire-cli.md) |
| **Ralph for Claude Code** | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. | B (6/6) | [→](ralph-claude-code.md) |
| **Context Mode** | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. | D (6/6) | [→](context-mode.md) |
| **Planning with Files** | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. | B (4/6) | [→](planning-with-files.md) |
| **Vercel Skills** | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. | D (6/6) | [→](vercel-skills.md) |
| **AgentsView** | Use it when you run several coding agents and want local-first cross-agent session search and token/cost analytics — but it's months-old and pre-1.0, expect churn. | B (6/6) | [→](agentsview.md) |
| **Agent Orchestrator** | Use it when you supervise several parallel coding agents on real branches and want a desktop control plane that isolates each in a git worktree and auto-routes CI/review/conflict feedback — but it's ~4.5 months old, pre-1.0, single-User-owned, with a loopback-no-auth daemon. | B (5/6) | [→](agent-orchestrator.md) |
| **CLI-Anything** | Use it when you want a coding agent to drive GUI-only software through a generated CLI harness backed by the app's own engine — but it's pre-1.0 and each harness is community-maintained. | B (6/6) | [→](cli-anything.md) |
| **Hermes Workspace** | Use it when you run Nous's hermes-agent and want its state as a web console — chat, memory, skills, terminal, tmux swarm dispatch, phone via PWA/Tailscale — but its enhanced panes are keyed to the Hermes gateway/dashboard APIs and it's ~6 months old. | B (5/6) | [→](hermes-workspace.md) |
| **CloudCLI (Claude Code UI)** | Use it when your brain is Claude Code / Codex / Cursor CLI and you want a browser/mobile cockpit for those sessions (files, terminal, git) — but it's AGPL-3.0-or-later and single-operator shaped. | C (5/6) | [→](claudecodeui.md) |
| **Plannotator** | Use it when a human must annotate or approve what the agent produced — a plan, a diff, an HTML artifact — and send that markup back as the agent's next instruction. | B (6/6) | [→](plannotator.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [beads](beads.md) | ✅ | B (6/6) | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. |
| [CCPM](ccpm.md) | ✅ | B (4/6) | Use it when a feature is too big for one session and you want PRD-to-GitHub-Issues specs plus parallel git-worktree agents. |
| [Entire](entire-cli.md) | ✅ | B (5/6) | Use it when you want AI agent sessions captured as Git checkpoints alongside commits, searchable and rewindable. |
| [Ralph for Claude Code](ralph-claude-code.md) | ✅ | B (6/6) | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. |
| [Context Mode](context-mode.md) | ✅ | D (6/6) | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. |
| [Planning with Files](planning-with-files.md) | ✅ | B (4/6) | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. |
| [Vercel Skills](vercel-skills.md) | ✅ | D (6/6) | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. |
| [AgentsView](agentsview.md) | ✅ | B (6/6) | Use it when you run several coding agents and want local-first cross-agent session search and token/cost analytics — but it's months-old and pre-1.0, expect churn. |
| [Agent Orchestrator](agent-orchestrator.md) | ✅ | B (5/6) | Use it when you supervise several parallel coding agents on real branches and want a desktop control plane that isolates each in a git worktree and auto-routes CI/review/conflict feedback — but it's ~4.5 months old, pre-1.0, single-User-owned, with a loopback-no-auth daemon. |
| [CLI-Anything](cli-anything.md) | ✅ | B (6/6) | Generated CLI harnesses that drive the app's real backend — broad reach across GUI software, but pre-1.0 and community-maintained. |
| [Hermes Workspace](hermes-workspace.md) | ✅ | B (5/6) | Use it when you run Nous's hermes-agent and want its state as a web console — chat, memory, skills, terminal, tmux swarm dispatch, phone via PWA/Tailscale — but its enhanced panes are keyed to the Hermes gateway/dashboard APIs and it's ~6 months old. |
| [CloudCLI (Claude Code UI)](claudecodeui.md) | ✅ | C (5/6) | Use it when your brain is Claude Code / Codex / Cursor CLI and you want a browser/mobile cockpit for those sessions (files, terminal, git) — but it's AGPL-3.0-or-later and single-operator shaped. |
| [Plannotator](plannotator.md) | ✅ | B (6/6) | Choose it when the agent must wait on a human's line-level annotations before continuing — plan review in the browser, feedback returned through the hook protocol; the cost is a 9-month-old pre-1.0 single-maintainer project. |
| Taskmaster / GitHub Issues + gh / Linear | 未收录 | — | Other task/work-tracking backends for agents named across the pages. |

## What belongs here

Infrastructure an AI **coding agent** uses to track work, carry state, and hand control back to you — task/issue graphs, session capture, planning / context plumbing, review-and-approval surfaces. Not LLM-agnostic memory libraries (see `agent-memory`), not agent runtimes (see `agent-frameworks`), not LLM-authored code review (see `ai-code-review`).
