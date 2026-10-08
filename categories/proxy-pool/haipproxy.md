---
name: haipproxy
slug: haipproxy
repo: https://github.com/SpiderClub/haipproxy
category: proxy-pool
tags: [proxy, proxy-pool, scrapy, redis, distributed, scraping, python, self-hosted]
language: Python
license: MIT
maturity: last release v0.1 (2018-03-11), last commit 2019-07-16, quiet since (as of 2026-10-08), ~5.5k stars
last_verified: 2026-10-08
type: app
upstream:
  pushed_at: 2022-12-26T11:50:58Z
  default_branch: master
  default_branch_sha: ab30ccf4b1d78e9304c27830006cc5800fe41bb3
  archived: false
health:
  schema: 1
  computed_at: 2026-10-08T08:25:11Z
  overall: D
  overall_score: 1.25
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 2641
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: haipproxy
        package_link: ecosystems_repository_url
        dependent_repos_count: 1
        downloads_last_month: 47
        graph_tier: D
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3309
        last_commit_age_days: 2641
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# haipproxy

A distributed, high-availability IP proxy pool built on Scrapy + Redis — crawlers harvest public proxies, validators score them, and consumers pull low-latency proxies via a Python client or a Squid integration.

![haipproxy — health radar](../../assets/health/haipproxy.svg)

## When to use

You're running a *large, distributed* crawl — many spiders across machines hammering a target — and a single-node free-proxy harvester can't keep the pool fresh or available enough. You want crawling, validation, and scheduling decoupled so they can scale and survive node failures. You stand up Redis, deploy haipproxy's Scrapy-based crawlers to continuously harvest proxies, let its validators score and rank them, and then have your spiders pull a validated proxy from the Redis-backed pool (via the bundled Python client) or route through the Squid integration. The architecture is explicitly HA: crawlers and schedulers are designed to run redundantly, and a "greedy" selection strategy is documented for squeezing more out of the pool. The project cites a test handling ~80k requests over 11 hours against a target — the use case is sustained, high-volume distributed scraping, not a quick local pool.

This is the right reach when scale and availability are the actual problem — Redis-backed task routing, distributed crawlers, and a consumer client matter — and you accept the heavier infra that comes with it.

## How it works

haipproxy is a set of cooperating Python processes that share one Redis database (an in-memory store used here as both the job queue and the proxy pool). **It does the harvesting and checking for you**: crawler processes built on Scrapy (a scraping framework) fetch free proxy lists from public sites — Splash, a headless rendering service, handles the ones that need JavaScript — and push the IPs into Redis; scheduler processes re-queue that work on a timer, and validator processes test each IP against the specific sites you care about, scoring it per site, because one proxy can work for one site and fail on another. **You run Redis and the components, then consume**: there is no HTTP API — your spider imports the bundled `ProxyFetcher` client and asks for a proxy validated for its target, or routes through the bundled Squid forwarder on port 3128. The README itself says to download a release rather than run `master`, which is not guaranteed to work.

![haipproxy — backbone user story](../../assets/flow/haipproxy.svg)

<!-- flow-steps:begin (generated from flows/haipproxy.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Point the settings at Redis and Splash, then start every component — `docker-compose up` — component: `config/settings.py`
2. **haipproxy**: Crawlers scrape public proxy-list sites and push the IPs into Redis queues — component: `crawler_booter.py`
3. **haipproxy**: Schedulers re-queue the work; validators test each IP against specific target sites and score it — component: `scheduler + validator`
4. **You**: In your spider, ask the client for proxies validated for your target site — `ProxyFetcher('zhihu', strategy='greedy', redis_args=args)`
5. **haipproxy**: Hands back a proxy from that site's scored pool on each request

**Value**: A large distributed crawl keeps a self-refreshing pool of free proxies without buying any

</details>
<!-- flow-steps:end -->

## When NOT to use

- **A small or single-machine scrape.** The Scrapy + Redis + scrapy-splash stack is overkill for a handful of requests; a single-node pool (or just a paid proxy) is far less to run.
- **You can't run Redis (and possibly Splash).** Redis is a hard dependency for the task queues and pool state; JS-rendered sources pull in scrapy-splash. If you can't operate those, this isn't your tool.
- **Production reliability on free proxies.** It pools *free public* proxies — flaky by nature; the README itself notes some proxies can't reach sites like Google due to geo-restrictions. For must-not-fail jobs, buy commercial proxies.
- **You need a maintained dependency.** The repo is **long-dormant** — last release v0.1 (2018-03), last default-branch commit 2019-07-16. You'd be adopting and operating effectively-frozen, Python-2/3-era code; expect compatibility work (see Health). [未验证]
- **Sensitive traffic.** Routing credentials/private data through unknown harvested proxies is a data-exposure risk. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Scylla](scylla.md) | ✅ | Choose Scylla when a simpler single-service pool with UI/API is enough. | Single-service pool with a web UI + JSON API, no Redis required — far simpler to run, but not built for distributed/HA crawler scale the way haipproxy is. |
| [ProxyBroker](proxybroker.md) | ✅ | Choose ProxyBroker when a lightweight CLI finder/checker/server is enough. | A lightweight CLI finder/checker/server with no infra — easiest to invoke, but no distribution, no HA, and itself dormant/Python-fragile. |
| [proxy_pool (jhao104)](proxy-pool.md) | ✅ | Choose proxy_pool when you want a popular Redis-backed pool with simpler single-process design. | Popular Redis-backed self-hosted pool, simpler single-process design than haipproxy's distributed Scrapy architecture; comparable free-proxy niche. [未验证] |
| Paid proxy providers (Bright Data, Oxylabs, …) | 未收录 | Choose paid providers when production SLAs, residential IPs, and rotation matter. | Commercial residential/datacenter pools with SLAs and rotation — the production answer; haipproxy only fits when you specifically need a self-hosted *distributed* free pool. |

