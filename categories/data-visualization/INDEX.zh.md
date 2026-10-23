# data-visualization

> 分类节点。数据图表编译与渲染库，以及在 SQL 仓库之上自托管的 BI／数据探索看板。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Flint** | 复用字段含义和图表映射，投向多个渲染器；须审查溢出警告与后端限制。 | B（6/6） | [→](flint-chart.zh.md) |
| **Rill** | 用 YAML／SQL 评审指标和看板，再在本地或托管部署里探索共同口径。 | A（6/6） | [→](rill.zh.md) |
| **Apache Superset** | 当你想要在数据仓库之上自托管 SQL BI 看板与探索时用它——不是基础设施指标/可观测性。 | A（6/6） | [→](superset.zh.md) |
| **Evidence** | 当分析工程师想把报表写成 git 里的 Markdown 加 SQL 文件，能 diff、能评审、能交给编码 agent 改时用它——但业务人员没法点选出问题，自托管只有 Basic Auth，而且 2026 年的重写让代码库从头来过。 | B（6/6） | [→](evidence.zh.md) |
| **Metabase** | 当不会 SQL 的同事总把简单的数据问题排进你的队列，你想当天就起一个自托管应用、让他们自己点选表、加过滤、存进共享看板时用它——但 SSO、行级权限和 Git 同步都要付费，核心还是 AGPL。 | A（4/6） | [→](metabase.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Flint](flint-chart.zh.md) | ✅ | B（6/6） | 语义图表编译器，可选本地 MCP 渲染；不是带治理的 SQL BI 门户，也不完整抹平后端差异。 |
| [Rill](rill.zh.md) | ✅ | A（6/6） | 代码管理的语义指标，查询 DuckDB／分析引擎；本地 Developer 不等于治理完整的生产门户。 |
| [Apache Superset](superset.zh.md) | ✅ | A（6/6） | 在仓库之上自托管 SQL BI + 探索；部署比 Metabase 更重（多服务）。 |
| [Grafana](../observability/grafana.zh.md) | ✅ | B（5/6） | 面向指标/日志/追踪的可观测性看板——非仓库 BI，受众不同。 |
| Redash / Tableau / Looker | 未收录 | — | 各页对比里点到的其他 BI/分析工具。 |

## 什么该放这里

主要职责是**将表格数据编译成图表**，或给分析师做 **SQL 仓库之上的 BI 看板与数据探索**的工具。图表库消费已准备好的数据，BI 应用覆盖更完整的探索流程。不含基础设施指标／可观测性（见 `observability`），不含文档／图检索（见 `rag-retrieval`）。
