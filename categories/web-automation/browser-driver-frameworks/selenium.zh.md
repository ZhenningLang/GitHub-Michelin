---
name: Selenium
slug: selenium
repo: https://github.com/SeleniumHQ/selenium
category: browser-driver-frameworks
tags: [browser-automation, webdriver, w3c, cross-browser, end-to-end-testing, grid, selenium-ide, java, python, multi-language]
language: Java
license: Apache-2.0
maturity: v4.45.0 (2026-06), active; ~34.2k stars (as of 2026-06)
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-06-29T08:45:44Z
  default_branch: trunk
  default_branch_sha: ffb4528fe77b4bc0a054f79c462a665b425833c8
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:12:09Z
  overall: A
  overall_score: 4.0
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 21.8
        qualifying_issues: 40
        band: default
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: nuget.org
        canonical_package: selenium.support
        dependent_repos_count: 0
        downloads_last_month: 128246077
        graph_tier: E
        volume_tier: A
        cross_check_divergence: null
        homebrew_installs_90d: 1019
        homebrew_tier: B
        release_downloads: 33478704
        release_assets: 684
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4999
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 39
        top1_share: 0.354
        top3_share: 0.603
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Selenium

历史悠久的跨浏览器自动化总项目，通过 **W3C WebDriver** 协议工作：一套语言中立的编程接口（Java/Python/JS/C#/Ruby 等），外加用于分布式执行的 **Grid** 和录制回放的 **Selenium IDE**。

![selenium — 健康度雷达](../../../assets/health/selenium.zh.svg)

## 何时使用

你是某家企业的 QA 或 SDET 工程师，公司交付的 Web 应用，客户会用 Chrome、Firefox、Edge、Safari 各种浏览器打开——「在 Chrome 上能跑」根本不算「做完」。你需要一套端到端 UI 回归测试：用*同一份*测试逻辑驱动支持矩阵里的每一种浏览器，在 CI 里每次合并都跑，并且分散到一组机器上并行执行，让整套用例几分钟跑完而不是耗一个钟头。你的团队已经用 Java 写代码（有几个服务用 Python），所以你想要一套自动化 API，两边都能调，不必再各学一个语言专属工具。

于是你选 **Selenium WebDriver**。你照着 WebDriver API 把测试写一遍，同一份代码就能驱动 ChromeDriver、GeckoDriver、EdgeDriver 或 SafariDriver——因为它们都实现了 W3C WebDriver 规范：真实浏览器、真实渲染，最接近真实用户的那种。要扩规模就架起 **Selenium Grid**：一个 hub/node（或完全分布式）拓扑，把你的测试调度到许多浏览器实例和 OS 组合上并行跑，也支持 Docker 化的 node。给团队里不写代码的人，**Selenium IDE** 能在浏览器里录制一段流程，再导出成某个语言绑定作为起点。因为 WebDriver 协议是 W3C 标准、生态极广（BrowserStack/Sauce Labs 这类云 Grid、几乎所有 CI 集成、堆成山的 Stack Overflow 答案），当*跨浏览器广度*和*语言自由*是硬需求时，Selenium 就是那个稳妥、无处不在的默认选项。

## 何时不用

- **你只针对一种（Chromium）浏览器，又想要现代化的开发体验。** 对单浏览器项目、想要开箱即用的自动等待、网络拦截和更顺手的调试体验，Playwright 或 Cypress 就是更舒服；相比之下 Selenium 显得更底层、更啰嗦。
- **你指望测试不写等待就「能跑」。** Selenium 不像 Playwright/Cypress 那样对元素/网络自动等待；除非你处处用显式/期望条件等待去管住它，否则用例出了名地容易**抖动（flaky）**。这是日常里最大的一笔成本。
- **你想要 AI/agent 驱动的自然语言自动化。** Selenium 是选择器加代码驱动的，不是让 LLM 按意图操作页面。要 NL/agent 控制，请用页面内 GUI agent 如 [page-agent](../agent-browser-tools/page-agent.zh.md)，或 CLI/守护进程式的 agent browser 如 [Agent Browser](../agent-browser-tools/agent-browser.zh.md)。
- **你想要轻量的 CDP 调试/测量工具。** 要做 Chrome 原生的性能 trace、网络/控制台检查、堆快照并由 agent 驱动，像 [Chrome DevTools MCP](../agent-browser-tools/chrome-devtools-mcp.zh.md) 这类 CDP 工具，比架起 WebDriver + Grid 轻得多。
- **你不想运维基础设施。** 规模化的 Grid 是真正的运维活——一个 hub/distributor、一堆 node、浏览器与驱动的版本匹配、排队、node 健康检查都得管（或者你花钱买云 Grid）。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Playwright](../playwright-family/playwright.zh.md) | ✅ | 当现代自动等待、trace，以及一套代码覆盖 Chromium/Firefox/WebKit 比 WebDriver 标准更重要时，选 Playwright。 | 现代跨浏览器（Chromium/Firefox/WebKit）自动化，带自动等待、网络拦截、tracing 和顺手的 API；单一代码库的开发体验好得多，但生态更新更窄，也不是 Selenium 所锚定的 W3C WebDriver 标准。 |
| Cypress | 未收录 | 做 Web 应用、接受只用 JS/TS，且最看重开发者体验时，选 Cypress。 | 对开发者友好的浏览器内 E2E，带时间旅行调试和自动重试；Web 应用开发体验极佳，但历来偏 Chromium，运行在浏览器事件循环内（多标签/跨域有架构限制），且只支持 JS/TS。 |
| [Puppeteer](puppeteer.zh.md) | ✅ | 需要 Node.js 里的底层 Chrome/CDP 脚本能力，而不是可移植跨浏览器覆盖时，选 Puppeteer。 | 更底层的 Chrome/CDP 自动化库（Node.js）；做 Chrome 脚本/抓取很好，但单引擎，不是跨浏览器、多语言的 WebDriver 框架。 |
| [Agent Browser](../agent-browser-tools/agent-browser.zh.md) | ✅ | 任务是让 AI agent 通过稳定 a11y 树 ref 控制页面时，选 Agent Browser。 | Rust 写的 CLI/守护进程，通过 CDP 驱动 Chrome 给 AI agent 用，带稳定的 a11y 树 ref；是 agent 原语，不是跨浏览器测试框架——活儿不同。 |
| [Chrome DevTools MCP](../agent-browser-tools/chrome-devtools-mcp.zh.md) | ✅ | 需要把 Chrome trace、网络、控制台和堆诊断暴露给 agent 时，选 Chrome DevTools MCP。 | 把 Chrome DevTools（trace、网络、堆）通过 MCP 暴露给 agent 的服务器；调试/测量深度强但只在 Chrome 上，不是可移植的跨浏览器测试自动化。 |

