# harness-extensions

> Category node. Bolting capabilities onto an existing coding-agent harness — installing skill packs across agents, and giving an agent a command surface for software that only has a GUI.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Vercel Skills** | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. | D (6/6) | [→](vercel-skills.md) |
| **CLI-Anything** | Use it when you want a coding agent to drive GUI-only software through a generated CLI harness backed by the app's own engine — but it's pre-1.0 and each harness is community-maintained. | B (6/6) | [→](cli-anything.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Vercel Skills](vercel-skills.md) | ✅ | D (6/6) | A package manager for skills: install, find and update `SKILL.md` packs across ~70 agents — it distributes capability, it does not define it. |
| [CLI-Anything](cli-anything.md) | ✅ | B (6/6) | Generated CLI harnesses over each app's real engine, so an agent can drive GUI-only software — broad reach, per-harness community maintenance. |
| Curated skill packs (e.g. agent-skills entries) | 部分已收录 | — | The content side: see [`agent-skills`](../../agent-skills/INDEX.md) for the packs themselves rather than the installer. |

## What belongs here

Ways to **extend what a running agent can reach or do**: skill/extension installation and discovery, and machine surfaces for otherwise GUI-only software. Not the prompt/skill collections themselves (see `agent-skills`), not agent frameworks or runtimes (see `agent-frameworks`).
