# orchestration-and-review

> Category node. Coding-agent control planes, multi-agent runners, and review/automation wrappers.
> ← back to [coding-agents](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **CC Switch** | Use it when you juggle several AI coding CLIs (Claude Code, Codex, Gemini CLI, OpenCode) across providers and want one desktop app to rewrite their configs, MCP servers and skills — but it is a single-user GUI, useless headless or as a team gateway. | B (5/6) | [→](cc-switch.md) |
| **Claude Octopus** | A Claude Code plugin that fans a single task out to up to ~8 other AI models (Codex, Gemini, Perplexity, Ollama, OpenRouter, etc.) and uses their disagreement as a blindspot/consensus gate, all driven by `/octo:*` slash commands. | C (6/6) | [→](claude-octopus.md) |
| **oh-my-claudecode** | A multi-agent orchestration layer for Anthropic's Claude Code CLI: it stages teams of specialized agents (plan → prd → exec → verify → fix), routes each subtask to a cheaper or stronger model, and runs parallel workers under tmux — installed as a Claude Code plugin or via the `oh-my-claude-sisyphus` npm package. | B (6/6) | [→](oh-my-claudecode.md) |
| **OpenHands** | Use it when you want one self-hosted browser console to run OpenHands, Claude Code, Codex or Gemini CLI sessions on chosen machines plus scheduled agent jobs — but this repo became the beta Agent Canvas in July 2026, and the classic `openhands-ai` agent is gone. | B (6/6) | [→](openhands.md) |
| **SWE-agent** | Use it when you must reproduce published SWE-agent results by batch-running a model on repository issues in Docker sandboxes under one YAML config — but its maintainers say mini-swe-agent has superseded it, so do not start new work on it. | B (5/6) | [→](swe-agent.md) |
| **Background Agents (Open-Inspect)** | Use it when one trusted organization needs self-hosted background coding-agent sandboxes, integrations, and automation. | B (5/6) | [→](background-agents.md) |
| **SwarmForge** | Use it when you want a self-hosted role pipeline (spec→code→clean→architect→harden→QA) over your own repo, with each role in its own git worktree and commit-based handoffs — but it ships no license and no tagged releases. | D (5/6) | [→](swarm-forge.md) |
| **OpenChamber** | Use it when you run OpenCode and want a cross-device operator workspace — goal-audited sessions, up to five models per prompt with optional worktrees, a diff walkthrough, and the git/PR surface beside the chat — accepting a 12-month-old, single-maintainer app locked to one agent runtime. | B (5/6) | [→](openchamber.md) |
| **OpenResearch** | Use it when your coding agent and GPUs are already in place and the missing layer is the experiment bookkeeping — a branch-per-experiment tree, immutable commit snapshots, and runs dispatched across nine compute backends — accepting a 3.5-month-old, fast-release app whose managed-compute half is a closed service. | B (6/6) | [→](openresearch.md) |
| **herdr** | Use it when you supervise several coding agents in parallel and want the multiplexer itself to badge blocked/working/done and let agents drive each other via `herdr agent wait/prompt` — but it's 6 months old, pre-1.0, and effectively single-maintainer. | B (6/6) | [→](herdr.md) |
| **TUIOS** | Use it when you supervise several coding agents from one terminal and want a tiling window manager whose daemon tracks each agent's state and gathers every waiting approval or question into one Inbox — but it's 13 months old, pre-1.0 with protocol breaks, one maintainer, and panes default to full control. | B (6/6) | [→](tuios.md) |
| **GitHub Agentic Workflows (gh-aw)** | Use it when you want coding agents doing unattended chores on a GitHub repo — issue triage, CI-failure digging, reports, docs PRs — written as Markdown and compiled into Actions workflows where the agent runs read-only and firewalled and only declared writes are applied — but it's GitHub-only, Public Preview, and ships weekly with 11 security advisories in 7 weeks. | B (4/6) | [→](gh-aw.md) |

## What belongs here

Coding-agent control planes, multi-agent runners, and review/automation wrappers.
