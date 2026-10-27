# stealth-session-tools

> Category node. Agent-facing browser tools for sessions blocked by automation detection or browser fingerprints.
> ← back to [agent-browser-tools](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **invisible_playwright_mcp** | Use it when an MCP assistant keeps hitting captchas and bot walls — it drives a C++-patched stealth Firefox with seed-derived fingerprints; Windows/Linux only, single maintainer, stars inherited from a renamed job-bot repo. | B (5/6) | [→](invisible-playwright-mcp.md) |
| **playwright-bot-bypass** | Use it when a script your coding agent writes gets flagged as a bot on your own desktop — a skill plus one factory that drives your real headed Chrome through rebrowser-playwright; needs a display, does nothing for IP/behavioural/CAPTCHA gates, and rests on a dependency unreleased since 2025-05. | C (5/6) | [→](playwright-bot-bypass.md) |
| **camofox-browser** | Use it when a multi-user, always-on agent keeps getting captchas — a resident REST/MCP/OpenClaw server over the Camoufox stealth Firefox with per-user sessions and ref-based snapshots; routes open and telemetry on by default, one dominant committer, eight months old. | B (6/6) | [→](camofox-browser.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [invisible_playwright_mcp](invisible-playwright-mcp.md) | ✅ | B (5/6) | Use it when an MCP assistant keeps hitting captchas and bot walls — it drives a C++-patched stealth Firefox with seed-derived fingerprints; Windows/Linux only, single maintainer, stars inherited from a renamed job-bot repo. |
| [playwright-bot-bypass](playwright-bot-bypass.md) | ✅ | C (5/6) | An agent skill plus a ~180-line factory over real headed Chrome and rebrowser-playwright: fingerprint tells are absent rather than faked, on macOS too; desktop-only, self-measured, single maintainer, stale core dependency. |
| [camofox-browser](camofox-browser.md) | ✅ | B (6/6) | A shared Node server that puts the Camoufox stealth Firefox behind REST, OpenClaw and MCP tools with per-user sessions, cookie import and proxy rotation; all stealth is inherited from upstream Camoufox, routes are unauthenticated and telemetry is on until you configure otherwise, and memory-leak reports recur. |

## What belongs here

Tools whose deciding selection axis is an agent's browser session being detected or blocked: stealth MCP surfaces, agent-oriented browser recipes and resident anti-detection session servers. This is not a guarantee of bypassing challenges or permission to automate a target. General browser control, DevTools inspection and bridges into an existing login stay in [agent-browser-tools](../INDEX.md); script-first browser engines stay in [browser-driver-frameworks](../../browser-driver-frameworks/INDEX.md).
