# task-queue

> Category node. Distributed background job execution — task queues and job schedulers.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **XXL-JOB** | Use it when a Java/Spring shop needs centrally-managed, visual, sharded scheduled jobs — mind GPL-3.0 and the central-scheduler SPOF. | B (5/6) | [→](xxl-job.md) |
| **Celery** | Use it when a Python app must offload async/background jobs at scale — at the cost of running a broker + workers. | B (5/6) | [→](celery.md) |
| **Kombu** | Use it when a Python service must publish/consume messages across swappable brokers (RabbitMQ, Redis, SQS) — virtual transports emulate AMQP imperfectly, so "swap the URL" is not identical behavior. | A (5/6) | [→](kombu.md) |
| **Flower** | Use it when a production Celery cluster needs a live dashboard to inspect and control workers and export Prometheus metrics — it can revoke tasks, so never expose it unauthenticated. | B (4/6) | [→](flower.md) |
| **RQ** | Use it when a Python app already has Redis or Valkey and needs a small, readable queue-and-worker model — accepting Redis-only transport and separate worker operations. | B (5/6) | [→](rq.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [XXL-JOB](xxl-job.md) | ✅ | B (5/6) | Use it when a Java/Spring shop needs centrally-managed, visual, sharded scheduled jobs — mind GPL-3.0 and the central-scheduler SPOF. |
| [Celery](celery.md) | ✅ | B (5/6) | Use it when a Python app must offload async/background jobs at scale — at the cost of running a broker + workers. |
| [Kombu](kombu.md) | ✅ | A (5/6) | Use it when a Python service must publish/consume messages across swappable brokers (RabbitMQ, Redis, SQS) — virtual transports emulate AMQP imperfectly, so "swap the URL" is not identical behavior. |
| [Flower](flower.md) | ✅ | B (4/6) | Use it when a production Celery cluster needs a live dashboard to inspect and control workers and export Prometheus metrics — it can revoke tasks, so never expose it unauthenticated. |
| [RQ](rq.md) | ✅ | B (5/6) | Use it when a Python app already has Redis or Valkey and needs a small, readable queue-and-worker model — accepting Redis-only transport and separate worker operations. |
| [RQ](rq.md) | ✅ | B (5/6) | Use it when a Redis/Valkey-only Python queue plus a built-in scheduler is enough — a deliberately smaller model than Celery's, so no broker choice or workflow primitives. |
| Dramatiq / arq / Quartz / PowerJob | 未收录 | — | Other task queues & schedulers named across the pages. |

## What belongs here

Systems whose primary job is **distributed background job execution** — task queues and job schedulers. Not workflow/DAG orchestrators (see `workflow-orchestration`), not agent runtimes (see `agent-frameworks`).
