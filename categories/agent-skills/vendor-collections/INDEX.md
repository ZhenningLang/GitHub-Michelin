# vendor-collections

> Leaf of [agent-skills](../INDEX.md). Official / vendor-published first-party skill & plugin bundles.
> ← up to [agent-skills](../INDEX.md) · root [route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **Anthropic Skills** | Anthropic's official public collection of Agent Skills — self-contained SKILL.md folders (document editing, design, MCP/skill authoring, comms) installable into Claude Code, Claude.ai, or the Claude API. | A (3/5) | [→](anthropic-skills.md) |
| **Agent Plugins for AWS** | AWS Labs' official collection of nine agent plugins (serverless, Amplify, SageMaker, migration, databases, deploy/cost-estimate, etc.) that teach Claude Code / Cursor / Codex to architect, deploy, and operate on AWS via marketplace-installed, trigger-phrase skills wired to AWS MCP servers. | B (5/6) | [→](aws-agent-plugins.md) |
| **Claude Plugins (Official)** | Anthropic's first-party Claude Code plugin marketplace: a curated directory of installable plugins (commands, agents, skills, MCP servers) installed by name via the native /plugin system. | A (4/5) | [→](claude-plugins-official.md) |
| **MiniMax Skills** | MiniMax's official ~16-skill Agent Skills bundle (frontend/mobile/shader dev plus pdf/docx/xlsx/pptx, music & multimodal generation), installable into Claude Code and other coding agents via plugin marketplace. | B (4/5) | [→](minimax-skills.md) |
| **Anthropic Knowledge Work Plugins** | Use it when you want Anthropic's official open-source plugins aimed at knowledge work (docs, comms, research) for Claude — very young. | B (4/5) | [→](knowledge-work-plugins.md) |
| **Remotion Agent Skills** | Remotion's official 12-skill bundle that teaches a coding agent (Claude Code, Codex, Cursor, Kimi Code) to write correct Remotion React video code — installable with `npx skills add remotion-dev/skills`, version-locked to the framework. | C (4/5) | [→](remotion-skills.md) |
| **HumanLayer Skills** | HumanLayer's official six-skill bundle — visual explanation (`show-me`), PR outlining (`visual-pr`), CLAUDE.md rewriting, React prop narrowing, and two skills that turn a repeatable agent job into a scheduled GitHub Actions loop carrying an agent-memory file and an `/iterate` comment channel. | B (4/5) | [→](humanlayer-skills.md) |
| **Android Skills** | Google's official 24-skill pack for the Android jobs models still fail (edge-to-edge, R8, Navigation 3, Play policy) — installed with the Android CLI, not `npx skills add`. | B (5/6) | [→](android-skills.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Anthropic Skills](anthropic-skills.md) | ✅ | A (3/5) | Anthropic's official public collection of Agent Skills — self-contained SKILL.md folders (document editing, design, MCP/skill authoring, comms) installable into Claude Code, Claude.ai, or the Claude API. |
| [Agent Plugins for AWS](aws-agent-plugins.md) | ✅ | B (5/6) | AWS Labs' official collection of nine agent plugins (serverless, Amplify, SageMaker, migration, databases, deploy/cost-estimate, etc.) that teach Claude Code / Cursor / Codex to architect, deploy, and operate on AWS via marketplace-installed, trigger-phrase skills wired to AWS MCP servers. |
| [Claude Plugins (Official)](claude-plugins-official.md) | ✅ | A (4/5) | Anthropic's first-party Claude Code plugin marketplace: a curated directory of installable plugins (commands, agents, skills, MCP servers) installed by name via the native /plugin system. |
| [MiniMax Skills](minimax-skills.md) | ✅ | B (4/5) | MiniMax's official ~16-skill Agent Skills bundle (frontend/mobile/shader dev plus pdf/docx/xlsx/pptx, music & multimodal generation), installable into Claude Code and other coding agents via plugin marketplace. |
| [Anthropic Knowledge Work Plugins](knowledge-work-plugins.md) | ✅ | B (4/5) | Use it when you want Anthropic's official open-source plugins aimed at knowledge work (docs, comms, research) for Claude — very young. |
| [Remotion Agent Skills](remotion-skills.md) | ✅ | C (4/5) | Vendor-canonical, version-locked guidance for agents authoring React video; useless if you are not on a skill-loading harness or not using Remotion, and its content license is undeclared. |
| [HumanLayer Skills](humanlayer-skills.md) | ✅ | B (4/5) | A vendor's six opinionated dev-process skills, two of which ship runnable CI-loop machinery; Claude-only distribution, no tagged release to pin, and the loop templates default to broad agent permissions. |
| [Android Skills](android-skills.md) | ✅ | B (5/6) | Google's official Android playbooks for the jobs models still fail; Android-only, CLI-installed, contributions closed. |

## What belongs here

**Official or vendor-published** skill/plugin collections (Anthropic, AWS, MiniMax, …) — first-party bundles.
