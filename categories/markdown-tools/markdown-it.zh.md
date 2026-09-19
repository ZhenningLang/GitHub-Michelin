---
name: markdown-it
slug: markdown-it
repo: https://github.com/markdown-it/markdown-it
category: markdown-tools
tags: [markdown, parser, commonmark, gfm, plugin, javascript, html, tokenization]
language: JavaScript
license: MIT
maturity: v14.0.x, active, ~18k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-03T11:55:46Z
  default_branch: master
  default_branch_sha: 2d9bbea7df2ab1a48caecfafc39cb8599f193d3c
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T03:49:07Z
  overall: A
  overall_score: 3.5
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 7.5
        qualifying_issues: 9
        band: default
        window_offset_days: 3
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: markdown-it
        dependent_repos_count: 205037
        downloads_last_month: 100038387
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
    longevity:
      grade: A
      raw:
        repo_age_days: 4213
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 10
        top1_share: 0.776
        top3_share: 0.879
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

# markdown-it


一款快速、可插拔的 JavaScript Markdown 解析器，遵循 CommonMark 与 GFM 规范，先将文本解析为 token AST 再渲染为 HTML——相比 marked 更安全、更严格、更可扩展。


![markdown-it — health radar](../../assets/health/markdown-it.zh.svg)

## 何时使用

你正在搭建静态站点生成器、文档系统或内容平台，作者用 Markdown 写作，你需要可靠、符合规范的 HTML 输出。你想要一个严格遵循 CommonMark 并支持 GFM 扩展的解析器，同时希望能够通过插件扩展功能——表情符号、数学公式渲染、标题锚点、语法高亮代码块——而无需从头重写解析器。你安装 `markdown-it`，配置几个插件，就能获得干净、安全的 HTML，然后将其缓存、转换或注入模板。当*正确性与可扩展性*是首要考量时，它是合适的选择：文档站点、CMS、服务端渲染器，或任何 Markdown 作为用户可见内容的场景。

## 何时不用

- **你需要完整的 AST 操作工具链。** markdown-it 是一个“解析-渲染”管道，而非通用文档转换引擎。如需 lint、重写、MDX 或任意 AST 遍历，请使用 remark / unified。
- **你想要最精简的 bundle 来做简单 Markdown→HTML。** marked 更轻量，API 更小，适合一次调用渲染；markdown-it 的插件架构与 token 模型会增加你不需要的体积。
- **你需要原生非 HTML 输出。** markdown-it 默认渲染为 HTML；要生成 PDF、React 元素或其他格式，需要额外的适配器或自定义渲染规则。[未验证]
- **你在无消毒措施的情况下解析不受信任的 Markdown。** 与 marked 类似，markdown-it 默认不消毒输出 HTML——原始 HTML 会直接透传，除非你将 `html` 设为 `false` 或对输出做消毒处理。[推断]
- **你需要流式或内存受限的解析器。** 对于超大文档或流式 tokenization，micromark 的流式设计可能更合适。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [marked](marked.zh.md) | ✅ | 追求更简单、更快、footprint 更小的一次调用渲染器时，选 marked。 | 更简单、更快、footprint 更小的一次调用渲染器；规范性较弱，插件目录较小。 |
| [remark](remark.zh.md) | ✅ | 需要完整的 mdast AST 流水线来解析、转换、lint、序列化 Markdown 或 MDX 时，选 remark。 | 完整的 mdast AST 流水线，用于解析、转换、lint、序列化（Markdown、MDX）；功能强大得多，也重得多——是工具链，不是一次调用渲染器。 |
| [micromark](micromark.zh.md) | ✅ | 需要 remark 底层低层 CommonMark/GFM 分词器时，选 micromark。 | 底层 CommonMark/GFM 分词器，支撑 remark；正确且面向流式，但渲染层需自己搭建。 |
| [CommonMark](commonmark.zh.md) | ✅ | 需要规范自身的参考实现，而不是带插件的生产级渲染器时，选 CommonMark。 | 规范自身的参考实现，是合规性标尺；但 GFM 便利功能较少，未针对生产渲染优化。 |
| [Pandoc](pandoc.zh.md) | ✅ | 需要跨几十种格式的通用文档转换器，而不只是 Markdown→HTML 时，选 Pandoc。 | 基于 Haskell 的通用文档转换器，跨几十种格式；体积大得多，无法嵌入 JS 应用。 |
| Showdown | 未收录 | 仅在维护已依赖它的遗留代码时，选 Showdown。 | 较老的 JS Markdown 转换器；活跃度较低，规范合规性较弱，总体已被 markdown-it 或 marked 取代。 |
| [Goldmark](goldmark.zh.md) | ✅ | 在 Go 生态（如 Hugo）中需要 Markdown 解析器时，选 Goldmark。 | Go 的 Markdown 解析器，Hugo 在用；JS 环境不可用。 |

