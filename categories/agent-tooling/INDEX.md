# agent-tooling

> Category node. Infrastructure for AI coding agents — task/work tracking, persistent memory, agent state, and the human review/approval surfaces where the agent hands control back to you.
> Split into sub-categories by **where in the loop you are wiring**: holding the work state while the agent runs, replaying what already happened, the surface a human reviews or steers through, or bolting new capability onto the harness.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Work State** | The agent keeps losing the plan, the backlog or the context mid-run, and you need that state somewhere on disk it can read back. | [→](work-state/INDEX.md) |
| **Session History** | You want to search, replay or cost-account for sessions that already happened, across several agents. | [→](session-history/INDEX.md) |
| **Supervision Surfaces** | A human has to look at the agent's work — review a plan or diff, approve it, steer several agents — from something other than the terminal. | [→](supervision-surfaces/INDEX.md) |
| **Harness Extensions** | You are extending what the agent can reach or install — skill-pack managers, command surfaces for GUI-only software. | [→](harness-extensions/INDEX.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [Work State](work-state/INDEX.md) | Sub-category | beads, CCPM, Ralph, Context Mode, Planning with Files — the agent keeps working because its tasks, plan and context live outside the chat window. |
| [Session History](session-history/INDEX.md) | Sub-category | AgentsView, Entire — capture and query what already ran; read-side and replay, with no say over the next step. |
| [Supervision Surfaces](supervision-surfaces/INDEX.md) | Sub-category | Plannotator, CloudCLI, Agent Orchestrator, Hermes Workspace — the human's screen: annotation gates and cockpits, at the cost of another local service to run. |
| [Harness Extensions](harness-extensions/INDEX.md) | Sub-category | Vercel Skills, CLI-Anything — widen the agent's reach (skill installers, generated CLI harnesses) rather than managing its work. |

## What belongs here

Infrastructure an AI **coding agent** uses to track work, carry state, and hand control back to you — task/issue graphs, session capture, planning / context plumbing, review-and-approval surfaces, harness extensions. Not LLM-agnostic memory libraries (see `agent-memory`), not agent runtimes (see `agent-frameworks`), not LLM-authored code review (see `ai-code-review`). Pick a sub-category by **which part of the loop** you are wiring: state while working (`work-state`), history after it (`session-history`), the human's screen (`supervision-surfaces`), or new capability (`harness-extensions`).
