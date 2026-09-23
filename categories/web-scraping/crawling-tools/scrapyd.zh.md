---
name: Scrapyd
slug: scrapyd
repo: https://github.com/scrapy/scrapyd
category: crawling-tools
tags: [scrapy, crawler, daemon, deployment, scheduler, http-api, python, twisted]
language: Python
license: BSD-3-Clause
maturity: v1.6.0 (2025-07), active, ~3.1k stars (as of 2026-06)
last_verified: 2026-06-28
type: service
upstream:
  pushed_at: 2026-06-19T03:52:53Z
  default_branch: master
  default_branch_sha: c661f050d76342e057509986ef851d3c7c1d0208
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:14:59Z
  overall: B
  overall_score: 2.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: scrapyd
        dependent_repos_count: 525
        downloads_last_month: 33535
        graph_tier: C
        volume_tier: C
        cross_check_divergence: null
        release_downloads: 149
        release_assets: 2
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4981
        last_commit_age_days: 2
        cohort: service
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-3-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# Scrapyd

一个通过 JSON HTTP API 部署并运行 Scrapy 爬虫的服务守护进程——把 Scrapy 项目打成 egg、上传，然后远程调度/取消/监控抓取作业。它是 Scrapy 官方组织出品、把“在生产里跑 Scrapy”这件事标准化的守护进程。

![scrapyd — 健康度雷达](../../../assets/health/scrapyd.zh.svg)

## 何时使用

你是数据工程师，写了几个在自己笔记本上跑得好好的 Scrapy 爬虫，现在需要让它们在服务器上跑——按计划、可重启、还能有多个项目版本来回前滚后滚。你不想 SSH 进去手动 `scrapy crawl`，也不想自己围着它搓一个 supervisor。你在机器上装好 Scrapyd，用 `scrapyd-deploy` 把每个项目打包成 egg 并上传，此后一切都走 HTTP：`POST schedule.json` 排一个抓取、`listjobs.json` 看在跑什么、`cancel.json` 停掉某个。Scrapyd 把每个作业作为受管的 `scrapy crawl` 子进程拉起、并发可配，保留日志与 item feed，并在 6800 端口提供一个极简状态页。它是 Scrapy 官方背书、把本地爬虫变成可部署抓取服务的标准方式——也是 ScrapydWeb、Gerapy、SpiderKeeper 这类管理 UI 所依托的那层 API。

## 何时不用

- **它只跑 Scrapy。** 它字面上就是拉起 `scrapy crawl`；不是通用作业调度器。要编排任意任务，用 Airflow、Celery 或 cron。
- **默认单节点。** 没有内建集群或跨机分布——横向扩展意味着跑多个 Scrapyd 实例并自己协调它们（通常靠一个面向多个守护进程的 UI 层）。
- **极简、需自行开启的安全。** JSON API 默认无鉴权；没有你自己的鉴权/反向代理层之前，别把 6800 端口暴露到公网。[推断——基于“minimal web interface”文档措辞与 Twisted auth 痕迹，未逐行核验默认配置]
- **要真正好用，你会想在上面加个 UI。** 内建 web 页只能监控——日常管理需要在其上叠 [SpiderKeeper](spiderkeeper.zh.md)、ScrapydWeb 或 Gerapy。
- **你想要托管、省心的 SaaS。** 如果你压根不想自己跑这个守护进程，Zyte Scrapy Cloud 替你卸掉 Scrapyd 留给你的运维负担。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [SpiderKeeper](spiderkeeper.zh.md) | ✅ | 需要叠在 Scrapyd 之上的 Flask 管理 UI 时，选 SpiderKeeper。 | 不是竞品——是**叠在 Scrapyd 之上**的 Flask 管理 UI（部署、周期调度、看板）。更老更陈旧；是 Scrapyd 的补充而非替代。 |
| ScrapydWeb / Gerapy | 未收录 | 需要 Scrapyd 之上更丰富的管理 UI 时，选 ScrapydWeb 或 Gerapy。 | 同样是 Scrapyd 之上的管理 UI：ScrapydWeb 加多节点/日志解析/告警；Gerapy 是 Django+Vue、更现代。二者都调 Scrapyd 的 API，不是守护进程的替代。 |
| Zyte Scrapy Cloud | 未收录 | 需要 Scrapy 商业托管 SaaS 时，选 Zyte Scrapy Cloud。 | Scrapy 的商业托管 SaaS（无需自托管）；以厂商锁定和按量计费为代价卸掉运维。 |
| Apache Airflow / Celery / cron | 未收录 | 需要通用调度器，而不是 Scrapy 原生部署模型时，选 Airflow、Celery 或 cron。 | 通用调度器——范围更广，但没有 Scrapy 原生的 eggify/部署/版本模型；跑爬虫的胶水得你自己搭。 |

