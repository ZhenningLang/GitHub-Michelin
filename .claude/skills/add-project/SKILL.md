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
   - **When to use** — the trigger scenario that defines the choice against substitutes (§2
     `"When to use" is the trigger scenario`).
   - **How it works** — the mechanism paragraph only (§2 `"How it works" is the backbone user
     story`); its flow card is generated in step 5.
   - **When NOT to use** — the strongest section; each anti-pattern names a substitute (§2
     `"When NOT to use" names substitutes`).
   - **Comparison** — 3–5 real substitutes; status per §2 `Status vocabulary` — `未收录` means a
     real repository you did not add (debt), `非仓库` / `not a repo` means it is not a repository at
     all (hosted SaaS, closed app, paid service, article) and is out of scope by shape; verdicts per
     §2 `Verdict quality contract` (no template/vague verdicts).
   - **Close the loop on comparisons.** Every **real repository** named as a comparison
     alternative must itself get an entry in the same batch (its own bilingual page, wired into
     INDEX/README) — do not leave `未收录` dangling for something addable. `非仓库` is the status
     that closes a row without a page, and it is a factual claim about the alternative, not a
     preference: use it for closed SaaS like Runway, commercial NLEs, paid services and hosted
     APIs, and record the reason in the tradeoff cell. A repository you deliberately skip stays
     `未收录` with the reason in the tradeoff cell and in the commit/PR summary. The obligation
     covers the 3–5 named direct substitutes, not transitive alternatives-of-alternatives.
    - **Health & viability** — required for all types; dated, labeled judgment per §7.
    - **Q&A / 快问快答** — optional leftover bin (schema §2). After When to use, before How it works.
      Harvest the human's actual questions that the template has no slot for, and short versions
      of the agent's answers. Not a transcript. If nothing leftover, omit the heading. Uncertain
      claims still get a Caveats bullet. Golden example: `prime-agent`.
    - **Truth labeling + Caveats ledger** (§3) — inline labels only on the load-bearing few;
      everything unverified gets a ledger bullet.
   - **Chinese punctuation** in `.zh.md` (§6) — fullwidth next to 汉字; lint ERRORs on violations.
   Model the negative-space writing on the golden examples listed in §2.

5. **Backbone flow card (generated — do not hand-draw).** The `How it works` section's diagram is
   rendered from a spec; the contract is `tools/schema.md` §2 `"How it works" is the backbone user
   story`. Author it while the sources from step 2 are still open:
   - **Find the backbone in the sources, don't invent it.** The path is usually spelled out by the
     README quick start plus a real sample (`examples/`, `samples/`, `demo/`, the integration test,
     or the docs "getting started"). Keep the shortest path by which a developer gets the core
     value, and note who does each step — the project or the user.
   - Write `flows/<slug>.json` (stem = slug; category-prefixed only for a duplicated slug):
     two lanes (`you` / `them`), 3–9 **linear** steps, bilingual `en`/`zh` per step, a `value`
     payoff, and `sources` naming where each command/API was seen.
   - **Granularity** (schema §2 has the full rules): collapse generic setup (build/install/permission)
     into one step; stop at the step where the value lands — no inspection commands or optional
     features; if one lane runs 4+ steps in a row while the other is empty, you have a checklist, not
     a handoff. `code` is what the user types or writes, never an internal function/class name.
     **One backbone, not two paths**: a project enterable two ways (run-the-demo vs wire-it-in, a
     customer surface vs an operator surface) still gets one card — keep the path to the core value,
     move the other into the mechanism paragraph. **`phase`** (optional, ≤3, first step labeled) may
     label real lifecycle stages ("Build" then "Every turn"; write then recall) when the card would
     otherwise hide that boundary; it is a label, not a branch.
   - **Every `code` value must appear verbatim in a source you actually read.** If you cannot find
     the command/annotation/API, write the step generically ("call its query API") — an invented
     command inside a diagram reads as authoritative and is worse than no command.
   - Render + wire: `python3 tools/flow_card.py categories/<category>/<slug>.md` (does both
     siblings). Embed the card in each page inside `How it works`, right after the mechanism
     paragraph: `![<slug> — backbone user story](../../assets/flow/<slug>.svg)` (EN) /
     `![<slug> — 主干用户故事](../../assets/flow/<slug>.zh.svg)` (ZH), then re-run the command so it
     writes the generated text twin under the card. Never hand-edit that block.
   - Sanity-check the rendered SVG (`open assets/flow/<slug>.svg`): the lanes must read as
     "what I do" vs "what it does for me", and the value line must say what you no longer do.

6. **Wire it in.** Add the project to its `categories/<category>/INDEX.md` **and** `INDEX.zh.md`
   (one-liner + comparison-matrix row in each; put `—` in the `Health` / `健康度` cell — it is a
   machine projection filled in step 8, never hand-graded) **and to the README
   master listing** (`README.md` + `README.zh.md`). If new category, also add it to root `INDEX.md` +
   `INDEX.zh.md`. The linter ERRORs if a page is missing from its INDEX or from either README, so
   nothing drifts silently.

7. **Upstream snapshot.** Record the cheap stale-check snapshot before finishing:
   `python3 tools/upstream_snapshot.py --page categories/<category>/<slug>.md --apply --yes`.
   This writes the same `upstream:` block into both siblings; `sync-entry` uses it to skip full
   rereads when a stale page's upstream default-branch state has not changed.

8. **Health radar (automated — do not hand-grade).** Compute the 6-axis viability radar and embed
   its card:
   - `python3 tools/health.py --page categories/<category>/<slug>.md --write` — scores the repo from
     GitHub + package registries (via the authenticated `gh` CLI) and writes the identical `health:`
     block into **both** the `.md` and `.zh.md` frontmatter. Never hand-author the grades.
    - `python3 tools/health_card.py categories/<category>/<slug>.md categories/<category>/<slug>.zh.md`
      — regenerates both `assets/health/<slug>.svg` and `assets/health/<slug>.zh.svg` from that block.
    - Embed the card once in **each** page, right after the TL;DR line:
       `![<name> — health radar](../../assets/health/<slug>.svg)` (EN) /
       `![<name> — 健康度雷达](../../assets/health/<slug>.zh.svg)` (ZH).
    - Project the grade into the index rows written in step 6:
      `python3 tools/sync_index_health.py --apply` — it rewrites every `Health` / `健康度` cell in
      the category INDEXes + READMEs from the page frontmatter (the SSOT). Never hand-edit those
      cells; lint.py ERRORs on drift.
    See `docs/health-rubric.md` for the rubric (A–E + `?`; `?` is first-class, never a low score).

9. **Validate.** Run structural lint, then run a scoped or changed-only quality scan for the pages
   just written:
   - `python3 tools/lint.py` — fix every ERROR before finishing.
   - `python3 tools/reverse_index.py --check` — the new page changes the committed reverse index;
     if it fails, run `python3 tools/reverse_index.py --write` and commit the regenerated
     `reports/` in the same change (CI's `structural-lint` job runs this check).
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
