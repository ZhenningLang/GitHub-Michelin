# crawling-tools

> 分类节点。网页抓取、爬虫编排、站点/API 包装与爬虫部署工具。
> ← 返回[web-scraping](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Firecrawl** | 一款可规模化搜索、抓取并与网页交互的 API——将原始网页转化为干净的 Markdown 或结构化数据，供你的 agent 直接使用。 | B（6/6） | [→](firecrawl.zh.md) |
| **fuck-login** | 一批约 20 个 Python 脚本，逐个复刻知名网站（多为中文站：知乎、微博、百度、京东、B 站、GitHub、豆瓣）的登录流程，让你把拿到的会话 cookie 带进爬虫。这是一个 2016 年的教学仓库，作者已明确**不再维护**。 | E（5/6） | [→](fuck-login.zh.md) |
| **gopup** | 一个 Python 库，把一大堆（多为中文的）公开数据源封装成返回 pandas DataFrame 的单行调用——百度/微博/谷歌搜索指数、中国宏观指标（CPI/PPI/PMI、货币供应量、汇率）、Shibor/LPR 利率、独角兽公司名单、影视票房和疫情数据等等。 | E（3/6） | [→](gopup.zh.md) |
| **PRAW** | “Python Reddit API Wrapper”——一个 Python 包，在 Reddit 官方 OAuth API 之上给你类型化、Pythonic 的对象（Submission、Comment、Subreddit、Redditor），并替你处理限速合规，让你不必在代码里到处撒 `sleep`。 | B（5/6） | [→](praw.zh.md) |
| **requests-html** | "HTML Parsing for Humans"——一个 Python 库，把 `requests`、PyQuery/lxml 解析，以及可选的 JavaScript 渲染（经 pyppeteer/Chromium）打包到一套顺手的 API 后面，让一个小脚本无需把三个库接线串起来就能抓页面、选元素。 | D（3/6） | [→](requests-html.zh.md) |
| **Scrapyd** | 一个通过 JSON HTTP API 部署并运行 Scrapy 爬虫的服务守护进程——把 Scrapy 项目打成 egg、上传，然后远程调度/取消/监控抓取作业。它是 Scrapy 官方组织出品、把“在生产里跑 Scrapy”这件事标准化的守护进程。 | B（5/6） | [→](scrapyd.zh.md) |
| **SpiderKeeper** | 一个基于 Flask、叠在 Scrapyd 之上的 Scrapy 爬虫管理 web UI / 看板——在浏览器里部署项目、调度周期作业、查看运行统计。它自己什么都不抓；它是覆盖在一个或多个 Scrapyd 服务器之上的管理层。轻量、流行，且大体已陈旧。 | E（3/6） | [→](spiderkeeper.zh.md) |

## 什么该放这里

网页抓取、爬虫编排、站点/API 包装与爬虫部署工具。
