# agent-multiplexers

> Category node. Terminals and multiplexers built for supervising several coding agents at once — they track which agent is blocked, working or done and pull you to the one waiting on you.
> ← back to [coding-agents](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **herdr** | Use it when you supervise several coding agents in parallel and want the multiplexer itself to badge blocked/working/done and let agents drive each other via `herdr agent wait/prompt` — but it's 6 months old, pre-1.0, and effectively single-maintainer. | B (6/6) | [→](herdr.md) |
| **TUIOS** | Use it when you supervise several coding agents from one terminal and want a tiling window manager whose daemon tracks each agent's state and gathers every waiting approval or question into one Inbox — but it's 13 months old, pre-1.0 with protocol breaks, one maintainer, and panes default to full control. | B (6/6) | [→](tuios.md) |
| **cmux** | Use it when you run several CLI coding agents side by side on a Mac and want the terminal app itself to ring the pane whose agent is waiting, with branch/PR/latest message in a vertical sidebar and a browser pane the agent can drive — but it's macOS-only, 8 months old, ships telemetry on by default, and its server side is BUSL-1.1. | D (5/6) | [→](cmux.md) |

## What belongs here

Terminal apps, multiplexers and tiling window managers whose main job is hosting several CLI coding agents side by side and surfacing each agent's state (waiting for approval, working, done) so one person can supervise them. Not the coding agents themselves (see `terminal-agents`); not control planes that dispatch, schedule or review agent work (see `orchestration-and-review`); not general-purpose terminal multiplexers with no agent awareness (see `terminal-ui`).
