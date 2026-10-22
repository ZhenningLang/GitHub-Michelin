# human-review-gates

> Category node. Inspect understanding, annotate, or read a source-linked review artifact; not an overview of running sessions.
> ← back to [supervision-surfaces](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Sphinx** | Pause a local Git push to answer source-grounded behavior questions; bypassable learning aid, not release authorization. | C (5/6) | [→](sphinx.md) |
| **Plannotator** | Use it when a human must annotate or approve what the agent produced — a plan, a diff, an HTML artifact — and send that markup back as the agent's next instruction. | B (6/6) | [→](plannotator.md) |
| **Whiteboard** | Use it when you want your coding agent to *draw* the review — an interactive RFC over a pinned branch whose diagrams, quotes and code peeks click back to the exact lines of your checkout — but it's ~6 weeks old, v0.1.x, and the review surface is read-only. | B (5/6) | [→](whiteboard.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Sphinx](sphinx.md) | ✅ | C (5/6) | Tests your prediction of committed behavior before Git continues; adds model cost and fallible grading rather than review findings. |
| [Plannotator](plannotator.md) | ✅ | B (6/6) | A human gate inside the agent loop: annotate the plan or diff, and the decision returns through the hook protocol — at the cost of a very young, single-maintainer project. |
| [Whiteboard](whiteboard.md) | ✅ | B (5/6) | The agent authors an evidence-linked RFC over a pinned branch — every diagram node clicks to code; read-only surface, ~6 weeks old. |
| Harness built-in plan approval (Claude Code / Codex) | not a repo | — | Zero install, but no annotations, no rendered document, no record of what you approved. |

## What belongs here

Human review organized around one plan, diff, design explanation or behavior question. Sphinx checks understanding, Plannotator takes annotations and approvals, and Whiteboard presents source-linked review. For ongoing task, session or business supervision, use [agent-cockpits](../agent-cockpits/INDEX.md).
