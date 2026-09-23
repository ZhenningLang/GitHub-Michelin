---
name: bpmn-js
slug: bpmn-js
repo: https://github.com/bpmn-io/bpmn-js
category: diagramming
tags: [bpmn, process-modeling, diagram, svg, web-modeler, javascript, camunda]
language: JavaScript
license: MIT + bpmn.io watermark clause
maturity: v18.19.0, active, ~9.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-26T07:11:27Z
  default_branch: develop
  default_branch_sha: 2067c99c8a807061ed78a7c0d6de9329610c3c44
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:15:30Z
  overall: B
  overall_score: 3.2
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 2.8
        qualifying_issues: 3
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: bpmn-js
        dependent_repos_count: 1072
        downloads_last_month: 878232
        graph_tier: B
        volume_tier: B
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4579
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 13
        top1_share: 0.613
        top3_share: 0.839
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# bpmn-js

面向浏览器的 BPMN 2.0 渲染与建模工具包——导入 BPMN XML、渲染成可交互的图、并就地编辑，由 Camunda 旗下 bpmn.io 团队打造。

![bpmn-js — 健康度雷达](../../assets/health/bpmn-js.zh.svg)

## 何时使用

你在做一个工作流或流程自动化产品，你的用户——是业务分析师，不是开发——需要在你的 Web 应用里设计和评审 BPMN 流程图。你不想发给他们一个桌面工具，也不想重造一个图编辑器；你想把官方的、符合标准的 BPMN 画布嵌进你的 UI。你 `npm install bpmn-js`，把一个 `BpmnModeler`（或更轻、只读展示的 `BpmnViewer`）挂到一个 `<div>` 上，喂给它 BPMN 2.0 XML，用户就得到由调色板驱动的拖拽建模——任务、网关、事件、池——而图会被序列化回标准 BPMN XML，供你持久化或交给流程引擎（Camunda 或任何符合 BPMN 的引擎）。因为它经 `bpmn-moddle` 读写规范的 BPMN XML，这些图能与更广的 BPMN 工具生态互通，而不会把你锁进某种私有格式。

当你只需渲染既有图时（看板、审计视图、文档）选 **viewer** 构建，当用户要创作或编辑时选 **modeler** 构建。它是 Web 上事实标准的开源 BPMN 画布。

## 何时不用

- **你其实并不需要 BPMN 标准。** 如果你只想要通用的框线箭头，或一次性的文本转图渲染，bpmn-js 又重又专属 BPMN——画非标准流程图时 Mermaid 或 flowchart.js 轻得多。
- **你需要的是流程*引擎*，不是画布。** bpmn-js 渲染和编辑图，但不执行流程。执行需要单独的 BPMN 引擎（Camunda 7/8、Zeebe、Flowable 等）。
- **水印条款是个问题。** 许可证要求渲染图中的 bpmn.io 水印/署名链接保持可见且不被改动——这**不是纯 MIT**；移除它即违反许可证。白标前请核实条款。[推断]
- **你想要 DMN、表单或其他记法。** bpmn-js 只做 BPMN；DMN 要用 `dmn-js`，表单要用 `form-js`——是兄弟项目、单独安装。
- **你要在浏览器 DOM 之外用它。** 它面向浏览器/DOM（基于 `diagram-js`）；无头/服务端渲染不是它的目标。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [flowchart.js](flowchart-js.zh.md) | ✅ | 只需要一个极小的文本 DSL 到 SVG 渲染器来画简单非标准流程图时，选 flowchart.js。 | 极小的文本 DSL 转 SVG 流程图渲染器；做简单非标准流程图很好，但没有 BPMN 语义、不能交互编辑、范围小得多。 |
| [Mermaid](mermaid.zh.md) | ✅ | Markdown 原生文本图比真正的 BPMN 2.0 建模更重要时，选 Mermaid。 | 广义的文本转图工具（含一种基础的类 BPMN 流程），Markdown 原生；但不是真正的 BPMN 2.0 建模器，也不做交互编辑。 |
| dmn-js / form-js（bpmn.io） | 未收录 | 记法是 DMN 决策表或表单，而不是 BPMN 流程模型时，选这些 bpmn.io 兄弟库。 | 做 DMN 决策表和表单的兄弟库；同团队同架构，但记法不同——互补而非替代。 |
| jBPM / Flowable 自带 Web 建模器 | 未收录 | 关键需求是绑定某个 Java 流程引擎时，选引擎自带建模器。 | 与特定 Java 流程引擎绑定的引擎内置 BPMN 建模器；集成了执行，但更重，作为独立 JS 画布更难嵌入。 |
| GoJS / mxGraph（draw.io） | 未收录 | 只有准备自己实现 BPMN 正确性时，才选通用图画布。 | 你需要自己在其上搭 BPMN 的通用商业/开源图画布；更通用，但 BPMN 的正确性要你自己实现，而 bpmn-js 直接给你。 |

