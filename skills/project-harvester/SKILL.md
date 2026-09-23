---
name: project-harvester
version: 1.2.0
category: oss-atlas-maintainer
metadata:
  internal: true
  description: >
    Manually-triggered batch harvester for GitHub repositories. One trigger = one wave.
    Collects a batch of GitHub repos via search API, deduplicates against existing index,
    filters for software-project signals, and produces a classification report for review.
    Selected candidates are handed off to the add-project skill; this skill does not create pages.
---

# Project Harvester — Batch Discovery Skill

> One trigger = one wave. Scope → collect → dedupe → filter → classify → report → stop for review.

## Purpose

When the GitHub-Michelin index needs new entries, this skill automates the heavy lifting of
finding GitHub repos that are **not already indexed**, filtering out non-software resource
collections by default, and surfacing candidates with enough metadata to decide whether to add them.

## Prerequisites

- `GITHUB_TOKEN` or `GH_TOKEN` for authenticated GitHub API access. Without one, the script uses
  GitHub's lower unauthenticated rate limit.
- Python 3.9+ with standard library only (no pip deps needed for the harvester core).
- The GitHub-Michelin repo checked out locally at `{workspace}`.

## Supported Modes

| Mode | What it does | When to use |
|------|-------------|-------------|
| **Search** | GitHub Search API with an explicit domain query | You know the software domain to expand |
| **Wave** | Search → dedupe → filter → classification task → preliminary report | You want one auditable discovery wave |
| **Existing JSON pipeline** | Run `dedupe`, `filter`, `classify`, and `report` separately | You already have repository metadata in the harvester JSON shape |

`trending`, `backfill`, `create-page`, `--auto-create`, and `--git-commit` are not implemented by
`tools/harvest.py`; do not instruct users or agents to run them.

## Wave Workflow (Search Mode — default)

### Step 1: Select discovery directions

When the user names a software domain, task, or category, run one explicit domain-specific query.

When the user says only "run project-harvester", **do not ask them to choose a domain**. Read the
curated direction pool in `tools/harvest-directions.json`, randomly select 5 unique directions whose
categories exist in root `INDEX.md`, and run them as one aggregate wave. Record the random seed and
each candidate's source directions so the wave is reproducible and auditable.

Do not derive GitHub queries directly from category slugs. Slugs such as `im-automation` and `ocr`
are ambiguous in full-text search. The direction pool stores reviewed domain phrases such as
`"WeChat bot"` and `"optical character recognition"` to reduce semantic drift.

This automatic five-direction mode is the default because discovery is the harvester's job. Ask the
user only when an irreversible boundary decision remains after the report, such as creating a new
top-level category or adding selected repositories.

`discovery_directions` records search provenance, not the final taxonomy decision. The semantic
classification stage may place a candidate elsewhere when the search phrase matched a secondary
capability rather than the project's primary job.

For an explicit direction, build a domain-specific GitHub query:

```yaml
query_template: "topic:{domain} pushed:>2026-01-01"
per_page: 20           # GitHub API max = 100
min_stars: 0           # low-star real projects remain eligible
exclude_forks: true
exclude_archived: true
include_resource_collections: false
```

### Step 2: Collect raw candidates

Run the harvester core script:

```bash
cd {workspace}
python3 tools/harvest.py search \
  --query "topic:agent-governance pushed:>2026-01-01" \
  --per-page 20 \
  --output /tmp/harvest-wave-N.json
```

The script calls GitHub Search API (REST), returns a JSON array of repo stubs:

```json
[
  {
    "repo": "calesthio/OpenMontage",
    "html_url": "https://github.com/calesthio/OpenMontage",
    "stars": 28813,
    "forks": 3218,
    "language": "Python",
    "license": "AGPL-3.0",
    "description": "World's first open-source, agentic video production system...",
    "pushed_at": "2026-06-29T21:55:03Z",
    "created_at": "2026-03-29T15:23:22Z",
    "topics": ["ai-video", "video-production", "remotion"]
  }
]
```

### Step 3: Deduplicate against existing index

The harvester reads **all** existing `.md` files under `categories/`, extracts `repo:` from YAML frontmatter, and builds a dedup set. It then filters the candidate list:

```bash
python3 tools/harvest.py dedupe \
  --input /tmp/harvest-wave-N.json \
  --index-root categories/ \
  --output /tmp/harvest-wave-N-new.json
```

Output: only repos not already in the index.

### Step 4: Software-project filter

Apply a lightweight gate (no health.py yet — that comes later when creating the page):

```bash
python3 tools/harvest.py filter \
  --input /tmp/harvest-wave-N-new.json \
  --min-stars 0 \
  --exclude-archived \
  --exclude-forks \
  --output /tmp/harvest-wave-N-filtered.json
```

Quality signals checked at this stage (cheap, no extra API calls):
- `stars >= min_stars`
- `license != null` only when `--require-license` is explicitly passed
- `archived == false`
- `fork == false` (optional)
- `description` is non-empty
- resource collections are excluded by default: awesome lists, book lists, tutorial collections,
  interview-prep corpora, and similar learning/reference repositories

Use `--include-resource-collections` only when the user explicitly asks to discover those repository
types. Star count is not a quality gate for GitHub-Michelin inclusion; keep `--min-stars 0` unless the user
requests a popularity threshold.

