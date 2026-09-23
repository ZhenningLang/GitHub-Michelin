---
name: sync-entry
description: 当要刷新已有选型条目、对抗事实过期时使用；手动触发，按 last_verified 与今天的 delta 门控(超过阈值才真去联网重核),重核事实、更新变化项、bump last_verified,并对疑似废弃项目显著标注。不用于新增条目(用 add-project)或选型(用 select-oss)。
argument-hint: <项目 slug | 分类 | --all | --report>
metadata:
  internal: true
---

# sync-entry

Facts in this index are point-in-time snapshots. They rot. This skill is the **manual,
delta-gated** refresh: it only spends effort re-verifying entries that are actually stale.

## Staleness model

- Each page has `last_verified` (ISO date).
- `delta = today - last_verified`. Threshold = `STALE_DAYS`, default **90**
  (override via env `OSS_ATLAS_STALE_DAYS`; the linter uses the same value).
- `python3 tools/lint.py` already prints a **WARNING** for every entry past threshold — use that
  as the worklist.

## Modes

- **`--report`** — list entries sorted by `last_verified` (oldest first) with their delta.
  Run `python3 tools/lint.py` and read the staleness WARNINGs; or scan frontmatter dates.
  This is read-only; no fetching.
- **`<slug>` / `<category>` / `--all`** — re-verify the named scope. **Skip any entry whose
  delta ≤ STALE_DAYS** unless explicitly forced — do not waste a fetch on fresh entries. For stale
  entries, first run the cheap upstream probe below; only do the full reread when upstream changed.

## Cheap upstream probe for stale entries

For a stale page, do not immediately reread the whole repo. First compare today's upstream repo state
with the last recorded snapshot in the page frontmatter:

```yaml
upstream:
  pushed_at: 2026-06-29T00:00:00Z
  default_branch: main
  default_branch_sha: abc123
  archived: false
```

- If `upstream` is missing, do a full re-verify and write it.
- If `archived`, `default_branch`, or `default_branch_sha` changed, do a full re-verify.
- Treat `pushed_at` as a cheap hint, not the sole gate: GitHub updates it for non-default-branch
  pushes and tag/bot activity. The default-branch SHA is the stronger reread trigger.
- If the cheap probe matches the stored snapshot, skip the full **prose/fact reread** and report
  `unchanged_upstream`; do not silently bump `last_verified` as if prose/facts were reread.
- **`unchanged_upstream` does NOT skip the health re-score.** Maintenance/longevity are functions
  of elapsed time: a repo that goes quiet keeps the same `default_branch_sha` forever while its
  real grade decays from A toward D — the quiet case is exactly the one that needs re-scoring.
  Always run step 8 (re-score + regenerate cards) for a stale entry, even when upstream is
  unchanged. The scorer is cheap (a handful of API calls); `lint.py` warns when a page's
  `computed_at` exceeds `STALE_DAYS`.

Use the read-only compare mode for the probe:

```bash
python3 tools/upstream_snapshot.py --page categories/<cat>/<slug>.md --check
```

It prints `unchanged_upstream` or `changed_upstream`, writes nothing, exits `0` when unchanged and
`1` when changed. Only after a full re-verify should you refresh the stored snapshot with
`--apply --yes`.

## Re-verify procedure (per stale entry)

> **Bilingual:** each entry is a pair (`<slug>.md` + `<slug>.zh.md`) with **identical
> frontmatter**. Apply every fact/frontmatter change to both files, and update both bodies if a
> material fact moved. `last_verified` must match across the pair.

1. **Cheap upstream probe**: compare `upstream` frontmatter against GitHub repo state. If unchanged,
   skip steps 2–7 (prose/facts) but **still do steps 8–9** — health grades decay with elapsed time
   even when upstream is frozen.
2. **Refetch the source of truth**: GitHub repo page, latest release, README, last-commit date.
3. **Diff the facts** against frontmatter + body:
   - license, primary language, latest version / `maturity`, dependencies, tech stack.
   - star count (informational; not a gate).
4. **Update only what changed.** Keep the fact/judgment split; re-label `[未验证]` items if now
   confirmable (or vice versa).
