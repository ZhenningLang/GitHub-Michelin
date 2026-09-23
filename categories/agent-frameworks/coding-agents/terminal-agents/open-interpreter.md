---
name: Open Interpreter
slug: open-interpreter
repo: https://github.com/openinterpreter/open-interpreter
homepage: https://www.openinterpreter.com/
category: terminal-agents
tags: [coding-agent, terminal, codex-fork, harness, code-execution, mcp, acp, local-models]
language: Rust
license: Apache-2.0
maturity: rust-v0.0.17 (2026-07), active rewrite; ~64k stars (2026-07)
last_verified: 2026-07-01
type: framework
aka: [oi, interpreter]
upstream:
  pushed_at: 2026-07-06T01:41:29Z
  default_branch: main
  default_branch_sha: f3db7fff78125b0d6595e46bcbf43929b1c862a7
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:36:24Z
  overall: A
  overall_score: 3.5
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 3
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 164.5
        qualifying_issues: 26
        band: default
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: open-interpreter
        dependent_repos_count: 7
        downloads_last_month: 242577
        graph_tier: D
        volume_tier: B
        cross_check_divergence: 5.11
        release_downloads: 85381
        release_assets: 743
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1166
        last_commit_age_days: 3
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 363
        top1_share: 0.161
        top3_share: 0.298
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

# Open Interpreter

A terminal coding agent that is a **fork of OpenAI's Codex CLI**, re-focused on an *emulated agent harness* that squeezes good behavior out of low-cost / open models (DeepSeek, Kimi, Qwen) — it runs commands and edits files in a native OS sandbox, switches model + harness from a TUI, and exposes skills/MCP/hooks/`AGENTS.md`.

![open-interpreter — health radar](../../../../assets/health/open-interpreter.svg)

