---
name: Docusaurus
slug: docusaurus
repo: https://github.com/facebook/docusaurus
homepage: https://docusaurus.io
category: frameworks
tags: [documentation-site, static-site-generator, react, mdx, docs, i18n, docs-versioning, meta]
language: TypeScript
license: MIT
maturity: v3.10.2, active (released 2026-07-10; ~66.3k stars, 10.0k forks as of 2026-09); created 2017-06-20
last_verified: 2026-09-20
type: framework
upstream:
  pushed_at: 2026-09-18T20:35:06Z
  default_branch: main
  default_branch_sha: 714d743f9c461839b7e7d6101e2b65ac43a37956
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:16:53Z
  overall: B
  overall_score: 3.33
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
      grade: B
      raw:
        median_ttfr_hours: 74.1
        qualifying_issues: 23
        band: default
        window_offset_days: 5
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@docusaurus/types"
        dependent_repos_count: 14304
        downloads_last_month: 6061802
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.02
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3381
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 7
        top1_share: 0.958
        top3_share: 0.979
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

# Docusaurus

基于 React 的框架，用 Markdown／MDX 构建、做版本管理并部署项目文档站——一条命令就把文档、博客、自定义页面、i18n 与静态构建一起搭好。

![Docusaurus — 健康度雷达](../../../assets/health/docusaurus.zh.svg)

## 何时使用

你在维护一个开源项目或一款产品，文档集早已超出 README 的规模：多个版本、需要固定顺序的侧边栏、多语言、搜索框，还有一个发版说明用的博客。你希望用 Markdown 写内容、在需要的地方插入 React 组件，产出一个可以托管在任何地方的静态站——同时不必自己去搭和养这套站点骨架。

当**文档本身就是全部工作、而且版本管理与 i18n 是硬需求而非加分项**时，选 Docusaurus：`classic` 预设一次性生成文档侧边栏、文档的版本化副本、i18n 工作流与博客——这些正是你否则要自己手搓的部分。相对 [Nextra](nextra.zh.md)，取舍是「电池齐全」对「极简」——Docusaurus 直接给出文档信息架构与版本模型，Nextra 只给你 Next.js 上的一层薄 MDX，结构由你自己定。相对 [Astro](astro.zh.md)，是「文档优先」对「站点优先」：Docusaurus 很难顺手变成一个有 40 页 content collections 的通用营销站，而 Astro 的文档能力是要你自己拼装的模板，不是配置一下就完的预设。相对自己搭一个 Next.js 站点，Docusaurus 让你让出部分路由控制权，换来版本化文档、i18n 与一个有人维护的主题。

## 怎么用起来

入口就是脚手架命令：`npx create-docusaurus@latest my-website classic` 会生成带 `/docs`、`/blog`、`/src/pages`、`/static`、`docusaurus.config.js`、`sidebars.js` 的项目。**你把 Markdown 或 MDX 文件写进这些目录**——`/src/pages` 下的任何 JSX/TSX/MDX 会变成页面，`/docs` 配合 `sidebars.js` 变成文档区，`/blog` 变成带日期的文章——并在 `docusaurus.config.js` 里配置站点。**其余由 Docusaurus 完成：把文件树变成路由、用 React 渲染 MDX、套上预设的文档版式，`npm run build` 输出一整目录静态文件，可放到任何静态托管上。** 开发用 `npm run start`，本地服务器默认在 localhost:3000；内容始终是普通文件，站点结构可以在 diff 里审阅。

![docusaurus — 主干用户故事](../../../assets/flow/docusaurus.zh.svg)

