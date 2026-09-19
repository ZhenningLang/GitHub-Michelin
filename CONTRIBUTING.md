# Contributing to oss-atlas

This is an **agent-first** selection index. It collects open-source repositories broadly; honesty
and accurate judgment matter more than polish. Read [AGENTS.md](AGENTS.md) and
[tools/schema.md](tools/schema.md) first.

## Inclusion criteria

**The unit of inclusion is a git repository.** Add any real open-source repo, across any domain —
no domain restriction, and no requirement that a substitute already be in the index (comparisons may
cite `未收录` alternatives).

Do **not** add: things that aren't a repository (hosted SaaS, landing pages, articles, docs sites,
ads); an exact duplicate of an already-indexed repo; or an empty/contentless repo. Crowded fields
are handled by splitting categories (see "Keeping the tree balanced"), not by dropping entries.

## Adding a project

The fastest path is the `add-project` skill (`.claude/skills/add-project/`). By hand:

1. Pick the **leaf** category (one project = one bilingual pair = one leaf category; cross-cutting
   goes in `tags`). New category only if it genuinely doesn't fit — add its row to the parent/root
   `INDEX.md` + `INDEX.zh.md`.
2. Create the **bilingual pair** `<slug>.md` (English) + `<slug>.zh.md` (Chinese) following
   [tools/schema.md](tools/schema.md): identical frontmatter (facts, dated, incl. `type`) + the
   required sections for that `type` (skill-packs omit `Tech stack / Dependencies / Ops difficulty`),
   plus a `Caveats (unverified)` / `存疑（未验证）` ledger on every page.
3. Each file is **monolingual** — English page uses the English headings, Chinese page the Chinese
   ones. The `When to use` section is a **User Story** (second-person scenario).
4. **Separate facts from judgment.** Label anything unverified `[未验证]` / `[推断]` — but keep inline
   labels to the load-bearing few (≤3 before the Caveats ledger; the linter WARNs above that) and
   collect every unverified fact as a bullet in the page's final `Caveats (unverified)` ledger. The
   most valuable section is `When NOT to use` — be concrete and honest, not nice.
5. In `Comparison`, name real substitutes. Mark ones not in the index `未收录`; link ones that are.
6. Add the project to its category `INDEX.md` **and** `INDEX.zh.md` (one-liner + comparison row).
7. Set `last_verified` to today; run `tools/lint.py` and `tools/reverse_index.py --check`
   (regenerate the committed `reports/` with `tools/reverse_index.py --write`).

## Updating / de-staling

Use the `sync-entry` skill (`.claude/skills/sync-entry/`): it re-verifies facts against the
live repo when an entry is older than the staleness threshold, and flags abandoned projects.

## Keeping the tree balanced

`categories/` is a recursive, self-balancing tree. When a leaf category exceeds `MAX_FANOUT`
(default 12) the linter WARNs — that's the signal to **split** it into sub-categories; thin or
overlapping categories should be **merged**. Use the `refactor-index` skill
(`.claude/skills/refactor-index/`): additive-first, `git mv` to preserve history, repairs links,
ends on a clean `tools/lint.py` + `tools/reverse_index.py --check`.

## Before you commit

```bash
python3 tools/lint.py
python3 tools/reverse_index.py --check
python3 tools/quality_scan.py --fail-on-gated
# or: make gates
```

Fix every ERROR. WARNINGs (e.g. staleness) should be addressed or explained. CI runs the same gates
on every PR (`.github/workflows/lint.yml`: `structural-lint` = lint + reverse-index check;
`quality-gate` = gated quality scan).

## Tone

Write for an agent that will *act* on what you say. No marketing. Date your facts. When you
don't know, say `[未验证]` — never guess in a way that reads as fact.
