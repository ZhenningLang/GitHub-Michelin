# AGENTS.md — oss-atlas

> This repo is read **primarily by coding agents** (and secondarily by humans). It is a
> curated, natural-language knowledge base for **OSS selection** (选型): when an agent gets a
> task, it reads this index to choose the right open-source project — weighing *when NOT to
> use* each option, not just what it does.
>
> The index is deliberately **weak**: no database, no search engine, no embeddings. Just
> Markdown an agent reads and reasons over. The structure below is the only "query API".

## What this is (and is not)

- **Is**: a selection-decision corpus. Each project page is the *opposite of a README* — it
  leads with positive scenarios, negative scenarios, horizontal comparison, tech stack,
  dependencies, and ops difficulty.
- **Is not**: a tutorial site, a marketing collection, or a dump of non-repos (SaaS pages,
  articles). It collects real open-source **repositories** broadly, across any domain, and
  organizes them for selection. See "Inclusion criteria" below.

## READ ROUTE — how an agent navigates (recursive tree)

`categories/` is a **recursive tree** of arbitrary depth (not a fixed number of levels; large
categories split into sub-categories). Descend by `INDEX` — but **search first when the task's
wording doesn't map onto a category name**: the tree has one parent per page, so a project that sits
on a different axis than your task (a Python HTTP client that solves an anti-bot problem) is not
reachable by descent alone. `grep -ri` the task's symptoms across `categories/` and start from the
hits. What is *not* allowed is answering from memory: every recommendation must come from a page you
actually opened.

```
INDEX.md                              ← root: top-level category route (中文: INDEX.zh.md)
categories/<cat>/INDEX.md             ← a category node: its project pages + child sub-categories
categories/<cat>/<subcat>/INDEX.md    ← deeper nodes, as the tree grows
…/<slug>.md                           ← a leaf: the English selection page (中文 sibling <slug>.zh.md)
```

English (`*.md` / `INDEX.md`) is the **canonical path you read by default**. The `.zh.md` /
`INDEX.zh.md` files are the monolingual Chinese mirror.

Procedure when you have a task and need to pick a project:

1. Read `INDEX.md`; follow the category that matches your task. If the task is phrased as a symptom
   ("my scraper gets 403") rather than a category ("I need a web scraper"), `grep -ri` those symptom
   words across `categories/` first and descend from the hits instead.
2. Keep **descending** through sub-category `INDEX.md` files (the tree can be deep) until you reach
   project pages; scan their one-liners + the comparison matrix to shortlist 1–3.
   Before concluding a task is **not covered**, search for it — a false "not indexed" wastes the whole
   index, and descent alone produces them.
3. Read each shortlisted `<slug>.md`. The decisive section is usually **`## When NOT to use`**:
   check it against the task's hard constraints (scale, deps, ops budget, license). Then weigh
   **`## Health & viability`** — is it maintained, well-backed, and likely to last? Apply the
   **Lindy** prior: a long-lived *still-active* project is a safer bet than a young hyped one
   (high stars on a young/stale repo is a risk flag, not proof). See "Selection heuristics" below.
4. Recommend with the *tradeoff that decided it*. If the best fit is named in a `## Comparison`
   but is **not yet indexed** (`未收录`), say so — do not pretend the index is complete. `非仓库` /
   `not a repo` is a *different* status: it means the alternative is not a repository at all
   (hosted SaaS, closed app, paid service), so it is out of scope by shape rather than missing.

There is a skill for this: **`skills/select-oss/`** — a dual-mode navigator that reads the index
locally when you're inside a clone, or fetches the public raw files otherwise. It installs into any
coding agent via skills.sh (`npx skills add ZhenningLang/oss-atlas`); see the README "Install" section.

## Selection heuristics (beyond "what it does")

Picking OSS is a bet on the future, not just a feature match. Beyond `When NOT to use`, weigh each
page's `Health & viability` section:

- **The Lindy prior.** For non-perishable things (software, formats, tools), expected remaining
  life rises with current age: a project that has been *actively maintained* for 12 years is a
  safer long-term bet than one that exploded in 6 months. Use it as a **prior**, not a law —
  **age × still-active together**. It cuts both ways: it discounts a young hyped repo (suspicious
  stars, unproven) *and* it does **not** rescue an old **abandoned** one (age alone ≠ alive). It can
  also mislead across paradigm shifts (an old tool displaced by a new approach). [推断]
