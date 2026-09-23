---
name: Cua
slug: cua
repo: https://github.com/trycua/cua
category: agent-browser-tools
tags: [computer-use, desktop-automation, vm-sandbox, gui-agent, vision, litellm, osworld, screenspot, macos, windows, linux]
language: Python (HTML/Rust/Swift/TypeScript in repo)
license: MIT
maturity: multi-package monorepo; cua-agent v0.8.4, cua-sandbox v0.1.17, cua-cloud v0.1.1, cua-driver-rs v0.6.8 (pre-release), all updated 2026-06; active, trycua-maintained
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-29T08:11:15Z
  default_branch: main
  default_branch_sha: 7468487d303469b4993b960c8a2cb66289034bed
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:11:05Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 105.0
        qualifying_issues: 3
        band: default
        window_offset_days: 6
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@trycua/cua-driver-linux-x64-gnu"
        dependent_repos_count: 0
        downloads_last_month: 7562030
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.0
        homebrew_installs_90d: 603
        homebrew_tier: B
        release_downloads: 1847291
        release_assets: 1246
        release_tier: B
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 599
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 80
        top1_share: 0.434
        top3_share: 0.724
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Cua

Open-source infrastructure for **Computer-Use Agents**: VM/container sandboxes, a vision-driven Agent SDK, drivers, and benchmarks so an AI agent can control a *full desktop* (macOS, Windows, Linux, Android) by looking at the screen and clicking — not by scripting the DOM.

![cua — health radar](../../../assets/health/cua.svg)

## When to use

You're building an automation product that has to drive **arbitrary desktop applications**, not just web pages — think a workflow that opens a native macOS app, pastes data into a legacy Windows installer, then files something in a browser. Selector-based web tools fall apart the moment the task leaves the page, and you don't want to hand-stitch a VM, a screenshot pipeline, and a model loop yourself. You also need each run to be **isolated and disposable** so an agent misclick can't touch your real machine or another tenant's data.

You reach for **Cua**. You spin up an ephemeral sandbox with one async call — `Sandbox.ephemeral(Image.macos())` or `.linux()` / `.windows()` / `.android()` — and hand it to a `ComputerAgent` that drives the desktop from screenshots, the same API regardless of OS or runtime. Because the agent layer is built on liteLLM, you point it at whatever computer-use-capable model you already pay for (Anthropic, OpenAI, and others) rather than being locked to one vendor. On Apple Silicon you can run macOS guests locally via Lume/Lumier; for scale you push the same code to Cua Cloud. When you need to prove it works, Cua-Bench scores your agent on OSWorld / ScreenSpot / Windows Arena and can export trajectories to train on.

## When NOT to use

- **You only need to automate a web page.** A full desktop VM + screenshot loop is massive overkill for filling a form or scraping a site — use an in-page or browser-level tool ([page-agent](page-agent.md), Playwright, browser-use) where DOM access is faster, cheaper, and more deterministic than vision.
- **You need low latency / high throughput per action.** Vision agents take a screenshot, call a model, and act each step — slow and token-expensive compared to DOM/selector automation. Not a fit for tight real-time loops or huge parallel fan-out on a budget.
- **You can't run VMs/containers.** This is heavyweight infra: VMs, drivers, a computer-server. macOS guests realistically need Apple Silicon (Virtualization.framework); Linux Cua Drivers are flagged pre-release.
- **You want a single stable SDK with frozen APIs.** It's a fast-moving monorepo of many independently-versioned packages (agent, sandbox, computer-server, cli, bench, train, cloud) mostly at `v0.x` — expect churn and breaking changes.
- **Closed-loop pixel-perfect reliability matters more than coverage.** Computer-use models still misclick and hallucinate UI state; for compliance-critical or irreversible actions you need guardrails the framework doesn't provide for you.
- **Data egress is sensitive.** Screenshots of the desktop are sent to your chosen model provider — review privacy/compliance before pointing it at confidential apps, and watch per-screenshot token cost.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [page-agent](page-agent.md) | ✅ | Choose page-agent when you only need in-page DOM-as-text automation in the user's browser. | In-page JS GUI agent driving the DOM as text inside the user's own browser — no VM, no vision, far cheaper/faster, but web-only and can't touch native desktop apps. |
| [Chrome DevTools MCP](chrome-devtools-mcp.md) | ✅ | Choose Chrome DevTools MCP when you need a real Chrome exposed via DevTools Protocol over MCP. | Exposes a real Chrome via DevTools Protocol over MCP — strong for browser debugging/automation, but Chrome-scoped, not a full-desktop sandbox. |
| [Agent Browser](agent-browser.md) | ✅ | Choose Agent Browser when you need a lightweight headless browser automation CLI for agents. | Headless browser automation CLI for agents — lightweight web-task runner; no OS-level control or VM isolation. |
| OpenAI Operator / Anthropic computer use | 未收录 | Choose hosted computer-use products when turnkey proprietary vision agents are acceptable. | Hosted vision computer-use agents — turnkey but proprietary, tied to one model vendor; Cua is the open self-hostable infra layer (and can *run* such models via liteLLM). |
| OSWorld / WebArena (benchmarks) | 未收录 | Choose OSWorld or WebArena when you need evaluation environments rather than a runnable sandbox. | Evaluation environments Cua-Bench targets — they grade agents; Cua provides the runnable sandbox + agent that gets graded. |
| E2B / Daytona (dev sandboxes) | 未收录 | Choose E2B or Daytona when you need code-execution sandboxes for agents. | Code-execution sandboxes for agents — overlap on VM isolation, but oriented at running code, not screenshot-driving a GUI desktop. |

