---
name: dbskill
slug: dbskill
repo: https://github.com/dontbesilent2025/dbskill
category: knowledge-content
tags: [agent-skills, business-diagnosis, claude-code, chinese, content-creation]
language: JavaScript
license: CC-BY-NC-4.0
maturity: v2.14.2, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-29T03:58:40Z
  default_branch: main
  default_branch_sha: 096f726a20407901ca517cfc42509f96232fd0ea
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:49:23Z
  overall: C
  overall_score: 2.0
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 16
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 5226
        release_assets: 63
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 186
        last_commit_age_days: 16
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.948
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: type_na }
    risk_license: { reason: license_unparsed }
---

# dbskill

A personal, curated pack of ~21 Chinese-language agent skills (`/dbs-*`) for business-model diagnosis, content creation, and personal decision-making, installable into Claude Code and other harnesses via a plugin marketplace or a `skills` CLI.

![dbskill — health radar](../../../../assets/health/dbskill.svg)

## When to use

You're a solo founder, indie creator, or operator who runs a one-person business in Chinese-speaking markets, and you use Claude Code (or Codex / Cursor / Trae Solo) as a thinking partner. You keep asking the agent things like "is my business model actually viable", "why isn't this content getting traction", "what should my next 90-day goal be" — and you keep getting generic, slop-flavored advice because the agent has no opinionated framework to anchor on. dbskill drops in a coherent set of business-diagnosis skills: `/dbs-diagnosis` (business-model teardown), `/dbs-benchmark` (competitor analysis), `/dbs-content` and `/dbs-content-system` (content diagnosis and a structured content-engineering system), `/dbs-hook` and `/dbs-xhs-title` (short-video openings, Xiaohongshu title formulas), `/dbs-action` (execution-power diagnosis), `/dbs-decision` (a personal decision system), plus state-management commands (`/dbs-save`, `/dbs-restore`, `/dbs-report`) so a diagnosis session can persist and resume.

You reach for it when you want this *specific author's* methodology — the frameworks, case library, and ~4k+ knowledge atoms behind the commands — rather than building your own prompt stack. Install once (`claude plugin marketplace add dontbesilent2025/dbskill`, or `npx -y skills add dontbesilent2025/dbskill -g --all`), and the skills load on demand through your harness's native skill mechanism.

## When NOT to use

- **You don't operate in Chinese-language business contexts.** The skills, knowledge atoms, and case material are primarily Chinese; the frameworks lean on China-specific channels (Xiaohongshu titles, short-video hooks). Outside that context most of the value evaporates.
- **You want generic SDLC / coding discipline, not business coaching.** This is a domain pack about commerce, content, and decisions — not TDD, refactoring, or agent engineering. Pair it with a coding methodology pack instead of expecting overlap.
- **You already trust your own diagnosis frameworks.** dbskill is opinionated (Adlerian execution model, "slow is fast" friction-asset thesis, fixed title templates). Layering it over an existing coaching prompt stack invites conflicting advice — pick one source of truth.
- **You're on an unsupported / bespoke harness.** It activates through Claude Code / Codex / Cursor / Trae Solo skill-loading; with no loader the markdown won't auto-fire.
- **Commercial / productized use.** Licensed CC BY-NC 4.0 — commercial use requires the author's separate permission, so you can't freely bake it into a paid product. [未验证]
- **You need stability.** Single-maintainer pack at v2.x with frequent releases; framework wording and command routing can shift release-to-release. Pin a version if you depend on specific behavior. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [antfu/skills](../engineering-workflows/antfu-skills.md) | ✅ | Choose antfu/skills when you need personal coding/devtools skills rather than business diagnosis. | A maintainer's personal coding/devtools skills; engineering-flavored, English-first. dbskill is a domain pack for business diagnosis, not code workflow. |
| [Dimillian/Skills](../engineering-workflows/dimillian-skills.md) | ✅ | Choose Dimillian/Skills when you need iOS/Swift developer workflow skills. | Personal skills from an iOS/Swift developer; software-focused. Disjoint domain — pick by whether you want coding help or business coaching. |
| [awesome-claude-code-subagents](../../subagent-collections/awesome-claude-code-subagents.md) | ✅ | Choose awesome-claude-code-subagents when you need broad technical-role subagent coverage. | A large broad subagent collection across many technical roles; breadth over a single opinionated voice. dbskill is one author's deep, narrow business methodology. |
| Generic LLM business-coaching prompts | 未收录 | Choose ad-hoc prompts only when you do not need a curated framework or persistent author voice. | Ad-hoc prompts have no curated framework, case library, or persistence; dbskill ships ~4k knowledge atoms and state commands behind a coherent author voice. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance (2026-06):** active — last pushed 2026-06, at v2.14.2 with frequent releases and only ~10 open issues. It does cut tagged releases, so a version is pinnable. Active, not coasting.
- **Governance & bus factor:** single-author `User`-owned pack (dontbesilent2025); the entire value — frameworks, case library, ~4k knowledge atoms — is one creator's methodology, with no foundation or team behind it. ~7k stars on a one-person pack is a bus-factor flag; continuity is tied to that author.
- **Age & Lindy verdict:** created 2026-03, so only ~3 months old as of 2026-06 — very young and hyped, with no longevity track record. Treat as unproven; its frameworks are the author's opinions, not time-tested standards. Fails the Lindy test purely on age.
- **Risk flags:** licensed **CC BY-NC 4.0** — non-commercial only, so you cannot bake it into a paid product without separate permission (GitHub reports the license as `Other`/`NOASSERTION`). Chinese-market-specific and advisory-only (prompt-level coaching, no enforcement).

## Caveats (unverified)

- [未验证] License stated as CC BY-NC 4.0 in the README ("本项目采用 CC BY-NC 4.0 许可证"); GitHub's API reports the license as `Other` / `NOASSERTION` because CC licenses aren't in its SPDX detection set — verify the LICENSE/README before any commercial use.
- [未验证] Latest release reported as v2.14.2 (published 2026-06-05) with the repo last pushed 2026-06-05 per GitHub metadata as of 2026-06-26; re-verify before relying on a specific version's skills or behavior.
- [未验证] Star count (~6,969 per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] Skill inventory (~21 `/dbs-*` commands), the "4,176 knowledge atoms" and "12 methodology documents" counts, and the supported-harness list (Claude Code, Codex, Cursor, Trae Solo, Grok Build) are from the project README; not independently confirmed here, and they change release-to-release.
- [未验证] GitHub reports the primary language as JavaScript, but the README describes the deliverables as skill markdown / JSONL knowledge files with build/packaging scripts rather than a runnable application; treat it as a skill-pack, not a CLI.
- [推断] Because behavior lives in prompt/markdown skills loaded by the agent, the frameworks are advisory — the agent can still deviate; outputs are coaching prompts, not guaranteed business outcomes.
