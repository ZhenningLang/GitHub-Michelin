# concurrent-editing

> Category node. Parallel agents (or people) write to the same repo and their branches collide at `git merge` — semantic merge drivers and merge analysis that keep independent edits from halting on a human.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **weave** | Use it when parallel agents or branches keep halting merges on independent same-file edits and you want git to compare functions and keys instead of lines — but it's ~8 months old, pre-1.0, single-core-author, with engine verdicts still changing between releases. | B (6/6) | [→](weave.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [weave](weave.md) | ✅ | B (6/6) | An entity-level merge driver under the git you already run: independent edits stop conflicting, at the cost of trusting a 0.x semantic engine with merge outcomes. |
| Stock git line merge + rerere | not a repo | — | Zero install and the auditable baseline, but every pair of independent same-file edits is a stop for a human. |

## What belongs here

Tools that sit underneath version control to fix *what happens when concurrent writers collide*: semantic merge drivers, merge analysis and explanation, live write-coordination. Not the human's review screen (see `supervision-surfaces`), not the task/plan state the agent runs on (see `work-state`), not LLM-authored review findings (see `ai-code-review`).