## 技术栈

- **语言：** JavaScript（ES2015+）；附带 TypeScript 类型定义。
- **运行目标：** Node.js 与浏览器；以 ESM 和 UMD 构建分发。
- **架构：** 基于 token 的管道——解析器将 Markdown 转为 token 流/AST，然后渲染器遍历 token 输出 HTML。插件可在两个阶段介入。
- **标准：** 核心严格遵循 CommonMark 规范，支持 GFM 扩展（表格、删除线、任务列表、自动链接），可通过 `@markdown-it/gfm` 或内置选项开启，具体取决于版本。[推断]

## 依赖

- **运行时：** 核心解析器无需外部依赖——自包含。
- **插件：** 生态基于 npm（`markdown-it-emoji`、`markdown-it-anchor`、`markdown-it-math`、`markdown-it-container` 等）——每个都是独立包，安装后通过 `.use()` 注册。
- **安装：** `npm install markdown-it`；也可通过 CDN 引入。

## 运维难度

**低。** 它只是一个库——加入依赖树，require/import 后调用 `.render()` 即可。无需部署服务，无需运维数据存储。唯一运维注意点是插件卫生：每增加一个插件就多一个需要审计和更新的依赖，且安全模型（原始 HTML 透传）要求你在处理不受信任内容时配置 `html: false` 或对输出做消毒。

## 健康度与可持续性

- **维护——活跃（最近提交 2026-07）。** 2026 年中持续发布 v14.0.x 版本；成熟、范围稳定的解析器保持定期提交与发布。[推断]
- **治理与 bus factor。** 由 GitHub 上 `markdown-it` 组织社区维护——小团队而非单人，相比单作者库降低了 bus factor 风险。[推断] 不受厂商控制，无商业版功能限制。
- **年龄与 Lindy 判断——老而活跃 ⇒ 强 Lindy 信号。** 约 2014 年创建（约 12 年），2026 年仍在持续发布：年龄 × 仍活跃 的典型信号。多年来一直是 VuePress、VitePress 及众多静态站点生成器的默认选择，其长期可靠性优于年轻替代品。
- **采用与生态。** 在 JS 静态站点生态中被广泛采用——VuePress、VitePress 及众多文档生成器使用它。插件生态丰富（表情、数学、锚点、图表、容器等）且文档完善。[推断]
- **风险标志——极少。** MIT 许可证，无重新许可历史，无 open-core 功能限制。主要注意点与任何 Markdown 解析器相同：默认不消毒原始 HTML，处理不受信任输入时需适当配置。

## 存疑（未验证）

- [未验证] 截至 2026-07，GitHub 约 18k stars，主线 v14.0.x；star 数与版本号随发布漂移，仅供参考。
- [推断] “多数基准测试比 marked 快”反映社区基准；实际吞吐量取决于文档大小、插件数量与运行环境。
- [推断] “VuePress、VitePress 使用”基于公开文档与依赖树；请针对你的具体版本确认。
- [未验证] 无原生非 HTML 输出：生成 React 元素、PDF 或其他格式需要自定义渲染规则或第三方适配器。
- [未验证] 插件数量与 bundle 体积正相关——加载大量插件可能显著增加解析时间与 bundle 大小。
