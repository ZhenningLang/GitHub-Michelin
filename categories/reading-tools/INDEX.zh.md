# reading-tools

> 分类节点。阅读工具——阅读模式扩展与 RSS 阅读器。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Read Frog** | 当你靠读真实文章学外语，想要双语段落、按水平讲解、朗读、自定义 AI 动作和间隔重复生词卡，并接自己的 AI 服务商时用它——但它由公司掌控双授权，2026-09 起还依赖专有排版包，无法 fork 出完全自由的构建。 | B（6/6） | [→](read-frog.zh.md) |
| **FluentRead** | 当你想用一个开源扩展覆盖网页双语对照、PDF/ePub、OCR 和视频字幕，引擎可选免费服务、自带密钥或浏览器内本地模型时用它——但它是 GPL-3.0、实际单人维护，零配置默认会把文本发往公开翻译端点。 | C（6/6） | [→](fluentread.zh.md) |
| **Margin Read** | 当页面文字只能发往你自己的 Ollama、LM Studio 或公司网关，又想要 MIT 许可、写明威胁模型的扩展时用它——但它是年轻的单人维护 Chrome MVP，近期已放缓，不含 PDF、字幕和 OCR。 | C（5/6） | [→](margin-read.zh.md) |
| **Pair Translate** | 当 Read Frog 和 FluentRead 显得太重，你想要一个小巧的双语翻译扩展，把文本从浏览器直接发给微软、DeepL 或你自己的大模型（含本机 Ollama）时用它——但它是 GPL-3.0，实际是一个人维护、刚满一年的项目。 | C（5/6） | [→](pair-translate.zh.md) |
| **NetNewsWire** | 当你在 Mac／iPhone 上读大量订阅、想要一个快速无广告、数据自己掌控的原生 RSS 客户端时用它——但它仅限 Apple 平台，别处一概不支持。 | B（6/6） | [→](netnewswire.zh.md) |
| **Just Read** | 当你想在浏览器里按自己的方式清掉文章的广告与杂乱、还能按站点记忆选择器时用它——但它是 EULA 授权的源码，并非真正的开源。 | C（6/6） | [→](just-read.zh.md) |
| **FreshRSS** | 当你想把订阅和已读状态放在自己的 VPS、NAS 或树莓派上，并让任何兼容 Google Reader 接口的客户端同步时用它——但升级、备份和 TLS 永远是你的事；不需要插件的话，Miniflux 更精简。 | B（6/6） | [→](freshrss.zh.md) |
| **Horizon** | 当订阅源多到刷不完、你想要一条自托管的 LLM 流水线每天替你打分、筛选、去重并生成双语简报，而不是一个自己刷的阅读器时用它。 | B（6/6） | [→](horizon.zh.md) |
| **Follow Builders** | 当你想不配任何 key 就每天收到一份固定 AI 建造者名单在 X、播客和两个博客上说了什么的摘要时用它——但信源你改不了，可用性系在一个人的 X API 账单上。 | C（4/6） | [→](follow-builders.zh.md) |
| **Bilingual Book Maker** | 当你想要一个可脚本化的 CLI，把 epub/txt/md/srt/pdf 经 LLM/MT API 做成双语对照书，带断点续跑和 PyPI 打包时用它——不是 agent 流水线。 | A（5/6） | [→](bilingual-book-maker.zh.md) |
| **TranslateBooksWithLLMs** | 当非开发者要把整本 EPUB／DOCX／SRT／TXT 译成单一目标语言、保住格式、带术语表和断点续跑，用桌面程序接 Ollama 或云端 key 时用它；只适合单人本机。 | C（6/6） | [→](translate-books-with-llms.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Read Frog](read-frog.zh.md) | ✅ | B（6/6） | 功能最全、发版很勤，代价是 GPL 加商业双授权、向 FEELIO 授权的贡献条款，以及一个闭源依赖。 |
| [FluentRead](fluentread.zh.md) | ✅ | C（6/6） | 一个扩展覆盖最广的阅读场景，代价是 GPL 许可、单人维护的巴士因子，以及默认配置下文本去向不够可控。 |
| [Margin Read](margin-read.zh.md) | ✅ | C（5/6） | 换来可审计的数据流和宽松许可，代价是功能极简、采用度很小，2026 年 6 月后再没发版。 |
| [Pair Translate](pair-translate.zh.md) | ✅ | C（5/6） | 体量更轻、请求直连服务商，代价是沉浸式翻译工作流更少、采用度比 Read Frog 低一个数量级，还要申请全站点权限。 |
| [NetNewsWire](netnewswire.zh.md) | ✅ | B（6/6） | 当你在 Mac／iPhone 上读大量订阅、想要一个快速无广告、数据自己掌控的原生 RSS 客户端时用它——但它仅限 Apple 平台，别处一概不支持。 |
| [Just Read](just-read.zh.md) | ✅ | C（6/6） | 当你想在浏览器里按自己的方式清掉文章的广告与杂乱、还能按站点记忆选择器时用它——但它是 EULA 授权的源码，并非真正的开源。 |
| [Bilingual Book Maker](bilingual-book-maker.zh.md) | ✅ | A（5/6） | 双语电子书文件的成熟 CLI 路径：任意 LLM/MT 后端、断点续跑、PyPI 打包——但段落流式翻译，没有人工整理的术语表。 |
| [TranslateBooksWithLLMs](translate-books-with-llms.zh.md) | ✅ | C（6/6） | 图形界面 + 命令行的整文件翻译器，占位符校验保标签、整书术语表、SQLite 断点续跑——但不支持 PDF、不发 PyPI 包、AGPL、单维护者、没有多用户认证。 |
| [Horizon](horizon.zh.md) | ✅ | B（6/6） | 自托管 AI 新闻雷达：profile 驱动的 LLM 打分去重，覆盖 RSS／HN／Reddit／Telegram／X，产出双语每日简报——但只有约 7 个月历史、单一维护者、尚无 release。 |
| [Follow Builders](follow-builders.zh.md) | ✅ | C（4/6） | 零配置 agent skill，吃作者每天生成的中央 feed（26 位 X 建造者、6 个播客、2 个博客）——但信源不可改、无 LICENSE 文件、Claude Code 上定时只发原始 JSON、X API 由单一维护者付费。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向终端用户的**阅读**工具——阅读模式浏览器扩展、双语／沉浸式翻译扩展、RSS／订阅阅读器。文章正文提取库见 `web-scraping`。
