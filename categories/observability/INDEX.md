# observability

> Category node. Dashboards, alerting, and visualization over metrics/logs/traces from many datasources.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Grafana** | Use it when you need one dashboard + alerting layer over Prometheus/Loki/Elasticsearch and other sources — it visualizes, it doesn't store. | B (5/6) | [→](grafana.md) |
| **Prometheus** | Use it when you need per-service request rates, error ratios and latency histograms with PromQL alerts on Kubernetes or cloud-native software that already exposes /metrics — but its local storage is single-node, so long retention or HA needs Thanos, Mimir or VictoriaMetrics. | A (6/6) | [→](prometheus.md) |
| **OpenTelemetry Collector** | Use it when several services send traces, metrics and logs to more than one backend and you want sampling, PII redaction and routing set once in YAML, not per service — but with one service and one OTLP backend it is just an extra process. | A (6/6) | [→](opentelemetry-collector.md) |
| **Loki** | Use it when your Prometheus-and-Grafana stack's log bill is driven by full-text indexing nobody queries, and label-scoped searches by app, namespace or pod are enough — but full-text search across weeks scans every chunk, and it is AGPL-3.0. | B (6/6) | [→](loki.md) |
| **Jaeger** | Use it when a slow request crosses dozens of services and you want a self-hosted, OpenTelemetry-native tracing backend with its own UI under CNCF governance — but you must run its storage database, and v1 binaries and jaeger-client libraries are end-of-life. | A (6/6) | [→](jaeger.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Grafana](grafana.md) | ✅ | B (5/6) | Unified dashboard/alerting over many datasources; a visualization layer, not a datastore (AGPL-3.0). |
| [Telegraf](../dev-utilities/ops-infra/telegraf.md) | ✅ | A (6/6) | Plugin-driven collection/routing agent that feeds the backends Grafana reads — different job. |
| Kibana / Datadog / Apache Superset | partly indexed | — | Other dashboard/observability/BI stacks named across the pages; Apache Superset is indexed under data-visualization, Kibana and Datadog are not. |

## What belongs here

Tools whose primary job is **visualizing and alerting** on metrics/logs/traces from datasources you already run. Not collection agents (see `dev-utilities` → Telegraf), not SQL/BI analytics (see `data-visualization`).
