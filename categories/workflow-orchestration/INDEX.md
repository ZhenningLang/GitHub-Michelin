# workflow-orchestration

> Category node. Author, schedule, and monitor batch data/workflow pipelines (DAG orchestrators).
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Apache Airflow** | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. | A (6/6) | [→](airflow.md) |
| **Gaia** | Use it when studying the "pipelines-as-compiled-plugins" design as a read-only reference — the repo is archived and abandoned, never pick it for new production work. | D (6/6) | [→](gaia.md) |
| **Airflow Maintenance DAGs** | Use it when self-managed Airflow needs proven copy-in DAGs to clean metadata-DB rows and stale logs — they run destructive DELETEs tied to version-specific internals, so dry-run and back up first. | D (4/6) | [→](airflow-maintenance-dags.md) |
| **n8n** | Use it when you need a visual-first workflow automation platform with 400+ integrations, native AI capabilities, and the option to self-host — but not for sub-second real-time streaming or fully unrestricted open-source use. | A (4/6) | [→](n8n.md) |
| **Argo Workflows** | Workflow Engine for Kubernetes | A (6/6) | [→](argo-workflows.md) |
| **Prefect** | Prefect is a workflow orchestration framework for building resilient data pipelines in Python. | A (6/6) | [→](prefect.md) |
| **Dagster** | An orchestration platform for the development, production, and observation of data assets. | A (6/6) | [→](dagster.md) |
| **Temporal** | Temporal service | A (6/6) | [→](temporal.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Apache Airflow](airflow.md) | ✅ | A (6/6) | Use it when you orchestrate scheduled batch data pipelines as Python DAGs with a UI — not low-latency or event-driven flows. |
| [Gaia](gaia.md) | ✅ | D (6/6) | Use it when studying the "pipelines-as-compiled-plugins" design as a read-only reference — the repo is archived and abandoned, never pick it for new production work. |
| [Airflow Maintenance DAGs](airflow-maintenance-dags.md) | ✅ | D (4/6) | Use it when self-managed Airflow needs proven copy-in DAGs to clean metadata-DB rows and stale logs — they run destructive DELETEs tied to version-specific internals, so dry-run and back up first. |
| [n8n](n8n.md) | ✅ | A (4/6) | Visual-first workflow automation with 400+ integrations and native AI; self-hostable but fair-code licensed and not for real-time streaming. |

## What belongs here

Tools whose primary job is to **author, schedule, and monitor batch data/workflow pipelines** as DAGs. Not low-latency event/stream processing, not agent build/run frameworks (see `agent-frameworks`).
