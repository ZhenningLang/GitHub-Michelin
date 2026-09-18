# kafka-tools

> Category node. Apache Kafka clients and management UIs.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **UI for Apache Kafka (provectus/kafka-ui)** | Use it when you want a one-`docker run` web dashboard to browse Kafka brokers, topics, and consumer-group lag — but this `provectus` upstream is stalled (last release 2024-04); deploy the maintained `kafbat/kafka-ui` fork instead. | D (3/6) | [→](kafka-ui.md) |
| **kafka-python** | Use it when you want a pure-Python Kafka client that just `pip install`s with no librdkafka to compile — but a pure-Python client can't match `confluent-kafka`'s throughput and may trail the newest broker features. | A (6/6) | [→](kafka-python.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [UI for Apache Kafka (provectus/kafka-ui)](kafka-ui.md) | ✅ | D (3/6) | Use it when you want a one-`docker run` web dashboard to browse Kafka brokers, topics, and consumer-group lag — but this `provectus` upstream is stalled (last release 2024-04); deploy the maintained `kafbat/kafka-ui` fork instead. |
| [kafka-python](kafka-python.md) | ✅ | A (6/6) | Use it when you want a pure-Python Kafka client that just `pip install`s with no librdkafka to compile — but a pure-Python client can't match `confluent-kafka`'s throughput and may trail the newest broker features. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Clients and management UIs for **Apache Kafka**. General messaging libs may live in `task-queue`.
