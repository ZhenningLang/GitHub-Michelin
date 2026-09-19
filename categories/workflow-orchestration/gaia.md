---
name: Gaia
slug: gaia
repo: https://github.com/gaia-pipeline/gaia
category: workflow-orchestration
tags: [pipelines, automation, ci-cd, golang-plugins, hashicorp-go-plugin, archived]
language: Go
license: Apache-2.0
maturity: v0.2.9 (2022-01), archived/abandoned (2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2026-01-10T15:10:21Z
  default_branch: master
  default_branch_sha: 98a306bd4c7558f167bf076863dca38406d7eff9
  archived: true
health:
  schema: 1
  computed_at: 2026-07-03T15:04:39Z
  overall: D
  overall_score: 1.0
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 174
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: relaxed_solo
        window_offset_days: 12
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 3109
        last_commit_age_days: 174
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
    adoption: { reason: no_package_structural }
---

# Gaia

An automation/pipeline platform that lets you build pipelines in any programming language (Go, Python, Java, C++, …) by compiling your code into plugins it executes — **now archived and no longer maintained**.

![gaia — health radar](../../assets/health/gaia.svg)

## When to use

Honestly, in 2026 you mostly *shouldn't* — the repo is archived. But the historical fit: you were a platform engineer who wanted CI/CD-style or general automation pipelines, and you were tired of expressing pipeline logic in YAML or a bespoke DSL. Gaia's pitch was that you write pipeline jobs as **real code in your own language**, compile them against its SDK, and Gaia runs them as plugins over HashiCorp's `go-plugin` (gRPC) mechanism, giving you a web UI, scheduling, secrets, and a run history without learning a new workflow language. If you already had a codebase of Go/Python automation and wanted a server to orchestrate and visualize it, Gaia let you keep your logic in code.

Today this is a *read-only reference*: study it if you're researching the "pipelines-as-compiled-plugins" design or evaluating whether to fork it, but it should not be chosen for new production work — see "When NOT to use".

## When NOT to use

- **Any new production deployment.** The repo is **archived** (read-only) with its last release v0.2.9 in 2022-01 — no security patches, no bug fixes, no roadmap. Treat it as abandoned. [推断]
- **You need an actively-governed orchestrator.** For scheduled DAGs and a living ecosystem, [Apache Airflow](airflow.md), Dagster, or Prefect are maintained alternatives with communities behind them.
- **You want a low-friction declarative pipeline.** Gaia required compiling your jobs into plugins against its SDK — heavier than writing YAML in a CI system (GitHub Actions, GitLab CI, Argo Workflows).
- **You can't take on fork/maintenance risk.** Adopting an archived project means *you* own all future patches; only do this with eyes open and a fork plan.
- **You need it to still be pre-1.0-mature.** It never reached a 1.0 release (last tag v0.2.9), so it stopped while still explicitly pre-stable.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Apache Airflow](airflow.md) | ✅ | Choose Airflow for new DAG scheduling work; keep Gaia only as an archived compiled-plugin design reference. | Mature, actively-maintained DAG scheduler with a huge ecosystem; Python-DAG model rather than compiled-plugin jobs, and not archived — the safe default for new work. |
| [Argo Workflows](argo-workflows.md) | ✅ | Choose Argo Workflows when Kubernetes-native, container-per-step YAML workflows fit better than Gaia's plugin-server model. | Kubernetes-native, container-per-step workflows; actively maintained, declarative YAML, no "write jobs in any language as plugins" model. |
| [Dagster](dagster.md) / [Prefect](prefect.md) | ✅ | Choose Dagster or Prefect for maintained Python-first orchestration instead of adopting an archived Gaia fork. | Modern Python-first orchestration with active development and SaaS options; different programming model, maintained — pick over an archived project. |
| Jenkins | 未收录 | Choose Jenkins when the problem is CI/CD with a vast plugin ecosystem rather than general-purpose Gaia-style workflow plugins. | Old but still-maintained CI/CD server with vast plugin ecosystem; Groovy/declarative pipelines instead of compiled-code plugins. |
| GitHub Actions / GitLab CI | 未收录 | Choose hosted CI when VCS-tied YAML pipelines matter more than self-hosting a pipeline server. | Hosted, YAML-driven CI/CD tied to your VCS; far lower setup friction than self-hosting a pipeline server. |

## Tech stack

- **Language:** Go for the server/core; pipeline *jobs* are written in Go, Python, Java, C++, etc. and compiled into plugins.
- **Plugin mechanism:** HashiCorp's `go-plugin` over gRPC — each pipeline runs as an out-of-process plugin the Gaia server invokes.
- **Interfaces:** a web UI (Vue-based frontend) plus a backend API for triggering and viewing runs, scheduling, and secrets.
- **Persistence:** an embedded store for pipeline metadata/run history (no external DB required for the basic install).

## Dependencies

- **Runtime:** the Gaia server binary (Go), plus the toolchain/SDK for whatever language you write pipeline jobs in (e.g. Go to compile Go pipelines).
- **Deploy unit:** a single server process; historically published as a Docker image.
- **No external service strictly required** for a basic install (metadata kept in an embedded store), but a real deployment would still want reverse-proxy/auth in front.

## Ops difficulty

**Medium — and dominated by the abandonment risk, not the day-one setup.** Standing it up was a single server binary or Docker image, which is easy; the operational weight is that you'd be running **unmaintained software**: no upstream security patches, no dependency updates, and any bug you hit is yours to fix in a fork. The compiled-plugin model also means your ops includes a build step for every pipeline job and managing the SDK/toolchain per language. For a *new* deployment the honest difficulty is "high", because the real cost is the maintenance you inherit, not the install. [推断]

## Health & viability

- **Responsiveness**: Grade E.
- **Maintenance (2026-06).** **Archived** — the repo is read-only. Last release v0.2.9 in 2022-01; last push 2026-01 is consistent with an archive/housekeeping action, not active development. **Abandoned** for practical purposes. [推断]
- **Governance / bus factor.** Lived under the `gaia-pipeline` org but driven by a small core (michelvocks, Skarlso); with the project archived, there is effectively **no active maintainer or roadmap**. [推断]
- **Age & Lindy verdict.** Created 2017-12 (~8 years) but **archived** ⇒ Lindy **fails**: age without ongoing activity is a negative signal, not a positive one. A long-abandoned project is *less* safe to bet on, not more. [推断]
- **Adoption.** ~5.2k stars reflect past interest, but stars are historical and don't imply current users; with no releases since 2022 and an archive flag, assume the community has moved on. [未验证]
- **Risk flags.** The archive status is the dominant risk. Apache-2.0 license is permissive (forking is allowed), but adopting means owning all future maintenance. [推断]

## Caveats (unverified)

- [未验证] Repository is archived per GitHub metadata; ~5.2k stars and last release v0.2.9 (2022-01) as of 2026-06 — numbers are date-sensitive.
- [推断] "Archived = abandoned" is inferred from GitHub's archived flag + no release since 2022; there is no guarantee a maintainer returns, and none is implied.
- [未验证] Internal architecture (HashiCorp `go-plugin`/gRPC, Vue frontend, embedded metadata store) is stated from the project's historical README/docs and not re-verified against current source.
- [未验证] Supported pipeline languages and the exact SDK surface are from the project's marketing; verify against the (frozen) source before any fork decision.
