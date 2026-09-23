---
name: newspaper
slug: newspaper
repo: https://github.com/codelucas/newspaper
category: article-extraction
tags: [article-extraction, news, web-scraping, nlp, content-extraction, metadata, python]
language: Python
license: MIT
maturity: "newspaper3k 0.2.8 (last PyPI 2018-09), codebase stale since ~2020; active fork newspaper4k — ~15.1k stars (as of 2026-06)"
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-05-13T04:02:34Z
  default_branch: master
  default_branch_sha: b97791d8f5187387782ca0f8b5de19b996f7f258
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:13:16Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 7
        active_weeks_13: 5
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: newspaper3k
        dependent_repos_count: 1068
        downloads_last_month: 526510
        graph_tier: B
        volume_tier: B
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4684
        last_commit_age_days: 7
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
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

# newspaper

一个 Python 库：给它一个新闻/文章 URL，它就下载、解析，吐出干净的正文、标题、作者、发布日期、头图，以及（可选的）NLP 关键词/摘要——样板内容剥掉，不用为每个站点手写抓取规则。

![newspaper — 健康度雷达](../../../assets/health/newspaper.zh.svg)

## 何时使用

你是数据工程师，在搭一条媒体监测流水线，手里有几千个新闻文章 URL——新闻稿、报纸报道、博客文章。你不在乎导航栏、广告位、评论组件或 cookie 横幅，你要的是*正文*、标题、谁写的、什么时候发的、头图，每个 URL 一个干净的 dict。给每家媒体写一套定制 CSS/XPath 提取器会是上百条脆弱规则，所以你改用 `newspaper`：对每个 URL 执行 `Article(url).download()`、`.parse()`，然后读 `.text`、`.title`、`.authors`、`.publish_date`、`.top_image`。再调 `.nlp()`，还能拿到 `.keywords` 和一个朴素的 `.summary`。对单一媒体，你可以建一个 `Source` 来发现并批量取它的文章 URL。

当输入是*文章形态*、而你想要一个通用提取器而非 N 个站点专用提取器时，它最出彩——这就是经典的「把这条新闻链接背后的可读正文给我，规模化地给」的活：在很多域名上「大致正确」的启发式，胜过逐站手调。

## 何时不用

- **页面不是文章形态。** 它针对新闻/文章版式。在靠 JS 渲染的 SPA、付费墙或登录墙页面、列表/搜索/首页、产品页或论坛上，它返回空或乱码 `.text`——它解析的是静态 HTML，不是无头浏览器。
- **你需要高或有保证的提取准确率。** 启发式的样板剥离因站点差异很大；预期在相当一部分页面上漏段落、作者识别错、日期为空。在*你自己的*来源上先做基准测试再信它。[未验证]
- **你装的是原版 `newspaper3k`。** 上游 `codelucas/newspaper` 实质上已停滞（最后 PyPI 发布在 2018 年，代码库自 ~2020 起沉寂）。维护中的路径是社区分叉 **newspaper4k**（`AndyTheFactory/newspaper4k`）——新项目优先选它。[未验证]
- **你需要爬虫/调度器。** 它只下载并解析你交给它的 URL；它不是分布式爬虫、队列或调度器。要做带重试/礼貌/管线的大规模爬取，请用 Scrapy。
- **你需要任意结构化抓取。** 要从非文章页面提取表格、价格或字段，选择器/提取框架（Scrapy + parsel）或通用 readability 提取器比文章正文启发式更合适。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [trafilatura](trafilatura.zh.md) | ✅ | 需要维护活跃、专注正文和元数据提取的工具时，选 trafilatura。 | 专注正文 + 元数据提取；通常提取更强更干净且维护活跃——如今做「只要正文」往往是更好的默认选项。 |
| readability-lxml | 未收录 | 需要 Arc90 Readability 移植版且只做正文提取时，选 readability-lxml。 | Arc90 Readability 的移植；只做正文提取（无作者/日期/头图/NLP），面更小、更简单。 |
| [boilerpipe](boilerpipe.zh.md) | ✅ | 需要较老的 Java 样板剥离算法及 Python 封装时，选 boilerpipe。 | 较老的 Java 样板剥离算法（带 Python 封装）；历史上有影响力，但有 JVM 依赖且偏老。 |
| Scrapy + 定制 | 未收录 | 需要完整爬取框架时，选 Scrapy 加自写提取规则。 | 完整爬取框架——你自己写提取规则，但能拿到队列、并发、重试、管线；当你需要的是*爬虫*而非单 URL 提取器时的正解。 |
| Goose3 | 未收录 | 需要 Goose 文章提取器的 Python 移植版时，选 Goose3。 | Goose 文章提取器的 Python 移植；和 newspaper 同一生态位（正文/元数据/头图），启发式不同——可直接拿来做基准对比的同类。 |
| newspaper4k | 未收录 | 需要本项目维护中的分叉时，选 newspaper4k。 | 正是本项目维护中的分叉；同一 API 血统，修 bug、跟进 Python 版本——推荐的继任者。 |

