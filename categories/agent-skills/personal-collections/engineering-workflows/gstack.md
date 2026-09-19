---
name: gstack
slug: gstack
repo: https://github.com/garrytan/gstack
category: engineering-workflows
tags: [claude-code, slash-commands, subagent-personas, sdlc-workflow, harness-config]
language: TypeScript
license: MIT
maturity: no tagged release, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-25T16:42:45Z
  default_branch: main
  default_branch_sha: 11de390be1be6849eb9a15f91ff4922dd16c589a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T10:45:43Z
  overall: B
  overall_score: 3.0
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 8
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 114
        last_commit_age_days: 8
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 76
        top1_share: 0.769
        top3_share: 0.797
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
    adoption: { reason: no_package_structural }
---

# gstack

Garry Tan's personal Claude Code setup: ~23 opinionated slash-command skills that role-play a virtual engineering team (CEO review, designer, eng-manager, release manager, doc engineer, QA, security officer) and drive a plan → build → review → ship → retro loop.

![gstack — health radar](../../../../assets/health/gstack.svg)

## When to use

You're a solo founder or small-team developer who lives in Claude Code, and you keep doing the "team" work in your own head: deciding whether a feature is even worth building, locking the architecture before coding, doing a design pass, QA-ing your own work, then writing release notes and shipping. You want that whole assembly line as named, repeatable steps instead of ad-hoc prompts you retype every session. You clone gstack into `~/.claude/skills/`, run its `./setup`, and now you have slash commands like `/office-hours` (product interrogation), `/plan-eng-review` (architecture lock), `/review`, `/qa`, `/cso` (security audit), `/ship`, `/document-release`, and `/retro` — each a persona that interrogates the work from one role's angle.

You reach for it when you'd rather adopt one person's battle-tested, end-to-end harness wholesale than assemble your own skill stack command-by-command. It's explicitly "how Garry Tan does it" — an opinionated software-factory workflow he uses daily — so the value is the *taste and sequencing* baked into those 23 commands, not a generic toolbox. Install once; the commands then activate through Claude Code's native skill-loading, and `setup` can also fan the same commands out to other detected agents (Codex CLI, OpenCode, Cursor, Droid, and others) [未验证].

## When NOT to use

- **You already run a curated command/skill system you trust.** gstack is prescriptive and personality-driven (a CEO that second-guesses your roadmap, an eng-manager that locks architecture). Layering it over an existing workflow stack creates competing slash commands and double-routing — pick one source of truth.
- **You want a runtime/library/CLI to import.** The deliverable is a bag of prompt-defined skills, not an API or service. Outside a supporting agent harness, the markdown does nothing.
- **You're off the supported harnesses.** It activates via Claude Code's skill loader (and claims auto-detection for ~10 other agents). On a bespoke or unsupported agent there's no loader to fire the commands.
- **You don't want the install footprint.** Setup clones into `~/.claude/skills/`, symlinks per-skill dirs, can write `.gstack/` state, and a "browse daemon" auto-starts; team mode commits `.claude/` + `CLAUDE.md` into your repo. That's heavier than dropping in a few `.md` files.
- **Single-maintainer, one person's taste.** This is one founder's personal config, no tagged releases; commands and their behavior can shift with any push, and the workflow encodes his preferences, not a community standard.
- **Advisory, not enforced.** "Reviews" and "locks" are prompt-level instructions the agent can still ignore; nothing here is a hard gate in CI.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Superpowers](../../../agent-dev-methodology/coding-agent-harnesses/superpowers.md) | ✅ | Choose Superpowers when you need a cross-harness SDLC skill library rather than one founder's role loop. | Composable SDLC skills library (brainstorm → plan → TDD → verify) shipped as a cross-harness plugin. More TDD/test-first discipline and a marketplace install; gstack is one founder's *role-based* command set (CEO/designer/QA personas) tuned to his daily factory rather than a generic methodology. |
| [antfu/skills](antfu-skills.md) | ✅ | Choose antfu/skills when you want another personal Claude Code skill collection with different workflow assumptions. | Another personal Claude Code skill collection; compare on which workflow each author bakes in and how much it assumes about your setup. |
| [Dimillian/Skills](dimillian-skills.md) | ✅ | Choose Dimillian/Skills when a personal collection's author taste and command routing fit better. | Personal skill collection; pick by author taste and how their commands route. |
| [wshobson/agents](../../subagent-collections/wshobson-agents.md) | ✅ | Choose wshobson/agents when you need a broad subagent/persona catalog. | Large subagent/persona collection; broader catalog of agents vs. gstack's tighter founder-opinionated factory loop. |
| Building your own commands from scratch | 未收录 | Choose custom commands when maximum fit matters more than maintenance burden. | Maximum fit, zero lock-in, but you author and maintain every persona and the sequencing yourself. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance (2026-06):** active — last pushed 2026-06, but with ~743 open issues and **no tagged releases**, so there's no version to pin and you track a moving `main`. High activity, but the open-issue backlog is large for a personal config.
- **Governance & bus factor:** this is the standout flag — a `User`-owned personal repo (Garry Tan) carrying ~117k stars and ~743 open issues, with one maintainer and no foundation/team behind it. That is an extreme bus-factor concentration: enormous adoption resting on one person's taste and availability. The workflow encodes his preferences, not a community standard.
- **Age & Lindy verdict:** created 2026-03, only ~3 months old as of 2026-06 — very young and intensely hyped (the star count outruns the project's history). Hype ≠ Lindy: there's no longevity track record, and breaking changes can land on any push. Unproven.
- **Adoption note:** the ~117k stars signal viral attention more than battle-tested stability; with no releases and a heavy issue backlog, treat adoption as a popularity signal, not a maturity one.
- **Risk flags:** heavy install footprint (clones into `~/.claude/skills/`, symlinks, `.gstack/` state, auto-starting browse daemon; team mode commits `.claude/`+`CLAUDE.md`). Advisory-only — "reviews"/"locks" are prompt-level, not CI gates.

## Caveats (unverified)

- [未验证] License MIT and primary language TypeScript per GitHub metadata as of 2026-06-26; repo last pushed 2026-06-25; no GitHub release/tag was reported (`latestRelease: null`), so there is no stable version to pin — re-verify before relying on specific command behavior.
- [未验证] Star count (~116k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] The "23 tools"/command list (e.g. `/office-hours`, `/plan-eng-review`, `/review`, `/qa`, `/cso`, `/ship`, `/document-release`, `/retro`) is drawn from the project README; the exact set and naming change with the repo and should be read from the current `skills/` directory, not this page.
- [未验证] Claimed support for ~10 AI coding agents (Codex CLI, OpenCode, Cursor, Factory Droid, Slate, Kiro, Hermes, GBrain, etc.) via `./setup --host` auto-detection is from the README; per-agent activation fidelity is not independently confirmed here.
- [未验证] Install/runtime requirements (Git, Bun v1.0+, optional Node on Windows, an auto-starting "browse daemon", optional Supabase/PGLite for a memory feature) are from the README and not verified by running setup.
- [推断] Because behavior lives in prompt/markdown skills loaded by the agent, every "review"/"lock"/"gate" is advisory — the agent can deviate; treat these as guidance, not enforced controls.
- [推断] As one person's personal config with no releases, breaking changes can land on any push; vendor the version you tested if you need stability.
