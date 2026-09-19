---
name: CommonMark
slug: commonmark
repo: https://github.com/commonmark/commonmark.js
category: markdown-tools
tags: [markdown, commonmark, reference-implementation, parser, specification, javascript, ast, compliance]
language: JavaScript
license: BSD-3-Clause
maturity: v0.31.0, stable reference impl, ~1.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-03-01T10:10:09Z
  default_branch: master
  default_branch_sha: 497bdcc8f8bf8400e99d7741f049233820048c8a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T04:19:25Z
  overall: B
  overall_score: 2.8
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 124
        active_weeks_13: 0
        carve_out: mature_library_lindy
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 360.0
        qualifying_issues: 0
        band: default
        window_offset_days: 6
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: commonmark
        dependent_repos_count: 6702
        downloads_last_month: 2842367
        graph_tier: B
        volume_tier: B
        cross_check_divergence: 1.0
    longevity:
      grade: B
      raw:
        repo_age_days: 4177
        last_commit_age_days: 124
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.5
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# CommonMark


CommonMark 规范的官方 JavaScript 参考实现——生成可遍历的 Concrete Syntax Tree（AST），但不以生产环境渲染速度为目标。


![CommonMark — health radar](../../assets/health/commonmark.zh.svg)

## 何时使用

你正在构建需要对照规范验证 Markdown 解析器正确性的工具，或者正在撰写关于 Markdown 解析的学术论文，需要一套权威的、符合规范的基准。你是一名开发者，在构建新的 Markdown 解析器或 linter，需要一份保证符合规范的参考实现来进行对比。你引入 commonmark.js，喂给它边界情况的 Markdown 输入，检查它生成的 AST——你知道它的输出就是其他解析器被衡量时所对照的“真相”。你遍历这棵具体的语法树来分析文档结构、构建自定义渲染器，或验证你自己的解析器是否正确处理了每一种规范的边界情况。

它也适合用于必须保证规范合规的工具——合规测试套件、Markdown 教学工具，或任何“规范怎么说”比“多快能出 HTML”更重要的场景。

## 何时不用

- **你需要一个快速的生产环境 Markdown→HTML 渲染器。** 这是一个参考实现，不以速度为优化目标——marked 和 markdown-it 在生产渲染上都更快。[推断]
- **你需要 GFM 特性（表格、任务列表、删除线、自动链接）。** commonmark.js 仅支持 CommonMark；GitHub Flavored Markdown 不是内置的。[推断]
- **你需要插件生态。** 与 markdown-it 或 remark 不同，它没有插件架构——所见即所得。[推断]
- **你要渲染不受信任的用户 Markdown 且不做消毒。** 和大多数解析器一样，commonmark.js 不会消毒输出的 HTML；原始 HTML 会透传，因此不经处理直接使用会有 XSS 漏洞。你必须自行通过消毒器处理输出。
- **你想要一个“一键调用给我 HTML”的库。** 它给你的是 AST；你需要自己遍历这棵树并渲染。内置的 HTML 渲染器非常基础，主要供演示和验证使用，不适合生产环境。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [marked](marked.zh.md) | ✅ | 更需要速度和简单的一次调用渲染器，而不是规范参考实现时，选 marked。 | 快速、底层的 Markdown→HTML 解析器，API 极小；不严格遵循规范，且你必须自己做输出消毒。 |
| [markdown-it](markdown-it.zh.md) | ✅ | 需要生产级 Markdown→HTML 渲染、CommonMark/GFM 合规和插件生态时，选 markdown-it。 | 严格遵循 CommonMark/GFM，可插拔，插件目录丰富；比 marked 重，且仍需做输出消毒。 |
| [remark](remark.zh.md) | ✅ | 需要完整的 mdast AST 管线来做解析、变换、lint 和序列化时，选 remark。 | 完整的 mdast AST 工具链，插件生态庞大；远比单个库强大，但也重得多——是工具链，不是一次调用的渲染器。 |
| [micromark](micromark.zh.md) | ✅ | 需要 remark 底层的低层 tokenizer，而不是参考 AST 解析器时，选 micromark。 | 流式导向的 CommonMark/GFM tokenizer，为 remark 提供动力；你需要自己构建渲染层。 |
| [Pandoc](pandoc.zh.md) | ✅ | 需要通用文档转换，而不是只做 Markdown 解析或一致性测试时，选 Pandoc。 | 通用文档转换器，可读写数十种格式；但它是重型 CLI 工具，不是 JS 库。 |
| [Goldmark](goldmark.zh.md) | ✅ | 需要在 Go 中有一个快速、可扩展的 Markdown 解析器时，选 Goldmark。 | 用 Go 编写的快速、可扩展的 CommonMark/GFM 解析器；不适用于 JS 项目。 |