## 技术栈

- **语言：** Python 3。
- **解析：** `lxml` 做 HTML 解析，以及标题/正文/作者/日期的 XPath/启发式提取。
- **抓取：** `requests` 做 HTTP 下载（仅静态 HTML——不执行 JS）。
- **图像/NLP：** 头图检测的图像处理；可选的 NLP 步骤（关键词 + 抽取式摘要），背后用 NLTK 语料和停用词/词性方法。

## 依赖

- **运行时：** Python 3，加上 `lxml` 和 `requests`（及其传递的 C/HTTP 依赖）。
- **NLP 数据：** `.nlp()` 路径需要先下载 NLTK 数据（如 `punkt`）一次；没有它，`.text`/元数据仍可用，但关键词/摘要会失败。
- **无服务：** 不需要数据库、服务器或浏览器——它是一个进程内的库，按 URL 逐个调用。

## 运维难度

**低。** 它是一个 `pip install` 的库，没有基础设施——没有服务器、数据存储或浏览器要跑。真正的运维成本在于*规模化下的质量与健壮性*：会报错或超时的页面、会封爬虫的站点、需要你检测并跳过的空提取，以及 NLP 功能那一次性的 NLTK 语料下载。并发、限速、重试逻辑由你自己负责（库一次只处理一个 URL）。请钉到维护中的分叉（newspaper4k），以免跑在一个停滞的依赖上。[未验证]

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（截至 2026-06）。** 上游 `codelucas/newspaper`（newspaper3k）实质停滞：最后 PyPI 发布 0.2.8 在 2018-09，代码库自 ~2020 起沉寂。即便仓库带着「pushed 2026-05」的时间戳，看起来也更像一次琐碎的 touch 而非开发复活——把原版当作维护模式/已弃，而非活跃演进。[未验证]
- **治理 / bus factor。** 单一维护者、`User` 所有的仓库（Lucas Ou-Yang）——典型的 bus-factor 风险，而且这里维护者大体已转向他处。更健康的路径是社区分叉 **newspaper4k**，由 Andrei Paraschiv 维护（`AndyTheFactory/newspaper4k`），其维护状况被评为健康、发布节奏规律。[未验证]
- **年龄与 Lindy 判断。** 2013-11 创建（约 13 年）——这个*概念*久经验证、足够耐用，所以对「想法」的 Lindy 很强；但 Lindy 要的是 **年龄 × 仍活跃**，而原版已不再活跃。年龄信号转移到了延续血脉的 newspaper4k 身上。[推断]
- **采用度。** 约 15.1k star，加上在教程和流水线里极广的历史使用，表明采用度强、装机量大；不过相当一部分注意力正在向 newspaper4k 和 trafilatura 迁移。[未验证]
- **风险标记。** 维护/时效性是*那个*标记——在现代 Python 和现代站点上跑原版，会有未修 bug 的风险。许可宽松（MIT）；未发现 relicense 或 open-core 顾虑。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 15.1k GitHub star——star 数不可靠且对时间敏感，仅供参考。
- [未验证] newspaper3k 最后 PyPI 发布是 0.2.8（2018-09），代码库据称自 ~2020 年 9 月起沉寂；任何 2026 年的仓库「pushed」时间戳未被确认反映实质开发。
- [未验证] newspaper4k（`AndyTheFactory/newspaper4k`）据称是维护中、节奏健康的社区分叉；依赖它前请核实其当前发布/活跃情况。
- [未验证] 提取准确率本质上因站点而异；「准确率参差」是启发式提取器的普遍性质，而非对任一具体来源的实测数字。
- [未验证] 确切的依赖集（lxml/requests/Pillow/NLTK 及版本）与所需 NLP 语料在 newspaper3k 与 newspaper4k 之间、以及各版本之间都有差异——请对照你实际安装的版本核实。
- [推断] 2013-11 创建（约 13 年）作为 Lindy/年龄信号给出；该耐用性推断适用于文章提取这个想法和仍在活跃的分叉，而非停滞的原版。
