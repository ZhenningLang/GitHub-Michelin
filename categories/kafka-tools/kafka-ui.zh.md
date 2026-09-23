---
name: UI for Apache Kafka (provectus/kafka-ui)
slug: kafka-ui
repo: https://github.com/provectus/kafka-ui
category: kafka-tools
tags: [kafka, web-ui, cluster-management, monitoring, schema-registry, kafka-connect]
language: Java
license: Apache-2.0
maturity: v0.7.2 (2024-04), upstream stalled — see Health, ~12.2k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2024-07-26T08:00:52Z
  default_branch: master
  default_branch_sha: 83b5a60cc08501b570a0c4d0b4cdfceb1b88d6b7
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T03:03:38Z
  overall: C
  overall_score: 1.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 897
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.0
        qualifying_issues: 8
        band: relaxed_solo
        window_offset_days: 5
        source: pr
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 94244
        release_assets: 15
        release_tier: D
        signal_basis: releases
    longevity:
      grade: E
      raw:
        repo_age_days: 2492
        last_commit_age_days: 897
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: unattributable }
---

# UI for Apache Kafka (provectus/kafka-ui)

一个免费、开源的 Web UI，用于管理和观测 Apache Kafka 集群——在浏览器里浏览 broker、topic、分区、消费组及其 lag，生产/查看消息，并接入 Schema Registry 和 Kafka Connect。**注意：** 活跃开发已转移到社区分叉 `kafbat/kafka-ui`（见健康度）。

![kafka-ui — 健康度雷达](../../assets/health/kafka-ui.zh.svg)

## 何时使用

你是运行着一个或多个 Kafka 集群的工程师或 SRE，每次有人问「这个 topic 在收消息吗？」或「这个消费组为什么有 lag？」时，你都受够了 `kafka-console-consumer.sh` 和一长串 CLI 参数。你想要一个一条 `docker run` 就能起的轻量看板，能显示 broker、topic、分区分配、消费组 lag，并且能点进某个 topic 真正*读到*消息——JSON、纯文本、Avro、Protobuf——而不必自己写个消费者。你把它指向你的 bootstrap servers（可选地再加上 Schema Registry 和一个 Connect 集群），打开 `:8080`，你的数据流对整个团队都可见了，而不只是笔记本上装了 CLI 和正确配置的那一个人。

当你需要一个自托管、零授权成本、用来替代商业版 Kafka 控制台的方案时，它也合适——带 OAuth（GitHub/GitLab/Google）、基于角色的访问控制，以及对敏感字段的数据脱敏——治理能力足以摆在团队面前而不暴露原始 PII。临时生产测试消息、手动创建/配置 topic、点几下就注册 schema，这些都帮你省掉很多控制台摩擦。

## 何时不用

- **你想要仍在维护的版本。** 这个 `provectus/kafka-ui` 仓库实际上已停滞（最后发布 v0.7.2，2024-04；最后 push 2024-07）。社区分叉 **`kafbat/kafka-ui`** 才是开发延续的地方。对新部署，优先用维护中的分叉而非这个上游——拿不再维护的软件对着持续演进的 Kafka 协议跑，是这里最大的风险。
- **你需要完整的流式控制平面。** 它是观测/管理 UI，不是 Kafka 治理/血缘/数据目录工具，也不是托管平台的控制平面。topic/ACL 即代码、大规模多租户治理、血缘，都需要专门工具。
- **超大规模多集群、且对 RBAC/审计要求很高。** 它支持多集群和 RBAC，但企业级审计轨迹、细粒度配额管理、SLA 支持，正是商业控制台（Confluent Control Center、Conduktor）的差异化所在。
- **你不走 JVM/Docker 路线。** 它是 Spring Boot 的 Java 应用，要跑 JVM（通常用官方 Docker 镜像）。若你想要极小的单二进制或桌面应用，它不是。
- **以重写入式管理为主工作流。** 它能创建 topic、生产消息，但把点击式 UI 当作你的供给事实源很脆弱——把破坏性/管理操作留在版本受控的工具里。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| kafbat/kafka-ui | 未收录 | 新部署或升级时选 kafbat/kafka-ui，因为它是维护中的延续；当前页主要用于理解停滞的 Provectus 上游和迁移风险。 | 正是本项目的**维护中社区分叉**——同一套 UI、持续发布；对新装而言通常比停滞的上游更优。 |
| Conduktor | 未收录 | 当打磨过的体验、企业治理和商业支持比完全开源自托管更重要时，选 Conduktor；当一个 OSS 浏览器 UI 已经够用时，才考虑 kafka-ui。 | 打磨精良的桌面/Web Kafka 平台；功能更丰富、有企业治理，但 freemium/商业——不是完全开源的自托管 OSS UI。 |
| Confluent Control Center | 未收录 | 当你已经在 Confluent Platform 内，且需要深度企业监控或治理时，选 Confluent Control Center；当只要更轻的独立看板时，选 kafka-ui。 | Confluent Platform 里深度的企业级监控/治理；商业且绑定该生态，比一个单容器 UI 重得多。 |
| AKHQ | 未收录 | 当你要一个 Apache-2.0 的直接 OSS Kafka Web UI 替代，且接受不同栈和 UX 时，选 AKHQ；新装时不要默认押停滞的 kafka-ui 上游，除非已证明兼容。 | 开源（Apache-2.0）的 Kafka Web UI，范围相近（topic、消费者、Connect、schema registry、ACL）；是直接的 OSS 替代，栈/UX 不同。 |
| Redpanda Console | 未收录 | 当你要基于 Go 的 Kafka/Redpanda UI，尤其在 Redpanda 环境里时，选 Redpanda Console；只有 Java/Spring 栈和现有功能面合适时，才选 kafka-ui。 | 开源 Kafka/Redpanda UI（Go）；干净、快、也能对接原生 Kafka；部分高级功能向 Redpanda 商业版倾斜。 |
| kafka-python admin CLI | 未收录 | kafka-python admin CLI 是互补项：脚本化或无头管理用它；人工浏览和团队看板用 kafka-ui。 | 是 CLI 而非 UI——可脚本化/无头管理；与看板互补而非替代。 |

