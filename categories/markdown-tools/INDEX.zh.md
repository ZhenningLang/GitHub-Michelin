# markdown-tools

> 分类节点。Markdown 解析、渲染与写作工具。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **CommonMark** | 当你需要规范合规、可遍历 AST 的 Markdown 官方参考实现时用它——但它不以速度见长，也不支持 GFM 或插件生态。 | B（5/6） | [→](commonmark.zh.md) |
| **Markdown Here** | 当你想用浏览器/Thunderbird 扩展把邮件用 Markdown 写好、发送前渲染成 HTML 时用它——注意维护已放缓。 | C（4/6） | [→](markdown-here.zh.md) |
| **marked** | 当你需要一个快速、底层的 JS Markdown→HTML 解析器时用它——但你得自己做 XSS 消毒，且不要求严格 CommonMark。 | A（5/6） | [→](marked.zh.md) |
| **remark** | 当你需要完整的 mdast AST 管线来解析、变换、lint 和序列化 Markdown 时用它——但它是工具链，不是一次调用的渲染器。 | A（6/6） | [→](remark.zh.md) |
| **markdown-it** | 当你需要一个严格遵循 CommonMark/GFM、可插拔的 JS Markdown→HTML 解析器时用它——但插件生态会增加体积，且处理不受信任内容时仍需消毒。 | A（6/6） | [→](markdown-it.zh.md) |
| **micromark** | 当你需要一个低层、面向流式处理的 JS CommonMark/GFM 分词器时用它——remark 的底层引擎——但渲染层要你自己搭。 | B（6/6） | [→](micromark.zh.md) |
| **Pandoc** | Universal markup converter | B（6/6） | [→](pandoc.zh.md) |
| **Goldmark** | :trophy: A markdown parser written in Go. Easy to extend, standard(CommonMark) compliant, well structured. | A（6/6） | [→](goldmark.zh.md) |
| **markdownlint** | A Node.js style checker and lint tool for Markdown/CommonMark files. | A（6/6） | [→](markdownlint.zh.md) |
| **MDX** | 当文档活在 React／Preact／Vue 应用里、正文需要 import 并渲染你自己的组件时用它——但交付物是独立 PDF、书或可发布文档时不要用。 | B（5/6） | [→](mdx.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Markdown Here](markdown-here.zh.md) | ✅ | C（4/6） | 当你想用浏览器/Thunderbird 扩展把邮件用 Markdown 写好、发送前渲染成 HTML 时用它——注意维护已放缓。 |
| [marked](marked.zh.md) | ✅ | A（5/6） | 当你需要一个快速、底层的 JS Markdown→HTML 解析器时用它——但你得自己做 XSS 消毒，且不要求严格 CommonMark。 |
| [remark](remark.zh.md) | ✅ | A（6/6） | 当你需要完整的 mdast AST 管线来解析、变换、lint 和序列化 Markdown 时用它——但它是工具链，不是一次调用的渲染器。 |
| [markdown-it](markdown-it.zh.md) | ✅ | A（6/6） | 当你需要一个严格遵循 CommonMark/GFM、可插拔的 JS Markdown→HTML 解析器时用它——但插件生态会增加体积，且处理不受信任内容时仍需消毒。 |
| [CommonMark](commonmark.zh.md) | ✅ | B（5/6） | 当你需要规范合规、可遍历 AST 的 Markdown 官方参考实现时用它——但它不以速度见长，也不支持 GFM 或插件生态。 |
| [micromark](micromark.zh.md) | ✅ | B（6/6） | 当你需要一个低层、面向流式处理的 JS CommonMark/GFM 分词器时用它——remark 的底层引擎——但渲染层要你自己搭。 |

## 什么该放这里

主要职责是**解析、渲染或撰写 Markdown** 的工具——解析器、转换器与编辑器扩展。不含把文档解析成结构化数据供 gen-AI 消费（见 `document-parsing`），不含从文本生成图表（见 `diagramming`）。