## Tech stack

- **Languages:** Python (Agent/Sandbox SDKs, computer-server), Rust (`cua-driver-rs` drivers), Swift (Lume — Apple `Virtualization.framework`), plus HTML/TypeScript in the repo.
- **Agent layer:** `cua-agent` — `ComputerAgent` loop driven by screenshots (vision), with **liteLLM** integration for model routing.
- **Sandboxing:** `cua-sandbox` SDK over Lume/Lumier (macOS/Linux VMs on Apple Silicon), Linux containers, local QEMU backends, and Cua Cloud (cua.ai).
- **Drivers:** `cua-driver-rs` / Cua Drivers — background desktop automation, also exposed as an MCP server.
- **Eval/training:** `cua-bench` (OSWorld, ScreenSpot, Windows Arena, custom tasks; trajectory export), `cua-train`.
- **Third-party:** Kasm (MIT), OmniParser (CC-BY-4.0), optional ultralytics (AGPL-3.0) — note the AGPL optional dep.

## Dependencies

- **Runtime:** Python ≥ 3.11 for the SDKs (`pip install cua`). A model endpoint usable by liteLLM (e.g. Anthropic / OpenAI computer-use-capable model) + API key.
- **Sandbox host:** for local macOS guests, an **Apple Silicon Mac** (Virtualization.framework via Lume); for Linux guests, containers or QEMU; Windows/Android guests per docs. Cua Cloud removes the local-host requirement.
- **Drivers:** installed via bash (macOS/Linux) / PowerShell (Windows) scripts; Linux driver support is pre-release.
- **Bench:** `uv tool install` for `cua-bench`.

## Ops difficulty

**Medium-to-high.** The Cloud path (cua.ai) is the easy on-ramp — managed sandboxes, no local VM to babysit. Self-hosting is heavier: you operate VMs/containers, a computer-server, and drivers, and on Apple Silicon you manage Lume/Lumier guest images. Across the many `v0.x` packages you'll track several independent version streams, and the vision agent loop adds ongoing **per-screenshot model cost/latency** plus the data-governance question of shipping desktop screenshots to a model provider. Linux drivers being pre-release means platform coverage is still uneven.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 105.0 hours across 3 qualifying issues/PRs.
- **Maintenance — active across many packages.** Last pushed 2026-06, not archived; the monorepo's packages (cua-agent v0.8.4, cua-sandbox v0.1.17, cua-cloud, cua-driver-rs v0.6.8, cua-bench) were all updated 2026-06. Active, but you track **several independent version streams**, and `cua-driver-rs`/Linux drivers are flagged pre-release. `[未验证]`
- **Governance / backing — single startup (trycua).** **Organization**-owned (`trycua/cua`), ~19k stars [未验证]. Backed by one venture-stage company behind the cua.ai hosted product — better than a lone maintainer, but its longevity is tied to that company's survival and funding. `[推断]`
- **Age & Lindy — young (created 2025-01, ~1.5 years as of 2026-06).** Old enough to show real benchmark integration (OSWorld/ScreenSpot/Windows Arena) but the many `v0.x` packages signal a pre-stable API; no Lindy prior yet. Expect breaking changes; pin per-package versions.
- **Adoption / ecosystem — credible niche.** Vision computer-use infra with benchmark+training surface and a hosted cloud on-ramp; model-agnostic via liteLLM rather than locked to one vendor — a real ecosystem signal for an early project.
- **Risk flags — open-core + AGPL optional dep.** MIT core, but the hosted Cua Cloud is the commercial layer (open-core tension), and the optional `ultralytics` dependency is **AGPL-3.0** — confirm whether your usage path pulls it in before assuming MIT-only licensing for a deployment. `[推断]` Desktop screenshots are also shipped to your model provider (data-governance flag).

## Caveats (unverified)

- [未验证] Star count ~19.0k (gh snapshot 2026-06-26) — GitHub stars are unreliable and date-sensitive; indicative only.
- [未验证] Package versions (cua-agent v0.8.4, cua-sandbox v0.1.17, cua-cloud v0.1.1, cua-driver-rs v0.6.8, cua-bench v0.2.11) read from the releases list dated 2026-06-24/26; treat exact numbers as snapshot-time.
- [推断] Specific supported model strings (e.g. Anthropic Claude / OpenAI computer-use-preview / UI-TARS / OmniParser loops) are inferred from the documented liteLLM integration and vision design, not quoted verbatim from a current supported-models table — verify against docs before relying on a given model.
- [推断] "Same API regardless of OS or runtime" and the `Sandbox.ephemeral(Image.macos())`-style snippet are paraphrased from the README's own framing; exact current API surface should be checked against the SDK.
- [未验证] Comparison substitutes (Operator, OSWorld/WebArena, E2B/Daytona) are partly inferred positioning from repo + secondary context, not all first-party confirmed.
- [推断] Optional ultralytics dependency is AGPL-3.0 — confirm whether your usage path pulls it in before assuming MIT-only licensing for a deployment.
