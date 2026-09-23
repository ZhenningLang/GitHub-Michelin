---
name: Pezzo
slug: pezzo
repo: https://github.com/pezzolabs/pezzo
category: llm-eval
tags: [llmops, prompt-management, observability, prompt-versioning, self-hosted, typescript]
language: TypeScript
license: Apache-2.0
maturity: v0.9.2, likely stalled (last real commit ~2025-06), ~3.2k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2026-03-31T02:03:01Z
  default_branch: main
  default_branch_sha: 886d38b50bd7d8af723eb12e7d815e1e2b625c87
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:27:13Z
  overall: C
  overall_score: 2.4
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
        last_commit_age_days: 32
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: "@pezzo/client"
        dependent_repos_count: 1
        downloads_last_month: 1879
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 1249
        last_commit_age_days: 32
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
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

# Pezzo

An open-source, self-hostable LLMOps platform for prompt management, versioning, observability and cost/latency monitoring — a central place to author prompts and watch how they behave in production.

![pezzo — health radar](../../assets/health/pezzo.svg)

## When to use

You're a developer on a small product team that's started shipping LLM features, and your prompts are scattered across the codebase as inline strings — nobody knows which version is live, you can't see what a call cost or how long it took, and changing a prompt means a redeploy. You self-host Pezzo (Docker Compose: Postgres + ClickHouse + Redis), move your prompts into its UI where they're versioned and editable without a code change, and instrument your app with the Node or Python SDK. Now each LLM request is traced — prompt version, tokens, cost, latency, errors — in one observability dashboard, you can roll a prompt forward or back from the UI, and caching can cut repeat-call spend. It's aimed at teams who want a single self-hosted control plane for prompts + monitoring rather than gluing together a prompt registry, a tracing tool, and a cost dashboard separately.

## When NOT to use

- **The project looks stalled — don't bet a new stack on it.** Its last substantive commit appears to be ~mid-2025; for a young VC-backed startup repo that's a serious abandonment risk. Verify current activity before adopting, and assume you may end up maintaining it yourself. [推断]
- **You want a managed service.** Pezzo offered a hosted "Pezzo Cloud," but self-hosting is the safe assumption for an OSS project whose company trajectory is uncertain — don't depend on the cloud tier persisting. [推断]
- **You need a heavyweight eval / experimentation platform.** Pezzo centers on prompt management + observability; rigorous offline evals, dataset-driven scoring, and A/B experimentation are stronger in tools built for that (LangSmith, Langfuse, Helicone).
- **You don't want to run three datastores.** Self-hosting requires Postgres, ClickHouse, and Redis — non-trivial infra for a small team versus a hosted alternative.
- **You need broad, current SDK/provider coverage.** SDKs were Node/Python with some integrations in progress; on a stalled project, expect gaps and unmaintained provider support.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Langfuse](langfuse.md) | ✅ | Choose Langfuse for new open-source LLM observability, prompt management, and eval deployments; keep Pezzo only for an existing self-hosted Pezzo stack you are prepared to maintain yourself. | Open-source LLM observability + prompt management + evals, actively maintained with a strong community; broadly the healthier successor to Pezzo's niche today. |
| Helicone | 未收录 | Choose Helicone when logging, cost tracking, caching, and proxy-based adoption are the main needs; keep Pezzo only if its prompt-versioning UI already fits and the stall risk is acceptable. | Open-source LLM observability/proxy focused on logging, cost, and caching; lighter to adopt (proxy-based), narrower prompt-management story. |
| LangSmith (LangChain) | 未收录 | Choose LangSmith when managed tracing, evals, prompt hub, and LangChain integration matter more than self-hosted OSS; keep Pezzo only when SaaS is off the table and self-maintenance is acceptable. | Hosted tracing + evals + prompt hub, deep LangChain integration; managed and feature-rich, but proprietary/SaaS, not self-hostable OSS. |
| PromptLayer | 未收录 | Choose PromptLayer for hosted prompt registry and request logging; keep Pezzo only when you specifically need self-hosted prompt management and accept a likely stalled codebase. | Prompt registry + request logging; overlapping prompt-management scope, hosted-first. |

## Tech stack

- **Language:** TypeScript (primary), with a Python SDK as well.
- **Backend:** Node.js (NestJS-style services); a GraphQL API (GraphQL codegen tooling referenced).
- **Frontend:** React web console.
- **Datastores:** PostgreSQL (core data), ClickHouse (high-volume request/telemetry data), Redis (cache/queue).
- **Deployment:** Docker Compose for local/self-host; SDKs for Node and Python.

## Dependencies

- **Datastores (you run):** PostgreSQL + ClickHouse + Redis — three services, typically via the provided Docker Compose.
- **Runtime:** Node.js 18+ for the platform; a container runtime (Docker) for the self-host path.
- **LLM providers:** your own provider/API keys; Pezzo wraps/observes the calls (specific provider coverage unverified, and unmaintained on a stalled project).
- **SDK:** the Node or Python SDK embedded in your application to capture traces and fetch prompt versions.

## Ops difficulty

**Medium-to-high.** The day-one deploy via Docker Compose is approachable, but you're operating a stateful multi-service app: Postgres + ClickHouse + Redis to back up, upgrade, and monitor, plus the API/console. ClickHouse in particular is real infrastructure to run well at volume. The larger operational risk is the project's apparent stall (see Health): on an unmaintained codebase you inherit security patching, dependency upgrades, and bug fixes yourself, which turns "medium" deployment effort into an open-ended maintenance commitment.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** **Likely stalled.** GitHub's `pushed_at` reads 2026-03, but the last *substantive commit* on the default branch appears to be ~2025-06 — roughly a year of inactivity. Latest release v0.9.2 (pre-1.0). Not archived, but the cadence looks dead, not coasting. [推断]
- **Governance / backing.** A VC-style startup project (pezzolabs / pezzo.ai) with a small core team. Single-company stewardship plus apparent inactivity is a high bus-factor risk — if the company pivoted or wound down, the OSS repo and any cloud tier are at risk. [推断]
- **Age & Lindy verdict.** Created 2023-04, ~3 years old but **apparently no longer active** — this **fails Lindy**: age only counts when still-active, and a stalled project trends toward abandonment, not durability. [推断]
- **Adoption.** ~3.2k stars / ~276 forks captured real early interest, but a stalled repo means the community and ecosystem are likely drifting to actively maintained alternatives (Langfuse, Helicone). [未验证]
- **Risk flags.** Apache-2.0 (clean license, no relicense found). The dominant flags are **inactivity/abandonment risk** and **single-startup dependency** — both argue for a maintained alternative unless you're prepared to fork and own it. [推断]

## Caveats (unverified)

- [未验证] ~3.2k stars / ~276 forks and v0.9.2 as of 2026-06; counts are date-sensitive.
- [推断] "Likely stalled / ~1 year inactive" is inferred from a mismatch between GitHub's `pushed_at` (2026-03) and the last substantive default-branch commit (~2025-06-28) — `pushed_at` can be bumped by branch/tag activity without real changes. Confirm current commit history before relying on the project.
- [推断] NestJS backend, React frontend, and GraphQL API are inferred from README/tooling references, not confirmed by reading the source layout here.
- [未验证] Supported LLM providers and the exact SDK/integration coverage are not detailed in the material reviewed — verify against the repo if it matters.
- [推断] The Pezzo Cloud hosted tier's current status is uncertain given the company's apparent inactivity; treat the cloud option as not guaranteed to persist.
