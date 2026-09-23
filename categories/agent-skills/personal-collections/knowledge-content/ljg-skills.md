---
name: ljg-skills
slug: ljg-skills
repo: https://github.com/lijigang/ljg-skills
category: knowledge-content
tags: [skills, claude-code, knowledge-work, chinese, reading, visual-cards, skills-cli]
language: HTML
license: NOASSERTION
maturity: no tagged releases, active (pushed 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-26T04:33:36Z
  default_branch: master
  default_branch_sha: 2e91dec43ed34dd926329c8cdf2f6b404de6abee
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:49:30Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 6
        active_weeks_13: 13
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
        repo_age_days: 199
        last_commit_age_days: 6
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.963
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

# ljg-skills

Li Jigang's personal, curated Claude Code skill collection (20+ skills) for Chinese-language knowledge work — reading, deconstructing papers/books, conceptual analysis, plain-language rewriting, and turning content into visual PNG cards — installed via the `skills` CLI.

![ljg-skills — health radar](../../../../assets/health/ljg-skills.svg)

## When to use

You're a Chinese-speaking knowledge worker, researcher, or content creator who reads academic papers, books, and long-form articles, and you keep wanting your coding agent to do *intellectual* work rather than write code: distill a dense paper for a non-specialist, deconstruct a book around its central problem, rewrite a tangled concept so a 12-year-old gets it, or turn your notes into a shareable infographic card. Out of the box your agent has no opinionated method for any of this — it summarizes blandly and the output isn't reusable. You want a battle-tested set of structured knowledge prompts that one person has refined for exactly these tasks.

You run `npx skills add lijigang/ljg-skills -g --all` (append `#md` for the Markdown branch if you live in Obsidian/VSCode/Notion rather than Emacs/Denote org-mode) and your agent gains a menu of on-demand skills it loads when the task matches: `ljg-paper` (extract paper insights for a general audience), `ljg-book` (problem-centered book deconstruction), `ljg-learn` (analyze a concept across eight dimensions), `ljg-plain` (rewrite for 12-year-old comprehension), `ljg-read`/`ljg-reads` (companion reading with translation and cross-disciplinary analysis), `ljg-card`/`ljg-library` (render content into visual PNG cards and illustrated book-collection cards), `ljg-qa` (turn an article into a structured Q&A chain), `ljg-travel`, `ljg-invest`, plus more covering writing, word analysis, relationship diagnostics, structured debate, and presentation design. Pre-built workflows chain several skills (e.g. read a paper, then generate a card). Because it ships in the `skills` CLI's `SKILL.md` format, the pack installs into your harness's skills directory, so the same skills can travel across Claude Code and other agents the CLI supports.

## When NOT to use

- **You want code/engineering skills.** This pack is knowledge-work and content-creation, not SDLC. For TDD, review, refactoring or framework conventions, a code-oriented pack (see Comparison) fits better; these skills won't help you ship software.
- **You don't work primarily in Chinese.** Skills are authored in Chinese (with English technical terms) and tuned for Chinese knowledge-work idioms; on English-first tasks the framing and output style may not fit.
- **You already run a curated knowledge/writing skill stack you trust.** Layering another opinionated set of reading/analysis prompts on top invites conflicting methods and double-routing — pick one source of truth per concern.
- **Your harness has no skills loader.** It activates through the third-party `skills` CLI writing `SKILL.md` files into the agent's skills directory; on a bespoke or unsupported agent there's nothing to fire them and the markdown won't auto-apply.
- **You need enforcement or determinism.** Output is a prompt-shaped analysis the agent *produces*; nothing validates the distillation's accuracy. It's a method, not a gate — verify the substance yourself. [推断]
- **You need version stability.** No tagged releases as of this check — you track a moving branch, and the dual org-mode (`master`) / markdown (`md`) branches plus the skill inventory can shift between pulls.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [pua](../engineering-workflows/pua.md) ✅ | indexed | Choose pua when you want another single-maintainer Chinese skill collection with a persistence persona. | Another single-maintainer Chinese skill collection; different focus and conventions. Same genre (one person's curated Chinese skills); compare on which author's method and domain match your work. |
| [qiushi-skill](../engineering-workflows/qiushi-skill.md) ✅ | indexed | Choose qiushi-skill when you need a sibling Chinese skill set with its own task coverage. | Single-maintainer Chinese skill set; sibling personal collection with its own task coverage. ljg-skills centers reading/knowledge-distillation and visual cards. |
| [antfu/skills](../engineering-workflows/antfu-skills.md) ✅ | indexed | Choose antfu/skills when Vue/Vite frontend engineering conventions matter more than knowledge work. | Maintainer's personal pack too, but for the Vue/Vite frontend *engineering* stack — opposite domain. Pick by whether you need code conventions or knowledge-work methods. |
| [Dimillian/Skills](../engineering-workflows/dimillian-skills.md) ✅ | indexed | Choose Dimillian/Skills when Swift/Apple development conventions are the real need. | Personal collection skewed toward Swift/Apple development. Same "one person's skills" genre, different (code) domain. |
| Anthropic's official skills / built-in slash commands | 未收录 | Choose official skills or built-in slash commands when you want the platform's own ecosystem. | The platform's own skill ecosystem; ljg-skills is a third-party curated bundle layered on top, so it can duplicate or conflict with native skills. |

## Health & viability

- **Responsiveness**: Cannot be scored — type_na.
- **Maintenance** — actively maintained: last pushed 2026-06, not archived (as of 2026-06). The cadence reads active rather than coasting, but there are no tagged releases — you track a moving branch.
- **Governance & bus factor** — single-maintainer personal repo (`User`-owned). One author's curated method; if Li Jigang stops, the pack stops. ~6k stars don't change that — it's a one-person bus factor, normal for a personal collection but plan for fork-and-own.
- **Age & Lindy** — created 2026-03, so ~0 years old as of 2026-06: young, unproven by Lindy. It's active, but too new to have a track record across model/CLI churn — adopt for the method, not for longevity.
- **Risk flags** — no detected license (`NOASSERTION`) as of 2026-06: reuse/redistribution rights are unclear, confirm with the author before depending on it. Content (skill inventory, dual org-mode/markdown branches) can shift pull-to-pull.

## Caveats (unverified)

- [未验证] No license file detected via GitHub metadata on 2026-06-26 (`licenseInfo` is null) — frontmatter records `NOASSERTION`; without an explicit license, reuse/redistribution rights are unclear, confirm with the author before depending on it.
- [未验证] No tagged releases / `latestRelease` is null as of 2026-06-26; "maturity" is inferred from last push (2026-06-26) and activity, not a semver. Repo is not archived.
- [未验证] Star count (~6,237 per GitHub on 2026-06-26) is unreliable and date-sensitive; treat as indicative only, not a quality signal.
- [未验证] Primary language reported as HTML (with Shell/Python/JS shares) per GitHub on 2026-06-26; that reflects the card-rendering/automation tooling, not a runnable app — the substance is markdown/org `SKILL.md`-style prompt files.
- [未验证] The skill inventory (`ljg-paper`, `ljg-book`, `ljg-learn`, `ljg-plain`, `ljg-read`/`ljg-reads`, `ljg-card`, `ljg-library`, `ljg-qa`, `ljg-travel`, `ljg-invest`, and others), the "20+ skills" count, and the dual `master` (org-mode) / `md` (markdown) branch structure are read from the README on 2026-06-26 and can shift between pulls; verify the live `skills/` directory rather than trusting this snapshot.
- [未验证] Install via the third-party `skills` CLI (`npx skills add lijigang/ljg-skills -g --all`, `#md` for the markdown branch) and its supported-harness behavior are properties of that CLI, not of this repo; activation fidelity per harness is not independently confirmed here.
- [推断] Because behavior lives in prompt/markdown skills the agent loads, output is advisory — the agent can deviate and the analysis can be wrong; these are method prompts, not hard guarantees of accuracy.
- [推断] Skills encode one maintainer's personal knowledge-work method (e.g. the "eight dimensions" or problem-centered framings); useful if you share that approach, friction if you don't, and not an independently verified standard.
