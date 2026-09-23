---
name: Excalidraw
slug: excalidraw
repo: https://github.com/excalidraw/excalidraw
category: diagramming
tags: [whiteboard, diagram, canvas, collaboration, hand-drawn, sketch, react, export]
language: TypeScript
license: MIT
maturity: active, ~126.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-05T20:21:54Z
  default_branch: master
  default_branch_sha: 9357f98a9b6c4f8af3ada6ccce38e54330f2627c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:15:54Z
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
        last_commit_age_days: 0
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 34.4
        qualifying_issues: 26
        band: default
        window_offset_days: 5
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: "@excalidraw/excalidraw"
        dependent_repos_count: 523
        downloads_last_month: 1918275
        graph_tier: C
        volume_tier: B
        cross_check_divergence: 1.02
        release_downloads: 31973
        release_assets: 14
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 2456
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 13
        top1_share: 0.599
        top3_share: 0.889
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Excalidraw

一个手绘风格的虚拟白板——支持协作、端到端加密，可作为 React 组件嵌入，也可直接在 excalidraw.com 上使用。

![Excalidraw — 健康度雷达](../../assets/health/excalidraw.zh.svg)

## 何时使用

你是产品经理或设计师，需要在会议中快速白板画出架构草图、用户流程或线框图，并与团队分享。你选 Excalidraw 而不选 Mermaid，是因为你希望结果看起来非正式、平易近人——像餐巾纸草图而非渲染出来的文本图——这样干系人关注想法本身，而非语法。你选它而不选 draw.io，是因为你想要轻量的手绘风格，而非一个带丰富图形和集成的完整 WYSIWYG 画布。你选它而不选 Figma，是因为你需要一个快速白板，而非带有组件变体、约束和响应式预览的高保真设计工具。你打开 excalidraw.com，在无限画布上画矩形和箭头，拖入图片，然后分享链接；协作是端到端加密的，`.excalidraw` JSON 格式也是开放的。当你是 React 开发者、需要在文档站或应用里嵌入白板时，你也会选它：`@excalidraw/excalidraw` npm 包提供了一个即插即用的组件，自带暗黑模式、图形库、国际化以及 PNG／SVG／剪贴板导出。

## 何时不用

- 如果你需要可进版本库的纯文本图表，请用 Mermaid 或 PlantUML，而不用 Excalidraw，因为 Excalidraw 以 JSON（或二进制 PNG／SVG）存储图；它不是 Mermaid 或 PlantUML 那样的文本转图语法，无法在 Git 里 diff。
- 如果你需要像素级精确或自动排版的图，请用 draw.io 或 bpmn-js，而不用 Excalidraw，因为手绘风格就是它的核心卖点；它不强制 BPMN 合规、UML 严格性或自动图布局。
- 如果你需要从代码程序化生成图，请用 Mermaid 或 PlantUML，而不用 Excalidraw，因为它没有声明式文本语法可供渲染，要从 CI 管线或 LLM 输出产图，需要手写 JSON 或换工具。
- 如果你需要完整的设计／原型工具，请用 Figma，而不用 Excalidraw，因为 Excalidraw 是白板，没有组件变体、约束、响应式预览或设计交付。
- 如果你必须在完全离线、无构建步骤的环境下工作，请用 draw.io 或桌面图应用，而不用 Excalidraw，因为 Web 应用需要浏览器；虽然 React 组件打包后可离线运行，但零摩擦路径是托管应用。[推断]
- 如果你需要企业规模的实时协作，请用 Figma 或 draw.io Enterprise，而不用 Excalidraw，因为免费版跑在 excalidraw.com 上；重度团队使用可能需要 Excalidraw+（付费）或自建基础设施，开箱并不提供。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Mermaid](mermaid.zh.md) | ✅ | 需要手绘风格、协作白板时选 Excalidraw；需要把图表写成纯文本、在 Git 里 diff、在 Markdown 里渲染时，再选 Mermaid。 | 纯文本、可 diff 的图表，在 Markdown 和文档里渲染；以视觉风格换取版本控制的可移植性。 |
| [flowchart.js](flowchart-js.zh.md) | ✅ | 需要手绘风格、协作白板时选 Excalidraw；需要浏览器里极简轻量的流程图渲染器时，再选 flowchart.js。 | 只做流程图的窄 JS 渲染器；Mermaid 覆盖更多类型、宿主支持更广。 |
| [draw.io（diagrams.net）](drawio.zh.md) | ✅ | 需要轻量、手绘风格草图白板时选 Excalidraw；需要完整 WYSIWYG 画布、丰富图形和集成时，再选 draw.io。 | 全功能 WYSIWYG 画布编辑器，支持 Google Drive／OneDrive／GitHub 集成；比 Excalidraw 更重、更正式。 |
| tldraw | 未收录 | 需要开源界手绘风格白板的事实标准时选 Excalidraw；需要更新的、对开发者 API 更友好的可扩展白板库时，再选 tldraw。 | 较新的白板库，程序 API 强大；生态更小，但对自定义应用更灵活。 |
| Figma | 未收录 | 需要快速、非正式草图白板时选 Excalidraw；需要高保真 UI 设计、原型和设计系统管理时，再选 Figma。 | UI/UX 行业标准设计工具；不是草图白板，完整功能需付费团队版。 |

