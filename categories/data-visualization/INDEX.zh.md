# data-visualization

> 分类节点。在 SQL 数据仓库之上自托管的 BI / 数据探索看板。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Apache Superset** | 当你想要在数据仓库之上自托管 SQL BI 看板与探索时用它——不是基础设施指标/可观测性。 | A（6/6） | [→](superset.zh.md) |
| **Evidence** | Business intelligence as code: build fast, interactive data visualizations in SQL and markdown | B（5/6） | [→](evidence.zh.md) |
| **Metabase** | The easy-to-use open source Business Intelligence and Embedded Analytics tool that lets everyone work with data :bar_chart: | A（4/6） | [→](metabase.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Apache Superset](superset.zh.md) | ✅ | A（6/6） | 在仓库之上自托管 SQL BI + 探索；部署比 Metabase 更重（多服务）。 |
| [Grafana](../observability/grafana.zh.md) | ✅ | B（5/6） | 面向指标/日志/追踪的可观测性看板——非仓库 BI，受众不同。 |
| Metabase / Redash / Tableau / Looker | 未收录 | — | 各页对比里点到的其他 BI/分析工具。 |

## 什么该放这里

主要职责是给分析师做**SQL 仓库之上的 BI 看板与数据探索**的工具。不含基础设施指标/可观测性（见 `observability`），不含文档/图检索（见 `rag-retrieval`）。
