# task-queue

> 分类节点。分布式后台任务执行——任务队列与作业调度器。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **XXL-JOB** | 当 Java/Spring 团队需要中心化、可视化、分片的定时作业调度时用它——注意 GPL-3.0 与中心调度器单点。 | B（5/6） | [→](xxl-job.zh.md) |
| **Celery** | 当 Python 应用需要把异步/后台任务规模化外包时用它——代价是要跑 broker + worker。 | B（5/6） | [→](celery.zh.md) |
| **Kombu** | 当 Python 服务要在可替换 broker（RabbitMQ、Redis、SQS）间收发消息时用它——虚拟 transport 对 AMQP 的模拟并不完整，换 URL 不等于行为一致。 | A（5/6） | [→](kombu.zh.md) |
| **Flower** | 当生产 Celery 集群需要实时面板查看、控制 worker 并导出 Prometheus 指标时用它——它能撤销任务，绝不能无鉴权暴露。 | B（4/6） | [→](flower.zh.md) |
| **RQ** | 当 Python 应用已有 Redis 或 Valkey，并需要小而易读的队列加 worker 模型时用它——接受仅 Redis 系传输和另行运维 worker。 | B（5/6） | [→](rq.zh.md) |
| **Dramatiq** | 当 Python 服务想要 actor 式后台处理、并真的能在 RabbitMQ 与 Redis 之间选时用它——前提是能接受 LGPL-3.0 的分发义务。 | B（6/6） | [→](dramatiq.zh.md) |
| **arq** | 当应用已经 asyncio-first、一个小的 Redis 协程队列就够时用它——README 自称 maintenance-only，因此按「稳定但不再演进」预期。 | B（6/6） | [→](arq.zh.md) |
| **PowerJob** | 当 JVM 团队需要带 Web 控制台、支持 DAG 与 map-reduce 的集中式调度/计算平台时用它——稳定版自 2025-08 起未再发版。 | C（4/6） | [→](powerjob.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [XXL-JOB](xxl-job.zh.md) | ✅ | B（5/6） | 当 Java/Spring 团队需要中心化、可视化、分片的定时作业调度时用它——注意 GPL-3.0 与中心调度器单点。 |
| [Celery](celery.zh.md) | ✅ | B（5/6） | 当 Python 应用需要把异步/后台任务规模化外包时用它——代价是要跑 broker + worker。 |
| [Kombu](kombu.zh.md) | ✅ | A（5/6） | 当 Python 服务要在可替换 broker（RabbitMQ、Redis、SQS）间收发消息时用它——虚拟 transport 对 AMQP 的模拟并不完整，换 URL 不等于行为一致。 |
| [Flower](flower.zh.md) | ✅ | B（4/6） | 当生产 Celery 集群需要实时面板查看、控制 worker 并导出 Prometheus 指标时用它——它能撤销任务，绝不能无鉴权暴露。 |
| [RQ](rq.zh.md) | ✅ | B（5/6） | 当 Python 应用已有 Redis 或 Valkey，并需要小而易读的队列加 worker 模型时用它——接受仅 Redis 系传输和另行运维 worker。 |
| [RQ](rq.zh.md) | ✅ | B（5/6） | 只依赖 Redis/Valkey、自带调度器就够用时选它——是刻意做小的模型，没有 Celery 那种 broker 选择与工作流原语。 |
| [Dramatiq](dramatiq.zh.md) | ✅ | B（6/6） | 以 actor 为中心的 Python 任务处理，真的能在 RabbitMQ 与 Redis 之间选，还带中间件；LGPL-3.0 决定了你能怎么分发它。 |
| [arq](arq.zh.md) | ✅ | B（6/6） | asyncio-native 的 Redis 队列，面向协程作业；README 自称 maintenance-only，因此按「稳定但不再演进」对待。 |
| [PowerJob](powerjob.zh.md) | ✅ | C（4/6） | Java 分布式调度/计算平台，带中央控制台、DAG 与 map-reduce 执行；稳定版自 2025-08 起未再发版。 |
| Quartz | 未收录 | — | 各页点到的 Java Quartz Scheduler。（按名字搜索命中的是 jackyzha0/quartz——一个静态站点生成器；要收录得先人工把仓库认准。） |

## 什么该放这里

主要职责是**分布式后台任务执行**的系统——任务队列与作业调度器。不含工作流/DAG 编排器（见 `workflow-orchestration`），不含 agent 运行时（见 `agent-frameworks`）。
