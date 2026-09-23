---
name: AnyProxy
slug: anyproxy
repo: https://github.com/alibaba/anyproxy
category: debugging-proxy
tags: [proxy, mitm, http, https, nodejs, debugging, traffic-capture]
language: JavaScript
license: Apache-2.0
maturity: v4.x (npm 4.1.3), master frozen since 2020-06, coasting, ~7.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2023-03-06T17:20:04Z
  default_branch: master
  default_branch_sha: b93f948107b956e07c7b68faeff0c777a1f50486
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:06:11Z
  overall: C
  overall_score: 1.5
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
        last_commit_age_days: 2287
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: anyproxy
        dependent_repos_count: 238
        downloads_last_month: 7372
        graph_tier: C
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 4425
        last_commit_age_days: 2287
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

# AnyProxy

一个用 Node.js 写的完全可配置 HTTP/HTTPS 中间人代理：把你机器（或移动设备）的流量路由穿过它，在 web UI 里检视、录制，并用 JS 规则文件改写请求/响应。阿里背书——但 master 分支自 2020 年中起就没动过。

![anyproxy — 健康度雷达](../../assets/health/anyproxy.zh.svg)

## 何时使用

你是移动或 Web 工程师，在调试一个 app 的网络层，需要*看到并改写*它发出的内容——检视实时 HTTP/HTTPS 流量、mock 一个慢的或坏的后端响应、或者在服务端改动上线前翻转某个请求的 path/header 来测边界情况。你把手机或浏览器指向 AnyProxy、信任它生成的根 CA 以便解密 HTTPS，再打开它的 web UI（默认 8002 端口）看请求流过——它甚至带个二维码助手让手机指向代理。要改流量，你写一个小 JS 规则文件，用 generator/Promise 钩子（`*beforeSendRequest`、`*beforeSendResponse`、`*beforeDealHttpsRequest`）返回修改后的请求/响应细节；你还能限带宽或把会话录进内嵌数据存储。安装是 `npm install -g anyproxy`。

当你特别想要一个*可脚本化*的 Node.js 代理、其规则就是你已熟悉的纯 JavaScript 时（相对 Charles 这类 GUI 工具），它是个合理选择。但先掂量它的陈旧程度（见下）。

## 何时不用

- **别为 2026 年的新工作选它——master 已冻结。** 最后一次真实 master 提交是 2020-06（"release 4.1.3"）；GitHub 最新 release tag 只到 v4.0.5，没有 v4.1.3 tag。约 6 年无代码 release，248 个 open issue。阿里背书没有转化为维护。[推断]
- **存在更活跃维护的 Node.js 替代。** [whistle](whistle.zh.md) 是同一细分里活跃开发的 Node.js MITM 调试代理——新搭建优先用它。
- **在现代系统上要预期证书/运行时摩擦。** 它面向 Node 6 时代（`engines: node >=6.0.0`），依赖已弃用的 `request` 库；在 Node 18/20+ 以及证书信任和 TLS 有效期规则更严的 macOS/iOS 上，老的 MITM-CA 代理常会崩。当前 OS/Node 上的兼容性在你实测前当作未验证。[推断]
- **不用于生产流量。** 它设计上就是调试/MITM 工具——录制和限速带来开销，且把真实流量经 MITM 路由本身是安全负担。
- **来源含糊。** npm 发布的是 4.1.3（外加一个 4.2.0-beta），而 GitHub 最新 release 是 v4.0.5 且无对应 tag——已发布的 4.1.x 线从未作为 GitHub release 切出，这让你难以审计自己实际装的是什么。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [whistle](whistle.zh.md) | ✅ | 需要活跃维护的 Node.js MITM 代理默认选择时，选 whistle。 | 活跃维护的 Node.js MITM 调试代理；规则系统更丰富、持续发布——同细分里新工作的更优默认。 |
| [mitmproxy](mitmproxy.zh.md) | ✅ | Python 脚本能力和 CLI/TUI/web UI 比 Node.js 规则更重要时，选 mitmproxy。 | Python，活跃维护，强脚本 + TUI/web UI；若你不绑死 Node.js，这是可编程 MITM 代理的首选。 |
| Charles / Fiddler | 未收录 | 成熟桌面 GUI 调试体验是优先项时，选 Charles 或 Fiddler。 | 成熟的商业/免费 GUI 调试代理；UX 打磨好但闭源，不像 AnyProxy 规则文件那样能用 JS 脚本化。 |
| Proxyman | 未收录 | 现代 macOS/跨平台 GUI 打磨最重要时，选 Proxyman。 | 现代 macOS/跨平台 GUI 代理；UX 很好，freemium，不是你内嵌的 Node.js 库。 |

