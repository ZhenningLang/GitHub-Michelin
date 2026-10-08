# observability

> 分类节点。在多数据源的指标/日志/追踪之上做看板、告警与可视化。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Grafana** | 当你需要在 Prometheus/Loki/Elasticsearch 等多数据源之上加一层统一看板和告警时用它——它做可视化，不做存储。 | B（5/6） | [→](grafana.zh.md) |
| **Prometheus** | 当你要在 Kubernetes 或已暴露 /metrics 的云原生软件上拿到每个服务的请求率、错误率、延迟直方图，并用 PromQL 设告警时用它——但本地存储是单节点的，长期保留或高可用要加 Thanos、Mimir 或 VictoriaMetrics。 | A（6/6） | [→](prometheus.zh.md) |
| **OpenTelemetry Collector** | 当多个服务要把链路、指标、日志发往不止一个后端，并希望采样、脱敏、路由都在一份 YAML 里集中配置、而不是写进每个服务时用它——但只有一个服务、一个 OTLP 后端时，它只是多一个进程。 | A（6/6） | [→](opentelemetry-collector.zh.md) |
| **Loki** | 当你的 Prometheus + Grafana 体系里，日志账单主要花在没人查的全文索引上，而按应用、命名空间、Pod 这类标签圈定范围的查询就够用时用它——但跨几周的全文检索要扫遍每个块，而且它是 AGPL-3.0。 | B（6/6） | [→](loki.zh.md) |
| **Jaeger** | 当一个慢请求穿过几十个服务，你想要一个自托管、原生支持 OpenTelemetry、自带界面、由 CNCF 治理的链路追踪后端时用它——但存储数据库得你自己运维，而且 v1 二进制和 jaeger-client 库都已停止维护。 | A（6/6） | [→](jaeger.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Grafana](grafana.zh.md) | ✅ | B（5/6） | 多数据源之上的统一看板/告警；是可视化层而非存储（AGPL-3.0）。 |
| [Telegraf](../dev-utilities/ops-infra/telegraf.zh.md) | ✅ | A（6/6） | 插件驱动的采集/路由 agent，负责把数据喂给 Grafana 读取的后端——分工不同。 |
| Kibana / Datadog / Apache Superset | 部分已收录 | — | 各页对比里点到的其他看板/可观测/BI 方案；其中 Apache Superset 收录在 data-visualization 分类下，Kibana 与 Datadog 尚未收录。 |

## 什么该放这里

主要职责是在你已经运行的数据源之上**可视化与告警**指标/日志/追踪的工具。不含采集 agent（见 `dev-utilities` → Telegraf），不含 SQL/BI 分析（见 `data-visualization`）。
