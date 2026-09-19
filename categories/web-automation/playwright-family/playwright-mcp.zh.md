---
name: Playwright MCP
slug: playwright-mcp
repo: https://github.com/microsoft/playwright-mcp
category: playwright-family
tags: [mcp, playwright, browser-automation, accessibility-tree, agent-tooling]
language: TypeScript
license: Apache-2.0
maturity: v0.0.x line (latest v0.0.81, 2026-09-14), active; ~37k stars (as of 2026-09-16); Microsoft-maintained
last_verified: 2026-09-16
type: tool
upstream:
  pushed_at: 2026-09-14T21:24:01Z
  default_branch: main
  default_branch_sha: e73d72e01f162054a3d0a6b0fe8d4affffb095ee
  archived: false
health:
  schema: 1
  computed_at: 2026-09-16T07:55:57Z
  overall: A
  overall_score: 3.5
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 33.9
        qualifying_issues: 26
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@playwright/mcp"
        dependent_repos_count: 0
        downloads_last_month: 23360601
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.0
    longevity:
      grade: C
      raw:
        repo_age_days: 544
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 30
        top1_share: 0.547
        top3_share: 0.823
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

# Playwright MCP

微软官方的 MCP server：让 LLM agent 通过 Playwright 的无障碍树快照驱动真实浏览器——确定性定位，不需要截图或视觉模型。

![playwright-mcp — 健康度雷达](../../../assets/health/playwright-mcp.zh.svg)

## 何时使用

你在给一个支持 MCP 的 agent（Claude Code、VS Code Copilot、Cursor、Claude Desktop……）接浏览器，场景是**迭代式、有状态的回路**：探索式自动化（「在这个应用里乱点，把结账 bug 找出来」）、自愈测试编写、或需要跨多步持续对页面结构做推理的长自治工作流。把 `@playwright/mcp` 加进客户端的 MCP 配置，agent 就拿到 Playwright 的完整浏览器面——导航、点击、填表、evaluate、等待——页面以结构化无障碍快照而非像素呈现，元素定位保持确定性。

选它而不是手写 headless 脚本的理由是：微软维护的、规范合规的 MCP 集成，底下是 Playwright 成熟的跨浏览器引擎。但有一个 2026 年的关键提醒，来自微软自家 README：对**高吞吐 coding agent**，他们现在更推荐 `playwright-cli`（CLI+SKILLs），因为 MCP 的大工具 schema 加冗长的无障碍树会吃掉 coding agent 写代码所需的上下文。当持久浏览器状态和丰富内省比 token 成本更重要时选本 MCP；token 效率优先时选 CLI 兄弟。

## 何时不用

- **上下文预算紧张的 coding agent。** 微软 README 自己就建议这类场景去用 [Playwright CLI](playwright-cli.zh.md) 兄弟（CLI+SKILLs）——MCP 工具 schema 加每步的无障碍树在上下文里实打实更贵。如果你的 agent 主要在改代码、偶尔碰浏览器，走 CLI 路径或 CLI-first 的 [Agent Browser](../agent-browser-tools/agent-browser.zh.md)。
- **需要 DevTools 级诊断**——performance trace、Core Web Vitals、网络瀑布、source-mapped 的 console 报错。Playwright MCP 暴露的是浏览器*自动化*面，不是 DevTools 协议面；诊断页面慢/内存泄漏用 [Chrome DevTools MCP](../agent-browser-tools/chrome-devtools-mcp.zh.md)。
- **需要你日常登录的那个浏览器。** 它拉起的是 Playwright 管理的浏览器实例（`--user-data-dir` 持久 profile 和 `--cdp-endpoint` attach 存在，但默认是自动化浏览器，不是你带着 cookie、2FA 会话和风控信誉的日常 Chrome）。必须操作真实登录会话的场景，[OpenCLI](../agent-browser-tools/opencli.zh.md) 或 [Agent Browser](../agent-browser-tools/agent-browser.zh.md) 的会话持久更贴近。
- **像素级或 canvas 重度交互。** 整个设计就是「不用截图」——canvas 应用、按像素拖拽、视觉验证都出界；这类交给 vision 系 agent（browser-use 一类）。
- **非 MCP 的 harness。** 它是 MCP server；你的 agent 不说 MCP 就没有东西可调——直接用 [Playwright](playwright.zh.md) 框架本身或 CLI 包装。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Playwright CLI](playwright-cli.zh.md) | ✅ | 消费方是 coding agent 且 token 效率重要时选 Playwright CLI——微软自家 README 就把 coding agent 往那边引；持久状态与内省回路更重要时选本 MCP。 | 同一 Playwright 引擎、同一厂商；CLI+SKILLs 把上下文负载压到最低，MCP 把会话连续性与内省深度拉到最高。 |
| [Chrome DevTools MCP](../agent-browser-tools/chrome-devtools-mcp.zh.md) | ✅ | 任务是诊断页面（trace、CWV、网络、console）时选 Chrome DevTools MCP；任务是操作页面（多步表单、流程、探索）时选 Playwright MCP。 | DevTools MCP 有诊断面但只支持 Chromium 且为诊断塑形；Playwright MCP 是跨浏览器自动化塑形但没有性能工具。 |
| [Agent Browser](../agent-browser-tools/agent-browser.zh.md) | ✅ | 要 CLI-first 控制、快照 refs、常驻 Rust daemon、保存登录会话时选 Agent Browser；要厂商官方 MCP 路径与最广客户端兼容列表时选 Playwright MCP。 | Agent Browser shell 调用更快且带会话持久，但是一家厂商较年轻的工具；Playwright MCP 吃着微软的维护与 Playwright 引擎的成熟度。 |
| [browser-use](../agent-browser-tools/browser-use.zh.md) | ✅ | 要开箱即用的 Python agent 回路（带 vision 兜底）时选 browser-use；已有 agent、只差一个确定性浏览器工具面时选 Playwright MCP。 | browser-use 自带 LLM 回路（更重、有视觉能力）；Playwright MCP 是自带 agent 前提下的确定性 AX 树定位。 |
| [Playwright](playwright.zh.md)（框架） | ✅ | 写要入库的测试代码而不是让 agent 现场控制时选 Playwright 框架；agent 需要对活页面即兴操作时选 Playwright MCP。 | 框架是 CI 套件的正确产物；MCP server 用入库代码的可靠性换运行时灵活性。 |

