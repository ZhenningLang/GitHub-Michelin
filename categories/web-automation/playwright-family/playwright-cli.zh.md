---
name: Playwright CLI
slug: playwright-cli
repo: https://github.com/microsoft/playwright-cli
category: playwright-family
tags: [playwright, cli, browser-automation, agent-skills, token-efficient, microsoft]
language: JavaScript
license: Apache-2.0
maturity: v0.1.x line (latest v0.1.20, 2026-09-14), active; repo created 2020-06, repositioned as agent CLI + SKILLs in 2026; Microsoft-maintained
last_verified: 2026-09-16
type: tool
upstream:
  pushed_at: 2026-09-14T21:26:38Z
  default_branch: main
  default_branch_sha: 12228454ed024c9ac89abd59df3b706ed9135fd9
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:12:21Z
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
        last_commit_age_days: 4
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 76.8
        qualifying_issues: 8
        band: relaxed_solo
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: "@playwright/cli"
        dependent_repos_count: 0
        downloads_last_month: 3299425
        graph_tier: E
        volume_tier: B
        cross_check_divergence: 1.01
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 2286
        last_commit_age_days: 4
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 11
        top1_share: 0.477
        top3_share: 0.908
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

# Playwright CLI

微软的 token 高效路径：CLI+SKILLs 形态让 coding agent 用简洁命令（`open`、`type`、`press`、`check`、`screenshot`）驱动 Playwright 浏览器，不把 MCP 工具 schema 和整棵无障碍树塞进上下文。

![playwright-cli — 健康度雷达](../../../assets/health/playwright-cli.zh.svg)

## 何时使用

你在跑一个高吞吐 coding agent（Claude Code、GitHub Copilot 或同类），它的主业是改代码，只是**偶尔**需要驱动浏览器——在活页面上复现 bug、走一遍 todo 应用流程、给刚写出来的界面截个图——又不想把半个上下文窗口让给浏览器工具。微软自己的定位（两个仓库的 README 都写明）是：coding agent 越来越偏好 CLI 调用而非 MCP，因为前者跳过大工具 schema 和每步冗长的无障碍树。你 `npm install -g @playwright/cli`，跑 `playwright-cli install --skills` 让 agent 学会命令面，之后 agent 就是 shell 调用：`open --headed`、`type`、`check e21`、`screenshot`——交互元素用短 `e`-ref 指代。

当 token 效率和 coding agent 人体工学是主导因素时选它而不是 Playwright MCP；需要流程跨调用存活时用会话（`-s=name`、`--persistent` 持久 profile）。这是微软自己在 2026-09 时点明给 coding agent 的路径。

## 何时不用

- **有状态、内省式的 agent 回路。** 探索式自动化、自愈测试编写、每步都要重新推理页面结构的长自治工作流，是微软明确留在 [Playwright MCP](playwright-mcp.zh.md) 上的场景——那里持久浏览器上下文和丰富内省的价值超过 token 成本。
- **DevTools 级调试。** 这里同样没有 performance trace、Core Web Vitals、网络瀑布、source-mapped console——「页面慢/有泄漏」用 [Chrome DevTools MCP](../agent-browser-tools/chrome-devtools-mcp.zh.md)。
- **你日常登录的浏览器。** 会话只在一次运行内保留 cookie/storage（或加 `--persistent` 落盘）；它不像 [OpenCLI](../agent-browser-tools/opencli.zh.md) 或 [Agent Browser](../agent-browser-tools/agent-browser.zh.md) 的会话保存那样桥接你日常的 Chrome profile。任务要用一个已带 2FA 登录的账号时，这一层不对。
- **今天就要稳定契约。** v0.1.x 加 2026 年的重新定位（仓库本身更早，是旧版 Playwright CLI）——flag、skill 格式、会话语义都还可能动；agent 配置里 pin 版本。
- **非 CLI 的 agent / 只支持 MCP 的客户端。** harness 不会 shell 调用就没有东西可用——改用 [Playwright MCP](playwright-mcp.zh.md)。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Playwright MCP](playwright-mcp.zh.md) | ✅ | agent 回路以浏览器为中心且有状态（探索、自愈测试）时选 MCP；agent 以代码为中心、浏览器步骤只是偶尔时选本 CLI。 | 同引擎同厂商：MCP 买持久内省、代价是高 token 成本；CLI 买最小上下文占用、代价是每步页面结构更薄。 |
| [Agent Browser](../agent-browser-tools/agent-browser.zh.md) | ✅ | 要常驻 Rust daemon、快照 refs、跨 run 自动保存登录会话时选 Agent Browser；要微软的维护分量和原生 SKILLs 安装时选 Playwright CLI。 | Agent Browser 运维更丰富（daemon、会话恢复）但更年轻、单一厂商；Playwright CLI 随 Playwright 组织路线图走，但会话持久是手动的（`--persistent`）。 |
| [Chrome DevTools MCP](../agent-browser-tools/chrome-devtools-mcp.zh.md) | ✅ | 诊断页面（trace、CWV、网络）选 Chrome DevTools MCP；从 coding agent 里低成本操作页面选 Playwright CLI。 | 诊断对操作——互补而非竞争；很多组合两个都要。 |
| [OpenCLI](../agent-browser-tools/opencli.zh.md) | ✅ | 目标是你已登录的第三方站点时选 OpenCLI（扩展桥接你日常 Chrome）；从 coding agent 驱动一次性干净浏览器时选 Playwright CLI。 | OpenCLI 继承你的真实会话和站点适配器，但多了扩展+daemon 攻击面；Playwright CLI 待在它完全掌控的干净自动化浏览器里。 |
| [browser-use](../agent-browser-tools/browser-use.zh.md) | ✅ | 要开箱即用、带 vision 兜底的 Python agent 回路时选 browser-use；已有 coding agent、只差便宜浏览器命令时选 Playwright CLI。 | browser-use 自带 LLM 回路与视觉路径；Playwright CLI 是自带 agent 前提、AX/DOM 基础、每步轻得多。 |

