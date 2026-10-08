# engineering-workflows

> Leaf of [personal-collections](../INDEX.md). Personal skill packs focused on coding-agent workflow, engineering process, harness setup, review, and architecture.
> ← up to [personal-collections](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **agent-scripts** | One maintainer's canonical repo for sharing a single `AGENTS.MD` and ~70 skills across Codex and Claude Code via a symlink sync script; a reference layout more than a portable pack (many skills assume his machines). | B (4/5) | [→](agent-scripts.md) |
| **antfu/skills** | Anthony Fu's personal curated agent-skill collection for the Vue/Vite/Nuxt stack (his ESLint/pnpm/Vitest/UnoCSS prefs + generated/vendored framework skills), installed via the skills CLI. | B (4/5) | [→](antfu-skills.md) |
| **claude-code-harness** | A personal Claude Code harness that installs a governed plan → work → review → release loop as a plugin, with a Go-native doctor CLI for diagnosing plugin-cache and skill drift. | B (5/6) | [→](claude-code-harness.md) |
| **Dimillian Skills** | Use it when you run OpenAI Codex for iOS/macOS work and want ready SwiftUI, Swift concurrency, simulator-debugging and App Store skills — but it is a single-author, Codex-only snapshot, quiet since 2026-03 while tracking fast-moving Apple betas. | C (4/5) | [→](dimillian-skills.md) |
| **gstack** | Garry Tan's personal Claude Code harness: 54 skills — about half role personas (CEO, eng manager, designer, QA, security officer, release engineer), half utility commands — plus a real browser the agent drives, across one plan → build → review → ship → retro sprint. | B (4/5) | [→](gstack.md) |
| **andrej-karpathy-skills** | Use it when your Claude Code or Cursor agent over-engineers, edits unrelated files and declares done unverified, and you want a ~65-line CLAUDE.md base layer against that — but it is advisory prose, a third-party distillation not authored by Karpathy. | C (3/5) | [→](karpathy-skills.md) |
| **PUA** | A high-agency persona skill pack that uses corporate-PUA/PIP rhetoric to push a coding agent to exhaust debugging approaches. | C (4/6) | [→](pua.md) |
| **Qiushi-Skill** | A methodology skill pack arming a coding agent with “seek truth from facts” plus dialectical-materialist thinking tools. | B (4/6) | [→](qiushi-skill.md) |
| **shaping-skills** | Ryan Singer's personal Claude Code skill pack bringing Shape Up shaping into a coding agent before code is written. | E (4/5) | [→](shaping-skills.md) |
| **TÂCHES CC Resources** | Use it when you live in Claude Code, keep hand-scaffolding new slash commands, subagents, hooks or MCP servers, and want meta-generator skills plus auditor subagents for that — but it is a single-maintainer, Claude-Code-only snapshot, quiet since 2026-04. | C (4/5) | [→](taches-cc-resources.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [agent-scripts](agent-scripts.md) | ✅ | B (4/5) | Best when you need to distribute your own rules and skills across many repos and agents; borrow the layout, not the personal skills. |
| [antfu/skills](antfu-skills.md) | ✅ | B (4/5) | Best when your stack matches Anthony Fu's Vue/Vite/Nuxt conventions. |
| [claude-code-harness](claude-code-harness.md) | ✅ | B (5/6) | Best when you want a governed Claude Code harness with doctor tooling. |
| [Dimillian Skills](dimillian-skills.md) | ✅ | C (4/5) | Buys Swift/SwiftUI depth most generic skill packs lack; costs a Codex-only install path and skills that can go stale between the author's pushes. |
| [gstack](gstack.md) | ✅ | B (4/5) | Best when you want one operator's whole sprint loop — role skills plus a driven browser — rather than parts to assemble. |
| [andrej-karpathy-skills](karpathy-skills.md) | ✅ | C (3/5) | Buys a tiny drop-in rule file with zero setup; costs any enforcement, and it overlaps heavily with whatever global agent rules you already run. |
| [PUA](pua.md) | ✅ | C (4/6) | Best when you deliberately want a high-pressure persona prompt, not neutral process policy. |
| [Qiushi-Skill](qiushi-skill.md) | ✅ | B (4/6) | Best when “seek truth from facts” and dialectical investigation are the desired reasoning style. |
| [shaping-skills](shaping-skills.md) | ✅ | E (4/5) | Best for Shape Up style shaping; health is weaker because of licensing/maintenance signals. |
| [TÂCHES CC Resources](taches-cc-resources.md) | ✅ | C (4/5) | Buys a factory for consistent Claude Code extensions in one plugin install; costs adopting one person's house style, with advisory-only auditors and no versioned releases to pin. |

## What belongs here

Personal collections whose primary value is improving a coding agent's engineering workflow, review loop, architecture judgment, harness behavior, or coding persona.
