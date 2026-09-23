---
name: Qiushi-Skill
slug: qiushi-skill
repo: https://github.com/HughYau/qiushi-skill
category: engineering-workflows
tags: [skills, methodology, claude-code, dialectical-materialism, multi-harness, prompt-pack]
language: JavaScript
license: MIT
maturity: no tagged release, active (pushed 2026-05), ~3.3k stars (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-05-01T14:14:49Z
  default_branch: main
  default_branch_sha: 6cac8a569d3e5c48311d5bfe41c9d3dced27d14b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:48:52Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 16
        active_weeks_13: 5
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 181
        last_commit_age_days: 16
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 7
        top1_share: 0.852
        top3_share: 0.926
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

# Qiushi-Skill

A methodology skill pack (求是 Skill) that arms a coding agent with one core principle — "seek truth from facts" (实事求是) — plus nine dialectical-materialist / practice-philosophy "tools" (contradiction analysis, investigation-first, practice-cognition, mass line, criticism & self-criticism, protracted strategy, concentrate forces, spark-prairie-fire, overall planning), installable across Claude Code, Cursor, Codex, OpenCode and others via an `npx` installer.

![qiushi-skill — health radar](../../../../assets/health/qiushi-skill.svg)

## When to use

You're a developer (or a heavy agent user) who is tired of an obsequious assistant that agrees with whatever you say, jumps to a plausible-sounding answer, and declares victory without checking reality. You want the agent to behave like a disciplined analyst: investigate before deciding, name the *primary* contradiction instead of fixing the loudest symptom, validate hypotheses against actual practice (run it, observe it), and keep pushing until the work is genuinely done rather than nominally finished. Qiushi-Skill packages that posture as a set of on-demand skills: an "arming-thought" entry skill that injects the core principle at session start, plus nine method skills the agent loads only when a situation clearly calls for one (`/contradiction-analysis`, `/investigation-first`, etc.), with a `workflows/` layer to chain them.

You reach for it when you want a ready-made *thinking discipline* rather than building your own from scratch, and especially when you want that discipline to follow you across harnesses — the repo ships per-platform manifests (`.claude-plugin`, `.cursor-plugin`, `.codex`, `.opencode`, `.openclaw`, `.hermes`, `.nanobot`) and an `npx qiushi-skill install --target <harness>` flow, so the same "facts first, main contradiction, validate in practice" spine activates through each platform's native skill-loading mechanism.

## When NOT to use

- **You already run a curated thinking/planning skill stack.** This pack is opinionated and prescriptive (mandatory investigation-first, contradiction-naming before action). Layering its nine methods on top of an existing methodology system invites overlapping routing and competing instructions — pick one source of truth for "how the agent thinks."
- **Conceptual overlap with general dev-methodology packs.** Investigation-first, practice-cognition and criticism overlap heavily with brainstorm→plan→TDD→verify style packs; if you already have one, the added value is mostly the *contradiction / prioritization* framing, not the loop itself.
- **You're on an unsupported or bespoke harness.** Activation depends on each platform's loader; outside the shipped targets there's no mechanism to auto-fire the skills, and the markdown alone does nothing.
- **You want a runtime/library, not behavior shaping.** The `bin/` CLI is only an installer that copies skill files into your harness — there's no API or service to call; the product is prompts.
- **Enforcement is advisory.** "Mandatory" steps are prompt-level instructions the agent can still skip; this shapes behavior, it does not gate it. [推断]
- **Single-maintainer, no tagged release, naming may be a barrier.** Upstream is one maintainer with no semver release to pin, and the dialectical-materialism / historical-vocabulary framing (despite the README's "methodology, not propaganda" disclaimer) may be a non-starter for some teams or audiences.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [antfu/skills](antfu-skills.md) | ✅ | Choose antfu/skills when you need task-oriented build/repo chores rather than a thinking methodology. | Personal task-oriented skill set (build/repo chores) rather than a thinking methodology; complementary, not a substitute — Qiushi shapes *how to reason*, antfu's shape *how to do specific jobs*. |
| [Dimillian/Skills](dimillian-skills.md) | ✅ | Choose Dimillian/Skills when a stack-specific personal collection is the better fit. | Another personal curated collection skewed to a specific stack/workflow; overlaps as "someone's skill bundle" but not on the methodology/discipline axis. |
| [gstack](gstack.md) | ✅ | Choose gstack when you need harness configuration rather than a cognitive-method spine. | Personal harness-config collection; same leaf, different intent — config/tooling vs. a cognitive-method spine. |
| [wshobson/agents](../../subagent-collections/wshobson-agents.md) | ✅ | Choose wshobson/agents when you need a roster of role-specialist subagents. | Large subagent persona library (role specialists). Qiushi is a small set of *thinking methods*, not a roster of domain agents — combine rather than choose. |
| [awesome-claude-code-subagents](../../subagent-collections/awesome-claude-code-subagents.md) | ✅ | Choose awesome-claude-code-subagents when breadth-first subagent coverage matters most. | Breadth-first subagent catalog; Qiushi is depth-first on one methodology. Pick by whether you need many personas or one disciplined loop. |
| [Superpowers](../../../agent-dev-methodology/coding-agent-harnesses/superpowers.md) / general SDLC methodology packs | 部分已收录 | Choose Superpowers when brainstorm→plan→TDD→verify discipline is the core requirement. | Brainstorm→plan→TDD→verify methodology plugins occupy the same "discipline as skills" niche; Qiushi differs by leading with contradiction-analysis and prioritization rather than a test-first lifecycle. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance** — active: last pushed 2026-05, not archived (as of 2026-06), but no tagged release to pin — you track a moving branch. Reads active rather than abandoned, but without semver you can't lock a known-good state.
- **Governance & bus factor** — single-maintainer personal repo (`User`-owned), ~3.3k stars. One author owns the methodology and the multi-harness manifests; modest stars and a niche framing mean limited community backstop if the maintainer steps away.
- **Age & Lindy** — created 2026-03, ~0 years old as of 2026-06: young, Lindy-unproven. The *underlying* method (dialectical-materialist analysis) is old, but this packaging is new and untested across CLI churn — adopt for the discipline, not for longevity.
- **Risk flags** — the dialectical-materialism / historical-vocabulary framing (despite a "methodology, not propaganda" disclaimer) can be a non-starter for some teams or audiences; no enforcement (advisory prompts only). License recorded MIT as of 2026-06.

## Caveats (unverified)

- [未验证] GitHub metadata as of 2026-06-26: license MIT, primary language JavaScript, last pushed 2026-05-01, no tagged release (`latestRelease` null), topics `ai-agents/methodology/skills/workflow`, not archived — re-verify before relying on any of these.
- [未验证] Star count (~3.3k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, never as a quality signal.
- [未验证] The skill inventory (1 core principle "arming-thought" + 9 methods + a `workflows/` orchestration layer) and the supported-target list (Claude Code, Cursor, Codex, OpenCode, OpenClaw, Hermes, nanobot) are from the README; the actual `skills/` directory and per-harness activation fidelity were not independently inspected file-by-file here.
- [未验证] The hook-based session injection (arming-thought auto-injecting at session start, methods loading "only when clearly applicable") is described by the README; whether it fires reliably in any given harness is not confirmed.
- [推断] Because the methods live in prompt/markdown skills loaded by the agent, enforcement is advisory — the agent can still deviate from "mandatory" investigation-first / contradiction-naming steps.
- [推断] `type` is recorded as `skill-pack` because the `npx qiushi-skill` CLI is an installer for the skill files, not a standalone runtime; if you depend on the installer as tooling, evaluate it separately.
