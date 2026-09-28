# harness-extensions

> Category node. Bolting capabilities onto an existing coding-agent harness — installing skill packs across agents, giving an agent a command surface for software that only has a GUI, and bridging extra model backends into the harness.
> ← back to [agent-tooling](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Vercel Skills** | Use it when you want an npm-style CLI to install, find, and update SKILL.md packs across many coding agents. | A (6/6) | [→](vercel-skills.md) |
| **CLI-Anything** | Use it when you want a coding agent to drive GUI-only software through a generated CLI harness backed by the app's own engine — but it's pre-1.0 and each harness is community-maintained. | B (6/6) | [→](cli-anything.md) |
| **codex-chatgpt-web** | Use it when Codex quota runs dry while your paid ChatGPT web subscription sits idle, and you want Codex turns billed to the web plan's separate allowance — through an unofficial browser bridge upstream can break at any time. | C (5/6) | [→](codex-chatgpt-web.md) |
| **HEY CLI** | Use it when your mail lives on HEY and you want it in your terminal and your coding agent's hands — a first-party CLI/TUI plus an embedded agent skill and an MCP server, bound to a paid 37signals account. | B (6/6) | [→](hey-cli.md) |
| **SkillsGate** | Use it when your skills sprawl across several agents' hidden folders and you want a desktop GUI over them — one canonical copy symlinked per agent, skills.sh catalog, SSH push — but it's single-maintainer, global-only, and its lock file clashes with `npx skills`. | B (6/6) | [→](skillsgate.md) |
| **TanStack Intent** | Use it when you maintain an npm library and want agent instructions (`SKILL.md`) shipped inside the package, matched to the installed version and flagged when stale — npm/JS only, v0.x, and it delivers guidance without guaranteeing the agent follows it. | B (6/6) | [→](tanstack-intent.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Vercel Skills](vercel-skills.md) | ✅ | A (6/6) | A package manager for skills: install, find and update `SKILL.md` packs across ~70 agents — it distributes capability, it does not define it. |
| [CLI-Anything](cli-anything.md) | ✅ | B (6/6) | Generated CLI harnesses over each app's real engine, so an agent can drive GUI-only software — broad reach, per-harness community maintenance. |
| [codex-chatgpt-web](codex-chatgpt-web.md) | ✅ | C (5/6) | Bridges the ChatGPT web session (Plus/Pro, incl. web-only tiers) into Codex's model picker on the web plan's allowance — pure quota arbitrage, hostage to ChatGPT's DOM and ToS. |
| [HEY CLI](hey-cli.md) | ✅ | B (6/6) | The vendor's own command + skill + MCP surface for HEY mail/calendar — first-party and API-backed, but HEY-only: no HEY account, no use case. |
| [SkillsGate](skillsgate.md) | ✅ | B (6/6) | A desktop GUI over Vercel Skills' catalog and folder layout: per-agent toggles, an editor and SSH push to servers — but global installs only, and a v1 lock file that fights the CLI's v3. |
| [TanStack Intent](tanstack-intent.md) | ✅ | B (6/6) | The maintainer's side of skills: author, validate and ship `SKILL.md` inside your npm package so users' agents load the version they installed — npm-only, and a delivery channel rather than enforcement. |
| Curated skill packs (e.g. agent-skills entries) | 部分已收录 | — | The content side: see [`agent-skills`](../../agent-skills/INDEX.md) for the packs themselves rather than the installer. |

## What belongs here

Ways to **extend what a running agent can reach or do**: skill/extension installation and discovery, machine surfaces for otherwise GUI-only software, and model-backend bridges that attach new providers or tiers to the harness. Not the prompt/skill collections themselves (see `agent-skills`), not agent frameworks or runtimes (see `agent-frameworks`).