## 技术栈

JavaScript，Node.js ≥ 18，架在 Playwright 引擎上（Chromium/Firefox/WebKit）；以 npm 包 `@playwright/cli` 分发；经 `playwright-cli install --skills` 给 Claude Code / GitHub Copilot 类 agent 装技能；交互元素用短 `e`-ref 指代；会话支持内存态或 `--persistent` 落盘 profile。

## 依赖

- Node.js ≥ 18；Playwright 浏览器二进制（首次使用时下载）。
- 一个能 shell 调用的 coding agent（Claude Code、GitHub Copilot……）——不需要 MCP server 或 daemon。

## 运维难度

**低。** 全局 npm 安装加一步 skills 安装；无服务。注意 v0.1.x churn——共享 agent 配置里 pin 版本，升级后复查会话/flag 语义。

## 健康度与可持续性

- **维护（2026-09）：** 活跃——v0.1.20 于 2026-09-14 发布并当日 push；2026 年重新定位后节奏很快。
- **治理 / 背书：** `Organization` 所有，归属微软，13 个 contributor；与 Playwright 本体同组织——背书强，巴士因子风险极小。
- **年龄与 Lindy（2026-09）：** 仓库 tag 历史证实了这次重新定位：旧版 Playwright CLI 一路发到 v0.180.0（当前 release 源里最早到 2026-01-31），随后 agent-CLI 线在 2026 年从 v0.1.x 重启版本号。因此约 13.3k star 部分继承自旧 CLI 的历史——别把它读作新方向的验证。「coding agent 用 CLI 而非 MCP」这个概念本身年轻且未经大规模检验。
- **采用：** npm 包 `@playwright/cli` 在线（v0.1.20）；采用遥测未独立测量。[未验证]
- **风险标记：** Apache-2.0，许可证无虞。战略标记：2026 年的 CLI 对 MCP 分家刚发生——微软仍可能重排两个表面，且 v0.1.x 期间 skill 格式大概率会 churn。[推断]

## 存疑（未验证）

- [未验证] star（约 13.3k）/ contributor（13）来自 2026-09-16 的 GitHub API；star 数包含该仓库 2026 年前作为另一款 Playwright CLI 存在时的历史。
- [未验证] 相对 MCP 的 token 效率优势是微软在两个 README 里的自述；无独立基准引用。
- [未验证] Claude Code / GitHub Copilot 之外的 agent 兼容性为厂商自述。
- 已核实 tag 历史（2026-09-17）：旧版 tag 发到 v0.180.0，agent-CLI 线从 v0.1.x 重启——重新定位是事实而非推断。
- [推断] 会话语义（默认内存态、`--persistent` 可选）在 v0.1.x 各版本间仍可能变动。
