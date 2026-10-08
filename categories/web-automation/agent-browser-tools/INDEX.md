# agent-browser-tools

> Category node. Agent-facing browser and computer-use surfaces — MCP servers, CLI+SKILLs, in-page agents, and logged-in-session bridges.
> ← back to [web-automation](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Agent Browser** | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. | B (5/6) | [→](agent-browser.md) |
| **Browser Harness** | Use it when a coding agent must drive the Chrome you are already logged into over CDP, writing missing helpers into a local workspace — Alpha, default-on telemetry, no inner agent loop. | A (6/6) | [→](browser-harness.md) |
| **browser-use** | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | A (6/6) | [→](browser-use.md) |
| **BrowserSkill** | Use it when an agent must drive your already-logged-in Chromium without taking it over — it borrows your tabs only after you confirm and hands control back for login or CAPTCHA. | B (6/6) | [→](browserskill.md) |
| **Chrome DevTools MCP** | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. | A (6/6) | [→](chrome-devtools-mcp.md) |
| **OpenCLI** | Use it when an agent must operate sites behind *your* login — it bridges your already-logged-in Chrome via extension+daemon and freezes site workflows into reusable CLI commands; expect adapter churn and a real trust surface. | B (6/6) | [→](opencli.md) |
| **page-agent** | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. | B (6/6) | [→](page-agent.md) |
| **Jev Ultrafast** | Use it when per-step latency is the binding constraint and you accept a hosted decision API — one request returns both the operation and the element for each browser step. | C (6/6) | [→](jev-ultrafast.md) |
| **PinchTab** | Use it when an agent needs a resident local browser service that orchestrates multiple isolated Chrome instances/profiles over CLI, HTTP and MCP, with default-deny capability gates and prompt-injection scanning built in; pre-1.0 and effectively single-maintainer. | B (6/6) | [→](pinchtab.md) |
| **invisible_playwright_mcp** | Use it when an MCP assistant keeps hitting captchas and bot walls — it drives a C++-patched stealth Firefox with seed-derived fingerprints; Windows/Linux only, single maintainer, stars inherited from a renamed job-bot repo. | B (5/6) | [→](invisible-playwright-mcp.md) |
| **playwright-bot-bypass** | Use it when a script your coding agent writes gets flagged as a bot on your own desktop — a skill plus one factory that drives your real headed Chrome through rebrowser-playwright; needs a display, does nothing for IP/behavioural/CAPTCHA gates, and rests on a dependency unreleased since 2025-05. | C (5/6) | [→](playwright-bot-bypass.md) |
| **camofox-browser** | Use it when a multi-user, always-on agent keeps getting captchas — a resident REST/MCP/OpenClaw server over the Camoufox stealth Firefox with per-user sessions and ref-based snapshots; routes open and telemetry on by default, one dominant committer, eight months old. | B (6/6) | [→](camofox-browser.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Agent Browser](agent-browser.md) | ✅ | B (5/6) | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. |
| [Browser Harness](browser-harness.md) | ✅ | A (6/6) | Coding agent attaches to your live Chrome over CDP and writes missing helpers locally; no inner LLM loop, telemetry on until you opt out, still 0.1.x Alpha. |
| [browser-use](browser-use.md) | ✅ | A (6/6) | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. |
| [BrowserSkill](browserskill.md) | ✅ | B (6/6) | Bridges your already-logged-in Chromium from any shell-capable agent, keeps your own windows untouched, and hands human-only steps back to you; the same trust surface as OpenCLI, minus its deterministic site adapters. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | ✅ | A (6/6) | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. |
| [OpenCLI](opencli.md) | ✅ | B (6/6) | Bridges your logged-in Chrome so agents never touch login flows, plus reusable site adapters; Chromium-only, adapter churn is structural, and the extension+daemon inherits all your sessions. |
| [page-agent](page-agent.md) | ✅ | B (6/6) | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. |
| [Jev Ultrafast](jev-ultrafast.md) | ✅ | C (6/6) | Use it when per-step latency is the binding constraint and you accept a hosted decision API — one request returns both the operation and the element for each browser step. |
| [PinchTab](pinchtab.md) | ✅ | B (6/6) | One resident Go server gives an agent CLI/HTTP/MCP control of multiple isolated Chrome instances under named profiles, folding action and snapshot into one round trip, with default-deny capability gates and IDPI content scanning; young, pre-1.0, effectively single-maintainer. |
| [invisible_playwright_mcp](invisible-playwright-mcp.md) | ✅ | B (5/6) | Use it when an MCP assistant keeps hitting captchas and bot walls — it drives a C++-patched stealth Firefox with seed-derived fingerprints; Windows/Linux only, single maintainer, stars inherited from a renamed job-bot repo. |
| [playwright-bot-bypass](playwright-bot-bypass.md) | ✅ | C (5/6) | An agent skill plus a ~180-line factory over real headed Chrome and rebrowser-playwright: fingerprint tells are absent rather than faked, on macOS too; desktop-only, self-measured, single maintainer, stale core dependency. |
| [camofox-browser](camofox-browser.md) | ✅ | B (6/6) | A shared Node server that puts the Camoufox stealth Firefox behind REST, OpenClaw and MCP tools with per-user sessions, cookie import and proxy rotation; all stealth is inherited from upstream Camoufox, routes are unauthenticated and telemetry is on until you configure otherwise, and memory-leak reports recur. |

## What belongs here

Surfaces built for an agent loop rather than for committed test code: protocol servers and CLIs, vision/NL agents, and bridges into a real logged-in browser.
