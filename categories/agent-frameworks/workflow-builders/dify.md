---
name: Dify
slug: dify
repo: https://github.com/langgenius/dify
category: workflow-builders
tags: [agentic-workflow, low-code, rag, mcp, orchestration, nextjs]
language: TypeScript
license: NOASSERTION
maturity: v0.x, active, 147k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-04T10:43:04Z
  default_branch: main
  default_branch_sha: 2e1ab194b718dea0ec364d3f1ae94fa0dd45e9e3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T08:47:26Z
  overall: B
  overall_score: 3.2
  scored_axes: 5
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
        median_ttfr_hours: 0.0
        qualifying_issues: 15
        band: default
        window_offset_days: 2
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: dify-client
        dependent_repos_count: 8
        downloads_last_month: 8835
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: B
      raw:
        repo_age_days: 1178
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 256
        top1_share: 0.111
        top3_share: 0.226
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Dify

A production-ready platform for building and deploying agentic workflows with low-code visual orchestration, built-in RAG, MCP support, and multi-LLM provider connectivity.

![Dify — health radar](../../../assets/health/dify.svg)

## When to use

You're a product team that needs to ship AI-powered workflows fast without writing everything from scratch. You want a visual builder where non-engineers can design agent flows, but developers can still drop into code when needed. You need built-in RAG for document Q&A, multi-step workflow orchestration, and the ability to connect various LLM providers (OpenAI, Anthropic, Gemini, local models) through a single platform. You deploy Dify self-hosted and iterate on chatbots, AI agents, and automated pipelines in one place. Choose Dify over Langflow because Dify has more mature deployment features, built-in RBAC, and a stronger enterprise orientation; choose it over n8n because Dify is purpose-built for LLM and agent workflows rather than general business automation. The deciding tradeoff is production-ready AI platform features combined with low-code accessibility.

## When NOT to use

- If you need a lightweight or single-purpose script, use LangChain or a direct API call instead of Dify, because Dify is a full platform and using it for a simple one-off task is overkill.
- If your team is pure code-first and dislikes visual builders, use LangChain or CrewAI instead of Dify, because the low-code layer will feel like friction for developers who prefer hand-rolling every agent loop in Python.
- If you need strict open-source license clarity for commercial redistribution, use Langflow or a fully MIT-licensed project instead of Dify, because GitHub metadata lists `NOASSERTION` for the Dify license and the actual terms must be verified before commercial use.
- If you have a small-resource deployment, use a lighter Python script or LangChain instead of Dify, because self-hosting Dify requires Docker, PostgreSQL, Redis, and a vector store, and a tiny VPS will struggle.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [LangChain](langchain.md) | ✅ | Pick LangChain when a code-first agent/RAG library is preferable to a visual deployment platform. | LangChain is code-first and framework-shaped; Dify is a visual platform with built-in RAG and deployment. |
| [n8n](../../workflow-orchestration/n8n.md) | ✅ | Pick n8n when the workflow is broader business automation with some AI nodes. | n8n is broader business-process automation; Dify is purpose-built for LLM and agent workflows. |
| [LangFlow](langflow.md) | ✅ | Pick LangFlow when a Python-first MIT visual builder is preferred over Dify's fuller platform/RBAC stack. | Similar visual approach; LangFlow is Python-first and MIT-licensed, while Dify has more mature deployment and RBAC features. |
| [AutoGPT](autogpt.md) | ✅ | Pick AutoGPT when the goal is fully autonomous long-running agents rather than designed workflows. | AutoGPT targets fully autonomous long-running agents; Dify focuses on orchestrated, human-designed workflows. |
| [CrewAI](../agent-runtimes/agent-sdks/crewai.md) / LlamaIndex | partly indexed | Pick specialized frameworks when you want multi-agent teams or RAG-first plumbing without Dify's bundled platform. | CrewAI is multi-agent team-oriented; LlamaIndex is RAG-first. Dify bundles both concerns into one platform. |

## Tech stack

- **TypeScript / Next.js** — frontend and API layer
- **Python** — backend workflow engine and AI logic
- **PostgreSQL** — primary metadata and config store
- **Redis** — caching and message broker
- **Docker** — containerized deployment

## Dependencies

- Docker and Docker Compose (recommended deployment path)
- PostgreSQL database
- Redis instance
- Vector database (Weaviate, Qdrant, or Milvus) for RAG
- LLM provider API keys or local model endpoints

## Ops difficulty

**Medium**. Docker Compose is the standard path, but running Dify in production requires managing a database, Redis, a vector store, and LLM credentials. Upgrades, backup of PostgreSQL, and scaling the worker tier add operational surface. The cloud offering offloads this but shifts to SaaS dependency.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 0 days ago.
- **Responsiveness**: Grade A — median first-response time 0.0 hours across 15 qualifying issues/PRs.
- **Adoption**: Grade D — 8,835 monthly downloads via npmjs.org (package: dify-client).
- **Longevity**: Grade B — 1178 days old.
- **Governance**: Grade A — top-3 contributor share 22.6% (?).
- **Risk / License**: Cannot be scored — custom_modified_license. Upstream `LICENSE` is a modified Apache License 2.0 with extra commercial-license conditions for multi-tenant service use and frontend logo/copyright removal; treat GitHub `NOASSERTION` as a real license-review signal, not a parser glitch.
## Caveats (unverified)

- [未验证] The GitHub API reports `NOASSERTION` as the license; direct `LICENSE` lookup on 2026-07-04 shows a modified Apache License 2.0 with additional terms around multi-tenant service use, frontend logo/copyright removal, contributor grants, and appearance-patent notice. Legal review is required before commercial redistribution or hosted multi-tenant use.
- [未验证] The exact resource requirements for production self-hosting (CPU, RAM, disk) are not confirmed from official docs.
- [推断] The 147k star count on a ~3-year-old repo may include significant hype-driven growth; organic enterprise adoption should be verified independently.
