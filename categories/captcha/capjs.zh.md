---
name: Cap
slug: capjs
repo: https://github.com/tiagozip/cap
category: captcha
tags: [captcha, proof-of-work, bot-detection, anti-spam, self-hosted, privacy]
language: JavaScript
license: Apache-2.0
maturity: standalone v3.1.5, capjs-core v0.1.1, active (2026-06)
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-21T11:12:11Z
  default_branch: main
  default_branch_sha: a7f6c15b15ee1a60b9e79b9e85ff57c1beee4b61
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T03:02:59Z
  overall: C
  overall_score: 2.4
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 9.6
        qualifying_issues: 12
        band: default
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: cap-widget
        dependent_repos_count: 0
        downloads_last_month: 18143
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 619
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 19
        top1_share: 0.889
        top3_share: 0.927
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Cap

一个轻量、可自托管的 reCAPTCHA/hCaptcha/Turnstile 替代品：用一道无感的工作量证明（proof-of-work，客户端做 SHA-256 nonce 搜索，跑在 Rust→WASM worker 里）外加可选的 JavaScript instrumentation 检测来拦住某个动作，发放一个可兑换 token 让你的服务端校验——自托管时没有图片验证，也不向第三方发任何网络请求。

![capjs — 健康度雷达](../../assets/health/capjs.zh.svg)

## 何时使用

你是后端或全栈工程师，手上有一个注册表单、一个联系页接口，或一条公开 API 路由，老被机器人刷——刷假账号、刷垃圾提交、撞库。你不想嵌 reCAPTCHA 或 Turnstile，因为那会把用户数据和一段脚本送到 Google/Cloudflare，你也不想让真人去点红绿灯方格图。你希望把滥用的成本压到**机器**身上（花 CPU 去解题），而不是耗用户的耐心和隐私。

Cap 正好适合这个场景。你在受保护的表单上放一个 `<cap-widget>`（也可以走编程式调用，或用无感的 floating 模式），服务端把 `capjs-core`——一个**无状态、自带存储**的生成/校验器——接进你的 Node 或 Bun handler。widget 拉一道挑战，让访客的 CPU 在并行 WASM worker 里花几百毫秒去凑 SHA-256 前缀，然后提交解；你的服务端重新生成同样的挑战、校验通过后发回一个 token，你在处理请求前用 `validateToken()` 检查它。如果你完全不想碰这个库，就跑 **Standalone** 的 Docker 镜像（`tiago2/cap:latest`），把应用指向它那个兼容 reCAPTCHA 的 `/siteverify` 接口，并在内置面板里管理 site key。

## 何时不用

- **你要挡住一个有钱有决心的攻击者或打码平台。** 工作量证明抬高的是滥用的*成本*，并不能*打败*一个愿意烧 CPU 或雇真人的求解者。它是摩擦，不是墙——高价值目标仍需限流、风控评分和服务端校验。
- **你想要一道全站 / 反向代理级的机器人墙。** Cap 守的是*具体动作*（表单、接口），放正常浏览通行。要在代理层把整站对爬虫封死，Anubis（`未收录`）才是对口工具；Cap 是按动作粒度的。
- **工作量证明对你用户的设备是硬伤。** PoW 会消耗客户端 CPU/电量；在低端手机上或难度调高时会增加延迟、耗电。如果你不能接受任何客户端计算，无感的行为/风险评分服务（Turnstile）是另一种取舍。
- **你要的是全托管、有 SLA、零运维的服务。** 自托管意味着*你*来跑服务（或 Standalone 容器 + Redis）、轮换密钥、自己扛可用性。没有厂商可呼叫。
- **你想把 CAPTCHA 当成一个有审计支持的法务/合规无障碍勾选项。** 这是个年轻的开源项目（`capjs-core` v0.1.1），不是带支持合同的企业级供应商。
- **你指望开箱即用的强机器人*分类*能力。** Cap 的 instrumentation 层增加了一些信号，但它不是 ML 风控引擎；它不会像商业服务宣称的那样去给访客打“有多像真人”的分。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| reCAPTCHA (Google) | 未收录 | 想要托管、免费、风控评分强，且能接受 Google 作为第三方依赖时，选 reCAPTCHA。 | 它会把用户数据送到 Google、要点图，且不可自托管。Cap 把流程留在你自己的基础设施里，但没有 Google 量级的风控信号。 |
| hCaptcha | 未收录 | 托管图片挑战和站长分成生态比自托管更重要时，选 hCaptcha。 | 它仍是第三方、基于图片。Cap 的 widget 小得多，可自托管且无外部请求。 |
| Cloudflare Turnstile | 未收录 | 想要托管无感检查、客户端不做 PoW，并借 Cloudflare 网络信号时，选 Turnstile。 | 它是托管在 Cloudflare 上的依赖；Cap 用自托管运维换掉这套风控网络。 |
| Altcha | 未收录 | 想要最接近的开源 PoW widget，且能自己组装服务端和面板时，选 Altcha。 | Altcha 开源版只有 PoW；ML 检测是付费 Sentinel 产品。Cap 打包了 instrumentation 和带面板的 Standalone 服务。 |
| mCaptcha | 未收录 | 想要自托管 Rust PoW CAPTCHA，并需要它自己的限流式难度模型时，选 mCaptcha。 | 目标重叠，但技术栈与手感不同。 |
| FriendlyCaptcha | 未收录 | 想要注重隐私的 PoW，但能接受维护中的产品是托管商业服务时，选 FriendlyCaptcha。 | Cap 则是完全开源、自托管。 |
| Anubis | 未收录 | 需要反向代理或全站级 PoW 网关来挡爬虫和 AI crawler 时，选 Anubis。 | 作用域不同：入口闸门 vs 按动作挑战。两者互补而非互替。 |

