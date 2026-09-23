---
name: Firecrawl
slug: firecrawl
repo: https://github.com/firecrawl/firecrawl
category: crawling-tools
tags: [web-scraping, ai-crawler, markdown, data-extraction, api]
language: TypeScript
license: AGPL-3.0
maturity: v1.x, active, 142k stars (as of 2026-07)
last_verified: 2026-07-01
type: service
upstream:
  pushed_at: 2026-07-06T07:42:51Z
  default_branch: main
  default_branch_sha: 84d736273d3165cb4da718b6b75a5d966dc7fd5d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:13:59Z
  overall: B
  overall_score: 3.0
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
      grade: B
      raw:
        median_ttfr_hours: 52.0
        qualifying_issues: 34
        band: default
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: firecrawl-py
        dependent_repos_count: 0
        downloads_last_month: 6277142
        graph_tier: E
        volume_tier: A
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 890
        last_commit_age_days: 0
        cohort: service
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: empty_or_gated }
---

# Firecrawl

一款可规模化搜索、抓取并与网页交互的 API——将原始网页转化为干净的 Markdown 或结构化数据，供你的 agent 直接使用。

![Firecrawl — 健康度雷达](../../../assets/health/firecrawl.zh.svg)

## 何时使用

你正在构建一个需要大规模摄入网页内容的 AI agent 或数据流水线，而你需要干净、结构化的输出，而非原始 HTML。你考虑过写 Scrapy 爬虫或 Playwright 脚本，但维护浏览器自动化、处理反爬，以及把 messy HTML 转成 Markdown 并非你的核心工作。你选择 Firecrawl，因为它是一个 API 优先的服务，替你处理搜索、抓取，甚至浏览器交互（点击、导航），返回结构化的 Markdown 或 JSON，无需你自己管理爬虫基础设施。需要别人替你完成提取和转换层，而不是调度自己手写的爬虫时，选 Firecrawl 而非 [Scrapyd](scrapyd.zh.md) 或原生 Scrapy；需要大规模通用网页抓取、搜索与交互，而非单页文章提取时，选 Firecrawl 而非 [newspaper](../article-extraction/newspaper.zh.md) 或 [Readability.js](../article-extraction/readability-js.zh.md)。如果你需要托管 API，同时希望有 AGPL-3.0 开源自托管选项，Firecrawl 比专有替代品更贴合。


## 何时不用

- **简单的一次性抓取**——如果你只需要单页或偶尔抓取，用 `curl` + `pandoc` 或 `trafilatura` 代替 Firecrawl，因为为偶发任务付费或自托管完整的爬虫 API 属于杀鸡用牛刀。
- **严格的闭源合规要求**——如果你需要宽松许可、无网络 copyleft 义务的抓取工具，用 [newspaper](../article-extraction/newspaper.zh.md)（MIT）或 `trafilatura`（Apache-2.0）代替 Firecrawl，因为 AGPL-3.0 要求修改并分发服务时共享源码。[未验证]
- **大规模预算受限**——如果你需要高频抓取而不想按请求付费，用自建基础设施上的 Scrapy 或 Playwright 代替 Firecrawl 的托管服务，因为 API 定价在规模化时会显著增长，且自托管 Firecrawl 仍需管理 Node.js 和浏览器自动化。
- **深网 / 需认证站点**——如果你需要复杂的登录流程和跨站会话管理，用自定义 Playwright 脚本代替 Firecrawl，因为虽然它支持交互，但复杂的多步认证和有状态爬取更适合由你直接控制的浏览器自动化。


## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Scrapyd](scrapyd.zh.md) | ✅ | 自托管 Scrapy 爬虫调度器。 | Scrapyd 用于运行你手写的 Scrapy 爬虫；Firecrawl 是一个直接帮你完成抓取与提取的 API。 |
| [newspaper](../article-extraction/newspaper.zh.md) | ✅ | 从新闻 URL 提取文章正文。 | newspaper 仅限 Python 且聚焦文章；Firecrawl 是全功能 API，支持搜索、抓取与交互。 |
| [Readability.js](../article-extraction/readability-js.zh.md) | ✅ | Firefox 阅读视图文章提取。 | Readability.js 是浏览器库，用于文章提取；Firecrawl 是可扩展 API，支持搜索与交互。 |
| [PRAW](praw.zh.md) | ✅ | Reddit 专用 API 封装。 | PRAW 仅限 Reddit；Firecrawl 是通用网页抓取。 |
| Scrapy / [Playwright](../../web-automation/playwright-family/playwright.zh.md) | 部分已收录 | 底层抓取框架。 | Scrapy 和 Playwright 提供完全控制，但需要自建和维护爬虫基础设施。 |

## 技术栈

- **TypeScript**——主要实现语言
- **Node.js**——API 服务器运行时
- **Docker**——容器化部署选项
- **Playwright**——JS 渲染页面的底层浏览器自动化

## 依赖

- 托管 API：API key 和互联网连接
- 自托管：Docker、Node.js 运行时以及带宽充足的服务器
- 可选：Redis 用于缓存和队列管理
- 浏览器依赖（通过 Playwright 的 Chromium）用于动态内容

## 运维难度

**低（托管） / 中等（自托管）**。托管 API 只需简单的 HTTP 集成。自托管需要管理 Node.js 服务、Playwright 浏览器实例以及队列/缓存基础设施。浏览器自动化资源密集，可能消耗大量内存。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade B——中位首次响应时间 52.0 小时，基于 34 个 qualifying issues/PRs。
- **采用广度**：Grade A——pypi.org 上月下载量 6,277,142（包名：firecrawl-py）。
- **长青度**：Grade B——仓库已创建 890 天。
- **治理集中度**：无法计算——unknown。
- **许可风险**：Grade D——AGPL-3.0 许可证。
## 存疑（未验证）

- [未验证] AGPL-3.0 许可在 SaaS 场景下可能要求衍生作品披露源码；请针对具体用例咨询法律顾问。
- [未验证] 开源自托管版与付费托管 API 之间的功能对等性尚未确认。
- [推断] 约 2 年的仓库拥有 142k star，表明存在显著炒作；请验证 GitHub star 之外的真实生产级采用情况。
