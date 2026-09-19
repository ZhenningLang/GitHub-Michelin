---
name: Firecrawl
slug: firecrawl
repo: https://github.com/firecrawl/firecrawl
category: crawling-tools
tags: [web-scraping, ai-crawler, markdown, data-extraction, api]
language: TypeScript
license: AGPL-3.0
maturity: v1.x, active, 142k stars (as of 2026-07)
last_verified: 2026-07-01
type: service
upstream:
  pushed_at: 2026-07-06T07:42:51Z
  default_branch: main
  default_branch_sha: 84d736273d3165cb4da718b6b75a5d966dc7fd5d
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:59:27Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 147.3
        qualifying_issues: 37
        band: default
        window_offset_days: 1
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: firecrawl-py
        dependent_repos_count: 0
        downloads_last_month: 5804535
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.21
    longevity:
      grade: B
      raw:
        repo_age_days: 809
        last_commit_age_days: 2
        cohort: service
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 48
        top1_share: 0.374
        top3_share: 0.591
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# Firecrawl

The API to search, scrape, and interact with the web at scale — turning raw web pages into clean Markdown or structured data your agents can ship with.

![Firecrawl — health radar](../../../assets/health/firecrawl.svg)

## When to use

You're building an AI agent or data pipeline that needs to ingest web content at scale, and you want clean, structured output rather than raw HTML. You've looked at writing Scrapy spiders or Playwright scripts, but maintaining browser automation, handling anti-bot, and converting messy HTML into Markdown is not your core job. You reach for Firecrawl because it is an API-first service that handles search, scraping, and even browser interaction (click, navigate) for you, returning structured Markdown or JSON without you managing crawler infrastructure. Pick Firecrawl over [Scrapyd](scrapyd.md) or raw Scrapy when you want the extraction and conversion layer handled for you rather than scheduling spiders you wrote yourself; pick it over [newspaper](../article-extraction/newspaper.md) or [Readability.js](../article-extraction/readability-js.md) when you need general-purpose web scraping, search, and interaction at scale rather than single-page article extraction. If you need a hosted API with an AGPL-3.0 open-source self-host option, Firecrawl is the closer fit than proprietary alternatives.


## When NOT to use

- **Simple one-off scraping.** If you need a single page or occasional curl, use `curl` + `pandoc` or `trafilatura` instead of Firecrawl, because paying for or self-hosting a full crawling API is overkill for sporadic tasks.
- **Strict closed-source compliance.** If you need a permissive-license scraper without network-copyleft obligations, use [newspaper](../article-extraction/newspaper.md) (MIT) or `trafilatura` (Apache-2.0) instead of Firecrawl, because AGPL-3.0 requires sharing source if you modify and distribute the service. [未验证]
- **Budget-constrained at scale.** If you need high-volume scraping without per-request pricing, use Scrapy or Playwright on your own infrastructure instead of Firecrawl's hosted service, because the API pricing becomes significant at scale and self-hosting Firecrawl still requires managing Node.js and browser automation.
- **Deep web / authenticated sites.** If you need complex login flows and session management across many sites, use custom Playwright scripts instead of Firecrawl, because while it supports interaction, complex multi-step authentication and stateful crawling are better handled by direct browser automation you control.


## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Scrapyd](scrapyd.md) | ✅ | Self-hosted Scrapy spider scheduler. | Scrapyd is for running Scrapy spiders you write; Firecrawl is an API that handles crawling and extraction for you. |
| [newspaper](../article-extraction/newspaper.md) | ✅ | Article text extraction from news URLs. | newspaper is Python-only and article-focused; Firecrawl is a full-service API with search, scrape, and interaction. |
| [Readability.js](../article-extraction/readability-js.md) | ✅ | Firefox Reader View article extraction. | Readability.js is a browser library for article extraction; Firecrawl is a scalable API with search and interaction. |
| [PRAW](praw.md) | ✅ | Reddit-specific API wrapper. | PRAW is Reddit-only; Firecrawl is general-purpose web scraping. |
| Scrapy / [Playwright](../../web-automation/playwright-family/playwright.md) | partly indexed | Lower-level scraping frameworks. | Scrapy and Playwright give full control but require building and maintaining crawler infrastructure. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — API server runtime
- **Docker** — containerized deployment option
- **Playwright** — underlying browser automation for JS-rendered pages

## Dependencies

- For hosted API: API key and internet connectivity
- For self-hosted: Docker, Node.js runtime, and a server with sufficient bandwidth
- Optional: Redis for caching and queue management
- Browser dependencies (Chromium via Playwright) for dynamic content

## Ops difficulty

**Low (hosted) / Medium (self-hosted)**. The hosted API is a simple HTTP integration. Self-hosting requires managing a Node.js service, Playwright browser instances, and queue/caching infrastructure. Browser automation is resource-intensive and can consume significant memory.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 1 days ago.
- **Responsiveness**: Grade B — median first-response time 147.3 hours across 37 qualifying issues/PRs.
- **Adoption**: Grade A — 5,804,535 monthly downloads via pypi.org (package: firecrawl-py).
- **Longevity**: Grade B — 809 days old.
- **Governance**: Grade A — top-3 contributor share 59.1% (?).
- **Risk / License**: Grade D — AGPL-3.0 license.
## Caveats (unverified)

- [未验证] The AGPL-3.0 license may require source disclosure for derivative works in a SaaS context; verify with legal counsel for your specific use case.
- [未验证] The exact feature parity between the open-source self-hosted version and the paid hosted API is not confirmed.
- [推断] The 142k star count on a ~2-year-old repo suggests significant hype; verify organic production adoption beyond the GitHub star metric.