## 技术栈

- **语言：** TypeScript，编译为 JavaScript；以 npm 包（`@excalidraw/excalidraw`）和 CDN 可用 bundle 分发。
- **前端：** 基于 HTML5 Canvas API 的 React 组件（交互层和导出用 SVG）；使用 `rough.js` 实现手绘风格的渲染效果。
- **协作：** 托管实例通过 WebSocket 实现端到端加密实时协作；自建或嵌入场景不含此功能。
- **导出：** PNG、SVG、剪贴板复制以及 `.excalidraw` JSON 开放格式；内置暗黑模式与图形库。
- **样式：** 可自定义主题颜色和元素样式；「素描感」是核心设计选择，而非后期效果。

## 依赖

- **运行时：** 支持 Canvas 的现代浏览器。嵌入使用时需要 React 18+ 应用。
- **库依赖：** 通过 `npm i @excalidraw/excalidraw` 或 CDN 引入；包自带渲染逻辑，画图不需要额外后端。
- **协作后端：** 托管应用使用 WebSocket 中继和端到端加密服务器；自建协作需要自行搭建信令服务器。
- **无数据库：** 白板状态在客户端以 JSON 形式存在；持久化靠导出、本地存储或你自己的后端。

## 运维难度

**低**（常见情形）：直接用 excalidraw.com 免费托管应用，导出图，收工。**中**（嵌入 React 组件）：需要钉死 npm 包版本、处理升级（组件 API 可能变动），并在构建管线里打包。**中高**（自建实时协作）：必须运维 WebSocket 中继服务器、管理加密密钥，并处理 NAT/防火墙穿透。作为客户端库，主要维护负担是跟上 React/TypeScript 兼容性，以及 npm 包偶尔带来的破坏性 API 变更。[推断]

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 12 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 34.4 小时，基于 26 个 qualifying issues/PRs。
- **采用广度**：Grade B——npmjs.org 上月下载量 1,918,275（包名：@excalidraw/excalidraw）。
- **长青度**：Grade A——仓库已创建 2456 天。
- **治理集中度**：Grade B——前三贡献者占比 88.9%（过去 12 个月内 13 位活跃维护者）。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [未验证] 截至 2026-07-01 约 126.5k GitHub star；star 数为近似值且对时间敏感。
- [未验证] npm 包 API 版本与 React 兼容性要求随版本变动；嵌入前请核实当前 `@excalidraw/excalidraw` 文档。
- [未验证] 托管协作的端到端加密细节系据项目 README 概括；敏感场景请确认当前加密模型与密钥处理方式。
- [未验证] 自建协作服务器需求系据仓库架构推断；生产部署请参考官方文档。
- [推断] 产品核心就是「素描感」风格，无法关闭以换取干净矢量线条；如需 crisp 线条请评估其他工具。
- [推断] 画布元素极多时浏览器内存可能吃紧；请先用预期复杂度测试后再决定。