## 技术栈

- **语言：** Node.js（`engines: node >=6.0.0`——非常老的底线）。
- **服务 / UI：** `express`、`ws`、`body-parser`、`compression`；web UI 用 React 15 / antd 2 / redux / webpack 3（都落后好几个大版本）。
- **MITM / 证书：** `node-easy-cert`，从自己的根 CA 生成并签发各 host 证书（`bin/anyproxy-ca`、`lib/certMgr.js`）。
- **杂项：** `request`（2020 起已弃用）、`stream-throttle`（带宽）、`nedb`（内嵌录制存储）、`brotli` / `iconv-lite`；异步用 `co` / `thunkify` / `async@~0.9` generator（async-await 之前的写法）。
- **规则 API：** JS 规则文件——`*beforeSendRequest`、`*beforeSendResponse`、`*beforeDealHttpsRequest` 返回修改后的 `requestDetail` / `responseDetail`；样例在 `rule_sample/`。

## 依赖

- **运行时：** Node.js（为 Node 6 时代构建；现代 Node 兼容性未验证——见存疑）。
- **CA 证书：** 你必须生成并信任它的根 CA（`anyproxy-ca`）才能 MITM HTTPS——一个设备/OS 的信任步骤。
- **存储：** 录制用内嵌 `nedb`；不需要外部数据库或服务。
- **客户端配置：** 你要抓流量的设备/浏览器必须指向代理（HTTP 代理设置，或在移动端扫二维码助手）。

## 运维难度

**做随手调试属于低，但有注意事项。** `npm install -g anyproxy`、用 `anyproxy-ca` 配好证书，再跑 `anyproxy` 并把客户端指过来——没有数据存储或集群要运维。真正的难点由年龄驱动：在当前 Node 运行时上装一个带弃用 `request` 依赖的 Node 6 时代包，以及在证书有效期和 TLS 规则更严的现代 macOS/iOS 上让生成的 MITM CA 被信任，两者都可能以无人会修的方式失败。它是个本地开发者工具，不是你会跑在生产里的服务。[推断]

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 吃老本/实质废弃：master 代码自 2020-06 冻结，最新 GitHub release v4.0.5，248 个 open issue。2023-03 的 `pushed_at` 反映的是推到陈旧 feature 分支（20 个分支：`typescript`、`optimze_memory_usage`、`feat/websocket_hooks`、若干 `fix/*`）、从未合进 master 的提交——不是真维护。[推断]
- **治理 / 背书。** 归属阿里 GitHub 组织，但实际上严重单作者（`ottomao` 约 168 次提交，远超其余）。大厂所有**并未**意味着活跃维护——提醒：组织背书 ≠ 活着。
- **年龄 × Lindy。** 创建于 2014（约 12 年）——老，但**当前不活跃**，所以 Lindy 不适用：有寿命无活力不是安全信号。[推断]
- **采用度。** 约 7.9k star，历史上在移动流量调试里用得广；生态势头已转向 whistle/mitmproxy/Proxyman。
- **风险标记。** 依赖腐烂（弃用的 `request`、Node 6 底线、React 15/webpack 3 的 UI）、npm 与 GitHub 的版本不一致（发布了 4.1.3 却无对应 tag），以及内部被悄悄弃用的疑虑。Apache-2.0，未发现 relicense 历史。[推断]

## 存疑（未验证）

- [推断] 2023-03 的 `pushed_at` 反映的是非 master 的 feature 分支推送，不是 master 维护；master HEAD 是 2020-06 的 "release 4.1.3" 提交。
- [推断] 现代 OS/Node 上的证书/Node 兼容性摩擦，是从 Node 6 底线 + 弃用的 `request` + 更严的现代证书/TLS 规则推理而来——未在当前系统上实测。
- [推断] “在阿里内部被悄悄弃用”是从冻结的 master + release 落差推断，不是确认的说法。
- [未验证] npm `latest` 4.1.3 与 GitHub release v4.0.5（无 v4.1.3 tag）；已发布 4.1.x 线的来源未独立审计。
- [未验证] 截至 2026-06 约 7.9k star；star 数对时间敏感，仅供参考。