<!-- flow-steps:begin (generated from flows/docusaurus.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：用 classic 预设生成站点骨架 — `npx create-docusaurus@latest my-website classic`
2. **你**：用 Markdown 或 MDX 文件写文档与博客 — `docs/ · blog/ · src/pages/`
3. **你**：配置站点与侧边栏顺序 — `docusaurus.config.js · sidebars.js`
4. **Docusaurus**：把文件树变成路由，并套上文档版式
5. **你**：写作时本地预览 — `npm run start`
6. **Docusaurus**：构建出可托管到任何地方的静态站点目录 — `npm run build`

**价值**：一个文件夹里的 Markdown 变成带版本、可搜索的文档站

</details>
<!-- flow-steps:end -->

## 何时不用

- **你的站点主要是营销页、落地页与内容集合，文档只占其中一块。** 改用 [Astro](astro.zh.md)：它的 content collections 与组件模型更贴合这种形态，而 Docusaurus 的价值（版本化文档、文档侧边栏、博客）在文档很少时纯属累赘。
- **你想要一层极简的 MDX，并愿意自己掌控路由与布局。** 改用 [Nextra](nextra.zh.md)——它是 Next.js 之上更薄的一层，代价是文档那套家具要你自己组装。
- **你的团队用 Vue 或 Svelte 而不是 React。** Docusaurus 是一个 React 应用；Vue 团队应看 VitePress 或 Vue 侧的文档框架，Svelte 团队看 SvelteKit 的文档模板。两者本索引都未收录。
- **团队里没人能维护一个 React 应用。** 脚手架只能带你走一段——超出预设的定制意味着写 React 组件、MDX provider 与插件代码。纯 Markdown 工具链如 [Quarkdown](../../typesetting/quarkdown.zh.md) 或 [Asciidoctor](../../typesetting/asciidoctor.zh.md) 能在不引入 JS 框架的前提下产出文档站。
- **你需要从同一份源额外得到 PDF 或纸质书。** Docusaurus 只产出网站；要排版成品请看 [Quarkdown](../../typesetting/quarkdown.zh.md)（一份 Markdown 超集源同时出 PDF、幻灯片与文档站）或 [LaTeX](../../typesetting/latex.zh.md)。
- **你需要内容就地渲染、不经构建。** Docusaurus 的 MDX 文件不会在 GitHub 上渲染；站点只在构建之后存在。若就地预览比站点本身更重要，请继续用纯 Markdown。
- **你的 Node 版本较旧，或 CI 镜像钉在更老的运行时上。** Docusaurus 3 要求 Node 20.0 及以上；在选定它之前先对照你的构建镜像。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Nextra](nextra.zh.md) | ✅ | 当版本化文档、i18n 与文档侧边栏必须在第一天就有、而且你宁愿配置而不是自己造时选 Docusaurus；当你想要 Next.js 之上的一层薄 MDX、其余自己组装时选 Nextra。 | Docusaurus 换来开箱即用的完整文档信息架构与明确的版本模型；代价是预设更重、以及一个你未必完全掌控的 React 应用。Nextra 正好相反：家具更少、魔法更少、拼装更多。 |
| [Astro](astro.zh.md) | ✅ | 当交付物是带版本的文档站时选 Docusaurus；当交付物是内容驱动的网站、文档只是其中一节时选 Astro。 | Astro 换来通用站点框架（content collections、islands、任意 UI 框架、默认近乎零 JS）；代价是没有内置的文档版本管理，纯文档项目得把 Docusaurus 预设的东西重做一遍。 |
| VitePress | 未收录 | 当团队用 Vue、想要快速极简、以 Markdown 为主要配置方式的文档生成器时选 VitePress；当你需要在文档里用 React 组件、或需要它自带的版本与 i18n 工作流时选 Docusaurus。 | VitePress 换来小得多的运行时、与 Vue 的对齐和简单性；代价是没有 React，插件生态也比一套 Docusaurus 预设薄。 |
| [Next.js](nextjs.zh.md) 自己接 MDX | ✅ | 只有当站点需求确实与任何文档预设都不同、并且你接受自己拥有路由、布局、搜索、版本与 i18n 时，才选自接 MDX 的 Next.js；否则选 Docusaurus，再把不需要的部分删掉。 | Next.js 换来完全的控制与不受框架约束；代价是把一套 Docusaurus 预设视为基线的文档基础设施——版本化侧边栏、i18n 路由、搜索——重新实现一遍。 |

## 技术栈

- **语言：** TypeScript。框架以一组 `@docusaurus/*` npm 包发布，必须保持同一版本。
- **核心：** React 应用加 MDX 管线；`classic` 预设捆绑 `@docusaurus/preset-classic`，带来文档插件、博客插件、自定义页面与支持暗色模式的 CSS 框架。
- **构建：** Node 工具链（Node 20+），使用自带的打包器；`npm run build` 把静态站点写进 `/build`，可部署到 GitHub Pages、Vercel、Netlify 或任何静态托管。
- **内容模型：** `/docs` 下是文档（顺序在 `sidebars.js` 中声明），`/blog` 下是带日期的文章，`/src/pages` 下的 JSX／TSX／MDX 会变成路由。
- **i18n：** 一等公民的本地化支持，历史上与 Crowdin 打通用于社区翻译。

## 依赖

