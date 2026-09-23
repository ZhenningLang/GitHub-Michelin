# OSS HEALTH Rubric — 6-Axis JoJo Stand-Stats Spec (implementation-ready)

> **Implementation notes (deviations from this spec, applied in `tools/health.py`):**
> 1. The responsiveness GraphQL query uses `issues(first:60 …DESC)`, not `last:60` — `last:N` on a
>    DESC connection returns the *oldest* issues, the opposite of the 90-day-window intent.
> 2. The "first response" rule excludes the issue **author's own** label/assign/close events (not
>    just their comments) — otherwise a reporter self-labeling at t=0 fakes TTFR≈0.
> Both verified against live data; see the scorer's header comment.

> **Status:** LOCKED design. This document is the SSOT for the Python scorer + SVG generator.
> **Population:** 229 EN project pages (the `.zh.md` sibling carries identical frontmatter; score the EN page, write the same `health:` block to both).
> **Auth:** A GitHub PAT is **mandatory** for the whole pipeline (unauthenticated 60/hr dies at ~repo 15). All `auth_needed:true` calls assume `Authorization: Bearer $GITHUB_TOKEN`.
> **Date semantics:** all "as of" computations use the **run timestamp** (`now`, UTC). Persist it.

---

## 0. The Stand: six hexagon vertices

A project is rendered as a hexagon radar (JoJo-stand-stats *visual style* only — no Stand vocabulary). Six axes, each graded **A / B / C / D / E** or **`?`** (unknown — first-class, never coerced to a grade). Filled tier-colored polygon; `?` axes render as a dashed/gray ghost spoke and are **excluded from area**.

**Label orientation: every axis is phrased so MORE = BETTER**, matching the radar (fuller = healthier). No negative-semantics labels (e.g. "risk", "single-point dependency") that would invert against the chart.

| # | Axis key | EN label | ZH label | One-line meaning (positive direction) |
|---|----------|----------|----------|---------------------------------------|
| 1 | `maintenance` | Maintenance | 维护活跃度 | Still alive and shipping on the default branch right now. |
| 2 | `responsiveness` | Responsiveness | 响应速度 | A human notices filed issues quickly. |
| 3 | `adoption` | Adoption | 采用广度 | Reach into the dependency graph / install base (downloads + dependents). |
| 4 | `longevity` | Longevity | 长青度 | Old AND still active — proven survival (Lindy), never age alone. |
| 5 | `governance` | Bus Factor | 维护者分散度 | Work is spread across enough people to survive the busiest one leaving. |
| 6 | `risk_license` | Permissiveness | 许可宽松度 | License is permissive / safe to embed long-term (no relicense / source-available trap). |

**Rejected alternative (do not implement):** *Momentum / 成长势头* (trailing-90d commit-acceleration ratio). Dropped because it double-counts Maintenance (its `curr90=0 → E` and `pushed_at≤45d` gates are pure liveness), its newcomer-inflow corroborator is structurally unobservable for >100-contributor repos (GitHub caps `stats/contributors` at top-100 by lifetime total), and acceleration mis-scales for the index's solo/skill-pack-heavy makeup. Its one survivable idea — *release recency* — is folded into Maintenance's optional A-confirm. **6A = Risk/License is the 6th axis.**

---

## 1. Cross-cutting rules (apply to every axis)

### 1.1 Repo type (from frontmatter `type:`)
Every page already carries `type ∈ {library, framework, tool, app, service, skill-pack, model}`. Type drives several carve-outs below. Measured EN-page distribution (from verifier counts, treat as approximate, re-derive at runtime): library ~64, tool ~57, skill-pack ~42, app ~34, framework ~25, model ~4, service ~3.

### 1.2 `?` is first-class, never silently coerced
`?` means **"the spine signal for this axis could not be obtained."** It is NOT a low score. A scorer MUST NOT map `?`→E, `?`→A, or `?`→0 in any aggregate. Every `?` carries a machine-readable `reason` code (enumerated per-axis). `?` axes are excluded from polygon area and from the overall grade (§3), but stay in the coverage denominator — the reader should see that something is missing.

**An axis that is structurally inapplicable to a type is `N/A`, not `?`** (added 2026-09; see §2.3c). The two were one value until then, which told the reader "unknown" in both cases and hid which one they were looking at. `N/A` leaves the denominator as well, since counting a question the artifact cannot be asked would understate its real coverage.

### 1.2b A failure must never be able to look like a measurement

This scorer runs unattended over 600 pages and writes its output straight into them. A grade that
came out of a broken fetch is indistinguishable, on the page, from one that came out of a real
one — nobody reads 600 radar cards looking for a number that is subtly wrong. So every path that
reads a number carries an obligation: **failure must be a different type from a measured value, and
that difference must survive all the way to the page.**

Ten violations of this shape were found and fixed in a single session in 2026-09. Three of them are
representative:

| Violation | What the page would have said |
|---|---|
| An exhausted GitHub rate limit returned 403, which the axis functions degrade to `?` | Hundreds of real grades overwritten with "unmeasurable", mid-batch, silently |
| The Homebrew index cache stored an empty dict when the fetch failed | Every Homebrew lookup for the next 24h returns "not in Homebrew" |
| A calibration fetch swallowed its timeout and reported zero downloads | The largest projects drop out of the sample that sets the anchors |

The rules that follow from it, enforced in `tools/health.py`:

1. **Never cache an empty result.** A transport failure and a genuinely empty index produce the
   same `{}`; persisting it serves the failure as a fact for the whole TTL.
2. **Wait out a rate limit, do not degrade through it.** `gh_api` parses `x-ratelimit-remaining`
   and `x-ratelimit-reset` and blocks until the window resets rather than handing the axis a 403.
3. **Retry transport failures before concluding absence.** A blip on a registry lookup is
   otherwise indistinguishable from "this project has no package" — that is how playwright, with
   323M monthly npm downloads, came to carry `?`.
4. **Distinguish "could not identify" from "identified, no counts".** `ambiguous` and
   `registry_no_counts` are different findings and route to different fixes.
5. **`?` and `N/A` are different claims.** See §2.3c.

When a check cannot satisfy this, it does not ship: a signal we cannot trust to fail loudly is
worse than no signal, because it spends the reader's trust on noise.

**These rules are not self-enforcing.** The same session that wrote them down broke them again
several times afterwards, which is evidence that a written rule is not a control. Two of them are
now machine gates in `tools/lint.py`, checked on every page on every run and covered by tests in
`tools/test_lint.py`:

| Gate | Rejects | The bug it closes |
|---|---|---|
| adoption `E` must carry a number in one of `dependent_repos_count`, `downloads_last_month`, `homebrew_installs_90d`, `release_downloads`, `docker_pulls` | an `E` whose evidence is all `null` | 39 pages scored `E` when the scorer had matched no package at all — "found nothing" served as "measured zero". A *measured* zero still passes; only the absence of a number fails |
| `canonical_package` must name-match the repo or be scoped to its owner (re-checked offline with the scorer's own `_match_quality`) | a package that cannot be shown to be this repo | `crates.io/waza` (a reserved name owned by someone else) attached to `tw93/Waza`; `npmjs.org/d2` (DHIS2's library) to `d2lang/d2`; `digitalbanking` reported as jaeger's package |

A gate that never fires is worse than no gate — this repo shipped a `?` warning that silently
matched nothing across 600 pages. So each gate has a test asserting it fires *through the normal
lint entry point*, not just when called directly.

The same principle applies to tools that rewrite pages, not only to those that measure them.
`tools/sync-health-to-body.py` rewrites one body section; it used to scan forward to a hardcoded
next header, so it swallowed any section in between and, on a page without that header, replaced
the whole tail of the file. It now stops at the next H2 of any kind, refuses to write when the set
of H2 headings would change, and requires an explicit `--overwrite-prose` for `--all`, because
`--all` replaces hand-written analysis with generated one-line-per-axis text.

### 1.3 Bot / AI-agent author filter (shared by maintenance, governance, momentum-derived signals)
When counting *human* authors or commits, drop authors whose `login` (or, if null, `commit.author.email` local-part) matches:

