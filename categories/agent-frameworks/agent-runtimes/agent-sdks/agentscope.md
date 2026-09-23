---
name: AgentScope
slug: agentscope
repo: https://github.com/agentscope-ai/agentscope
category: agent-sdks
tags: [multi-agent, llm-agent, react-agent, observability, message-passing, mcp, tool-use, async, human-in-the-loop]
language: Python
license: Apache-2.0
maturity: v2.0.2, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-29T06:35:40Z
  default_branch: main
  default_branch_sha: 3467754dc48c7ba12cfce79fae6e0fa39831074b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:30:42Z
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
      grade: A
      raw:
        median_ttfr_hours: 11.6
        qualifying_issues: 19
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: agentscope
        dependent_repos_count: 0
        downloads_last_month: 321531
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.02
        release_downloads: 56
        release_assets: 3
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 985
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 90
        top1_share: 0.415
        top3_share: 0.652
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

# AgentScope

A Python framework for building and serving multi-agent LLM applications, leaning on model reasoning/tool-use over rigid orchestration, with a unified event bus, fine-grained tool permissions, and OpenTelemetry tracing baked into the agent loop.

![agentscope — health radar](../../../../assets/health/agentscope.svg)

## When to use

You're a backend or platform engineer tasked with shipping an LLM agent as a real service — not a notebook demo. You need more than a single ReAct loop: tools must run inside an isolated sandbox (a user's `bash` call shouldn't touch the host), every model call and tool invocation has to be traceable when something goes wrong in production, and a human reviewer must be able to approve or block a sensitive action mid-run. You also need the service to hold up under multiple tenants and concurrent sessions without their state bleeding into each other. AgentScope 2.0 is built for exactly this lane: it ships a FastAPI-based agent service, a permission system that gates tools and resources, workspace backends for local/Docker/E2B sandboxes, and OpenTelemetry tracing wired in as middleware, so the observability and isolation you'd otherwise hand-roll come with the framework.

The other moment AgentScope fits is when you want a composable, event-driven agent rather than a prompt-and-pray script. Its middleware system lets you hook into the reasoning-acting loop (context compression, tool-result compaction, custom guards), and a unified event bus streams `REPLY_START` / `MODEL_CALL_START` / `TEXT_BLOCK`-style events out to a frontend — there's a pre-built web UI under `examples/web_ui` for agent teams, task planning, and permission controls. If your end goal is an inspectable, human-in-the-loop agent app with a UI and multiple model backends (DashScope, OpenAI, Anthropic, Gemini, Ollama, xAI), this is squarely in scope.

## When NOT to use

- **You want a single-file, zero-infra agent.** AgentScope's value is the service/permission/observability/sandbox machinery. For a quick tool-using loop in a script, a thinner library (raw OpenAI SDK + a few tools, or a minimal ReAct helper) has far less surface to learn and deploy.
- **You're optimizing prompt *programs*, not orchestration.** If your problem is "compile and tune the prompts/pipeline" rather than "run and serve agents," a program-synthesis approach like [DSPy](../../workflow-builders/dspy.md) is a different tool entirely — AgentScope does not do prompt optimization.
- **You need a battle-tested, large-ecosystem framework with years of third-party integrations.** AgentScope 2.0 is a recent major rewrite [推断]; its 2.x API surface is newer and smaller than long-standing alternatives, so community recipes, Stack Overflow coverage, and third-party plugins are thinner.
- **API churn is a dealbreaker.** v2.0 was a substantial refactor of the `Msg` class, tool module, and middleware vs v1.x — code written against 1.x does not carry over cleanly, and a fast-moving 2.x line may keep moving. Pin versions.
- **You're a non-Python shop.** It is Python-only (>=3.11). No first-class TypeScript/Go/Java SDK.
- **You just need a hosted agent product.** This is a framework you run and operate, not a managed SaaS — you own deployment, scaling, and the model API keys.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [DSPy](../../workflow-builders/dspy.md) | ✅ | Choose DSPy when you need declarative prompt/pipeline *optimization* rather than multi-agent serving. | Declarative prompt/pipeline *optimization* (compile + tune programs); not a multi-agent serving runtime. Reach for it to tune quality, not to orchestrate/serve agents. |
| [openfang](../agent-services/openfang.md) | ✅ | Choose openfang when you want another indexed agent framework with a more OS-shaped runtime. | Sibling agent framework in this index; different design point — compare scope/maturity before choosing. [未验证] |
| [Symphony](../agent-services/symphony.md) | ✅ | Choose Symphony when you need an indexed multi-agent framework focused on scheduling autonomous coding runs. | Sibling multi-agent framework in this index; overlapping "orchestrate multiple agents" goal, different ergonomics. [未验证] |
| [claude-octopus](../../coding-agents/orchestration-and-review/claude-octopus.md) | ✅ | Choose claude-octopus when you need a Claude-style multi-agent workflow sibling. | Sibling in this index, oriented around Claude-style multi-agent workflows; narrower model focus than AgentScope's multi-provider serving. |
| [LangGraph](langgraph.md) | ✅ | Choose LangGraph when you need graph/state-machine orchestration with a large ecosystem and explicit control flow. | Graph/state-machine orchestration with a large ecosystem and explicit control flow; heavier, more opinionated than AgentScope's "trust the model" loop. |
| [AutoGen](autogen.md) | ✅ | Choose AutoGen when you need a mature conversation-driven multi-agent framework. | Mature conversation-driven multi-agent framework; comparable multi-agent scope, different abstractions and a larger community footprint. |
| [CrewAI](crewai.md) | ✅ | Choose CrewAI when role/crew-based agent orchestration and strong DX matter more than AgentScope's serving stack. | Role/crew-based agent orchestration with strong DX; less emphasis on the service/permission/sandbox/observability stack AgentScope ships. |

