---
name: Kong Gateway
slug: kong
repo: https://github.com/Kong/kong
category: api-gateway
tags: [api-gateway, ai-gateway, llm-gateway, reverse-proxy, plugins, kubernetes-ingress, openresty]
language: Lua
license: Apache-2.0
maturity: v3.9.x, active (2026-06)
last_verified: 2026-06-26
type: service
upstream:
  pushed_at: 2026-06-29T09:48:26Z
  default_branch: master
  default_branch_sha: 1730282ec2f8ed097cf6ad6a3d69e55b7ba9ebb6
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:14:24Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 5
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 26.0
        qualifying_issues: 5
        band: default
        window_offset_days: 5
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 4245
        last_commit_age_days: 2
        cohort: service
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 17
        top1_share: 0.158
        top3_share: 0.395
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: no_package_structural }
---

# Kong Gateway

基于 OpenResty/Nginx 的 API 网关，靠插件层把一个反向代理变成可编程的流量边界：既管 REST/微服务流量，也从 3.x 起通过 AI Gateway 插件管 LLM 与 MCP 流量。

![kong — 健康度雷达](../../assets/health/kong.zh.svg)

## 何时使用

你是某公司的平台工程师，手里跑着几十个内部微服务，每个团队各写一套鉴权、限流、日志代码，互相复制粘贴，散落到处都是。你想把这些横切关注点从应用里抽出来，集中到一个可配置的边界上。于是你在服务前面架起 Kong，把每个上游声明为 Service + Route，再按需打开插件——`key-auth` 或 `jwt` 做鉴权、`rate-limiting` 限流、`prometheus` 出指标、`request-transformer` 改写报文——全程不用重新部署任何后端。配置要么放在 PostgreSQL（走 Admin API / Kong Manager），要么以一份声明式 YAML 存在 DB-less 模式里、提交进 git、用 decK 下发，于是网关行为可评审、可复现。

更新的理由是 AI Gateway 这条路。你的团队正从应用代码里直接调 OpenAI、Anthropic、Bedrock、Gemini，却没有一个集中处去管 key、限流、成本、prompt 日志或语义缓存。`ai-proxy` 系列插件给你一个 OpenAI 兼容的端点，向后扇出到多家 LLM 供应商，再加上 MCP 流量治理——让你能把当年给 HTTP API 装的那套策略边界，照样装到 LLM/agent 流量前面，复用你已经在跑的插件和可观测性机制。

## 怎么用起来

Kong 是站在你所有后端服务前面的一道门。**门本身和一整套现成插件（鉴权、限流、指标、改写请求）都是 Kong 自带的**——你不写处理逻辑，只**声明**「哪条路由转给哪个后端、挂哪些插件、参数是多少」。请求进门后，Kong 按顺序把这条路由上的插件跑一遍，全部放行才转给后端，任一插件不放行就直接拒绝。这些声明要么存进 PostgreSQL（通过 Admin API 改），要么写成一份 YAML 放进 git（DB-less 模式）。只有现成插件不够用时，你才需要自己写插件。

![kong — 主干用户故事](../../assets/flow/kong.zh.svg)