```
/(\[bot\]$)|(^dependabot)|(^renovate)|(-bot$)|(^github-actions)|( bot$)|(^mergify)|(^release-please)|(^pre-commit-ci)/i
```

plus known AI committers: `claude`, `ampagent`, `devin`, `cursor-agent`, `copilot`, `sweep-ai`. **Known limitation [推断]:** a denylist on free-text logins is leaky in both directions (a human-named service account like `ci-deploy` passes; a real maintainer whose login contains "bot" is wrongly dropped). Document this; do not claim it is exhaustive.

### 1.4 committer date, not author date; default branch only
Recency uses `commit.committer.date` on the **default branch** (resists back-dated authorship; `pushed_at` fires on any branch/tag/bot push and is NOT used as a recency spine anywhere). `created_at` is server-assigned and forgery-resistant; used for age.

### 1.5 Determinism
Same inputs → same grade. No randomness in tier assignment. The only stochastic element is the *anti-window-gaming sampling offset* for responsiveness (§2.2), which is seeded and recorded so a re-run is reproducible.

---

## 2. The six axes — exact thresholds, `?` rules, data sources, gameability

For all axes: **radius mapping is uniform** — A=1.0, B=0.8, C=0.6, D=0.4, E=0.2, `?`=excluded-from-area dashed/gray at neutral 0.5 (see §5).

---

### 2.1 `maintenance` — Maintenance / 维护活跃度 — Power / 破壊力

**Spine:** days since last default-branch commit + a *velocity-robust liveness* check (presence across weeks, not absolute volume). Release cadence is **NOT** part of this axis (moved out — it was longevity/momentum bleed). Archived/disabled is an E override (acknowledged to correlate with the risk axis by construction; do not treat the correlation as independent confirmation).

**Inputs**
- `archived`, `disabled`, `default_branch`, `created_at` from the core repo object.
- `last_commit_age_days` = `now − commits?per_page=1 .[0].commit.committer.date`.
- `active_weeks_13` = number of the last 13 ISO weeks with ≥1 commit, from `stats/participation .all[-13:]` (count of nonzero entries — **shape, not sum**, so a 5-commit/quarter stable lib and a 400-commit churner are judged on *presence*).

**Exact tiers** (evaluate top-down; first match wins)

| Tier | Condition |
|------|-----------|
| **E** | `archived==true` OR `disabled==true` OR `last_commit_age_days ≥ 730` OR repo is a redirect/tombstone (README "moved"/redirect). |
| **A** | NOT archived/disabled AND `last_commit_age_days < 30` AND `active_weeks_13 ≥ 6` (committed in ≥6 of last 13 weeks — sustained presence). |
| **B** | NOT archived/disabled AND `last_commit_age_days < 90` AND `active_weeks_13 ≥ 2`. |
| **C** | NOT archived/disabled AND (`90 ≤ last_commit_age_days < 365`) OR (`last_commit_age_days < 90` AND `active_weeks_13 < 2`, i.e. a lone recent commit, no sustained activity). |
| **D** | NOT archived/disabled AND `365 ≤ last_commit_age_days < 730`. |

**Mature-library Lindy carve-out (overrides C/D up to one tier):** if `type ∈ {library, framework}` AND `repo_age ≥ 3y` AND NOT archived AND `last_commit_age_days < 365`, then a low-cadence result that would land **C/D purely on low `active_weeks_13`** is lifted to **B** (a finished, correct, rarely-touched old library is "done", not "coasting"). The carve-out never lifts a repo whose last commit is ≥365d.

**`?` rule** (checked only when the spine is unreadable)
- `repo_404_or_private` — core repo object 404s / private / moved without resolvable redirect.
- `empty_repo` — `/commits` returns 409 "Git Repository is empty" (no commits — distinct from abandoned).
- `recency_unreadable` — `stats/participation` still 202s after 3 retries AND `/commits?per_page=1` also fails (rate-limited/transient).
- A missing **release** signal is NEVER `?` here (release is not on this axis). Archived flag ships in the core object and is almost never `?`. Expected `?` rate <2%. Re-runs retry `?` next cycle.

**Data source / exact calls**
```
gh api repos/{owner}/{repo} --jq '{archived,disabled,fork,default_branch,created_at,pushed_at}'
gh api 'repos/{owner}/{repo}/commits?per_page=1' --jq '.[0].commit.committer.date'
gh api repos/{owner}/{repo}/stats/participation --jq '.all'    # 52 weekly ints; 202 on cold cache → retry ≤3 w/ backoff
```
Fallback when `stats/participation` stays 202: `gh api 'repos/{o}/{r}/commits?since={now-91d ISO}&per_page=1' -i` and read `rel="last"` page number from the `Link` header (no Link header ⇒ 0–1 commit; disambiguate with a `per_page=1` body-length check). Derive a coarse `active_weeks_13` proxy only if needed.

**Gameability resistance**
- pushed_at bot/gh-pages spoofing → resisted (we read default-branch committer date, never pushed_at).
- One cosmetic commit every 89d → lands **C** (fails `active_weeks_13 ≥ 2`).
- committer.date spoofing on the single latest commit is cheap (one cron with `GIT_COMMITTER_DATE`); **mitigated** because A/B both require the histogram *shape* (`active_weeks_13`), not a single timestamp. **Residual [推断]:** a curated index sharing one owner across many repos could run one scripted commit/cron to green-light recency on all of them; the `active_weeks_13` floor blunts but does not fully stop a sustained cron — disclose, do not claim "prevents".
- Un-archive to dodge E → un-archiving is a deliberate liveness act; correct to re-grade on recency.

---

### 2.2 `responsiveness` — Responsiveness / 响应性 — Speed / スピード

**Spine (PURE latency):** median time-to-first-response (TTFR) on issues **opened in a 90-day window**. First response = earliest of {first non-author, non-bot comment | first label | first assignment | close}. **Close-rate, PR-merge-rate, and pushed_at have been REMOVED from the tier logic** (they were momentum/maintenance double-counts). Tiers are set by median TTFR **alone**, with type-aware bands.

**Window-gaming defense:** sample the 90-day window at a **seeded random offset** of 0–13 days before `now` (record the seed + offset in the YAML), or compute a trailing continuously-updated median, so just-in-time acking of a predictable cron snapshot can't be timed.

**Qualifying-issue & first-response hardening**
- An issue qualifies if `createdAt` ∈ window AND author is human.
- A "first response" comment is excluded if its author matches the bot regex (§1.3) **OR** its body is a near-duplicate template across the window (shingle/Jaccard similarity ≥ 0.8 to another first-response in the window) — defeats a human-named auto-ack service account. **Documented as best-effort heuristic, not a guarantee.**
- If the qualifying issue sample is <3, PR review/comment response is used as a fallback signal. PR fallback uses the same sample floors as issues: default A still requires ≥5 qualifying responses; B requires ≥3. The persisted `qualifying_issues` raw field is historical: when `source: pr`, it means qualifying PRs.