## 技术栈

- **语言：** Python（>=3.10–3.13）。
- **核心框架：** Twisted——该守护进程是一个 Twisted 应用（Twisted 风格的 `render_GET`、avatar/realm 鉴权原语）。
- **状态：** 作业/版本状态持久化在 sqlite3。[推断——从 ruff S608 忽略注释与配置推断，未读运行时源码逐行确认]
- **运行时依赖（pyproject，v1.6.0）：** `scrapy>=2.0.0`、`twisted>=17.9`、`w3lib`、`zope.interface`、`packaging`、`setuptools`，Windows 上加 `pywin32`。
- **接口：** JSON HTTP API（`schedule.json`、`cancel.json`、`addversion.json`、`listjobs.json`……）加一个极简状态 web 页；`scrapyd-deploy`（来自单独的 `scrapyd-client`）负责 eggify + 上传。

## 依赖

- **运行时：** Python 3.10+、一个 Twisted/Scrapy 安装，以及放 egg、日志和 sqlite 状态文件的磁盘。
- **配套工具：** `scrapyd-client`（单独的包）提供 `scrapyd-deploy` 来打包并部署项目。
- 守护进程本身**不需要外部数据库/服务**；状态是本地 sqlite。若对外暴露，建议加反向代理 + 鉴权。
- **可选 UI：** 若想要管理看板，可上 SpiderKeeper / ScrapydWeb / Gerapy。

## 运维难度

**低到中。** 顺路径是 `pip install scrapyd`、跑起来、`scrapyd-deploy` 你的项目——一个进程、本地 sqlite 状态、无集群。难度出现在边缘：它默认无鉴权，所以暴露前你必须加鉴权/反向代理/防火墙；超出一台机器的扩展意味着起多个守护进程加一个面向它们的 UI/协调器；而主机级看护（systemd）、日志/egg 的磁盘清理、并发抓取的背压调优都归你。守护进程本身稳定省心——功夫在它周围的生产加固。[推断——默认无鉴权的具体配置未逐行核验]

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 活跃——最后 push 于 2026-06-19，最新 release v1.6.0（2025-07-22），大致每年一个特性版本，状态“Production/Stable”，未 archived。仅约 6 个 open issue——小而被精心照料的范围。[推断——GitHub Releases API 只到 1.4.1，1.5.0/1.6.0 以 docs/news.rst changelog 为准]
- **治理 / bus factor。** 归在 **`scrapy` GitHub 组织**下（维护 Scrapy 框架的同一社区/团队），不是个人账号——`jpmckinney` 是当前的代表性维护者，还有几位 Scrapy 核心组成员贡献。bus-factor 风险低。
- **年龄 × Lindy。** 创建于 2013（约 13 年）且本月仍有 push ⇒ **强 Lindy** 信号：成熟、慢节奏的基础设施，早已熬过炒作周期。
- **采用度。** 约 3.1k star；它是事实上的 Scrapy 部署守护进程，周围有一整套面向其 API 构建的管理 UI（ScrapydWeb/Gerapy/SpiderKeeper）。
- **风险标记。** 很少。BSD-3-Clause，无 relicense 历史；主要注意点是默认无鉴权的 API，这属于部署责任，不是项目健康问题。[推断]

## 存疑（未验证）

- [推断] sqlite3 持久化与默认无鉴权的 API，是从配置/ruff 注释与文档措辞推断，未通过逐行读运行时源码确认。
- [推断] GitHub Releases API 停在 1.4.1（2023）；1.5.0/1.6.0 取自 `docs/news.rst` changelog，并以其为准——团队似乎停止切 GitHub Release 对象，但仍向 PyPI 发布。
- [未验证] 截至 2026-06 约 3.1k star、约 6 个 open issue；计数对时间敏感，仅供参考。