- **Backing & bus factor.** A foundation (Apache/CNCF/LF) or a committed vendor outlasts a single
  maintainer's free time. Note who owns the roadmap and that org's track record.
- **Risk flags over hype.** Relicense history (Grafana→AGPL, Redis→SSPL), open-core feature-gating,
  CLA, deprecation/CVEs — these decide more than star count.

Surface the *signal that decided it* in your recommendation, the same way you surface the deciding
tradeoff.

## WRITE CONTRACT — how to add or update an entry

The schema is the contract: **`tools/schema.md`**. In short:

- A project is a **bilingual pair** in the same dir: `categories/<category>/<slug>.md` (English,
  canonical) + `categories/<category>/<slug>.zh.md` (Chinese). Both = YAML frontmatter (**facts**)
  + Markdown body (**judgment**). Keep facts and judgment separate.
- Required frontmatter (identical in both files): `name, slug, repo, category, tags, language, license, maturity, last_verified, type`.
- `type` ∈ `tool | library | app | framework | service | model | skill-pack` and decides which body
  sections are required.
- Required body sections — **all types**: `When to use`, `When NOT to use`, `Comparison` (Chinese:
  `何时使用`, `何时不用`, `横向对比`). `When to use` is the *trigger scenario* (when to think of it);
  `How it works` / `怎么用起来` (between those two; backfill in progress) is the *backbone user story* —
  plain-language mechanism + a flow card generated from `flows/<stem>.json` by `tools/flow_card.py`. **Non-`skill-pack` types also require**: `Tech stack`,
  `Dependencies`, `Ops difficulty` (`技术栈`, `依赖`, `运维难度`). A `skill-pack` (prompt/skill
  collection) omits those three — don't pad them with "N/A". **Every page (all types) also has a**
  `Health & viability` / `健康度与可持续性` **section** — a dated, labeled viability verdict
  (maintenance, governance/bus-factor, backing, **age/Lindy**, adoption, risk flags; see schema §7)
  — **and ends with a** `Caveats (unverified)` / `存疑（未验证）` **ledger** — the uncertainty list.
- **Bilingual**: the two files are monolingual mirrors — do NOT mix languages inside one file.
- **Truth labeling**: anything not confirmed from a source is `[未验证]` / `[推断]`. Date your
  facts (`maturity`, `last_verified`) — **dates are UTC**, and the gate compares `last_verified`
  against UTC today, so a local date ahead of UTC (writing just after midnight at UTC+8) is an
  ERROR. Never assert opinion as fact — an agent will act on it. Keep
  inline labels in the prose to the load-bearing/contested few (≤3 before the Caveats ledger — the
  linter WARNs above that); every unverified fact still gets a bullet in the Caveats ledger.
- **Chinese punctuation**: in `.zh.md` bodies, use fullwidth Chinese punctuation (`，；：！？（）“”`),
  not the Western ASCII forms — the most common slip is a half-width comma `,` between Chinese
  characters where it must be `，` (parens wrapping Chinese use `（）`, quotes use `“”`). Code spans,
  link targets, URLs, and the language-neutral frontmatter keep their ASCII punctuation. The linter
  ERRORs on ASCII `, ; ! ? : ( ) "` touching a CJK character in a `.zh.md` body.
- After writing, update its category `INDEX.md` + `INDEX.zh.md` (and parent/root `INDEX` files for a
  new category) **and the README master listing** (`README.md` + `README.zh.md`), then run the
  linter. If a category overflows (lint WARNs), run `refactor-index`. The linter ERRORs if a page is
  missing from its `INDEX` **or** from the README listing, so neither can silently drift. The
  `Health`/`健康度` column in those tables is **machine-synced, never hand-graded**: run
  `python3 tools/sync_index_health.py --apply` after scoring a page's `health:` block (lint
  ERRORs on any row that drifts from the page frontmatter).