> **Identity change — read this first.** The project you may remember — the Python "natural-language interface for your computer" REPL that wrote and executed code locally — is *not* what this repo ships today. That Python codebase last shipped `v0.4.2` (2024-10) and now lives on as a community fork at [`endolith/open-interpreter`](https://github.com/endolith/open-interpreter). The `openinterpreter/open-interpreter` repo was rewritten in **Rust as a Codex fork** and relaunched mid-2026. Everything below describes the *current* Rust project. If you want the old Python tool, use the community fork, not this page.

## When to use

You're a developer who likes the Codex / Claude Code terminal-agent workflow but doesn't want to pay frontier-model prices for every loop. You've got access to cheaper or open-weight models — DeepSeek, Kimi, Qwen, or a local server — and you've noticed they behave worse than the closed models *not* because they're hopeless, but because the agent harness around them (system prompt, tool framing, edit format, step discipline) was tuned for someone else's model. You install Open Interpreter, type `i`, and pick a model with `/model`; then you switch the **harness** with `/harness` — `native`, `claude-code`, `kimi-cli`, `qwen-code`, `deepseek-tui`, `swe-agent`, `minimal` — to find the prompt/tool scaffolding that gets the most out of *your* model. The agent runs shell commands and edits files inside OS-native sandboxing, can drive a real browser or native apps via a built-in QA skill, and can run as an [Agent Client Protocol](https://agentclientprotocol.com/) agent so your editor talks to it. Because it inherits Codex's machinery, you also get `exec`, MCP, skills, hooks, permissions, and `AGENTS.md` support out of the box.

It fits when the harness *is* the point: you're benchmarking or productionizing low-cost models for coding and want a maintained, Codex-grade runtime where the model-specific scaffolding is a first-class, swappable knob rather than something you re-implement per provider.

## When NOT to use

- **You are about to run an LLM coding agent on a machine that matters — understand the execution risk first.** This is an agent that runs shell commands and edits files based on model output. It ships "native sandboxing" and a permissions/approvals layer, but a sandbox + approvals is mitigation, not immunity: prompt-injected or simply wrong model output can still delete files, exfiltrate secrets, or run destructive commands within whatever scope you approve. Treat it like Codex/Claude Code — review what it does, scope its access, never point it at production credentials, and read the [sandbox & approvals docs](https://www.openinterpreter.com/docs/terminal/sandbox) before trusting it. The risk is *inherent to agentic code execution*, not a bug to wait out. [推断]
- **You wanted the old Python "talk to your computer" REPL.** It's gone from this repo (see the note above). Building on `openinterpreter/open-interpreter` expecting the Python `interpreter` package / API will break — that API is the community fork's, not this one's.
- **You need a stable API or production track record for *this* codebase.** The Rust rewrite is at `rust-v0.0.17` (2026-06) — a `0.0.x`, weeks-old line. Expect churn, breaking changes, and rough edges; this is not a frozen, battle-tested release despite the repo's high star count (those stars were earned by the *Python* project). [推断]
- **You want a library/SDK to *build* multi-agent systems.** This is an end-user terminal coding agent (plus an ACP/SDK surface), not an orchestration framework for composing many agents with graphs, message passing, and durable state. For that, reach for a runtime like [AgentScope](../../agent-runtimes/agent-sdks/agentscope.md) or LangGraph, not this.
- **You'd rather use the canonical upstream.** Since it's a Codex fork, if you don't specifically need the low-cost-model harness emulation, OpenAI's own Codex CLI (or Claude Code) is the upstream with the larger team and faster mainline — Open Interpreter rides their `main` and adds a layer on top.
- **Cost/latency of a model-in-a-loop still bites — just less.** The premise lowers per-token cost by using cheaper models, but an agent that iterates (run → observe → edit → re-run) still spends many calls; cheap models can also need *more* steps to converge, eating part of the savings, and agentic code-gen remains non-deterministic and sometimes wrong.
- **You need the browser/native-app QA mode to be reliable.** OS/computer-control and app-driving via external tools (agent-browser, trycua) is inherently fragile across OS versions, app updates, and screen states; useful, but don't build a critical workflow on it without your own guardrails. [未验证]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| OpenAI Codex CLI | 未收录 | Choose OpenAI Codex CLI when you want the canonical upstream that Open Interpreter forks. | The **upstream** Open Interpreter forks. Canonical, larger team, faster mainline; tuned for OpenAI models. Open Interpreter adds the swappable low-cost-model harness layer on top and tracks Codex's `main`. |
| Claude Code / similar vendor coding-CLI | 未收录 | Choose Claude Code or a similar vendor CLI when you need polished terminal coding agents tied to a model family. | Polished, vendor-backed terminal coding agents tied to a specific model family; more turnkey but not built around emulating harnesses for arbitrary cheap/open models. |
| [aider](aider.md) | ✅ | Choose aider when you need a mature, model-agnostic terminal pair-programmer for git-aware edits. | Mature, model-agnostic terminal pair-programmer focused on git-aware edits across many providers; lighter and longer-lived, but not a Codex-derived sandboxed harness-switching runtime. |
| [smolagents](../../agent-runtimes/agent-sdks/smolagents.md) | ✅ | Choose smolagents when you need a tiny *library* for building code-acting agents you embed and own. | A tiny *library* for building code-acting agents you embed and own — the opposite end: you write the loop, vs. Open Interpreter being a full end-user coding-agent app. |
| endolith/open-interpreter (the old Python OI) | 未收录 | Choose the old Python Open Interpreter when you need the original natural-language computer REPL. | The **original** Python "natural-language interface for computers" REPL, now community-maintained. Choose this if you actually wanted the legacy Python tool; expect community-pace maintenance. |

## Tech stack

- **Core:** Rust (the `codex-rs` workspace, inherited from OpenAI Codex — many crates: cli, exec, MCP, sandbox, ACP server, etc.). A thin `codex-cli` / npm packaging layer and a docs site also live in-repo.
- **Agent harness layer:** Open Interpreter's distinctive addition — selectable harnesses (`native`, `claude-code`, `claude-code-bare`, `kimi-cli`, `qwen-code`, `deepseek-tui`, `swe-agent`, `minimal`) switchable at runtime via `/harness`, each a different prompt/tool/edit scaffolding tuned per model family.
- **Execution & sandboxing:** runs commands inside native OS sandboxing on macOS, Linux, and Windows, with an `exec` surface, a permissions/approvals model, hooks, and `AGENTS.md` support (all Codex-lineage).
- **Interfaces:** interactive terminal TUI (`i` / `interpreter`); Agent Client Protocol agent (`interpreter acp`) for editors; an SDK directory; MCP client support; a built-in QA skill that drives web apps (agent-browser) and native apps (trycua).
- **Models:** provider/model switching from the TUI (`/model`), aimed at low-cost / open models (DeepSeek, Kimi, Qwen) and others; provider config per the docs.

## Dependencies

- **Install:** a shell one-liner (`curl … openinterpreter.com/install | sh`) on macOS/Linux or a PowerShell command on Windows — note this pipes a remote script to a shell; review it if that's a concern. Prebuilt installers are served directly.
- **Build from source:** a Rust toolchain plus **Bazel** (the repo uses Bazel/`MODULE.bazel`, with Cargo workspaces underneath) and `pnpm` for the JS/packaging side — a non-trivial polyglot build (inferred from the manifests; see Caveats).
- **Runtime:** at least one model backend (a hosted provider API key or a local model server). No bundled model.
- **Optional integrations:** MCP servers; `agent-browser` (Vercel Labs) for web QA; `trycua` for native-app control — each an external dependency you opt into.
- **State:** config and session state stored locally under `~/.openinterpreter`.

## Ops difficulty

**Low to run, medium to run *safely*, high to build from source.** Using it is a one-line install and `i` — no servers, no datastore, state is a local dir. The real operational weight is the same as any code-executing agent: deciding and enforcing what it's allowed to do (sandbox scope, approvals, credentials it can see), watching token spend across iterative loops, and accepting non-deterministic results. Building from source is the hard path: a Bazel + Cargo + pnpm polyglot toolchain. And because it tracks Codex's fast-moving `main` and is itself on a `0.0.x` line, expect frequent updates and occasional breakage on upgrade.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 164.5 hours across 26 qualifying issues/PRs.
- **Maintenance — active, mid-rewrite (as of 2026-06).** Last push 2026-06-20; not archived; the Rust line is releasing (`rust-v0.0.16`/`rust-v0.0.17` both 2026-06-20). But note the **gap**: the prior (Python) releases ended at `v0.4.2` on 2024-10-24, so the project went roughly **~20 months without a tagged release** before the Rust relaunch — a real discontinuity, not steady cadence. The "active" verdict applies to the *new* codebase, which is brand-new. [推断]
- **Governance & bus factor — founder + upstream Codex contributors.** Organization-owned (`openinterpreter`); commit history is dominated by the founder ("killian") plus a stream of OpenAI Codex contributors via "Merge upstream Codex main" commits — i.e. much of the engineering is *inherited* from OpenAI's Codex team, while the OI-specific layer rests heavily on a small core. The project's roadmap is coupled to a fork it does not control. [推断]
- **Age & Lindy — repo is old, the *current* product is not.** The repo dates to 2023-07 (~3 years), but the thing it ships today (Rust Codex fork) is only weeks/months old. The Lindy prior from age does **not** transfer: an old repo that just threw away its codebase and identity is closer to a young project than a proven one. The ~64k stars were earned by the discontinued Python tool and say little about the new one's durability. [推断]
- **Adoption & ecosystem — large brand, unproven new form.** Big mindshare and star count from the original era, an active Discord and docs site; but adoption of the *Rust/Codex-fork* incarnation is early and unmeasured. [未验证]
- **Risk flags — strategic dependency on a fork + intrinsic code-execution risk, not licensing.** Apache-2.0 (no relicense history). The durable risks are: (1) it lives or dies by tracking OpenAI's Codex upstream and the small OI core that maintains the harness layer; (2) it is an agent that executes model-generated commands — an inherent attack surface — so its sandbox/approvals are load-bearing. [推断]

## Caveats (unverified)

- [未验证] Repo facts as of 2026-07-01 via GitHub API: created 2023-07-14, last push 2026-06-20, not archived, ~64.2k stars, ~5.6k forks, Apache-2.0, language reported as Rust, owner type Organization. Stars/forks are noisy and date-sensitive — and here the star count predates the rewrite, so it overstates the new codebase's traction. Treat as indicative only.
- [未验证] Latest release `rust-v0.0.17` (2026-06-20), preceding `rust-v0.0.16` (2026-06-20); the last *Python-era* release was `v0.4.2` (2024-10-24, marked prerelease). The ~20-month release gap is inferred from the releases list, not a maintainer statement.
- [推断] "Fork of OpenAI's Codex" and "emulating the agent harness for low-cost models" are the project's own README framing, corroborated by the repo containing `codex-rs`/`codex-cli`/`.codex` trees, a CHANGELOG that points to `openai/codex/releases`, and "Merge upstream Codex main" commits — but the exact divergence from upstream Codex is not audited here.
- [未验证] The harness list (`native`, `claude-code`, `claude-code-bare`, `kimi-cli`, `qwen-code`, `deepseek-tui`, `swe-agent`, `minimal`), the QA skill's browser/native-app drivers (agent-browser, trycua), ACP support, and MCP/hooks/permissions are from the current README; exact behavior, stability, and per-OS support are not verified here.
- [未验证] The original Python project "lives on as a community fork at endolith/open-interpreter" is stated in this repo's README; the fork's own maintenance status was not independently verified.
- [推断] The from-source build using Bazel + Cargo + pnpm is inferred from the repo's `MODULE.bazel`, `Cargo.toml`, and `pnpm-lock.yaml`; the exact supported build path may differ — follow the install/build docs.
- [未验证] "Native sandboxing on macOS, Linux, and Windows" and the approvals model are README claims (Codex-lineage); their precise isolation guarantees are not audited — do not treat the sandbox as a hard security boundary without verifying.
