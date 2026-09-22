---
name: HiThink Financial-API
slug: financial-api
repo: https://github.com/HiThink-Tech/Financial-API
category: investment-finance
tags: [a-share, market-data, china-stock-market, financial-data, mcp, cli, python-sdk, hosted-service, quantitative-finance]
language: TypeScript
license: MIT
maturity: CLI v0.1.13, active, ~3.7k stars, created 2026-06; official Tonghuashun (hithink) client toolkit for a hosted A-share data service (as of 2026-09)
last_verified: 2026-09-22
type: tool
aka: [hithink-finance, 同花顺金融数据服务]
upstream:
  pushed_at: 2026-09-22T08:02:30Z
  default_branch: main
  default_branch_sha: 3bca7805a4127ece8d81961917e740d2effac6ec
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T14:39:28Z
  overall: B
  overall_score: 2.5
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 90.6
        qualifying_issues: 17
        band: relaxed_solo
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: "@hithink-tech/hithink-finance-cli"
        dependent_repos_count: 0
        downloads_last_month: 4460
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: D
      raw:
        repo_age_days: 106
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# HiThink Financial-API

Scraping Chinese stock quotes and financials off public pages gets you stale fields, renamed columns, and a pipeline that dies on the next site redesign. This repo is the client side of Tonghuashun's hosted A-share (mainland-China-listed stock) data service: one API key, and the same normalized quotes, statements, index/fund/futures data come back through a CLI, a REST call, an MCP tool or a Python toolkit — with full-market history landing in a local DuckDB you query with SQL.

![HiThink Financial-API — health radar](../../assets/health/financial-api.svg)

## When to use

You are wiring Chinese equity data into an agent or a research script — latest quotes, K-line history, income/balance/cash-flow statements, valuation snapshots, limit-up and dragon-tiger-list special data, fund and futures/options reference data — and the free routes keep failing you: the scrape-based library returned an empty frame because the upstream page changed shape, or a turnover number is obviously wrong and you have no contract to appeal to. A commercial terminal (Wind, iFinD, Choice) would settle it, but it wants a seat licence and a desktop client.

Reach for this page when one key and one documented field contract should serve both the human path (`hithink-finance market snapshot --thscodes 600519.SH` in a terminal) and the agent path (the bundled `hithink-finance` Agent Skill, or the six hosted MCP endpoints), plus a locally maintained DuckDB for long-history SQL work. The deciding tradeoff against the free alternatives is **contractual field stability from an official vendor source** — every endpoint's parameters, response fields and null semantics are documented in-repo and mirrored into the skill — paid for with a key, a vendor dependency, and the capability scope the vendor chose.

## How it works

The repo is not the data; it is the official client toolkit around a hosted service. You create one API key on the vendor's site and hand it to the client once — after that the CLI (a Node.js package, `@hithink-tech/hithink-finance-cli`), the Python toolkit, the hosted MCP servers and raw REST all authenticate with that same key. What you do: name the security and the window, supply the key, and decide where oversized results land. What it does: resolve a name or partial code into the service's unique security id (`thscode`, e.g. `600519.SH`), route the request to the right endpoint, and return a normalized envelope that preserves nulls rather than zero-filling them. For history it stops querying one symbol at a time and instead downloads full-market Parquet dumps plus REST deltas into a local DuckDB, so a multi-year backtest reads a local table. There is no offline mode: with no key and no reachable service the client has nothing to serve.

![financial-api — backbone user story](../../assets/flow/financial-api.svg)

