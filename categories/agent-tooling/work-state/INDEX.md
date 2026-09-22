# work-state

> Category node. Keeping the agent's *what-next* outside the chat window — task and issue graphs, plans on disk, unattended loop drivers, and the in-run context that survives compaction.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **beads** | Use it when an AI agent loses task state across sessions and you want a versioned, dependency-aware task graph in the repo. | B (6/6) | [→](beads.md) |
| **CCPM** | Use it when a feature is too big for one session and you want PRD-to-GitHub-Issues specs plus parallel git-worktree agents. | B (4/6) | [→](ccpm.md) |
| **Ralph for Claude Code** | Use it when you want Claude Code to grind through a fix_plan.md checklist unattended with rate limits, a circuit breaker, and a dual-condition exit gate. | B (6/6) | [→](ralph-claude-code.md) |
| **Context Mode** | Use it when a coding agent burns context on raw tool output and you want sandboxed execution plus compaction-surviving session memory. | D (6/6) | [→](context-mode.md) |
| **Planning with Files** | Use it when a long agent run keeps losing its plan to /clear, compaction, or crashes. | B (4/6) | [→](planning-with-files.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [beads](beads.md) | ✅ | B (6/6) | A versioned, dependency-aware issue graph inside the repo — the strongest fit when the agent itself reads and writes the backlog. |
| [CCPM](ccpm.md) | ✅ | B (4/6) | PRD → GitHub Issues plus parallel worktree agents; buys issue-tracker truth and fan-out at the cost of Git-native state. |
| [Ralph for Claude Code](ralph-claude-code.md) | ✅ | B (6/6) | A guarded unattended loop over a checklist — it drives the agent, it does not store the work. |
| [Context Mode](context-mode.md) | ✅ | D (6/6) | Sandbox off the tool noise and keep memory across compaction; it manages context, not the task list. |
| [Planning with Files](planning-with-files.md) | ✅ | B (4/6) | The plan as plain files on disk — the cheapest recovery from /clear, with no graph or dependency semantics. |
| Taskmaster / GitHub Issues + gh / Linear | 未收录 | — | Other task/work-tracking backends for agents named across the pages. |

## What belongs here

State the agent needs **while the work is in progress**: task and issue graphs, plan files, checklist-driven unattended loops, and in-run context/memory plumbing. Not capturing what already happened for later replay (see `session-history`), not the screen a human watches or approves through (see `supervision-surfaces`), and not prompt/skill packs (see `agent-skills`).
