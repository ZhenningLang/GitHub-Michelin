---
name: select-agent-skills
description: Use when a task needs choosing agent skills, SKILL.md packs, prompt workflows, subagent bundles, or a combination of skills from GitHub-Michelin. Trigger on requests like "pick skills for this task", "which agent skill should I use", "recommend a skill combo", "根据任务推荐 skills", or when the user specifically asks for agent-skills rather than a general OSS library/tool. Navigates the GitHub-Michelin `agent-skills` category first and outputs fit, sequence, tradeoffs, and when-not-to-use caveats.
---

# select-agent-skills

Use this skill to choose **agent-consumable skills** from GitHub-Michelin, not arbitrary OSS projects. If the user asks for a database, framework, library, app, model, or infrastructure component, use `select-oss` instead.

## Resolve the Index

Read GitHub-Michelin from the best available source:

- Local clone: start at `categories/agent-skills/INDEX.md`.
- Remote fallback: fetch from `https://raw.githubusercontent.com/ZhenningLang/GitHub-Michelin/main/categories/agent-skills/INDEX.md`.

English pages are canonical. Use `.zh.md` only when the user wants Chinese-facing output or when the skill itself is Chinese-first.

## Procedure

1. **Frame the task.** Capture the user's job in one line and list hard constraints:
   - output type: code, prose, slide deck, social card, review, research, security, memory, etc.
   - host harness: Claude Code, Codex, Cursor, OpenCode, Gemini CLI, unknown.
   - language/locale: Chinese, English, bilingual, domain-specific voice.
   - artifact expectations: editable files, HTML, PNG, Markdown, installed plugin, subagent delegation.
   - risk constraints: license, commercial use, network access, browser/Node/GPU/API keys.

2. **Route by task leaf.** Read `categories/agent-skills/INDEX.md`, then descend into the most relevant leaf `INDEX.md` files. Prefer task leaves over provenance leaves when both fit:
   - `slides-ppt` for decks and presentation generation.
   - `visual-content` for cards, covers, illustrations, and rendered publishing visuals.
   - `writing` for translation, AI-text humanizing, editorial voice, or long-form writing.
   - `design` for UI taste, anti-slop, design critique, redesign, or visual judgment.
   - `engineering` for code quality, web performance, testing, scientific/engineering workflows.
   - `context-engineering` for context routing, compression, memory, and harness context discipline.
   - `security` for security playbooks and review skills.
   - `vendor-collections`, `personal-collections`, or `subagent-collections` when source/provenance or consumption unit is the deciding constraint.

3. **Shortlist.** Use leaf one-liners and comparison matrices to pick 1-5 candidates. Include a skill only if its task surface matches the user's requested artifact or workflow.

4. **Read decisive pages.** For each candidate, read its page and especially:
   - `## When NOT to use` for blockers and better substitutes.
   - `## Comparison` for adjacent skills or non-indexed alternatives.
   - `## Health & viability` for maintenance, license, Lindy, and bus-factor risks.
   - `## Caveats (unverified)` for uncertainty that must be surfaced.

5. **Compose only when useful.** Recommend a combination only when the skills operate on different stages of the same workflow. Do not stack overlapping rubric skills that will fight each other.

## Output Format

Use this structure:

```md
## Recommendation
- **Pick:** <skill or combo> — <why it fits the task>
- **Use sequence:** <step 1 → step 2 → step 3, or "single skill">
- **Decisive tradeoff:** <why this beats the runner-up>

## Candidates
| Candidate | Role in workflow | Fit | Watch out |
|---|---|---|---|
| <linked skill> | <stage/artifact> | <why> | <when-not / caveat> |

## Not Chosen
- <candidate> — <specific blocker or mismatch>

## Gaps
- <say what GitHub-Michelin does not cover, or "None identified from the pages read">
```

## Honesty Rules

- Do not recommend by star count. Use fit-to-task, `When NOT to use`, dependencies, license, and health.
- Do not hide `[未验证]` or `[推断]` labels. Surface them when they affect the choice.
- If a good alternative is named in a comparison table but marked `未收录`, mention that it is not indexed.
- If the user's harness cannot load skills, say so and recommend a non-skill substitute or a design-system/prompt document instead.
- If the task calls for a normal OSS library/tool rather than an agent skill, stop and use `select-oss`.
- If two skills overlap directly, pick one source of truth instead of chaining both.
