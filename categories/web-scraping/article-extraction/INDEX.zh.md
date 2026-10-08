# article-extraction

> 分类节点。正文抽取、样板噪声移除与内容解析工具。
> ← 返回[web-scraping](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **boilerpipe** | 当 JVM 上的索引器或语料管线要用经典浅层文本特征启发式从原始 HTML 里剥出正文、又不想引入浏览器或 Python 服务时用它——但它实际已废弃（最后 push 在 2018-01），得自己 vendor 并接管修复。 | "?"（2/6） | [→](boilerpipe.zh.md) |
| **dragnet** | 当启发式抽取器老把你的页面切错、而你有标注数据想在 Python 里训练一个能把正文和用户评论分开的模型时用它——但它近乎停摆，且把 scikit-learn 钉在 0.21 以下，现代环境里安装很痛苦。 | D（4/6） | [→](dragnet.zh.md) |
| **newspaper** | 一个 Python 库：给它一个新闻/文章 URL，它就下载、解析，吐出干净的正文、标题、作者、发布日期、头图，以及（可选的）NLP 关键词/摘要——样板内容剥掉，不用为每个站点手写抓取规则。 | B（5/6） | [→](newspaper.zh.md) |
| **python-readability** | 一个快速、基于 lxml 的 arc90 Readability Python 移植——递给它一个 HTML 文档，它返回清理过的正文（`summary()`）和标题（`title()`），剥掉导航、广告和样板。 | A（3/6） | [→](python-readability.zh.md) |
| **Readability.js** | Firefox Reader View 背后那个 readability 库的独立版本——给它一个 DOM document，拿回文章的标题、作者署名和清理过的正文，导航、广告和样板内容都被剥掉。 | B（6/6） | [→](readability-js.zh.md) |
| **trafilatura** | 当你要从几千个管不了的网站页面里抽出正文、标题、作者和日期，又不想按站点写选择器时用它——但它只处理原始 HTML，JavaScript 渲染或被反爬拦截的页面要先用浏览器或隐身抓取器下载。 | A（6/6） | [→](trafilatura.zh.md) |

## 什么该放这里

正文抽取、样板噪声移除与内容解析工具。
