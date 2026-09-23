# observability

> Category node. Dashboards, alerting, and visualization over metrics/logs/traces from many datasources.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Grafana** | Use it when you need one dashboard + alerting layer over Prometheus/Loki/Elasticsearch and other sources — it visualizes, it doesn't store. | B (5/6) | [→](grafana.md) |
| **Prometheus** | The Prometheus monitoring system and time series database. | A (6/6) | [→](prometheus.md) |
| **OpenTelemetry Collector** | OpenTelemetry Collector | A (5/6) | [→](opentelemetry-collector.md) |
| **Loki** | Like Prometheus, but for logs. | B (6/6) | [→](loki.md) |
| **Jaeger** | CNCF Jaeger, a Distributed Tracing Platform | A (6/6) | [→](jaeger.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Grafana](grafana.md) | ✅ | B (5/6) | Unified dashboard/alerting over many datasources; a visualization layer, not a datastore (AGPL-3.0). |
| [Telegraf](../dev-utilities/ops-infra/telegraf.md) | ✅ | A (6/6) | Plugin-driven collection/routing agent that feeds the backends Grafana reads — different job. |
| Kibana / Datadog / Apache Superset | partly indexed | — | Other dashboard/observability/BI stacks named across the pages; Apache Superset is indexed under data-visualization, Kibana and Datadog are not. |

## What belongs here

Tools whose primary job is **visualizing and alerting** on metrics/logs/traces from datasources you already run. Not collection agents (see `dev-utilities` → Telegraf), not SQL/BI analytics (see `data-visualization`).
