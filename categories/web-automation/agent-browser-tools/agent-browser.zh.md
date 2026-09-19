---
name: Agent Browser
slug: agent-browser
repo: https://github.com/vercel-labs/agent-browser
category: agent-browser-tools
tags: [browser-automation, cli, rust, cdp, mcp, accessibility-tree, agent-tooling, headless, snapshot-refs, chrome]
language: Rust
license: Apache-2.0
maturity: v0.31.0 (2026-06-25); active, Vercel Labs; CDP-based Rust daemon + CLI
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-26T17:22:26Z
  default_branch: main
  default_branch_sha: ed2e10598c9064aecfaeb7cf21b540684db4be2c
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:55:59Z
  overall: B
  overall_score: 3.0
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 7
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 118.9
        qualifying_issues: 13
        band: relaxed_solo
        window_offset_days: 12
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: agent-browser
        dependent_repos_count: 0
        downloads_last_month: 2005864
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 2.17
    longevity:
      grade: D
      raw:
        repo_age_days: 173
        last_commit_age_days: 7
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 96
        top1_share: 0.67
        top3_share: 0.766
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

# Agent Browser

来自 Vercel Labs 的原生 Rust CLI + 守护进程，通过 CDP 直接驱动一个真实 Chrome 供 AI agent 使用：每次 `snapshot` 都把可访问性树（accessibility tree）连同稳定的元素引用（`@e1`、`@e2`）交给模型，于是 agent 操作 `@e1` 而不必去写一改 markup 就失效的脆弱 CSS 选择器。

![agent-browser — 健康度雷达](../../../assets/health/agent-browser.zh.svg)

## 何时使用

你在做一个 coding agent，或一套靠 shell 驱动的自动化，需要操作真实网站——登录后台、填多步表单、抓取表格、确认 deploy preview 渲染正常。你不想把 Node.js 的 Playwright 库塞进 agent 里，也不想让模型瞎编 CSS 选择器、markup 一变就崩。你要的是一条 agent 能直接 shell 调用的命令，外加一个 LLM 能稳定指向、推理的元素句柄。

你装上 `agent-browser`（npm、Homebrew 或 cargo），跑一次 `agent-browser install` 拉取 Chrome for Testing，之后循环就是：`agent-browser snapshot -i` 返回带 refs 的交互式可访问性树，模型挑出 `@e2`，你执行 `agent-browser click @e2` 或 `agent-browser fill @e3 "value"`。每条命令都支持 `--json` 供机器解析。由于守护进程在命令之间常驻，你不必为每个动作付一次浏览器启动开销——当 agent 连发几十步时很实用。如果你更想把它作为工具接进 Claude Code / Cursor 而非 shell 调用，`agent-browser mcp` 会把同样的操作通过 MCP 暴露出来。会话的 cookies/localStorage 自动保存与恢复，登录态的流程能跨次运行存活。

## 何时不用

- **你想要的是页面内、无后端的自然语言 copilot。** Agent Browser 从 CLI 驱动一个*外部* Chrome，它不在你应用现有的浏览器标签/会话里运行。要可嵌入页面内的 GUI agent，改用 [page-agent](page-agent.zh.md)。
- **你在写普通的 Node.js 测试/自动化库。** 它是 CLI + 守护进程，不是可 import 的 JS API。如果你的代码在 TypeScript 里、想要 `await page.click(...)`，原生 Playwright/Puppeteer 更合适。
- **你需要视觉优先 / 像素级精确交互。** 选择锚定在可访问性树而非截图上。Canvas/WebGL 界面、按像素坐标点击、或不在 a11y 树里的内容是弱项；标注截图在 Safari/WebDriver 后端尚不支持。
- **你需要开箱即用的托管云浏览器集群。** 它默认跑本地 Chrome；大规模并发/无头集群意味着要接上某个云厂商插件（Browserbase、Browser Use、Kernel 等）并自行运维。
- **跨引擎广度是硬要求。** 核心路径面向 Chrome over CDP；非 Chromium/Safari 覆盖是部分的（`[推断]` 功能对齐度落后于 Chrome 路径）。
- **成熟度 / 频繁变动。** 它处于 1.0 之前且迭代很快（每周多个 release），CLI 表面与配置可能在版本间变化——若要脚本化依赖请锁版本。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [page-agent](page-agent.zh.md) | ✅ | 需要复用用户浏览器会话的页内 JS GUI agent 时，选 page-agent。 | 页面内 JS GUI agent，复用用户自己的浏览器会话、无后端、自然语言指令。Agent Browser 则从 CLI/守护进程驱动外部 Chrome——更适合服务端/agent 自动化，更不适合嵌入活页面。 |
| [Chrome DevTools MCP](chrome-devtools-mcp.zh.md) | ✅ | 需要 Google 官方把 Chrome DevTools 暴露给 agent 的 MCP server 时，选 Chrome DevTools MCP。 | Google 出的 MCP server，把 Chrome DevTools 暴露给 agent——仅 MCP、官方 DevTools 面。Agent Browser 是 CLI 优先*且*自带 MCP 模式，带 snapshot-ref 人体工学和常驻 Rust 守护进程。 |
| [Cua](cua.zh.md) | ✅ | 需要驱动整个桌面/VM 的 computer-use 框架时，选 Cua。 | computer-use agent 框架，驱动整个桌面/VM（基于视觉）。Agent Browser 只管浏览器、基于 a11y 树——更轻更确定，但操作不了原生桌面应用。 |
| [Playwright](../playwright-family/playwright.zh.md) / Puppeteer | 部分已收录 | 需要成熟、代码优先的 Node 自动化库时，选 Playwright 或 Puppeteer。 | 成熟的 Node.js 自动化库，跨浏览器、API 丰富——但你要以代码方式 import 并自己写/维护选择器；Agent Browser 是 CLI，带 LLM 友好的 refs 且无每命令启动开销。 |
| [browser-use](browser-use.zh.md) | ✅ | 需要自带 LLM 循环的 Python 浏览器 agent 时，选 browser-use。 | Python，视觉+DOM 浏览器 agent，自带 LLM 循环。Agent Browser 是更底层的 Rust CLI 原语（agent 循环你自己提供），shell 调用更快、MCP 原生。 |

