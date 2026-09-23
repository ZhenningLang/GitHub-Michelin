---
name: MiroThinker
slug: mirothinker
repo: https://github.com/MiroMindAI/MiroThinker
category: deep-research
tags: [deep-research, agent, llm, mcp-tools, browsecomp, self-hosted, qwen]
language: Python
license: Apache-2.0
maturity: v1.7 models, active, ~8.3k stars (as of 2026-06)
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-04-25T05:23:54Z
  default_branch: main
  default_branch_sha: 370f98361553ddf787bedc5745760e04114cb161
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:08:01Z
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
        last_commit_age_days: 184
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: C
      raw:
        repo_age_days: 411
        last_commit_age_days: 184
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 10
        top1_share: 0.595
        top3_share: 0.798
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

# MiroThinker

An open-source deep-research agent: fine-tuned LLMs plus an MCP-tool environment (web search, scraping, code execution) orchestrated by the MiroFlow framework to answer complex, multi-step research and prediction questions.

![mirothinker — health radar](../../assets/health/mirothinker.svg)

## When to use

You're an ML engineer at a research-tooling team and you want a self-hosted, open-weights answer to "deep research" agents — something that browses the web, reads pages, runs code, and synthesizes a multi-step answer, but that you can run on your own GPUs instead of paying a closed API per query. You clone MiroThinker, host one of its fine-tuned models (Qwen-based, 30B–235B scale for v1.7) on SGLang or vLLM, set API keys for the tool layer (Serper for search, Jina for scraping, E2B for the code sandbox), pick a prebuilt agent config, and run a research task end-to-end. Because the agent's tools are wired as MCP servers and the orchestration (context retention, up to hundreds of tool calls per task) lives in the MiroFlow framework, you can study, modify, or extend the agent loop rather than treat it as a black box. It's aimed at people who want to *reproduce and build on* a competitive open deep-research agent — including its reported BrowseComp/GAIA benchmark results — not just call a product.

## When NOT to use

- **You just want a working research assistant, not infrastructure.** This is a framework + model weights you self-host, with multiple commercial API dependencies wired in. If you want a turnkey product, a hosted deep-research offering is far less work.
- **You can't provision serious GPU.** The 30B–235B models need GPU clusters (multiple GPUs typical) plus a serving stack (SGLang/vLLM). Without that hardware, this isn't runnable at full capability. [推断]
- **You need a fully self-contained / offline / no-egress agent.** Full functionality depends on external commercial APIs (Serper, Jina, E2B, and OpenAI for some preprocessing/benchmarking) — data leaves your environment and costs accrue per run.
- **You need production stability and SLAs.** It's a young (2025) research project tracking benchmarks; expect churn, rough edges, and reproducibility caveats, not a hardened product. [推断]
- **Robust multimodal or non-English is critical.** The README notes text-only LLM behavior with GPT-4o preprocessing for some multimodal tasks, and early versions had limited Chinese — verify the current version's coverage for your language/modality. [未验证]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| OpenAI / Gemini "Deep Research" | 未收录 | Choose hosted Deep Research products when turnkey quality and no GPU matter most. | Hosted, turnkey, strong quality, no GPU to run; but closed, paid per use, no self-hosting or model control — the opposite tradeoff to MiroThinker. |
| [GPT-Researcher](gpt-researcher.md) | ✅ | Choose GPT-Researcher when you need a lightweight open agent over LLM APIs and web tools. | Lightweight open research agent that orchestrates a frozen LLM API + web tools; far cheaper to run (no self-hosted weights) but not its own fine-tuned models or benchmark-tuned framework. |
| [smolagents](../agent-frameworks/agent-runtimes/agent-sdks/smolagents.md) / LangGraph + tools | 部分已收录 | Choose smolagents or LangGraph when you want to assemble the research loop yourself. | General agent frameworks you'd assemble a research loop on; more flexible and model-agnostic, but you build the research pipeline and provide tuning yourself. |
| [Open Deep Research (HF)](open-deep-research.md) | ✅ | Choose Open Deep Research when you need an API-model reproduction of a deep-research agent. | Open reproduction of a deep-research agent over an API model; similar open spirit, different stack and (usually) no self-hosted fine-tuned weights. |

## Tech stack

- **Language:** Python (3.10+).
- **Orchestration:** the **MiroFlow** agent framework — manages the agent–environment loop, large context windows, and a context-retention strategy (keep last K tool responses). Config via Hydra.
- **Models:** Qwen-based, fine-tuned via SFT + DPO; multiple scales (v1.7: ~30B–235B). Served with **SGLang** or **vLLM**.
- **Tools:** MCP servers for web search, content extraction, code execution, document processing.
- **ML deps:** `transformers` and the usual Python ML ecosystem.

## Dependencies

- **Models:** self-hosted Qwen-based weights (or a compatible LLM backend) — sizeable downloads.
- **Hardware:** GPU cluster (multiple GPUs typical for 30B+); a serving runtime (SGLang/vLLM).
- **External APIs (required for full function):** Serper (search), Jina (scraping), E2B (code sandbox), plus a summary LLM service and OpenAI for some preprocessing/benchmarking — configured via `.env`. API credits accrue per run.
- **Network:** outbound egress to those services; not an offline agent.

## Ops difficulty

**High.** This is the most demanding kind of deployment here: you stand up a GPU serving stack (SGLang/vLLM) for a large model, manage the model download/placement, wire several third-party API keys, and tune agent config (context retention, tool-call budgets). Running it well means owning GPU capacity, monitoring cost across the external APIs, and accepting reproducibility caveats of a fast-moving research codebase. Evaluation/benchmark reproduction adds its own harness setup. This is infrastructure to operate, not a library to import.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 145.8 hours across 4 qualifying issues/PRs.
- **Maintenance (2026-06).** Last pushed 2026-04 (latest commit ~2026-04); the v1.x model line shows ongoing iteration. **Active** and **not archived**, but the cadence and a young codebase mean churn. [推断]
- **Governance / backing.** Org-backed (**MiroMindAI**, miromind.ai), multi-contributor — better bus factor than a solo repo, but it's a single company's research project; longevity tracks that company's continued investment. [推断]
- **Age & Lindy verdict.** Created 2025-08, **<1 year old** — **no Lindy yet**. High stars (~8.3k) on a very young repo is a hype/momentum signal, not durability proof; treat sustainability as unproven. [推断]
- **Adoption.** Strong early traction (~8.3k stars, ~645 forks) driven by competitive open benchmark claims (BrowseComp/GAIA); real production adoption beyond research/eval is unverified. [未验证]
- **Risk flags.** Apache-2.0 code (clean), but heavy external-API and GPU dependence, young age, single-company stewardship, and benchmark-driven framing (numbers vary by version and harness) are the bets you're making. [推断]

## Caveats (unverified)

- [未验证] ~8.3k stars / ~645 forks as of 2026-06; v1.7 model line. Counts and version labels are date-sensitive.
- [未验证] Reported benchmark numbers (BrowseComp ~74–88, BrowseComp-ZH ~75, GAIA ~83, HLE-Text ~43) are the project's own claims and vary across the README's own statements and versions — not independently reproduced here; verify against the current model card.
- [推断] GPU-cluster / multi-GPU requirement and the 30B–235B scale are inferred from the README's model sizes and serving stack, not measured.
- [未验证] Python version, Hydra config, transformers usage, and the exact tool/API list are read from README at one point in time and may change release-to-release.
- [推断] "No Lindy yet / sustainability unproven" follows directly from the 2025 creation date plus single-company backing.
