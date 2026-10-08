# workflow-orchestration

> Category node. Author, schedule, and monitor batch data/workflow pipelines (DAG orchestrators).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Apache Airflow** | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. | A (6/6) | [→](airflow.md) |
| **Gaia** | Use it only when researching the pipelines-as-compiled-plugins design, where jobs are real code run over go-plugin, or deciding whether to fork it — but the repo is archived with its last release in 2022-01, so never pick it for new production work. | D (6/6) | [→](gaia.md) |
| **Airflow Maintenance DAGs** | Use it when a self-managed Airflow cluster is bogged down by old metadata rows and stale logs and you want copy-in cleanup DAGs — but db-cleanup deletes on its first run by default and relies on version-specific internals, so dry-run and back up first. | D (4/6) | [→](airflow-maintenance-dags.md) |
| **n8n** | Use it when a small ops team needs self-hosted SaaS-to-SaaS glue on a visual canvas business people can read, with 1,500+ connector nodes and code fallbacks — but its Sustainable Use License forbids reselling or embedding, and it is not built for sub-second streams. | A (4/6) | [→](n8n.md) |
| **Argo Workflows** | Use it when batch or ML pipelines already run as containers on Kubernetes and you want YAML DAGs where each step is a retried pod with artifacts and a UI — but it needs Kubernetes, and thousands of tiny steps each pay pod startup. | A (6/6) | [→](argo-workflows.md) |
| **Prefect** | Use it when working Python scripts need schedules, retries, run history, and alerts without being rewritten as DAG files — add decorators, keep plain Python control flow — but non-engineer glue fits n8n, and exact crash resumption needs Temporal. | A (6/6) | [→](prefect.md) |
| **Dagster** | Use it when you own a warehouse pipeline and must say which table is stale, what built it, and what depends on it, via Python-declared assets — but Airflow has a broader operator catalog, and alerts, RBAC, and SSO are paid Dagster+ features. | A (6/6) | [→](dagster.md) |
| **Temporal** | Use it when a long-running business process — payments, fulfilment, provisioning, an AI agent — must survive crashes and deploys and resume from the exact step, written as ordinary code — but self-hosting means a multi-service cluster with irreversible shard choices. | A (5/6) | [→](temporal.md) |
| **TanStack Workflow** | Use it when durable, multi-day flows must live inside your TypeScript app on your own database — no workflow server to operate; expect a 0.0.x assembly with no control-plane UI. | C (6/6) | [→](tanstack-workflow.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Apache Airflow](airflow.md) | ✅ | A (6/6) | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. |
| [Gaia](gaia.md) | ✅ | D (6/6) | Gets a readable reference for pipeline jobs written in your own language behind a web UI and scheduler; costs no patches or roadmap, pre-1.0 maturity, and owning every future fix. |
| [Airflow Maintenance DAGs](airflow-maintenance-dags.md) | ✅ | D (4/6) | Gets proven housekeeping that runs on the Airflow you already operate, with nothing new to deploy; costs destructive SQL you own, no commits since 2022-10, and re-testing on every Airflow major version. |
| [n8n](n8n.md) | ✅ | A (4/6) | Visual, self-hosted integrations non-engineers can edit, traded for a source-available internal-use license, paid enterprise features, and a database-backed engine unsuited to high-volume streams. |
| [TanStack Workflow](tanstack-workflow.md) | ✅ | C (6/6) | Headless TypeScript durable execution on your own store — no workflow server like Temporal's, but you assemble store, cron and operations yourself on a 0.0.x surface. |

## What belongs here

Tools whose primary job is to **author, schedule, and monitor batch data/workflow pipelines** as DAGs. Not low-latency event/stream processing, not agent build/run frameworks (see `agent-frameworks`).
