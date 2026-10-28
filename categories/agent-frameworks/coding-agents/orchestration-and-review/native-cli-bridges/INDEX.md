# native-cli-bridges

> Category node. In-conversation delegation and cross-model review through installed native agent CLIs.
> ← back to [orchestration-and-review](../INDEX.md) · root: [category route](../../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **AutoSwarm** | Delegate from the current conversation to installed native agent CLIs; keep credentials and sessions, but supply workspace isolation and acceptance yourself. | B (6/6) | [→](autoswarm.md) |
| **Claude Octopus** | A Claude Code plugin that fans a single task out to up to ~8 other AI models (Codex, Gemini, Perplexity, Ollama, OpenRouter, etc.) and uses their disagreement as a blindspot/consensus gate, all driven by `/octo:*` slash commands. | C (6/6) | [→](claude-octopus.md) |
| **Codex plugin for Claude Code** | Use it when you live in Claude Code, already have a Codex login, and want OpenAI's Codex to review your diff or take over a stuck task without leaving the session — but it is one vendor, write-by-default on rescue, leaks broker processes, and nothing has been merged since 2026-07. | B (5/6) | [→](codex-plugin-cc.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [AutoSwarm](autoswarm.md) | Indexed | B (6/6) | Lightweight native-call and approval bridge; no task board, worktree allocator or automatic acceptance. |

## What belongs here

Bridges that keep delegation or cross-model review inside an existing agent conversation while dispatching work through installed native agent CLIs. Task pipelines, container workspace provisioning, operator consoles and CLI configuration managers remain in the [parent category](../INDEX.md).
