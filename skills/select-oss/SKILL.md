---
name: select-oss
description: Use when a task needs choosing an open-source project — pick a library, tool, framework, model, or system. Navigates the oss-atlas index (an agent-first "inverse-of-a-README" corpus that leads with *when NOT to use*) to produce a shortlist with the decisive tradeoff. Trigger phrases like "which library should I use", "pick an OSS for X", "compare open-source options for Y", "选型".
---

# select-oss

[oss-atlas](https://github.com/ZhenningLang/oss-atlas) is a natural-language index built so an
agent can pick OSS for a task **fast and honestly**. Each page is the *opposite of a README* — it
leads with positive scenarios, **when NOT to use**, a comparison matrix, deps, and ops cost.

**Never answer from memory** — every recommendation must come from a page you actually opened.
Descend the route; but when the task reads as a *symptom* rather than a category, **search first and
descend from the hits** (each page has exactly one parent, so cross-cutting projects are not
reachable by descent alone).

## Where the index lives (resolve this first)

The index is a tree of Markdown files. Read them from whichever source you have:

- **Local copy** — if you're working inside an oss-atlas clone, or one exists on disk, read the
  files directly. Get one with: `git clone https://github.com/ZhenningLang/oss-atlas`.
- **Remote (default)** — otherwise fetch over HTTP from the canonical source. Base URL:

  ```
  https://raw.githubusercontent.com/ZhenningLang/oss-atlas/main/
  ```

  Prefer `curl -s <url>` when you have a shell (it returns the exact Markdown, links intact). If
  you only have a web-fetch tool, ask it to **return the file contents verbatim, including all
  links** — you navigate by those links, so a summary is useless here.

  Resolve relative links the way a browser would: treat the base URL as the web root and join each
  relative link against the directory of the file you just read. So a root-`INDEX.md` link to
  `categories/agent-memory/INDEX.md` becomes
  `…/main/categories/agent-memory/INDEX.md`; a page link `mem0.md` inside that category becomes
  `…/main/categories/agent-memory/mem0.md`.

English (`*.md` / `INDEX.md`) is the canonical path. The `.zh.md` files are a Chinese mirror.

## Procedure

1. **Frame the selection** from the task. Write down the hard constraints up front — these are
   what kill candidates:
   - scale / throughput expectations
   - deployment & ops budget (can the user run a DB? a GPU? a server?)
   - license constraints
   - language / ecosystem fit
   - must-have vs nice-to-have features

2. **Level 1 — category.** Read `INDEX.md`. Match the task to one or more categories by their
   "use when". If the task's words don't map onto any category name, don't force it — search the
   corpus for the task's symptoms and start from the hits:

   ```bash
   grep -ril "403\|fingerprint\|anti-bot" categories/     # local clone
   ```

   Remote-only (no clone): fetch `reports/repo-page-index.csv`, which lists every page's repo, slug,
   category and path in one file, and scan it before descending.

   Only after searching may you say the index doesn't cover this domain — a false "not indexed" is the
   worst answer this index can give.

3. **Level 2 — shortlist.** Descend into each candidate category's `INDEX.md` (the tree can be
   deep — keep following sub-category `INDEX.md` files until you reach project pages). Use the
   one-liners + comparison matrix to pick 1–3 candidates.

4. **Level 3 — decide.** Read each candidate's `<slug>.md`. The decisive section is usually
    **`## When NOT to use`**: check it against the hard constraints from step 1. Then weigh
    `## Ops difficulty` and `## Dependencies` against the user's budget. If `## Q&A` /
    `## 快问快答` is present, read it — leftover questions from the reading conversation.

5. **Recommend** with the *tradeoff that decided it*, not just a name. Format:

   ```md
   ## Recommendation
   - **Pick: <project>** — <one-line why it fits this task>
   - Decisive tradeoff: <the when-not / ops / dep fact that ruled out the runner-up>
   - Runner-up: <project> — <why second>
   - Not chosen: <project> — <the disqualifying constraint>
   ```

## Honesty rules

- If the best fit is named in a `## Comparison` but marked `未收录` (not yet indexed), **say
  so** and recommend it anyway with a caveat — do not pretend the index is complete.
- Respect `last_verified` in the frontmatter: if a page is old, flag that its facts may be
  outdated and verify the decisive ones against the live repo before relying on them.
- Surface `[未验证]` / `[推断]` labels and the `## Caveats (unverified)` ledger from the page —
  don't launder them into confident facts.
- **Challenge `?` on the health radar.** A gray `?` on a radar axis means the machine could
  not confidently measure it — **not** that the project is deficient. If `risk_license` is `?`,
  the license may be a standard MIT/Apache that GitHub's licensee failed to parse (e.g. a trailing
  third-party notice pushed the text outside the template-match tolerance). If `maintenance` or
  `governance` is `?`, the repo may live on GitLab or a non-Git host the scorer cannot reach.
  Treat `?` as "unverified" and, when the choice hinges on that axis, verify it manually
  (e.g. `gh repo view <owner>/<name>` or read the LICENSE file) before deciding.
- If two candidates are genuinely tied, present both with their tradeoffs instead of forcing a
  single pick.

## Anti-patterns

- Picking by star count or popularity instead of fit-to-constraints.
- Ignoring `## When NOT to use` because the positive scenario looked good.
- Recommending a project whose `## Dependencies` exceed the user's stated ops budget.
- Reading one page and stopping — always check the category's comparison matrix for alternatives,
  including `未收录` ones.
