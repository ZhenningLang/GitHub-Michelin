---
name: Scylla
slug: scylla
repo: https://github.com/MikeChongCan/scylla
category: proxy-pool
tags: [proxy, proxy-pool, scraping, web-ui, json-api, python, self-hosted]
language: Python
license: Apache-2.0
maturity: last release 1.2.0 (2022-03), repo touched 2025-06, ~4.0k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2025-06-09T01:51:36Z
  default_branch: main
  default_branch_sha: b051fd586f2e3268bb07f8d94a0b27dce01dea12
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:55:26Z
  overall: D
  overall_score: 1.25
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 752
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: scylla
        dependent_repos_count: 13
        downloads_last_month: 245
        graph_tier: D
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3087
        last_commit_age_days: 752
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
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# Scylla

一个自托管的「智能代理池」应用，持续爬取公开代理、校验并打分（延迟、稳定性、匿名度），再经网页 UI、JSON API 和内置正向代理服务器把它们暴露出来。

![scylla — 健康度雷达](../../assets/health/scylla.zh.svg)

## 何时使用

你跑的爬虫老是被限流或封 IP，你想要一个*常驻服务*替你维护一池筛过的免费代理供你取用——而不是一个你手动反复重跑的 CLI。你 `docker run` 起 Scylla，等一两分钟让它把池子填上，然后访问 `http://localhost:8899/api/v1/proxies?https=true&anonymous=true&country=US` 拿到一份按 HTTPS 支持、匿名度和国家过滤后、当前有效的代理 JSON 列表——再以极少代码直接喂给 requests/Scrapy。你也可以把流量指向它内置的正向代理端口，让它替你挑一个已校验的 IP，并在网页 UI 里看池子健康度和一张地理分布图。它是「带 API 的可运行服务」这种形态：起一次，从多个任务里查它。

当你想要一个*可查询、常开*的免费代理池，带质量打分和仪表盘，且你乐意自托管一个小型 Python 服务（最好走 Docker）时，它是对的选择。

## 何时不用

- **经内置正向代理走 HTTPS。** 文档说正向代理服务器**不**支持 HTTPS 请求——对 HTTPS，你消费 JSON API 的代理列表并自己连接，而不是串过 Scylla 的代理端口。这是一个要绕开来设计的真实约束。
- **生产可靠性。** 它池化的是*免费公开*代理——天生不稳、慢，有时还恶意。任何不能失败的事，请买商业代理；Scylla 用于低风险/实验性爬取。
- **频繁维护的依赖。** 最后打标版本是 2022 年，此后活动稀疏（2025 年一次改动）。你采纳的是近乎冻结的代码——做实验没问题，当承重依赖有风险（见健康度）。
- **敏感流量。** 把凭据或私密数据经由未知收割代理转发是数据暴露风险。[推断]
- **零运维预期。** 它是带数据存储和爬虫的服务；虽然 Docker 让启动容易，你仍要运维一个运行中的进程，并接受池子质量起伏。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [ProxyBroker](proxybroker.zh.md) | ✅ | CLI 优先的 finder/checker/server 比常驻服务更轻时，选 ProxyBroker。 | 一个 CLI 优先的 finder/checker/server，而非 UI+API 服务；更休眠、更易在现代 Python 上崩，但快速收割时调用更轻。 |
| [haipproxy](haipproxy.zh.md) | ✅ | 分布式 Scrapy+Redis 高可用比单服务简洁更重要时，选 haipproxy。 | 为爬虫规模的高可用而建的分布式 Scrapy+Redis 池；基建重得多（需 Redis）且同样长期休眠，对照 Scylla 的单服务简洁。 |
| 付费代理供应商（Bright Data、Oxylabs……） | 未收录 | 需要生产 SLA、鉴权、住宅 IP 和轮换时，选付费代理供应商。 | 带 SLA、鉴权、住宅 IP 和轮换的商业池——生产答案；只有当「免费 + 自托管」可接受时 Scylla 才合适。 |
| [proxy_pool（jhao104）](proxy-pool.zh.md) | ✅ | 想要 Redis 支撑、形态相近但更简单的免费代理池时，选 proxy_pool。 | 另一个流行的自托管免费代理池，爬取/校验/API 形态相似（Redis 支撑）；生态位相近，栈和维护状态不同。[未验证] |

## 技术栈

- **语言：** Python（带一个小的 JS/构建前端做网页 UI，从源码经 npm + make 构建）。
- **组件：** 一个持续的爬虫/校验器、一个存代理记录 + 质量指标的数据存储、一个 JSON REST API（`/api/v1/proxies`）、一个网页 UI（代理列表 + 地理图）和一个内置 HTTP 正向代理服务器。
- **校验：** 对延迟、稳定性、有效性和匿名度打分；对来源具备无头浏览器爬取能力。

## 依赖

- **运行时：** Python；一个数据库用于持久化代理记录与指标（打包/内嵌）。
- **安装：** Docker（推荐，单条命令）、从 PyPI 走 `pip`，或从源码构建（git + npm + make）。
- **网络：** 出站访问以爬取代理来源；本地暴露 API + 正向代理端口。
- **基础单节点部署不需要外部服务集群。**[推断]

## 运维难度

**低到中。** Docker 让顺路径成为一行命令，预热 1–2 分钟后你就有一个活的 API。「中」的部分在于它是一个带数据存储和后台爬虫的*常驻服务*：你运维一个运行中的进程，池子质量随免费代理流失而起伏，且你必须通过直接消费 API 列表来绕开「正向代理不支持 HTTPS」的限制。从源码构建多一道 npm/make 前端步骤。单节点用无集群，但比一次性 CLI 要多跑些东西。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后打标版本 1.2.0 来自 2022-03；仓库最近一次改动在 2025-06，但没有新发布——**滑向休眠**，未在积极开发。这是一个 fork 谱系仓库（`MikeChongCan/scylla`），其描述被改写成了 AI/LLM 口吻。未归档。
- **治理 / bus factor。** 一个 User 账号仓库，贡献者很少（含 dependabot）；单一维护者的 bus-factor 风险，无基金会背书。一个发版停滞的 User 仓库上有约 4.0k star，是个值得掂量的标记，而非社会证明。[推断]
- **年龄与 Lindy 判断。** 约 8 年（2018-04 创建）但发版线停滞⇒ Lindy **弱到参半**：长寿，但鉴于无近期发布，「仍活跃」那一半站不太稳。
- **采用度。** 约 4.0k star 表明自托管代理池历史上人气不错；鉴于发版断档，当前采用度/健康度不太清楚。[未验证]
- **风险标记。** 停滞的发版 + 免费代理不可靠 + 正向代理不支持 HTTPS 是当前风险；Apache-2.0，无 relicense 顾虑。被改写的 AI 时代描述是营销，不是能力变化。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 4.0k star，最后发布 1.2.0（2022-03）——数字对时间敏感；2025-06 的 push 来自 API，其实质未审阅。
- [未验证] 确切的数据存储、无头浏览器使用和当前精确的来源列表，来自 README/文档，本轮未对照代码确认。
- [推断] 「滑向休眠」是从发版断档（2022）对照后来零星提交推断，而非官方状态。
- [推断] 免费代理的安全/可靠性风险是收割公开代理的普遍属性，并非对 Scylla 具体来源的实测。
