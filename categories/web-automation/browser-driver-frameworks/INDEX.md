# browser-driver-frameworks

> Category node. Programmatic drivers and automation frameworks you script yourself — WebDriver, CDP, and their archived predecessors.
> ← back to [web-automation](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | B (6/6) | [→](selenium.md) |
| **Selenium Wire** | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. | D (5/6) | [→](selenium-wire.md) |
| **Puppeteer** | JavaScript API for Chrome and Firefox | A (5/6) | [→](puppeteer.md) |
| **nodriver** | Use it for Python-first async control of Chromium over direct CDP without WebDriver; it is Chromium-only, AGPL-3.0, and its anti-detection behavior is best-effort rather than a stable bypass. | C (5/6) | [→](nodriver.md) |
| **PhantomJS** | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. | D (5/6) | [→](phantomjs.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Selenium](selenium.md) | ✅ | B (6/6) | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. |
| [Selenium Wire](selenium-wire.md) | ✅ | D (5/6) | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. |
| [Puppeteer](puppeteer.md) | ✅ | A (5/6) | Chrome-first JavaScript automation; its index entry still needs a selection-oriented boundary review. |
| [nodriver](nodriver.md) | ✅ | C (5/6) | Direct async Python CDP control without WebDriver, trading away cross-browser coverage and permissive licensing; anti-detection is best-effort. |
| [PhantomJS](phantomjs.md) | ✅ | D (5/6) | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. |
| undetected-chromedriver / SeleniumBase | 未收录 | — | Selenium-compatible stealth tooling and a batteries-included Python browser-testing framework named on the nodriver page. |

## What belongs here

Libraries and frameworks a developer codes against directly, including archived ones kept for migration decisions.
