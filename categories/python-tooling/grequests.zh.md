---
name: GRequests
slug: grequests
repo: https://github.com/spyoungtech/grequests
category: python-tooling
tags: [http, async, gevent, requests, concurrency, python]
language: Python
license: BSD-2-Clause
maturity: v0.7.0, low-activity (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2024-08-08T21:52:34Z
  default_branch: master
  default_branch_sha: 60f70e99e942a2df378b4e4f6202dcf862754c2d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:56:22Z
  overall: C
  overall_score: 1.75
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
        last_commit_age_days: 775
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: grequests
        dependent_repos_count: 1000
        downloads_last_month: 293723
        graph_tier: B
        volume_tier: B
        cross_check_divergence: null
        release_downloads: 40
        release_assets: 2
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 5248
        last_commit_age_days: 775
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-2-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# GRequests

Requests + Gevent：用熟悉的 `requests` API 并发发出大量 HTTP 请求，通过 `map()`/`imap()` 收集结果，而不必自己写异步代码。

![grequests — 健康度雷达](../../assets/health/grequests.zh.svg)

## 何时使用

你是数据工程师，在维护一套又老又关键的 Python 2/3 同步代码，它要扇出到几百个 URL——抓一批页面、轮询一组内部端点，或者预热缓存——而 `for url in urls: requests.get(url)` 这种顺序循环成了瓶颈。你不想为了改成 `asyncio`/`httpx` 而重写所有调用点、去学 `await`、或手动维护连接池；你只想让现有的那些 `requests` 调用并行起来。你构造一个未发送的 `grequests.get(u)` 请求对象列表，交给 `grequests.map(reqs, size=10)`，拿回一个顺序一致的 `Response` 列表——还能传一个 `exception_handler`，让单个超时不至于拖垮整批。因为底层是 gevent 用 greenlet 做协作式调度，你不碰 `threading`、也不把逻辑改写成协程，就拿到了 I/O 并发。

当周边技术栈本就基于 gevent（或你能接受 gevent 的 monkeypatching）、且诉求是「用最小 diff 让现有同步 `requests` 代码并发起来」时，你才会专门选它。对顺序不敏感的流式消费，则用 `imap()` / `imap_enumerated()` 按完成顺序取响应。

## 何时不用

- **全新的异步代码。** 对新项目，原生 `asyncio` 配 `httpx` 或 `aiohttp` 是更受支持、维护更活跃的路线——grequests 的定位是给*已有*同步代码做改造，而非充当你的异步 HTTP 栈。
- **你无法容忍 gevent 的 monkeypatching。** gevent 在 import 时就给标准库（socket、ssl、threading）打补丁；这可能和其他库冲突，README 也警告你往往必须在 `requests` 等之前**先** import grequests。在混用原生 asyncio、多进程或不预期被打补丁 I/O 的 C 扩展的代码里，这是个真实的坑。[未验证]
- **CPU 密集或需要真并行。** greenlet 是单线程协作式并发——它救 I/O 等待，不救 CPU 计算。要并行跑 CPU，你仍得用多进程。
- **你需要 HTTP/2、现代 TLS 特性或流式优先的 API。** 它只是经典 `requests` 上的薄封装，继承了 requests 的能力与局限。
- **你想要一个被高频维护的依赖。** 发布节奏偏慢（见健康度）——作为稳定工具尚可，但若你需要上游快速修问题，要权衡。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| httpx | 未收录 | 新代码可以接受现代同步／异步客户端，并且需要 HTTP/2 支持时，选 httpx。 | 更适合作为长期并发 HTTP 路线，但异步并发需要 `async`/`await`，不是 drop-in `requests` 调用。 |
| aiohttp | 未收录 | 应用已经 asyncio-native，或还需要异步 HTTP 服务端栈时，选 aiohttp。 | 异步生态成熟，但编程模型与 drop-in `requests` 不同。 |
| requests-futures | 未收录 | 想保留 `requests` 兼容性，同时用真实线程且不做 gevent monkeypatching 时，选 requests-futures。 | 对一些应用集成更简单，但线程池并发有不同的扩展和阻塞取舍。 |
| `requests` + `concurrent.futures` | 未收录 | 显式的小型线程／进程池比再加一个依赖更清楚时，选普通 `requests` 加标准库 futures。 | 无额外依赖、无 monkeypatching，但比 `grequests.map()` 多一点样板代码。 |

## 技术栈

- **语言：** Python。
- **核心依赖：** `requests`（HTTP 层与 `Response` 对象）和 `gevent`（基于 greenlet 的协作式并发，底层 libev/libuv，并对标准库做 monkeypatching）。
- **API 面：** 未发送的请求对象（`grequests.get/post/...`），加上 `map()`、`imap()`、`imap_enumerated()` 来并发派发，可带可选的 `size`（池大小）与 `exception_handler`。

## 依赖

- **运行时：** Python，外加 `requests` 与 `gevent`（后者拉入 `greenlet` 及编译好的事件循环后端）。[未验证]
- **服务/基础设施：** 无——它是客户端库，没有服务端或数据存储。
- **import 顺序约束：** 因为 gevent 要 monkeypatch，README 建议尽早 import grequests；这是对你*如何*组织 import 的运维约束，而非一个软件包。[未验证]

## 运维难度

作为库**很低**——`pip install grequests` 然后调用即可。真正的运维成本在 gevent 的 monkeypatching：把 import 顺序弄对，并核实它不与你栈里其他部分冲突（其他异步框架、原生线程、某些 C 扩展）。这一关过了之后就只是函数调用，没有任何东西要部署或运维。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最近发布 v0.7.0（2023-06）；仓库最后 push 于 2024-08。发布稀疏、近期间隔很长——更像一个**稳定、低活跃**的工具，靠一小块稳定面吃老本，而非在积极开发。未归档。[推断]
- **治理 / bus factor。** owner 是 **User** 账号（spyoungtech），他接手了项目；最初的提交可追溯到 Kenneth Reitz（`requests` 作者）。实质上是单一维护者——一个 bus-factor 标记。[推断]
- **年龄与 Lindy。** 2012 年创建，约 14 岁且仍被广泛安装。年龄加上窄而稳的范围是中等 Lindy 信号——但 Lindy 需要*仍然活跃*，而这里活跃度偏低，所以应按「稳定的遗留库」而非「蓬勃维护」来权衡。[推断]
- **采用度。** 约 4.6k star 与长期的 PyPI 存在表明历史采用真实；新项目大多已转向 asyncio 客户端（httpx/aiohttp）。[未验证]
- **风险标记。** 单一维护者＋慢节奏＋对 gevent monkeypatching 行为的硬依赖是主要风险；BSD-2-Clause 宽松，未发现 relicense 历史。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 4.6k GitHub star；star 数对时间敏感且不可靠，仅供参考。
- [未验证] 支持的 Python 版本这里不断言——README 有版本徽章，但确切矩阵跟随 gevent/requests 的支持范围、随版本变动；请对照当前打包元数据核实。
- [推断]「低活跃 / 吃老本」是从发布日期（2023 的 v0.7.0、2024 的 push）推断，而非维护者声明。
- [未验证] gevent 的 import 顺序与 monkeypatching 冲突在 README 与 gevent 通行行为中有描述；在你具体栈里的精确失败模式因环境而异，这里未验证。
- [推断] 单一维护者 bus-factor 是从 User 类型 owner 与贡献者历史推断，而非治理文档。
