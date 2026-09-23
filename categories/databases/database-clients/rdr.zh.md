---
name: RDR
slug: rdr
repo: https://github.com/xueqiu/rdr
category: database-clients
tags: [redis, rdb, memory-analysis, offline, cli, profiling]
language: JavaScript
license: Apache-2.0
maturity: v0.0.1 (only tagged release 2019), low activity, ~1.2k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2024-04-03T02:31:46Z
  default_branch: master
  default_branch_sha: d2ec33ef69107a21148c29a3f609162a75f58854
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:04:55Z
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
        last_commit_age_days: 2261
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: proxy.golang.org
        canonical_package: github.com/xueqiu/rdr
        dependent_repos_count: 1200
        downloads_last_month: null
        graph_tier: B
        volume_tier: "?"
        cross_check_divergence: null
        release_downloads: 26759
        release_assets: 3
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3491
        last_commit_age_days: 2261
        cohort: tool
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

# RDR

一个快速的离线 Redis RDB 文件解析器（尽管仓库标注语言为 JavaScript，核心其实是 Go 写的），用来揭示哪些 key 和 key 前缀在吃内存——`rdr show` 在本地端口起一个 HTML 内存报告，`rdr keys` 把所有 key 导出。

![rdr — 健康度雷达](../../../assets/health/rdr.zh.svg)

## 何时使用

你是某个 Redis 集群的值班工程师，凌晨两点它撞上了 `maxmemory` 告警，你需要在决定淘汰、分片还是叫人之前，先搞清楚到底是*哪些* key 在作怪。你不想对着一个高负载的生产实例逐个 key 跑 `MEMORY USAGE`，而 `redis-cli --bigkeys` 又只是采样。于是你从磁盘上抓最近一份 RDB 快照（或在从库上 `BGSAVE`），拷到工作机上跑 `rdr show dump.rdb`。它离线解析这个文件——不连活实例、不给生产加负载——然后打开一个浏览器报告，按 key 前缀和数据类型把内存拆开，于是你一眼看到 `session:*` 是 4 GB 没人管的 hash。要做一次性的「这个 RDB 里到底有什么」审计，`rdr keys` 会把完整 key 列表流式打到 stdout。

你专门在分析必须**离线且快**时选它：作者的卖点是它能在几分钟内啃完一个数 GB 的 RDB，而这在替代品（更老的 Python `redis-rdb-tools`）对大 dump 明显更慢时很重要。[未验证]

## 何时不用

- **你需要在线、持续的监控。** RDR 分析的是某一时刻的静态 RDB 快照。要做持续的内存看板，你想要的是 Redis exporter + Prometheus/Grafana，而不是一次性的文件解析器。
- **你拿不出 RDB 文件。** 如果持久化被关掉了（`save ""`）且你又不能 `BGSAVE`，那 RDR 就没东西可读。它不与活实例通信。
- **你需要精确到字节的核算。** README 自己就标注 `show` 的内存数字是**近似值**——适合找出大 key，不适合用来精确算容量账。
- **你跑的是非常新的 Redis/RDB 版本。** RDB 是带版本的二进制格式；一个针对老版本写的解析器可能读不懂新版 Redis 里新增的编码或类型——请先核实它能干净解析你的 RDB 版本。[推断]
- **你想要一个在积极维护、有支持渠道的工具。** 唯一的 tag 发布是 v0.0.1（2019），仓库最后一次 push 在 2024 年；把它当成一个好用但在吃老本的小工具，而非有支持通道的产品。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| redis-rdb-tools（sripathikrishnan） | 未收录 | 需要最早的 Python RDB 解析/内存分析器时，选 redis-rdb-tools。 | 最早的 Python RDB 解析/内存分析器；输出格式更多、支持 CSV 导出，但对大 dump 慢得多，且本身基本已无人维护。 |
| `redis-cli --bigkeys` / `--memkeys` | 未收录 | 需要 Redis 内置、无需 dump 文件的在线采样时，选 redis-cli bigkeys/memkeys。 | Redis 内置，在线跑、无需文件，但只*采样*且会给服务器加负载；没有按前缀的拆分，也没有报告 UI。 |
| RedisInsight（Redis Ltd.） | 未收录 | 需要完整 GUI 和在线内存分析时，选 RedisInsight。 | 带完整 GUI 和在线内存分析页；功能丰富得多，但它是连活实例的重型桌面应用，不是离线文件解析器。 |
| `MEMORY USAGE` / `MEMORY DOCTOR` | 未收录 | 需要 live server 上按 key 或实例自省时，选原生 MEMORY 命令。 | 在线服务器上做按 key/实例内存自省的原生命令；单 key 精确，但你得先知道该问哪些 key。 |

