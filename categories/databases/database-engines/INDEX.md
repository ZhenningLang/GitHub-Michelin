# database-engines

> Category node. Database engines and self-hosted database services.
> ← back to [databases](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **ClickHouse** | Use it when a self-hosted team needs sub-second SQL aggregates over hundreds of millions of append-mostly events served to many dashboard users — but not for transactional row updates, unbatched single-row inserts, or data one laptop process could handle with DuckDB. | A (5/6) | [→](clickhouse.md) |
| **DuckDB** | Use it when one script, notebook or CI job needs fast SQL joins and aggregates over local or S3 Parquet/CSV files without running a server — but not when several processes must write the same database or the data exceeds one machine. | A (5/6) | [→](duckdb.md) |
| **PikiwiDB** | A Redis-protocol-compatible, disk-backed KV store (RocksDB engine) built by Qihoo360's infra team — keeps hot data in memory and persists the full dataset to disk so a single node can hold hundreds of GB the way Redis can't. (This repo is the home of the project historically known as **Pika**.) | B (6/6) | [→](pikiwidb.md) |
| **Supabase** | Use it when a small team needs auth, auto-generated APIs, storage and realtime on one Postgres this month, with row-level security as access control — but self-hosting in production needs an owner: the bundle is community-supported and insecure by default. | A (5/6) | [→](supabase.md) |
| **Turso Database** | Use it when an app, agent or edge service that already stores data in SQLite files needs async I/O, experimental multi-writer MVCC or vector search from a Rust rewrite — but it is pre-1.0, single-process, and not yet a full SQLite superset. | A (6/6) | [→](turso.md) |
| **Valkey** | Use it when your caches, sessions and rate limits run on Redis and you need a BSD-licensed, vendor-neutral drop-in after Redis's relicensing — but not if you need Redis 8's newest built-ins or a dataset larger than RAM. | A (6/6) | [→](valkey.md) |

## What belongs here

Database engines and self-hosted database services.
