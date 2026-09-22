---
name: Celery
slug: celery
repo: https://github.com/celery/celery
category: task-queue
tags: [task-queue, distributed, async, background-jobs, workers, scheduling, python, broker]
language: Python
license: BSD-3-Clause
maturity: v5.x, active (2026-06), ~28.6k stars
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-06-27T11:27:51Z
  default_branch: main
  default_branch_sha: d6131816f172750f7ba6204f903cd2fc243853ad
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:13:59Z
  overall: B
  overall_score: 3.4
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 99.5
        qualifying_issues: 11
        band: default
        window_offset_days: 8
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: celery
        dependent_repos_count: 40119
        downloads_last_month: 53621751
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.02
    longevity:
      grade: A
      raw:
        repo_age_days: 6279
        last_commit_age_days: 2
        cohort: framework
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 21
        top1_share: 0.644
        top3_share: 0.8
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Celery

The de-facto Python distributed task queue: hand off asynchronous and background jobs to a pool of workers over a message broker (RabbitMQ/Redis), with retries, scheduling (beat), routing, and an optional result backend.

![celery — health radar](../../assets/health/celery.svg)

## When to use

You're building a Python web app — Django or FastAPI — and your request handlers are starting to do too much. Sending the welcome email, generating the PDF invoice, transcoding the upload, calling three slow third-party APIs: all of it is blocking the HTTP response and your p99 is climbing. You don't want users staring at a spinner while a 20-second job runs inline, and you can't just spawn threads because you need the work to survive a process restart and scale across machines. You reach for Celery: you decorate the slow function as a `@app.task`, call `process_upload.delay(upload_id)` from the view, and the request returns immediately. A separate pool of Celery workers — on the same box or a fleet of them — pulls the job off RabbitMQ or Redis and runs it, retrying with backoff if the third-party API times out.

As the app grows you lean on the rest of the framework: `beat` for cron-like periodic tasks (nightly reports, cache warmups), routing so heavy GPU jobs go to a dedicated queue and worker pool, `chain`/`group`/`chord` canvas primitives to fan out and join work, rate limiting, and a result backend (Redis/DB) when a caller actually needs the return value. It's the boring, proven default for "run this Python work later, elsewhere, reliably" — and the surrounding ecosystem (Flower for monitoring, Django integration, mature broker support) means you're rarely the first to hit a problem.

## When NOT to use

- **Your jobs are simple and your scale is modest.** Celery carries real operational weight — a broker *plus* worker processes *plus* (often) a result backend, plus the failure modes of all three. For a single app that just needs a few background jobs, lighter task queues like **RQ**, **Dramatiq**, or **arq** are far less to stand up and reason about.
- **You need a data-pipeline / DAG orchestrator.** Celery runs independent tasks; it is not built to express "step B runs after A succeeds, then C and D in parallel, backfill last Tuesday, show me the DAG." For scheduled multi-step data workflows with dependencies and lineage, use [Airflow](../workflow-orchestration/airflow.md) (or Prefect/Dagster).
- **You're not on Python.** Celery is a Python framework. A JVM/Spring shop wanting a managed, dashboard-driven scheduler should look at [XXL-JOB](xxl-job.md); other ecosystems have their own (Sidekiq for Ruby, BullMQ for Node).
- **You need exactly-once or strict ordering guarantees.** Celery is at-least-once by default — tasks can run more than once (redelivery, visibility timeouts), so your tasks must be idempotent. If you need strong delivery/ordering semantics, that's a broker/stream design problem, not something Celery hands you for free. [推断]
- **You want deep visibility out of the box.** Knowing *why* a task is stuck, lost, or duplicated has historically been a Celery foot-gun — debugging the worker/broker/backend triangle (especially Redis as broker) takes operational maturity. Budget for Flower/metrics and broker-level inspection.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [RQ (Redis Queue)](rq.md) | ✅ | Choose RQ when Redis-only simplicity matters more than broker choice, routing, scheduling, and throughput tuning. | Dead-simple to run and read, but narrower than Celery's broker/backend and workflow surface. |
| [Dramatiq](dramatiq.md) | ✅ | Choose Dramatiq when you want a modern Python task queue with RabbitMQ/Redis support and fewer Celery-era foot-guns. | Smaller ecosystem and fewer canvas/workflow primitives than Celery. |
| [arq](arq.md) | ✅ | Choose arq when your app is already asyncio-first and a lightweight Redis queue is enough. | Good async ergonomics, but minimal compared with Celery's routing, beat, and canvas. |
| [Airflow](../workflow-orchestration/airflow.md) | ✅ | Choose Airflow when dependency-aware multi-step DAG **workflows**, lineage, backfills, and UI matter more than low-latency task offload. | Data-pipeline orchestration, not a direct background-job queue. |
| [XXL-JOB](xxl-job.md) | ✅ | Choose XXL-JOB when a JVM/Spring distributed scheduler with built-in admin dashboard is the requirement. | The Java-world scheduler answer; not a natural fit for a Python codebase. |
| Sidekiq / BullMQ | 未收录 | Choose Sidekiq or BullMQ when the same background-job problem lives in Ruby or Node instead of Python. | Same problem shape, different language ecosystem. |