Skills: `.claude/skills/add-project/` (author a new entry), `.claude/skills/sync-entry/`
(re-verify a stale entry), `.claude/skills/refactor-index/` (rebalance the tree — split overflowing
categories into sub-categories, merge thin/overlapping ones). These three are **maintainer** skills,
marked `metadata.internal: true` so skills.sh hides them from the public install (only `select-oss`
ships); to install one for contributing, set `INSTALL_INTERNAL_SKILLS=1`.

## Inclusion criteria

**The unit of inclusion is a git repository.** Add any real open-source **repo**, across any domain —
no domain restriction, and no requirement that an in-index substitute already exists (comparisons may
cite `未收录` alternatives). Breadth is the goal: whatever task an agent gets, it should find guidance.

Do **not** add: things that aren't a repository (hosted SaaS, landing pages, articles, docs sites,
ads); an exact duplicate of an already-indexed repo; or an empty/contentless repo. That's the whole
bar — crowded fields are handled by the self-balancing tree (split into sub-categories), not by
dropping entries.

## Lint (the structural gate — no tests)

This is a content repo with no runtime logic. The pre-merge gates are the structural linter, the
committed-report freshness check, and the deterministic quality gate:

```bash
python3 tools/lint.py                        # structural: shape, routing, dead links, fanout
python3 tools/reverse_index.py --check       # reports/ must match the pages (SSOT)
python3 tools/quality_scan.py --fail-on-gated   # deterministic triage categories (whole repo)
# or: make gates   (runs all three, same as CI)
```

ERROR = exit non-zero (CI fails). WARNING = printed (e.g. an entry is stale). Run all three before
committing. CI runs them on every PR and every push to `main` (`.github/workflows/lint.yml`): the
`structural-lint` job is `lint.py` + `reverse_index.py --check`; `quality-gate` is
`quality_scan.py --fail-on-gated`.

**Touch the tree shape → refresh the reports.** Adding, renaming, moving, or deleting pages changes
the reverse index (and the named-but-unindexed backlog). `reports/` are committed SSOT, so regenerate
them with `python3 tools/reverse_index.py --write` in the same change — the pre-commit hook does this
automatically for staged `categories/` changes, and CI fails if you forget.

**First-pass intake pages are backlog, not finished pages.** 96 English pages (plus their mirrors)
were mass-created from a name backlog by `tools/intake_queue_apply.py` /
`tools/agent_skills_intake.py`: the facts are machine-read from the GitHub API, but `When to use`
describes picking software in general rather than *this* project's trigger, and `Dependencies` /
`Ops difficulty` / `Health & viability` say only that nobody has looked yet. `lint.py` passes them —
the sections exist — so `quality_scan.py` reports them as `intake-stub-page` (report-only, with a
backlog count in its summary) and a reader should treat such a page as a lead, not a verdict.
Re-verifying one is exactly when the placeholder prose has to be rewritten, so a page that still
carries it while claiming `last_verified >= 2026-09-22` fails the gate as
`intake-stub-page-reverified` (`OSS_ATLAS_STUB_BLOCKED_FROM` moves the date). Rewrite with
`sync-entry`.

**Neither gate is a *semantic* review.** `lint.py` enforces shape: frontmatter keys, bilingual pair
+ frontmatter parity, required/forbidden sections per `type`, H1, links, the Caveats ledger, fanout.
`quality_scan.py --fail-on-gated` fails only on its **gated** deterministic categories
(`generic-comparison-template`, `indexed-page-marked-non-repo`, `indexed-page-marked-not-indexed`,
`composite-alternative-partly-indexed`, `truncation-fragment`, `zh-link-to-english-sibling`,
`intake-stub-page-reverified`); run it without the flag for the full report-only triage. Neither can judge whether `When to use` is a real
trigger scenario, whether `How it works` matches how the project is really used, whether `Comparison` compares real substitutes, or whether prose is accurate — a clean
run ≠ content reviewed. Those remain agent/human judgment per `tools/schema.md`.

## Conventions

- Slugs are kebab-case; `slug` in frontmatter MUST equal the **base** filename (`beads` for both
  `beads.md` and `beads.zh.md`).
- `category` in frontmatter MUST equal the **immediate** parent directory name (the leaf category),
  at any depth in the tree.
- Internal links are relative and must resolve (the linter checks this).
- One project = one bilingual page pair = one leaf category. Cross-cutting belongs in `tags`.