## 技术栈

TypeScript MCP server，架在 Playwright 自动化引擎上（Chromium、Firefox、WebKit）；面向 LLM 的页面表示是结构化无障碍树快照；Node.js ≥ 18。以 npm 包 `@playwright/mcp` 分发。

## 依赖

- 一个支持 MCP 的客户端（Claude Code、VS Code Copilot、Cursor、Claude Desktop、Goose……）；无其它运行时服务。
- Node.js ≥ 18；浏览器由 Playwright 首次运行时下载（或经 `--cdp-endpoint` 指向已有 Chrome）。

## 运维难度

**低。** 客户端 MCP 配置里一行 npx；没有 daemon 或服务要养。运维注意点是版本 churn（v0.0.x 线——次版本间可能有 breaking change）和上下文成本（大页面的无障碍树按设计就很费 token；尽量用小页面或 interactive-only 模式收窄快照）。

## 健康度与可持续性

- **维护（2026-09）：** 很活跃——v0.0.81 发布于 2026-09-14，当日 push；自创建（2025-03-21）以来约 18 个月持续发版。
- **治理 / 背书：** `Organization` 所有，归属**微软**，30 个 contributor——浏览器 agent 品类里最强的背书配置；路线图随 Playwright 走。巴士因子风险极小。
- **年龄与 Lindy（2026-09）：** 约 1.5 岁，仍在 v0.0.x 版本线——微软的投入明确，但 API 契约明示不稳定；agent 配置里 pin 版本。
- **采用：** 约 37k star / 3.2k fork（2026-09-16），为一打 MCP 客户端提供安装按钮；事实上是生态里的默认「MCP 浏览器」。[推断]
- **风险标记：** 许可证无虞（Apache-2.0，无再许可历史）。战略层面的标记是微软自己的指引：他们在积极开发 CLI+SKILLs 兄弟并把 MCP 定位为有状态/内省回路的细分场景——长期投入重心可能向 CLI 漂移。[推断]

## 存疑（未验证）

- [未验证] star（约 37k）/ fork（约 3.2k）/ contributor（30）来自 2026-09-16 的 GitHub API；对日期敏感。
- [未验证] MCP 与 CLI 的 token 效率对比是微软自家 README 的说法，非独立测量。
- [未验证] 客户端兼容列表（VS Code、Cursor、Claude Desktop、Goose、Grok、Junie……）为厂商自述；各客户端实际行为未在此验证。
- [推断] v0.0.x 版本线意味着 breaking change 可能不作预告地发；升级视为需要复查配置。
- [推断] 「事实上的默认 MCP 浏览器」是从 star 数、厂商背书与客户端安装按钮推断，不是使用遥测数据。