## 技术栈

- **核心协议：** W3C WebDriver——一套语言与浏览器中立的线协议；Selenium 同时提供客户端绑定和（历史上的）服务端参考组件。
- **实现语言：** 项目自身覆盖 Java、Python、Ruby、C#、JavaScript，仓库里还有 Rust/C++；WebDriver 客户端**绑定**面向 Java/Python/JS/C#/Ruby（以及社区移植版）。
- **组件：** Selenium WebDriver（API）、Selenium Grid（分布式/并行执行——standalone、hub-node 或完全分布式角色）、Selenium IDE（浏览器录制回放扩展）。
- **浏览器驱动：** 委托给各浏览器的驱动可执行文件——ChromeDriver、GeckoDriver（Firefox）、msedgedriver（Edge）、SafariDriver——各自实现 WebDriver 规范；Selenium Manager 负责解析/下载匹配的驱动。

## 依赖

- **每个目标都要一个真实浏览器 + 对应的 WebDriver 驱动**（Chrome+ChromeDriver、Firefox+GeckoDriver、Edge+msedgedriver、Safari+SafariDriver）。Selenium Manager 可自动准备驱动。
- **你所选绑定的语言运行时**（Java 的 JDK、Python、Node.js、.NET 或 Ruby），外加一个测试运行器（JUnit/TestNG、pytest、Mocha 等）。
- **可选的 Selenium Grid**，若你需要分布式/并行运行——它是自己要部署的进程（常用官方 Docker 镜像），或者用托管云 Grid（BrowserStack/Sauce Labs/LambdaTest）。
- 它自身没有数据存储；状态就是它控制的那些浏览器会话。

## 运维难度

**中。** 单个本地 WebDriver 测试很容易：加上绑定依赖，让 Selenium Manager 取驱动，跑。成本随着让 Selenium 有价值的那些东西一起上升：让**浏览器与驱动版本保持一致**（浏览器自动更新时常见的故障源）、写并维护显式等待来对抗抖动，以及——最关键的——规模化地**运维 Grid**：distributor/router/session-map 角色、node 池、Docker/Kubernetes 部署、队列调优和健康监控。很多团队靠租用云 Grid 绕开 Grid 运维负担，用基础设施换按分钟计费的成本。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 12.6 小时，基于 38 个 qualifying issues/PRs。
- **维护（2026-06）** —— 最近推送在 2026-06，未归档，持续交付 v4.x 线（v4.45.0）；一个紧跟浏览器/WebDriver 目标演进、持续发版的项目，即**活跃**而非停滞滑行。`[推断]`
- **治理与 bus factor** —— 归属 **SeleniumHQ** 组织（`Organization` 所有），是历史悠久的社区/多贡献者项目，而非某一个人或单一厂商的产品；它所锚定的 W3C 标准 WebDriver 协议进一步降低了任何单一所有者依赖的风险。`[推断]`
- **年龄与 Lindy** —— 约 2013-01 创建，到 2026-06 约 13 岁且仍在积极发版：教科书式的**强 Lindy**下注——既长寿*又*仍活跃，叠加深厚的生态惯性（云 Grid、CI 集成、多年问答），使它成为稳妥默认项。`[推断]`
- **采用与生态** —— 自动化的 registry/dependent graph 把这一轴评为 E，但这个口径会低估分散在多语言绑定、浏览器驱动、托管 Grid 和 CI 集成里的 WebDriver 生态。人工阅读时应把 Selenium 视为深度扎根的生态，而不是只按包依赖图理解。`[推断]`
- **风险标记** —— Apache-2.0，未见 relicense / open-core 历史；实际风险在于**不写规范等待就抖动**和 **Grid 运维负担**，而非项目可持续性。`[未验证]`

## 存疑（未验证）

- [未验证] 截至 2026-06，约 34.2k GitHub star，v4.45.0（约 2026-06-16 发布）；star 数和版本号对时间敏感且会漂移——仅供参考，请对照仓库重核。
- [未验证] 官方维护的语言绑定（Java/Python/JS/C#/Ruby）与社区移植版的确切集合，以及仓库里哪些语言（Rust/C++）是发行组件还是内部用途，来自 README/仓库表述，随版本变动。
- [推断]「不写显式等待就抖动」以及相对 Playwright/Cypress 的开发体验差距，是社区广泛共识和架构推断，并非本页的实测基准。
- [推断] Selenium Grid 的角色/拓扑细节（standalone / hub-node / 分布式）是从项目自己的文档表述归纳而来；设计部署前请核实当前的 Grid 架构。
- [未验证] 对比里的替代品（Playwright、Cypress、Puppeteer）反映的是大致定位，而非头对头实跑；相对取舍属判断。