## Tech stack

- **Language:** Python 3 (Scrapy-based crawlers).
- **Infra:** **Redis** (task queues, pool state, scheduling) and **Scrapy** as the crawling framework; **scrapy-splash** for JavaScript-rendered proxy sources.
- **Architecture:** decoupled crawler / validator / scheduler components designed for high availability; flexible task routing; configurable selection strategies (e.g. greedy).
- **Consumers:** a bundled Python client and a Squid proxy integration for downstream spiders.

## Dependencies

- **Runtime:** Python 3, a running **Redis** server (required), Scrapy; **scrapy-splash** (and thus a Splash instance) for JS-rendered sources.
- **Deploy:** standalone (manual dependency install + component startup) or **docker-compose** for a containerized stack.
- **Consumer side:** the Python client lib, or Squid if you route through it.
- **It is a multi-component system**, not a single binary or single process.

## Ops difficulty

**Medium to high.** This is genuinely a *distributed system* to operate: Redis, multiple Scrapy crawler/validator/scheduler components, optionally Splash for JS sources, and a consumer client or Squid. docker-compose eases standup, but you still run and monitor several moving parts, keep Redis healthy, and accept that the free-proxy pool quality fluctuates. The dormancy compounds this — running ~2018-era Scrapy/Python code today likely needs dependency pinning or porting before it even comes up. The infra burden plus the compatibility burden makes this the heaviest of the three pools indexed here.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (as of 2026-10-08).** **Dormant.** Last release v0.1 is from 2018-03; last default-branch commit 2019-07-16 (2641 days ago; the 2022-12 push touched no default-branch code), no activity since — not actively developed, though not formally archived. Treat as frozen, Python-2/3-transition-era code.
- **Governance / bus factor.** An **Organization** account (SpiderClub) but with a very small active contributor core; the org wrapper doesn't change that real maintenance has stopped. Bus factor is effectively the same as an abandoned single-maintainer repo. [推断]
- **Age & Lindy verdict.** ~9 years old (created 2017-09) but **dormant since 2019-07** ⇒ Lindy *fails*: age without continued activity signals abandonment, not durability. Old + dormant is a red flag, not social proof.
- **Adoption.** ~5.5k stars and ~900 forks reflect real historical popularity (especially in the Chinese scraping community), but on a dormant repo this is *legacy* adoption — not evidence it works on today's stack. [未验证]
- **Risk flags.** Long dormancy + likely modern-stack incompatibility are the headline risks, on top of the inherent unreliability/security exposure of free public proxies. MIT, no relicense concern.

## Caveats (unverified)

- [未验证] ~5.5k stars as of 2026-10-08; last release v0.1 (2018-03-11), last default-branch commit 2019-07-16, last push 2022-12 — figures are date-sensitive and from the GitHub API.
- [未验证] Compatibility with current Python/Scrapy is not tested here; ~2018-era code likely needs porting/pinning, but the specific failures are unconfirmed.
- [未验证] The ~80k-requests/11-hours figure is the project's own benchmark from the README, not independently reproduced.
- [推断] "Org account but effectively abandoned" is inferred from the commit/release gap, not an official deprecation notice; free-proxy security risk is a general property, not a measured claim about its sources.
