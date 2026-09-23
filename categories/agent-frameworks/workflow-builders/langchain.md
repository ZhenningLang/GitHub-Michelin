---
name: LangChain
slug: langchain
repo: https://github.com/langchain-ai/langchain
category: workflow-builders
tags: [llm, agents, rag, framework, python, typescript]
language: Python
license: MIT
maturity: v0.x, active, 141k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-06T05:58:34Z
  default_branch: master
  default_branch_sha: 701cc0e6bbb9112b67bee9c9cfd88405061acc37
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:37:32Z
  overall: A
  overall_score: 3.6
  scored_axes: 5
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
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: langchain
        dependent_repos_count: 18663
        downloads_last_month: 175109180
        graph_tier: A
        volume_tier: A
        cross_check_divergence: null
        release_downloads: 1865
        release_assets: 186
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1437
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 42
        top1_share: 0.488
        top3_share: 0.746
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
    responsiveness: { reason: no_window_signal }
---

# LangChain

The agent engineering platform — a framework for building agents and LLM-powered applications by chaining interoperable components and third-party integrations. Install it with `uv add langchain`.

![LangChain — health radar](../../../assets/health/langchain.svg)

## When to use

You are a Python developer building an AI application that needs to connect LLMs to external tools, databases, and APIs. You have looked at Dify, but Dify is a low-code platform with a visual builder — you want code-level control over every prompt, chain, and tool invocation. You have looked at AutoGPT, but AutoGPT is a higher-level platform with a web UI and deployment model; you need to build a custom application, not run a pre-built agent. You choose LangChain over both because it is a code-first framework that gives you full compositional control: you assemble prompt templates, manage conversation memory, and route between models and tools in Python, with a massive ecosystem of pre-built integrations so you do not write every adapter yourself. You are building agents that need to reason, use tools, and maintain state across multiple steps — and you want to own the architecture.

## When NOT to use

- **Simple single-prompt apps** — If you just need to call an LLM API once, LangChain adds abstraction overhead with no benefit. Use the OpenAI SDK or Anthropic SDK directly instead of LangChain, because a direct SDK call is faster and has no framework dependency.
- **Low-code or no-code platform needs** — If you want a visual drag-and-drop interface for building agents without writing code, use Dify or LangFlow instead of LangChain, because those platforms provide visual builders and built-in deployment.
- **Production latency-critical paths** — The framework's abstraction layers can introduce overhead. For millisecond-critical inference paths, use direct API calls or LiteLLM instead of LangChain, because those options remove the framework indirection.
- **Vendor lock-in aversion at the framework level** — Deep integration with LangChain's ecosystem can create migration friction if you later want to move away from it. If you want maximum vendor independence, use LiteLLM or direct SDKs with your own orchestration instead of LangChain, because those approaches keep you closer to the underlying APIs.
- **You need a ready-to-run agent out of the box** — LangChain is a library for building agents, not a pre-configured agent. If you want something that runs immediately without writing orchestration code, use AutoGPT or Hermes Agent instead of LangChain, because those are higher-level platforms that include a runtime and UI.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Dify](dify.md) | ✅ | Visual platform for agentic workflows. | Dify is a low-code platform with built-in RAG and deployment; LangChain is a code-first library for building custom agents with full control. |
| [DSPy](dspy.md) | ✅ | Prompt optimization via metrics. | DSPy optimizes prompts/weights against a metric; LangChain is a general composition framework for agents, chains, and tools. |
| [AutoGPT](autogpt.md) | ✅ | Platform for autonomous workflow automation. | AutoGPT is a higher-level platform with a web UI and deployment model; LangChain is a lower-level framework you build on. |
| [smolagents](../agent-runtimes/agent-sdks/smolagents.md) | ✅ | Tiny transparent agent loop from Hugging Face. | smolagents is minimal and transparent; LangChain is comprehensive and integration-rich. |
| [LlamaIndex](llamaindex.md) | ✅ | RAG-first data framework for LLMs. | LlamaIndex specializes in retrieval and data ingestion; LangChain is broader, covering agents, chains, tools, and orchestration. |

## Tech stack

- **Python** — primary implementation (also has TypeScript/JS packages)
- **Pydantic** — data validation and serialization
- **LangGraph** — companion library for building multi-agent workflows
- **LangServe** — deployment layer for LangChain chains

## Dependencies

- Python 3.9+ environment
- LLM provider API keys (OpenAI, Anthropic, Gemini, etc.) or local model endpoints
- Optional: vector databases (Pinecone, Weaviate, Chroma, FAISS) for RAG
- Optional: various tool integrations (search APIs, databases, etc.)

## Ops difficulty

**Low**. LangChain is a pip-installable library, not a service. The ops burden is in your application code: managing API keys, handling model rate limits, and optimizing chain latency. Deployment is standard Python application deployment. The main complexity is dependency management due to the large integration ecosystem.

## Health & viability

- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 0 days ago.
- **Responsiveness**: Cannot be scored — unknown.
- **Governance**: Grade B — top-3 contributor share 74.6% (?).
- **Longevity**: Grade B — 1437 days old.
- **Adoption**: Grade A — 175,109,180 monthly downloads via pypi.org (package: langchain).
- **Risk flags**: LangChain AI offers commercial products (LangSmith, LangGraph Cloud) that may create open-core or feature-gating pressure. The framework's rapid evolution has historically caused breaking changes between versions.

## Caveats (unverified)

- [未验证] The exact roadmap and open-source vs. commercial feature boundaries for LangSmith and LangGraph Cloud are not confirmed.
- [未验证] The historical frequency of breaking changes between minor versions may have stabilized, but verify for production use.
- [推断] As a venture-backed company, LangChain AI may shift focus toward revenue-generating products; evaluate the community fork or alternative if vendor independence is critical.
