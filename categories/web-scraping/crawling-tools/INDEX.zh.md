# crawling-tools

> 分类节点。网页抓取、爬虫编排、站点/API 包装与爬虫部署工具。
> ← 返回[web-scraping](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Claude Code Skill Scrapling** | 当你想让 Python 机器上的 Claude Code agent 在遇到 Cloudflare 403 后自己从普通请求升级到隐身浏览器、而不是瞎猜时用它——但它是只有四次提交的单人封装，速查卡已和当前 Scrapling 脱节；库自带的官方 skill 才是有人维护的那份。 | C（4/5） | [→](claude-code-skill-scrapling.zh.md) |
| **Firecrawl** | 当你的 agent 或 RAG 入库要把 URL、搜索结果或整站变成干净的 Markdown 或 JSON，又不想自己扛渲染、代理和爬取队列时用它——但自托管拿不到只在云上的反爬、页面动作和 Agent，核心还是 AGPL-3.0。 | B（6/6） | [→](firecrawl.zh.md) |
| **fuck-login** | 当你想通过可读的 Python 脚本学习 2016–2018 年中文网站登录的底层机制（CSRF token、RSA 加密密码、验证码图片）时用它——但仓库已废弃，多数脚本大概率已失效，且没有许可证。 | E（5/6） | [→](fuck-login.zh.md) |
| **gopup** | 当你在 notebook 里做探索性研究、想不写爬虫就拿到中文公开数据（微博或百度指数、CPI、Shibor）的 DataFrame 时用它——但它自 2023-09 起停滞，TOKEN 接口所在站点已下线，失败还会悄悄返回 `None`。 | E（4/6） | [→](gopup.zh.md) |
| **PRAW** | “Python Reddit API Wrapper”——一个 Python 包，在 Reddit 官方 OAuth API 之上给你类型化、Pythonic 的对象（Submission、Comment、Subreddit、Redditor），并替你处理限速合规，让你不必在代码里到处撒 `sleep`。 | B（5/6） | [→](praw.zh.md) |
| **requests-html** | 当你在维护一个已经用它、靠一个 `requests` 风格对象完成抓取和 CSS 选择服务端渲染 HTML 的旧脚本时用它——但它自 2019 年起没发过版，JS 渲染还依赖无人维护的 pyppeteer。 | D（3/6） | [→](requests-html.zh.md) |
| **Scrapling** | 你的 Python 爬虫拿到的是 403 或 Cloudflare 验证页，网站一改版选择器又全空——一个 BSD 许可的包，带 HTTP、浏览器和隐身三种抓取器，一个按相似度找回元素的解析器，外加 Scrapy 形状的爬虫层。只对付 Cloudflare，0.x 且常有破坏性变更，单人维护。 | B（6/6） | [→](scrapling.zh.md) |
| **Scrapyd** | 一个通过 JSON HTTP API 部署并运行 Scrapy 爬虫的服务守护进程——把 Scrapy 项目打成 egg、上传，然后远程调度/取消/监控抓取作业。它是 Scrapy 官方组织出品、把“在生产里跑 Scrapy”这件事标准化的守护进程。 | B（5/6） | [→](scrapyd.zh.md) |
| **SpiderKeeper** | 当已经在跑 Scrapyd 的小团队想要一个极简浏览器看板来上传 egg、按 cron 调度爬虫、查看作业统计时用它——但最后提交在 2018-05，钉着 2017 年的 Flask 栈，默认账号密码是 admin/admin。 | E（3/6） | [→](spiderkeeper.zh.md) |

## 什么该放这里

网页抓取、爬虫编排、站点/API 包装与爬虫部署工具。