## 技术栈

- **Widget：** JavaScript web component（`<cap-widget>`），gzip 后约 20 KB、运行时零依赖；支持 normal、floating（无感）和编程式三种模式。
- **求解器：** 挑战在客户端通过反复对 salt+nonce 做 **SHA-256** 直到 hash 命中目标前缀来求解；热循环是 **Rust 编译成 WebAssembly**（`@cap.js/wasm`），并在多个 **Web Worker** 里并行跑。
- **服务端库（`capjs-core`）：** 面向 Node.js 和 Bun 的无状态 TypeScript/ESM 模块，负责生成挑战、兑换解（`redeemChallenge()`）、校验 token（`validateToken()`）。它定义了挑战与 token 的*可插拔存储接口*（`store/read/delete/deleteExpired`）——存储用 Postgres、内存 `state` 对象或任何后端都行。
- **Standalone 服务：** 基于 **Bun** + **Elysia**，自带面板、兼容 reCAPTCHA 的 `/siteverify` 接口、多 site key 支持，可选 MaxMind GeoIP 与无头浏览器检测。
- **Instrumentation 挑战：** 可选，在沙箱 iframe 中解压并执行，与 PoW 一起构成第二道校验层。

## 依赖

- **库路径（`capjs-core`）：** Node.js 或 Bun 运行时。*不自带存储 / 文件系统*——存储后端由你提供（如 Postgres），或用内存 `state` 对象。构建期依赖 `esbuild`（可选 `javascript-obfuscator`）。
- **Standalone 路径：** Docker（镜像 `tiago2/cap:latest`）加一个 **Redis 兼容存储**（官方 `docker compose` 用 **Valkey**，经 `REDIS_URL` 连接）。配置走环境变量：`ADMIN_KEY`（面板登录，建议 32+ 字符）、`REDIS_URL`；默认端口 `3000`。
- **客户端：** 支持 WebAssembly + Web Workers 的现代浏览器（实际上等于所有当前浏览器）。

## 运维难度

**库路径低，Standalone 低到中。** 在已有的 Node/Bun 服务里用 `capjs-core` 基本就是接线活：实现（或复用）一个存储适配器，在 handler 之前加一次校验调用，再嵌上 widget。没有独立服务要看护。**Standalone** 路线则多出一个容器加一个 Redis/Valkey 实例要运行和备份、一个 `ADMIN_KEY` secret 要管理、跨站点的密钥轮换——是标准的小型服务运维，但比“插一段 script”要重。真正需要判断的是*难度调参*：调太低，PoW 几乎挡不住机器人；调太高，会拖累正常用户的设备。预期要按接口逐个调参、盯着滥用指标，而不是一劳永逸。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 5.5 小时，基于 37 个 qualifying issues/PRs。
- **维护（截至 2026-06）：** 最后 push 在 2026-06，未归档，活跃。Standalone 服务已到看起来成熟的 v3.1.5，而库（`capjs-core`）还在 v0.1.x，所以*库*这一半的 API 面更不稳定。[推断]
- **治理与 bus factor：** `User` 所有（tiagozip），单维护者。约 7k star 下 bus-factor 暴露真实存在，但比 4 万 star 的单人项目更可控——只是背后没有基金会或厂商，延续性押在一位作者身上。[推断]
- **年龄与 Lindy 判断：** 建于 2025-01，约 1.5 年——**年轻；Lindy 尚未建立**。它过了头一个月的「蒸汽」阶段，但还没跨年证明自己；pre-1.0 的 `capjs-core` 进一步说明「预期 API 变动、请锁版本」。[推断]
- **风险标记：** Apache-2.0，但 GitHub API 在 LICENSE 头部报 `NOASSERTION`（见存疑），自动 SPDX 扫描器可能会标记——是 license 的表层瑕疵，而非 relicense。安全上它是摩擦（工作量证明），不是经过加固的反滥用引擎；自托管也意味着可用性与难度调参都归你。[推断]

## 存疑（未验证）

- [未验证] 仓库活跃度与所谓热度（2026-06 约 7k GitHub stars）——GitHub stars 不可靠且对日期敏感，仅供参考。
- [未验证] “约 20 KB / 比 hCaptcha 小 250 倍”以及与 Altcha（约 34 KB）的体积对比，是项目自己 README/docs 里的营销数字，本页未独立复测。
- [未验证] 对比表里 Cap-vs-Altcha / vs-Anubis / vs-Turnstile 的定位取自 Cap 自己的文档；竞品当前能力（如 Altcha Sentinel、Turnstile 内部机制）未独立复核。
- [推断] License 判为 Apache-2.0：仓库 LICENSE 文件是逐字的 Apache 2.0 文本，但 GitHub API 报 `NOASSERTION`（文件头部非标准），自动 SPDX 检测器可能会标记。
- [未验证] 对真实打码服务 / 打码平台的实际抵抗效果本页未测；工作量证明抬高成本但可被足够算力或付费人工求解攻破。
- [推断] `capjs-core` 处于 v0.1.x，说明是年轻的、pre-1.0 的库面；API（存储接口、`validateToken` 选项）在版本间可能变化——请锁定版本。
- [未验证] Standalone 里的 MaxMind GeoIP 与无头浏览器检测在文档中被描述为可选特性，其确切行为/准确度未实测。
