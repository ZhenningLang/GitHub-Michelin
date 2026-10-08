# proxy-pool

> Category node. Self-hosted rotating proxy-IP pools for web scraping.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **proxy_pool** | Use it when a hobby or research scraper keeps getting IP-banned and you want free proxies crawled, validated and served from a self-hosted, Redis-backed HTTP API — but free proxies are slow, short-lived and untrusted, so never route sensitive traffic through them. | C (5/6) | [→](proxy-pool.md) |
| **ProxyBroker** | Use it when a low-stakes prototype needs throwaway free proxies found, checked for anonymity and served through one rotating local endpoint — but it has been dormant since 2019-03 and is widely reported to break on modern Python without pinning. | D (4/6) | [→](proxybroker.md) |
| **Scylla** | Use it when you want an always-on free-proxy service started with one docker run and filtered by HTTPS, anonymity and country through a JSON API with a dashboard — but its forward proxy cannot carry HTTPS, and releases stopped in 2022. | D (4/6) | [→](scylla.md) |
| **haipproxy** | Use it when many spiders across machines need a distributed, high-availability free-proxy pool with decoupled crawlers, validators and schedulers on Scrapy and Redis — but it has been dormant since 2019-07, runs Python 2/3-era code, and is the heaviest pool to operate. | D (4/6) | [→](haipproxy.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [proxy_pool](proxy-pool.md) | ✅ | C (5/6) | Gets free IP rotation behind a tiny HTTP API from a long-lived codebase that still gets commits; costs running Redis plus a scheduler, an unpredictable pool size, and no anti-bot evasion beyond swapping IPs. |
| [ProxyBroker](proxybroker.md) | ✅ | D (4/6) | Gets find, check and serve in one pip-installable asyncio CLI with no datastore to run; costs a frozen codebase, missing proxy auth and uptime tracking, and the usual unreliability of public proxies. |
| [Scylla](scylla.md) | ✅ | D (4/6) | Gets a quality-scored, queryable pool that many jobs share from one container; costs HTTPS only via the API list, a single-maintainer repo coasting toward dormancy, and free-proxy flakiness. |
| [haipproxy](haipproxy.md) | ✅ | D (4/6) | Buys horizontal scale and node-failure tolerance for proxy harvesting; costs running Redis and possibly Splash, compatibility work on frozen code, and a pool that is still only flaky free proxies. |
| paid residential proxies | not indexed | — | Paid proxy services named across the pages; they are not repositories, so they stay out of scope (Scylla is already listed above). |

## What belongs here

Self-hosted **rotating proxy-IP pools** for web scraping. Not scraping frameworks themselves, not web/browser automation (see `web-automation`).