## Tech stack

- **Language:** Python (pure-Python framework; runs on CPython, supports modern 3.x).
- **Brokers (pluggable transport):** RabbitMQ (AMQP, the reference broker) and Redis are first-class; others (e.g. SQS) exist with varying support — verify your transport's feature parity. [未验证]
- **Result backend (optional):** Redis, databases (SQLAlchemy/Django ORM), RabbitMQ/RPC, and others — only needed when callers consume task return values or states.
- **Core libraries:** `kombu` (messaging/transport abstraction), `billiard` (process pool), `click` (CLI). Scheduling via `celery beat`; monitoring commonly via Flower.
- **Primitives:** tasks, queues/routing, retries, rate limits, and canvas (`chain`, `group`, `chord`, `map`, `chunks`) for composing workflows.

## Dependencies

- **A message broker (required):** you must run RabbitMQ or Redis (or another supported transport). This is the backbone — Celery does not ship one.
- **A result backend (optional):** required only if you need task results/states (Redis or a DB are common). Many fire-and-forget setups skip it.
- **Worker processes:** one or more Celery worker processes (and `beat` if you use periodic tasks) running alongside your app, supervised by systemd/Docker/Kubernetes.
- **Python runtime + the broker client libs** (e.g. `redis`/`amqp` via kombu) installed in your environment.

## Ops difficulty

**Medium-to-high.** A toy setup is easy — `pip install celery`, point it at a local Redis, start a worker. Production is where the weight shows: you're now operating (at least) a broker and a worker fleet as long-running stateful infrastructure, plus often a result backend. You have to supervise and autoscale workers, size prefetch/concurrency, set acks-late and visibility timeouts correctly (especially with Redis as broker, where misconfiguration causes duplicate or lost tasks), watch queue depth and dead/stuck tasks, and roll out worker code without dropping in-flight jobs. The classic pain is observability: when a task vanishes or runs twice, you're debugging across the worker, the broker, and the backend at once. Flower, broker dashboards, and task-level metrics/idempotency are not optional at scale.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 99.5 hours across 11 qualifying issues/PRs.
- **Maintenance (2026-06).** Repo last pushed 2026-06 and actively shipping on the v5.x line (latest release v5.6.3, 2026-03) — **active**, not coasting; not archived. [推断]
- **Governance / bus factor.** Owned by the `celery` GitHub **organization** with a broad contributor base over many years rather than a single author — but it's community/volunteer-maintained without a large foundation or vendor bankrolling it, so sustained maintainer bandwidth is the thing to watch. [推断]
- **Age & Lindy verdict.** Created **2009-04 (~17 years)** and **still actively maintained** ⇒ a **very strong Lindy** signal — one of the longest-lived, most battle-tested task queues in any language, the boring proven default rather than a hyped newcomer. [推断]
- **Adoption & ecosystem.** Ubiquitous in Python: the default background-job framework for Django/Flask/FastAPI stacks, huge real-world deployment base, mature docs, first-class broker support, and an ecosystem (Flower, django-celery-beat/results, integrations). ~28.6k stars is indicative of broad adoption. [未验证]
- **Risk flags.** No relicense history — **BSD-3-Clause** permissive throughout; main risk is the operational complexity / debuggability discussed above, plus reliance on community maintenance rather than a funded backer. [推断]

## Caveats (unverified)

- [未验证] ~28.6k GitHub stars and latest release v5.6.3 (2026-03) as of 2026-06 — star counts and version numbers are date-sensitive and drift; treat as indicative.
- [未验证] Creation date 2009-04 and "~17 years" age are from the project's history as recalled here; re-verify against the repo's actual creation date.
- [未验证] Broker/transport feature parity differs (RabbitMQ vs Redis vs SQS, etc.) and shifts release-to-release; confirm your transport supports the features you rely on.
- [推断] At-least-once delivery and the "tasks must be idempotent" / no exactly-once guarantee framing is general distributed-queue reasoning applied to Celery, not a quoted guarantee — and behavior depends on broker + ack/visibility config.
- [推断] "Medium-to-high" ops difficulty and the "visibility foot-gun" framing are judgment from the worker/broker/backend architecture, not a measured benchmark.
