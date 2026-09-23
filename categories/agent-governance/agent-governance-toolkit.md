---
name: agent-governance-toolkit
slug: agent-governance-toolkit
repo: https://github.com/microsoft/agent-governance-toolkit
category: agent-governance
tags: [agent-governance, agent-governance-toolkit, tool]
language: Python
license: MIT
maturity: active, ~4,889 stars (as of 2026-07)
last_verified: 2026-07-16
type: tool
upstream:
  pushed_at: 2026-07-16T07:08:50Z
  default_branch: main
  default_branch_sha: a3b327de2648e7cdcc4bfda2f1cf7e69f7b59e20
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:38:34Z
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
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 118.4
        qualifying_issues: 29
        band: relaxed_solo
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: agent_governance_toolkit
        dependent_repos_count: 0
        downloads_last_month: 127874
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        release_downloads: 832
        release_assets: 83
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 204
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 97
        top1_share: 0.329
        top3_share: 0.721
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
# agent-governance-toolkit

Microsoft's public-preview governance toolkit for production AI agents: policy-gated tool calls, identity/trust, audit/compliance, MCP security gateway, SRE controls, and multi-language SDKs around agent frameworks.

![agent-governance-toolkit — health radar](../../assets/health/agent-governance-toolkit.svg)

## When to use

You are shipping AI agents that call tools, browse, query databases, delegate to other agents, or run through frameworks such as Semantic Kernel, AutoGen, LangGraph/LangChain, CrewAI, OpenAI Agents SDK, Claude Code, Google ADK, LlamaIndex, Haystack, Mastra, or MCP. Use agent-governance-toolkit when you need deterministic policy checks and audit records around agent actions rather than only prompt-level instructions.

It is strongest when governance has to be a product surface: YAML/Cedar/OPA-style policy evaluation, identity/trust, compliance CLI (`agt verify`, `agt lint-policy`, red-team scan), language SDKs (Python, TypeScript, .NET, Rust, Go), and framework adapters. The upstream README labels the project **Public Preview**, so use it as an actively developed governance stack with possible breaking changes before GA.

## When NOT to use

- **You need a stable GA contract today.** Upstream explicitly says Public Preview and warns about possible breaking changes before GA.
- **You need OS-level containment as the primary control.** The README states AGT works at the application middleware layer and recommends separate containers for OS-level isolation; do not treat it as a kernel sandbox.
- **You only need one small local policy check.** Open Policy Agent, Cedar, or a few lines of application middleware may be smaller than adopting AGT's full governance stack.
- **You cannot afford multi-language/package surface area.** The project spans Python, TypeScript, .NET, Rust, Go, Claude Code plugins, Copilot CLI, MCP, docs, compliance artifacts, and framework adapters; that breadth is operational weight.
- **Your risk model is content quality, not agent action governance.** Use eval/red-team tools for prompt quality and model behavior; AGT is about governing tool calls, identity, audit, compliance, and runtime controls.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Open Policy Agent | 未收录 | Choose OPA when you only need a general policy engine and already own the agent middleware. | Smaller and mature for policy decisions; AGT packages agent-specific identity, audit, compliance, and framework adapters. |
| Cedar / Cedarling | 未收录 | Choose Cedar when authorization semantics and fine-grained policy evaluation are the core requirement. | Strong policy model; AGT is broader and more agent-governance specific. |
| Custom middleware | 未收录 | Build custom when you only need to gate a handful of tools in one service. | Less dependency surface, but you must design audit, identity, enforcement points, and compliance evidence yourself. |
| Prompt-only safety rules | 未收录 | Use only for low-risk guidance where policy violations have low consequence. | Cheap to add, but not a deterministic control surface for tool execution. |


## Tech stack

- **Python-first monorepo** — Python packages provide the full stack; TypeScript, .NET, Rust, and Go packages expose core governance surfaces.
- **CLI and SDKs** — README documents `agt doctor`, `agt verify`, `agt red-team scan`, `agt lint-policy`, Python `govern()`, TypeScript `PolicyEngine`, .NET MCP integration, Rust, and Go examples.
- **Agent framework adapters** — documented integrations include Microsoft Agent Framework, Semantic Kernel, AutoGen, LangGraph/LangChain, CrewAI, OpenAI Agents SDK, Claude Code, Google ADK, LlamaIndex, Haystack, Mastra, Dify, and MCP.

## Dependencies

- **Python 3.10+** for the documented quick start; Node.js 18+ / npm 9+, .NET 8+, Go 1.25+, and Rust 1.70+ for the corresponding SDKs.
- **Package registries** — PyPI (`agent-governance-toolkit`), npm (`@microsoft/agent-governance-sdk` and related packages), NuGet, crates.io, plus source packages in the monorepo.
- **Optional Azure credentials** — README lists `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_CLIENT_SECRET` for Azure-integrated features.
- **Framework-specific hooks** — real deployment depends on where you insert AGT into your agent framework, MCP server, CLI, or plugin flow.

## Ops difficulty

**Medium to high.** `pip install agent-governance-toolkit[full]` and a two-line `govern()` wrapper are easy to try, but production rollout means defining policies, enforcement points, audit retention, identity/trust model, framework adapters, and OS/container boundaries.


## Health & viability

- **Maintenance snapshot (2026-07-16):** GitHub reports `archived=false` and `pushed_at=2026-07-16T07:08:50Z`; health scores maintenance and responsiveness as A.
- **Adoption snapshot:** ~4,889 GitHub stars as of 2026-07 and health found 127,874 last-month PyPI downloads for `agent_governance_toolkit`; treat this as early adoption, not a mature long-lived standard.
- **License snapshot:** MIT verified from GitHub metadata and root `LICENSE` in the read-only upstream check.
- **Lindy / governance:** the project is very young (health longevity D) but backed by Microsoft, has governance docs, maintainers docs, security policy, and broad contributor signals.
- **Risk flags:** Public Preview status, broad package surface, and middleware-level security boundary are the main practical risks.

## Caveats (unverified)

- [未验证] The README claims broad standards/framework coverage and many conformance tests; this pass read the README and license, not the full conformance suite.
- [未验证] Package split and legacy compatibility notes are moving quickly in Public Preview; pin exact versions before production rollout.
- [推断] Teams with only one or two internal tools may find AGT's breadth heavier than a small policy middleware.
