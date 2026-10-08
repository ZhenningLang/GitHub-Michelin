# work-state

> Category node. Keeping the agent's *what-next* outside the chat window — task and issue graphs, plans on disk, unattended loop drivers, and the in-run context that survives compaction.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **beads** | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. | B (5/6) | [→](beads.md) |
| **CCPM** | Use it when a feature is too big for one agent session and you want PRD-to-epic-to-GitHub-Issues specs plus parallel agents in git worktrees — but it requires GitHub Issues and has had no commits since 2026-03. | C (4/5) | [→](ccpm.md) |
| **Ralph for Claude Code** | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. | C (5/6) | [→](ralph-claude-code.md) |
| **Context Mode** | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. | D (6/6) | [→](context-mode.md) |
| **Planning with Files** | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. | B (5/6) | [→](planning-with-files.md) |
| **LoopX** | Use it when agent work must keep moving across days, restarts and runtimes, with durable goals, human gates, quotas and evidence governing each turn. | B (6/6) | [→](loopx.md) |
| **Token Optimizer** | Use it when a coding agent burns tokens on tool output, re-reads and compaction loss, and you want hook-layer compression, compaction checkpoints and a local dollar ledger — accepting its noncommercial license. | C (5/6) | [→](token-optimizer.md) |
| **RTK** | Your agent's context fills with passing-test spam and `git push` progress lines; RTK hooks the agent's shell commands and hands back only failures and one-line confirmations (Bash output only; Apache-2.0). | A (5/6) | [→](rtk.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [beads](beads.md) | ✅ | B (5/6) | A versioned, dependency-aware issue graph inside the repo — the strongest fit when the agent itself reads and writes the backlog. |
| [CCPM](ccpm.md) | ✅ | C (4/5) | Buys written intent and merge-safe fan-out with GitHub Issues as shared truth; costs a five-phase ceremony that is pure overhead on small work, and lock-in to GitHub. |
| [Ralph for Claude Code](ralph-claude-code.md) | ✅ | C (5/6) | A guarded unattended loop over a checklist — it drives the agent, it does not store the work. |
| [Context Mode](context-mode.md) | ✅ | D (6/6) | Sandbox off the tool noise and keep memory across compaction; it manages context, not the task list. |
| [Planning with Files](planning-with-files.md) | ✅ | B (5/6) | The plan as plain files on disk — the cheapest recovery from /clear, with no graph or dependency semantics. |
| [LoopX](loopx.md) | ✅ | B (6/6) | State kernel plus a quota-gated heartbeat driver across runtimes — the fullest loop governance here, at the cost of a fail-closed protocol and a very young, fast-moving surface. |
| [Token Optimizer](token-optimizer.md) | ✅ | C (5/6) | Hook-layer compression plus compaction checkpoints plus a local dollar ledger across ~10 coding agents; source-available noncommercial license and a 7-month-old single-maintainer surface. |
| [RTK](rtk.md) | ✅ | A (5/6) | Shell-output compression only — a single Apache-2.0 Rust binary that rewrites the agent's Bash commands and keeps exit codes; no checkpoints, no ledger beyond `rtk gain`, file reads bypass it. |
| Taskmaster / GitHub Issues + gh / Linear | 未收录 | — | Other task/work-tracking backends for agents named across the pages. |

## What belongs here

State the agent needs **while the work is in progress**: task and issue graphs, plan files, checklist-driven unattended loops, and in-run context/memory plumbing. Not capturing what already happened for later replay (see `session-history`), not the screen a human watches or approves through (see `supervision-surfaces`), and not prompt/skill packs (see `agent-skills`).
