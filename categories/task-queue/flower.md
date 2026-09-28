---
name: Flower
slug: flower
repo: https://github.com/mher/flower
category: task-queue
tags: [celery, monitoring, web-admin, task-queue, dashboard, real-time, python]
language: Python
license: BSD-3-Clause
maturity: v2.x, active (2026-09), ~7.2k stars
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-22T14:15:14Z
  default_branch: master
  default_branch_sha: ea34f92dc4c898a6788af13ec8e36d1d53d357d1
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T09:03:40Z
  overall: B
  overall_score: 3.0
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 16
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 239.5
        qualifying_issues: 6
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: flower
        dependent_repos_count: 3295
        downloads_last_month: 8044726
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.0
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5195
        last_commit_age_days: 16
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 8
        top1_share: 0.927
        top3_share: 0.964
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Flower

A real-time web dashboard and admin tool for Celery — it shows live task/worker state, lets you inspect and control workers, and exposes a REST API and Prometheus metrics for a running Celery cluster.

![flower — health radar](../../assets/health/flower.svg)

## When to use

You're running a Celery deployment in production and you're flying blind: tasks are queued in Redis or RabbitMQ, workers are processing them somewhere, but when something stalls you're grepping worker logs and guessing. You drop in Flower as a separate process pointed at the same broker (`celery --broker=... flower`) and immediately get a web UI showing every worker, its concurrency and pool, the live stream of tasks with their args/results/runtime, and which tasks are pending, succeeded, retried, or failed. When a worker is wedged you can inspect it, rate-limit it, revoke a task, or restart its pool from the browser instead of SSHing around. You wire its `/metrics` endpoint into Prometheus so task throughput and failure rates show up next to the rest of your dashboards, and you put it behind your auth (basic auth, OAuth) since it can control workers.

You reach for Flower specifically because it's the de-facto, purpose-built monitor for Celery — it speaks Celery's events natively, so there's no exporter to write or schema to map. If your team already runs Celery and just needs *visibility and basic control* without standing up a full APM stack, Flower is the lightweight answer.

## How it works

Flower rides Celery's built-in telemetry instead of embedding anything in your workers. Celery workers publish *events* (task received/succeeded/failed, worker heartbeats and stats) onto a broadcast exchange on the broker; Flower subscribes to that exchange and keeps an in-memory view of the cluster, which it renders as a live web UI. Control flows the other way: when you revoke a task or resize a pool in the browser, Flower sends Celery's worker-control command back over the same broker, and the workers respond — no agent, no extra port on the workers. On top of the UI it exposes two programmatic surfaces: a JSON REST API mirroring the dashboard, and a Prometheus `/metrics` endpoint (`localhost:5555/metrics` by default). What stays yours: running Flower as another supervised process pointed at the right broker URL, and putting auth in front of it — an unauthenticated Flower is a remote control for your queue. Its event stream is best-effort and its task history is in-memory, so treat counts as live diagnostics, not a ledger that survives restarts.

![Flower — backbone user story](../../assets/flow/flower.svg)

<!-- flow-steps:begin (generated from flows/flower.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install Flower where your Celery app and broker URL are reachable — `pip install flower`
2. **You**: Point it at the cluster's broker and start the dashboard — `celery --broker=amqp://guest:guest@localhost:5672// flower` — component: `web UI on port 5555`
3. **Flower**: Joins the cluster's event feed and renders live worker and task state — component: `Celery events`
4. **You**: Drill in from the UI, or act via the REST API (revoke a task, grow a pool)
5. **Flower**: Sends control commands over the broker and serves /metrics for Prometheus scraping — component: `worker control`

**Value**: A running Celery cluster becomes visible and operable from one web page, with no agent installed on any worker

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You're not running Celery.** Flower is Celery-specific. For arbitrary queues (Sidekiq, RQ, Dramatiq, BullMQ) or a non-Celery stack, it doesn't apply — use that system's own dashboard.
- **You need durable historical analytics.** Flower's task history is in-memory by default and bounded; it's a *real-time* monitor, not a long-term store. For trend analysis, push events to Prometheus/your TSDB or a results backend rather than relying on Flower to retain them.
- **You need full APM (traces, profiling, alerting).** Flower shows state and basic metrics; it has no tracing, profiling, or alerting engine. Pair it with Prometheus+Alertmanager/Grafana or an APM product for that.
- **You're exposing it carelessly.** It can revoke tasks and restart worker pools — an unauthenticated Flower is a remote-control panel for your queue. It must sit behind auth and not be public. [推断]
- **You want guaranteed event delivery for accounting.** Flower observes Celery's event stream, which is best-effort; don't treat its counts as a billing-grade ledger.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Celery](celery.md) | ✅ | Choose Celery when you need the task framework itself, not the dashboard that monitors it. | Celery's `inspect`/`control` CLI gives raw access but no UI. Flower is the dashboard *for* Celery, not a substitute. |
| Prometheus + [Grafana](../observability/grafana.md) (celery-exporter) | 部分已收录 | Choose Prometheus/Grafana when long-term metrics, alerting, and unified dashboards matter more than live task control. | More to operate and no live per-task drill-down or worker control. Grafana is indexed; Prometheus and celery-exporter are not. Often run *alongside* Flower. |
| Celery `events`/`inspect` CLI | 未收录 | Choose the built-in Celery CLI when zero extra process is worth giving up a web UI and REST API. | Terminal-only, no at-a-glance fleet view. |
| [Apache Airflow](../workflow-orchestration/airflow.md) UI | ✅ | Choose Airflow UI when you are operating scheduled DAG workflows, not monitoring ad-hoc Celery tasks. | Different model: scheduled workflows vs. background task queues. |
| Datadog / Sentry / commercial APM | 未收录 | Choose commercial APM when traces, alerting, and fleet-wide observability matter more than a Celery-purpose-built dashboard. | Paid and heavier, but broader than Flower. |

