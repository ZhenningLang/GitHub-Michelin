---
name: SpiderKeeper
slug: spiderkeeper
repo: https://github.com/DormyMo/SpiderKeeper
category: crawling-tools
tags: [scrapy, scrapyd, dashboard, admin-ui, scheduler, flask, python]
language: Python
license: MIT
maturity: PyPI v1.2.0 (2017-09), repo stale since 2023-05, ~2.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2023-05-04T20:44:05Z
  default_branch: master
  default_branch_sha: d6156d35a95ba8c3ac759a08367079619555b6dd
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:15:02Z
  overall: E
  overall_score: 0.25
  scored_axes: 4
  applicable_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NONE"
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 3039
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: spiderkeeper
        dependent_repos_count: 5
        downloads_last_month: 28
        graph_tier: D
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3900
        last_commit_age_days: 3039
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# SpiderKeeper

一个基于 Flask、叠在 Scrapyd 之上的 Scrapy 爬虫管理 web UI / 看板——在浏览器里部署项目、调度周期作业、查看运行统计。它自己什么都不抓；它是覆盖在一个或多个 Scrapyd 服务器之上的管理层。轻量、流行，且大体已陈旧。

![spiderkeeper — 健康度雷达](../../../assets/health/spiderkeeper.zh.svg)

## 何时使用

你在 Scrapyd 上跑一个小型抓取，受够了用 `curl` 去敲 JSON 端点来部署和调度爬虫。你想要一个浏览器看板：点一下上传项目 egg、设某个爬虫每晚按 cron 跑、看哪些作业在跑/已完成、瞄一眼统计——而不用自己写 UI。你 `pip install spiderkeeper`，把它指向你的 Scrapyd 服务器（`--server=http://localhost:6800`），就得到一个 5000 端口上的 Flask 看板，带周期调度（经 APScheduler）、作业板和 Swagger API。对一个已经在跑 Scrapyd、想要尽可能简单控制面板的单人或小团队，SpiderKeeper 是那个轻量的经典之选——前提是你接受这软件很老（见下）。

## 何时不用

- **别为 2026 年的新项目采用它。** 仓库代码自 2023-05 起陈旧，PyPI release 冻结在 v1.2.0（2017-09）。它钉的是 2017 年的栈（Flask 0.12、SQLAlchemy 1.1、Werkzeug 0.12），所以在现代 Python（3.11+）上安装意味着放宽 pin 的摩擦，还要背着未打补丁的传递依赖。[推断]
- **没有 Scrapyd 它没价值。** 它纯粹是 Scrapyd 之上的 UI——你若不跑 Scrapy/Scrapyd，它对你毫无用处。见 [Scrapyd](scrapyd.zh.md)。
- **安全弱——别把它暴露在不受信任的网络。** 鉴权只有可选的 HTTP basic，默认 `admin`/`admin`，没有用户管理、RBAC 或 TLS。未为多租户或公网部署加固。
- **更新的替代更能打。** Gerapy（Django+Vue、更现代、分布式管理）和 ScrapydWeb（多节点、日志解析、告警）是这个细分里更完整的后继；SpiderKeeper 是更老更简单的那个。
- **别指望许可证干净。** MIT 在 `setup.py` 和 README 徽章里有声明，但 README 链接的 `LICENSE.md` 在仓库里并不存在——所以 GitHub 检测不到许可证，MIT 文本/版权授予是声明了却没真正随仓库交付。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Scrapyd](scrapyd.zh.md) | ✅ | 需要 SpiderKeeper 封装的守护进程时，选 Scrapyd。 | SpiderKeeper 封装的守护进程——活跃维护、组织背书。SpiderKeeper 是叠在*它之上*的 UI，不是它的替代。 |
| Gerapy | 未收录 | 需要面向分布式 Scrapy 管理的 Django + Vue 看板时，选 Gerapy。 | 面向分布式 Scrapy 管理的 Django + Vue 看板；更现代，通常是这个细分今天推荐的后继。 |
| ScrapydWeb | 未收录 | 需要 Scrapyd 之上更丰富的 web UI 时，选 ScrapydWeb。 | Scrapyd 之上更丰富的 web UI（多节点、日志解析、邮件告警），但它本身也相当陈旧。 |
| Zyte Scrapy Cloud | 未收录 | 需要商业托管替代时，选 Zyte Scrapy Cloud。 | 商业托管替代——无需自托管 scrapyd+UI 栈，代价是厂商锁定和计费。 |

