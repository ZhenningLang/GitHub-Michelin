---
name: Chrome DevTools MCP
slug: chrome-devtools-mcp
repo: https://github.com/ChromeDevTools/chrome-devtools-mcp
category: agent-browser-tools
tags: [mcp-server, chrome-devtools, puppeteer, cdp, browser-automation, performance-tracing, network-inspection, debugging, typescript, byo-agent]
language: TypeScript
license: Apache-2.0
maturity: "v1.10.1 (2026-09-23), active, ChromeDevTools (Google) org, ~52.7k stars (as of 2026-09)"
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-28T08:33:49Z
  default_branch: main
  default_branch_sha: ae0aaef884c41445d83f86f099ef211f4584b791
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T08:49:34Z
  overall: A
  overall_score: 3.67
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
        last_commit_age_days: 3
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 6.1
        qualifying_issues: 44
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: chrome-devtools-mcp
        dependent_repos_count: 0
        downloads_last_month: 7877606
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.0
        homebrew_installs_90d: 603
        homebrew_tier: B
        signal_basis: homebrew
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 382
        last_commit_age_days: 3
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 90
        top1_share: 0.386
        top3_share: 0.593
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

# Chrome DevTools MCP

Agent 读得了源码，却看不到跑起来的页面：录不到性能 trace，说不清哪个请求阻塞了渲染，控制台报错也没有带 source map 的堆栈。Chrome DevTools MCP 把一个真实的 Chrome 交给 coding agent 去驱动和检查，底座是 Puppeteer + DevTools 协议（CDP）。

![chrome-devtools-mcp — 健康度雷达](../../../assets/health/chrome-devtools-mcp.zh.svg)

## 何时使用

你是一个 coding agent（或正在给它接线的工程师），接到的任务是排查“页面感觉很慢，还像是有内存泄漏”。光读源码到不了底：你得真把页面在 Chrome 里加载起来，录一段性能 trace，看 Core Web Vitals(LCP/INP/CLS)，查清是哪些网络请求阻塞了渲染，再读带 source map 的控制台报错——这些都是人会打开 DevTools 去做的事。纯 DOM 文本自动化测不出其中任何一项。

你把 `chrome-devtools-mcp` 加进 MCP 客户端配置（`npx chrome-devtools-mcp@latest`），于是 agent 就能启动或附着到 Chrome、导航、点击和填表、截图、跑 Lighthouse 审计、录 trace 拿到可执行的性能洞察，甚至抓堆快照去追泄漏——全部通过这一个 MCP 服务器完成，而主流编码客户端（Antigravity、Claude Code、Cursor、VS Code/Copilot、Gemini CLI 等，每个都有文档化的接入配置）已经能和它对话。因为它跑在 Puppeteer + CDP 之上、对接真实 Chrome，所以当你的任务是**调试和度量**一个 Web 应用、而不只是点点点时，它特别合适：前端性能工作、网络/控制台分诊、自动复现 UI bug，以及在真实浏览器里验证修复。如果你只需要基础浏览动作，`--slim` 参数会暴露一个精简工具集。

## 怎么用起来

这个服务器是你的 MCP 客户端经 stdio 拉起的一个 Node 进程。进程内部，Puppeteer 通过 Chrome DevTools 协议（CDP，即 Chrome 自家 DevTools 前端所用的调试协议）驱动一个真实的 Chrome，并把每一项 DevTools 能力变成一个具名的 MCP 工具：`navigate_page`、`click`、`evaluate_script`、`performance_start_trace`、`list_network_requests`、`get_console_message`、堆快照分析等等（2026-09 的工具参考列了 59 个，且随版本增长）。浏览器是懒启动的——只有客户端第一次调用需要浏览器的工具时，服务器才启动或附着 Chrome——而且 Puppeteer 会自动等待动作生效，agent 不必轮询状态。它替你做的：把整套 DevTools 的“测量与操作”面包装成工具调用。留给你的：准备一个可达的 Chrome（本机、容器，或远程调试端口/WebSocket），选好 flag（`--headless`、`--isolated`、`--slim`），以及设定安全/遥测姿态。近期版本还附带一个实验性 CLI（`chrome-devtools`），经后台守护进程通信，脚本和 subagent 不接 MCP 客户端也能用同一套引擎。

![chrome-devtools-mcp — 主干用户故事](../../../assets/flow/chrome-devtools-mcp.zh.svg)

