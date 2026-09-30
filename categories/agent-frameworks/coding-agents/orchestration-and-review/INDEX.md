# orchestration-and-review

> Category node. Coding-agent control planes, multi-agent runners, and review/automation wrappers.
> ← back to [coding-agents](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CC Switch** | A cross-platform desktop All-in-One manager for Claude Code, Claude Desktop, Codex, Gemini CLI, OpenCode, OpenClaw, and Hermes Agent — built with Rust and Tauri 2. | B (5/6) | [→](cc-switch.md) |
| **Claude Octopus** | A Claude Code plugin that fans a single task out to up to ~8 other AI models (Codex, Gemini, Perplexity, Ollama, OpenRouter, etc.) and uses their disagreement as a blindspot/consensus gate, all driven by `/octo:*` slash commands. | C (6/6) | [→](claude-octopus.md) |
| **oh-my-claudecode** | A multi-agent orchestration layer for Anthropic's Claude Code CLI: it stages teams of specialized agents (plan → prd → exec → verify → fix), routes each subtask to a cheaper or stronger model, and runs parallel workers under tmux — installed as a Claude Code plugin or via the `oh-my-claude-sisyphus` npm package. | B (6/6) | [→](oh-my-claudecode.md) |
| **OpenHands** | 🙌 OpenHands: AI-Driven Development | A (6/6) | [→](openhands.md) |
| **SWE-agent** | SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding challenges. [NeurIPS 2024] | A (5/6) | [→](swe-agent.md) |
| **Background Agents (Open-Inspect)** | Use it when one trusted organization needs self-hosted background coding-agent sandboxes, integrations, and automation. | B (5/6) | [→](background-agents.md) |
| **SwarmForge** | Use it when you want a self-hosted role pipeline (spec→code→clean→architect→harden→QA) over your own repo, with each role in its own git worktree and commit-based handoffs — but it ships no license and no tagged releases. | D (5/6) | [→](swarm-forge.md) |
| **OpenChamber** | Use it when you run OpenCode and want a cross-device operator workspace — goal-audited sessions, up to five models per prompt with optional worktrees, a diff walkthrough, and the git/PR surface beside the chat — accepting a 12-month-old, single-maintainer app locked to one agent runtime. | B (5/6) | [→](openchamber.md) |
| **OpenResearch** | Use it when your coding agent and GPUs are already in place and the missing layer is the experiment bookkeeping — a branch-per-experiment tree, immutable commit snapshots, and runs dispatched across nine compute backends — accepting a 3.5-month-old, fast-release app whose managed-compute half is a closed service. | B (6/6) | [→](openresearch.md) |
| **herdr** | Use it when you supervise several coding agents in parallel and want the multiplexer itself to badge blocked/working/done and let agents drive each other via `herdr agent wait/prompt` — but it's 6 months old, pre-1.0, and effectively single-maintainer. | B (6/6) | [→](herdr.md) |
| **TUIOS** | Use it when you supervise several coding agents from one terminal and want a tiling window manager whose daemon tracks each agent's state and gathers every waiting approval or question into one Inbox — but it's 13 months old, pre-1.0 with protocol breaks, one maintainer, and panes default to full control. | B (6/6) | [→](tuios.md) |

## What belongs here

Coding-agent control planes, multi-agent runners, and review/automation wrappers.
