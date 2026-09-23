---
name: Impeccable
slug: impeccable
repo: https://github.com/pbakaus/impeccable
category: ai-design-generation
tags: [design-language, frontend-linting, design-detector, agent-skill, ui-quality, css]
language: JavaScript
license: Apache-2.0
maturity: CLI v3.1.0 / Skill v3.8.0, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T07:31:57Z
  default_branch: main
  default_branch_sha: c979ac37c361da564dcce100a4f2623d94ef54c8
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:57:19Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 5.5
        qualifying_issues: 46
        band: relaxed_solo
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: impeccable
        dependent_repos_count: 0
        downloads_last_month: 494145
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        release_downloads: 755990
        release_assets: 111
        release_tier: C
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 311
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 49
        top1_share: 0.794
        top3_share: 0.953
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

# Impeccable

面向 AI coding agent 的设计语言层：一个 `/impeccable` skill（约 23 个子命令）外加一个独立 CLI，用 44 条确定性 detector 规则（无 LLM、无 API key）扫描 AI 生成的前端产物。

![impeccable — 健康度雷达](../../assets/health/impeccable.zh.svg)

## 何时使用

你是前端开发，或者负责运营某个 coding agent，而你的 agent 总是吐出同一批“AI 味”——紫蓝渐变、玻璃拟态卡片、弹跳缓动、过窄内边距、侧标签边框。代码能跑，但每个页面都像出自同一套模板，而“做得好看点”这类 prompt 只会换一种口味的同质 slop。你想要一个确定性、可复现的检查，在 CI 和编辑器里把这些模式标出来，再加一套 agent 能直接执行的共享设计词汇，而不是凭感觉。你跑 `npx impeccable detect src/`（或用 Puppeteer 指向某个 URL），拿到一组具体违规项，全程不需要 API key，并把 design hook 接上，让 detector 在 Cursor、Claude Code、Copilot、Gemini CLI、Codex CLI、OpenCode 等 harness 的每次文件编辑时触发。

当你想让 agent 自己去改进设计而不只是 lint 时，就装上 `/impeccable` skill，在 `/impeccable init` 把你的受众、品牌、voice、配色和字体蒸馏进 `PRODUCT.md` / `DESIGN.md` 之后，运行 `audit`、`critique`、`polish`、`bolder`、`quieter` 等子命令。确定性 detector 给你一道离线的硬底线；skill 的 LLM 驱动 critique 命令在其上叠一层判断。

## 何时不用

- **你需要一套完整设计系统 / 组件库。** Impeccable 做的是 critique 和 detect，不给你 token、组件或 Figma 事实源。把它和真正的设计系统配合用，别拿它替代。
- **你的技术栈不是 Web 前端。** 这 44 条规则面向 HTML/CSS/JS 的 UI 产物（行长、触控目标、标题层级、AI 设计模式）。原生移动端、后端、数据可视化或非 Web UI 几乎用不上。
- **你想要跨 provider 的一致保证。** 集成靠按 harness 构建的 provider-native skill/hook manifest（`dist/claude-code/`、`dist/cursor/` 等）；没有对应 manifest 的 harness 需要手动接线，而且 skill 的命令面是 Impeccable 专有锁定。
- **你不信任写进规则里的主观审美。** 确定性规则编码了某个团队对“AI slop”的看法（比如把紫渐变、暗发光判为问题）。有意使用这些风格的项目会和误报搏斗。[推断]
- **你需要一套冻结、可审计的规则集。** CLI、Skill、Extension 各自独立发版且更新频繁（2026 年 6 月内多次发布）；不 pin 版本，行为会在版本间漂移。
- **无头/离线 URL 扫描有约束。** URL 检测会引入 Puppeteer（下载一个无头 Chromium）；在封闭 CI 里这是额外体积和网络依赖。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [html-anything](html-anything.zh.md) | ✅ | 需要 agent 生成 HTML 产物时，选 html-anything。 | 由 agent 生成 HTML 产物；Impeccable 则是 critique/lint agent 已经产出的东西。互补而非替代。 |
| [open-design](open-design.zh.md) | ✅ | 需要设计语言/生成层而非 lint harness 时，选 open-design。 | 同类目下的设计语言 / 生成层；在“让 agent 设计更好”上有重叠，但分歧在于是 lint 现有产物还是驱动生成。建议直接对照两页。 |
| [guizang-ppt](../agent-skills/slides-ppt/guizang-ppt.zh.md) | ✅ | 需要幻灯片生成 skill-pack 时，选 guizang-ppt。 | 面向幻灯片生成的 skill-pack；产物类型窄，没有确定性 detector 或 CLI。Impeccable 是更宽的前端质量工具。 |
| [guizang-social-card](../agent-skills/visual-content/guizang-social-card.zh.md) | ✅ | 需要社交卡片生成 skill-pack 时，选 guizang-social-card。 | 社交卡片生成的 skill-pack；单一产物类型，对比 Impeccable 的通用 UI linting。 |
| ESLint + a11y 插件（eslint-plugin-jsx-a11y） | 未收录 | 需要成熟 AST-based 可访问性/代码 linting 时，选 ESLint/a11y 插件。 | 成熟、基于 AST 的可访问性/代码 linting，完全离线；但没有“AI 设计 slop”模式概念，也没有审美 critique 或 agent-skill 层。 |
| Stylelint | 未收录 | 需要规则生态庞大的确定性 CSS linting 时，选 Stylelint。 | 确定性 CSS linting，规则生态庞大；面向 CSS 正确性/约定，而非审美 AI 模式检测或 agent 设计辅导。 |
| Lighthouse / axe-core | 未收录 | 需要渲染后页面的性能/可访问性审计时，选 Lighthouse 或 axe-core。 | 在渲染后的页面上审计性能/可访问性；在 URL 扫描上有重叠，但不做 AI 设计模式检测，也没有 skill 驱动的 "polish/bolder/quieter" 工作流。 |

