# article-extraction

> Category node. Article readability extraction, boilerplate removal, and content parsing.
> ← back to [web-scraping](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **boilerpipe** | Use it when a JVM indexer or corpus pipeline needs the main text stripped from raw HTML with classic shallow-text-feature heuristics and no browser or Python service — but it is effectively abandoned (last push 2018-01), so you vendor it and own fixes. | "?" (2/6) | [→](boilerpipe.md) |
| **dragnet** | Use it when heuristic extractors keep mis-cutting your pages and you have labeled data to train a Python model that separates article text from user comments — but it is near-dormant and pins scikit-learn below 0.21, which makes modern installs painful. | D (4/6) | [→](dragnet.md) |
| **newspaper** | A Python library that takes a news/article URL, downloads it, and pulls out the clean article text, title, authors, publish date, top image, and (optionally) NLP keywords/summary — boilerplate stripped, no per-site scraping rules to write. | B (5/6) | [→](newspaper.md) |
| **python-readability** | A fast, lxml-based Python port of arc90's Readability — hand it an HTML document and it returns the cleaned main body (`summary()`) and the title (`title()`), stripping nav, ads, and boilerplate. | A (3/6) | [→](python-readability.md) |
| **Readability.js** | The standalone version of the readability library behind Firefox Reader View — give it a DOM document, get back the article's title, byline, and cleaned main content with the navigation, ads, and boilerplate stripped out. | B (6/6) | [→](readability-js.md) |
| **trafilatura** | Use it when you need the main text, title, author, and date from thousands of article pages on sites you don't control, without writing per-site selectors — but it reads raw HTML only, so JavaScript-rendered or bot-blocked pages need a browser or stealth fetcher first. | A (6/6) | [→](trafilatura.md) |

## What belongs here

Article readability extraction, boilerplate removal, and content parsing.
