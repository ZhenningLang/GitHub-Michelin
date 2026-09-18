# reading-tools

> 分类节点。阅读工具——阅读模式扩展与 RSS 阅读器。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Read Frog** | 当你想要功能丰富的开源沉浸式／双语翻译扩展，且需要 BYOK AI provider、本地 Ollama／自定义端点、TTS 和 YouTube 字幕翻译时用它。 | B（6/6） | [→](read-frog.zh.md) |
| **FluentRead** | 当你想要中文优先、支持许多引擎的开源沉浸式翻译浏览器扩展，带双语／全文翻译和 Ollama／自定义 OpenAI-compatible 设置时用它。 | C（6/6） | [→](fluentread.zh.md) |
| **Margin Read** | 当 MIT 许可、明确 BYOK／本地端点支持和写清楚的隐私 threat model 比功能完整度更重要时用它。 | C（5/6） | [→](margin-read.zh.md) |
| **Pair Translate** | 当你想要更轻量的双语网页翻译器，支持 direct provider requests、LLM 模板和 Chrome／Firefox／Edge 分发时用它。 | C（5/6） | [→](pair-translate.zh.md) |
| **NetNewsWire** | 当你在 Mac／iPhone 上读大量订阅、想要一个快速无广告、数据自己掌控的原生 RSS 客户端时用它——但它仅限 Apple 平台，别处一概不支持。 | B（5/6） | [→](netnewswire.zh.md) |
| **Just Read** | 当你想在浏览器里按自己的方式清掉文章的广告与杂乱、还能按站点记忆选择器时用它——但它是 EULA 授权的源码，并非真正的开源。 | D（6/6） | [→](just-read.zh.md) |
| **FreshRSS** | A free, self-hostable news aggregator… | ?（0/6） | [→](freshrss.zh.md) |
| **Bilingual Book Maker** | 当你想要一个可脚本化的 CLI，把 epub/txt/md/srt/pdf 经 LLM/MT API 做成双语对照书，带断点续跑和 PyPI 打包时用它——不是 agent 流水线。 | A（5/6） | [→](bilingual-book-maker.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Read Frog](read-frog.zh.md) | ✅ | B（6/6） | 本分类里功能最丰富的开源 AI 阅读／翻译扩展：BYOK provider、本地／自定义端点、TTS、字幕和批量请求——但 GPL／商业双授权且权限面宽。 |
| [FluentRead](fluentread.zh.md) | ✅ | C（6/6） | 翻译优先的开源沉浸式翻译器，支持许多引擎和商店安装——但 endpoint／隐私边界不如 Margin Read 明确，维护也更集中。 |
| [Margin Read](margin-read.zh.md) | ✅ | C（5/6） | 当 MIT、BYOK、本地 OpenAI-compatible runtime 和隐私文档决定选择时最合适——但仍是早期 Chrome／Chromium MVP，采用度很小。 |
| [Pair Translate](pair-translate.zh.md) | ✅ | C（5/6） | 轻量双语翻译器，已验证 LLM／本地模板且 release 活跃——但 GPL、年轻，浏览器侧 API key 仍是信任边界。 |
| [NetNewsWire](netnewswire.zh.md) | ✅ | B（5/6） | 当你在 Mac／iPhone 上读大量订阅、想要一个快速无广告、数据自己掌控的原生 RSS 客户端时用它——但它仅限 Apple 平台，别处一概不支持。 |
| [Just Read](just-read.zh.md) | ✅ | D（6/6） | 当你想在浏览器里按自己的方式清掉文章的广告与杂乱、还能按站点记忆选择器时用它——但它是 EULA 授权的源码，并非真正的开源。 |
| [Bilingual Book Maker](bilingual-book-maker.zh.md) | ✅ | A（5/6） | 双语电子书文件的成熟 CLI 路径：任意 LLM/MT 后端、断点续跑、PyPI 打包——但段落流式翻译，没有人工整理的术语表。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向终端用户的**阅读**工具——阅读模式浏览器扩展、双语／沉浸式翻译扩展、RSS／订阅阅读器。文章正文提取库见 `web-scraping`。
