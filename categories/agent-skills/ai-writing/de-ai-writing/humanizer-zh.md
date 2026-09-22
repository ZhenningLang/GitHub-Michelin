---
name: Humanizer-zh
slug: humanizer-zh
repo: https://github.com/op7418/Humanizer-zh
category: de-ai-writing
tags: [claude-code, skill, humanize, ai-text-removal, chinese-writing, editorial]
language: Markdown
license: MIT
maturity: no tagged release, last pushed 2026-01, not archived (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-01-19T07:46:35Z
  default_branch: main
  default_branch_sha: 91f3d394db8419c20d67ebe22a96cf8fee0a404b
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T10:48:19Z
  overall: C
  overall_score: 2.25
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 165
        active_weeks_13: 0
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
        repo_age_days: 165
        last_commit_age_days: 165
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
    adoption: { reason: no_package_structural }
---

# Humanizer-zh

A single Claude Code skill (`SKILL.md`, in Simplified Chinese) that rewrites text to strip out tell-tale AI-writing patterns — a Chinese localization of `blader/humanizer`, driven by a checklist of ~24 patterns across content, language, style, and filler.

![humanizer-zh — health radar](../../../../assets/health/humanizer-zh.svg)

## When to use

You're a Chinese-language writer, editor, or marketer who drafts with an LLM and keeps shipping copy that *reads* like a machine wrote it: every section ends with a "挑战与展望" wrap-up, the prose leans on "此外 / 至关重要 / 展示", every list is forced into three items, headers carry emoji, and the whole thing closes with "希望这对您有帮助". You want the agent to act as a real editor — find those tells and rewrite them into plain, human-sounding Chinese — without you re-explaining the rubric each time. Install Humanizer-zh into `~/.claude/skills/` and the agent loads a curated checklist of ~24 patterns (grouped into content / language-grammar / style / communication-filler) and applies them on demand, preserving meaning and tone while removing the AI signature.

You reach for it specifically when your output language is Chinese and you'd rather adopt a vetted, community-translated rubric than hand-write your own de-slop prompt. Install is a drop-in: `npx skills add https://github.com/op7418/Humanizer-zh.git`, or clone/copy the folder into your Claude Code skills directory; the skill then fires through Claude Code's native skill-loading.

## When NOT to use

- **You already run an AI-text-removal / voice skill you trust.** This overlaps directly with any existing "去 AI 腔 / humanize" routine (and with the original `blader/humanizer`). Stacking two de-slop rubrics invites contradictory edits — keep one source of truth.
- **You're not on Claude Code (or a harness that loads `SKILL.md`).** It's prompt-only markdown with no runner; on an unsupported agent there's nothing to invoke and the file won't auto-fire. [推断]
- **Your target language isn't Chinese.** The rubric and example patterns are written in Simplified Chinese and tuned to Chinese AI-writing tells; for English use the upstream `blader/humanizer` instead.
- **You need enforcement / scoring, not suggestions.** It rewrites by advisory instruction — the agent can still miss a pattern or over-edit; there's no lint pass or measurable "AI score" gate.
- **Low maintenance signal.** Single-author localization with no tagged release and no recent pushes; the upstream pattern list can drift away from this snapshot. Re-check before relying on it for current tells.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| `blader/humanizer` (upstream) | 未收录 | Choose the upstream project when English copy and the original rubric matter. | The English original this repo translates. Pick upstream for English copy; pick Humanizer-zh for Chinese-language tells and examples. |
| [Baoyu Skills](../content-production/baoyu-skills.md) | ✅ | Choose Baoyu Skills when you need a broader Chinese writing/translation skill bundle. | A broader Chinese-author skill collection (translation / markdown / content-gen helpers) rather than a single de-slop rubric. Compare on whether you want one focused humanize skill or a multi-skill writing bundle. |
| Hand-written de-slop prompt in `CLAUDE.md` | 未收录 | Choose a hand-written prompt when a few maintained inline rules are enough. | A few inline rules you maintain yourself: zero install and fully yours, but you re-derive and re-tune the pattern list instead of inheriting a vetted ~24-item checklist. |
| Wikipedia "Signs of AI writing" guide | 未收录 | Choose the Wikipedia guide when you need the reference source, not an installable skill. | The reference source behind the rubric — a human-readable guide, not an installable skill. Use it to audit or extend the checklist, not to run edits. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance** — last push 2026-01 (as of 2026-06), so ~5 months idle with no tagged release; this is a small localization repo, not an evolving product. Treat it as coasting-toward-static rather than actively maintained. [推断]
- **Governance / bus factor** — single-author (`User`-owned) localization of upstream `blader/humanizer`; ~11k stars on a one-person, single-purpose repo is a bus-factor flag — if the author stops, the Chinese pattern list freezes wherever it was. [推断]
- **Age & Lindy** — created 2026-01, so under a year old as of 2026-06: too young to claim a Lindy track record, and being a translation it inherits upstream's direction rather than setting its own. [推断]
- **Risk flags** — `[未验证]` no scoring/enforcement layer and no auto-fire runner; it's prompt-only markdown. The real durability risk is *drift*: the upstream rubric can evolve while this snapshot does not, so the value decays silently unless re-synced. MIT license, no relicense history.

## Caveats (unverified)

- [未验证] License is MIT and the repo is not archived per GitHub metadata as of 2026-06-26; `latestRelease` is null (no tagged version) and last push was 2026-01-19 — re-verify maturity before depending on it.
- [未验证] GitHub reports `primaryLanguage` as null (the repo is markdown/skill content); `language: Markdown` in frontmatter is an inference about content type, not a detected code language.
- [未验证] Star count (~11.6k per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] The "~24 patterns across 4 categories" figure and the example tells (此外 / 至关重要 / "挑战与展望" / emoji headers / "希望这对您有帮助") are read from the README/SKILL.md; the exact count and grouping may change with edits — read the current `SKILL.md` rather than trusting this summary.
- [未验证] Install commands (`npx skills add …`, clone into `~/.claude/skills/humanizer-zh`) and the claim that it activates via Claude Code's native skill loader are from the README; activation fidelity on other harnesses is not independently confirmed.
- [推断] Because behavior lives entirely in a prompt/markdown skill, rewriting is advisory — coverage of any given AI tell is best-effort, not guaranteed, and the agent may introduce its own edits.
