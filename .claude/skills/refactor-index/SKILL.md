---
name: refactor-index
description: 当索引目录随项目增多变乱(分类失衡/重叠、项目错位、tag 不一致、对比矩阵过期、命名漂移)、需要重新整理分类结构时使用;诊断混乱信号→最小化且可追溯地搬动/合并/拆分→修链接→跑 lint。不用于新增项目(用 add-project)或刷新单条事实(用 sync-entry)。
argument-hint: <分类名 | --report | --all>
metadata:
  internal: true
---

# refactor-index

This index is only useful if an agent can **navigate** it. As entries accumulate, the *taxonomy*
rots — not the facts (that's `sync-entry`), the **structure**. This skill keeps the directory
navigable. A chaotic index defeats the project's entire purpose.

Division of labor:

- `sync-entry` fights **fact rot** (per-entry freshness).
- `refactor-index` fights **structural rot** (taxonomy health across the whole tree).

## Self-balancing tree (split / merge)

`categories/` is a **recursive tree**: a category node can hold project pages, child sub-categories,
or both. It is meant to **self-balance**:

- **Split (overflow).** When a leaf category exceeds `MAX_FANOUT` project pages (default 12;
  `OSS_ATLAS_MAX_FANOUT`), `tools/lint.py` prints an **overflow WARNING**. That is the automatic
  signal to split it into sub-categories along a natural axis (vendor, sub-domain, capability).
  The overflowing leaf becomes a **parent node** whose `INDEX` links the new child sub-category
  `INDEX` files; the pages move down into the children.
- **Merge (underflow).** Thin or overlapping sibling categories (each with a page or two, blurbs
  that blur) should be merged back up. This is a judgment call (lint won't force it).

Detection is automatic (the lint WARN); the restructure is run **here**, with the guardrails below.

## Chaos signals — what "混乱" means concretely

Gather these first (this is `--report` mode: observe, propose nothing, change nothing). Refactor
only what a signal justifies.

- **Category overflow/imbalance** — `tools/lint.py` WARNs when a leaf exceeds `MAX_FANOUT` (the
  primary split signal); or a category has sat at 1 page for a long time (candidate to merge).
  ```bash
  # pages per leaf category (recursive; portable — BSD/macOS find has no -printf)
  python3 -c "import collections,pathlib; c=collections.Counter(str(p.parent) for p in pathlib.Path('categories').rglob('*.md') if p.name not in ('INDEX.md','INDEX.zh.md') and not p.name.endswith('.zh.md')); [print(f'{n:4} {d}') for d,n in c.most_common()]"
  ```
- **Overlapping / near-duplicate categories** — two categories whose "what belongs here" blurbs
  blur together; an agent wouldn't know which to pick. Read every `categories/*/INDEX.md` tail.
- **Miscategorization** — a page whose primary category no longer fits better than another (read
  its `tags` + `## When to use`).
- **Tag drift** — the same concept spelled differently across pages (`gplv3` vs `gpl-3`,
  `on-device-llm` vs `on-device`).
  ```bash
  # recursive over the whole tree (categories/*/*.md only sees one level deep)
  grep -rh '^tags:' categories --include='*.md' | sed 's/tags: *\[//; s/\]//' | tr ',' '\n' | sed 's/^ *//' | sort | uniq -c | sort -rn
  ```
- **Stale routing** — a category `INDEX.md` one-liner or comparison-matrix row that no longer
  matches the page (project moved, renamed, or its when-not changed).
- **Naming drift** — slug/category not kebab-case (lint already flags `slug != filename` and
  `category != dir`).

## Refactor procedure — safe + traceable

Moving/renaming breaks links — do it in THIS order so `tools/lint.py` is your safety net at the end.

> **Bilingual:** every page is a pair (`<slug>.md` + `<slug>.zh.md`) and every category has both
> `INDEX.md` and `INDEX.zh.md`. Move/update **both** halves together, and keep the English INDEX
> linking `.md` pages and the Chinese INDEX linking `.zh.md` pages. The linter enforces parity.

### Splitting an overflowed category (the common rebalance)

1. Choose a **split axis** the entries cluster on naturally (vendor / sub-domain / capability), and
   2–5 child sub-category slugs. Don't force more children than the data supports.
2. `mkdir` each child dir; give each its own `INDEX.md` + `INDEX.zh.md` (with the "what belongs here").
3. `git mv` each page pair (`<slug>.md` + `<slug>.zh.md`) down into its child; update each page's
   `category:` to the **child** dir name; list it in the child's `INDEX.md`/`INDEX.zh.md`.
4. The overflowed dir becomes a **parent node**: its `INDEX.md`/`INDEX.zh.md` now link the child
   `INDEX` files (not pages). Keep its row in the grandparent/root `INDEX` files.
5. Lint — overflow WARN should be gone and 0 errors.

### Per-page moves (recategorize / merge)

For each justified move:

1. **`git mv`** the page to the new category dir (preserves history). Create the dir + a new
   category `INDEX.md` if it's a new category.
2. **Update the page frontmatter**: `category:` must equal the new parent dir name.
3. **Update routing**:
   - remove the row from the OLD category `INDEX.md` (and its comparison matrix); if the old
     category is now empty, remove the directory and its row in root `INDEX.md`.
   - add the row to the NEW category `INDEX.md` (one-liner + comparison-matrix row).
   - if categories were added/removed/renamed, update root `INDEX.md`.
4. **Fix cross-references** — grep for relative links to the moved file and repair them:
   ```bash
   grep -rn "<old-slug>.md" categories/ INDEX.md
   ```
5. **Normalize tags** if you touched tag drift: pick the canonical spelling and apply it across
   every affected page.
6. **Lint + refresh the reverse index** — `python3 tools/lint.py` must be **0 errors** before you
   stop. It catches orphans, dead links, `category != dir`, and missing INDEX files. Moves and
   renames also change the committed reverse index, so run `python3 tools/reverse_index.py --write`
   and commit `reports/` (`python3 tools/reverse_index.py --check` is what CI's `structural-lint`
   job runs).

## Discipline — don't make it worse

- **Additive-first.** Adding a category or moving a few pages is cheap. **Renaming or deleting a
  category is a one-way-door** — it breaks bookmarks, external links, and any agent that cached
  the path. Treat renames as high-cost: do them only when the old name is *actively misleading*,
  and call it out in the commit.
- **Minimal churn.** Every move must trace to a concrete chaos signal above, not aesthetic
  preference. A taxonomy that reshuffles every week is its own kind of chaos — an agent can't
  build intuition for a moving target.
- **One project = one leaf category.** Cross-cutting traits belong in `tags`, not a second
  category. Tempted to file a page under two categories? Fix the tags instead.
- **Split only when genuinely overloaded** (lint overflow WARN) and the split lines are obvious to a
  reader (not forced). Prefer a few well-separated children over many micro-categories.
- **Preserve git history** (`git mv`, never delete+recreate) so blame/log survive a move.
- **Commit the refactor on its own** (separate from content edits) so it is easy to review and revert.

## Stop criteria

- `tools/lint.py` is clean (0 errors) and `tools/reverse_index.py --check` is current.
- Every category's "what belongs here" is distinct from its siblings.
- No category is wildly imbalanced without a stated reason; no near-duplicate categories.
- Report what changed: moved / renamed / merged / split, and which links were repaired.

## Relationship to other skills

- `add-project` — if adding a project reveals there is no good category (or the obvious one is
  overloaded), run `refactor-index` first, then add.
- `sync-entry` — facts, orthogonal to structure.
- `tools/schema.md` — the per-page contract; `refactor-index` changes *where pages live*, not the
  page schema itself.