## Tech stack

- **Language:** Python (3.10–3.14 classifiers per `setup.py`, `python_requires>=3.10`); a Tornado-based web server (requires `tornado>=6.5.7,<7`) serving the dashboard and REST API, with `prometheus_client` for the metrics endpoint.
- **Integration:** consumes Celery's native event stream and worker control protocol over the broker (`celery>=5.0.5` is a hard requirement) — no separate agent on workers.
- **Interfaces:** web UI, a JSON REST API for task/worker inspection and control, and a Prometheus `/metrics` endpoint.
- **Auth:** pluggable — HTTP basic auth, Google/GitHub/GitLab/Okta OAuth (per the 2026 README), and reverse-proxy auth.

## Dependencies

- **Runtime:** Python plus Celery and the same broker your app uses (Redis, RabbitMQ, etc.); Flower connects to that broker to read events and send control commands.
- **Deploy unit:** a single extra process/container alongside your Celery cluster; commonly run via `celery --broker=... flower` (or `celery -A tasks.app flower`) and the `mher/flower` Docker image.
- **Install:** `pip install flower` from PyPI, or the published Docker image.

## Ops difficulty

**Low.** It's one stateless process you point at your broker — `pip install flower` (or the Docker image), set the broker URL, put it behind auth, and expose its port. There's no datastore to run for Flower itself. The real operational care is **security** (it controls workers, so never expose it unauthenticated) and remembering that its in-memory history doesn't survive restarts, so anything you need long-term must go to Prometheus or a results backend. At fleet scale you may run one Flower per Celery cluster and front it with your ingress/auth proxy. Compared to standing up a full metrics-and-alerting stack, Flower is the easy, drop-in piece.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 239.5 hours across 6 qualifying issues/PRs; help is slow but it does arrive.
- **Maintenance (2026-09).** Tagged releases are back after a long gap: v2.1.0 (2026-08-16) and v2.2.0 (2026-09-22) followed v2.0.1 (2023-08), and the repo was last pushed 2026-09 — **active** again, not abandoned. Not archived.
- **Governance / bus factor.** Owned by an **individual account** (`mher`) with ~7.2k stars — a high-stars, single-owner project is a **bus-factor flag**: contribution comes partly from the Celery maintainer circle (ask, auvipy), but the namespace and final say rest with one person. [推断]
- **Age & Lindy verdict.** Created 2012-07 (GitHub `created_at`), ~14 years old and **active again in 2026** ⇒ a **strong Lindy** signal with a caveat: it has been *the* Celery dashboard for over a decade, but the 2023–2026 release gap shows maintenance can stall.
- **Adoption.** The de-facto monitor wherever Celery runs in production — ~7.2k stars (2026-09), 8,044,726 monthly PyPI downloads, and a widely-pulled Docker image indicate broad real-world use.
- **Risk flags.** License is BSD-3-Clause (confirmed from the LICENSE file; GitHub's API reports `NOASSERTION`), no relicense history found; the main flags are single-owner governance and the security exposure of an admin tool.

## Caveats (unverified)

- [未验证] License: GitHub's API returns `NOASSERTION` and PyPI reports plain `BSD`, but the repo's LICENSE file and README state a 3-clause BSD license (Copyright Mher Movsisyan and contributors) — recorded here as BSD-3-Clause.
- [未验证] ~7.2k GitHub stars as of 2026-09; latest tagged release v2.2.0 (2026-09-22). Release cadence restarted only in 2026 after v2.0.1 sat from 2023-08 — treat the burst of activity as recovery, not a settled rhythm.
- [推断] Task history retention is in-memory and bounded by default; durability and limits depend on configuration and version — verify before relying on Flower for historical data.
- [推断] Worker-control capabilities make an unauthenticated deployment dangerous; the auth-required posture is inferred from the tool's function, not a measured security claim.
- [未验证] Tornado web server and OAuth provider support are stated from the repo's requirements/README at 2026-09; exact supported providers and Python versions shift across releases.
