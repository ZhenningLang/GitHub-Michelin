# web-automation

> Category node. Drive or automate a web UI — browser automation, or an in-page natural-language GUI agent.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **page-agent** | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. | B (6/6) | [→](page-agent.md) |
| **Chrome DevTools MCP** | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. | A (6/6) | [→](chrome-devtools-mcp.md) |
| **Cua** | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. | B (6/6) | [→](cua.md) |
| **Agent Browser** | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. | B (6/6) | [→](agent-browser.md) |
| **Selenium** | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. | B (6/6) | [→](selenium.md) |
| **PhantomJS** | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. | D (5/6) | [→](phantomjs.md) |
| **Selenium Wire** | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. | D (5/6) | [→](selenium-wire.md) |
| **browser-use** | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | B (6/6) | [→](browser-use.md) |
| **Playwright** | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. | A (5/6) | [→](playwright.md) |
| **Puppeteer** | JavaScript API for Chrome and Firefox | A (5/6) | [→](puppeteer.md) |
| **nodriver** | Use it for Python-first async control of Chromium over direct CDP without WebDriver; it is Chromium-only, AGPL-3.0, and its anti-detection behavior is best-effort rather than a stable bypass. | C (5/6) | [→](nodriver.md) |
| **Playwright MCP** | Use it when an MCP-capable agent needs vendor-official, deterministic browser automation via accessibility-tree snapshots — for stateful exploratory loops; Microsoft's own README steers high-throughput coding agents to its CLI sibling. | A (6/6) | [→](playwright-mcp.md) |
| **Playwright CLI** | Use it when a coding agent (Claude Code, Copilot) needs cheap, token-efficient browser commands with SKILLs installed — Microsoft's own recommended path for coding agents; v0.1.x, freshly repositioned. | A (5/6) | [→](playwright-cli.md) |
| **OpenCLI** | Use it when an agent must operate sites behind *your* login — it bridges your already-logged-in Chrome via extension+daemon and freezes site workflows into reusable CLI commands; expect adapter churn and a real trust surface. | B (6/6) | [→](opencli.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [page-agent](page-agent.md) | ✅ | B (6/6) | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | ✅ | A (6/6) | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. |
| [Cua](cua.md) | ✅ | B (6/6) | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. |
| [Agent Browser](agent-browser.md) | ✅ | B (6/6) | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. |
| [Selenium](selenium.md) | ✅ | B (6/6) | Use it when you need cross-browser WebDriver automation across a browser/language matrix — Playwright/Cypress are nicer for modern single-browser DX. |
| [PhantomJS](phantomjs.md) | ✅ | D (5/6) | Avoid for new work — an archived, abandoned scriptable headless browser; use headless Chrome (Puppeteer/Playwright) or Selenium instead. |
| [Selenium Wire](selenium-wire.md) | ✅ | D (5/6) | Use it when a legacy Selenium suite needs to read or modify the browser's background HTTP traffic — but it's archived, so new projects should use Selenium 4's native CDP/BiDi or Playwright. |
| [Playwright](playwright.md) | ✅ | A (5/6) | Cross-browser testing and automation with a full runner and tracing surface; its index entry still needs a selection-oriented boundary review. |
| [Puppeteer](puppeteer.md) | ✅ | A (5/6) | Chrome-first JavaScript automation; its index entry still needs a selection-oriented boundary review. |
| [nodriver](nodriver.md) | ✅ | C (5/6) | Direct async Python CDP control without WebDriver, trading away cross-browser coverage and permissive licensing; anti-detection is best-effort. |
| [Playwright MCP](playwright-mcp.md) | ✅ | A (6/6) | Microsoft's official MCP browser: AX-tree snapshots, cross-browser, widest client support; token-heavier than the CLI sibling Microsoft steers coding agents toward. |
| [Playwright CLI](playwright-cli.md) | ✅ | A (5/6) | Microsoft's token-efficient CLI+SKILLs path for coding agents; v0.1.x and freshly repositioned, so expect contract churn. |
| [OpenCLI](opencli.md) | ✅ | B (6/6) | Bridges your logged-in Chrome so agents never touch login flows, plus reusable site adapters; Chromium-only, adapter churn is structural, and the extension+daemon inherits all your sessions. |
| undetected-chromedriver / SeleniumBase | 未收录 | — | Selenium-compatible stealth tooling and a batteries-included Python browser-testing framework named on the nodriver page. |

## What belongs here

Tools that **drive or automate a web/browser (or computer) GUI** — headless browser automation, computer-use, or in-page GUI agents. Not server-side scraping frameworks; not enterprise desktop-only RPA.
