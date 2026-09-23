# data-sync

> 分类节点。CDC、复制与数据库同步工具。
> ← 返回[databases](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Debezium** | Change data capture for a variety of databases. Please log issues at https://github.com/debezium/dbz/issues. | A（5/6） | [→](debezium.zh.md) |
| **go-mysql-elasticsearch** | 一个小巧的 Go 服务，实时把 MySQL 同步进 Elasticsearch：先做一次初始 dump，再以伪从库身份 tail MySQL binlog，按一份映射规则文件把 insert／update／delete 应用到 ES 索引。 | D（4/6） | [→](go-mysql-elasticsearch.zh.md) |
| **python-mysql-replication** | MySQL 复制协议的纯 Python 实现（构建于 PyMySQL）：以伪从库身份连接、流式读取 binlog，把解析后的 row／query／rotate 事件作为 Python 对象交给你——大多数 Python MySQL CDC 工具底下的那块积木。 | D（5/6） | [→](python-mysql-replication.zh.md) |

## 什么该放这里

CDC、复制与数据库同步工具。
