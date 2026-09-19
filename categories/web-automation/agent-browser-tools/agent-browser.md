---
name: Agent Browser
slug: agent-browser
repo: https://github.com/vercel-labs/agent-browser
category: agent-browser-tools
tags: [browser-automation, cli, rust, cdp, mcp, accessibility-tree, agent-tooling, headless, snapshot-refs, chrome]
language: Rust
license: Apache-2.0
maturity: v0.31.0 (2026-06-25); active, Vercel Labs; CDP-based Rust daemon + CLI
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-26T17:22:26Z
  default_branch: main
  default_branch_sha: ed2e10598c9064aecfaeb7cf21b540684db4be2c
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:55:59Z
  overall: B
  overall_score: 3.0
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 7
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 118.9
        qualifying_issues: 13
        band: relaxed_solo
        window_offset_days: 12
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: agent-browser
        dependent_repos_count: 0
        downloads_last_month: 2005864
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 2.17
    longevity:
      grade: D
      raw:
        repo_age_days: 173
        last_commit_age_days: 7
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 96
        top1_share: 0.67
        top3_share: 0.766
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Agent Browser

A native Rust CLI + daemon (from Vercel Labs) that drives a real Chrome over CDP for AI agents: each `snapshot` hands the model an accessibility tree with stable element refs (`@e1`, `@e2`), so the agent acts on `@e1` instead of writing brittle CSS selectors.

![agent-browser — health radar](../../../assets/health/agent-browser.svg)

## When to use

You're building a coding agent or a shell-driven automation that has to operate real websites — log into a dashboard, fill a multi-step form, scrape a table, verify a deploy preview rendered. You don't want to embed a Node.js Playwright library inside the agent and you don't want the model inventing CSS selectors that snap the moment the markup changes. What you want is a command the agent can shell out to, plus a stable handle on each element that the LLM can reason about.

You install `agent-browser` (npm, Homebrew, or cargo), run `agent-browser install` once to fetch Chrome for Testing, then the loop is: `agent-browser snapshot -i` returns the interactive accessibility tree with refs, the model picks `@e2`, and you run `agent-browser click @e2` or `agent-browser fill @e3 "value"`. Every command takes `--json` for machine parsing. Because the daemon persists between commands, you don't pay a browser-launch cost per action — handy when an agent issues dozens of steps. When you'd rather wire it into Claude Code / Cursor as tools instead of shelling out, `agent-browser mcp` exposes the same operations over MCP. Session cookies/localStorage auto-save and restore, so a logged-in flow survives across runs.

## When NOT to use

- **You want an in-page, no-backend NL copilot.** Agent Browser drives an *external* Chrome from the CLI; it does not run inside your app's existing browser tab/session. For an embeddable in-page GUI agent, use [page-agent](page-agent.md) instead.
- **You're writing a normal Node.js test/automation library.** It's a CLI + daemon, not an importable JS API. If your code lives in TypeScript and wants `await page.click(...)`, plain Playwright/Puppeteer is the better fit.
- **You need vision-first / pixel-precise interaction.** Selection is anchored on the accessibility tree, not screenshots. Canvas/WebGL UIs, pixel-coordinate clicks, or content absent from the a11y tree are weak spots; annotated screenshots aren't supported on the Safari/WebDriver backend yet.
- **You need a managed cloud browser fleet out of the box.** It runs a local Chrome by default; large-scale concurrent/headless fleets mean wiring up a cloud provider plugin (Browserbase, Browser Use, Kernel, etc.) and operating that yourself.
- **Cross-engine breadth as a hard requirement.** Core path targets Chrome over CDP; non-Chromium/Safari coverage is partial (`[推断]` feature parity lags the Chrome path).
- **Maturity / churn.** It is pre-1.0 and shipping fast (multiple releases per week), so the CLI surface and config can shift between versions — pin a version if you script against it.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [page-agent](page-agent.md) | ✅ | Choose page-agent when you need an in-page JS GUI agent reusing the user's browser session. | In-page JS GUI agent that reuses the user's own browser session, no backend, NL commands. Agent Browser instead drives an external Chrome from a CLI/daemon — better for server-side/agent automation, worse for embedding in a live page. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | ✅ | Choose Chrome DevTools MCP when you need Google's official MCP server exposing Chrome DevTools. | Google's MCP server exposing Chrome DevTools to agents — MCP-only, official DevTools surface. Agent Browser is CLI-first *and* ships an MCP mode, with snapshot-ref ergonomics and a persistent Rust daemon. |
| [Cua](cua.md) | ✅ | Choose Cua when you need a computer-use framework driving a full desktop/VM. | Computer-use agent framework driving a full desktop/VM (vision-based). Agent Browser is browser-only and a11y-tree-based — lighter and more deterministic, but can't operate native desktop apps. |
| [Playwright](../playwright-family/playwright.md) / Puppeteer | partly indexed | Choose Playwright or Puppeteer when you want mature code-first Node automation libraries. | Mature Node.js automation libraries with cross-browser support and rich APIs — but you import them as code and write/maintain selectors; Agent Browser is a CLI with LLM-friendly refs and no per-command launch cost. |
| [browser-use](browser-use.md) | ✅ | Choose browser-use when you need a Python browser agent with a batteries-included LLM loop. | Python, vision+DOM browser agent with batteries-included LLM loop. Agent Browser is a lower-level Rust CLI primitive (you supply the agent loop), faster to shell out to and MCP-native. |

