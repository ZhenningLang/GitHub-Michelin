---
name: OpenFang
slug: openfang
repo: https://github.com/RightNow-AI/openfang
category: agent-services
tags: [autonomous-agents, agent-os, rust, mcp, scheduler, channels, self-hosted]
language: Rust
license: Apache-2.0 OR MIT
maturity: "v0.6.9, pre-1.0, ~18.2k stars (as of 2026-09)"
last_verified: 2026-09-27
type: framework
upstream:
  pushed_at: 2026-07-02T08:13:12Z
  default_branch: main
  default_branch_sha: acf2587e46be174c10200489c9a2d23a39a98aeb
  archived: false
health:
  schema: 1
  computed_at: 2026-09-27T16:44:24Z
  overall: C
  overall_score: 2.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 138
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 87791
        release_assets: 2262
        release_tier: D
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 215
        last_commit_age_days: 138
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 64
        top1_share: 0.582
        top3_share: 0.653
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# OpenFang

A Rust "agent operating system" that ships as a single self-contained binary: it runs autonomous agents ("Hands") on schedules — 24/7, without you prompting them — with a built-in kernel, scheduler, WASM tool sandbox, MCP support, and 40 messaging-channel adapters.

![openfang — health radar](../../../../assets/health/openfang.svg)

## When to use

You're a solo founder or small ops team and you want an agent that *does work on a timer*, not one you babysit in a chat box. Think: scrape leads and score them against your ICP every morning, run an OSINT change-detection sweep on competitors, draft and schedule X/Twitter posts, or have a research agent cross-reference sources and hand you a cited brief — all running unattended on a box you control. You don't want to stitch together a Python framework plus a cron daemon plus a queue plus a dashboard plus per-channel webhook glue; you want one process that already has the scheduler, the persistence, the channel adapters, and the guardrails baked in. OpenFang resolves this by being an "OS" rather than a library: you `openfang init`, drop in a Hand (a `HAND.toml` manifest + system prompt + skill doc + approval gates), and it runs on its schedule, talks to you over Telegram/Discord/Slack/WhatsApp, and logs every action to a tamper-evident audit chain.

It also fits when you care about footprint and self-hosting. The whole thing is one ~32 MB Rust binary with low idle memory, so it's plausible on a small VPS or a homelab box where a heavyweight Python agent stack would feel wrong, and the WASM sandbox plus capability-based access control give you a security story for letting an agent touch the open web and your accounts. If you're migrating off OpenClaw, OpenFang explicitly courts that crowd with a migration path (a dedicated `migrate` crate and README section, verified 2026-09).

## How it works