## 技术栈

- **后端：** Java / Spring Boot（reactive），打包为 JAR 和官方 Docker 镜像（`provectuslabs/kafka-ui`）。
- **前端：** 由后端托管的 JavaScript/TypeScript 单页 Web UI。
- **Kafka 集成：** Kafka Admin/Consumer/Producer API、Schema Registry（Avro / JSON Schema / Protobuf）、Kafka Connect，以及可插拔 serde（自定义序列化/反序列化插件，如 AWS Glue）。
- **认证与安全：** OAuth 2.0（GitHub/GitLab/Google）、基于角色的访问控制、数据脱敏。

## 依赖

- **一个 JVM 运行时**——实际上就是官方 Docker 镜像；或自己跑 JAR。
- **一个或多个 Kafka 集群**作为指向目标（bootstrap servers）——这是它存在的全部理由。
- **可选集成：** Schema Registry、Kafka Connect 集群、用于 SSO 的 OAuth 身份提供方。动态配置需 `DYNAMIC_CONFIG_ENABLED=true`。
- **基础单集群场景不需要它自己的数据库**——它实时读取集群状态；配置通过 env/YAML。[推断]

## 运维难度

**低到中。** 演示路径确实一条命令（`docker run -p 8080:8080 -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui`）。真正使用时你要写一份配置（YAML/env），列出集群、schema registry、Connect 端点和认证——直接但会随集群数量和 RBAC 矩阵增长。在大 topic 上重度浏览消息时，JVM 内存调优很重要。更大、常被忽视的成本是**停留在不再维护的上游**：出于安全和 Kafka 版本修复，你大概率会想迁到 `kafbat/kafka-ui` 分叉，所以把一次迁移纳入运维计划，而不是永远 pin 在这个仓库上。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）——上游停滞。** `provectus/kafka-ui` 最后发布 v0.7.2 在 **2024-04**，最后 push 在 **2024-07**；截至撰写已约 2 年没有发布。API 并**未**把它标记为 `archived`，但它读起来是**休眠**而非活跃。活跃开发在社区分叉 **`kafbat/kafka-ui`** 中延续（2026-06 有 push）。这是主导结论：把上游当作冻结。[推断]
- **治理 / 背书。** `Organization` 所有（Provectus，一家咨询公司）；README 声称保持免费/开源、无付费档。但一个由单一厂商策划的 OSS 项目在厂商停更后，正是那种已经上演的 bus-factor 情形——社区不得不分叉来续命。[推断]
- **年龄 × Lindy。** 2019-11 创建（约 6–7 年）。年龄中等，但*上游的* Lindy 被维护停摆削弱——老而停滞过不了「仍活跃」这一关。把 Lindy 往前延续的是**分叉**，不是这个仓库。[推断]
- **采用度。** 历史采用度强（约 12.2k star、约 1.4k fork、大量 Docker 拉取历史）——代码库久经验证、部署广泛；问题在于后续维护，而非它能不能用。[未验证]
- **风险标记。** 拿实际上无人维护的软件对着演进中的 Kafka 协议（新 broker 版本、CVE）跑是首要风险；缓解办法是迁到维护中的分叉。Apache-2.0，未发现 relicense 历史。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 12.2k star / 346 open issue / 最后 push 2024-07 / 最后发布 v0.7.2（2024-04）——易变，请重新核实。
- [推断]「上游休眠、开发已转移到 kafbat/kafka-ui」由两个仓库的发布/push 时间推断（kafbat 在 2026-06 有 push，约 2.5k star）加上广为人知的社区分叉；上游并未被 API 标记为 `archived`。
- [推断]「基础场景不需要自己的数据库」由其实时读取架构推断，未对每种部署模式核实（某些功能可能需要额外存储）。
- [未验证] provectus 上游与 kafbat 分叉之间当前确切的功能对等和配置差异这里未核实——迁移前请对照分叉文档确认。
