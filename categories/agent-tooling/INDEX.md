# agent-tooling

> Category node. Infrastructure for AI coding agents — task/work tracking, persistent memory, agent state, and the human review/approval surfaces where the agent hands control back to you.
> Split into sub-categories by **where in the loop you are wiring**: holding the work state while the agent runs, replaying what already happened, the surface a human reviews or steers through, the live UI a human points at so the agent finds the code, bolting new capability onto the harness, or fixing what happens when concurrent writers collide at git merge.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **Work State** | The agent keeps losing the plan, the backlog or the context mid-run, and you need that state somewhere on disk it can read back. | [→](work-state/INDEX.md) |
| **Session History** | You want to search, replay or cost-account for sessions that already happened, across several agents. | [→](session-history/INDEX.md) |
| **Supervision Surfaces** | A human has to look at the agent's work — review a plan or diff, approve it, steer several agents — from something other than the terminal. | [→](supervision-surfaces/INDEX.md) |
| **UI Annotation** | A human sees the problem in the *running app's UI* and needs the agent to find the exact element and code behind it — click-to-annotate evidence, not artifact review. | [→](ui-annotation/INDEX.md) |
| **Harness Extensions** | You are extending what the agent can reach or install — skill-pack managers, command surfaces for GUI-only software. | [→](harness-extensions/INDEX.md) |
| **Concurrent Editing** | Parallel agents (or people) write to the same repo and their branches collide at `git merge` on independent same-file edits — you want the merge itself to understand functions and keys instead of lines. | [→](concurrent-editing/INDEX.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [Work State](work-state/INDEX.md) | Sub-category | beads, CCPM, Ralph, Context Mode, Planning with Files — the agent keeps working because its tasks, plan and context live outside the chat window. |
| [Session History](session-history/INDEX.md) | Sub-category | AgentsView, Entire, dsh-context — capture, query and take apart what already ran; read-side and replay, with no say over the next step. |
| [Supervision Surfaces](supervision-surfaces/INDEX.md) | Sub-category | Plannotator, CloudCLI, Agent Orchestrator, Hermes Workspace — the human's screen: annotation gates and cockpits, at the cost of another local service to run. |
| [UI Annotation](ui-annotation/INDEX.md) | Sub-category | Agentation, Vibe Annotations, Pointa, earmark, patch-mark, markupkit — the human points at the running UI and the agent gets selectors, source lines, and a structured handoff. |
| [Harness Extensions](harness-extensions/INDEX.md) | Sub-category | Vercel Skills, CLI-Anything, codex-chatgpt-web — widen the agent's reach (skill installers, generated CLI harnesses, model-backend bridges) rather than managing its work. |
| [Concurrent Editing](concurrent-editing/INDEX.md) | Sub-category | weave — a semantic merge driver under git itself, so independent same-file edits stop halting merges; the rest of the loop keeps working the way it did. |

## What belongs here

Infrastructure an AI **coding agent** uses to track work, carry state, and hand control back to you — task/issue graphs, session capture, planning / context plumbing, review-and-approval surfaces, live-UI annotation feeds, harness extensions. Not LLM-agnostic memory libraries (see `agent-memory`), not agent runtimes (see `agent-frameworks`), not LLM-authored code review (see `ai-code-review`). Pick a sub-category by **which part of the loop** you are wiring: state while working (`work-state`), history after it (`session-history`), the human's screen (`supervision-surfaces`), what the human sees in the running app (`ui-annotation`), new capability (`harness-extensions`), or what happens when concurrent writers collide at merge (`concurrent-editing`).
