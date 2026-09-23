---
name: BrowserAct Skills
slug: browser-act-skills
repo: https://github.com/browser-act/skills
category: engineering
tags: [agent-skill, browser-automation, scraping, remote-assist, skill-pack]
language: Python
license: MIT
maturity: active, ~4,449 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-07-14T09:53:38Z
  default_branch: main
  default_branch_sha: 51daea1532eff83baeb1d6e7f1f54a424a5536a9
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:47:09Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 29
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 228
        last_commit_age_days: 29
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.913
        top3_share: 0.972
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---
# BrowserAct Skills

Agent-facing browser automation skill pack for BrowserAct: indexed browser control, stealth/private sessions, remote human handoff, and Skill Forge scraping workflows.

![browser-act-skills — health radar](../../../assets/health/browser-act-skills.svg)

## When to use

You're building or operating an agent that must use a real browser rather than a DOM-only library: logged-in pages, anti-bot friction, multi-session browsing, remote human takeover, or repeatable extraction workflows. Pick BrowserAct Skills when you want an LLM-oriented CLI and skill instructions: `state` returns indexed elements, actions target those indexes, and the skill exposes browser modes, remote assist, stealth extraction, and Skill Forge.

The deciding tradeoff versus plain Playwright is that BrowserAct optimizes for agent operation and handoff, not for a stable developer-authored test suite. Use it when the browser is part of an agent workflow; use Playwright when you are writing deterministic tests or automation code.

## When NOT to use

- **You need deterministic browser tests.** Use [Playwright](../../web-automation/playwright-family/playwright.md) for CI tests, trace viewer, fixtures, and code-first browser automation; BrowserAct is shaped for agent-driven sessions.
- **You cannot accept managed-service or paid-feature coupling.** The README says core automation is free, but stealth browsers beyond the first five and managed proxies are paid; choose Playwright or a self-hosted browser stack if that boundary is unacceptable.
- **Your target site forbids scraping or automation.** Use the site's official API or seek explicit permission instead of BrowserAct; anti-blocking features do not remove legal, contractual, or ethical constraints.
- **You do not want user browser state touched.** Use privacy-mode Playwright profiles or a disposable browser environment; BrowserAct supports Chrome login reuse and profile import, which must be governed carefully.
- **You only need static page-to-Markdown fetching.** Use a narrower URL-to-Markdown skill or document parser; BrowserAct's stealth/session stack is overkill for public static pages.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Playwright](../../web-automation/playwright-family/playwright.md) | ✅ | For test suites and developer-authored automation, pick Playwright; for agent sessions that need indexed actions, handoff, and stealth modes, pick BrowserAct Skills. | BrowserAct adds agent UX and service features; Playwright is more standard and easier to reason about in CI. |
| [Puppeteer](../../web-automation/browser-driver-frameworks/puppeteer.md) | ✅ | For simple Node.js browser scripts, Puppeteer may be enough; pick BrowserAct when agent-readable state, session naming, or human handoff matter. | Puppeteer is lighter and familiar; BrowserAct has more workflow surface and external feature boundaries. |
| Browserbase / hosted browser services | 未收录 | For hosted browser infrastructure, evaluate Browserbase-style services; pick BrowserAct when its skill/CLI workflow and free local modes fit better. | Hosted browsers reduce local setup but introduce stronger vendor dependency. |
| Custom site scraper skill | 未收录 | For one stable target with known APIs, write a custom skill; pick BrowserAct Skill Forge when you want an agent to discover and package the scraping flow. | Custom scrapers are narrower and easier to audit; Skill Forge is faster for exploratory extraction. |


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2026-07-14T09:53:38Z`; the health scorer grades maintenance `A`.
- **Adoption snapshot:** GitHub API reports ~4,449 stars as of 2026-07, plus a public docs/community surface in the README; adoption axis remains `?` because this is not a package-download style project.
- **License snapshot:** root `LICENSE` is MIT and GitHub metadata reports MIT.
- **Lindy / governance:** the repo is young, so longevity is `C`; governance is `D` in the health block because the scorer sees concentrated contributions.
- **Risk flags:** anti-blocking, remote assist, profile import, proxies, cookies, and third-party sites create operational and policy risk; require explicit authorization and secret handling in real use.

## Caveats (unverified)

- [未验证] The stealth and anti-bot claims were read from the README but not independently tested against target websites.
- [未验证] Pricing and free-tier boundaries may change; verify BrowserAct's current service terms before relying on managed proxies or stealth-browser quotas.
- [推断] BrowserAct is best treated as an agent browser workflow layer rather than a replacement for deterministic browser test frameworks.
