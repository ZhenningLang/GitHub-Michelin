---
name: Markdown Here
slug: markdown-here
repo: https://github.com/adam-p/markdown-here
category: markdown-tools
tags: [inline]
language: JavaScript
license: MIT
maturity: "v2.16.0, low-cadence/effectively stale, ~60.2k stars (last pushed 2025-08)"
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2025-08-22T00:21:50Z
  default_branch: master
  default_branch_sha: e00d005299922198aef968e0cd42b275525c20a6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:34:02Z
  overall: C
  overall_score: 1.75
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: D
      raw:
        archived: false
        last_commit_age_days: 440
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: proxy.golang.org
        canonical_package: github.com/adam-p/markdown-here
        dependent_repos_count: 1
        downloads_last_month: null
        graph_tier: D
        volume_tier: "?"
        cross_check_divergence: null
        release_downloads: 13458
        release_assets: 6
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 5246
        last_commit_age_days: 440
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# Markdown Here

一个 Chrome/Firefox/Thunderbird 浏览器扩展，把你在受支持的邮件或网页 textarea 里敲的 Markdown 就地转成渲染好的 HTML——点发送前点一下即可。

![markdown-here — 健康度雷达](../../assets/health/markdown-here.zh.svg)

## 何时使用

你是个写大量邮件的工程师——code review 笔记、事故复盘、“按这步复现”的操作说明——而你的网页邮箱给你的只是一个干巴巴的 textarea 配一个笨重的所见即所得工具栏。你想要一个带项目符号的列表、一段带语法高亮的代码块、一张表格、再加几个链接，用工具栏手动排出这些又慢又难看。于是你装上 Markdown Here，像写 `README` 那样用纯 Markdown 把信打出来，写好后按一下切换键（或快捷键）：扩展会把那个字段里的 Markdown 解析掉，就地替换成渲染好的 HTML，于是收件人在任意邮件客户端里看到的都是排好版的内容。要是哪里写错了，可以切回 Markdown 源码改好再重渲染。它在不少非邮件的网页 textarea 里也会生效（Google Groups、部分博客/论坛的撰写框），同一套肌肉记忆在邮件之外也用得上。

它之所以站得住脚，恰恰在于它是*就地、按需*地作用在你掌控不了的字段上：你不是导出文件、也不是跑构建，而是在发送那一刻把撰写框里已有的文本变成 HTML。对于“这一封邮件用 Markdown 写”这个很窄的活，它比在外部编辑器里起草再粘回来轻得多。

## 何时不用

- **维护 / 寿命风险——最尖锐的理由。** 原仓库被普遍视为低维护/事实上停滞：star 很高，但发布节奏慢、积压长。[推断] 别把一个*依赖*它及时修 bug 的工作流建在它上面。
- **Manifest V3 下的浏览器扩展可用性。** 它是个跑在 Chrome MV3 迁移浪潮里的 content-script 扩展；一个无人维护的 MV3 扩展可能被下架，或被浏览器更新弄坏，这是你掌控范围之外的可用性风险。[未验证]
- **它只在*受支持*的字段里按需转换。** 它不是无处不在的“到处都能 Markdown”层——只在它做了集成的邮件客户端和 textarea 里、且只在你触发切换时才工作。目标字段若不在支持范围内，它什么都不做。
- **你要的是给程序用的 Markdown *渲染器/库*。** 这是个 UI 便利工具，不是 API。要在代码里（站点、文档构建、服务端）把 Markdown 解析成 HTML，请用 marked 这类解析库——Markdown Here 没法被嵌入调用。
- **文档 / 发布管线。** 静态站点、知识库或 CI 渲染的文档，你要的是确定性的构建步骤和真正的渲染器，而不是一个一次只切换一个撰写框的浏览器扩展。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [marked](marked.zh.md) | ✅ | 需要一个供 JavaScript 调用的 Markdown→HTML *解析库*时，选 marked。 | 一个供 JavaScript 调用的 Markdown→HTML *解析库*；当你需要在 app 或管线里做渲染时它才是对的工具——但它不是浏览器 UI，编辑器/撰写框集成得你自己接。 |
| 浏览器原生富文本撰写（Gmail/Outlook 工具栏） | 未收录 | 需要邮件客户端内置能力且不想安装扩展时，选浏览器原生富文本撰写。 | 邮件客户端自带、无需安装；但它是工具栏式所见即所得，没有 Markdown，代码块/表格支持也弱——正是 Markdown Here 要消除的摩擦。 |
| Obsidian / 编辑器 Markdown 插件 | 未收录 | 需要文档编辑器里的 Markdown 写作和实时预览时，选 Obsidian 或编辑器插件。 | 一流的 Markdown 写作加实时预览，但是在*文档编辑器*里，而非你的网页邮箱撰写框；你得在那边起草再粘过来，丢掉了就地、发送时转换那一环。 |
| Markdown Here Revival（分叉/后继） | 未收录 | 明确需要社区后继分叉，尤其围绕 Thunderbird 继续使用时，选 Markdown Here Revival。 | 一个社区分叉，意在让这个点子活下去（尤其面向 Thunderbird），因为原项目停滞了；其托管位置和自身维护状态在依赖前需自行核实（见存疑）。 |