**Exact tiers** (type-aware bands; bands chosen to fit this index's solo-tool / skill-pack makeup, not a Western team-OSS SLA)

Default bands (library, framework, service):

| Tier | Condition (median TTFR over window) |
|------|-------------------------------------|
| **A** | median TTFR < 48h AND ≥5 qualifying issues. |
| **B** | median TTFR < 7d AND ≥3 qualifying issues. (ceiling if 3–4 issues) |
| **C** | median TTFR < 30d. |
| **D** | median TTFR ≥ 30d AND < 180d. |
| **E** | median TTFR ≥ 180d, OR zero non-author/non-bot responses to ANY of the last ≥10 issues each opened >30d ago. |

Relaxed bands for `type ∈ {tool, app}` (solo / hobby cadence is healthy, not "unreliable"): **A** <7d, **B** <30d, **C** <90d, **D** ≥90d & <365d, **E** ≥365d (or the zero-response clause). `archived==true` forces **E** for any type.

**`?` rule** (checked BEFORE A–E — it is a gate)
- `issues_disabled` — `hasIssuesEnabled == false`.
- `no_traffic` — <3 issues AND <3 PRs opened in trailing 365d (empty denominator — absence of demand, not slow).
- `no_window_signal` — traffic exists in the trailing year, but the seeded 90-day sample has no qualifying issue or PR response. This is unknown, not a fabricated slow-response grade.
- `too_young` — repo `created_at` < 180d AND thin traffic (distinct from `no_traffic`; youth never reads as E or as a strength).
- `type_na` — `type ∈ {skill-pack, model}` (canonical contribution channel is not issues/PRs).
- `github_unavailable` — the GraphQL call or repository node is unavailable; this is a tool/data-source failure, not evidence of no traffic.
- `mirror` — read-only mirror / PRs disabled with issues empty.
- `vendor_support_elsewhere` — issues enabled but ignored *by policy* (vendor drop). If "ignored by policy" cannot be distinguished from "ignored by neglect," route to `?`, **not E**.

**Data source / exact calls** (1 GraphQL/repo; close-rate counts, if ever needed for tooltips, are derived from the SAME issue page — no separate Search calls)
```
POST https://api.github.com/graphql
query($o:String!,$n:String!){ repository(owner:$o,name:$n){
  hasIssuesEnabled isArchived createdAt
  issues(first:60, orderBy:{field:CREATED_AT,direction:DESC}){ nodes{
    number createdAt closedAt author{login}
    comments(first:5){nodes{createdAt author{login} bodyText}}
    timelineItems(first:10, itemTypes:[LABELED_EVENT,ASSIGNED_EVENT,CLOSED_EVENT]){
      nodes{__typename
        ... on LabeledEvent{createdAt actor{login}}
        ... on AssignedEvent{createdAt actor{login}}
        ... on ClosedEvent{createdAt actor{login}}}}
  }}
  pullRequests(first:30, orderBy:{field:CREATED_AT,direction:DESC}){ nodes{
    createdAt author{login}
    reviews(first:10){nodes{createdAt author{login}}}
    comments(first:10){nodes{createdAt author{login}}}
  }}
}}
# in code: keep issues with createdAt in the offset 90d window; TTFR_i = min(first non-author/non-bot comment, first label, first assign, close) − createdAt; if issue sample is <3, use PR review/comment response as the fallback signal; report median and source.
```

**Gameability resistance**
- Stale-bot auto-close inflating close-rate → irrelevant (close-rate is no longer a tier gate).
- Acknowledgment-bot via human-named service account → blunted by the near-duplicate-template exclusion (best-effort).
- Backdated burst clearing old backlog → defeated (window measures latency on *newly opened* issues).
- Just-in-time acking of the current window → blunted by the seeded random offset.
- Issue suppression → routes to `?` (dashed/gray), cannot fake a green axis.

---

### 2.3 `adoption` — Adoption / 采用度 — Range / 射程距離

**The fix that matters:** `rankings.downloads` from ecosyste.ms is **NOT** a 0–1 percentile (verified live: instructor=1.90, dspy=15.13, `None` for crewai/very-popular pkgs, flask=0.0106 fails its own A bar). **Do not use it as the ranker.** Use **`dependent_repos_count` as the PRIMARY structural signal** (it works for npm/PyPI/crates/Go/Maven in live tests) and **absolute last-month downloads vs per-registry anchor tables** as the co-signal. Tier = **max(graph_tier, volume_tier)**; **persist both sub-scores** so the conflation is auditable (a high-volume-zero-dependents app-package and a low-volume-foundational lib must not silently collapse to the same number).

**Canonical-package selection (THE single most important anti-gaming rule):** `packages/lookup?repository_url=` returns typosquats/forks/mirrors (flask buried at position 6 behind `falask`, `flasl`). Pick canonical = the entry with the **strongest claim to be this repo**, then max `.downloads`, with a `downloads >= 1000` noise floor. Claim strength, best first:

1. `.name` fuzzy-matches the repo name (scoped names are matched on the bare name too, so `@playwright/test` matches `playwright`).
2. The package is **scoped to the repo's owner** (`@mui/material` for `mui/material-ui`). Monorepos publish under a scope where no single package carries the repo's name; without this rule they look unpackaged.
3. Neither — accepted only when nothing else clears the noise floor.

**`proxy.golang.org` entries are excluded from the pool whenever any non-Go candidate exists.** The Go proxy synthesizes a module named `github.com/{owner}/{repo}` for *every* GitHub repo regardless of language, so its name always contains the repo name and always wins a substring match. Live consequence: `mui/material-ui` selected its 2-dependent Go pseudo-module over npm packages carrying 154k dependents and scored **D instead of A**. Real Go projects are unaffected — they reach the same number through the pkg.go.dev importers fallback below.

**Only the project's own distribution channel can be canonical.** ecosyste.ms indexes 100
registries and most repackage other people's software. Candidates are filtered to an **allowlist of
primary ecosystems** (`npm, pypi, cargo, rubygems, packagist, maven, nuget, go, hex, pub, cocoapods,
cran, cpan, clojars, hackage, luarocks, elm, julia, swiftpm, deno, bower, dub, vcpkg`), keyed on the
candidate's `registry.ecosystem` rather than its name — registry names are version-suffixed
(`alpine-v3.19`, `alpine-edge`, `nixpkgs-24.11`, `ubuntu-23.10`) and a name-based denylist is
unmaintainable. Mirrors of a primary registry (`gem.coop`) and redistribution channels
(`conda-forge.org`, `anaconda.org`, `formulae.brew.sh`, `spack.io`) are excluded too: right
ecosystem, wrong copy. When nothing primary remains, a repackaged candidate is accepted **only if it
carries a real count**, since for some projects it is the only number that exists; a distro entry
with neither downloads nor dependents is pure noise in the `registry:` field.

Live consequences before this rule: `gem.coop` beat rubygems.org for **selenium** (345,857,423
downloads/month), **asciidoctor** and **loki** — all three scored **E**; `conda-forge.org` beat the
project's own registry for **pandoc**, **ripgrep**, **jq** and **FreeCAD**; and an Alpine build
(`jq-dev`) was reported as jq's canonical package.

**An unlisted registry no longer discards the download figure.** `volume_tier_from_downloads`
returned `None` for any registry missing from the anchor table, and the count was dropped entirely —
selenium's nine-figure monthly downloads vanished and the page scored its dependents-only tier, E.
**20 pages** carried a silently-dropped count this way. Unlisted registries now fall back to a
default anchor row; an approximate tier beats throwing the measurement away.

**The `rank != null` condition is withdrawn (2026-09).** ecosyste.ms now returns `rank: null` for every candidate of every repo probed (flask 18/18, playwright 100/100, material-ui 83/83), so the filter dropped 100% of candidates and every lookup fell through to the fallback branches — it had stopped doing anything years before anyone noticed. The typosquat defense never rested on it: flask's squatters either fail the name match (`f-ask`) or lose max-downloads by seven orders of magnitude (`flask-mirror-upstream`, dl=17 vs 133M).

**Secondary discovery by package name.** ecosyste.ms builds its repo→package mapping by scraping manifests and the mapping has a long tail of gaps; a gap there is not evidence of an unpackaged project. When the `repository_url` lookup yields nothing usable, retry by **name** against `registries/{registry}/packages/{name}`, trying the repo name and its language-suffix-stripped variants (`elasticsearch-dsl-py` → `elasticsearch-dsl`). A hit is accepted only when the package's own `repository_url` points back at a repo of the same name; the owner is deliberately not required to match, because org renames leave the old owner in ecosyste.ms's record.

**Transport failures are retried.** A blip on the lookup is otherwise indistinguishable from "no package exists", and `registry_lookup_failed` then masquerades as missing adoption data. Observed live before the retry existed: playwright (323M monthly npm downloads), material-ui, chakra-ui and radix-ui all carried `?` on this axis.

**Per-registry absolute anchors** (for `volume_tier`):

| Tier | npm last-mo | PyPI last-mo | crates recent | RubyGems/Packagist mo | Go (importers) | dependent_repos_count |
|------|------------|--------------|---------------|------------------------|----------------|------------------------|
| **A** | ≥5,000,000 | ≥2,000,000 | ≥1,000,000 | ≥500,000 | ≥10,000 | ≥10,000 |
| **B** | ≥500,000 | ≥200,000 | ≥100,000 | ≥50,000 | ≥1,000 | ≥1,000 |
| **C** | ≥50,000 | ≥20,000 | ≥10,000 | ≥5,000 | ≥100 | ≥100 |
| **D** | >0 below C floor | >0 below C | >0 below C | >0 below C | >0 below C | 1–99 |
| **E** | <1,000 | <1,000 | <500 | <500 | 0 importers | 0 |

**Exact tier rule**
1. `graph_tier` from `dependent_repos_count` column (Go uses pkg.go.dev importers mapped to the same column; Maven uses ecosyste.ms `dependent_repos_count`).
2. `volume_tier` from absolute downloads vs the matching registry column. If `downloads`/`rank` is `None`, `volume_tier = ?` (fall back to graph, NEVER force E).
3. **tier = max(graph_tier, volume_tier)** (A best).
4. **E guard:** E only if `dependent_repos_count == 0` AND `downloads < E-floor` (AND on both). A `None` download value never forces E.
5. GitHub "Used by" scrape is **soft evidence only** (the scrape failed live / anti-bot); never a tier driver.

**Mandatory cross-check (cheap, ~30–60 extra calls):** for every **A or B** result, hit the direct registry API and flag `>2×` divergence from ecosyste.ms for human review (field unreliability makes this non-optional, not "borderline-only").

### 2.3b Install signals — the channel a project's users actually take

A registry download count answers "how many projects install this" only for artifacts that
ship to a language registry. An IDE, a database server, a desktop app or a CLI binary is adopted
just as measurably; its trace is simply somewhere else. Through 2026-09 this scorer reported those
as `?` — 273 of 600 pages (45%) — which stated a gap in our instruments as a gap in the project.

| Instrument | Source | A | B | C |
|---|---|---|---|---|
| GitHub release asset downloads (cumulative) | `repos/{o}/{r}/releases?per_page=100`, summing `assets[].download_count` | ≥10,000,000 | ≥1,000,000 | ≥100,000 |
| Homebrew installs, trailing 90d | `formulae.brew.sh` `formula.json` + `cask.json` joined to `analytics/install/90d.json` | ≥3,000 | ≥500 | ≥100 |
| Docker Hub pulls (cumulative) | `hub.docker.com/v2/repositories/{ns}/{name}` — **`type: service` and `type: app` only** | ≥100,000,000 | ≥10,000,000 | ≥1,000,000 |

**Measured for every project, not only for those with no package.** Having a registry package does
not mean the registry is where the project's users get it. Binary-first tools keep a token package
and ship through releases: `jq` read as a minor package and scored **D** while 295M people pulled
its binaries; `ripgrep` **D** against 53M; `pandoc` **B** against 40M; `ImageMagick` and `ComfyUI`
**E**. The axis therefore takes `max(registry_tier, install_tier)`, the same max() the registry path
already applies across its own two sub-signals, and records `tier_source` so the page says which
channel decided.

This cannot inflate a registry-first project, and the symmetric evidence is what shows it: angular
publishes 24.6M npm downloads a month against **324** release-asset downloads, ray 276, faker 716.
A channel a project does not use reports nothing, and `max()` with nothing is unchanged.

#### Why the anchors are channel-relative, not absolute

**The two kinds of channel do not measure the same users, and there is no ground truth to calibrate
one against the other.** Measured over 138 projects carrying both numbers: Spearman correlation
between release-asset downloads and registry downloads is **0.124**; against `dependent_repos_count`,
**0.002**. Grouping by registry-derived grade gives medians that are not even monotonic (A 86k,
B 32k, C 8.8k, D 98k, E 31k release downloads). Neither channel is the truth the other should be
scaled to; each sees the slice of users that came its way.

So a letter here means **top decile / quartile / half of the channel this project actually ships
through**, and nothing stronger. Populations used:

- **Releases** — the 270 repos in this index that publish release assets (no global GitHub
  population is obtainable). p90 12.7M, p75 907k, p50 72k, rounded to the table above.
- **Homebrew** — Homebrew's own 7,900 formulae and casks, the channel's true global population.
  p90 3,000, p75 406, p50 83. Note this index's projects sit high in that distribution by
  selection, so most of the 32 with Homebrew data land A or B. Homebrew analytics also counts only
  opted-in users, which understates every absolute figure — a percentile is invariant to that
  scaling, which is a further reason to prefer it here.
- **Docker** — no enumerable population, so these anchors stay absolute and are the weakest of the
  three. `pull_count` is cumulative and CI-inflated (envoy alone reports 5.76e9).

A consequence to be honest about: a Homebrew-derived A and an npm-derived A are **not** the same
amount of adoption. `signal_basis` and `tier_source` are on every page for exactly this reason, and
no aggregate should be read as comparing them.

**E is unreachable through this path**, unlike the registry path. The evidence is asymmetric: a
large install count proves adoption, a small one does not disprove it, because the channel we can
read may not be the channel its users take. A tool distributed mainly by `git clone` or a
curl-to-shell script can show a handful of release-asset downloads while being widely used; calling
that E would assert "measurably unadopted" from a number that never measured the main path. The
registry path keeps E because there the registry **is** the distribution channel. Floor here is D.

#### Attention is not adoption, and is not used

Star count was evaluated as a fallback and rejected on this index's own data: across the 268 pages
with a measured adoption grade, Spearman correlation between stars and that grade is **0.125**,
against `dependent_repos_count` **0.065**, against `downloads_last_month` **0.007**. Five-tier exact
agreement is 12%, below the 20% random assignment would give. In an index weighted toward AI/agent
tooling — the worst cohort for star inflation — a star-derived grade would systematically reward
demo repos with no production use, precisely the failure this axis exists to expose. Forks and
watchers are excluded for the same reason: they count attention, not installs.

#### Known limitations

- **Release counts have no independent cross-check**, unlike registry A/B results which are verified
  against the direct registry API. One publisher controls both the artifact and the counter. Treat
  an A/B resting only on release downloads as weaker than one resting on dependents.
- **Cumulative vs periodic.** Release and Docker counts are all-time; Homebrew is 90-day; registry
  is last-month. Within a channel this is consistent, so the percentile holds, but an older project
  accumulates more all-time volume than an equally-adopted young one. The `longevity` and
  `maintenance` axes carry the "is it still alive" question separately.
- **Only the most recent 100 releases** are read, so all-time totals undercount projects with very
  long release histories.

**Operational notes.** Docker Hub's anonymous API rate-limits hard (429 observed live at 8
concurrent requests) and is the weakest of the three instruments, so it is spent only where a
container image is plausibly the project's primary channel (`service`, `app`) and is serialized
behind a 1.2s delay. That scoping cuts Docker calls across a full rescore by ~70% (177 of 607
pages) and keeps the batch clear of the one limit this scorer has actually been refused by. A
library that happens to publish an image is simply not measured this way.

