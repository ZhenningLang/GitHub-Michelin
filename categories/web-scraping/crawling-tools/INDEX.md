# crawling-tools

> Category node. Web crawling, scraping orchestration, site/API wrappers, and crawler deployment tools.
> ← back to [web-scraping](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Claude Code Skill Scrapling** | Use it when a Claude Code agent on a Python machine should escalate from a plain request to a stealth browser on its own instead of guessing after a Cloudflare 403 — but it is a four-commit, single-author wrapper whose cheat sheet has drifted from current Scrapling; the library's official skill is the maintained one. | C (4/5) | [→](claude-code-skill-scrapling.md) |
| **Firecrawl** | Use it when your agent or RAG pipeline needs URLs, searches, or whole sites returned as clean Markdown or JSON without owning rendering, proxies, and crawl queues — but self-hosting drops the cloud-only anti-bot, actions, and Agent features, and the core is AGPL-3.0. | B (6/6) | [→](firecrawl.md) |
| **fuck-login** | Use it when you want to study how 2016–2018 Chinese site logins worked under the hood — CSRF tokens, RSA-encrypted passwords, captcha images — from readable Python scripts — but it is abandoned, most scripts are likely broken, and there is no license. | E (5/6) | [→](fuck-login.md) |
| **gopup** | Use it when notebook research needs a quick DataFrame of Chinese public data — Weibo or Baidu indices, CPI, Shibor — without writing a scraper — but it has coasted since 2023-09, its TOKEN API site is gone, and failures silently return None. | E (4/6) | [→](gopup.md) |
| **PRAW** | The "Python Reddit API Wrapper" — a Python package that gives you typed, Pythonic objects (Submission, Comment, Subreddit, Redditor) over Reddit's official OAuth API, and handles rate-limit compliance so you don't have to sprinkle `sleep` calls in your code. | B (5/6) | [→](praw.md) |
| **requests-html** | Use it when you are maintaining an old script that already uses it to fetch and CSS-select server-rendered HTML through one requests-style object — but it has had no release since 2019, and its JS rendering rides on unmaintained pyppeteer. | D (3/6) | [→](requests-html.md) |
| **Scrapling** | Your Python scraper gets a 403 or a Cloudflare challenge page, and a site redesign empties your selectors — one BSD package with HTTP, browser and stealth fetchers, a parser that relocates elements by similarity, and a Scrapy-shaped spider layer. Cloudflare only, 0.x with frequent breaking changes, one maintainer. | B (6/6) | [→](scrapling.md) |
| **Scrapyd** | A service daemon for deploying and running Scrapy spiders over a JSON HTTP API — eggify a Scrapy project, upload it, and schedule/cancel/monitor crawl jobs remotely. The canonical "run Scrapy in production" daemon, from the Scrapy org itself. | B (5/6) | [→](scrapyd.md) |
| **SpiderKeeper** | Use it when a small team already running Scrapyd wants a minimal browser dashboard to deploy eggs, cron-schedule spiders and watch job stats — but it was last committed in 2018-05, pins a 2017 Flask stack, and defaults to admin/admin. | E (3/6) | [→](spiderkeeper.md) |

## What belongs here

Web crawling, scraping orchestration, site/API wrappers, and crawler deployment tools.
