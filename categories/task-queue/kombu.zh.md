---
name: Kombu
slug: kombu
repo: https://github.com/celery/kombu
category: task-queue
tags: [messaging, amqp, rabbitmq, redis, sqs, python, transport, broker-abstraction]
language: Python
license: BSD-3-Clause
maturity: v5.6.2, active (2026-09), ~3.1k stars
last_verified: 2026-09-28
type: library
upstream:
  pushed_at: 2026-09-28T04:30:32Z
  default_branch: main
  default_branch_sha: 09f26b00c0fbe40da2d111eae17344f07126e7a9
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T09:04:32Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 267.4
        qualifying_issues: 10
        band: default
        window_offset_days: 3
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: kombu
        dependent_repos_count: 26706
        downloads_last_month: 43453410
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5941
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 19
        top1_share: 0.787
        top3_share: 0.836
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-3-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Kombu

一个 Python 消息库，用一套地道的高层 API 统一封装多种消息 broker——AMQP/RabbitMQ，外加可插拔的“虚拟”传输（Redis、Amazon SQS、MongoDB、ZooKeeper、内存）——它正是 Celery 所构建于其上的传输层。

![kombu — 健康度雷达](../../assets/health/kombu.zh.svg)

## 何时使用

你是后端工程师，要写一个需要发布和消费消息的 Python 服务，又不想把 AMQP 的线协议细节写死、也不想把代码绑死在某一个 broker 上。今天你用 RabbitMQ，但运维在讨论换成 Redis 或 Amazon SQS，你可不想到时候把生产者和消费者全部重写。你引入 Kombu，把 exchange/queue 声明成 Python 对象，针对它的高层 API 写 `Producer`/`Consumer`。同一份代码只要换个连接 URL 就能跑在 `amqp://`、`redis://` 或 `sqs://` 上，因为 Kombu 把每个 broker 藏在统一的传输接口后面，并替你处理那些本来要自己重造的消息管道——连接池、自动重连、序列化（JSON/pickle/msgpack/YAML）与压缩。

当你要做的是框架级基础设施而非应用本身时，你也会选 Kombu：一个任务队列、一条事件总线，或一个需要精细控制 ack、prefetch 和 consumer mixin 的 worker 池。它正是 Celery 自身使用的底座，所以如果你已经超出 Celery 任务抽象的范围、但仍想要一个久经考验的 broker 层，Kombu 就是可以直接在其上构建的更底层原语。

## 怎么用起来

Kombu 是客户端库而不是服务——它待在你的进程里，替你跟 broker 的协议打交道。你把 AMQP 形状的那几件东西（*exchange*：负责给消息路由的邮局；*queue*：消费者读取的信箱）声明成普通 Python 对象，然后用一个 URL 开出一条 `Connection`。发布走 `Producer`：它把载荷序列化（JSON/pickle/msgpack/YAML），经带连接池、会自动重连的连接交给 exchange。消费走 `Consumer` 加 `conn.drain_events()` 事件循环（在 socket 上等下一条消息），消息被派发给你的回调，直到你调用 `message.ack()` 告诉 broker 这次投递已了结。诀窍在**传输层**：对 RabbitMQ 它经 py-amqp 说真正的 AMQP；对 Redis、SQS、MongoDB 之类，则由「虚拟传输」用后端自己的原语模拟这套语义——所以可移植性在 API 层，不在保证层。留在你手上的事：自己运维 broker，以及按传输层把 ack/可见性超时/prefetch 调对。

![Kombu — 主干用户故事](../../assets/flow/kombu.zh.svg)

<!-- flow-steps:begin (generated from flows/kombu.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：把 Kombu 装进你的 Python 服务 — `pip install kombu` — 组件：`应用环境`
2. **你**：用对象声明 exchange/queue，按 URL 开连接 — `with Connection('amqp://guest:guest@localhost//') as conn:`
3. **Kombu**：同一传输接口管尽 amqp、redis、SQS 数种后端 — 组件：`传输层`
4. **你**：经 Producer 发布消息，随消息声明队列 — `producer = conn.Producer(serializer='json')`
5. **Kombu**：序列化载荷并路由到绑定的队列
6. **你**：用回调列表加事件循环来消费 — `conn.drain_events()` — 组件：`Consumer`
7. **Kombu**：把每条消息派发给你的回调，由 message.ack() 确认

**价值**：一套生产/消费 API 横跨 AMQP、Redis、SQS 等——换 broker 只是换 URL，不是重写

</details>
<!-- flow-steps:end -->

## 何时不用

- **你只是想跑后台任务。** 如果你的目标是“稍后调用某个函数，带重试和 worker 池”，请直接用 [Celery](celery.zh.md)（它就架在 Kombu 之上），而不是手工接生产者/消费者。Kombu 是管道，不是任务框架。
- **你不在 Python 上。** Kombu 只支持 Python。要做跨语言消息，请用 broker 的原生客户端或跨语言协议（裸 AMQP、Kafka、NATS）。
- **你想要完整的事件流平台。** Kombu 是 broker 的*客户端/抽象*，不是日志结构化的流存储。要做高吞吐、可重放、带 consumer-group 语义的事件流，Kafka/Redpanda/Pulsar 才是对的层级。
- **你需要每个 broker 行为完全一致。** 虚拟传输（Redis、SQS……）对 AMQP 语义的模拟并不完美——exchange 类型、优先级、投递保证等特性因后端而异。可移植性是“换 URL”，不是“行为一致”。[推断]
- **你想要一等公民的 async/await。** Kombu 的核心消费模型是 Celery 风格的同步/事件循环驱动；若你的技术栈围绕 `asyncio`，async 原生的 AMQP 客户端（如 `aio-pika`）可能更合适。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Celery](celery.zh.md) | ✅ | 需要架在 Kombu *之上*的任务队列，而不是裸 broker 抽象时，选 Celery。 | “跑某个 job”用 Celery；需要传输层 broker 抽象时用 Kombu。不是替代品，而是更高一层。 |
| py-amqp / pika | 未收录 | 需要更底层的纯 AMQP 客户端时，选 py-amqp 或 pika。 | 抽象更少、无多 broker 可移植性，但若你只会用 RabbitMQ，活动部件更少。 |
| aio-pika | 未收录 | 需要面向 `asyncio` 的 async 原生 AMQP 客户端时，选 aio-pika。 | async 体验更好，仅支持 RabbitMQ，范围比 Kombu 的多传输模型窄。 |
| confluent-kafka-python / [kafka-python](../kafka-tools/kafka-python.zh.md) | 部分已收录 | 需要日志结构化流而不是 broker 抽象时，选 Kafka 客户端。 | 语义不同：重放、分区、consumer group。confluent-kafka-python 未单独收录。 |
| NATS / Redis Streams（直连） | 未收录 | 已认定某一个 broker 或 stream 系统时，选直连客户端。 | 单系统下更简单，但没有 broker 无关层。 |