- **Node.js 20.0 及以上**用于构建站点本身；这是文档明确写出的要求。
- **包管理器与 Node 构建工具链**——Docusaurus 站点**就是**一个 React 应用，可以往里加任何 npm 包，而你加的每个依赖都会进入构建。
- **运行期没有服务、没有数据库。** 产物是静态文件；托管可以是 CDN、GitHub Pages 或对象存储。搜索要么用预设的本地搜索，要么接你自己配置的托管搜索服务。
- **不需要账号。** 脚手架、构建与开发服务器全部本地；部署目标（Vercel、Netlify、GitHub Pages）是彼此独立的服务。

## 运维难度

**低到中等——构建很简单，真正的活在升级路径。** 脚手架、写作、部署各是一条命令，产物是静态文件，没有运行时需要运维。中等的部分来自版本纪律：所有 `@docusaurus/*` 包必须一起升级，历史上大版本都需要迁移指南，而一个带了自定义插件与 swizzle 组件的站点会积累出让升级踩坑的代码。文档还说明 `npm install` 报告的漏洞通常无害，这是一项你被动继承的判断，而不是一个能做完的任务。

## 健康度与可持续性

- **维护活跃度——活跃，但支持这一路较慢（截至 2026-09-20）。** `pushed_at` 为 2026-09-18T20:35:06Z；最新版本 v3.10.2（2026-07-10）、v3.10.1（2026-04-30）、v3.10.0（2026-04-07）；最近 13 周里 12 周有活动；并有明确的版本支持矩阵与归档的旧文档站。未归档。评分器把维护评为 `A`，但把响应速度评为 `B`——**25 个合格 issue 上的首次响应中位数为 56.6 小时**：项目稳定出货，而 issue 要等上一两天。
- **治理与维护者分散度——卡片与贡献者名单不一致，而卡片量的是更近期的事。** 历史总贡献分散在 `slorber`（1,258）、`lex111`（644）、`endiliey`（628）、`Josh-Cena`（615）、`yangshun`（361）身上，这是成熟多维护者项目的形态。但最近 12 个月的窗口给出了不同的答案：**top1 占比 0.958、top3 占比 0.979**，也就是说近期几乎全部工作由一个账号完成——这正是治理一轴评为 `D`、成为本页最弱项的原因。请读作「一个长期项目当前由一个人扛着」，而不是「有一支活跃的大团队」。README 说明 Meta 开源它是因为它帮助公司规模化支撑自家 OSS 项目站点，所以有一个有理由让它活下去的归属方，但眼下的日常 bus factor 很薄。
- **背书与寿命——老到已经扛过两次大重写。** 创建于 2017-06-20，截至 2026-09 约九年（仓库年龄 3,379 天），v3 线仍在维护，还有 canary 通道和大量基于它的站点。Lindy 先验里真正有用的是「年龄 + 持续活跃」这两点同时成立。
- **采用与生态——在文档框架里属于头部，且有分发数据佐证。** 评分器把采用广度解析到 npm 上的包：**14,304 个依赖仓库、月下载 6,638,380**；仓库本身约 66.3k star、约 10.0k fork，采用者从小项目到大型厂商文档站都有，另有插件生态与社区 swizzle 模式。Star 只是关注度，但这里的关注度有一条近十年的发布线背书。
- **风险旗标——Meta 的所有权与 npm 供应链面。** MIT 许可，未发现换证历史。两点要计入：路线图最终由 Meta 决定；以及一个文档站会拉进一棵由第三方维护的庞大 npm 依赖树，`npm audit` 的输出因此是你要学会分诊的噪音。

## 存疑（未验证）

- `[未验证]` **Meta 持续投入的承诺。** README 说 Docusaurus 支撑 Meta 自家的 OSS 项目；这一承诺是否会超出当前人员配置存续，没有评估。
- `[未验证]` **大版本之间的升级成本。** 迁移指南是有的，但一个深度定制过的站点在两个大版本之间实际要改多少，没有测量。
- `[未验证]` **搜索行为。** 预设的本地搜索以及任何托管替代方案的质量与索引规模上限，没有评估。
- `[未验证]` **对小规模文档站而言，预设是否真的比在 Next.js 里自接 MDX 省事。** 对比表断言「需要版本与 i18n 时是这样」；这依据的是两个产品文档化的功能，而不是实测对比。
- `[未验证]` **大文档集的性能。** 上千页时的构建时间与包体积没有测量；超大规模文档站可能撞上本页没有描述的构建上限。
- `[未验证]` **npm 依赖树的安全态势。** 文档关于「报告的漏洞通常无害」的说明是读到了，但没有独立核实。
- `[未验证]` **classic 预设中的博客是否被多数文档站需要**——这是一个预设选择，本页只描述它随预设附带，而非必需。