## 技术栈

- **语言：** JavaScript——一个浏览器/WebExtension content-script 扩展（撰写框那部分代码跑在页面里，转换逻辑随扩展一起打包）。
- **Markdown 渲染：** Markdown 被解析成 HTML，代码块带语法高亮；项目自带打包的 JS 渲染/高亮，而非调用外部服务（见存疑）。
- **目标平台：** 打包给 Chrome（及 Chromium/Opera）、Firefox 和 Thunderbird，并为一组网页邮箱与网页 textarea 撰写界面做了集成。

## 依赖

- **运行时：** 一个受支持的浏览器（Chrome/Chromium/Opera、Firefox）或 Thunderbird——没有服务器、账号或后端，一切都在扩展里客户端运行。
- **分发：** 从浏览器/扩展商店安装，或作为未打包/已打包扩展加载；受该商店的审核与 Manifest 版本要求约束。
- **构建：** 从源码构建需要 Node/JS 工具链；具体版本由仓库的构建工具在构建时决定。

## 运维难度

**低。** 没什么要运维的——没有服务、数据存储或部署。对终端用户它就是个装上即切换的扩展。真正的“运维”成本是*寿命*而非运行：因为原项目推进缓慢，现实风险在于未来某次浏览器变更（尤其是 MV3 迁移）把它弄坏或下架，而没有及时的修复落地，到那时你得迁移到某个维护中的分叉或换条路。把它当成一个可能会失去的便利工具，而不是你赖以为生的基础设施。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护——事实上停滞（最近一次 push 约 2025-08，截至 2026-06）。** 没有 archive 标记，但相对于它的人气，发布节奏很低、积压很长；当作「滑向废弃的吃老本」而非「积极维护」来看待 [推断]。README 并未宣告项目已死——但别指望及时修复。
- **治理与 bus factor——单人维护风险。** `User` 所有（`adam-p/`），约 60k star：典型的 bus factor 风险，海量采用全压在一个人的注意力上，而这份注意力显然已减弱。社区的回应是「Markdown Here Revival」分叉，这本身就是「原项目不再是维护中那条路」的信号 [推断]。
- **年龄与 Lindy 判断——老但已废弃 ⇒ Lindy 不成立。** 创建于 2012 年（约 14 岁）：单看年龄令人安心，但检验标准是「年龄 × 仍活跃」，而活跃已停止。一个长寿后停滞的项目，正是 Lindy 先验转为*负面*的情形——押维护中的分叉，别押原项目。
- **风险标记。** Manifest V3 下的浏览器扩展可用性：一个无人维护的 MV3 content-script 扩展，可能被浏览器更新下架或弄坏而无修复落地——这是你掌控之外的可用性风险 [未验证]。MIT 许可，所以分叉无负担（Revival 分叉即由此而来）。

## 存疑（未验证）

- [未验证] 约 60.2k GitHub star、v2.16.0、最近一次 push 约在 2025-08（据仓库，2026-06 核对）；star 数和日期对时间敏感，仅供参考——请对照当前仓库重核。
- [推断] “低维护 / 事实上停滞”是从发布节奏慢、相对 star 数而言积压大推断出来的，而非 README 里有什么废弃声明——README 并未宣告项目已死。
- [未验证] Manifest V3 状态、以及该扩展当前是否在各浏览器商店上架/可安装，会随时间变化；依赖前请在目标浏览器里核实。
- [未验证] 受支持的邮件客户端与网页 textarea 的确切清单、以及每个集成的可用程度各不相同且可能已回退——请确认你具体的撰写界面能用。
- [未验证] “Markdown Here Revival”作为社区分叉/后继确有其事（尤其面向 Thunderbird），但其权威托管位置和当前维护状态本次未能确认——采用前请核实。
