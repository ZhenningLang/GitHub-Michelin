---
name: haipproxy
slug: haipproxy
repo: https://github.com/SpiderClub/haipproxy
category: proxy-pool
tags: [proxy, proxy-pool, scrapy, redis, distributed, scraping, python, self-hosted]
language: Python
license: MIT
maturity: last release v0.1 (2018), repo dormant (pushed 2022-12), ~5.5k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2022-12-26T11:50:58Z
  default_branch: master
  default_branch_sha: ab30ccf4b1d78e9304c27830006cc5800fe41bb3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:54:59Z
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
        last_commit_age_days: 2625
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: haipproxy
        dependent_repos_count: 1
        downloads_last_month: 47
        graph_tier: D
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3293
        last_commit_age_days: 2625
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# haipproxy

一个基于 Scrapy + Redis 的分布式高可用 IP 代理池——爬虫收割公开代理，校验器给它们打分，消费者经一个 Python 客户端或 Squid 集成拉取低延迟代理。

![haipproxy — 健康度雷达](../../assets/health/haipproxy.zh.svg)

## 何时使用

你在跑一个*大型、分布式*的爬取——多台机器上一堆 spider 猛攻一个目标——单节点的免费代理收割器把池子保持得既不够新也不够可用。你想把爬取、校验和调度解耦，让它们能扩展并扛住节点故障。你起一个 Redis，部署 haipproxy 基于 Scrapy 的爬虫持续收割代理，让它的校验器打分排序，然后让你的 spider 从 Redis 支撑的池子里（经自带 Python 客户端）拉一个已校验代理，或走 Squid 集成路由。架构明确是 HA：爬虫和调度器被设计成可冗余运行，并有一个「贪婪」选择策略文档化以从池子里榨更多。项目引用了一个测试：对某目标在 11 小时内处理约 8 万请求——用例是持续、高吞吐的分布式爬取，不是一个快速的本地池。

当规模和可用性才是真正的问题时，它是对的选择——Redis 支撑的任务路由、分布式爬虫和一个消费者客户端都很要紧——且你接受随之而来的更重基建。

## 何时不用

- **小规模或单机爬取。** 对几十个请求而言，Scrapy + Redis + scrapy-splash 这套是杀鸡用牛刀；单节点池（或干脆一个付费代理）要跑的东西少得多。
- **你跑不了 Redis（也可能跑不了 Splash）。** Redis 是任务队列和池状态的硬依赖；JS 渲染的来源还会拉进 scrapy-splash。若你运维不了这些，这不是你的工具。
- **在免费代理上要生产可靠性。** 它池化*免费公开*代理——天生不稳；README 自己指出，因地理限制有些代理连不上 Google 这类站点。不能失败的任务请买商业代理。
- **你需要一个在维护的依赖。** 仓库**长期休眠**——最后发布约 2018，最后 push 2022-12。你采纳并运维的实质上是冻结的、Python 2/3 时代的代码；预期要做兼容工作（见健康度）。[未验证]
- **敏感流量。** 把凭据/私密数据经由未知收割代理转发是数据暴露风险。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Scylla](scylla.zh.md) | ✅ | 简单的单服务池、网页 UI 和 JSON API 已足够时，选 Scylla。 | 单服务池，带网页 UI + JSON API，不需 Redis——跑起来简单得多，但不像 haipproxy 那样为分布式/HA 爬虫规模而建。 |
| [ProxyBroker](proxybroker.zh.md) | ✅ | 轻量 CLI finder/checker/server 已足够时，选 ProxyBroker。 | 一个轻量 CLI finder/checker/server，无基建——调用最容易，但无分布、无 HA，且自身休眠/Python 易碎。 |
| [proxy_pool（jhao104）](proxy-pool.zh.md) | ✅ | 想要更简单的 Redis 支撑单进程自托管池时，选 proxy_pool。 | 流行的 Redis 支撑自托管池，比 haipproxy 的分布式 Scrapy 架构更简单的单进程设计；免费代理生态位相近。[未验证] |
| 付费代理供应商（Bright Data、Oxylabs……） | 未收录 | 生产 SLA、住宅 IP 和轮换更重要时，选付费代理供应商。 | 带 SLA 和轮换的商业住宅/数据中心池——生产答案；只有当你确实需要一个自托管的*分布式*免费池时，haipproxy 才合适。 |

## 技术栈

- **语言：** Python 3（基于 Scrapy 的爬虫）。
- **基建：** **Redis**（任务队列、池状态、调度）和 **Scrapy** 作为爬取框架；**scrapy-splash** 处理 JavaScript 渲染的代理来源。
- **架构：** 解耦的爬虫 / 校验器 / 调度器组件，为高可用而设计；灵活的任务路由；可配置的选择策略（如贪婪）。
- **消费者：** 一个自带 Python 客户端和一个 Squid 代理集成，供下游 spider 使用。

## 依赖

- **运行时：** Python 3、一个运行中的 **Redis** 服务器（必需）、Scrapy；JS 渲染来源还需 **scrapy-splash**（因而需一个 Splash 实例）。
- **部署：** 独立（手动装依赖 + 启动组件）或 **docker-compose** 容器化整套栈。
- **消费端：** Python 客户端库，或你路由经过的 Squid。
- **它是一个多组件系统**，不是单个二进制或单个进程。

## 运维难度

**中到高。** 这确实是一个要运维的*分布式系统*：Redis、多个 Scrapy 爬虫/校验器/调度器组件、JS 来源可选的 Splash，以及一个消费者客户端或 Squid。docker-compose 缓解了起步，但你仍要运行并监控好几个活动部件、保持 Redis 健康，并接受免费代理池质量起伏。休眠让这雪上加霜——今天跑约 2018 年代的 Scrapy/Python 代码，很可能在能起来之前就要先钉死依赖或移植。基建负担加上兼容负担，使它成为此处收录三个池里最重的一个。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** **休眠。** 最后发布 v0.1 来自 2018；最后 push 2022-12，此后无活动——未在积极开发，虽未正式归档。当作冻结的、Python 2/3 过渡期代码对待。
- **治理 / bus factor。** 一个 **Organization** 账号（SpiderClub），但活跃核心贡献者很少；org 外壳改变不了真实维护已停止这一事实。bus factor 实质上等同于一个被弃的单维护者仓库。[推断]
- **年龄与 Lindy 判断。** 约 9 年（2017-09 创建）但**自约 2022 起休眠**⇒ Lindy *失效*：有年龄而无持续活动是弃用信号，不是耐久性。老 + 休眠是红旗，不是社会证明。
- **采用度。** 约 5.5k star、约 900 fork 反映真实的历史人气（尤其在中文爬虫圈），但在休眠仓库上这是*遗产*采用——不是它能在今天的栈上跑的证据。[未验证]
- **风险标记。** 长期休眠 + 很可能与现代栈不兼容是头号风险，外加免费公开代理固有的不可靠/安全暴露。MIT，无 relicense 顾虑。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 5.5k star；最后发布 v0.1（2018）、最后 push 2022-12——数字对时间敏感，来自 GitHub API。
- [未验证] 与当前 Python/Scrapy 的兼容性此处未测试；约 2018 年代代码很可能需移植/钉死，但具体崩点未确认。
- [未验证] 约「8 万请求/11 小时」的数字是项目 README 自己的基准，未独立复现。
- [推断] 「org 账号但实质被弃」是从提交/发布断档推断，而非官方弃用声明；免费代理安全风险是普遍属性，并非对其来源的实测断言。
