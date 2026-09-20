# agent-browser-tools

> Category node. Agent-facing browser and computer-use surfaces — MCP servers, CLI+SKILLs, in-page agents, and logged-in-session bridges.
> ← back to [web-automation](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Agent Browser** | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. | B (6/6) | [→](agent-browser.md) |
| **browser-use** | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | B (6/6) | [→](browser-use.md) |
| **BrowserSkill** | Use it when an agent must drive your already-logged-in Chromium without taking it over — it borrows your tabs only after you confirm and hands control back for login or CAPTCHA. | B (6/6) | [→](browserskill.md) |
| **Chrome DevTools MCP** | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. | A (6/6) | [→](chrome-devtools-mcp.md) |
| **Cua** | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. | B (6/6) | [→](cua.md) |
| **OpenCLI** | Use it when an agent must operate sites behind *your* login — it bridges your already-logged-in Chrome via extension+daemon and freezes site workflows into reusable CLI commands; expect adapter churn and a real trust surface. | B (6/6) | [→](opencli.md) |
| **page-agent** | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. | B (6/6) | [→](page-agent.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Agent Browser](agent-browser.md) | ✅ | B (6/6) | Use it when an agent must shell-drive a real Chrome over CDP with stable element refs instead of CSS selectors. |
| [browser-use](browser-use.md) | ✅ | B (6/6) | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. |
| [BrowserSkill](browserskill.md) | ✅ | B (6/6) | Bridges your already-logged-in Chromium from any shell-capable agent, keeps your own windows untouched, and hands human-only steps back to you; the same trust surface as OpenCLI, minus its deterministic site adapters. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | ✅ | A (6/6) | Use it when an agent needs to drive and DevTools-inspect real Chrome — traces, network, console, heap. |
| [Cua](cua.md) | ✅ | B (6/6) | Use it when an agent must control a full desktop OS via vision in isolated VM sandboxes, not just web pages. |
| [OpenCLI](opencli.md) | ✅ | B (6/6) | Bridges your logged-in Chrome so agents never touch login flows, plus reusable site adapters; Chromium-only, adapter churn is structural, and the extension+daemon inherits all your sessions. |
| [page-agent](page-agent.md) | ✅ | B (6/6) | Use it when you want to control a web UI with natural language in-page via direct DOM read/write, no backend. |

## What belongs here

Surfaces built for an agent loop rather than for committed test code: protocol servers and CLIs, vision/NL agents, and bridges into a real logged-in browser.