## 技术栈

- **语言：** JavaScript（浏览器、ES 模块；经 npm 与预构建 bundle 分发）。
- **核心架构：** 基于 **diagram-js**（通用图渲染/编辑引擎，同团队）与 **bpmn-moddle**（在浏览器里读写 BPMN 2.0 XML）。
- **渲染：** SVG（经 `tiny-svg`）；工具库 `min-dash` / `min-dom`、direct-editing 和 `ids` 辅助库——一套小而自研的依赖集，无大型外部框架。
- **构建：** 分开的 **Viewer**（只渲染）与 **Modeler**（可编辑）发行版。

## 依赖

- **运行时：** 一个浏览器/DOM。纯客户端库——渲染/编辑无需后端、数据存储或服务。
- **npm 依赖：** `diagram-js`、`bpmn-moddle`、`diagram-js-direct-editing`、`ids`、`inherits-browser`、`min-dash`、`min-dom`、`tiny-svg`——均由同一组织维护。
- **执行（不打包）：** 若你想真正*运行*建好的流程，需要一个 BPMN 流程引擎——那是你自备的独立基础设施。

## 运维难度

**低（作为库）。** 它是个前端依赖：安装、挂载、喂 XML。服务端没什么要部署或运维；BPMN XML 的持久化是你应用的事。真正的复杂在*集成*——接自定义调色板项、属性面板（`bpmn-js-properties-panel`），以及对照你目标引擎的 BPMN 方言校验并往返 XML——外加在生产构建里遵守水印/署名许可条款。bpmn-js 自身没有数据存储、集群或运行时要维护。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 25.5 小时，基于 3 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06；最新 tag v18.19.0，发布节奏稳定且频繁（约 81 个 release）。明显**活跃**而非吃老本；未归档。[推断]
- **治理 / 背书。** 由 **Camunda 旗下 bpmn.io 团队**维护（一家成熟的工作流自动化厂商）——多维护者、有组织背书的项目（nikku、philippfromme、barmac、marstamm……），bus factor 健康。方向跟随 Camunda 的商业利益，是主要的治理顾虑。[推断]
- **年龄与 Lindy 判断。** 2014-03 创建，约 12 年且**仍在活跃发布**——**强 Lindy** 信号；是 Web 上正统、久经验证的开源 BPMN 画布，而非新秀。[推断]
- **采用度。** Web 应用里嵌入 BPMN 的事实标准（约 9.6k star、约 1.5k fork）；插件生态庞大（属性面板、lint、取色器）以及兄弟记法（dmn-js、form-js）。强、文档完善。[未验证]
- **风险标记。** **自定义许可证**（类 MIT 文本，但加了一条强制、不可移除的 bpmn.io 水印/署名要求于渲染输出中）是首要标记——GitHub 报为 `NOASSERTION`；白标前请读 `LICENSE` 并确认。厂商主导路线图（Camunda）为次要项。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 9.6k star / 约 1.5k fork、版本 v18.19.0；计数对时间敏感——仅供参考。
- [推断] 该许可证是 MIT 衍生文本，外加一条要求渲染图中 bpmn.io 水印/署名链接保持可见且不被改动的条款；GitHub 归类为 `NOASSERTION`。我读了 `LICENSE` 文件（Camunda Services GmbH，2014 至今）——但你应针对自己的用途确认确切义务，尤其是白标。
- [推断] “活跃 / 多维护者 / bus factor 健康”是从提交近况、发布节奏和贡献者名单推断的，而非来自公开的治理文档。
- [未验证] npm 依赖清单是某一时间点从仓库 `package.json` 读取的，且随版本变动——请对照你安装的版本核实。
- [未验证] Camunda 背书和更广的 bpmn.io 生态（dmn-js、form-js、properties-panel）依据公开项目认知陈述，未在此独立审计。
