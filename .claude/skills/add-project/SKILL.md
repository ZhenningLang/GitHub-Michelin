---
name: add-project
description: 当要把一个新开源项目加进本选型索引时使用；联网调研该项目，按 tools/schema.md 产出合规的选型页(frontmatter 事实 + type 自适应小节 + Caveats 存疑账本)，归类、更新分类 INDEX、跑 lint。不用于选型(用 select-oss)或刷新已有过期条目(用 sync-entry)。
argument-hint: <项目名 或 GitHub URL>
metadata:
  internal: true
---

# add-project

Author one conformant selection page. The contract is `tools/schema.md`; read it first.

## Procedure

1. **Gate on inclusion criteria** (AGENTS.md / schema §4 — keep the bar wide). The unit is a
   **git repository**. Add it if it is a real, non-empty open-source repo and not an exact
   duplicate of one already indexed — **across any domain, with no requirement that a substitute
   already exists in the index** (the `## Comparison` may cite `未收录` alternatives). Do not
   reject a valid long-tail repo for lack of in-index peers. Only stop if it is a non-repo (hosted
   SaaS, landing page, article, docs site), an exact duplicate, or contentless.

2. **Research live** — follow the `read-repo` skill's methodology (read order, how deep, how to mine
   the negative space). Fetch repo metadata (`gh api repos/<o>/<r>`: `created_at` for age/Lindy,
   `pushed_at`, `archived`, releases cadence, contributors for bus factor, `owner.type`), README,
   docs, the dependency manifest, and governance/LICENSE files. Separate **facts** (stars, license,
   language, deps, latest version, age — each dated) from **judgment**. Anything you can't confirm
   from a source → label `[未验证]` / `[推断]`, never assert it.

   **`[未验证]` is a last resort, not a convenience.** Before writing any unverified claim into a
   page, attempt verification with the tools at hand: `gh api` (metadata, issues, release/tag
   history), raw file reads from the repo tree (does the claimed config/benchmark/file actually
   exist? count it), package registries (npm/PyPI download numbers), the referenced external source
   itself (if a page claims a leaderboard position, fetch the leaderboard), and issue/PR bodies
   (what did the maintainer actually answer?). Classify each candidate claim:
   - *Verifiable now* → verify it, then write it as a dated fact (no label needed).
   - *Not verifiable without a reproduction environment* (author-reported runtimes/costs, AV
     verdicts, internal governance) → keep the label **and** state why it can't be checked.
   A Caveats ledger full of claims you never tried to verify is unfinished work.

3. **Classify.** Pick the single best **primary** category (= directory under `categories/`).
   Cross-cutting traits go in `tags`, not extra categories. Only create a new category if it
   genuinely doesn't fit — then also add a row to root `INDEX.md` **and** `INDEX.zh.md`.

4. **Write the bilingual pair** `categories/<category>/<slug>.md` (English) **and**
   `categories/<category>/<slug>.zh.md` (Chinese). All writing rules live in `tools/schema.md` —
   follow it, don't re-derive from memory. Checklist of its load-bearing parts:
   - **Frontmatter** (§1) — identical in both siblings, incl. the `upstream:` and `health:` blocks;
     `type` decides which H2 sections are required (§2 table). Each file is monolingual.
   - **When to use** — a User Story that defines the choice against substitutes (§2
     `"When to use" is a User Story`).
   - **When NOT to use** — the strongest section; each anti-pattern names a substitute (§2
     `"When NOT to use" names substitutes`).
   - **Comparison** — 3–5 real substitutes, `未收录` for unindexed ones; verdicts per §2
     `Verdict quality contract` (no template/vague verdicts).
   - **Close the loop on comparisons.** Every **real repository** named as a comparison
     alternative must itself get an entry in the same batch (its own bilingual page, wired into
     INDEX/README) — do not leave `未收录` dangling for something addable. `未收录` remains
     legitimate only for **non-repos** (closed SaaS like Runway, commercial NLEs, services) and
     for alternatives you explicitly justify as out-of-scope, with the reason recorded in the
     commit/PR summary. The obligation covers the 3–5 named direct substitutes, not transitive
     alternatives-of-alternatives.
   - **Health & viability** — required for all types; dated, labeled judgment per §7.
   - **Truth labeling + Caveats ledger** (§3) — inline labels only on the load-bearing few;
     everything unverified gets a ledger bullet.
   - **Chinese punctuation** in `.zh.md` (§6) — fullwidth next to 汉字; lint ERRORs on violations.
   Model the negative-space writing on the golden examples listed in §2.

5. **Wire it in.** Add the project to its `categories/<category>/INDEX.md` **and** `INDEX.zh.md`
   (one-liner + comparison-matrix row in each, including `Health` / `健康度`) **and to the README
   master listing** (`README.md` + `README.zh.md`). If new category, also add it to root `INDEX.md` +
   `INDEX.zh.md`. The linter ERRORs if a page is missing from its INDEX or from either README, so
   nothing drifts silently.

6. **Upstream snapshot.** Record the cheap stale-check snapshot before finishing:
   `python3 tools/upstream_snapshot.py --page categories/<category>/<slug>.md --apply --yes`.
   This writes the same `upstream:` block into both siblings; `sync-entry` uses it to skip full
   rereads when a stale page's upstream default-branch state has not changed.

7. **Health radar (automated — do not hand-grade).** Compute the 6-axis viability radar and embed
   its card:
   - `python3 tools/health.py --page categories/<category>/<slug>.md --write` — scores the repo from
     GitHub + package registries (via the authenticated `gh` CLI) and writes the identical `health:`
     block into **both** the `.md` and `.zh.md` frontmatter. Never hand-author the grades.
    - `python3 tools/health_card.py categories/<category>/<slug>.md categories/<category>/<slug>.zh.md`
      — regenerates both `assets/health/<slug>.svg` and `assets/health/<slug>.zh.svg` from that block.
   - Embed the card once in **each** page, right after the TL;DR line:
      `![<name> — health radar](../../assets/health/<slug>.svg)` (EN) /
      `![<name> — 健康度雷达](../../assets/health/<slug>.zh.svg)` (ZH).
   See `docs/health-rubric.md` for the rubric (A–E + `?`; `?` is first-class, never a low score).

8. **Validate.** Run structural lint, then run a scoped or changed-only quality scan for the pages
   just written:
   - `python3 tools/lint.py` — fix every ERROR before finishing.
   - Either scope the exact bilingual pair:
     `python3 tools/quality_scan.py --scope categories/<category>/<slug>.md --scope categories/<category>/<slug>.zh.md --fail-on-any-scoped`
   - Or, when the new pages are the relevant markdown changes in the worktree, use changed-only:
     `python3 tools/quality_scan.py --changed-only --fail-on-any-scoped`
   A scanner PASS is deterministic triage, **not semantic approval**. Before finishing, still read
   the Comparison verdicts, When NOT to use, and Caveats ledger for specific, true judgment.

## Quality bar

- Facts dated; judgment labeled. No marketing tone — write for an agent that will *act* on it.
- The page must answer "when should I NOT reach for this?" better than the project's own README.
- If you couldn't verify the basics (license, language, maintenance status), say so explicitly
  rather than guessing — a confident wrong fact routes an agent into a wall.