## 技术栈

- **语言：** Python；一个 Flask web 应用。
- **Web/UI：** Flask 0.12 + Werkzeug/Jinja2/itsdangerous（2017 版本），Flask-RESTful + flask-restful-swagger 提供 API/Swagger UI。
- **存储：** Flask-SQLAlchemy / SQLAlchemy 1.1——默认 SQLite，MySQL 经 PyMySQL。
- **调度：** APScheduler 3.3 做周期/cron 作业。
- **鉴权：** Flask-BasicAuth（仅 HTTP basic）。
- **Scrapyd 连接：** 用 `requests` 调 Scrapyd 的 JSON API；egg 用 `scrapyd-client` 构建。

## 依赖

- **硬性依赖：** 一个在跑的 Scrapyd 服务器（`--server=...`、`--type=scrapyd`）。没有它 SpiderKeeper 无用。
- **运行时：** Python（2017 年的 pin 面向 Python 2.7 / 3.5；现代 Python 大概率需要放宽 pin——见存疑）。
- **数据库：** 默认 SQLite（零配置）；可选 MySQL 经 PyMySQL。
- **构建/部署流程：** 用 `scrapyd-client` 打项目 egg，经 SpiderKeeper 上传到 Scrapyd。

## 运维难度

**跑起来低，但要交“陈旧软件”的税。** 第一天很容易：`pip install spiderkeeper`、指向 Scrapyd、开 5000 端口——SQLite 意味着不用配数据库。摩擦在于让一个 2017 年钉死的 Flask 0.12 栈在当前解释器上还能装，以及安全姿态：默认 `admin`/`admin` 的 basic 鉴权、没有 TLS/RBAC，意味着别人能访问之前你必须把它放在带真实鉴权的反向代理后（或留在 localhost/VPN）。没有集群或 HA 方案——就是一个你看着的单一轻量 Flask 进程。

## 健康度与可持续性

- **响应速度**：无法计算——no_data。
- **维护（2026-06）。** 陈旧 / 大概率废弃——仓库代码自 2023-05 起未动，PyPI 自 2017-09 冻结在 v1.2.0，无 GitHub release 或 tag，约 70 个 open issue。未 archived，但没有发布节奏。[推断]
- **治理 / bus factor。** bus factor 为 **1**：`DormyMo` 约 93 次提交，其余每个贡献者 1–3 次。单维护者 User 账号，无组织延续性。
- **年龄 × Lindy。** 自 2016 起存在但沉默约 3 年（且包沉默约 9 年）——不过 Lindy，后者要求又老**又**活；一个无人维护的工具面对演进中的 Scrapy/Python 栈只会腐烂。[推断]
- **采用度。** 约 2.8k star 反映它作为最简单 Scrapyd 看板的真实过往热度，但势头已转向 Gerapy/ScrapydWeb。厂商 demo homepage 大概率已下线。[未验证]
- **风险标记。** 陈旧的依赖底线、默认凭据的弱鉴权、单一维护者，以及不完整的许可证（声明了 MIT 但仓库里缺许可证文件）。[推断]

## 存疑（未验证）

- [推断] 许可证是*声明*的 MIT（setup.py + README 徽章），但被引用的 `LICENSE.md` 文件在仓库里不存在，所以 MIT 授予是声明了却没随实际许可证文本交付；GitHub 元数据报告无许可证。
- [推断] PyPI v1.2.0（2017-09）比仓库（最后 push 2023-05）陈旧得多；已发布的包在现代 Python 上不放宽 pin 就能装这一点存疑，本次未实测。
- [未验证] 厂商 demo homepage 是否还活，以及 ScrapydWeb 与 Gerapy 当前的相对陈旧度，本次未独立抓取。
- [未验证] 截至 2026-06 约 2.8k star / 约 70 个 open issue；计数对时间敏感，仅供参考。
