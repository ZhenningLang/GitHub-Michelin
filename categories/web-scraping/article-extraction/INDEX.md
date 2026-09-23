# article-extraction

> Category node. Article readability extraction, boilerplate removal, and content parsing.
> ← back to [web-scraping](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **boilerpipe** | A Java library for boilerplate removal and full-text extraction from HTML — the classic, algorithm-driven approach (shallow text features, link density, tag ratios) that pulls the article out and drops navigation, ads, and surrounding clutter. | "?" (2/6) | [→](boilerpipe.md) |
| **dragnet** | A machine-learning approach to web content extraction — trained models pull the main article (and optionally user comments) out of a page's HTML, using diverse text/markup features rather than hand-tuned heuristics. | D (4/6) | [→](dragnet.md) |
| **newspaper** | A Python library that takes a news/article URL, downloads it, and pulls out the clean article text, title, authors, publish date, top image, and (optionally) NLP keywords/summary — boilerplate stripped, no per-site scraping rules to write. | B (5/6) | [→](newspaper.md) |
| **python-readability** | A fast, lxml-based Python port of arc90's Readability — hand it an HTML document and it returns the cleaned main body (`summary()`) and the title (`title()`), stripping nav, ads, and boilerplate. | A (3/6) | [→](python-readability.md) |
| **Readability.js** | The standalone version of the readability library behind Firefox Reader View — give it a DOM document, get back the article's title, byline, and cleaned main content with the navigation, ads, and boilerplate stripped out. | B (6/6) | [→](readability-js.md) |
| **trafilatura** | Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML | A (6/6) | [→](trafilatura.md) |

## What belongs here

Article readability extraction, boilerplate removal, and content parsing.
