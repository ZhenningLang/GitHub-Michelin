# data-sync

> Category node. CDC, replication, and database-to-database sync tools.
> ← back to [databases](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Debezium** | Use it when a search index, cache or other service must follow one operational database and dual writes or `updated_at` polling keep drifting or missing deletes — but the default deployment means running Kafka and Kafka Connect. | A (5/6) | [→](debezium.md) |
| **go-mysql-elasticsearch** | Use it when you need a single Go binary that dumps MySQL into Elasticsearch and then tails the binlog for one-way sync — but it has been unmaintained since 2020 and supports only MySQL below 8.0 and ES below 6.0. | D (4/6) | [→](go-mysql-elasticsearch.md) |
| **python-mysql-replication** | A pure-Python implementation of the MySQL replication protocol (built on PyMySQL): connect as a fake replica, stream the binlog, and get parsed row/query/rotate events as Python objects — the building block under most Python CDC tooling for MySQL. | B (4/6) | [→](python-mysql-replication.md) |

## What belongs here

CDC, replication, and database-to-database sync tools.
