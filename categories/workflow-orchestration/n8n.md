---
name: n8n
slug: n8n
repo: https://github.com/n8n-io/n8n
category: workflow-orchestration
tags: [workflow-automation, low-code, integrations, ai-native, self-hosted]
language: TypeScript
license: NOASSERTION (fair-code)
maturity: v1.x, active, 195k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-04T08:19:53Z
  default_branch: master
  default_branch_sha: 3029ca0a38409a3a9bcbcef4a316e1676d0b7d3e
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T16:19:30Z
  overall: A
  overall_score: 3.75
  scored_axes: 4
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
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: n8n-workflow
        dependent_repos_count: 304
        downloads_last_month: 1313694
        graph_tier: C
        volume_tier: B
        cross_check_divergence: 1.04
    longevity:
      grade: A
      raw:
        repo_age_days: 2568
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 177
        top1_share: 0.062
        top3_share: 0.149
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    risk_license: { reason: license_unparsed }
---

# n8n

A fair-code workflow automation platform with native AI capabilities — combine visual building with custom JavaScript/Python code, self-host or use the cloud, with 400+ integrations and 900+ ready-to-use templates.

![n8n — health radar](../../assets/health/n8n.svg)

## When to use

You're a technical team that needs to automate internal processes — pulling data from APIs, transforming it, and pushing it to other systems — but you don't want to write and maintain thousands of lines of boilerplate integration code. You need a visual builder so non-engineers can contribute workflows, but you also want the ability to drop into JavaScript or Python when the visual nodes hit their limits. You want to self-host for data sovereignty, or you need an AI-native platform that can build agent workflows with LangChain. Choose n8n over Zapier because n8n is self-hostable and code-extensible; choose it over Apache Airflow because n8n is visual-first and comes with 400+ pre-built integrations rather than requiring you to write Python DAGs from scratch. The deciding tradeoff is speed of no-code prototyping plus the escape hatch of real code.

## When NOT to use

- If you need sub-second real-time event processing, use Kafka or Flink instead of n8n, because n8n is a batch workflow engine, not a low-latency stream processor.
- If you need a pure code-only CI/CD pipeline, use Argo Workflows or GitHub Actions instead of n8n, because n8n's visual builder is its selling point and adds overhead for infrastructure-as-code pipelines.
- If you need a fully OSI-approved open-source license without restrictions, use Apache Airflow or Prefect instead of n8n, because n8n uses a "fair-code" Sustainable Use License that restricts reselling and competing use.
- If your workflows are extremely simple (one or two HTTP calls), use Zapier or a simple cron job instead of n8n, because the overhead of running n8n (database, web server, workers) is overkill for trivial scripts.
- If you need enterprise-grade multi-tenant SaaS out of the box, use Zapier or Make instead of n8n, because the self-hosted version requires significant setup and the cloud offering is managed by n8n GmbH.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Apache Airflow](airflow.md) | ✅ | Pick Airflow when workflows are code-first Python data pipelines rather than visual business automation. | Airflow is code-first and batch-data-pipeline focused; n8n is visual-first and integration-focused with 400+ pre-built nodes. |
| [Prefect](prefect.md) | ✅ | Pick Prefect when Python developer experience matters more than a visual builder and packaged SaaS integrations. | Prefect is code-first; n8n adds a visual builder and 400+ pre-built integrations. |
| Zapier | 未收录 | Pick Zapier when zero self-hosting and managed SaaS convenience matter more than code escape hatches. | Zapier requires no setup but is proprietary, cloud-only, and charges per task; n8n is self-hostable and code-extensible. |
| [Argo Workflows](argo-workflows.md) | ✅ | Pick Argo when the workflow unit is a Kubernetes container, CI/CD job, or ML pipeline. | Argo is for containerized CI/CD and ML pipelines on K8s; n8n is for API integrations and business automation. |
| Make (Integromat) | 未收录 | Pick Make when you want a proprietary cloud visual automation product and do not need self-hosting. | Make is cloud-only and proprietary; n8n offers self-hosting and code extensibility. |

## Tech stack

- **TypeScript** — primary implementation language
- **Node.js** — runtime
- **Vue.js** — frontend editor UI
- **PostgreSQL / SQLite** — metadata database (configurable)
- **Redis** — job queue and caching (optional but recommended)

## Dependencies

- **Database** — PostgreSQL (recommended) or SQLite (lightweight)
- **Node.js** — runtime for the server
- **Redis** — for queueing and caching in production setups
- **Docker** — recommended for deployment
- **Reverse proxy** — nginx or traefik for TLS termination if exposed to the internet

## Ops difficulty

**Medium**. n8n can be started with a single `npx` command or Docker one-liner for local use, but production self-hosting requires a database, Redis, backups, and monitoring. The fair-code license also means you must understand the usage restrictions before commercial deployment.

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 0 days ago.
- **Responsiveness**: Cannot be scored — no qualifying recent issue/PR traffic was found by the scorer (`no_traffic`).
- **Adoption**: Grade B — 1,313,694 monthly downloads via npmjs.org (package: n8n-workflow).
- **Longevity**: Grade A — 2568 days old.
- **Governance**: Grade A — top-3 contributor share 14.9%.
- **Risk / License**: Cannot be scored — the fair-code license was not parsed into a comparable SPDX-style tier (`license_unparsed`).

## Caveats (unverified)

- [未验证] The exact fair-code license terms may have evolved; verify the current Sustainable Use License text before commercial deployment.
- [未验证] The "400+ integrations" number includes community and official nodes; quality and maintenance level vary.
- [推断] The n8n GmbH cloud offering's pricing and feature gates may change over time as the company pursues revenue growth.
