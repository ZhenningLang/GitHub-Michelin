---
name: python-readability
slug: python-readability
repo: https://github.com/buriy/python-readability
category: article-extraction
tags: [content-extraction, readability, lxml, article-parsing, python, html]
language: Python
license: Apache-2.0
maturity: v0.8.x, maintained (low cadence), ~2.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-01-26T13:06:04Z
  default_branch: master
  default_branch_sha: 701833ccb24f9a15b463434f78229e4d6daf1c79
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:13:26Z
  overall: A
  overall_score: 3.67
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 26
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 5622
        last_commit_age_days: 26
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: ambiguous }
    governance: { reason: fork }
---

# python-readability

一个快速、基于 lxml 的 arc90 Readability Python 移植——递给它一个 HTML 文档，它返回清理过的正文（`summary()`）和标题（`title()`），剥掉导航、广告和样板。

![python-readability — 健康度雷达](../../../assets/health/python-readability.zh.svg)

## 何时使用

你在写一条 Python 抓取或内容管线——喂 LLM、建搜索索引，或归档文章——而 `requests.get(url).content` 给你的是整张页面，可你要的是文章。你不想仅仅为了抽文本就起一个 headless 浏览器或 Node DOM。于是你转向 python-readability：`pip install readability-lxml`，然后用 `Document(html).summary()` 拿清理过的文章 HTML、`Document(html).title()` 拿标题。它是纯 Python 跑在 lxml 上，所以快，且能直接嵌进 `requests`/`httpx` 流程——无浏览器、无 Node、无服务。它血统上承自和 JS 版同一套 arc90 Readability，所以启发式熟悉、在真实页面上相当稳健，还带 `positive_keywords`/`negative_keywords` 和 `keep_all_images` 等选项可调。

当你明确就想要 *Python、lxml* 那个实现时，你也会选它——比如你本就依赖 lxml/cssselect、想要 CJK 友好的抽取（近版改进了 CJK 支持），或需要一个小巧可嵌入的抽取器而非更重的 ML 模型。当你的栈是 Python、且输入 HTML 已经抓好时，它是务实的默认选择。

## 何时不用

- **你的页面是 JS 渲染的。** 它解析静态 HTML；不跑 JavaScript、也不抓 URL。对 SPA 你必须先渲染（Playwright/headless）再把得到的 HTML 传进来。
- **你想要最丰富的抽取/元数据或最佳基准精度。** 更新的 Python 抽取器（如 trafilatura）常抽出更多元数据、在抽取基准上得分更高；若质量至上，也评估它们。[未验证]
- **你需要一个维护活跃、快速迭代的项目。** 维护是真实的但**慢**——尽管代码仍在改动，GitHub 上最新的 release tag 已经很旧；别指望快速修复。请在你的输入上验证行为。[推断]
- **你需要结构化字段抽取。** 它返回正文 + 标题，而非任意结构化数据（价格、表格、产品规格）——那是另一类抓取活。
- **你不在 Python。** JS 场景用 [Readability.js](readability-js.zh.md)；移植版在启发式和输出上有别。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Readability.js](readability-js.zh.md) | ✅ | 需要 Mozilla 的 JavaScript 引擎、也就是 Firefox Reader View 背后的实现时，选 Readability.js。 | Mozilla 的 JS 引擎，Firefox Reader View 背后那个；按语言选（JS/Node）——启发式不同，需要 DOM。 |
| [dragnet](dragnet.zh.md) | ✅ | 需要 Python 里的 ML-based 抽取时，选 dragnet。 | 基于 ML 的抽取（Python）；在某些页面上可胜出，但更重、pin 的依赖老化、维护较少。 |
| [boilerpipe](boilerpipe.zh.md) | ✅ | 需要 Java 样板移除算法时，选 boilerpipe。 | Java 样板移除算法；经典，但仓库实际已废弃（最后 push 2018）。 |
| [trafilatura](trafilatura.zh.md) | ✅ | 需要现代 Python 抽取库，带强基准、元数据和爬取功能时，选 trafilatura。 | 现代 Python 抽取库，基准强、带元数据和爬取功能；常是当下 Python 默认——范围更广、更重。 |
| newspaper3k / goose3 | 未收录 | 需要自带抓取和元数据的文章抽取库时，选 newspaper3k 或 goose3。 | 自带抓取和元数据的文章抽取库；方便，但历来维护起伏不定。 |

