---
name: jsPDF
slug: jspdf
repo: https://github.com/parallax/jsPDF
category: pdf-tools
tags: [pdf, javascript, browser, nodejs, generate, client-side, html2pdf, text, graphics]
language: JavaScript
license: MIT
maturity: v2.5.x, active maintenance, ~28k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-06T02:20:06Z
  default_branch: master
  default_branch_sha: a3930ce03a585a26b2c76d12a0f413ce96f6d1a3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:52:54Z
  overall: B
  overall_score: 3.4
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 9
        active_weeks_13: 1
        carve_out: mature_library_lindy
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: jspdf
        dependent_repos_count: 21994
        downloads_last_month: 52701611
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 6134
        last_commit_age_days: 9
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 10
        top1_share: 0.615
        top3_share: 0.769
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# jsPDF


一个在浏览器中把 HTML、文本和图形生成 PDF 的客户端 JavaScript 库——适合发票、报表和票据等场景，无需服务端往返。


![jsPDF — health radar](../../assets/health/jspdf.zh.svg)

## 何时使用

你是一个前端开发者，正在做一个需要让用户下载 PDF 的 Web 应用——发票、物流标签、票据或简单报表——你想直接在浏览器里生成它，而不把数据发到服务端再等响应。你手头有 HTML 模板或原始文本与图形要组装，需要一种快速、轻量的方式来在客户端构建 PDF 文档。你引入 `jspdf`，创建文档实例，添加文本、图片和表格（通过 `autotable` 插件），然后调用 `save()` 把文件塞进用户下载列表——不需要后端 PDF 服务，没有延迟，数据也从未离开客户端。

同一个库也适合你已经有样式化 HTML、想把它转成外观相近的 PDF 的场景：内置的 `html` 方法（底层调用 html2canvas）让你指向一个 DOM 元素，把它渲染后嵌入 PDF 页面——这对收据、证书和数据摘要很方便，因为它们本来就已经在屏幕上渲染好了。

## 何时不用

- **你需要修改现有 PDF。** jsPDF 只支持创建——从零开始构建新文档。它无法打开已有 PDF、编辑页面、填充已有表单、合并文件或在现有文档上盖戳。这类需求请用 pdf-lib（JS）或服务端工具。
- **你需要像素级精确的 HTML 转 PDF。** `html` 插件依赖 html2canvas，而 html2canvas 有已知的 CSS 支持缺口（flexbox/grid 可能脆弱，复杂布局可能漂移），且在大表格或跨页内容上容易出问题。[推断] 如需印刷品质的 HTML 转 PDF，无头浏览器（Puppeteer/Playwright）或专用服务端渲染器更可靠。
- **你的 PDF 复杂或体量很大。** jsPDF 虽然能处理文本、图片和基本图形，但它不是为重度文档操作设计的——复杂排版、富字体排版、嵌入式交互表单或非常大的多页文档可能超出它的舒适区。重度服务端生成请用 reportlab（Python）或类似工具。
- **你需要尽可能小的包体积。** jsPDF 功能丰富但不算小巧；在极度受限的环境中，请评估是否用更轻量的专用工具或服务端生成端点更合适。
- **你需要为 AI/RAG 做结构化文档解析。** jsPDF 生成 PDF，它不会解析或从 PDF 中提取结构化内容。如需对现有文档做版面感知的解析，请用 [Docling](../document-parsing/docling.zh.md) 或类似工具。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [PDF.js](pdfjs.zh.md) | ✅ | 需要渲染或读取已有 PDF 时，选 PDF.js。 | 渲染器/查看器，不是生成器——互补关系。PDF.js 显示 PDF；jsPDF 构建 PDF。 |
| [pdf-lib](pdf-lib.zh.md) | ✅ | 需要在 JS 中创建且修改 PDF（表单、合并、绘制）且不引入原生依赖时，选 pdf-lib。 | JS 库，可创建并修改 PDF——覆盖 jsPDF 不处理的编辑/修改场景。 |
| [PyMuPDF](pymupdf.zh.md) / [pdfplumber](pdfplumber.zh.md) | ✅ | 需要快速服务端 PDF 文本/表格提取或渲染时，选 PyMuPDF / pdfplumber。 | Python 库，用于服务端 PDF 处理；不是浏览器生成器。 |
| [Docling](../document-parsing/docling.zh.md) | ✅ | 需要把文档解析成结构化输出供 AI/RAG 时，选 Docling。 | 解析器，不是生成器——它把文档读成结构化 Markdown/JSON，从不创建 PDF。 |
| 原生 `<embed>` / 浏览器 PDF 插件 | 未收录 | 只需要零集成地显示已有 PDF 时，选原生嵌入。 | 零依赖展示，但无法生成、无法程序化控制，且各浏览器表现不一致。 |

