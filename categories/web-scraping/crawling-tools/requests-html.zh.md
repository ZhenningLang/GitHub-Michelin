---
name: requests-html
slug: requests-html
repo: https://github.com/psf/requests-html
category: crawling-tools
tags: [html-parsing, web-scraping, requests, pyquery, javascript-rendering, pyppeteer, css-selectors, python]
language: Python
license: MIT
maturity: "v0.10.0, effectively unmaintained — last pushed 2024-04 (~2y idle as of 2026-06)"
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2024-04-16T18:50:38Z
  default_branch: master
  default_branch_sha: 075ac162dc62fc532037df0d98954ab840a97516
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:14:44Z
  overall: D
  overall_score: 1.33
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1268
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 3132
        last_commit_age_days: 1268
        cohort: library
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
    adoption: { reason: ambiguous }
    governance: { reason: unattributable }
---

# requests-html

"HTML Parsing for Humans"——一个 Python 库，把 `requests`、PyQuery/lxml 解析，以及可选的 JavaScript 渲染（经 pyppeteer/Chromium）打包到一套顺手的 API 后面，让一个小脚本无需把三个库接线串起来就能抓页面、选元素。

![requests-html — 健康度雷达](../../../assets/health/requests-html.zh.svg)

## 何时使用

你是后端或数据工程师，正在为一份内部报表写一个临时爬虫——就几个来自稳定站点的页面，你只想 GET 一个 URL、把表格里的行取出来、再抓几个链接。你已经熟悉 `requests`，不想再在上面拼一个独立的 parser、学 XPath，也不想为一个 40 行的脚本搭一套爬虫框架。你 `pip install requests-html`，做 `session.get(url)`，然后 `r.html.find('table tr')`、`r.html.absolute_links`，或者一次 CSS/XPath 查询——`requests` 风格的 session 和解析活在同一个对象里，`.text`、`.links`、`.absolute_links` 都已经替你解析好。对一个抛弃型脚本、面对纯服务端渲染的 HTML，这种单一 API 的便利就是它的全部卖点。

偶尔你抓的某个页面需要一点 JavaScript 才能填充内容，`r.html.render()` 会拉起一个无头 Chromium（pyppeteer）先执行 JS 再交给你解析——对一次性场景挺顺手，否则你得搬出一整套浏览器自动化栈。**但在 2026 年做任何新工作时，请把它当成只用于遗留代码的选择**：这个库已基本无人维护（见健康度），所以主要在你维护一个已经依赖它的旧脚本时才考虑它，而不是从零起步时。

## 何时不用

- **2026 年的任何新东西——它已基本无人维护。** 最后 push 于 2024-04（截至 2026-06 闲置约 2 年）；是典型的 kennethreitz 项目套路（快速造出、广泛采用，然后吃老本）。新代码请优先 **httpx + parsel** 或 **requests + BeautifulSoup/selectolax**——同样的活、仍在活跃维护、没有死依赖风险。[未验证]
- **你需要可靠的 JavaScript 渲染。** `render()` 路径驱动 **pyppeteer**——一个老旧、自身也无人维护的 Chromium 驱动，它会下载一个重量级浏览器，且在不同 Chromium/OS 版本间很脆。真要渲染 JS 页面，请用 **Playwright（Python）** 做抓取、用 **selectolax/BeautifulSoup**（或 Playwright 自己的 locator）做解析——比 `requests-html` 内置的 pyppeteer 稳健得多。[推断]
- **大规模或生产爬取。** 它没有内建的并发模型、调度、重试/限流、去重或 pipeline——它是个便利封装，不是爬虫。要广度/吞吐请用 **Scrapy**（或在 httpx 上写一个异步抓取循环）。
- **你在意大文档的解析速度。** 它经 PyQuery/lxml 解析；若 HTML 解析是你的瓶颈，**selectolax**（Modest/lexbor）会快得多。
- **你在意长期依赖卫生。** 钉住一个吃老本的库、还把 pyppeteer + 一个内置 Chromium 拉进你的依赖树，是维护与安全负担——即便你的代码不变，传递依赖面也会持续腐化。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| httpx + BeautifulSoup / parsel | 未收录 | 想用仍在维护的 HTTP 客户端加专用解析器这一主流拆分时，选 httpx 加 BeautifulSoup/parsel。 | 主流的现代拆分：一个仍在活跃维护、支持异步的 HTTP 客户端，加一个专用 parser（bs4 容错解析 HTML，parsel 走 Scrapy 风格的 CSS/XPath）。是两个 import 而非一个，但两者都在维护、各块你都可控——纯 HTML 抓取的推荐替代。 |
| [Playwright](../../web-automation/playwright-family/playwright.zh.md)（Python） | ✅ | 需要维护中的真实浏览器自动化来处理重 JS 页面时，选 Playwright。 | 真正在维护的无头浏览器自动化（Chromium/Firefox/WebKit），面向重 JS 页面；比 `requests-html` 的 pyppeteer `render()` 稳健得多，但更重、是另一套（驱动浏览器的）心智模型。配 selectolax/bs4 做解析。 |
| Scrapy | 未收录 | 需要完整异步爬虫框架时，选 Scrapy。 | 一个完整的异步爬虫框架——并发、调度、中间件、pipeline、重试；当你要规模化爬取时它才对，对一个 40 行的一次性脚本则杀鸡用牛刀。 |
| selectolax | 未收录 | 需要很快的 C 后端 HTML parser 和 CSS 选择器时，选 selectolax。 | 很快的 C 后端（Modest/lexbor）HTML parser，带 CSS 选择器；只做解析（HTTP 客户端自带），但大文档场景的速度之选——恰是 `requests-html` 所不是的。 |
| requests + BeautifulSoup | 未收录 | 经典同步抓取组合仍够用时，选 requests + BeautifulSoup。 | 经典、至今够用的同步抓取组合；`requests-html` 本质就是这套再加 PyQuery 选择器和一个可选的 JS 渲染外挂，只是没了活跃维护。 |

