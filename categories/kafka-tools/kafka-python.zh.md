---
name: kafka-python
slug: kafka-python
repo: https://github.com/dpkp/kafka-python
category: kafka-tools
tags: [kafka, python, client, producer, consumer, admin, pure-python]
language: Python
license: Apache-2.0
maturity: v3.0.6 (2026-06), active, ~5.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-28T22:11:41Z
  default_branch: master
  default_branch_sha: a5da13adece530043e3a789cd27ba6bb088b3317
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:24:25Z
  overall: A
  overall_score: 3.5
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
        last_commit_age_days: 19
        active_weeks_13: 8
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.9
        qualifying_issues: 14
        band: default
        window_offset_days: 8
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: kafka-python
        dependent_repos_count: 3616
        downloads_last_month: 17551522
        graph_tier: B
        volume_tier: A
        cross_check_divergence: null
        release_downloads: 1864
        release_assets: 4
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5111
        last_commit_age_days: 19
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 10
        top1_share: 0.968
        top3_share: 0.985
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# kafka-python

一个纯 Python 的 Apache Kafka 客户端库——高层的 `KafkaConsumer`、`KafkaProducer`、`KafkaAdminClient` 类外加 CLI 脚本，没有 C/Cython/Rust 内核，所以在各种环境里安装都很简单。

![kafka-python — 健康度雷达](../../assets/health/kafka-python.zh.svg)

## 何时使用

你是 Python 开发者，需要在应用、数据管道或脚本里读写 Kafka，并且希望它*装上就能用*——不用编译 librdkafka、不用系统包、不用在笔记本、CI 和精简容器之间折腾 wheel 匹配。你 `pip install kafka-python`，import `KafkaConsumer('my_topic')`，把消息当 namedtuple 迭代；生产就是 `KafkaProducer().send(...)`。因为是纯 Python，它能干净地落进 PyPy、受限环境和那些「编译原生扩展很痛」的极简 Docker 镜像里。API 设计上对齐官方 Java 客户端，所以消费组、动态分区分配、offset 提交都如你所料。

当你想在机器上不带 JVM 做轻量管理时它也合适：`kafka-python admin -b localhost:9092 cluster describe`（或 `python -m kafka.admin`）替代了一部分 Kafka `bin/*.sh` 脚本，用于创建 topic、描述集群和快速交互——在手头没有兼容 JVM 的环境里很方便。要追求原始吞吐，你可以 `pip install crc32c` 把校验和卸载给一个优化过的 C 库，而不必把它变成硬依赖。

## 何时不用

- **追求极致吞吐 / 最低延迟。** 纯 Python 客户端比不过 `librdkafka` 加持的 `confluent-kafka-python` 在高量生产/消费上的表现。若你在打满链路或计较微秒，用原生客户端。
- **你要第一天就用上最新 broker 特性。** 协议/KIP 支持是用 Python 实现的，可能落后于最新 Kafka 版本；依赖某个全新特性前请核实你需要的 KIP/broker 版本是否已支持。[未验证]
- **以 async 为原生的代码库。** 公开 API 是同步/迭代器式的。3.x 内部转向了 async 事件循环，但若你想要一等公民的 `asyncio` API，`aiokafka` 是专为此打造的。
- **你已经在用 Confluent 全家桶。** 若你标准化在 Confluent Platform/Schema Registry 工具链上，`confluent-kafka-python` 与该生态（序列化器、registry 客户端）集成更紧。
- **重度流处理。** 它是客户端，不是流处理框架——没有 Kafka Streams 的等价物。要做有状态拓扑请用 Faust/Quix/ksqlDB 或 JVM 的 Streams API。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| confluent-kafka-python | 未收录 | 当吞吐、延迟、Confluent 生态集成或最快协议覆盖最重要时，选 confluent-kafka-python；当纯 Python 可移植性和安装简单才是硬约束时，选 kafka-python。 | 官方 Confluent 客户端，封装 `librdkafka`（C）——吞吐/延迟最佳、协议覆盖最快，但需要原生库，可移植性不如纯 Python 那么轻易。 |
| aiokafka | 未收录 | 当 async 优先的 Python 服务需要原生 `asyncio` API 时，选 aiokafka；当需求是同步消费者、生产者和管理脚本时，选 kafka-python。 | 原生 `asyncio` Kafka 客户端（脱胎于 kafka-python 一脉）；async 优先应用的正确选择，面比同步客户端窄。 |
| [kafka-ui](kafka-ui.zh.md) | ✅ | kafka-ui 是互补项：人要浏览和管理集群时选它；要嵌入 Python 生产者、消费者或脚本时，仍选 kafka-python。 | 是集群管理的 Web UI，而非客户端库——互补而非竞争；完全不同的活。 |
| Java/Scala 官方客户端 | 未收录 | 当服务在 JVM 上、需要参考客户端行为或 Kafka Streams 时，选 Java/Scala 官方客户端；当应用边界是 Python 且不能接受 JVM 客户端时，选 kafka-python。 | 参考实现，特性一等支持且带 Kafka Streams，但仅限 JVM——对 Python 服务不是选项。 |
| Sarama（Go） | 未收录 | 当 Go 服务需要成熟、无原生依赖的 Kafka 客户端时，选 Sarama；当你要在 Python 里获得同类可移植性取舍时，选 kafka-python。 | 成熟的纯 Go Kafka 客户端；同样「无原生依赖」的卖点，但面向 Go 而非 Python。 |

