---
name: read-repo
description: 当要为 oss-atlas 写/刷新一个选型页、需要"读懂一个开源仓库"时使用；给出读哪些源、读多深、怎么读源码、怎么把"何时不用"与健康度信号逼出来的方法论。供 add-project / sync-entry 调用，不面向最终用户安装。
argument-hint: <GitHub URL 或 owner/repo>
metadata:
  internal: true
---

# read-repo — how to actually read a project (so the page isn't README marketing)

A selection page is only as good as the *negative space* you found: when NOT to use, the real
tradeoffs, and how healthy the project is. README alone gives you marketing. This skill is the
reading methodology behind `add-project` / `sync-entry`.

**Goal, not coverage.** You are NOT reviewing the code. You read the *minimum* that lets you (1)
verify the project's claims, (2) find the disqualifiers, (3) judge health/viability. Stop when the
page's required sections are evidence-backed — not when you've read everything.

## Read order (cheapest, highest-signal first)

1. **Repo metadata (facts, dated)** — one `gh api repos/<owner>/<repo>` gives most health facts:
   `created_at` (→ **project age**, the Lindy prior), `pushed_at` (recency), `archived`,
   `stargazers_count`, `forks`, `subscribers_count`, `open_issues_count`, `license`, `owner.type`
   (User vs Organization), `language`. Also `gh api repos/<o>/<r>/releases?per_page=5` (latest
   release date + cadence) and `.../contributors?per_page=10` (bus factor signal).
2. **README + docs** — what it claims to do, install path, supported scope, explicit limitations.
   Treat superlatives as unverified marketing until corroborated.
3. **The usage path (how a developer actually puts it to work)** — the README quick start plus a
   real sample (`examples/`, `samples/`, `demo/`, an integration test, or the docs "getting
   started"). Extract: install/deploy command, the one hook/API/config the user writes, what the
   project does on its own afterwards, and where the value lands. This is the evidence for the
   page's `How it works` backbone flow — every command or annotation you put in that flow must come
   from here verbatim, never from memory of similar projects.
4. **Repo layout & entry points** — the file tree, `src/`/package layout, the CLI/lib entry, the
   dependency manifest (`package.json` / `pyproject.toml` / `go.mod` / `Cargo.toml`). This tells you
   the real tech stack and runtime deps (not the marketing list) and the actual surface area.
5. **Health & governance sources** — `CONTRIBUTING`, `GOVERNANCE`, `CODEOWNERS`, `SECURITY.md`,
   org/foundation (Apache/CNCF/LF) vs single-maintainer; `CHANGELOG`/releases for cadence & breaking
   changes; recent issues/PRs for responsiveness; `LICENSE` (read the file — GitHub's API often says
   `NOASSERTION`; relicense history matters: Grafana→AGPL, Redis→SSPL, Elastic, etc.).
6. **Tests & examples** — presence/shape of tests and examples corroborates production-readiness and
   reveals intended use. Skim, don't audit.
7. **Source — only as needed** — read source to *settle a specific question* a claim raised (does it
   really do X offline? is there a hidden service dependency / egress? is the parallelism real?).
   Read the relevant module, not the repo. If you couldn't confirm, label `[未验证]`, don't assert.

## How deep is enough

- **Light** (most pages): metadata + README + manifest + a glance at layout/releases. Enough for a
  clear-cut tool with honest docs.
- **Medium**: + read CONTRIBUTING/governance + skim 1–2 source modules to verify a load-bearing
  claim or a suspected limitation.
- **Deep** (only when it decides the page): a contested capability, a suspicious popularity signal,
  or an unclear hosted/egress dependency — read the specific code path that answers it.

Escalate only when the page's decisive section (usually **When NOT to use**) still rests on an
unverified claim. Don't deep-read for its own sake.

## Turn reading into the page

- **Usage path → `How it works`** — a plain-language mechanism paragraph that draws the line between
  *what the project does for you* and *what you do*, plus the backbone flow spec (`flows/<slug>.json`,
  rendered by `tools/flow_card.py`). See `tools/schema.md` §2.
- **Facts → frontmatter** (`maturity`, dated) and **Health & viability** bullets (also dated).
- **Disqualifiers → `When NOT to use`** — the sharpest section. Sources of real "don'ts": scale
  ceilings in issues, license/relicense traps in LICENSE, single-maintainer/abandonment from
  cadence + bus factor, hidden deps from the manifest/source, lock-in from open-core docs.
- **Health signals → `Health & viability`** — see the checklist in `tools/schema.md` §7
  (maintenance cadence, governance/bus-factor, backing org, age/**Lindy**, adoption/ecosystem, risk
  flags). Write dated judgment, label the unverified, and **use age × still-active together** —
  Lindy (old-and-active ⇒ likely to persist) is a prior, not proof; an old *abandoned* repo fails it.
- **Anything unconfirmed → `Caveats (unverified)` ledger**, one `[未验证]`/`[推断]` bullet each.

## Anti-patterns

- Paraphrasing the README's pitch as if verified. Marketing ≠ facts.
- Writing a `How it works` flow from how *similar* projects work. If the command isn't in this
  repo's docs/samples, it doesn't go in the flow.
- Reading lots of source to look thorough while leaving `When NOT to use` thin. Wrong budget.
- Asserting maintenance/health from stars alone — high stars on a young or stale repo is a *risk
  flag*, not social proof (treat anomalies as `[未验证]`).
- Stating a license from the GitHub API badge without opening `LICENSE` when it says `NOASSERTION`.
