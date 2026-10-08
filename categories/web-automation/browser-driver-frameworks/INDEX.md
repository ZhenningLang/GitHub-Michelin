# browser-driver-frameworks

> Category node. Programmatic drivers and automation frameworks you script yourself — WebDriver, CDP, and their archived predecessors.
> ← back to [web-automation](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | A (6/6) | [→](selenium.md) |
| **Selenium Wire** | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. | D (5/6) | [→](selenium-wire.md) |
| **Puppeteer** | JavaScript API for Chrome and Firefox | A (6/6) | [→](puppeteer.md) |
| **nodriver** | Use it for Python-first async control of Chromium over direct CDP without WebDriver; it is Chromium-only, AGPL-3.0, and its anti-detection behavior is best-effort rather than a stable bypass. | C (5/6) | [→](nodriver.md) |
| **PhantomJS** | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. | C (5/6) | [→](phantomjs.md) |
| **Moli** | Use it when a structure-first agent fleet needs ~100 MB single-process browsing with real layout/screenshots only as an opt-in exception, over CDP+WebDriver. | B (6/6) | [→](moli.md) |
| **Lightpanda** | Use it when mass JS+DOM extraction never needs pixels: a render-engine-free Zig browser, ~16x lighter than Chrome (vendor-reported), with CDP/BiDi/MCP surfaces. | B (6/6) | [→](lightpanda.md) |
| **Obscura** | Use it when scraping in adversarial lanes wants a self-contained Rust browser with built-in stealth and always-on rendering. | B (6/6) | [→](obscura.md) |
| **undetected-chromedriver** | Use it only to keep an existing Python Selenium suite running past chromedriver's bot-detection markers — the last PyPI release is from 2024-02, so new work belongs on nodriver or SeleniumBase UC Mode. | C (4/6) | [→](undetected-chromedriver.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Selenium](selenium.md) | ✅ | A (6/6) | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. |
| [Selenium Wire](selenium-wire.md) | ✅ | D (5/6) | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. |
| [Puppeteer](puppeteer.md) | ✅ | A (6/6) | Chrome-first JavaScript automation; its index entry still needs a selection-oriented boundary review. |
| [nodriver](nodriver.md) | ✅ | C (5/6) | Direct async Python CDP control without WebDriver, trading away cross-browser coverage and permissive licensing; anti-detection is best-effort. |
| [PhantomJS](phantomjs.md) | ✅ | C (5/6) | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. |
| [Moli](moli.md) | ✅ | B (6/6) | Use it when a structure-first agent fleet needs ~100 MB single-process browsing with real layout/screenshots only as an opt-in exception, over CDP+WebDriver. |
| [Lightpanda](lightpanda.md) | ✅ | B (6/6) | Use it when mass JS+DOM extraction never needs pixels: a render-engine-free Zig browser, ~16x lighter than Chrome (vendor-reported), with CDP/BiDi/MCP surfaces. |
| [Obscura](obscura.md) | ✅ | B (6/6) | Use it when scraping in adversarial lanes wants a self-contained Rust browser with built-in stealth and always-on rendering. |
| [undetected-chromedriver](undetected-chromedriver.md) | ✅ | C (4/6) | Keeps every Selenium call while patching chromedriver's markers out, at the price of GPL-3.0, no sandbox by default, and no release since 2024-02. |
| SeleniumBase | 未收录 | — | A batteries-included Python browser-testing framework whose UC Mode is built on undetected-chromedriver; named on the nodriver and undetected-chromedriver pages. |

## What belongs here

Libraries and frameworks a developer codes against directly, including archived ones kept for migration decisions.