## 技术栈

- **语言：** JavaScript（ES5/ES6+），附带 TypeScript 类型定义。
- **执行模型：** 在现代浏览器和 Node.js 中运行；可与打包器（Webpack、Vite、Rollup）配合，也可通过 CDN 直接加载。
- **架构：** 插件化——核心库很小，表格（`autotable`）、HTML 转 PDF（通过 html2canvas）和 SVG 导入等功能以独立插件形式添加。
- **HTML 转 PDF 管线：** `html` 插件将渲染工作委托给 html2canvas，把 DOM 元素栅格化为 canvas，再把图像数据嵌入 PDF。

## 依赖

- **运行时：** JavaScript 环境——现代浏览器或 Node.js。无原生二进制依赖。
- **安装：** `npm install jspdf` 装核心库；`jspdf-autotable` 等插件是单独的 npm 包。
- **html2canvas：** 使用 `html` 插件做 HTML 转 PDF 时需要；它是与 jsPDF 分开的依赖，必须额外安装。
- **Node 特定说明：** 在 Node 中服务端使用某些操作可能需要 canvas polyfill；纯文本+图片生成通常不需要。[未验证]

## 运维难度

**低。** jsPDF 是一个客户端库——没有服务要部署，没有数据库，没有集群。所谓「运维」负担主要是依赖管理：保持库和插件版本最新，并留意 html2canvas（HTML 转 PDF 引擎）有它自己的发布节奏和 CSS 兼容性限制。浏览器端用就是标准的 npm install 或 CDN 引入；Node 端则需确认你需要的操作（文本、图片、canvas-backed 功能）在你的 Node 版本里无需额外 polyfill 即可工作。

## 健康度与可持续性

- **维护（2026-07）：** v2.5.x 线持续发布，维护活跃；项目自 2014 年起存在，开发持续。[推断]
- **治理/背书：** 社区维护（`parallax/jsPDF`），无大型公司或基金会背书。这意味着维护依赖志愿者贡献者而非有资金的团队——与厂商背书方案相比，bus factor 风险中等。[推断]
- **年龄与林迪（约 2014 年创建，约 12 年）：** 老且仍活跃——不错的林迪信号。一个拥有约 28k star、持续更新、已有 12 年历史的库，比年轻炒作的替代品更安全，但社区维护模式意味着其长寿保障不如基金会背书项目。[推断]
- **采用度：** 约 28k star（volatile，见存疑）且被广泛用于 Web 应用的客户端 PDF 生成；插件生态（autotable、html2canvas 集成等）提供了实际价值。[未验证]
- **风险旗标：** MIT 许可（无 relicense 风险）。未观察到 open-core 阉割或 CLA 要求。主要关注点是社区维护模式：虽然当前活跃，但如果贡献者兴趣衰减，没有企业后盾兜底。[推断]

## 存疑（未验证）

- [未验证] 约 28k GitHub star 和「活跃维护」反映的是时点快照（v2.5.x，2026-07）；star 数有噪声且随时间敏感——仅作参考。
- [未验证] html2canvas 的 CSS 支持缺口与大表格崩溃是社区报告；具体失败模式因文档复杂度和浏览器版本而异。
- [未验证] Node.js 中某些功能（如特定图片格式）所需的 canvas polyfill 取决于 Node 版本和已安装包；请在目标环境中验证。
- [推断] 插件生态的健康度和各插件（autotable、html 等）的维护节奏与 jsPDF 核心维护是分开的；某些插件可能滞后于核心版本。
- [推断] 社区维护意味着 bug 修复优先级和功能路线由志愿者可用性驱动，而非商业路线；请结合你的项目支持需求评估。
