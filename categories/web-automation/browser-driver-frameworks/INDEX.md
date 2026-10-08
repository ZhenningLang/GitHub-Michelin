# browser-driver-frameworks

> Category node. Programmatic drivers and automation frameworks you script yourself — WebDriver, CDP, and their archived predecessors.
> ← back to [web-automation](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | A (6/6) | [→](selenium.md) |
| **Selenium Wire** | Use it when a legacy Python Selenium suite already depends on it to read or modify the browser's background requests and responses — but it is archived and unmaintained, so new projects should use Selenium 4's CDP/BiDi network access or Playwright. | D (5/6) | [→](selenium-wire.md) |
| **Puppeteer** | Use it when a Node.js job is Chrome-shaped — server-side PDF rendering, scheduled screenshots, prerendering, or a scripted login-and-download — and you want the Chrome team's reference CDP client — but it has no Safari/WebKit and no test runner; use Playwright for those. | A (6/6) | [→](puppeteer.md) |
| **nodriver** | Use it for Python-first async control of Chromium over direct CDP without WebDriver; it is Chromium-only, AGPL-3.0, and its anti-detection behavior is best-effort rather than a stable bypass. | C (5/6) | [→](nodriver.md) |
| **PhantomJS** | Use it only when a legacy CI job, screenshot service or scraper already pins it and you must keep that running until migration — but it is archived, development stopped in 2018, and new work belongs on headless Chrome via Puppeteer or Playwright. | C (5/6) | [→](phantomjs.md) |
| **Moli** | Use it when a structure-first agent fleet needs ~100 MB single-process browsing with real layout/screenshots only as an opt-in exception, over CDP+WebDriver. | B (6/6) | [→](moli.md) |
| **Lightpanda** | Use it when mass JS+DOM extraction never needs pixels: a render-engine-free Zig browser, ~16x lighter than Chrome (vendor-reported), with CDP/BiDi/MCP surfaces. | B (6/6) | [→](lightpanda.md) |
| **Obscura** | Use it when scraping in adversarial lanes wants a self-contained Rust browser with built-in stealth and always-on rendering. | B (6/6) | [→](obscura.md) |
| **undetected-chromedriver** | Use it only to keep an existing Python Selenium suite running past chromedriver's bot-detection markers — the last PyPI release is from 2024-02, so new work belongs on nodriver or SeleniumBase UC Mode. | C (4/6) | [→](undetected-chromedriver.md) |
| **Camoufox** | Use it when a Playwright scraper is blocked because the browser itself is detected: a Firefox fork with engine-level fingerprint spoofing — Firefox-only, ~1.3 GB, self-declared not production-stable. | B (6/6) | [→](camoufox.md) |
| **rebrowser-playwright** | Use it only when an existing Node.js Playwright job pinned to 1.52 is flagged for the `Runtime.Enable` CDP signal on Chrome — a pre-patched drop-in package, frozen since 2025-05. | D (3/6) | [→](rebrowser-playwright.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Selenium](selenium.md) | ✅ | A (6/6) | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. |
| [Selenium Wire](selenium-wire.md) | ✅ | D (5/6) | Gets request capture, mocking and HAR export by changing one import; costs a MITM proxy with its own CA cert, TLS overhead, breakage against cert pinning, and a dependency floor capped at Python 3.10. |
| [Puppeteer](puppeteer.md) | ✅ | A (6/6) | The smallest Chrome-first dependency with raw CDP access and Google backing, traded for no WebKit, no built-in test runner, and fast-moving majors with breaking changes. |
| [nodriver](nodriver.md) | ✅ | C (5/6) | Direct async Python CDP control without WebDriver, trading away cross-browser coverage and permissive licensing; anti-detection is best-effort. |
| [PhantomJS](phantomjs.md) | ✅ | C (5/6) | Keeps an old pipeline alive today with zero rewrite; costs a frozen WebKit that misrenders the modern web and engine CVEs that will never be patched, so isolate it and feed it nothing untrusted. |
| [Moli](moli.md) | ✅ | B (6/6) | Use it when a structure-first agent fleet needs ~100 MB single-process browsing with real layout/screenshots only as an opt-in exception, over CDP+WebDriver. |
| [Lightpanda](lightpanda.md) | ✅ | B (6/6) | Use it when mass JS+DOM extraction never needs pixels: a render-engine-free Zig browser, ~16x lighter than Chrome (vendor-reported), with CDP/BiDi/MCP surfaces. |
| [Obscura](obscura.md) | ✅ | B (6/6) | Use it when scraping in adversarial lanes wants a self-contained Rust browser with built-in stealth and always-on rendering. |
| [undetected-chromedriver](undetected-chromedriver.md) | ✅ | C (4/6) | Keeps every Selenium call while patching chromedriver's markers out, at the price of GPL-3.0, no sandbox by default, and no release since 2024-02. |
| SeleniumBase | 未收录 | — | A batteries-included Python browser-testing framework whose UC Mode is built on undetected-chromedriver; named on the nodriver and undetected-chromedriver pages. |
| [Camoufox](camoufox.md) | ✅ | B (6/6) | Keeps Playwright's API on a Firefox rebuilt to hide automation and rotate device identities; you pay in a gigabyte-class download, no Chrome identity, a 2025 maintenance gap, and ToS/legal exposure. |
| [rebrowser-playwright](rebrowser-playwright.md) | ✅ | D (3/6) | Keeps the Playwright API while removing one detectable CDP command; frozen at Playwright 1.52.0 with no maintainer activity since 2025-05, so patchright is the live choice for new work. |

## What belongs here

Libraries and frameworks a developer codes against directly, including archived ones kept for migration decisions.