## Tech stack

- **Language:** Rust (native CLI binary + persistent daemon).
- **Browser control:** direct Chrome DevTools Protocol (CDP) — "pure Rust daemon", no Node.js or Playwright in the runtime path.
- **Browser engine:** Chrome for Testing (auto-downloaded via `agent-browser install`) or a custom `--executable-path`.
- **Model integration:** built-in MCP server (`agent-browser mcp`) with typed tools; `--json` output on every command for shell/agent parsing.
- **Selection model:** accessibility-tree snapshots with stable element refs (`@e1`…), stable tab IDs (`t1`…), annotated screenshots with numbered overlays.
- **Extras:** network interception (route/mock/block), session persistence (cookies/localStorage), React DevTools inspection, Web Vitals (LCP/CLS/TTFB/FCP/INP), streaming WebSocket viewport preview, plugin system (out-of-process over stdio), cloud provider plugins (Browserbase, Browser Use, Kernel, AgentCore, Browserless), iOS Simulator via Appium.

## Dependencies

- **Runtime:** the native `agent-browser` binary + a Chrome/Chromium install (fetched by `agent-browser install`, or pointed at via `--executable-path`). No Node.js needed to *run* commands.
- **Install:** `npm install -g agent-browser`, `brew install agent-browser` (macOS), or `cargo install agent-browser`.
- **Build from source only:** Node.js 24+, pnpm 11+, and Rust.
- **Optional:** an MCP-capable client (Claude Code / Cursor) for `agent-browser mcp`; a cloud browser provider account for the fleet plugins; Appium + iOS Simulator for Safari-on-iOS.

## Ops difficulty

**Low-to-medium.** For a single local Chrome it's close to drop-in: one global install, one `agent-browser install`, then shell out. The daemon model means you manage a long-lived process (lifecycle/restore handling has been an active area across recent releases, so watch daemon-compatibility on upgrades). Difficulty rises to **medium** once you run headless at scale (wiring and paying for a cloud provider plugin), reuse Chrome profiles (Windows requires closing Chrome first), or depend on the Safari/WebDriver/iOS paths where feature parity is partial. Default operation timeout is 25s, just under the 30s CLI read timeout — relevant when scripting slow pages.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 118.9 hours across 13 qualifying issues/PRs.
- **Maintenance — very active.** Last pushed 2026-06, not archived, shipping fast (multiple releases per week; latest v0.31.0 on 2026-06-25). Daemon lifecycle/restore handling is an actively-moving area — watch daemon compatibility on upgrades. `[未验证]`
- **Governance / backing — Vercel Labs.** **Organization**-owned (`vercel-labs/agent-browser`); a `-labs` repo signals an experiment/incubation surface rather than a flagship product, so backing is real but the longevity commitment is softer than a core Vercel product. `[推断]` ~37.2k stars [未验证]; the org (not a lone maintainer) reduces bus-factor risk relative to single-owner repos.
- **Age & Lindy — young, unproven (created 2026-01, ~5 months as of 2026-06).** Pre-1.0 and too new for a Lindy prior; the heavy release cadence means CLI flags and config schema shift between versions. Pin a version if you script against it.
- **Risk flags — pre-1.0 churn + partial cross-engine parity.** Apache-2.0, no relicense/open-core observed. The real flags are API churn and that non-Chromium/Safari coverage lags the Chrome-over-CDP path [推断]; cloud-fleet use pulls in third-party provider plugins you operate yourself.

## Caveats (unverified)

- `[未验证]` Star count ~37.2k as of 2026-06-26 (from `gh repo view`); GitHub stars are unreliable and date-sensitive — treat as indicative only.
- `[未验证]` Feature list (React DevTools, Web Vitals, network interception, iOS Simulator, cloud plugins) is drawn from the README; not all features were exercised first-hand.
- `[推断]` Non-Chromium / Safari-WebDriver coverage lags the primary Chrome-over-CDP path (annotated screenshots explicitly unsupported there); exact parity per command is not enumerated.
- `[未验证]` "No per-command browser-launch cost" / startup-speed advantage vs Playwright is the project's framing (daemon persistence), not an independent benchmark.
- `[推断]` Pre-1.0 with multiple releases per week — CLI flags and config schema may change between versions; behavior pinned here is as of v0.31.0.