## Tech stack

- **Language:** Python (>=3.11).
- **Core runtime:** `asyncio`-based; model SDKs for `openai`, `anthropic`, `dashscope` (and optional `google-genai`, `ollama`, `xai-sdk`).
- **Protocols/tools:** Model Context Protocol via `mcp` (unified `MCPClient`); `tree_sitter` / `tree_sitter_bash` for tool/code handling; `jsonschema`, `docstring_parser`, `json_repair`, `json5` for tool schemas and robust parsing.
- **Service layer:** FastAPI + Uvicorn agent service (optional `service` extra), `apscheduler`, `ag-ui-protocol`; Socket.IO (`python-socketio`) event bus to the frontend.
- **Observability:** OpenTelemetry (`opentelemetry-api/sdk/exporter-otlp`, semantic conventions) wired in as tracing middleware.
- **Workspace/sandbox:** local, Docker (`aiodocker`), and E2B (`e2b`) backends (optional `workspace` extra).
- **Storage/memory:** Redis sessions (optional `storage` extra); `mem0ai` integration (optional `mem0` extra).

## Dependencies

- **Runtime:** Python >= 3.11. `pip install agentscope` (or `uv pip install agentscope`).
- **Always-installed deps:** `openai`, `anthropic`, `dashscope`, `mcp`, `httpx`, `numpy`, `aioitertools`, `aiofiles`, `jinja2`, `jsonschema`, `docstring_parser`, `json_repair`, `json5`, `filetype`, `python-datauri`, `python-socketio`, `python-frontmatter`, `shortuuid`, `tree_sitter`, `tree_sitter_bash`, and the OpenTelemetry stack (`opentelemetry-api/sdk/exporter-otlp>=1.39.0`).
- **Optional extras:** `service` (FastAPI/Uvicorn/apscheduler/ag-ui-protocol), `storage` (redis), `workspace` (aiodocker/e2b), `gemini` (google-genai), `ollama`, `xai`, `tools` (ripgrep), `mem0` (mem0ai>=2.0.0).
- **External infra (only if you opt in):** Docker daemon or an E2B account for sandboxed workspaces; a Redis instance for persistent sessions; an OTLP collector to receive traces; and at least one model provider API key.

## Ops difficulty

**Medium.** A bare in-process agent is easy — install, set a model key, run. Difficulty climbs as you turn on the parts that justify picking AgentScope: standing up the FastAPI service with multi-tenant/multi-session isolation, running the Docker/E2B sandbox backends (you now operate a container runtime), wiring an OTLP collector to actually consume the traces, and adding Redis for durable sessions. None of these are exotic, but each is a real moving piece to deploy and monitor, and a fast-evolving 2.x line means you should pin versions and budget for upgrade churn.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 11.6 hours across 19 qualifying issues/PRs.
- **Maintenance (2026-06):** actively maintained — default branch pushed 2026-06-25, latest release v2.0.2 (2026-06-16), not archived. A healthy open-issue count (~262) against steady releases reads as a live, engaged project rather than a stalled one.
- **Governance & backing:** Organization-owned (`agentscope-ai`), with DashScope (Alibaba's model platform) as the default/first-class backend — i.e. a real org with vendor adjacency behind it rather than a lone maintainer, a better bus-factor position than single-user repos. It is not under a neutral foundation (Apache/LF/CNCF), so treat governance as vendor-adjacent stewardship (see Caveats for what is unconfirmed).
- **Age & Lindy (2026-06):** created 2024-01, ~2.5 years old — the **oldest and most established** project in this chunk, and still actively shipping. Lindy verdict: **age × still-active is favorable** (a multi-year, maintained framework). The caveat is the recent **v2.0 rewrite**: the *project* is Lindy-strong, but the *2.x API surface* is young, so community recipes and third-party integrations are still thinner than the project's age suggests.
- **Risk flags:** Apache-2.0 (permissive, no relicense/CLA concerns observed). Main risk is **2.x API churn** — v2.0 broke `Msg`/tool/middleware vs v1.x and the line keeps moving, so pin versions and budget upgrade work. No CVEs were reviewed.

## Caveats (unverified)

- [未验证] Star count ~27.2k as of 2026-06 (from `gh repo view`). GitHub stars in this ecosystem are unreliable and date-sensitive — treat as indicative only.
- [未验证] Latest release v2.0.2 published 2026-06-16; default branch last pushed 2026-06-25 (per GitHub API). Exact version/dates can shift; re-verify against the repo.
- [推断] v2.0 being a "substantial rewrite" with breaking `Msg`/tool/middleware changes vs v1.x is inferred from the v2.0.0 release notes' refactor language; the precise breaking-change list should be read from the official changelog before migrating.
- [未验证] Relative comparisons to siblings (openfang, Symphony, claude-octopus) are positioning sketches, not benchmarked head-to-heads; verify each sibling's current scope before deciding.
- [未验证] "Production-ready" / "production-grade serving" is the project's own framing from the README, not an independently validated claim.
- [推断] The exact set of supported model providers and optional extras shifts release-to-release; the list here reflects the current `pyproject.toml` and should be re-checked for a specific provider.
