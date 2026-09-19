---
name: remark
slug: remark
repo: https://github.com/remarkjs/remark
category: markdown-tools
tags: [markdown, ast, mdast, unified, lint, transform, plugin, ecosystem, javascript, mdx]
language: JavaScript
license: MIT
maturity: v15.x, active, ~7k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-01T11:01:38Z
  default_branch: main
  default_branch_sha: 334415d7552f2ffa359a23efc100345e7ed7a9f7
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T03:49:26Z
  overall: A
  overall_score: 3.5
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 6.1
        qualifying_issues: 3
        band: relaxed_solo
        window_offset_days: 2
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: remark-parse
        dependent_repos_count: 376321
        downloads_last_month: 153940474
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
    longevity:
      grade: A
      raw:
        repo_age_days: 4357
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 4
        top1_share: 0.25
        top3_share: 0.75
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

# remark


建立在 unified 生态系统之上的 Markdown 处理器——将 Markdown 解析成 AST，通过插件进行变换或 lint，再序列化为 Markdown、HTML、MDX 或其他格式。


![remark — health radar](../../assets/health/remark.zh.svg)

## 何时使用

你正在构建一条文档管线或静态站点生成器，需求不止于「把 Markdown 渲染成 HTML」。你想把 Markdown 解析成结构化 AST（mdast），运行 lint 规则（断链检查、标题风格、行文质量），变换内容（注入目录、重写图片路径、添加语法高亮），并可选输出 HTML、MDX 甚至另一种 Markdown 方言。你选择 remark，因为它提供完整的管线：`remark().use(remarkGfm).use(remarkLint).process(src)` 把原始 Markdown 变成经过验证、变换过的文档树，你可以按任意需要序列化。当你需要*在渲染前以编程方式操纵* Markdown，而非仅仅转换它时，它就是正确的工具。

## 何时不用

- **你只需一次调用就能「Markdown → HTML」的渲染器。** remark 是工具链，不是单个函数。如果你只需要把 Markdown 字符串渲染成 HTML，并不关心 AST 检查、lint 或插件变换，marked 或 markdown-it 更轻更简单。[推断]
- **你对 AST 概念和插件组合感到陌生。** remark 要求理解 unified 管线（parser → transformer → compiler）、mdast 节点类型以及插件如何链式组合。学习曲线是真实存在的——如果你的团队没时间去学这个模型，更简单的解析器能更快交付。
- **你需要严格的 CommonMark 一致，且不需要插件。** remark 底层基于 micromark（本身 CommonMark 一致），但完整的 unified 管线增加了层次；若要做原始一致性测试或需要参考实现本身，请用 commonmark.js。
- **你需要通用文档转换器（不只是 Markdown）。** remark 处理 Markdown 和 MDX。若你需要在 Word、LaTeX、PDF、reStructuredText 和 Markdown 之间转换，Pandoc 才是通用工具——不是 remark。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [marked](marked.zh.md) | ✅ | 需要快速、零依赖、一次调用把 Markdown 解析成 HTML 时，选 marked。 | 快速、零依赖、一次调用即可把 Markdown 解析成 HTML、API 面极小；没有 AST 或插件管线，因此无法在渲染前 lint 或变换。 |
| [markdown-it](markdown-it.zh.md) | ✅ | 需要 CommonMark 严格、可插拔、插件目录庞大且 API 更简单时，选 markdown-it。 | CommonMark 严格、可插拔、插件目录庞大；API 比 remark 简单，但仍缺乏 unified 的完整 AST 变换工具链。 |
| [micromark](micromark.zh.md) | ✅ | 需要 remark 底层的流式分词器并自建渲染/变换层时，选 micromark。 | remark 底下那个低层流式分词器；正确且快速，但渲染和变换层要你自己搭建。 |
| [CommonMark](commonmark.zh.md) | ✅ | 需要规范自己的参考实现来做一致性测试时，选 CommonMark。 | 规范自己的参考实现；是一致性标尺，但无插件生态，也未针对生产渲染做优化。 |
| [Pandoc](pandoc.zh.md) | ✅ | 需要跨 Word、LaTeX、PDF 等几十种格式的通用文档转换器时，选 Pandoc。 | 跨几十种格式的通用文档转换器；是重型二进制，不是 JS 工具链，若只需操纵 Markdown 则杀鸡用牛刀。 |

## 技术栈

- **语言：** JavaScript（附带 TypeScript 类型定义；整个生态系统以现代 JS 实现）。[推断]
- **运行目标：** Node.js 和浏览器（通过打包器）；以 ESM/CJS 形式在 npm 分发。
- **架构：** unified 管线——`remark` 包裹 `micromark`（解析器）和 `mdast-util-to-markdown`（编译器），中间是插件式的变换阶段。AST 格式为 mdast（Markdown Abstract Syntax Tree）。
- **生态：** `remark-lint` 用于 lint，`remark-gfm` 用于 GitHub Flavored Markdown，`remark-mdx` 用于 Markdown 里的 JSX，`rehype` 用于 HTML 输出，`remark-frontmatter` 用于 YAML/TOML 前置元数据，还有数百个社区插件。

## 依赖

- **运行时：** Node.js ≥ 18（现代版本）或浏览器打包器。[未验证]
- **同生态 peer：** 插件单独安装（`remark-lint`、`remark-gfm` 等）——核心很小，但真实项目通常会拉入 5–15 个插件包。
- **安装：** `npm install remark`，然后按需添加插件；生态包大多以 `@remarkjs/` 作用域或 `remark-*` 名义发布在 npm 上。

## 运维难度

**低到中。** 它是库/工具链，不是服务——没有服务器要部署。运维负担主要在依赖管理：一条典型的 remark 管线依赖核心加多个插件，每个都有自己的版本周期。你需要跟踪插件与所锁定的 remark/unified 大版本的兼容性。管线本身是纯 JS，因此没有运行时基础设施，但调试 AST 变换可能很微妙（用 `console.log` 或 `unist-util-inspect` 查看 mdast 树）。

## 健康度与可持续性

- **维护——活跃。** unified 集体（由 Titus Wormer 及贡献者领导）在整个生态中持续规律发布；截至 2026-07，remark v15.x 是当前版本。[未验证]
- **治理与 bus factor。** 由 `remarkjs/` GitHub 组织下的集体维护；unified 生态有一支小而专注的核心团队，长期记录良好。不是单人项目，但也不是大型基金会——集体模式把风险分散到多位维护者身上。[推断]
- **背书与寿命。** unified 生态自约 2015 年起活跃（约 11 年），remark 本身是核心且稳定的支柱。「年龄 × 仍活跃」给出坚实的 Lindy 信号：多年来它一直是主要文档工具默认的 Markdown 管线。[推断]
- **采用与生态。** 被 Next.js（MDX）、Gatsby、Docusaurus 及众多文档站点使用。插件生态丰富，在 unifiedjs.com 上有良好文档。[推断]
- **风险标记——很少。** MIT 许可，无 relicense 历史，无开放核心或商业层。主要风险是生态复杂度：unified/remark/rehype/mdast 家族活动部件多，偶尔多个包一起做大版本升级。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-07 为 v15.x，约 7k GitHub star；请对照仓库核实当前版本和 star 数。
- [未验证] 当前版本要求 Node.js ≥ 18；请锁定版本的 `package.json` 中的 engine 字段确认。
- [推断]「被 Next.js、Gatsby、Docusaurus 使用」基于公开文档和依赖图谱；请针对你的具体版本确认。
- [推断] unified 生态自约 2015 年起活跃；具体创立日期和集体结构细节最好通过 unifiedjs.com 网站和 GitHub 组织页面核实。