**Pacing a full rescore.** GitHub's `rate_limit` endpoint does not decrement for this project's
token (verified: five REST calls, `remaining` stayed at 5000), so the budget cannot be observed and
must be assumed. Batches therefore run defensively — small chunks, low parallelism, a pause between
chunks — with the header-driven wait in `gh_api` (§1.2b) as the backstop if the assumption is wrong.
The runner is resumable: a page with an `ok` row is skipped, a `FAIL` row is retried. The Homebrew index is ~20MB of JSON and is
disk-cached with a 24h TTL, since the batch runner invokes this scorer once per page. **An empty
index is never cached** — a transport failure and a genuinely empty registry produce the same
result, and persisting that emptiness would serve it as a measured fact for the whole TTL.

### 2.3c `?` vs `N/A` — a gap in the data vs a gap in the question

These are different claims and must not share a grade:

- **`?`** — we tried to measure and could not. The reader should treat the axis as an open question
  and go look, and the failure may be ours. Stays in the aggregate denominator.
- **`N/A`** — the axis asks a question this artifact type cannot answer, however healthy it is.
  Removed from the denominator, so a skill-pack with its other five axes measured reads `5/5`
  rather than a deceptively thin `5/6`.

For adoption, `N/A` (reason `no_install_channel`) applies only to `skill-pack`, and **only after
every instrument above has been tried and returned nothing**: a skill-pack is copied into a
directory rather than installed, so where it also publishes no downloadable bundle there is no
install event anywhere to count. Conceding `N/A` by type alone would have been wrong — 18 of this
index's 84 skill-packs publish release bundles with real download counts.