## 技术栈

- **语言：** Python——已发布的 5.6.x 要求 Python ≥3.9；5.7 线（2026-09 起 alpha）升到 ≥3.10，分类器覆盖到 3.14。纯 Python 库。
- **核心抽象：** 可插拔的**传输**接口——一个真正的 AMQP 传输（经 `py-amqp` 或 `qpid`），外加在其它后端上模拟 AMQP 语义的「虚拟」传输。
- **内置传输：** Redis、Amazon SQS、MongoDB、ZooKeeper、Pyro、SoftLayer MQ，以及用于单测的内存传输；PGMQ 出现在 5.7（main）线的 README 内置清单里。已发布的 5.6.2 还带 Google Cloud Pub/Sub、Confluent Kafka、Azure Storage Queues / Service Bus、Consul 等 extra；SQS 的 fan-out 经 AWS SNS 在一个选项后实现。
- **序列化与封装：** 可插拔 serializer（JSON、pickle、msgpack、YAML）与压缩；连接池和自动故障切换/重连。

## 依赖

- **运行时：** Python 加上一个传输驱动——RabbitMQ 用 `amqp`（py-amqp）、Redis 传输用 `redis`、Amazon SQS 用 `boto3`/SQS 相关依赖等。你只需安装所用 broker 对应的 extra。
- **一个运行中的 broker（你自己运维）：** 视传输而定的 RabbitMQ、Redis、SQS 账号、MongoDB 或 ZooKeeper。Kombu 是客户端，不负责跑 broker。
- **安装：** 从 PyPI `pip install kombu`；按 broker 装 extra，如 `kombu[redis]` / `kombu[sqs]`。

## 运维难度

**库本身很低；真正的运维是 broker。** Kombu 自身不引入任何服务——它只是你进程里的一个 `pip` 依赖，所以 Kombu 本身没有额外要部署或监控的东西。运维分量全在你指向的那个 **broker**：运行并集群化 RabbitMQ、给 Redis 调容量并权衡它较弱的投递保证，或管理 SQS 的配额与可见性超时。库层面的关注点是把 prefetch/ack/heartbeat 调对，以免在故障下丢消息或重复消费，并清楚每个虚拟传输各有怪癖。如果你已经在跑 Celery，你其实已经在跑 Kombu 和它的 broker——运维面是同一片。

## 健康度与可持续性

- **响应速度**：Grade C——中位首次响应 267.4 小时，基于 10 个 qualifying issues/PRs。
- **维护（2026-09）。** 默认分支保持每日提交流（最后 push 2026-09-28）；最新稳定版 v5.6.2（2025-12），v5.7.0a1 预发布版于 2026-09 放出——发版比提交慢，但项目**活跃**，不是吃老本。未归档。
- **治理 / bus factor。** 归于 **celery** GitHub 组织，有多名长期维护者（ask、auvipy、thedrow、matusvalo 等），而非单人项目——bus factor 比独立 solo 仓库健康，尽管仍是社区运营而非基金会治理。[推断]
- **年龄与 Lindy 判断。** 2010-06 创建（GitHub `created_at`），约 16 年，且**仍在活跃发布**⇒ **强 Lindy** 信号；它做 Celery 底下的 broker 层已逾十年。
- **采用度。** 凡用 Celery 处几乎必然用到它（Celery 依赖它），因此其传递采用度远超约 3.1k 的直接 star（2026-09）；每月 43,453,410 次 PyPI 下载。Read the Docs 上文档成熟。
- **风险标记。** BSD-3-Clause，未发现 relicense 历史；主要考量是虚拟传输与真实 AMQP 的语义对齐并不完美，且随版本变动。

## 存疑（未验证）

- [未验证] 2026-09-28 从 GitHub/PyPI API 读到的约 3.1k star、稳定版 v5.6.2（2025-12）与 v5.7.0a1 预发布版；star/版本号对时间敏感，仅供参考。
- [未验证] Python 版本下限随产品线移动（5.6.x 为 3.9，5.7 开发线为 3.10），broker extra 的确切集合也随版本变化——固定依赖前请查当前 `setup.py`/PyPI 元数据。
- [推断] 虚拟传输（Redis、SQS、MongoDB……）对 AMQP 语义的模拟存在后端相关缺口；“换 URL”的可移植性并不等于跨 broker 行为一致。
- [未验证] 相对 async 原生 AMQP 客户端，其 async/await 体验有限；核心模型沿用 Celery 的事件循环/同步风格。