## 技术栈

- **语言：** JavaScript（ES 模块，可在 Node.js 和浏览器中运行）。
- **架构：** 解析器生成 Concrete Syntax Tree（AST）作为嵌套对象；你需要自己遍历并渲染该树。内置的 HTML 渲染器非常基础，主要供规范验证和演示使用。
- **规范对齐：** 精确实现 CommonMark 规范；规范的更新驱动版本号的提升（v0.31.0 与 CommonMark 规范 0.31 对齐）。

## 依赖

- **运行时：** 无——零运行时依赖。
- **安装：** `npm install commonmark`，或从 CDN 加载捆绑的浏览器构建文件。
- **输出处理：** 库输出 AST；HTML 渲染由你负责。包内包含一个基础 HTML 渲染器，但没有输出消毒功能——处理不受信任内容时你必须自行添加 DOMPurify 或等效工具。

## 运维难度

**低。** 它是一个库，没有需要运维的服务器或数据库。唯一的注意事项是：如果你要用于生产环境，必须基于 AST 自行构建渲染和消毒管线。无数据存储、无运行时、无基础设施。

## 健康度与可持续性

- **维护——稳定、低变动。** 作为与 CommonMark 规范绑定的参考实现，发布由规范修订驱动，而非功能迭代。v0.31.0 与 CommonMark 规范版本对齐。
- **治理与 bus factor。** 由 John MacFarlane（CommonMark 和 Pandoc 的创建者）维护，由 CommonMark 项目背书。参考实现采用单作者维护在规范项目中是常态；规范本身有更广泛的治理。
- **寿命与 Lindy 判断——老且仍活跃 ⇒ 强 Lindy。** CommonMark 项目始于 2014 年，JS 参考实现作为合规基准已有十年。一个与规范如此紧密跟踪的参考实现，是长期可持续性的非常安全的选择。
- **采用度与生态。** 按设计来看社区较小——它是参考工具，不是生产渲染器。衡量标准应看多少解析器测试套件依赖它，而非 npm 下载量。
- **风险旗标——极小。** BSD-3-Clause 许可，无 relicense 历史，无商业层级。其“风险”在于范围狭窄：它将保持为参考实现，而不会扩展成全功能的渲染器。

## 存疑（未验证）

- [未验证] 截至 2026-07 的确切 star 数和最新发布版本——如果这些数字对你的决策有影响，请对照 GitHub 仓库核实。
- [推断] “比 marked/markdown-it 慢”是从项目作为参考实现的自述目标推断而来，并非基于基准测试；如果吞吐量是你的关注点，请自行运行基准测试。
- [推断] “不支持 GFM”基于项目文档；请自上次检查以来是否已添加任何 GFM 扩展进行验证。
- [推断] “无运行时依赖”是项目自身的表述；请对照你锁定版本的 `package.json` 确认。
- [未验证] v0.31.0 与 CommonMark 规范 0.31 的对齐关系——请对照仓库中的当前规范版本与包版本核实。
- [推断] John MacFarlane 的作者身份与 CommonMark 项目背书是从公开文档和仓库所有权推断而来；请针对你的评估窗口确认当前维护者。
- [推断] “年龄 × 仍活跃”的 Lindy 评估基于项目的公开历史（CommonMark 约始于 2014 年）；如果近期活跃度对你重要，请核实当前提交和发布节奏。
- [推断] 内置 HTML 渲染器被描述为 minimal／基础——请对照你当前的渲染需求核实其能力。
- [推断] “无消毒功能”适用于 AST 输出；你基于 AST 构建的任何 HTML 渲染器都必须包含自身的消毒功能，才能处理不受信任的输入。