`app`, `service`, `tool` and the rest never go `N/A` on this axis: they *can* be adopted measurably,
so failing to find the number is our gap, not a statement that the question does not apply.

**`?` rule** (require POSITIVE proof of no-package, so a real E can't be dodged by mislabeling `type`)
- `no_package_structural` — `type ∈ {app, skill-pack, service, model}` AND `packages/lookup` returns zero entries clearing the noise filter AND GitHub "Used by" empty/unavailable. (model weights on HF Hub → `?` unless a pip/npm wrapper exists, in which case score the wrapper.)
- `registry_lookup_failed` — packages.ecosyste.ms lookup transport or HTTP/API failure; this is a tool/data-source failure, not evidence of zero adoption.
- `registry_no_counts` — a canonical package exists, but comparable dependency/download counts are unavailable. Maven/Go commonly hit this, but the condition is data-shape based rather than registry-name-only. If dependents ARE present → score from dependents, not `?`.
- `ambiguous` — multiple plausible canonical packages, none clears the noise filter, and the by-name secondary lookup (above) also found nothing.
- `no_install_channel` — **grade `N/A`, not `?`**: a `skill-pack` with no package and no install signal of any kind. See §2.3c.
- **A `tool`/`library` with a successful empty lookup is NOT `?`** — if packages.ecosyste.ms responds successfully and no canonical package clears the noise filter, score **E** (measurably unadopted) or manual-flag. Transport / HTTP / API failures are `registry_lookup_failed` (`?`), not evidence of zero adoption. Archived repos keep their last computed tier with an `archived` flag, not `?`.

**Data source / exact calls**
```
GET https://packages.ecosyste.ms/api/v1/packages/lookup?repository_url=https://github.com/{o}/{r}   # discover + filter typosquats
GET https://packages.ecosyste.ms/api/v1/registries/{registry}/packages/{name}
    # fields: .dependent_repos_count (PRIMARY), .downloads, .downloads_period, .dependent_packages_count
    # registry ∈ {npmjs.org,pypi.org,crates.io,rubygems.org,packagist.org,proxy.golang.org,repo1.maven.org}; anon 5000/hr
# A/B cross-check (mandatory):
npm:     GET https://api.npmjs.org/downloads/point/last-month/{pkg}          .downloads
PyPI:    GET https://pypistats.org/api/packages/{pkg}/recent                 .data.last_month
crates:  GET https://crates.io/api/v1/crates/{c}    (UA required)            .crate.recent_downloads
RubyGems:GET https://rubygems.org/api/v1/gems/{g}.json                       .downloads
Packagist:GET https://packagist.org/packages/{v}/{p}.json                    .package.downloads.monthly
Go:      GET https://pkg.go.dev/{module}?tab=importedby   (UA; parse "([0-9,]+) packages")  → importers (map to dependents column)
gh api repos/{owner}/{repo} --jq '{archived,pushed_at,name,homepage,language}'
```

**Gameability resistance**
- Download botting to A → must out-download the top-1% of a whole registry (millions of real installs); economically prohibitive vs star farms. Holds.
- Fake dependents → ecosyste.ms counts indexed *public* repos with real manifests; the A bar (≥10k) needs a fake-repo army. Higher cost than star bots; **residual [推断]:** it is a one-time cost an adversary pays once and keeps.
- Typosquat poisoning → defeated only by the canonical-selection rule above (load-bearing).
- Self-traffic to escape E → E floor set at a self-traffic level AND requires zero dependents.

**Honest scope (revised 2026-09):** the earlier claim — that this axis is measurable only for the
registry-shipping library/framework/tool cohort (~40% of the index) and is `?` for the rest — was
true of the *instrument*, not of the projects. Adding §2.3b's install signals and repairing §2.3's
selection bugs brought the unscored share down from **273/600 (45%)** to the residue documented in
the run log, of which the largest remaining block is `skill-pack` pages that genuinely publish
nothing downloadable and are now `N/A` rather than `?`.

What remains true: **one threshold table does not work across all distribution channels**, and no
single number spans them. The axis is a max() over per-channel anchor tables, each fitted to its
own measured distribution, and a project is only ever compared against the channel it actually
ships through.

---

### 2.4 `longevity` — Longevity (Lindy) / 寿命×仍活跃 — Staying-power / 持続力

**Spine (DECOUPLED):** `created_at` age as a multiplier, **gated** by a liveness floor (archived/disabled + last-commit recency). **Foundation/verified-org backing is REMOVED from tier A** (it was governance double-count) and **release-recency upgrade is REMOVED** (it was momentum). Longevity now depends ONLY on age × still-active. Age bars are **type-relative** so the index's flagship <2y skill-pack/agent cohort isn't floored at C/D.

**Inputs:** `created_at` → `repo_age_days`; `last_commit_age_days` (committer date, default branch); `archived`, `disabled`. (`/orgs` and `/releases/latest` calls are **dropped** — they only fed the removed signals; saves ~328 calls.)

**Type-relative age bars**

| Cohort | A-age | B-age | C-age |
|--------|-------|-------|-------|
| library, framework | ≥5y (1825d) | ≥3y (1095d) | ≥1y (365d) |
| tool, app, service | ≥3y (1095d) | ≥18mo (548d) | ≥6mo (183d) |
| skill-pack, model | ≥18mo (548d) | ≥9mo (274d) | ≥3mo (91d) |

**Exact tiers** (evaluate top-down)

| Tier | Condition |
|------|-----------|
| **E** | `archived==true` OR `disabled==true` OR `last_commit_age_days > 730`. (Hard floor: age cannot rescue a 12-year-old repo last touched 3y ago.) |
| **A** | NOT archived/disabled AND `last_commit_age_days ≤ 90` AND `repo_age_days ≥ A-age[cohort]`. |
| **B** | NOT archived/disabled AND `last_commit_age_days ≤ 180` AND `repo_age_days ≥ B-age[cohort]`. |
| **C** | NOT archived/disabled AND `last_commit_age_days ≤ 365` AND `repo_age_days ≥ C-age[cohort]`. |
| **D** | NOT archived/disabled AND ((`last_commit_age_days ≤ 365` AND `repo_age_days < C-age[cohort]`) OR (`365 < last_commit_age_days ≤ 730`)). Two failure modes: nascent-unproven, or 1–2y stalling. |

**`?` rule**
- `not_found` — repo 404s / private / renamed-not-followed (can't read `created_at` or commits).
- `no_activity_signal` — `created_at` present but BOTH `/commits` AND `pushed_at` unavailable (refuse age-alone fallback — the rubric forbids age without a liveness gate).
- `not_a_repo` — not a single GitHub repo (tarball-only / self-hosted git) and no registry publish-date fallback.
- NOT `?`: a `User` owner (real, low-backing value — but backing no longer affects this axis); a 404 on `/releases/latest` (release no longer used here); a brand-new repo (real **D**). Store the reason; re-runs retry transient 404s.

**Data source / exact calls**
```
gh api repos/{owner}/{repo} --jq '{created_at,pushed_at,archived,disabled}'
gh api 'repos/{owner}/{repo}/commits?per_page=1' --jq '.[0].commit.committer.date'   # fall back to .pushed_at only if /commits errors non-empty
```
Registry fallback (PyPI `.releases` max `upload_time` / npm `.time.modified`) is **dead code for this index** (all 229 are single `github.com` owner/repo) — keep the branch but expect it never to fire.

**Gameability resistance**
- Empty-commit / bot-bump cron to hold liveness → the gate uses committer date (movable). Mitigated by the substance check borrowed for B/C is *not* applied here (age is the differentiator), so disclose: a monthly no-op cron can hold a zombie at **C/D**. Reaching **A** additionally needs real `repo_age ≥ A-age` which is forgery-resistant (`created_at` server-assigned).
- Back-date authorship to fake age → defeated (`created_at`, not author dates).
- Fork-and-relabel → fork's `created_at` is the fork date; correctly lowers Lindy age (not a bug).
- Un-archive to dodge E → defeated (`last_commit_age > 730d ⇒ E` fires regardless of archived flag).

---

### 2.5 `governance` — Governance & Bus-factor / 治理与巴士系数 — Precision / 精密動作性

**Spine (PURE concentration, recency moved out):** top-1 and top-3 author commit-**share** among *active* humans over a trailing-12-month window. **`active_maintainers==0` and `archived` (the headcount-floor / E) are MOVED to the Maintenance axis** — bus-factor is a *structural* property (how concentrated is the work), not "is anyone home" (that is maintenance). This axis answers: *among those doing the work, how concentrated is it?*

**Unbiased windowing (fixes the velocity bug):** do **NOT** use a recent-1000-commit cap (it made the tier velocity-dependent — verified 2-tier swing on `beads`: full-window top1=0.636 → C vs capped-1000 top1=0.309 → A). Use **`GET /repos/{o}/{r}/stats/contributors`** (one call; per-author weekly totals for the full year; 202-async on cold cache → retry ≤3). Sum each author's `weeks[].c` over the trailing 52 weeks for unbiased 12-month per-author counts. If kept on `/commits` instead, sample **strided/random** across the window (never most-recent-N) and set a `sampled` confidence flag.

**Author identity:** dedupe by `author.login`, fall back to `commit.author.email` when login null (~8%); apply the bot/AI filter (§1.3). Count `Co-authored-by:` trailers toward distinct authors when present (don't silently ignore co-authors).

Let `active = #distinct human authors with ≥1 commit in trailing 12mo`, `top1_share` and `top3_share` = their fraction of human commit volume in the window.

**Exact tiers**

| Tier | Condition |
|------|-----------|
| **A** | `active ≥ 5` AND `top1_share ≤ 0.40` AND `top3_share ≤ 0.75`. (GOVERNANCE.md/CODEOWNERS/org-owner are corroborating only — never required.) |
| **B** | `active ≥ 3` AND `top1_share ≤ 0.60`. |
| **C** | `active == 2`, OR (`active ≥ 3` AND `0.60 < top1_share ≤ 0.80`). |
| **D** | `active == 1`, OR `top1_share > 0.80` regardless of headcount. |

**Single-maintainer carve-out:** for `type ∈ {library, tool}` with `repo_age ≥ 3y` AND low issue churn AND maintenance ≠ D/E, a `D` driven solely by `active == 1` is annotated `stable_solo` and lifted to **C** (a legitimately stable, low-churn solo library is not a "classic single point of failure"). The carve-out never lifts a repo whose `top1_share > 0.80` came from a multi-person project (real concentration risk).

**No tier E on this axis** — "no one home" is now Maintenance's E. If `active == 0` after filtering, emit `?` reason `unattributable` (you measured nobody, but governance-concentration is undefined with zero denominator) — Maintenance already carries the "dead" verdict.

**`?` rule** (distinct from a low score)
- `fork` — GitHub-native fork (`.fork==true`) with no independent attributable history. **Known gap:** re-uploaded mirrors have `fork==false` and will be MISSED by this branch — flag low commit-author entropy as a secondary mirror heuristic, or accept the miss and document it.
- `unattributable` — >50% of in-window commits have BOTH null login AND identical squash-bot email (monorepo-export / vendored dump), OR `active==0` after filtering.
- `empty_or_gated` — `/commits`/`stats` returns 409 empty or access-gated.
- `type_na` — **REMOVED for skill-pack.** Skill-packs are NOT blanket-`?`: a one-author skill bag IS a real bus-factor risk and IS visible in commits — compute the same concentration signal. `?` only if the skill-pack repo truly has no attributable history.

**Data source / exact calls**
```
gh api repos/{owner}/{repo} --jq '{owner_type:.owner.type, archived:.archived, fork:.fork}'   # owner_type corroborating only
gh api repos/{owner}/{repo}/stats/contributors    # 202 cold → retry ≤3; per-author weeks[].c; sum trailing 52w
# bonus presence (single cheap call, NEVER moves a tier — used only for a corroborating annotation):
gh api repos/{owner}/{repo}/community/profile --jq '{health:.health_percentage, files:(.files|keys)}'
```
**DROP** the 6 separate CODEOWNERS/GOVERNANCE `contents/` probes (bursts of 404s trip the secondary rate limit; they never move a tier — `community/profile` already reports `code_of_conduct`/`contributing`). **DROP** the per-committer `/users/{login}` company enrichment (up to 20 calls/repo, hammers the secondary limit, doesn't change the base tier).

**Gameability resistance**
- Wrap personal repo in an org → owner.type flips but `top1_share` unchanged → no effect (base tier is share-driven). *(Note: the verifier showed the original `beads`≈90% claim was wrong — it is top1=0.636 → C; do not cite a fabricated number.)*
- Add GOVERNANCE.md/CODEOWNERS → bonus-only, never lifts a tier.
- Bot/AI padding → filtered (§1.3, leaky — disclosed).
- Sockpuppet token commits → can't beat the `top1_share` gates (share is volume, not presence).
- Co-authored-by inflation → counted but bounded by share math.
- **Residual:** several real, regularly-committing alt accounts pass — but that is expensive, sustained, and indistinguishable from genuine multi-maintainer health (acceptable).

---

### 2.6 `risk_license` — Risk / License / 许可与风险 — Durability / 成長性

**Scope (NARROWED): license-permissiveness ONLY, plus relicense detection.** CVE/OSV/advisories are **REMOVED** (transient security state decays on a different timescale than license; and pkg/ecosystem/version is not reliably derivable for 229 repos from free APIs — OSV false-clean `{}` would silently grant A). SECURITY.md presence is **REMOVED** from tiers (it was a maintenance/governance leak). The smooth A–E radius communicates the permissiveness gradient; a **separate non-scoring CAP** (§3.3) handles the legal "can't embed this" cases.

**Permissiveness class** from the `conditions`/`limitations` arrays of `licenses/{key}` (generalizes beyond a hardcoded list; cache per key — only ~20 distinct keys across 229 repos):
- `conditions ⊆ {include-copyright, document-changes}` → **permissive** (MIT, Apache-2.0, BSD-2/3, ISC, Unlicense, MPL-no-spread).
- `disclose-source + same-license`, NO `network-use-disclose` → **weak/file copyleft** (MPL-2.0, LGPL, EPL).
- `disclose-source + same-license + network-use-disclose` → **strong/network copyleft** (GPL, AGPL).
- `spdx_id == NOASSERTION` reading as a source-available license (SSPL/BSL/Elastic-2.0/EULA), or non-OSI / non-commercial (CC-BY-NC, SSPL-1.0) → **source-available / proprietary**.

**Exact tiers** (smooth radius)

| Tier | Condition |
|------|-----------|
| **A** | permissive (conditions ⊆ {include-copyright, document-changes}) AND no relicense event in trailing 36mo. |
| **B** | permissive BUT carries a benign attribution/clause add-on (MIT + watermark like bpmn-js, BSD-2-Clause-Patent). No relicense. |
| **C** | weak/file copyleft (MPL-2.0, LGPL-2.1/3.0, EPL) — usable as a dependency with linking/redistribution obligations. |
| **D** | strong/network copyleft (GPL-2.0/3.0, AGPL-3.0) — whole-program / SaaS viral obligation; a real adoption constraint but open and embeddable. |
| **E** | `spdx_id ∈ {NOASSERTION-confirmed-source-available, NONE/no-LICENSE}` OR non-OSI/non-commercial (CC-BY-NC, SSPL-1.0, Elastic-2.0, BSL-1.1) OR detected relicense permissive→copyleft/source-available within trailing 36mo. |

Mixed/dual: `A OR B` → more permissive of the OR; `A AND B` → more restrictive of the AND. **Component-split** (per-directory, e.g. "MIT code / CC-BY-SA content") is neither — record both and tier on the **code** component; flag the content license in `caveats`.

**Content-license note:** CC-BY-SA / CC-BY-NC are *content* licenses; class them on a separate flag, NOT via the code-copyleft `conditions` map. A CC-BY-NC skill-pack is a real adoption constraint (shown as its tier) but is **never** subject to the overall CAP (§3.3) — it is a prompt bag, not embeddable code.

**Relicense detection (FIXED — the original was broken):** the hardcoded `commits?path=LICENSE` returns 0 for `elasticsearch` (its file is `LICENSE.txt`). **First resolve the real license filename** via `repos/{o}/{r}/license → .path` (or `git/trees?recursive=1` filtered on `LICENSE*`/`COPYING*`/`LICENSE-APACHE`), THEN query commit history on that exact path; for >1 commit fetch the two newest blobs and diff the SPDX class. A permissive→copyleft/NOASSERTION transition in the trailing 36mo = relicense flag.

**`?` rule** (split detection-failed from assessed-bad by reading the LICENSE blob)
- `repo_unreachable` — `gh api .../license` 404s on the **repo** itself (not just the license).
- `license_unparsed` — `spdx_id == NOASSERTION` but the LICENSE blob textually matches a real OSI license GitHub merely failed to detect → `?` + a `caveats` bullet for human review. (If the blob matches SSPL/BSL/EULA → **E**, not `?`.)
- **Skill-packs are NOT collapsed to "license N/A"** — verified to have real, varied licenses (MIT, Apache-2.0, AGPL, CC-BY-NC, NOASSERTION). Apply the smooth radius; exempt from the CAP.

**Data source / exact calls**
```
gh api repos/{owner}/{repo}/license --jq '{spdx:.license.spdx_id, key:.license.key, path:.path}'   # 404 ⇒ NONE = all-rights-reserved
gh api licenses/{key} --jq '{conditions,limitations}'                                               # cache per key (~20 keys)
# relicense (resolve real filename first):
gh api 'repos/{owner}/{repo}/commits?path={resolved_license_path}&per_page=100' --jq 'length'
#   if >1: fetch the two newest LICENSE blobs, diff SPDX class.
# NOASSERTION disambiguation (~4 repos, cheap): fetch the LICENSE blob, pattern-match SSPL/BSL/EULA vs OSI text.
```

**Gameability resistance**
- Re-add permissive LICENSE over an SSPL history → caught by the (now-fixed) relicense history read on the *resolved* path.
- An SPDX id is a public binary fact → the license signal itself is the least gameable in the whole rubric.
- **Residual / honest blind spot [推断]:** "open-core" — the indexed repo genuinely IS the permissive thing while the real product is proprietary. Not resolvable from the numeric tier; surfaced as a `caveats` bullet only.
- **NOT used:** OpenSSF Scorecard (4/6 sampled repos NOT-FOUND — sparse coverage; would force most repos to `?`); branch-protection (404 for any repo you don't admin).

---

## 3. Aggregate "overall HEALTH" grade

### 3.1 Letter → points
A=4, B=3, C=2, D=1, E=0. `?` axes contribute **nothing** and are **excluded from the denominator** (never averaged as 0 or A).

### 3.2 Base overall grade
`overall_score = mean(points over the non-? axes)`. Require **≥3 scored axes** or the overall grade is itself `?` (too little signal). Map the mean back to a letter by nearest band:

**Interpretation guardrail:** `overall` is a measured-signal aggregate over the scored axes, not a
project-quality verdict and not an OSS-selection conclusion. Always show `scored_axes/6` next to the
headline grade so a 3-axis aggregate cannot masquerade as a complete six-axis assessment.

| mean range | overall |
|------------|---------|
| ≥3.5 | **A** |
| 2.5–3.49 | **B** |
| 1.5–2.49 | **C** |
| 0.5–1.49 | **D** |
| <0.5 | **E** |

Record `scored_axes_count` and the list of `?` axes alongside the grade.

### 3.3 Risk/License CAP (constraint, not a quality demerit)
The CAP is a **legal-embeddability** guard, narrowed from the original (which smuggled "copyleft = bad" into the aggregate and clamped 13% of the index). **Copyleft is NOT capped** — GPL/AGPL/LGPL/MPL are open and embeddable; they live on the smooth radius only.

- **CAP applies ONLY when `risk_license` tier is E** *and* the E is a genuine "cannot legally embed" case: `spdx_id ∈ {NONE, NOASSERTION-confirmed-source-available}` OR non-OSI/non-commercial (SSPL/Elastic-2.0/BSL/CC-BY-NC). In that case the **overall grade is clamped at D** and a red ⚠ "license constraint" badge + a `caveats` bullet are emitted.
- **Skill-packs are EXEMPT from the CAP** (content-licensed prompt bags, not embeddable code) — they keep their computed overall grade; the license constraint shows as a badge/caveat only.
- **A `risk_license` tier of D (copyleft) does NOT cap anything** — it only lowers that one axis's radius.
- The per-axis radar vertex always shows the true `risk_license` radius (so the reader sees *why* a cap fired); the CAP modifies only the headline letter.

### 3.4 `?` handling summary
- Per-axis `?` → dashed/gray ghost spoke, excluded from area and from `overall_score`.
- All-or-mostly-`?` (scored axes < 3) → overall = `?`.
- A `?` is never a strength (full radius) and never a failure (E).
- The card must display the scored-axis count (`AXES n/6` / `已评分 n/6`) because `overall` is only
  an aggregate over the measured axes.

---

## 4. Automation notes

### 4.1 API calls per repo (steady state, with PAT)

| Axis | GitHub auth calls | Non-auth calls |
|------|-------------------|----------------|
| maintenance | core repo (shared) + commits?per_page=1 + stats/participation (shared w/ governance histogram) | — |
| responsiveness | 1 GraphQL | — |
| adoption | 1 (repo meta, shared) | ecosyste.ms lookup + ecosyste.ms package + (A/B only) 1 direct-registry + (Go) pkg.go.dev |
| longevity | shares core repo + commits?per_page=1 | (PyPI/npm fallback — never fires) |
| governance | stats/contributors + community/profile | — |
| risk_license | license + licenses/{key} (cached) + relicense path-history (≤3) | — |

**Shared calls counted once per repo.** Distinct GitHub calls/repo ≈ **core repo (1) + commits?per_page=1 (1) + stats/participation (1) + GraphQL issues (1) + stats/contributors (1) + community/profile (1) + license (1) + relicense-history (1, conditional) ≈ 7–8 auth calls**, plus `licenses/{key}` amortized (~20 total). Non-auth: ~2–3 ecosyste.ms + occasional direct-registry/Go (~3).

### 4.2 Rate-limit budget at 229 repos (PAT)
- GitHub authenticated **core**: ~8 × 229 ≈ **1,830 calls** → one full pass fits in a single hour under the **5,000/hr** ceiling with ~2.7× headroom.
- GitHub **GraphQL**: 1 pt × 229 ≈ **229 pts** vs 5,000 pts/hr — trivial.
- **Secondary/abuse limit is the real risk**, not the core ceiling: `stats/participation` and `stats/contributors` have a harsher, undocumented secondary profile and 202-cold-cache behavior; bursting them across 229 repos can 403 independently of the 5,000/hr budget. **Mitigations (mandatory):** run **serial** with backoff, use **ETag conditional requests** (304s don't count against the core limit), treat a cold 202 as `?` on the first pass and **warm-then-re-run**. The dropped `/users` enrichment and 6 `contents/` probes were the biggest secondary-limit hazards — gone.
- ecosyste.ms: ~700–900 anon calls vs 5,000/hr — fine. Direct-registry / PyPI / npm / pkg.go.dev are separate hosts, effectively unmetered.

### 4.3 Per-ecosystem download sources (canonical)
- npm → `api.npmjs.org/downloads/point/last-month/{pkg}`
- PyPI → `pypistats.org/api/packages/{pkg}/recent`
- crates → `crates.io/api/v1/crates/{c}` (UA required)
- RubyGems → `rubygems.org/api/v1/gems/{g}.json`
- Packagist → `packagist.org/packages/{v}/{p}.json`
- Go → **no download counter exists**; use `pkg.go.dev/{module}?tab=importedby` importers, mapped to the dependents column.
- Maven → **no public download counts**; use ecosyste.ms `dependent_repos_count` only; mark volume `?`.
- Unified discovery + dependents for ALL ecosystems → ecosyste.ms.

### 4.4 Caching & `last_verified` semantics
- Persist `computed_at` (run timestamp, UTC) in the `health:` block.
- Cache `licenses/{key}` (~20 keys) for the whole run; cache ETags per endpoint for conditional re-requests.
- Re-score cadence: full re-run on a schedule; **`?` axes are retried every cycle** (transient 202 / 404 / rate-limit), never frozen.
- A page's `health:` block is authoritative; the existing prose `## Health & viability` section is *superseded* by these axes for Adoption/Maintenance/Governance/Backing — state this so the two don't double-assert.

### 4.5 Graceful degradation → `?`
- `stats/*` still 202 after 3 retries → axis `?` (`recency_unreadable` / cold-cache), retry next cycle.
- Any endpoint 404 on the **repo** (moved/private) → that axis `?` with the repo-level reason.
- ecosyste.ms lookup empty + type non-product → adoption `?`; type product (tool/library) → **E or manual flag**, not `?`.
- Direct-registry cross-check >2× divergence (A/B only) → keep the tier but set `needs_human_review: true`.
- Never let a network failure silently downgrade a project; emit `?` + reason instead.

---

## 5. Score → polygon radius + frontmatter `health:` YAML

### 5.1 Radius mapping (uniform across all six axes)
| Grade | Radius (fraction of spoke) | Render |
|-------|----------------------------|--------|
| A | 1.0 | solid fill, gold |
| B | 0.8 | solid fill, green |
| C | 0.6 | solid fill, yellow |
| D | 0.4 | solid fill, orange |
| E | 0.2 | solid fill, red — a small non-zero nub so the polygon stays a hexagon and reads "measured: dead", NOT "no data" |
| `?` | drawn at neutral **0.5**, **hollow marker + dashed gray spoke**, polygon edge interpolated across it as a dashed segment; **excluded from area math** | gray |

Tier colors for SVG fills/strokes: **A=gold `#E5B80B`, B=green `#3FB950`, C=yellow `#D4C20A`, D=orange `#E8702A`, E=red `#E5484D`, ?=gray `#8B949E`.** The filled polygon is colored by **overall** grade; each vertex marker by its **own** axis grade. Area (if shown as a "health score") is computed over **non-`?` axes only** — never impute 0 for a `?` (it would defame a possibly-fine project).

### 5.2 Frontmatter `health:` YAML shape (SSOT — identical in `.md` and `.zh.md`)

```yaml
health:
  schema: 1                       # bump on breaking shape changes
  computed_at: 2026-06-29T12:00:00Z
  overall: B                      # A–E or "?"; reflects CAP if applied
  overall_score: 2.83             # mean over scored axes (null if overall is "?")
  scored_axes: 5                  # count of non-"?" axes (overall is "?" if < 3)
  capped: false                   # true if Risk/License CAP clamped the overall grade
  cap_reason: null                # e.g. "source-available: SSPL-1.0" when capped
  needs_human_review: false       # set by A/B adoption >2x cross-check divergence, etc.
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 4
        active_weeks_13: 9
        carve_out: null           # "mature_library_lindy" if the carve-out lifted the tier
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 33.5
        qualifying_issues: 7
        band: default             # "default" | "relaxed_solo"
        window_offset_days: 5     # seeded random offset (reproducible)
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: langchain
        dependent_repos_count: 18663
        downloads_last_month: 316000000
        graph_tier: A
        volume_tier: C            # max(graph,volume) = A; BOTH persisted
        cross_check_divergence: 1.04
    longevity:
      grade: B
      raw:
        repo_age_days: 1490
        last_commit_age_days: 4
        cohort: library           # which age-bar table was used
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.71
        top3_share: 0.93
        window_source: stats_contributors   # "stats_contributors" | "commits_strided"
        carve_out: null           # "stable_solo" if applied
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null     # e.g. "CC-BY-NC-4.0" for content/skill-packs
  unknowns:                       # one entry per "?" axis (omit key if none)
    # adoption: { reason: no_package_structural }   # reason codes per §2
```

**Reason-code enums** (the `unknowns.<axis>.reason` value):
- maintenance: `repo_404_or_private | empty_repo | recency_unreadable`
- responsiveness: `issues_disabled | no_traffic | no_window_signal | too_young | type_na | github_unavailable | mirror | vendor_support_elsewhere`
- adoption: `no_package_structural | registry_lookup_failed | registry_no_counts | ambiguous`
- longevity: `not_found | no_activity_signal | not_a_repo`
- governance: `fork | unattributable | empty_or_gated`
- risk_license: `repo_unreachable | license_unparsed`

---

## 6. Risks & honest caveats

**Where this rubric can mislead**
- **Maintenance ↔ Risk correlation [推断]:** `archived` forces Maintenance E and is also a real-world risk signal; on dead repos the two axes move together. The hexagon will *look* like two independent confirmations when it is one fact. Disclosed; not corrected (archived genuinely belongs on Maintenance).
- **Governance ↔ Maintenance by design:** we deliberately moved "no one home" to Maintenance so Governance is pure concentration. A feature-complete, well-governed but quiet repo now scores Maintenance-low / Governance-fine — correct, but readers used to "governance = activity" may be surprised.
- **Adoption is genuinely measurable for only ~40% of the index.** The remaining ~60% (apps, skill-packs, services, models, registry-less CLIs, C/C++ libs) are `?`. The radar's Range spoke will be a ghost for most non-library entries — by design, but it means the axis carries little signal across the corpus.

**Weakest / most-gameable axes (ranked)**
1. **Maintenance committer.date spoofing** — cheapest single-repo lie; a shared-owner curated index could cron-green-light recency across many repos. `active_weeks_13` blunts but a sustained cron defeats it for B/C. **[未验证]** whether any indexed repos actually do this.
2. **Responsiveness acknowledgment-bot** via a human-named service account — the near-duplicate-template filter is best-effort heuristic, **not a guarantee** [未验证 at scale]; login-regex alone is trivially evaded.
3. **Adoption fake-dependents** — the ≥10k bar is high but a one-time fake-repo army cost that persists [推断]. The canonical-package selection rule is load-bearing; if it regresses, the axis is trivially poisoned by typosquats.
4. **Governance alt-account farming** — defeats share gates only with sustained real-looking commits, which is indistinguishable from genuine health (accepted).

**What stays [未验证] / [推断]**
- [未验证] Exact per-type counts (library ~64, skill-pack ~42, etc.) — re-derive from the live tree at runtime; the original "37% ship zero releases" claim was wrong (skill-packs ≈ 15–18%, not 37%).
- [未验证] ecosyste.ms `dependent_repos_count` semantics edge cases (mirrors, monorepo subdirs) at the per-repo level.
- [推断] Secondary-rate-limit thresholds for `stats/*` (undocumented by GitHub) — the serial+ETag+warm-then-rerun strategy is the mitigation, behavior **not guaranteed**.
- [推断] That the registry-fallback branch in longevity never fires (all 229 are single `github.com` owner/repo) — keep the code path.
- [推断] LLM/agent behavior is irrelevant here — this rubric is deterministic; any future ML-assisted classification (e.g. README "moved/tombstone" detection) would need its own `[未验证]` disclaimer and is out of scope for v1.

**Explicit non-goals (v1):** CVE/security state (removed — wrong timescale, not reliably computable from free APIs at 229 repos), OpenSSF Scorecard (sparse coverage), GitHub "Used by" as a tier driver (anti-bot scrape, soft evidence only), and the Momentum axis (rejected — see §0).