5. **Abandonment check** — flag prominently in `## When NOT to use` if any hold:
   - archived / read-only repo, or no commits in ~12 months,
   - latest release far behind a moved-on ecosystem,
   - maintainer notice of deprecation.
   Treat single-maintainer / young projects as higher abandonment risk.
6. **Re-judge if facts moved materially.** A new major version can invalidate "when not to use"
   (e.g. a missing feature now exists). Don't just bump the date over stale judgment. If you touch `## Comparison` / `## 横向对比`, or if a material fact changes a comparison choice, follow
   `tools/schema.md` `Verdict quality contract`: each `Our verdict` / `我们的评价` cell must name the
   scenario, the choice, and the decisive tradeoff. Do not keep or introduce template verdicts such
   as `Use this page for its stated niche.` / `当前页用于它的主场景。` or vague claims such as `best`,
   `good choice`, or `open-source alternative`.
    **Callouts / 指指点点**: if the re-read produced leftover human judgment the template still
    cannot hold, write or refresh the section; if the leftover is gone or now fits a required
    section, delete the heading rather than leave an empty or duplicative bin.
    **How it works**: if the page has `flows/<stem>.json`, re-check every `code` value against the
   refetched README/source (renamed commands, new install path, removed APIs) and fix the spec +
   mechanism paragraph; then `python3 tools/flow_card.py <page>`. If the page lacks the section,
   add it per `tools/schema.md` while you have the sources open.
7. **Update `upstream` and bump `last_verified` to today.** Only after actually re-checking — never
   bump blindly.
   If the page is a **first-pass intake stub** (`quality_scan.py` reports it as `intake-stub-page`;
   its `When to use` describes picking software in general and Dependencies / Ops difficulty say
   "not exhaustively verified in this intake pass"), bumping the date without rewriting that prose
   turns it into a gated `intake-stub-page-reverified` ERROR. That is the point: a re-verified page
   may not still say nobody has looked. Rewrite those sections from the sources you just read.
8. **Re-score the health radar.** Health grades go stale like any
   fact — re-run the scorer when you re-verify:
   `python3 tools/health.py --page <page> --write && python3 tools/health_card.py <page>`
    This recomputes the 6 axes from live data, rewrites the identical `health:` block into both
    siblings (bumping its `computed_at`), and regenerates the card. See `docs/health-rubric.md`.
    Then re-project the new grade into the index rows — the `Health` / `健康度` cell in the
    category `INDEX.md`/`INDEX.zh.md` + READMEs is a machine projection of the page block, never
    hand-edited: `python3 tools/sync_index_health.py --apply` (lint.py ERRORs on any drift).
   The scorer prints a `grade changes vs previous block` diff to stderr — if any grade moved,
   reconcile the hand-written `## Health & viability` prose (both languages) with the new radar,
   and re-check the abandonment flag (step 5) when maintenance/overall dropped. This applies on
   the `unchanged_upstream` fast path too.
9. **Validate**: run structural lint, then run a scoped or changed-only quality scan for the pages
   updated in this sync:
   - `python3 tools/lint.py`.
   - `python3 tools/reverse_index.py --check` — regenerate with `--write` and commit `reports/` when
     the sync changed which alternatives a page names, or added/removed/renamed pages.
   - Either scope the exact bilingual pair:
     `python3 tools/quality_scan.py --scope categories/<cat>/<slug>.md --scope categories/<cat>/<slug>.zh.md --fail-on-any-scoped`
   - Or, when the updated pages are the relevant markdown changes in the worktree, use changed-only:
     `python3 tools/quality_scan.py --changed-only --fail-on-any-scoped`
   A scanner PASS is deterministic triage, **not semantic approval**. Before finishing, still read
   touched Comparison verdicts, When NOT to use, and Caveats for specific, true judgment.

## Discipline

- The date is a claim that *you verified the facts today*. Do not bump it without doing step 1–5.
- If a source is unreachable, leave the old date, add a `[未验证]` note on what couldn't be
  checked, and report it — don't fabricate a refresh.
- Report what changed: "synced N entries, U unchanged upstream, M facts updated, K flagged as abandonment-risk."
