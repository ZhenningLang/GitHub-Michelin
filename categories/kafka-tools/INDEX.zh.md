# kafka-tools

> 分类节点。Apache Kafka 客户端与管理界面。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **UI for Apache Kafka (provectus/kafka-ui)** | 当你想一条 docker run 起一个浏览器面板，看 Kafka broker、topic、消费组 lag 和消息内容时用它——但 provectus 上游自 2024-04 起再无发布，新部署请改用仍在维护的 kafbat/kafka-ui 分叉。 | C（5/6） | [→](kafka-ui.zh.md) |
| **kafka-python** | 当你想要一个纯 Python、pip install 即装、无需编译 librdkafka 的 Kafka 客户端时用它——但纯 Python 客户端的吞吐追不上 confluent-kafka，且对最新 broker 特性可能滞后支持。 | A（6/6） | [→](kafka-python.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [UI for Apache Kafka (provectus/kafka-ui)](kafka-ui.zh.md) | ✅ | C（5/6） | 换来免费、轻量、能接 Schema Registry 与 Connect 的管理观测界面；代价是停摆的代码要面对持续演进的 Kafka 协议，也没有治理与血缘能力。 |
| [kafka-python](kafka-python.zh.md) | ✅ | A（6/6） | 当你想要一个纯 Python、pip install 即装、无需编译 librdkafka 的 Kafka 客户端时用它——但纯 Python 客户端的吞吐追不上 confluent-kafka，且对最新 broker 特性可能滞后支持。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向 **Apache Kafka** 的客户端与管理界面。通用消息库可能在 `task-queue`。