### Step 5: Agent semantic classification (no keyword matching)

**This is the key step where a coding agent (LLM) performs classification, not an algorithm.**

The harvester generates a `classify-task.md` report containing:
- All candidate repos with their descriptions and topics
- All existing category definitions ("What belongs here")
- 1-3 example projects from each category

The agent reads the report, compares each repo to the category definitions by **semantic meaning**, and assigns the best fit. The agent can also read the full `categories/{cat}/INDEX.md` for deeper context.

```bash
python3 tools/harvest.py classify \
  --input /tmp/harvest-wave-N-filtered.json \
  --category-index categories/ \
  --output /tmp/harvest-wave-N-classify-task.md
```

The agent then reviews the task and applies classifications to the JSON file by setting `suggested_category` on each candidate. Possible answers:
- An existing category name (e.g., `agent-tooling`, `web-ui`, `dev-utilities`)
- `needs-new-category` — if no existing category fits
- `uncertain` — if the repo is too vague or niche to classify confidently

**Why agent-driven?** Keyword matching is unreliable — a project like "rust-lang/rust" (compiler) has no meaningful keywords in its description, and "tauri" (desktop framework with web frontend) could be miscategorized by any keyword heuristic. The agent understands *what the project actually does*.

### Step 6: Generate final report

After the agent has assigned categories, produce the final candidate report:

```bash
python3 tools/harvest.py finalize \
  --input /tmp/harvest-wave-N-classified.json \
  --output /tmp/harvest-wave-N-report.md
```

The report contains a table like:

| Repo | Stars | Lang | License | Suggested Category | Why |
|------|-------|------|---------|-------------------|-----|
| calesthio/OpenMontage | 28.8K | Python | AGPL-3.0 | video-production | AI video production, 12 pipelines, matches new category |
| ... | ... | ... | ... | ... | ... |

### Step 7: Human review (gate)

**STOP. The agent presents the report to the user.**

The user decides:
- **"Add all"** → proceed to Step 8 for all candidates
- **"Add #1, #3, #5"** → proceed for selected
- **"Skip this wave"** → discard, end
- **"Create a new category for #2"** → create category first, then proceed

### Step 8: Hand selected candidates to `add-project`

`tools/harvest.py` does not create pages. For each user-approved repository, invoke the repository's
internal `add-project` skill and pass the repo URL plus the reviewed category decision.

**Important:** The agent-generated body sections are **drafts**. The sub-agent must label unverified claims with `[未验证]` / `[推断]` and populate the `Caveats` ledger. Human review of the drafted pages is encouraged before final commit.

### Step 9: Verify

```bash
cd {workspace}
python3 tools/lint.py
python3 tools/reverse_index.py --check   # regenerate with --write and commit reports/ if it drifts
```

Fix any errors (missing INDEX entries, missing README rows, broken links, ASCII punctuation in `.zh.md` bodies, etc.).

### Step 10: Commit

```bash
git add -A
git commit -m "harvest: wave N — add K projects from {search_query}"
```

---

## Wave Size & Rate Limit Budget

| Resource | Budget per wave | Notes |
|----------|----------------|-------|
| GitHub Search API | 1 call per 100 results | Unauth: 10/min; Auth: 30/min |
| GitHub REST API (repo detail) | 1 call per candidate | Auth: 5000/hr |
| `health.py` | ~7-8 calls per repo | Auth: 5000/hr |
| `health_card.py` | 0 calls (offline) | SVG generation is local |
| LLM calls for page drafting | 1 per repo | Depends on provider |

**Recommended wave size: 10-15 repos.** This fits comfortably in a single hour's GitHub API budget and a 30-minute cron conversation timeout. Larger waves should be split into multiple manual triggers.

---

## One-Command Discovery Wave

Default automatic mode, with five directions selected from the root route:

```bash
cd {workspace}
python3 tools/harvest.py wave \
  --directions 5 \
  --per-page 5 \
  --min-stars 0 \
  --output /tmp/harvest-auto-wave.md
```

Use `--seed <n>` to reproduce a direction sample. Use `--query "..."` only when the user explicitly
requests a specific domain.

This stops after producing JSON, a classification task, and a preliminary report. Agent semantic
classification and human approval remain required before `add-project` runs.

---

## Caveats & Limits

- **Search scope controls the result more than filtering.** A generic language/high-star query will
  still produce generic repositories; always use a task/domain-specific query.
- **Resource filtering is heuristic.** Default filtering catches common awesome-list, book-list,
  tutorial, and learning-resource signals. It can produce false positives or miss unusual resource
  collections; inspect the report.
- **Classification is agent-reviewed.** `tools/harvest.py` generates a classification task but does
  not assign categories itself. Always review the final category decision.
- **Health scoring is as good as the data.** `health.py` needs `gh` auth. If rate-limited, some axes will be `?` — the page is still valid, but re-run `sync-entry` later to fill gaps.
- **Delegated page drafting is AI-generated.** After user approval, `add-project` synthesizes the
  selection page from upstream evidence. Review its `Caveats` ledger before committing.
- **Language detection is GitHub's.** Repos with mixed languages or mis-detected primary language may get wrong `language` frontmatter. Verify.
- **No dependency analysis.** The harvester does not clone repos or run dependency scanners. `Dependencies` and `Tech stack` sections are inferred from README mentions and may be incomplete.