## 技术栈

- **语言：** JavaScript（仓库约 94%），并含 TypeScript、CSS、Astro、HTML、Svelte。
- **分发：** npm 包，通过 `npx impeccable` 运行；按 provider 的构建产物放在 `dist/<harness>/`（Claude Code、Cursor 等）。
- **Detector:** 44 条确定性规则，无 LLM、无 API key 运行；覆盖 AI 设计模式（渐变、发光、弹跳缓动、侧标签边框）和通用质量（行长、内边距、触控目标、标题层级）。具体匹配机制（正则/AST/启发式）未文档化。[未验证]
- **URL 扫描：** Puppeteer（无头 Chromium），用于 `detect <url>`。
- **Skill 面：** 一个 `/impeccable` skill，约 23 个子命令；LLM 驱动的 critique 命令叠在离线 detector 之上。
- **浏览器扩展：** Chrome + Firefox 扩展，在实时页面上跑同一套确定性规则。

## 依赖

- **运行时：** Node.js（通过 `npx` 运行）；未文档化具体最低 Node 版本。[未验证]
- **URL 检测：** Puppeteer，会下载一个无头 Chromium——仅 URL 扫描需要的、较重且需联网拉取的依赖。
- **LLM:** detector/CLI/扩展不需要（明确“无 LLM、无 API key”）;skill 的 critique/polish 命令在你的 coding agent 内运行，用该 harness 提供的模型。
- **安装：** `npx impeccable install`（CLI 安装器），然后 `/impeccable init` 做一次性项目初始化。

## 运维难度

**低。** detector 路径就是一行 `npx impeccable detect …`，无需托管服务、无需 API key，带 `--json` 输出供 CI 使用；最重的部分是 URL 扫描时 Puppeteer 的 Chromium 下载。面向 agent 的路径是 skill/hook 安装，属于按 harness 写 manifest 的接线工作，而非基础设施。日常负担主要是跟上 CLI/Skill/Extension 的频繁发版，以及对有意为之的风格调掉误报。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 23.4 小时，基于 51 个 qualifying issues/PRs。
- **维护（截至 2026-06）：** 最后 push 在 2026-06，未归档，且发版很快——2026 年 6 月内 CLI/Skill/Extension 多次发布。活跃且明显处于密集开发；同样的节奏也是 churn 风险（请锁版本）。[推断]
- **治理与 bus factor：** `User` 所有的仓库（pbakaus）却背着约 41k star——单维护者项目上的高 star 是一个 **bus-factor 信号**：大量采用押在一个人持续投入上，看不到基金会或厂商兜底。[推断]
- **年龄与 Lindy 判断：** 建于 2025-11，年龄不足 1 年——**年轻但已被广泛 star**。star 数说明有真实关注度，而非 Lindy 验证过的耐久；延续性视为未被证明，规则集仍在变动。[未验证]
- **采用/生态：** 覆盖面广（Claude Code、Cursor、Copilot、Gemini CLI、Codex CLI、OpenCode，外加 Chrome/Firefox 扩展），加上无需 API key 的离线 detector，降低了试用门槛；这份广度是主要的采用信号。[推断]
- **风险标记：** 宽松的 Apache-2.0（法务/锁定风险低），但 detector 编码了某团队的审美立场（对有意为之的风格会误报），且三个组件各自独立发版——不 pin 版本，行为会在版本间漂移。

## 存疑（未验证）

- [未验证] 版本事实（CLI v3.1.0 发布于 2026-06-21;Skill v3.8.0;Extension v1.2.1）取自 GitHub releases，截至 2026-06；三个组件独立发版且更新频繁，任何 pin 都会很快过时。
- [未验证] star 约 41.5k（截至 2026-06）——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 44 条 detector 规则的内部匹配机制（正则 vs AST vs 启发式）和完整规则清单在所读 README 表面未说明；“44 条确定性规则”是项目自己的表述。
- [未验证] 受支持 harness 的确切集合与最低 Node 版本来自 README 文字，可能随版本变化——依赖前请对照当前仓库核实你的 harness/运行时。
- [推断] detector 标记的“AI slop”模式（如紫渐变、暗发光）编码了一种特定审美立场；某个标记是否真是缺陷取决于项目，有意为之的设计要预期会有误报。