## 技术栈

- **语言：** Rust（原生 CLI 二进制 + 常驻守护进程）。
- **浏览器控制：** 直接走 Chrome DevTools Protocol（CDP）——“纯 Rust 守护进程”，运行路径里没有 Node.js 或 Playwright。
- **浏览器引擎：** Chrome for Testing（由 `agent-browser install` 自动下载）或自定义 `--executable-path`。
- **模型集成：** 内置 MCP server（`agent-browser mcp`）带类型化工具；每条命令都有 `--json` 输出供 shell/agent 解析。
- **选择模型：** 带稳定元素引用（`@e1`…）的可访问性树快照、稳定标签 ID（`t1`…）、带编号叠加的标注截图。
- **附加能力：** 网络拦截（route/mock/block）、会话持久化（cookies/localStorage）、React DevTools 检查、Web Vitals（LCP/CLS/TTFB/FCP/INP）、流式 WebSocket 视口预览、插件系统（基于 stdio 的进程外扩展）、云厂商插件（Browserbase、Browser Use、Kernel、AgentCore、Browserless）、经 Appium 的 iOS Simulator。

## 依赖

- **运行时：** 原生 `agent-browser` 二进制 + 一个 Chrome/Chromium 安装（由 `agent-browser install` 拉取，或经 `--executable-path` 指向）。运行命令本身*不*需要 Node.js。
- **安装：** `npm install -g agent-browser`、`brew install agent-browser`（macOS），或 `cargo install agent-browser`。
- **仅源码构建需要：** Node.js 24+、pnpm 11+ 和 Rust。
- **可选：** 一个支持 MCP 的客户端（Claude Code / Cursor）用于 `agent-browser mcp`；一个云浏览器厂商账号用于集群插件；Appium + iOS Simulator 用于 Safari-on-iOS。

## 运维难度

**低到中。** 单个本地 Chrome 时近乎开箱即用：一次全局安装、一次 `agent-browser install`，然后 shell 调用即可。守护进程模型意味着你要管理一个长生命周期进程（生命周期/恢复处理在近几个 release 里一直在改，升级时留意 daemon 兼容性）。一旦你要无头跑大规模（接入并付费给云厂商插件）、复用 Chrome profile（Windows 需先关掉 Chrome）、或依赖 Safari/WebDriver/iOS 路径（功能对齐是部分的），难度升到**中**。默认操作超时 25s，刚好低于 30s 的 CLI 读取超时——脚本化处理慢页面时要注意。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 118.9 小时，基于 13 个 qualifying issues/PRs。
- **维护——非常活跃。** 最后一次 push 在 2026-06，未归档，迭代很快（每周多个 release；最新 v0.31.0 于 2026-06-25）。守护进程的生命周期/恢复处理是个一直在改的区域——升级时留意 daemon 兼容性。`[未验证]`
- **治理 / 背书——Vercel Labs。** 仓库为 **Organization** 所有（`vercel-labs/agent-browser`）；`-labs` 仓库标志的是实验/孵化性质，而非旗舰产品，所以背书是真实的，但寿命承诺比 Vercel 的核心产品要软。`[推断]` 约 37.2k star[未验证]；由组织（而非单个维护者）维护，相对单人所有的仓库降低了 bus-factor 风险。
- **年龄与 Lindy——年轻、未经证明（创建于 2026-01，截至 2026-06 约 5 个月）。** 处于 1.0 之前，太新，拿不到 Lindy 先验；高发版节奏意味着 CLI 标志和配置 schema 会在版本间变动。若要脚本化依赖请 pin 版本。
- **风险标志——1.0 前的 churn + 部分跨引擎对齐。** Apache-2.0，未观察到 relicense/open-core。真正的标志是 API churn，以及非 Chromium/Safari 覆盖落后于 Chrome-over-CDP 路径[推断]；云集群用法会引入需你自己运维的第三方厂商插件。

## 存疑（未验证）

- `[未验证]` Star 数 ~37.2k（截至 2026-06-26，来自 `gh repo view`）；GitHub star 不可靠且对日期敏感——仅作参考。
- `[未验证]` 功能清单（React DevTools、Web Vitals、网络拦截、iOS Simulator、云插件）取自 README；并非每项都亲手验证过。
- `[推断]` 非 Chromium / Safari-WebDriver 的覆盖落后于主 Chrome-over-CDP 路径（标注截图在那里明确不支持）；每条命令的精确对齐度未逐一列出。
- `[未验证]` “无每命令浏览器启动开销” / 相对 Playwright 的启动速度优势是项目自己的说法（基于守护进程常驻），非独立基准测试。
- `[推断]` 处于 1.0 之前且每周多个 release——CLI 标志与配置 schema 可能在版本间变化；此处记录的行为以 v0.31.0 为准。
