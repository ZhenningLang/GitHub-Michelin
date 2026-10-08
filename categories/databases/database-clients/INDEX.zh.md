# database-clients

> 分类节点。数据库客户端、GUI、查询层与检查工具。
> ← 返回[databases](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **DBeaver** | 当你要在 Postgres、SQL Server、Oracle、ClickHouse、SQLite 之间来回切，想用一个免费桌面客户端给它们统一配上编辑器、数据表格和 ER 图时用它——但 NoSQL 驱动只在 Pro 版，它也是个偏重的单用户 Eclipse 应用。 | A（6/6） | [→](dbeaver.zh.md) |
| **elasticsearch-dsl-py** | 只在阅读或迁移锁定 elasticsearch-dsl 8.17 及更老版本的遗留代码时用它——但它已归档；新代码请装 `elasticsearch>=8.18` 并改用 `elasticsearch.dsl`。 | C（5/6） | [→](elasticsearch-dsl-py.zh.md) |
| **elasticsearch-sql** | 用 SQL 而非原生 JSON Query DSL 查询 Elasticsearch——一个社区插件（兼库），把 SQL 解析并翻译成 ES 查询／聚合，发布版与你所跑的 ES 大版本对齐。 | C（5/6） | [→](elasticsearch-sql.zh.md) |
| **PrettyZoo** | 当你想用桌面 GUI 浏览、轻量编辑 ZooKeeper 的 znode 树、节点数据和 ACL，而不想敲 `zkCli.sh` 时用它——但它已归档，作者 2024-01 宣布停止维护。 | D（5/6） | [→](prettyzoo.zh.md) |
| **RDR** | 当 Redis 撞上 maxmemory、你要离线解析 RDB 快照找出吃内存的 key 前缀、又不想给生产加负载时用它——但它自 2020 年起冻结，内存数字也只是近似值。 | D（4/6） | [→](rdr.zh.md) |
| **MCP Toolbox for Databases** | 当生产 agent 要查多种数据库（57 种数据源、Google Cloud 一等公民），且只能走你在 YAML 里声明的参数化语句时用它——但引擎级只读只在 Cloud SQL／AlloyDB／BigQuery 上有，网络默认值也偏宽松。 | A（6/6） | [→](mcp-toolbox.zh.md) |

## 什么该放这里

数据库客户端、GUI、查询层与检查工具。