## 技术栈

- **语言：** Go——编译成 Linux、macOS、Windows 的独立二进制（GitHub 标的「JavaScript」语言似乎是打包进去的报告前端资源所致，而非核心；README 和二进制描述的都是一个 Go 程序）。
- **输入：** Redis RDB dump 文件（磁盘上的二进制快照格式）。
- **输出：** `rdr show` 内嵌一个 HTTP 服务渲染 HTML 内存报告（默认 `:8080`）；`rdr keys` 把 key 列表打到 stdout。

## 依赖

- **运行时：** 除了预编译二进制外没有——不连 Redis、不需要语言运行时、不需要外部服务。
- **输入产物：** 你自己提供的 Redis RDB 文件（来自磁盘、`BGSAVE` 或某个从库的 dump）。
- **构建：** 若从源码编译而非用 release 二进制，需要 Go 工具链。

## 运维难度

**低。** 它就是一个你在工作机上对着文件跑的单一二进制——下载、`chmod +x`、运行、打开 `localhost:8080`。没有要部署的服务、没有数据存储、没有配置。唯一需要在意的运维点是流程性的：安全地产出 RDB（去快照从库而非阻塞主库）、把一份可能很大且敏感的 dump 拷到你跑 RDR 的地方，并记得报告端口绑在本地。因为它离线，所以对生产 Redis 零负载——这正是事故期间相比在线 `--bigkeys` 扫描更该选它的理由。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 仓库最后 push 于 2024-04；唯一的 tag 发布是 **v0.0.1（2019）**。未归档，但实质上在**吃老本 / 低活跃**——可以拿来用，但别指望及时修 bug 或跟进新 RDB 版本。[未验证]
- **治理 / bus factor。** 归 **雪球（Xueqiu）** 组织所有（一家中国投资社区公司），但贡献集中在少数几位作者——这是「内部工具开源」典型的薄 bus factor。[推断]
- **年龄与 Lindy 判断。** 2017 年创建，约 9 岁，但**并未在积极发布**——这里的年龄*不是*强 Lindy 信号，因为 Lindy 要求又老**又**仍活跃；这是又老又安静。[推断]
- **采用度。** 约 1.2k star / 311 fork 说明它在 Redis 运维圈作为事故工具有真实使用，但没有发布节奏或活跃的 issue 处理可依赖。[未验证]
- **风险标记。** Apache-2.0，宽松，未发现 relicense 历史。真正的风险是它对不断演进的 RDB 格式版本的滞后，而非许可。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 1.2k star / 311 fork——star/fork 数对时间敏感，仅供参考。
- [未验证] 「5GB RDB 约 2 分钟」/「比 redis-rdb-tools 快得多」是作者 README 的表述，本页未独立基准测试。
- [推断] 实现语言是 Go（依据二进制与 README），尽管 GitHub 把「JavaScript」报成首要语言——很可能是打包的 web 报告资源造成的假象。
- [推断] 与近期 Redis 版本的 RDB 格式版本兼容性未经核实；一个 v0.0.1/2019 年份的解析器可能处理不了新版 Redis 新增的编码。
- [未验证] `rdr` 是否能处理 Redis 分叉（KeyDB、Valkey、Dragonfly）产出的 RDB，未确认。
