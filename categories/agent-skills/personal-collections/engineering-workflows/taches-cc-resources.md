---
name: TÂCHES CC Resources
slug: taches-cc-resources
repo: https://github.com/glittercowboy/taches-cc-resources
category: engineering-workflows
tags: [claude-code, slash-commands, skills, subagents, meta-prompting, hooks]
language: TypeScript
license: MIT
maturity: no tagged releases, active, last pushed 2026-04, ~1.9k stars (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-04-01T15:10:58Z
  default_branch: main
  default_branch_sha: 1757615b99ab789a72ff2d02e9f6112af2a15c04
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:49:03Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 174
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 313
        last_commit_age_days: 174
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# TÂCHES CC Resources

A personal, opinionated bundle of Claude Code extensions from TÂCHES (glittercowboy): ~27 slash commands, 9 "skills" (mostly meta-generators that build new commands/skills/subagents/hooks/MCP servers), 3 auditor subagents, and example hooks — installable as one marketplace plugin.

![taches-cc-resources — health radar](../../../../assets/health/taches-cc-resources.svg)

## When to use

You're a solo dev or small-team builder who lives in Claude Code and keeps re-writing the same boilerplate to scaffold *new* extensions: every time you want a slash command, a subagent, a hook, or an MCP server, you hand-craft the prompt structure from scratch and the results come out inconsistent. You also want a couple of reusable thinking frames (`/consider:pareto`, `/consider:first-principles`), a disciplined `/debug` flow, and todo helpers, without assembling them yourself one file at a time.

You reach for TÂCHES CC Resources because it's a curated, batteries-included starter kit: install the marketplace plugin (`glittercowboy/taches-cc-resources`) and you get meta-skills like *Create Agent Skills*, *Create Slash Commands*, *Create Subagents*, *Create Hooks*, and *Create MCP Servers* that walk Claude through producing well-formed extensions, plus three auditor subagents (skill-auditor, slash-command-auditor, subagent-auditor) to sanity-check what you generate. It's most useful as a "factory for your own Claude Code customizations" rather than a domain skill set — you adopt one person's house style for authoring extensions and iterate from there.

## When NOT to use

- **You already run a curated command/skill stack.** Many entries here are meta-generators ("Create Slash Commands", "Create Subagents", "Create Hooks") and thinking frames that overlap with whatever scaffolding discipline you already have; layering both invites duplicate routes and conflicting house styles — pick one source of truth.
- **You're not on Claude Code.** The pack targets Claude Code's native loaders (`~/.claude/commands`, `~/.claude/skills`, `.claude-plugin` marketplace). There's no documented Codex/Cursor/OpenCode/Droid manifest, so on another harness the markdown won't auto-fire. [推断]
- **You want enforced behavior, not suggestions.** These are prompt/markdown extensions the agent loads on demand; "auditors" and "debug protocols" are advisory prompts, not hard gates — the agent can still skip or deviate. [推断]
- **You need a maintained, versioned dependency.** It's a single-maintainer personal collection with no tagged releases and a last push in 2026-04; treat it as a snapshot to fork and own, not a stable upstream you track.
- **You want runtime domain skills (DB, frontend, security).** This is mostly tooling-about-tooling (scaffolding extensions, meta-prompts); it doesn't ship deep per-domain expertise the way some sibling collections do.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [antfu/skills](antfu-skills.md) | ✅ | Choose antfu/skills when you need concrete authoring/dev skills rather than extension generators. | Another personal Claude Code skill collection; centers concrete authoring/dev skills rather than meta-generators for building new extensions. |
| [Dimillian/Skills](dimillian-skills.md) | ✅ | Choose Dimillian/Skills when a specific stack/workflow personal set fits better. | Personal skill set skewed to a specific stack/workflow; TÂCHES is broader-but-shallower, focused on scaffolding Claude Code extensions themselves. |
| [wshobson/agents](../../subagent-collections/wshobson-agents.md) | ✅ | Choose wshobson/agents when you need ready-made domain subagent breadth. | Large library of ready-made domain subagents; TÂCHES ships only 3 auditor subagents plus generators to *make* your own. Pick wshobson for breadth of personas, TÂCHES to author extensions. |
| [awesome-claude-code-subagents](../../subagent-collections/awesome-claude-code-subagents.md) | ✅ | Choose awesome-claude-code-subagents when you want a consumption-oriented subagent catalog. | Big curated subagent catalog (consumption-oriented); TÂCHES is a small personal mixed bundle (commands + skills + auditors), generation-oriented. |
| [shaping-skills](shaping-skills.md) | ✅ | Choose shaping-skills when the need is a single methodology-shaped skill pack. | Methodology-shaped skill pack; TÂCHES is less a single methodology and more a grab-bag of authoring tools and thinking frames. |
| Anthropic's official Claude Code skills / built-in commands | 未收录 | Choose official Claude Code skills when platform-native behavior matters more. | The platform's native ecosystem; TÂCHES is a third-party personal bundle layered on top and can duplicate or conflict with native commands. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance** — last pushed 2026-04, not archived (as of 2026-06): a couple of months quiet, no tagged releases. Reads as a recently-touched personal collection rather than abandoned, but cadence is low and there's no semver to pin.
- **Governance & bus factor** — single-maintainer personal repo (`User`-owned, glittercowboy/TÂCHES), ~1.9k stars. One author's house style for authoring extensions; no team backstop — treat as a snapshot to fork and own.
- **Age & Lindy** — created 2025-11, ~0.5 years old as of 2026-06: young, Lindy-unproven. Too new to have weathered Claude Code's loader/marketplace changes — adopt for the scaffolding, not for stability.
- **Risk flags** — MIT-licensed (as of 2026-06), so reuse is clear, but "Setup Ralph" wires an autonomous coding loop whose safety envelope is undocumented — review before running unattended. Enforcement is advisory only.

## Caveats (unverified)

- [未验证] GitHub metadata (license MIT, primary language TypeScript ~57% / Shell ~36% / Python ~6%, not archived, no tagged release, last pushed 2026-04-01) read on 2026-06-26 — re-verify before relying on specifics.
- [未验证] Star count (~1,952 on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] Inventory counts (27 commands, 9 skills, 3 subagents, hooks present) come from the README/repo listing and may drift as the author edits; re-count the `commands/`, `skills/`, `agents/` dirs before depending on a specific item.
- [推断] Activation is Claude Code-specific (native skill/command/marketplace loaders); cross-harness use isn't documented and would require manual porting.
- [推断] Because behavior lives in prompt/markdown, the auditor subagents and debug protocols are advisory — they shape but don't enforce agent behavior.
- [未验证] "Setup Ralph" appears to wire an autonomous coding loop; its safety envelope and side effects aren't documented here — review before running it unattended.
