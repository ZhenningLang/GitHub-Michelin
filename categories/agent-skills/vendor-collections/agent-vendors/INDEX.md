# agent-vendors

> Leaf of [vendor-collections](../INDEX.md). First-party bundles from AI model, coding-agent and agent-tooling companies — general-purpose skills and plugin marketplaces for their own agent (documents, design, dev process), not a guide to some other product.
> ← up to [vendor-collections](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic's official public collection of Agent Skills — self-contained SKILL.md folders (document editing, design, MCP/skill authoring, comms) installable into Claude Code, Claude.ai, or the Claude API. | A (3/5) | [→](anthropic-skills.md) |
| **Claude Plugins (Official)** | Anthropic's first-party Claude Code plugin marketplace: a curated directory of installable plugins (commands, agents, skills, MCP servers) installed by name via the native /plugin system. | A (4/5) | [→](claude-plugins-official.md) |
| **Cursor Plugins** | Cursor's official plugin marketplace repo: `/add-plugin <name>` installs skills, rules, subagents, hooks and MCP config into Cursor — 16 first-party plugins (headlined by poteto's pstack rigorous-engineering workflow) plus 80 thin connectors to vendor-hosted MCP servers. | B (3/5) | [→](cursor-plugins.md) |
| **MiniMax Skills** | Use it when you want vendor-written skills for frontend, mobile and shader dev plus MiniMax document, music and vision generation in Claude Code, Cursor, Codex or OpenCode — but it is still Beta and has not been pushed since 2026-04-18. | B (4/5) | [→](minimax-skills.md) |
| **Anthropic Knowledge Work Plugins** | Use it when you want Anthropic's official open-source plugins aimed at knowledge work (docs, comms, research) for Claude — very young. | A (4/5) | [→](knowledge-work-plugins.md) |
| **HumanLayer Skills** | HumanLayer's official six-skill bundle — visual explanation (`show-me`), PR outlining (`visual-pr`), CLAUDE.md rewriting, React prop narrowing, and two skills that turn a repeatable agent job into a scheduled GitHub Actions loop carrying an agent-memory file and an `/iterate` comment channel. | B (4/5) | [→](humanlayer-skills.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Anthropic Skills](anthropic-skills.md) | ✅ | A (3/5) | Anthropic's official public collection of Agent Skills — self-contained SKILL.md folders (document editing, design, MCP/skill authoring, comms) installable into Claude Code, Claude.ai, or the Claude API. |
| [Claude Plugins (Official)](claude-plugins-official.md) | ✅ | A (4/5) | Anthropic's first-party Claude Code plugin marketplace: a curated directory of installable plugins (commands, agents, skills, MCP servers) installed by name via the native /plugin system. |
| [Cursor Plugins](cursor-plugins.md) | ✅ | B (3/5) | Cursor-native plugins (per-role model panels, hooks, cloud-agent fan-out) plus one-click SaaS connectors; Cursor-only loader, installs track `main` with no tags, and most connectors are config pointing at vendor-hosted servers. |
| [MiniMax Skills](minimax-skills.md) | ✅ | B (4/5) | Buys first-party recipes spanning dev and media generation across four harnesses; costs a 16-skill bundle you install whole, tied to MiniMax assumptions, with a stalled upstream. |
| [Anthropic Knowledge Work Plugins](knowledge-work-plugins.md) | ✅ | A (4/5) | Use it when you want Anthropic's official open-source plugins aimed at knowledge work (docs, comms, research) for Claude — very young. |
| [HumanLayer Skills](humanlayer-skills.md) | ✅ | B (4/5) | A vendor's six opinionated dev-process skills, two of which ship runnable CI-loop machinery; Claude-only distribution, no tagged release to pin, and the loop templates default to broad agent permissions. |

## What belongs here

First-party bundles from AI model, coding-agent and agent-tooling companies — general-purpose skills and plugin marketplaces for their own agent (documents, design, dev process), not a guide to some other product.