<!-- flow-steps:begin (generated from flows/financial-api.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Get one API key on the vendor site, install the CLI, hand it the key — `hithink-finance auth login` — component: `CLI + OS keyring`
2. **You**: Ask for one security's data by name or code — `hithink-finance market snapshot --thscodes 600519.SH` — component: `CLI`
3. **HiThink Financial-API**: Resolves the name to the unique thscode and routes to the right REST/MCP endpoint — component: `hosted data service`
4. **HiThink Financial-API**: Returns one normalized envelope that preserves nulls; oversized results go to disk — component: `hosted data service`
5. **You**: When you need long history, initialise the local database — `hithink-finance data init` — component: `local DuckDB`
6. **HiThink Financial-API**: Downloads the full-market Parquet dump, then applies incremental updates — component: `CLI data pipeline`
7. **You**: Run SQL against the local copy instead of refetching — `hithink-finance db query --sql "SELECT * FROM v_daily_qfq LIMIT 10"` — component: `local DuckDB`

**Value**: You stop maintaining scrapers and field maps: one key buys contractual A-share fields over four surfaces, and history becomes a local table you can SQL

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You need minute bars, tick or Level-2 data, Hong Kong/US listings, macro series, news or announcement full text, or research reports.** The service's own capability table excludes every one of these, and the vendor's premium capabilities (capital flow, high-frequency movement, futures/options professional data) are shipped only inside its desktop client, not through the public API, MCP, CLI or Python SDK. For US/global daily bars reach for [yfinance](yfinance.md); for tick/Level-2 and cross-market depth you are back to a commercial terminal or an exchange/broker feed.
- **You need the data without a vendor relationship.** No key, no data — the client carries no dataset. If zero budget is a hard constraint, use a community scrape source (AKShare, Tushare's free points tier) and accept that endpoints break without notice.
- **You intend to redistribute or publish the data.** The repository code is MIT, but MIT covers code, not the numbers you pull through the service; redistribution and storage terms live in the vendor's agreement. Read those terms before shipping data inside a product. [未验证]
- **You want a backtest engine, portfolio analytics or signals.** This is a data plane, not a research platform. Pair it with [backtrader](backtrader.md), [qlib](qlib.md) or [FinRL](finrl.md), which model and backtest rather than source.
- **You need a contractual SLA for a live or regulated data path.** Public issues show 429 global rate limits and 504 quote snapshots under normal load, and the project is roughly three months old under a single GitHub account. A production trading or compliance path usually wants a support contract instead. [推断]
- **Your environment cannot run Node.js ≥ 22.12 or Python ≥ 3.11 and you do not want to hand-write HTTP.** The default entry point is a Node CLI; the Python package is installed from the repo, not from PyPI (both `marketdb` and `hithink-finance` return 404 on PyPI as of 2026-09-22). Only raw REST is language-agnostic.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [yfinance](yfinance.md) | ✅ | Pick yfinance when you want keyless, free daily bars for US/global tickers and can accept that Yahoo sourcing is unofficial; pick this page when the securities are A-shares and you need statements, valuations and limit-up-class special data behind a documented field contract. | yfinance costs nothing and needs no account, but its A-share coverage is thin price series with no contractual fundamentals and no vendor to escalate field errors to. |
| [OpenBB](openbb.md) | ✅ | Pick OpenBB when you need one uniform API and terminal UI over many providers and will bring your own provider keys; pick this page when a single official Chinese source with a native agent and CLI surface matters more than an aggregation layer. | OpenBB is a platform rather than a data source — more flexible and multi-market, but it supplies no A-share data on its own. |
| AKShare | 未收录 | Pick AKShare when the budget is exactly zero and a broken endpoint is an acceptable Tuesday; pick this page when stable field names, documented parameters and an official source justify a key and a vendor dependency. | AKShare's breadth (macro, news, alternative datasets, HK/US) exceeds this service's public scope, but it is community-scraped with no contract, no null-semantics promise and no support. |
| Tushare | 未收录 | Closest structural peer — a hosted A-share data service behind a token. Pick Tushare for its points-based access and long-standing Python community; pick this page when you want the vendor-official data plus MCP, CLI and Agent Skill surfaces instead of a Python-only client. | Tushare trades a larger community and a broader community-contributed surface for Python-only ergonomics and quota economics; per-endpoint feature parity with this page is not claimed. [未验证] |
| Wind / Tonghuashun iFinD / Eastmoney Choice | 非仓库 | Pick a commercial terminal when you need tick/Level-2, institutional coverage and a support contract; pick this page when the public A-share, fund, futures and options API subset plus a self-service key is enough. | Closed desktop/feed products with seat pricing and no repository to read — out of scope for this index by shape, and materially more expensive. |

## Tech stack

- **Languages:** TypeScript for the CLI (Node.js ≥ 22.12.0), Python ≥ 3.11 for the `python/` toolkit and its `marketdb` package.
- **CLI runtime dependencies** (from `hithink-finance-cli/package.json`): `commander` for argument parsing, `zod` for schemas, `@duckdb/node-api` for the local database, `@napi-rs/keyring` for the OS credential store, `skills` for Agent Skill installation.
- **Python dependencies:** `duckdb`, `pyarrow`, `pandas`, `typer`, `rich`, `python-dotenv`, `requests`.
- **Data plane:** hosted REST plus six hosted MCP servers under `fuyao.aicubes.cn`; local storage is a DuckDB file fed by full-market Parquet dumps plus REST deltas.
- **Contracts as content:** endpoint documentation lives in Markdown under `docs/api/` and `docs/mcp/`, and `scripts/sync_skill_contracts.py` mirrors it into the standalone Agent Skill so the agent and the docs cannot drift.

## Dependencies

- **An API key** created on the vendor's site (`fuyao.aicubes.cn/admin/`), shared by REST, MCP, CLI and Python. The clients also read the `HITHINK_FINANCE_API_KEY` environment variable and a user-level `credentials.env` / OS credential store.
- **Network reach to `fuyao.aicubes.cn`** for every remote read and for the market dumps — there is no bundled dataset.
- **Node.js ≥ 22.12.0** for the CLI (it pulls native DuckDB and keyring bindings), or **Python ≥ 3.11** for the toolkit path.
- **Disk space** for the local DuckDB plus downloaded Parquet dumps; the project documents no size figure.
- **Nothing to self-host:** no server, no database service, no scheduler. The DuckDB file is the only state you own.

## Ops difficulty

**Low as a consumer — you hold a key, not a service.** Day-2 work is rate-limit-aware batching (the bundled skill instructs the agent to lower concurrency, back off and not retry in parallel on `4001`/429), refreshing the local database (`hithink-finance data sync`, or `marketdb auto-sync` for the Python path) and rotating the key that four surfaces share. Two traps come with the shape rather than the code: any full-market, paginated or long-window result must be written to disk instead of held in context, and the local copy is only as fresh as the last dump or sync. There is no cluster to operate; the hard part is governance — who holds the key, and what you are allowed to store and republish.

## Health & viability

- **Maintenance (2026-09-22).** Very active and release-driven: CLI tags `v0.1.3` through `v0.1.13` in about three months, `v0.1.13` published 2026-09-22 (same day as the last push), commits in every month since 2026-06, three GitHub Actions workflows, and a licence check wired into the npm publish path (`prepublishOnly` runs `check-license.mjs` plus the full verify chain).
- **Age and Lindy prior.** Created 2026-06-09, so roughly three and a half months old — the Lindy prior gives this project no protection at all: its longevity depends on the vendor continuing to run the service, not on a track record. [推断]
- **Adoption.** ~3,723 stars and 323 forks in three months, with ~4,460 npm downloads for the CLI in the last month measured. Fast growth, but on a young vendor-backed repo star velocity is as much a promotion signal as a quality signal. [推断]
- **Governance and bus factor.** The GitHub owner is a **user account** (`HiThink-Tech`), not an organisation, with one contributor listed on the repository; the roadmap is the vendor's and the data plane can be neither forked nor self-hosted. [推断]
- **Responsiveness.** Of the ten most recent issues (September 2026), eight are closed, most within a few hours of opening — including a same-day 504 snapshot report and a data-correctness report about anomalous turnover values. Open ones are feature requests (batch auction top-N, historical valuations).
- **Backing.** The README presents this as Tonghuashun's official A-share data service and links the vendor's own client download on `10jqka.com.cn`; the parent is a long-standing listed Chinese financial-information vendor, which makes operational backing plausible — but the GitHub account's corporate identity cannot be confirmed from the repository alone. [未验证]
- **Risk flags.** The licence is inconsistent inside the repo: root `LICENSE` and `hithink-finance-cli/LICENSE` are MIT, while `python/pyproject.toml` declares `license = { text = "Proprietary" }` for the `marketdb` package — read both before vendoring the Python side. Beyond that: vendor lock-in with key-gated access, and a capability scope that can contract — the 2026-09-20 changelog moved capital-flow, high-frequency and futures/options professional data into the vendor's desktop client, out of the public API surface.

## Caveats (unverified)

- [未验证] Pricing, free tier and quota economics are not documented in the repository or in the service's own `llms.txt`; the only publicly evidenced limits are runtime errors (429 / `4001`). Confirm commercial terms on the vendor site before assuming free access.
- [未验证] The claim that `HiThink-Tech` is Tonghuashun's official project rests on the README, the `fuyao.aicubes.cn` service domain and links to `lumi.10jqka.com.cn` — not on verifiable account ownership.
- [未验证] Data licensing, storage and redistribution terms are absent from the repository; the MIT grant covers the code only.
- [未验证] The local DuckDB plus Parquet dump footprint is not documented; size your disk from a real sync.
- [未验证] Field-level correctness is asserted by the vendor. No independent benchmark of these datasets against Wind, Tushare or AKShare was run for this page.
- [未验证] The Tushare and AKShare characterisations (quota model, breakage rate, breadth) come from general ecosystem knowledge, not from re-verification this pass.
- [推断] High stars-per-month on a young vendor repository is partly promotion — the README links a 同花顺 client download and a Skill Hub listing — as well as genuine demand.
- [推断] "The hosted service and its key are the single point of failure" follows from the absence of any self-hosted or offline mode, not from a measured outage record.
