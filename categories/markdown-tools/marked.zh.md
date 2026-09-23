---
name: marked
slug: marked
repo: https://github.com/markedjs/marked
category: markdown-tools
tags: [markdown, parser, compiler, html, javascript, gfm, commonmark]
language: JavaScript
license: MIT
maturity: v18.x, active (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-23T04:04:16Z
  default_branch: master
  default_branch_sha: f8f411256680bfc870a4faba729409be68fcef4b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:34:14Z
  overall: A
  overall_score: 3.8
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 4.8
        qualifying_issues: 14
        band: default
        window_offset_days: 6
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: marked
        dependent_repos_count: 468889
        downloads_last_month: 281266053
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.04
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5539
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 17
        top1_share: 0.422
        top3_share: 0.554
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# marked

一个快速、低层的 JavaScript Markdown 解析器与编译器——一次函数调用就把 Markdown 变成 HTML，无强制依赖、API 面很小（口号是「Built for speed」）。

![marked — 健康度雷达](../../assets/health/marked.zh.svg)

## 何时使用

你在做一个 Web 应用——评论框、文档浏览器、聊天客户端、README 渲染——需要把用户或作者写的 Markdown 转成 HTML，无论在浏览器还是 Node 里，而又不想拉进一整套重型工具链。你想要 `import { marked } from 'marked'`，然后 `marked.parse(src)` 直接给你一个 HTML 字符串，又快，默认就带合理的 GFM 倾向（表格、围栏代码、自动链接）。你把它接进去，把输出接到 DOM（先做净化——见下文），就完事了；没有 AST 要学，没有插件清单要拼装，除了你本来的打包器之外没有额外构建步骤。

当*吞吐和简洁*比严格规范一致更重要时，它是对的选择：一个页面里渲染大量小段 Markdown、服务端渲染一个文档站，或任何你本来会手搓正则然后后悔的地方。marked 打包体积紧凑，在 Node 和浏览器里行为一致，并暴露刚好够用的钩子（一个 `renderer`、一次 `walkTokens` 遍历、一个可直接调用的 lexer），让你不用引入整条管线就能定制输出。

## 何时不用

- **你需要 100% CommonMark 一致。** marked 快、且向 CommonMark/GFM *倾斜*，但默认**并非**完全规范一致——边界情况会偏离参考实现。若精确的规范行为是硬性要求，请用 markdown-it（CommonMark 严格）或 remark。[推断]
- **你要渲染不可信 Markdown 又不做净化。** marked **不**净化它输出的 HTML——原始 HTML 和精心构造的链接会原样透传，所以朴素用法就是个 XSS 漏洞。你**必须**自己把输出过一遍 DOMPurify（或同类）；净化是被有意从 marked 自身职责里移除的。
- **你想把 Markdown 当 AST / mdast 管线来变换。** marked 的 token 模型是为渲染服务的，不是通用文档变换工具链。要做 lint、改写、MDX 或基于插件的 AST 遍历，请用 remark / unified。
- **你依赖庞大的插件生态。** marked 有扩展机制，但远不如 markdown-it 的插件目录。若你需要脚注、容器、KaTeX、任务列表等现成插件，markdown-it 或 remark 的现成零件更多。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [markdown-it](markdown-it.zh.md) | ✅ | 需要 CommonMark 严格、可插拔架构和丰富插件生态时，选 markdown-it。 | CommonMark 严格、可插拔架构，插件生态丰富；API 更重、比 marked 略慢，但当规范一致和插件重要时它是首选。 |
| [remark](remark.zh.md) | ✅ | 需要完整 mdast AST 管线来解析、变换、lint、序列化 Markdown/MDX 时，选 remark。 | 完整的 mdast AST 管线，能解析、变换、lint、序列化（Markdown、MDX）；强大得多也重得多——是工具链，不是一次调用的渲染器。 |
| [micromark](micromark.zh.md) | ✅ | 需要 remark 底层的 CommonMark/GFM 分词器并自建渲染层时，选 micromark。 | remark 底下那个低层 CommonMark/GFM 分词器；正确、面向流式，但渲染层要你自己搭。 |
| [CommonMark](commonmark.zh.md) | ✅ | 需要规范自己的参考实现作为一致性标尺时，选 CommonMark。 | 规范自己的参考实现；是一致性标尺，但 GFM 便利特性更少，也未针对生产渲染做优化。 |

## 技术栈

- **语言：** JavaScript（发布的源码是 JS 加 TypeScript 类型定义；仓库里也含用于工具/文档的 TS 和 HTML）。[推断]
- **运行目标：** 在 Node 和浏览器里都能跑；以 ESM 和 UMD/CJS 形式分发，也走 CDN。
- **架构：** 一个 lexer/分词器把 Markdown 变成 token，再由 parser/renderer 输出 HTML；通过 `Renderer`、`Tokenizer`、`walkTokens` 钩子和扩展 API 做定制。
- **风味：** 在 CommonMark 风格内核之上带 GFM 倾向的默认项（表格、删除线、自动链接、围栏代码）。

## 依赖

- **运行时：** 无强制依赖——marked 在设计上就轻依赖、可独立运行。[未验证]
- **净化器（你自己加）：** 对任何不可信输入，你必须把它和 DOMPurify 或别的 HTML 净化器搭配使用——不内置，被有意留作你的职责。
- **安装：** `npm install marked`，或从 CDN 加载预编译包；它还提供一个 CLI（`marked`）用于命令行转换。

## 运维难度

**低。** 它是库不是服务——除了给应用加一个依赖，没有任何要部署或运维的东西。唯一真正的运维顾虑是安全那条：记得在把输出注入 DOM 前先净化，并锁定/跟踪大版本，因为 API 在跨大版本时变过。没有数据存储、没有运行时、没有基础设施。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 4.8 小时，基于 14 个 qualifying issues/PRs。
- **维护——活跃（最近一次 push 在 2026-06）。** v18.x 线持续规律发布（v18.0.5，日期 2026-06-04）；对一个范围被刻意做小、已经稳定的成熟解析器而言，这是一个健康、issue 数很低的仓库（约 36k star 下约 16 个 open issue）[未验证]。
- **治理与 bus factor。** `Org` 所有（`markedjs/`）——是一个维护者团队/组织而非单人，相对单作者库降低了 bus factor 风险 [推断]。长期运行的社区项目，非厂商掌控；没有锁特性的商业层。
- **年龄与 Lindy 判断——老且仍活跃 ⇒ 强 Lindy。** 创建于 2011 年（约 15 岁），到 2026 年仍在发版：教科书式的「年龄 × 仍活跃」信号。一个 15 岁仍在出版本的解析器，在这一类里几乎是最稳的寿命押注；不过 API 跨大版本有变动，请锁定并跟踪大版本。
- **风险标记——很少，但安全责任在你。** MIT 许可，无 relicense 历史，无开放核心锁特性。唯一长期存在的告诫是设计使然：marked **不**净化输出，所以不可信输入必须你自己过一遍 DOMPurify——这是使用责任，不是项目健康度的标记。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 36.9k GitHub star，最新发布在 v18.x 线（v18.0.5，日期 2026-06-04）；star 数和版本随发布漂移，仅供参考。
- [推断]「默认非完全 CommonMark 一致」反映 marked 长期以来「速度优先、向规范倾斜」的定位；具体偏离取决于版本和你的配置——若一致性关键，请对照当前规范测试集核实。
- [未验证]「无强制运行时依赖」是 marked 自己的表述；请对照你所用版本的 `package.json` 核实，尤其在你启用可选特性时。
- [推断] 许可证为 MIT（GitHub 自动识别可能对该仓库显示 NOASSERTION）；请对照你锁定版本的 LICENSE 文件确认。
