# observability

> 分类节点。在多数据源的指标/日志/追踪之上做看板、告警与可视化。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Grafana** | 当你需要在 Prometheus/Loki/Elasticsearch 等多数据源之上加一层统一看板和告警时用它——它做可视化，不做存储。 | B（5/6） | [→](grafana.zh.md) |
| **Prometheus** | The Prometheus monitoring system and time series database. | A（6/6） | [→](prometheus.zh.md) |
| **OpenTelemetry Collector** | OpenTelemetry Collector | A（5/6） | [→](opentelemetry-collector.zh.md) |
| **Loki** | Like Prometheus, but for logs. | B（6/6） | [→](loki.zh.md) |
| **Jaeger** | CNCF Jaeger, a Distributed Tracing Platform | A（5/6） | [→](jaeger.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Grafana](grafana.zh.md) | ✅ | B（5/6） | 多数据源之上的统一看板/告警；是可视化层而非存储（AGPL-3.0）。 |
| [Telegraf](../dev-utilities/ops-infra/telegraf.zh.md) | ✅ | A（5/6） | 插件驱动的采集/路由 agent，负责把数据喂给 Grafana 读取的后端——分工不同。 |
| Kibana / Datadog / Apache Superset | 未收录 | — | 各页对比里点到的其他看板/可观测/BI 方案。 |

## 什么该放这里

主要职责是在你已经运行的数据源之上**可视化与告警**指标/日志/追踪的工具。不含采集 agent（见 `dev-utilities` → Telegraf），不含 SQL/BI 分析（见 `data-visualization`）。