## 技术栈

- **语言：** Python。
- **核心依赖：** **lxml**（`lxml[html_clean]`，Python <3.11 上配 `lxml-html-clean`）、**chardet**（编码检测）和 **cssselect**。
- **API：** `from readability import Document` → `Document(html).summary()`（清理过的文章 HTML）和 `.title()`；选项含 `positive_keywords`、`negative_keywords`、`keep_all_images`，以及显式 `encoding`。
- **分发：** 以 `readability-lxml` 发布于 PyPI（也在 conda-forge）。

## 依赖

- **运行时：** Python 加 lxml、chardet、cssselect——全部 pip 可装，无系统服务。lxml 带原生（libxml2）绑定，所以某些平台上 wheel 很关键。[推断]
- **不抓取：** 它不取 URL；HTML 由你提供（通过 `requests`/`httpx`/你的爬虫）。
- **无 DOM/Node/浏览器：** 与 JS 移植版不同，不需要 DOM 运行时。
- **安装：** `pip install readability-lxml` 或 `conda install -c conda-forge readability-lxml`。

## 运维难度

**低。** 它是一个小库，不是服务——没什么要部署或跑。唯一的实际考量是安装 lxml（原生依赖；通常是预编译 wheel，偶尔要构建）、自己提供抓好的 HTML，以及在目标站点上验证抽取质量。规模化时它是 CPU 受限的解析、无外部状态——可轻松跨 worker 并行。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 push 于 2026-01，所以仓库**仍在改动**——但 GitHub 上最新的 release tag 已旧（v0.8.1 可追溯到 2020），changelog 提到后续 0.8.x 工作；当作**有维护但低节奏/吃老本**，而非快速迭代。未归档。[推断]
- **治理 / bus factor。** owner 类型是 **User**（`buriy`），即一个单维护者项目带社区贡献——一个 **bus-factor 标记**：延续性很大程度系于一人。[推断]
- **年龄 × Lindy（2026-06）。** 2011-05 创建——约 15 岁且**仍偶有维护**⇒ 对一个小抽取器是**强 Lindy** 信号；它早已熬过多数同侪。这里的长寿是真实的耐用性，而非废弃。[推断]
- **采用度与生态。** 约 2.9k star、在 PyPI 和 conda-forge 上，且长期是许多 Python 抓取栈的默认选项，表明扎实的细分采用度。约 37 个 open issue，小且可控。[未验证]
- **风险标记。** 单维护者 bus factor 和慢节奏是真实风险；对精度攸关的工作，请与 trafilatura 做基准对比。Apache-2.0，未发现 relicense 历史。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 2.9k star；GitHub 最新 release tag 是 v0.8.1（2020），而 changelog 提到更晚的 0.8.x 版本——本页版本记法为近似（"v0.8.x"）；pin 前请确认当前确切的 PyPI 版本。
- [推断] “有维护但低节奏/吃老本”由 2026-01 的 push 日期结合陈旧的 release tag 推断——代码活动与 tag 发布之间的落差。
- [推断] 单维护者 bus factor 由 `owner.type == User` 推断；实际贡献者广度/接班计划未核实。
- [推断] lxml 的原生（libxml2）构建/wheel 考量是 lxml 通识，未对本仓库当前打包核实。
- [未验证] 与 trafilatura/newspaper3k 的相对精度反映总体定位，而非实测基准。