OpenFang installs as a single Rust binary and runs as a daemon: `openfang init` walks you through LLM-provider setup, `openfang start` boots a kernel that owns the scheduler, SQLite persistence, the web dashboard (`localhost:4200`), and the MCP/tool layer. An agent in this model is a **Hand** — either one of the 7 bundled personas (researcher, lead, coder, …) or one you author as a `HAND.toml` manifest declaring tools, settings, and metrics, plus a system prompt and skill docs; everything ships compiled into the binary, "no downloading, no pip install, no Docker pull." Activate a Hand (`openfang hand activate researcher`) and the scheduler runs it on its own cadence — it reaches your configured providers (README claims 27) and executes tools inside a **WASM sandbox** (WebAssembly: tools run in an in-process VM under capability-based access control rather than with the daemon's full shell), while each action lands in a Merkle hash-chained, tamper-evident audit trail. Chat with a Hand (`openfang chat researcher`), or let it reach *you* over one of ~40 channel adapters. What stays yours: provider API keys, channel credentials, scoping approval gates and capabilities, and — given pre-1.0 status — pinning a known-good version.

![OpenFang — backbone user story](../../../../assets/flow/openfang.svg)

<!-- flow-steps:begin (generated from flows/openfang.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the single binary — `curl -fsSL https://openfang.sh/install | sh`
2. **You**: Set up providers, then start the daemon (dashboard on :4200) — `openfang init · openfang start`
3. **You**: Activate a bundled Hand — or author your own HAND.toml — `openfang hand activate researcher`
4. **OpenFang**: Runs the Hand on its schedule, LLM calls and tools inside the WASM sandbox — component: `kernel + scheduler`
5. **OpenFang**: Reports over your connected chat channel and logs every action to the audit chain — component: `channel adapters`

**Value**: Agents that do work on a timer, unattended — one process instead of cron + queue + webhooks + dashboard glue

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You want a conversational, in-the-loop orchestration library, not an OS.** If you're building a request/response agent inside your own app and need fine-grained control over the graph of LLM calls, a library like [DSPy](../../workflow-builders/dspy.md), LangGraph, or [AgentScope](../agent-sdks/agentscope.md) fits the shape better — OpenFang owns the runtime, scheduler, and process model, which is the opposite of "drop into my service."
- **You need a mature, API-stable foundation.** It is explicitly pre-1.0: the README warns to expect rough edges and breaking changes between minor versions and to pin a specific commit for production. Building a business-critical pipeline on it today means absorbing churn.
- **Single-vendor, young project — and the public repo has gone quiet.** Created 2026-02 and driven by one company (RightNow); as of 2026-09 the default branch has **no commits since 2026-05-12** (~4.5 months) and the release line is still v0.6.9 from that date (any-branch pushes continued to 2026-07). A young single-org project that has stopped landing code on `main` carries abandonment and direction-change risk a multi-maintainer foundation project does not. [推断：停滞判读基于公开提交，私有开发与否不可见]
- **You don't trust the benchmark/feature framing.** The README leads with self-run comparisons (cold start, idle memory, "16 security systems", "only one with channel adapters"). These are first-party and unaudited — do not select on them without your own measurement. [未验证]
- **You need a language/runtime your team can extend.** It's Rust end-to-end; if nobody on the team writes Rust, authoring new tools/Hands beyond the bundled ones (vs. just configuring) will be costly.
- **Compliance/data-residency or multi-tenant SaaS at scale.** It targets self-hosted single-operator/small-team autonomy on SQLite-backed local persistence; it is not a managed, horizontally-scaled multi-tenant control plane.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [DSPy](../../workflow-builders/dspy.md) | ✅ | Choose DSPy when you need a Python framework for *programming* and optimizing LLM pipelines. | A Python framework for *programming* (and optimizing) LLM pipelines; you embed it in your app. OpenFang is the opposite: an autonomous runtime/OS that owns scheduling and execution, not a library you call. |
| [AgentScope](../agent-sdks/agentscope.md) | ✅ | Choose AgentScope when you need a developer framework with explicit control over multi-agent apps. | Developer framework for building/orchestrating multi-agent apps with explicit control; OpenFang trades that control for a batteries-included, schedule-driven OS with channels and guardrails built in. |
| [Symphony](symphony.md) | ✅ | Choose Symphony when your work arrives as tracker issues (Linear/GitHub/Jira/Asana/GitLab) and you want each one turned into an isolated Codex implementation run ending in a PR; stay with OpenFang when you want standing scheduled agents across many providers and chat channels instead. | Symphony is a narrow OpenAI-shaped orchestrator (Codex-only, preview-stage, in-memory state) published as a spec; OpenFang owns the whole runtime — scheduler, 27-provider drivers, channels, audit chain — but no first-party coding-agent pipeline. |
| [claude-octopus](../../coding-agents/orchestration-and-review/claude-octopus.md) | ✅ | Choose claude-octopus when all you need is several Claude Code agents working a repo in parallel — a purpose-built driver, not a platform to run an agent estate on. | A narrower Claude-centric orchestration tool; OpenFang trades that focus for a general 27-provider OS with scheduler, channels, and audit chain — more surface to learn and operate. |
| [LangGraph](../agent-sdks/langgraph.md) | ✅ | Choose LangGraph when you need the default Python choice for stateful, interactive agent graphs inside your own service. | The default Python choice for stateful, interactive agent graphs inside your own service; no built-in scheduler/channels/binary distribution. OpenFang inverts this as a standalone OS. |
| [OpenClaw](../personal-assistants/openclaw.md) | ✅ | Choose OpenClaw when you need the project OpenFang positions itself against and offers a migration path from. | The project OpenFang positions itself against and offers a migration path from; OpenFang claims smaller footprint and the OS framing. Verify the comparison yourself. |
| [CrewAI](../agent-sdks/crewai.md) / [AutoGen](../agent-sdks/autogen.md) | ✅ | Choose CrewAI or AutoGen when you need role/conversation-oriented Python frameworks for in-app workflows. | Role/conversation-oriented multi-agent Python frameworks for in-app workflows; not single-binary autonomous runtimes. |

## Tech stack

- **Language:** Rust (primary, ~86% of bytes per the GitHub languages API, 2026-09), with HTML/JS/CSS (~10% combined) for the dashboard and a Tauri 2.0 desktop shell; small Python/Shell/PowerShell installers.
- **Structure:** a Cargo workspace of ~14 crates — kernel (orchestration/scheduler/RBAC), runtime (agent loop, LLM drivers, tools, WASM sandbox, MCP), api (REST/WS/SSE, OpenAI-compatible), channels, memory, wire (P2P protocol), CLI, desktop, migrate (crate count/LOC per README).
- **Datastore:** SQLite for persistence plus vector embeddings for memory.
- **Sandbox/security:** WASM tool sandbox, capability-based access control, Merkle hash-chain audit trail, Ed25519 signing, prompt-injection scanning, SSRF protection.
- **LLM/MCP:** Model Context Protocol support; many provider drivers (Anthropic, OpenAI, Gemini, Groq, DeepSeek, Ollama, vLLM, and more — README claims 27 providers / 123+ models).
- **Channels:** ~40 messaging adapters (Telegram, Discord, Slack, WhatsApp via QR gateway, Signal, Matrix, Email, Teams, etc.).

## Dependencies

- **Runtime:** a single self-contained binary (~32 MB per README); no external service required to start. Installs via `curl … | sh` (macOS/Linux) or PowerShell (Windows).
- **Optional:** Node.js ≥ 18 only for the WhatsApp Web (QR) gateway, which listens on port 3009; dashboard on port 4200 by default.
- **Build-from-source:** a recent Rust toolchain / Cargo (it's a large workspace; full builds are non-trivial).
- **External:** API keys for whichever LLM provider(s) you route to; for local models, an Ollama/vLLM endpoint.

## Ops difficulty

**Low to run, medium to operate seriously.** The happy path is genuinely light: one binary, `openfang init` / `openfang start`, a local dashboard — closer to running a CLI daemon than deploying a Python ML stack, and the small footprint suits a VPS or homelab. Difficulty rises once it's doing real autonomous work: you're now responsible for an agent acting unattended against live accounts and the open web, so you must configure approval gates, scope capabilities, manage secrets/API keys, watch the audit log, and — given the pre-1.0 status — pin to a known-good commit and budget for breaking changes on upgrade. Building from source or authoring new Rust tools/Hands moves it toward **high** for non-Rust teams.

## Health & viability

- **Responsiveness**: Cannot be scored — unknown.
- **Maintenance — stalled on the default branch (as of 2026-09).** Last commit to `main` 2026-05-12 (~4.5 months before this check); latest release still v0.6.9 (2026-05-12, security patches for RUSTSEC advisories); `pushed_at` on other branches runs to 2026-07-02; not archived. In June this read as "actively developed pre-1.0"; by September the public default branch is quiet — treat momentum as unconfirmed and churn risk as now coming from staleness rather than velocity.
- **Governance & backing — single vendor.** Driven by one company (RightNow / `RightNow-AI`), not a foundation or multi-org community; the roadmap and continuity ride on that vendor. A single-vendor pre-1.0 project carries direction-change and abandonment risk a foundation project does not — and the mid-2026 public stall is exactly the shape of that risk materializing. [推断]
- **Age & Lindy — very young, unproven.** Created 2026-02, ~7 months old (as of 2026-09). No track record; firmly "young and hyped," not Lindy-safe — do not bet a business-critical pipeline on it without absorbing churn.
- **Adoption — stars up, releases flat.** ~18.2k stars and ~2.3k forks (GitHub API, 2026-09-27) — slight star growth since June (~17.9k) while the release line stayed at v0.6.9; 125 open issues suggest an engaged but unanswered user base. [推断：issue 积压含义未逐条阅读]
- **Risk flags — first-party benchmarks + young single-vendor + stall.** All headline numbers (cold start, memory, "27 providers / 40 channels", LOC) are unaudited README figures; license is dual MIT OR Apache-2.0 (no relicense history). The dominant risk is youth + single-vendor concentration + a quiet default branch, not licensing.

## Caveats (unverified)

- [未验证] Star count ~18.2k (18,209) as of 2026-09 — GitHub stars in the agent-framework space are unreliable and time-sensitive; treat as indicative only.
- [未验证] All benchmark numbers (cold start ~180 ms, idle memory ~40 MB, install size ~32 MB) and "16 security systems / 40 channels / 27 providers / 123+ models / 14 crates / 137k LOC / 1,767+ tests" are first-party README figures, not independently audited.
- [未验证] The "only framework with messaging channel adapters" and head-to-head latency/memory comparisons vs LangGraph/CrewAI/AutoGen/OpenClaw are the project's own framing; no third-party verification found.
- [推断] License is dual MIT OR Apache-2.0 (both LICENSE-MIT and LICENSE-APACHE present in repo; GitHub's API surfaces only Apache-2.0) — confirm acceptable terms for your use.
- [推断] Single-vendor (RightNow), created 2026-02; maintenance breadth and long-term direction are unproven for a project this young, and the default-branch stall since 2026-05-12 may be a pivot, private development, or drift — indistinguishable from outside.
- [未验证] v0.6.9 released 2026-05-12 ("security patches" for RUSTSEC advisories) re-confirmed as the latest release on 2026-09-27 (GitHub API); the four-month gap between checks produced no new tag.
- [推断] Exact crate/component layout, provider list, and channel list are summarized from the README (unchanged since the June check — same default-branch commit); verify specific provider/channel/Hand support against the current repo before relying on it.
