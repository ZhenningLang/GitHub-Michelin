# crawling-tools

> Category node. Web crawling, scraping orchestration, site/API wrappers, and crawler deployment tools.
> ← back to [web-scraping](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Firecrawl** | The API to search, scrape, and interact with the web at scale — turning raw web pages into clean Markdown or structured data your agents can ship with. | B (5/6) | [→](firecrawl.md) |
| **fuck-login** | A collection of ~20 Python scripts that script the login flow of well-known (mostly Chinese) websites — Zhihu, Weibo, Baidu, JD, Bilibili, GitHub, Douban — so you can carry the resulting session cookies into a scraper. A 2016-era teaching repo, explicitly **no longer maintained**. | E (5/6) | [→](fuck-login.md) |
| **gopup** | A Python library that wraps a grab-bag of (mostly Chinese) public data sources behind one-line calls returning pandas DataFrames — Baidu/Weibo/Google search indices, Chinese macro indicators (CPI/PPI/PMI, money supply, FX rates), Shibor/LPR rates, unicorn-company lists, box-office and epidemic data, and more. | E (4/6) | [→](gopup.md) |
| **PRAW** | The "Python Reddit API Wrapper" — a Python package that gives you typed, Pythonic objects (Submission, Comment, Subreddit, Redditor) over Reddit's official OAuth API, and handles rate-limit compliance so you don't have to sprinkle `sleep` calls in your code. | B (5/6) | [→](praw.md) |
| **requests-html** | "HTML Parsing for Humans" — a Python library that bundles `requests`, PyQuery/lxml parsing, and optional JavaScript rendering (via pyppeteer/Chromium) behind one ergonomic API, so a small script can fetch a page and select elements without wiring three libraries together. | D (3/6) | [→](requests-html.md) |
| **Scrapyd** | A service daemon for deploying and running Scrapy spiders over a JSON HTTP API — eggify a Scrapy project, upload it, and schedule/cancel/monitor crawl jobs remotely. The canonical "run Scrapy in production" daemon, from the Scrapy org itself. | B (5/6) | [→](scrapyd.md) |
| **SpiderKeeper** | A Flask-based admin web UI / dashboard for Scrapy spiders that sits on top of Scrapyd — deploy projects, schedule periodic jobs, and watch run stats from a browser. It crawls nothing itself; it's a management layer over one or more Scrapyd servers. Lightweight, popular, and largely stale. | E (4/6) | [→](spiderkeeper.md) |

## What belongs here

Web crawling, scraping orchestration, site/API wrappers, and crawler deployment tools.
