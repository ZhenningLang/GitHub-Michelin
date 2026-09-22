---
name: Mermaid
slug: mermaid
repo: https://github.com/mermaid-js/mermaid
category: diagramming
tags: [diagram, flowchart, text-to-diagram, markdown, sequence-diagram, gantt, visualization, javascript]
language: TypeScript
license: MIT
maturity: active, ~89k stars (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-29T10:42:57Z
  default_branch: develop
  default_branch_sha: 338c98df454b7587f4e4a8a73c5dcbbd59ba3175
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:22:41Z
  overall: A
  overall_score: 4.0
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 42.9
        qualifying_issues: 28
        band: default
        window_offset_days: 7
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@mermaid-js/parser"
        dependent_repos_count: 1
        downloads_last_month: 32486503
        graph_tier: D
        volume_tier: A
        cross_check_divergence: 1.03
    longevity:
      grade: A
      raw:
        repo_age_days: 4261
        last_commit_age_days: 2
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 86
        top1_share: 0.136
        top3_share: 0.353
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

# Mermaid

一个 JavaScript/TypeScript 库，用一种类 Markdown 的文本语法渲染图表——流程图、时序图、甘特图、类图、ER 图、状态图、git-graph、饼图、思维导图等等——让图表以纯文本形式进版本库，而不再是二进制图片文件。

![mermaid — 健康度雷达](../../assets/health/mermaid.zh.svg)

## 何时使用

你是个工程师，架构文档和 runbook 一直写在 Markdown 里，而图表一直在烂掉：一年前有人用 draw.io 画了流程、导出成 PNG，如今 PNG 已经过时，但没人手里还有源文件。你想让图*活在*文档里、能在 PR 里 diff、自动重渲。于是你写一个 ` ```mermaid ` 围栏块，几行 `graph TD; A-->B`，推上去，GitHub、GitLab、你的文档站（Docusaurus、MkDocs、Obsidian）和 IDE 预览全都内联渲染出来——没有二进制资产、不用外部编辑器、不会有坏掉的导出。流程一改，你只改文本，图就跟着变；评审看到的是*图本身*的 diff，而不是被换掉的一张图片。

当你是个 agent 或工具、要程序化生成图时，你也会选它：输入就是可模板化、可拼接生成的文本，所以从代码或从 LLM 产出一张时序图或 ER schema 不过是字符串拼装，再在浏览器/无头环境里 `mermaid.render()`（或用 `@mermaid-js/mermaid-cli` 的 `mmdc`）拿到 SVG/PNG。它之所以成了事实上的文本转图格式，正是因为太多宿主平台已经认得这个围栏块——你只要瞄准 Mermaid，就白白继承了 GitHub/GitLab/Notion 那一套渲染。

## 何时不用

- **你需要像素级精确或手工微调的排版。** Mermaid 用它的布局引擎自动排版；节点不是你手摆的。当确切位置、间距或连线走向很要紧时，手动画布（draw.io/diagrams.net、Excalidraw）或一门你能调控的布局语言（Graphviz/DOT、D2）能给你 Mermaid 有意不给的控制力。
- **大或稠密的图。** 节点/边一多，自动布局质量和渲染性能都会下降；大流程图会画得乱成一团、读不下去。要在规模上做认真的图布局，Graphviz（成熟的布局算法）或基于 ELK 的引擎更强。[未验证]
- **它会在渲染器里跑 JavaScript。** Mermaid 在浏览器/JS 运行时里执行，历史上有过 XSS 面；渲染*不可信*的图文本意味着你必须把 `securityLevel`（`strict`/`sandbox`）设对，并接受部分交互功能因此被禁。别用 `securityLevel: 'loose'` 去渲染攻击者可控的 Mermaid。
- **你想要所见即所得的画图工具。** 没有拖拽画布——你编辑的是文本。指望推方块的非技术干系人不会满意；给他们 draw.io 或 Excalidraw。
- **它做得不好或根本不覆盖的图类型。** 高度自定义/自由形态的图、超出支持子集的严格 UML，或某些很特定的记号法，可能用 PlantUML（更广更严的 UML）或通用画图工具更合适。在把它定为标准前，先核实你具体那个图类型渲染得能接受。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Graphviz / DOT | 未收录 | 大型或稠密图的成熟布局算法比 Markdown 原生渲染更重要时，选 Graphviz。 | 成熟、可脚本化的图**布局**引擎，对大/稠密图有强算法；自动布局极佳，但 DOT 更底层，且不像 Mermaid 那样被文档平台原生内联渲染。 |
| [PlantUML](plantuml.zh.md) | ✅ | 需要更广、更严格的 UML 覆盖，并能接受 Java/服务端渲染时，选 PlantUML。 | UML 覆盖更广更严（图类型也更多）；通常需要 Java 运行时/服务来渲染，而 Mermaid 是纯 JS 浏览器内渲染、宿主支持无处不在。 |
| [D2](d2.zh.md) | ✅ | D2 的新语言和布局引擎选择比 Mermaid 的宿主平台普及度更重要时，选 D2。 | 较新的文本转图语言（Go），有多种布局引擎（含 ELK/dagre）、追求更干净的排版；安装量小得多，内建宿主平台渲染远不如 Mermaid。 |
| draw.io（diagrams.net） | 未收录 | 需要完整所见即所得画布，而不是可版本控制的图源码时，选 draw.io。 | 完整的所见即所得画布编辑器——像素级控制、丰富图形——但图存为 XML/二进制，不是可 diff 的纯文本，也不会从围栏块自动渲染。 |
| [Excalidraw](excalidraw.zh.md) | ✅ | 手绘风白板和协作比文本转图语法更重要时，选 Excalidraw。 | 手绘风的所见即所得白板；适合草图和协作，不是文本转图语法，源文件也不能在版本库里 diff。 |
| [flowchart.js](flowchart-js.zh.md) | ✅ | 只需要一个窄的流程图 JS 库时，才选 flowchart.js。 | 只做流程图的窄 JS 库；Mermaid 覆盖的图类型多得多，生态/宿主支持也大得多。 |

## 技术栈

- **语言：** TypeScript（夹带大量 JavaScript），以 npm 包和 CDN（jsDelivr）分发；另有 `@mermaid-js/mermaid-cli`（`mmdc`）用于无头渲染。
- **渲染：** 浏览器/DOM——产出 SVG。用 **D3.js** 操作 SVG、用 **dagre / dagre-d3** 做图布局；部分图类型/配置可走基于 ELK 的布局。
- **语法：** 每种图类型一套受 Markdown 启发的 DSL(`graph`/`flowchart`、`sequenceDiagram`、`classDiagram`、`erDiagram`、`stateDiagram`、`gantt`、`gitGraph`、`pie`、`mindmap`、`journey`、C4……)。
- **配置/安全：** 运行时配置对象含 `securityLevel`(`strict` / `loose` / `antiscript` / `sandbox`)，控制脚本执行与沙箱 iframe 渲染。[未验证]

## 依赖

- **运行时：** 一个带 DOM 的 JavaScript 环境。生产里那就是用户浏览器（或某个已打包它的宿主平台——GitHub/GitLab/Notion/Docusaurus/MkDocs/Obsidian）。服务端/CLI 渲染则需要无头浏览器（CLI 底层用 Puppeteer/Chromium）。
- **库依赖：** 作为 npm 依赖拉进 D3 和 dagre（及其传递依赖）；没有需要运维的服务。
- **安装路径：** `npm i mermaid`、从 jsDelivr CDN `<script>`，或 `npm i -g @mermaid-js/mermaid-cli` 装 `mmdc`。
- **无后端/数据存储：** 它是客户端渲染库，不是服务。

## 运维难度

**低**（常见情形）：没有东西要部署或运维——你往一个已能渲染 Mermaid 的平台里塞一个围栏块，或给页面加上 npm/CDN 脚本。只有当你*自己*渲染时才出现“运维”：用 `mermaid-cli` 做服务端/无头渲染会拖进 Chromium/Puppeteer 依赖，这通常是 CI 崩溃、沙箱/权限问题和镜像膨胀的根源。另一个真正的隐患是**安全**而非可用性：一旦你要渲染不可信的图文本，把 `securityLevel` 设对（并持续打补丁对抗 XSS 公告）就是维护负担。作为一个钉死版本的库依赖，它很省心；自动布局的输出偶尔会在版本间漂移，所以升级时要盯的是视觉回归。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 42.9 小时，基于 28 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06，近期有发布（如 `@mermaid-js/tiny@11.16.0`，2026-06-25）——处于**活跃**维护，未归档。[推断]
- **治理 / bus factor。** 归属 `mermaid-js` GitHub 组织（多维护者的社区项目，而非单作者仓库），相比单人维护的库降低了 bus-factor 风险。没有单一公司所有者。[推断]
- **年龄与 Lindy 判断。** 约 12 年（2014-11 创建）且仍活跃 ⇒ **强 Lindy** 信号；它是事实上的文本转图标准，被 GitHub/GitLab/Notion/Docusaurus/Obsidian 内嵌。[推断]
- **采用度与生态。** 采用度极大——约 89k star，更有意义的是主流平台内建的一流渲染——使它成为「图即代码」的安全默认选项。[未验证]
- **风险标记。** 未发现 relicense（MIT），也无商业 open-core 切分；长期隐患是**安全**而非可持续性——它在渲染器里跑 JS、历史上有过 XSS 面，渲染不可信输入时必须设置 `securityLevel`。约 1.6k open issue 对这种覆盖面的项目而言属正常，并非健康红旗。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06，仓库页显示约 88.9k GitHub star、主语言 TypeScript;star 数对时间敏感且为近似。
- [未验证] 观察到的最新发布是仓库 releases 里的 `@mermaid-js/tiny@11.16.0`(2026-06-25)；主 `mermaid` 包的版本号和当前确切数字随版本变动——钉版本前查 npm/releases。
- [未验证] 布局/渲染内部实现（D3 + dagre/dagre-d3，可选 ELK 引擎）系据 README 和通用认知陈述；每种图类型实际用的引擎与默认值随版本变化——请对照当前文档核实。
- [未验证] `securityLevel` 的取值及其确切效果（脚本执行、沙箱 iframe、禁用交互）系据文档概括；渲染不可信输入前，请核实你那个版本的当前取值集与默认值。
- [未验证] CLI/无头渲染依赖 Puppeteer/Chromium 系据 `@mermaid-js/mermaid-cli` 的通常实现推断；请确认当前渲染器及其系统要求。
- [推断] 大/稠密图上的性能与质量下降是自动布局的一般性质，而非对本库的实测基准；在定型前先用你最大的真实图测一遍。
- [推断] “某些图类型做得不好”是对自动布局适配度的推断，不是针对某一类型的缺陷断言——请评估你具体那个图类型。