<!-- flow-steps:begin (generated from flows/kong.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：部署 Kong，放在所有后端服务前面 — `docker-compose --profile database up`
2. **你**：声明 Service + Route：哪条路径转给哪个后端 — `Admin API :8001 or decK YAML`
3. **你**：给路由挂上现成插件，填参数 — `key-auth · rate-limiting · prometheus`
4. **Kong Gateway**：请求从 :8000 进门，匹配到路由
5. **Kong Gateway**：按顺序跑这条路由上的插件，任一不放行就直接拒绝
6. **Kong Gateway**：全部放行后转发给后端，同时记下指标

**价值**：鉴权、限流、监控在门口统一做掉，后端服务不用各写一份

</details>
<!-- flow-steps:end -->

## 何时不用

- **你想要一个无外部依赖的自包含单二进制。** Kong 传统模式需要 PostgreSQL；就算 DB-less 模式也要跑整套 OpenResty。如果你不需要 Kong 的插件广度，Go 系网关（Tyk、Traefik）或纯配置文件代理运维起来更轻。
- **你要在开源版里拿到最全插件集或热加载配置。** Kong OSS 版内置插件比企业版少；Developer Portal、RBAC 和不少高级插件是企业版专属。[推断] Apache APISIX 的 OSS 版自带更多插件，并借 etcd 做动态插件热加载。
- **你已经押注 service mesh / xDS 数据面。** 如果你已统一到 Envoy + 控制面（Istio、Gateway API），再在旁边塞一个 Kong 等于重复了代理层。
- **你想用主流语言一等公民地写代理逻辑。** 核心插件是跑在 LuaJIT 上的 Lua；Go/JS 插件通过 PDK 在进程外运行，带额外开销和运维零件。
- **你只有寥寥几条路由、没有策略需求。** 此时网关纯属无差别的重活——一个反向代理（Nginx、Caddy、Traefik）或你框架自带的路由就够了。
- **你以为 Cassandra 还是个选项。** 作为配置存储的 Cassandra 已在 3.4 这条线移除；如今只有 PostgreSQL 或 DB-less。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Apache APISIX | 未收录 | 当 etcd 配置、无状态节点、快速动态热加载和更广的 OSS 插件包更重要时，选 APISIX；当商业生态和门户体系更重要时，选 Kong。 | 同样是 OpenResty/Lua，但用 etcd 配置（节点无状态、动态热加载快），OSS 自带插件更多；商业/门户生态不如 Kong。 |
| Tyk | 未收录 | 当你优先要 Go 网关、开源 dashboard、开发者门户和多租户时，选 Tyk；当更看重插件深度和 OpenResty/Lua 扩展性时，选 Kong。 | Go 实现，开源栈自带 dashboard + 开发者门户 + 多租户；原始代理吞吐和插件数量比 Kong 窄。 |
| [Envoy](envoy.zh.md) | ✅ | 当你需要 xDS 数据面或 service mesh 代理时，选 Envoy；当你要开箱即用的 API 管理和 AI 网关插件，而不是自建控制面时，选 Kong。 | CNCF 毕业的 C++ L4/L7 代理，是事实上的 service mesh 数据面（xDS）；层级低得多——你得自带控制面，而非开箱即用的 API 管理插件。 |
| Traefik | 未收录 | 当 Kubernetes/容器自动发现和轻量文件/CRD 配置胜过插件广度时，选 Traefik；当你要更重的可编程策略网关时，选 Kong。 | Go 反向代理，容器/Kubernetes 自动发现强、配置走文件/CRD；跑起来更轻，但策略/AI 网关插件叙事更薄。 |
| KrakenD | 未收录 | 当你要单配置文件声明的无状态 API 聚合时，选 KrakenD；当边界层需要插件生态、Admin API 和更丰富运行时策略时，选 Kong。 | 无状态 Go 网关，聚焦单配置文件声明的 API 聚合/编排；无数据库，但不是插件丰富的可编程边界。 |
| [LiteLLM](litellm.zh.md) | 已收录 | 当所有流量只是模型供应商路由和模型策略时，选专用 LLM 代理；当 LLM 路由要和更广的 HTTP/API 策略共用同一网关时，选 Kong。 | 专门做 LLM 流量的多供应商路由，只覆盖 LLM 这一段；比 Kong 的 HTTP+AI 双网关窄，但若你只要 LLM 路由则更轻。 |
| Portkey Gateway | 未收录 | 想要把 guardrails 与可观测做成一等能力的 LLM 网关时，选 Portkey；同一边界还要承载通用 HTTP/API 策略时，选 Kong。 | Portkey 是 LLM 原生网关，open-core 姿态不同；Kong 是通用数据面网关，没有原生 token 计费。 |

## 技术栈

- **核心：** OpenResty（Nginx + LuaJIT）；代理与插件运行时是 Lua。
- **插件：** Lua 插件进程内运行；Go 与 JS/TS 插件通过 Plugin Development Kit（PDK）进程外运行。
- **配置存储：** PostgreSQL（传统/混合模式）**或** DB-less 声明式 YAML/JSON（内存态）。
- **控制面：** RESTful Admin API、Kong Manager Web UI，以及做声明式 GitOps 式配置的 decK。
- **AI Gateway：** `ai-proxy` / `ai-*` 插件，在多家 LLM 供应商（OpenAI、Anthropic、Bedrock、Gemini、Azure、Mistral 等）之上提供 OpenAI 兼容门面，并处理 MCP 流量。
- **部署模式：** 传统（带库）、混合（控制面/数据面分离）、DB-less，以及面向 Kubernetes 的 Kong Ingress Controller。

## 依赖

- **运行时：** OpenResty/Nginx + LuaJIT 栈（官方包/镜像已打包）。
- **数据存储：** 传统/混合模式需 PostgreSQL；DB-less 模式**无**（仅声明式文件）。
- **默认端口：** 8000（代理）、8001（Admin API）、8002（Kong Manager UI）。[未验证] 默认端口集合随版本/配置可能不同。
- **工具：** 声明式配置管理用 `decK`；Kubernetes 用 Kong Ingress Controller（独立仓库）。
- **安装：** 官方 Docker 镜像、Linux 包（deb/rpm）、Helm chart，或从源码构建。

## 运维难度

**中等。** DB-less 模式加 Docker 镜像是很容易的单节点起步，声明式文件也对 git 友好。难度随以下情况上升：PostgreSQL 集群（库的高可用、升级时的迁移）、混合控制面/数据面拓扑、跨版本升级的插件版本/兼容性管理，以及高负载下对 OpenResty/Nginx 层的调优。Kong Ingress Controller 又引入 Kubernetes CRD 与生命周期的关注点。在生产里跑 Lua 自定义插件本身就是一项专门技能。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 26.0 小时，基于 5 个 qualifying issues/PRs。
- **维护（截至 2026-06）：** 最后 push 在 2026-06，未归档，最新版本 3.9.x——一个持续发版、积极维护的网关，而非在吃老本。[推断]
- **治理与背书：** 由 `Organization` 持有且**厂商背书**（Kong Inc.，一家拿过融资的商业公司），不是基金会项目。这意味着有真实的路线图和支持，但**开源核心（open-core）**模式才是治理现实：OSS 网关只是一档，厂商掌控什么留在开源、什么挪进 Enterprise（Developer Portal、RBAC、高级 AI 插件）。路线图归厂商，而非中立基金会。[推断]
- **年龄与 Lindy 判断：** 建于 2014-11，约 12 年**且仍然活跃**——很强的 **Lindy** 信号：它熬过了多次架构变迁（甚至在 3.4 这条线移除了作为配置存储的 Cassandra），是寿命最长的 OSS API 网关之一。老 + 活跃 ⇒ 核心代理是安全的耐久押注。[推断]
- **采用/生态：** 广泛的生产采用、庞大的插件生态、一个 Kubernetes Ingress Controller、做 GitOps 配置的 decK，以及成熟文档——生态深度本身就是可持续性信号。
- **风险标记：** 真正要盯的是**开源核心的功能闸门**，而非 license 反水——OSS 核心仍是 Apache-2.0，但高级特性可能仅限企业版，且这条划分随版本变动。依赖某个具体插件前请先核实其 OSS 可用性。[推断]

## 存疑（未验证）

- [未验证] 观察到的最新版本为 3.9.3（2026-06-17 发布），仓库活动到 2026-06-17；star 数约 43.7k（截至 2026-06）——GitHub star 不可靠且对日期敏感，仅作参考。
- [未验证] 第三方对比里引用的吞吐/延迟数字（如 Kong 约 16k RPS/节点、APISIX 约 23k QPS/核、开插件后 APISIX 快约 200%）来自外部基准测试博客，随版本、配置、硬件差异巨大，无第一方保证。
- [推断] 开源版与企业版之间的插件划分（Developer Portal、RBAC、高级 AI 特性）随版本变动；依赖某个具体插件前，请对照当前仓库/文档核实其 OSS 可用性。
- [未验证] AI Gateway 插件支持的 LLM 供应商与 MCP 特性的确切清单随版本变化；此处的供应商列表反映 README 的表述，并非逐版本审计。
- [未验证] 据称 Cassandra 已在 3.4 这条线移除（自 2.7 起弃用）；如要迁移，请对照 UPGRADE.md 确认确切版本。