## 技术栈

- **语言：** 纯 Python，无 Cython/C/Rust 内核（核心可移植性卖点）；3.x 线要求 Python 3.8+。
- **组件：** `KafkaConsumer`、`KafkaProducer`、`KafkaAdminClient`，外加 `kafka-python`/`python -m kafka.*` CLI 入口。
- **3.0 内部：** 协议栈由 Apache Kafka 的 JSON 消息 schema 动态生成；网络层围绕事件循环、内部用 async/await 重构；通过编译/缓存 bytecode 做编解码优化（据 README「What's New in 3.0」）。
- **可选原生加速：** `crc32c` C 库加速校验和；压缩编解码（gzip/snappy/lz4/zstd）视你启用情况可能拉入可选库。

## 依赖

- **一个可达的 Kafka 集群**——宣称的 broker 兼容大致覆盖 Kafka 0.8 → 4.x 范围（见项目兼容性页）。[未验证]
- **核心安装：无**——纯 Python，基础场景无外部运行时依赖。
- **可选：** `crc32c`（吞吐）、压缩库（snappy/lz4/zstd，若用到这些编解码），以及视你的认证而定的 SASL/SSL 安全库。[未验证]
- **Python 3.8+** 用于当前大版本。

## 运维难度

**低。** 它是库而非服务——`pip install` 即完事；除了你自己的应用，没东西要部署或运维。「无原生依赖」的设计本身就是*运维*红利：CI 和精简容器里可重现安装、无需构建工具链，还能跑在 PyPy/受限主机上。你确实要承担的运维现实是 Kafka 客户端调优——批量、`acks`、重试、消费组再平衡、offset 提交语义——这是任何 Kafka 客户端固有的，并非本库特有。难跑的是你连的那个集群，而不是客户端。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 1.9 小时，基于 14 个 qualifying issues/PRs。
- **维护（2026-06）——活跃。** 发布很勤：v3.0.6 在 **2026-06-25**，同一周内还有数个补丁版本，最后 push 在 **2026-06-27**。3.0 线是一次大重构（协议生成、async 内部）。明显**活跃**而非吃老本。未归档。[推断]
- **治理 / bus factor。** `User` 所有（Dana Powers，`dpkp`）——名义上单一所有者，但是一个长期的**多贡献者**项目（jeffwidman、mumrah、wizzat 等都在头部贡献者里），所以 bus factor 好于典型的单人仓库。不过没有基金会背书——方向系于一个小核心团队。[推断]
- **年龄 × Lindy。** 2012-09 创建（约 14 年）且*仍在活跃发大版本* ⇒ **强 Lindy** 信号：最老、最久经验证的 Python Kafka 客户端之一，而非新秀。老而活跃是好象限。[推断]
- **采用度。** 历史上使用广泛（约 5.9k star、约 1.5k fork，PyPI 上随处可见）；极低的 open issue 数（约 15）配上频繁发布，提示一种盯得紧、跟得上的维护姿态。[未验证]
- **风险标记。** 主要考量是相对原生客户端的*性能上限*和相对最新 broker 特性的*协议滞后*——是能力边界，而非健康红旗。Apache-2.0，未发现 relicense 历史。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 5.9k star / 约 15 open issue / v3.0.6（2026-06-25）/ 最后 push 2026-06-27——易变，请重新核实。
- [未验证] 宣称的 broker 兼容范围（Kafka 0.8 → 约 4.x）和确切 KIP 覆盖来自 README/文档；依赖前请对照兼容性页确认你需要的具体 KIP/broker 版本。
- [未验证] 可选压缩/安全依赖细节（snappy/lz4/zstd、SASL/SSL 库）由典型 Kafka 客户端需求推断，未从清单逐一列出。
- [推断]「好于单人的 bus factor」由贡献者列表推断，而非治理文档；它仍是 `User` 所有的仓库、核心团队不大。
- [推断] async/await 内部与一等 asyncio API 之间的区分（async 优先应用更适合 aiokafka）由 3.0 说明和生态推断，未通过阅读此处公开 API 面来核实。
