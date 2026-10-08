# data-sync

> 分类节点。CDC、复制与数据库同步工具。
> ← 返回[databases](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Debezium** | 当搜索索引、缓存或其他服务要跟着一个业务数据库走，而双写或按 `updated_at` 轮询总是不一致、漏掉删除时用它——但默认部署意味着要运维 Kafka 和 Kafka Connect。 | A（5/6） | [→](debezium.zh.md) |
| **go-mysql-elasticsearch** | 当你要一个单独的 Go 进程，先把 MySQL dump 进 Elasticsearch、再 tail binlog 做单向同步时用它——但它自 2020 年起无人维护，只支持 MySQL 8.0 以下和 ES 6.0 以下。 | D（4/6） | [→](go-mysql-elasticsearch.zh.md) |
| **python-mysql-replication** | MySQL 复制协议的纯 Python 实现（构建于 PyMySQL）：以伪从库身份连接、流式读取 binlog，把解析后的 row／query／rotate 事件作为 Python 对象交给你——大多数 Python MySQL CDC 工具底下的那块积木。 | B（4/6） | [→](python-mysql-replication.zh.md) |

## 什么该放这里

CDC、复制与数据库同步工具。