## 技术栈

- **语言：** Python（历史上 3.6+；请对照你钉的版本核实——本项目早于当前的 Python 版本）。
- **HTTP：** 封装 `requests`（`HTMLSession`）做同步抓取；另有 `AsyncHTMLSession` 供异步使用。
- **解析：** 底层 PyQuery + lxml，对外暴露 `.find()`（CSS）、`.xpath()`、`.search()`/`.search_all()`（parse 模板）、`.text`、`.links`、`.absolute_links`。
- **JS 渲染：** `r.html.render()` 驱动 **pyppeteer**，后者下载并控制一个无头 **Chromium**；渲染是可选的，仅按需触发。

## 依赖

- **运行时：** `requests`、`pyquery`、`lxml`、`parse`、`bs4`、`w3lib`、`fake-useragent`（对一个“小”库来说，拉进来的这套栈并不轻）。
- **JS 渲染：** `pyppeteer`，外加一个它在首次 `render()` 时下载的**内置无头 Chromium**——一个大体积二进制依赖，而 pyppeteer 本身也老旧、维护不足。
- **无服务/基础设施：** 它是客户端库——没有数据存储、没有守护进程、没有后端；唯一的重型产物是 `render()` 要下载的 Chromium。

## 运维难度

**解析路径低，`render()` 路径中等且脆弱。** 作为一个纯库，它没有任何东西要部署或运维——`pip install`、import、跑起来。摩擦完全集中在两处：（1）`render()` 路径首次使用时会下载一整个 Chromium，并依赖 pyppeteer 在你的 OS/Chromium 版本上能跑通——在缺少正确系统库的容器/CI 里会坏，而且上游不会再修；（2）**依赖腐化**——在现代 Python 上安装一个吃老本的库，可能在 lxml/pyquery/pyppeteer 上冒出版本冲突，而你拿不到上游新版本来解决它们。请为钉版本预留时间，并在 JS 路径重要时用 Playwright 替换 `render()`。[推断]

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（DATED 2026-06）。** **最后 push 于 2024-04——大约闲置 2 年**；无近期发布或提交活动。这读起来就是**基本无人维护/吃老本**，也是 2026 年任何选型决策的主导信号。未正式归档，但时效性已死。[未验证]
- **kennethreitz 套路。** 这是 kennethreitz 作者的项目（像 `requests` 本身和他另外几个项目一样）：快速造出、极其顺手、广泛采用，然后在注意力转移后就放任吃老本。这里请把“流行且优雅”与“当前仍在维护”当成正交两件事。[推断]
- **治理 / bus factor。** 仓库挂在 **PSF（`psf`）组织**下（owner 类型为 Organization），这只是*名义上*的托管——PSF 持有这个仓库**并不**意味着有活跃维护者在出修复。未发现活跃维护者；对新修复而言可把 bus factor 视为接近零。[未验证]
- **年龄与 Lindy 判断。** 2018-02 创建（约 8 年），单看年龄像是 Lindy——但 **Lindy 要的是 年龄 × *仍然活跃***，而它在“仍然活跃”这一半上不及格。一个长寿**却闲置**的项目不是安全押注；这里的年龄并不保护你。[推断]
- **采用度与真正的风险。** 它仍被广泛 star（约 13.8k），也在老教程里被引用，所以你会在遗留代码里遇到它——但**依赖腐化才是活的风险**：内置 pyppeteer/Chromium 的 JS 渲染路径脆弱且无人维护，更广的传递依赖栈也在没有上游发布的情况下老化。采用惯性 ≠ 可持续性。[未验证]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 13.8k GitHub star、MIT 许可——star 数对时间敏感、作为健康代理不可靠，仅供参考。
- [未验证] “最后 push 于 2024-04 / 闲置约 2 年 / 基本无人维护”是主导论断，也是整份推荐的依据——依赖前请重新核实仓库实际的 last-commit/last-release 日期；项目并未正式归档。
- [未验证] 记录显示 PSF（`psf`）是拥有方组织（owner 类型 Organization），但 PSF 拥有并不能确认有*活跃*维护者；未核实当前的维护者/路线图。
- [推断] “kennethreitz 项目套路”（造完即吃老本）是从作者更广的项目历史所做的概括，而非项目明文政策。
- [推断] pyppeteer 老旧/无人维护、以及 `render()` 路径在不同 Chromium/OS 版本间脆弱，是从 pyppeteer 的总体状态和内置 Chromium 路径的工作方式推断而来——依赖 JS 渲染前请对照你的目标环境核实。
- [未验证] 确切的运行时依赖清单与最低 Python 版本随版本而变——请核对你钉的版本，而非信任本摘要。
