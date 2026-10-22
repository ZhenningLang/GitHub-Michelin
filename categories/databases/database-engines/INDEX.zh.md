# database-engines

> 分类节点。数据库引擎与可自建数据库服务。
> ← 返回[databases](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **KiviDB** | 试用多核 Redis 协议存储与内置关键词／向量搜索；AGPL 和五天公开历史要求先测兼容性与恢复。 | D（5/6） | [→](kividb.zh.md) |
| **DuckDB Object Storage** | 让原生 DuckDB 经 SlateDB 持久化到本地或对象存储，要求单写者。 | C（6/6） | [→](duckdb-object-storage.zh.md) |
| **ClickHouse** | 当团队要在自托管服务端上，对几亿行以追加为主的事件数据做亚秒级 SQL 聚合、供很多人同时看板时用它——但不适合频繁单行更新的事务负载、不攒批的逐行写入，或一台笔记本单进程用 DuckDB 就能搞定的数据量。 | A（5/6） | [→](clickhouse.zh.md) |
| **DuckDB** | 当一个脚本、notebook 或 CI 任务要对本地或 S3 上的 Parquet/CSV 直接做快速 SQL 关联和聚合、又不想起服务端时用它——但多个进程要同时写同一个库，或数据超出一台机器时不适合。 | A（5/6） | [→](duckdb.zh.md) |
| **PikiwiDB** | 一个兼容 Redis 协议、落盘的 KV 存储（RocksDB 引擎），由 Qihoo360 基础架构团队打造——热数据留在内存，全量数据持久化到磁盘，于是单节点能装下 Redis 装不下的几百 GB。（本仓库就是历史上称为 **Pika** 的项目所在地。） | B（6/6） | [→](pikiwidb.zh.md) |
| **Supabase** | 当小团队这个月就要在同一个 Postgres 上拿到认证、自动生成的 API、文件存储和实时更新，并用行级安全做权限时用它——但生产自托管必须有人负责：自托管包只有社区支持，默认配置不安全。 | A（5/6） | [→](supabase.zh.md) |
| **Turso Database** | 已经把数据放在 SQLite 文件里的应用、agent 或边缘服务，想要异步 I/O、实验性的多写者 MVCC 或向量检索时用它（Rust 重写版）——但它还没到 1.0、只支持单进程，也还不是完整的 SQLite 超集。 | A（6/6） | [→](turso.zh.md) |
| **Valkey** | 当缓存、会话和限流都跑在 Redis 上，而 Redis 改许可后你需要一个 BSD 许可、厂商中立、可直接替换的版本时用它——但要用 Redis 8 最新的内置功能，或数据集大于内存时不适合。 | A（6/6） | [→](valkey.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [DuckDB Object Storage](duckdb-object-storage.zh.md) | ✅ | C（6/6） | 虚拟化原生数据库文件；无多写者锁，远程读存在可见性延迟。 |
| [KiviDB](kividb.zh.md) | ✅ | D（5/6） | 搜索与共享内存多核存储集成；不是已充分验证的 Redis 等价替代，也不解决磁盘容量扩展。 |

## 什么该放这里

数据库引擎与可自建数据库服务。
