# session-history

> Category node. What the agents already did, captured so you can query it later — cross-agent session search and token/cost analytics, and sessions checkpointed into git.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **AgentsView** | Use it when you run several coding agents and want local-first cross-agent session search and token/cost analytics — but it's months-old and pre-1.0, expect churn. | B (6/6) | [→](agentsview.md) |
| **Entire** | Use it when you want AI agent sessions captured as Git checkpoints alongside commits, searchable and rewindable. | B (6/6) | [→](entire-cli.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [AgentsView](agentsview.md) | ✅ | B (6/6) | Index every agent's local session logs into one searchable, cost-aware view — read-side analytics over transcripts. |
| [Entire](entire-cli.md) | ✅ | B (6/6) | Pair each session with Git checkpoints next to your commits — replay and rewind the work, not just read the transcript. |
| grep over `~/.claude` / session dirs | not a repo | — | Not a project but a technique: zero-dependency and fully local, yet no UI, no token/cost math, no cross-agent normalization. |

## What belongs here

Recording and **retrospection over finished or running sessions**: capture, search, cost and usage analysis. Not the state an agent needs to keep working (see `work-state`), and not a live surface where you approve or steer the agent mid-turn (see `supervision-surfaces`).
