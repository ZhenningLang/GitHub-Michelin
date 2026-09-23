# playwright-family

> Category node. Microsoft's Playwright stack — the test/automation framework plus its agent-facing CLI+SKILLs and MCP surfaces.
> ← back to [web-automation](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Playwright** | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. | A (5/6) | [→](playwright.md) |
| **Playwright CLI** | Use it when a coding agent (Claude Code, Copilot) needs cheap, token-efficient browser commands with SKILLs installed — Microsoft's own recommended path for coding agents; v0.1.x, freshly repositioned. | A (6/6) | [→](playwright-cli.md) |
| **Playwright MCP** | Use it when an MCP-capable agent needs vendor-official, deterministic browser automation via accessibility-tree snapshots — for stateful exploratory loops; Microsoft's own README steers high-throughput coding agents to its CLI sibling. | A (6/6) | [→](playwright-mcp.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Playwright](playwright.md) | ✅ | A (5/6) | Cross-browser testing and automation with a full runner and tracing surface; its index entry still needs a selection-oriented boundary review. |
| [Playwright CLI](playwright-cli.md) | ✅ | A (6/6) | Microsoft's token-efficient CLI+SKILLs path for coding agents; v0.1.x and freshly repositioned, so expect contract churn. |
| [Playwright MCP](playwright-mcp.md) | ✅ | A (6/6) | Microsoft's official MCP browser: AX-tree snapshots, cross-browser, widest client support; token-heavier than the CLI sibling Microsoft steers coding agents toward. |

## What belongs here

The framework you write test code against, and the two agent-facing front ends Microsoft maintains on the same engine.