<!-- flow-steps:begin (generated from flows/chrome-devtools-mcp.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：在 MCP 客户端配置里加上这个服务器 — `npx -y chrome-devtools-mcp@latest` — 组件：`npm 包`
2. **Chrome DevTools MCP**：直到第一次调用需要浏览器的工具，才启动或附着 Chrome — 组件：`Puppeteer`
3. **你**：让 agent 去检查一个真实页面 — `Check the performance of https://developers.chrome.com`
4. **Chrome DevTools MCP**：通过 DevTools 协议驱动页面，自动等待动作生效 — 组件：`CDP 自动化`
5. **Chrome DevTools MCP**：录制 trace 并返回可执行的性能洞察 — 组件：`DevTools 追踪`

**价值**：agent 直接拿到完整 DevTools 能力——trace、网络、控制台、堆——不必亲手打开 Chrome

</details>
<!-- flow-steps:end -->

## 何时不用

- **你只是想用自然语言填表/点 UI。** 一整套 DevTools/CDP 服务器干这个太重；像 [page-agent](page-agent.zh.md) 这样的页内 DOM agent 直接嵌进用户已登录的浏览器会话，不需要单独的 Chrome 进程，也不需要后端。
- **你不在 Chrome 上。** 它官方只支持 Google Chrome 和 Chrome for Testing，其他 Chromium 浏览器“可能出现非预期行为”,Firefox/WebKit 不在范围内。要跨浏览器自动化请改用 Playwright。
- **你跑不起真实浏览器。** 它需要一个本地（或可远程调试的）Chrome 外加 Node.js——在受限沙箱、纯 serverless 函数，或任何无法启动/附着 Chrome 的地方都不可行。
- **要做 OS 级 / 多应用的桌面控制。** 它驱动的是浏览器，不是整台机器。要“操作整台电脑/VM”请用 computer-use agent 或像 [Cua](../../desktop-automation/cua.zh.md) 这样的沙箱。
- **不可信页面 + 敏感数据。** README 警告它会把全部浏览器内容（cookie、登录会话、页面内容）暴露给 MCP 客户端——以及模型。别让它指向那些装着你不愿粘进 agent 的机密的站点。
- **你想要默认零遥测。** 除非传 `--no-usage-statistics`，否则 Google 会默认收集使用统计；性能流程还可能调用 CrUX API，除非用 `--no-performance-crux` 关掉。
- **成熟度。** 版本虽是 v1.x，节奏却很快——v1.4.0（2026-06-23）到 v1.10.1（2026-09-23）三个多月出了六个 minor，庞大的 flag/工具面仍随版本变动；要可复现请锁版本。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [page-agent](page-agent.zh.md) | ✅ | 需要页内 JS GUI agent 而不是 DevTools 访问时，选 page-agent。 | 页内 JS GUI agent（DOM 即文本，无 headless 浏览器、无后端）；做 NL 表单/流程自动化很强，但**无法**录 trace、在 CDP 层检查网络、或抓堆快照。 |
| [Agent Browser](agent-browser.zh.md) | ✅ | 需要 Vercel-labs 面向 agent 的 CLI 浏览器自动化时，选 Agent Browser。 | Vercel-labs 的面向 agent 的浏览器自动化；“为 agent 驱动浏览器”这一目标重叠——栈/手感不同，DevTools 协议面没这么全。 |
| [Cua](../../desktop-automation/cua.zh.md) | ✅ | 当 agent 还要操作整台桌面上的非浏览器应用时，选 Cua。 | 整桌面的 computer-use 层——可驱动任意应用与系统弹窗，结构化状态或像素，VM／云隔离可选；更广但更重，且在 Web 性能/网络上不是 DevTools 级。 |
| [Playwright](../playwright-family/playwright.zh.md)(+ MCP) | ✅ | 需要跨浏览器、确定性的可移植自动化/CI 时，选 Playwright。 | 跨浏览器（Chromium/Firefox/WebKit）、确定性、可代码或 MCP 驱动、支持 headless；做可移植自动化/CI 的首选。Chrome DevTools MCP 是用广度换 Chrome 原生 DevTools 深度（trace、Lighthouse、堆、CrUX）。 |
| [Puppeteer](../browser-driver-frameworks/puppeteer.zh.md) | ✅ | 需要这台 server 所基于的底层 Chrome/CDP 库时，选 Puppeteer。 | 这台服务器所基于的更底层 Chrome/CDP 自动化库；脚本你自己写，没有 MCP/agent 层，也没有打磨过的性能洞察工具。 |
| [browser-use](browser-use.zh.md) | ✅ | 需要 Python、具视觉能力的自主浏览器 agent 时，选 browser-use。 | Python、具视觉能力的自主浏览器 agent；更偏“agent 自己决定做什么”而非“给 agent 精确的 DevTools 工具”，且在性能/网络检查上不是 DevTools 协议级。 |

## 技术栈

- **语言：** TypeScript；以 npm 包分发，通过 `npx chrome-devtools-mcp@latest` 运行，并附带实验性 CLI（`chrome-devtools`），经后台守护进程通信（Linux/Mac 用 Unix socket，Windows 用命名管道）。
- **浏览器控制：** Puppeteer 经 Chrome DevTools Protocol（CDP）驱动 Google Chrome。
- **协议：** Model Context Protocol（MCP）服务器——以 stdio 传输接入支持 MCP 的客户端。
- **工具面（2026-09 工具参考共 59 个；`--slim` 提供精简集）：** 输入自动化、导航、模拟（设备/视口/网络/配色）、性能 trace + 洞察、网络检查、调试（截图、控制台、`evaluate_script`、Lighthouse）、内存/堆快照分析（dominators/retainers/paths）、Chrome 扩展管理、实验性的 third-party/WebMCP 工具执行（WebMCP 需 Chrome 150+ 并开特性 flag），以及 Progressive Web App 自动化。
- **连接方式：** 自动启动、自动连接本机已运行的 Chrome（需 Chrome 144+）、带自定义 header 的手动 WebSocket、或远程调试端口转发。

## 依赖

- **Node.js**（当前 LTS）+ npm。
- **Google Chrome**（当前 stable 或更新）或 **Chrome for Testing**——必须可安装/启动，或有一个能在远程调试端口上访问的 Chrome。
- **一个 MCP 客户端**来托管它（Claude Code、Cursor、VS Code/Copilot、Gemini CLI、Cline、Windsurf 等）。
- 无数据库/服务后端；状态就是它管理的浏览器会话。

## 运维难度

**低到中。** 顺利路径是在 MCP 客户端配置里写一段 JSON,`npx chrome-devtools-mcp@latest` 首次运行时拉包——没有要托管的基础设施。成本上升来自：在 headless/CI/容器环境里搞到一个可用的真实 Chrome（经典的“Chrome 在 Docker 里启不起来”沙箱/`--no-sandbox` 摩擦）、30+ 个配置 flag 与多种连接方式，以及你必须有意识设定的安全/遥测姿态（给不可信页面加沙箱、`--no-usage-statistics`、`--no-performance-crux`）。因为每个 MCP 客户端各自启动一个服务器进程，所以没有共享服务要运维——但也没有集中治理访问的地方。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 6.1 小时，基于 44 个 qualifying issues/PRs（评分器，2026-09-28）。
- **维护——活跃、官方、在加速。** 默认分支最后一次提交在 2026-09-25，仓库 push 在 2026-09-28，未归档；最新 release v1.10.1（2026-09-23），且节奏在变快——v1.4.0 到 v1.10.1 是三个多月内的六个 minor 版（GitHub releases API，2026-09-28）。发布在 **ChromeDevTools（Google）** 组织名下，所以维护是机构级而非业余——是本处 web-automation 同类里最强的背书信号。
- **治理 / 背书——Google / Chrome DevTools 团队。** 仓库为 **Organization** 所有（`ChromeDevTools/chrome-devtools-mcp`），约 52.7k star（GitHub API，2026-09-28）。bus factor 很低（是 Google 内部一个团队，而非单个维护者）——但要注意 Google 砍掉副项目的履历参差，所以“官方”是降低而非消除弃坑风险。`[推断]`
- **年龄与 Lindy——约 1 岁（创建于 2025-09-11）。** 单看自身太新，拿不到强 Lindy 先验；flag/工具面仍随版本变动，要可复现请 pin 版本。它的 Lindy 强度，更多来自其底座（Chrome + CDP + Puppeteer）的耐久性，而非这个仓库自身的年龄。
- **风险标志——默认开启遥测 + 浏览器内容暴露。** Apache-2.0，未观察到 relicense。除非传 `--no-usage-statistics`（或设 `CHROME_DEVTOOLS_MCP_NO_USAGE_STATISTICS`/`CI` 环境变量），否则 Google 会收集使用统计；性能流程可能调用 CrUX API，除非传 `--no-performance-crux`；README 警告它会把全部浏览器内容（cookie/会话/页面内容）暴露给客户端和模型——请有意识地设定安全/遥测姿态。

## 存疑（未验证）

- [未验证] Star 数约 52.7k（2026-09-28 的 gh API 快照）；GitHub star 不可靠且对日期敏感——仅作参考。
- [未验证] “59 个工具”是对 2026-09-28 的 `docs/tool-reference.md` 逐节计数所得，“客户端名单”反映当前 README 的示例（Antigravity、Claude、Cursor、Copilot）——工具/flag 面随版本变动，依赖某个具体工具前请对照当前文档核对。
- [未验证] 准确的运行时版本下限（Node LTS、“Chrome 当前 stable 或更新”、自动连接需 Chrome 144+、网络阻断需 Chrome 149+、WebMCP 需 Chrome 150+）是 2026-09-28 README/configuration 文档所述，可能变化。
- [推断] 对 Agent Browser / Cua / browser-use 的定位是从各项目自己的表述推断，并非正面 benchmark；相对取舍（DevTools 深度 vs 广度）是判断而非实测。
- [推断] 安全警告（“暴露全部浏览器内容”）是 README 自己的提醒；实际影响半径取决于你接的是哪个客户端和模型，以及 Chrome 持有的会话。
- [推断] “机构级维护是同类中最强背书”是对组织归属的定性比较，未对同类项目做治理审计。
