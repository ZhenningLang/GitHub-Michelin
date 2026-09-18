# article-extraction

> 分类节点。正文抽取、样板噪声移除与内容解析工具。
> ← 返回[web-scraping](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **boilerpipe** | 一个用于从 HTML 做样板移除和全文抽取的 Java 库——经典的、算法驱动的路子（浅层文本特征、链接密度、标签比率），把文章抽出来、丢掉导航、广告和周边杂物。 | D（3/6） | [→](boilerpipe.zh.md) |
| **dragnet** | 一种用机器学习做网页正文抽取的方法——训练好的模型从页面 HTML 里拉出正文（可选连用户评论一起），靠多样的文本/标记特征而非手调启发式。 | D（4/6） | [→](dragnet.zh.md) |
| **newspaper** | 一个 Python 库：给它一个新闻/文章 URL，它就下载、解析，吐出干净的正文、标题、作者、发布日期、头图，以及（可选的）NLP 关键词/摘要——样板内容剥掉，不用为每个站点手写抓取规则。 | B（5/6） | [→](newspaper.zh.md) |
| **python-readability** | 一个快速、基于 lxml 的 arc90 Readability Python 移植——递给它一个 HTML 文档，它返回清理过的正文（`summary()`）和标题（`title()`），剥掉导航、广告和样板。 | B（3/6） | [→](python-readability.zh.md) |
| **Readability.js** | Firefox Reader View 背后那个 readability 库的独立版本——给它一个 DOM document，拿回文章的标题、作者署名和清理过的正文，导航、广告和样板内容都被剥掉。 | B（5/6） | [→](readability-js.zh.md) |
| **trafilatura** | Python & Command-line tool to gather text and metadata on the Web: Crawling, scraping, extraction, output as CSV, JSON, HTML, MD, TXT, XML | B（6/6） | [→](trafilatura.zh.md) |

## 什么该放这里

正文抽取、样板噪声移除与内容解析工具。
