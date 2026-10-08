# markdown-tools

> 分类节点。Markdown 解析、渲染与写作工具。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **CommonMark** | 当你要在 JavaScript 里拿到规范作者给出的标准答案、判定某个 Markdown 边界情况该怎么解析，并需要一棵可改写的节点树时用它——但它只做 CommonMark：没有表格、任务列表、删除线，也没有扩展 API。 | B（5/6） | [→](commonmark.zh.md) |
| **Markdown Here** | 当你在网页邮箱或 Thunderbird 里写技术邮件、想用 Markdown 写好代码块、表格和列表，发送前一键渲染成 HTML 时用它——但上游已近停滞，浏览器的 Manifest V3 变化可能让它失效或被下架。 | C（4/6） | [→](markdown-here.zh.md) |
| **marked** | 当你需要一个快速、底层的 JS Markdown→HTML 解析器时用它——但你得自己做 XSS 消毒，且不要求严格 CommonMark。 | A（5/6） | [→](marked.zh.md) |
| **remark** | 当你的 Node.js 文档或内容流水线要通过 mdast 语法树检查、改写、再写回 Markdown（列表符号、目录、链接路径）时用它——但只要 Markdown 转 HTML 的话，marked 或 markdown-it 更轻。 | A（6/6） | [→](remark.zh.md) |
| **markdown-it** | 当你的 JavaScript 文档站、CMS 预览或聊天界面要把 Markdown 转成 HTML，既要符合 CommonMark 又要用插件加自定义语法时用它——但它的扁平 token 流只为渲染设计，检查或改写 Markdown 该用 remark。 | A（6/6） | [→](markdown-it.zh.md) |
| **micromark** | 当你要在约 14 kB、默认安全的包里得到和 cmark 一致的 CommonMark 解析，或者要给检查器、编辑器拿到精确到字节的 token 位置时用它——但它只给 token 或 HTML，不给可修改的树，要改写 Markdown 请用 remark。 | B（6/6） | [→](micromark.zh.md) |
| **Pandoc** | 当同一份 Markdown、Org 或 LaTeX 源文件要交付成 DOCX、EPUB、PDF、HTML 或 wiki 标记，或要把同事的 .docx 转回 Markdown 时用它——但版式复杂的文档会有损，而且它读不了 PDF。 | B（6/6） | [→](pandoc.zh.md) |
| **Goldmark** | 当你的 Go 服务或工具要把 Markdown 渲染得和 GitHub 一致（包括中日文加粗），需要 GFM 扩展又不想引入第三方模块时用它——但 v2 改了 API，多数第三方扩展还没迁过来。 | A（6/6） | [→](goldmark.zh.md) |
| **markdownlint** | 当 Markdown 是你仓库的交付物，想用 MD001–MD060 规则在 CI 和编辑器里抓出混用的列表符号、跳级标题、失效锚点时用它——但这个仓库只是库，要命令行请用 markdownlint-cli2。 | A（6/6） | [→](markdownlint.zh.md) |
| **MDX** | 当文档活在 React／Preact／Vue 应用里、正文需要 import 并渲染你自己的组件时用它——但交付物是独立 PDF、书或可发布文档时不要用。 | B（5/6） | [→](mdx.zh.md) |
| **TanStack Markdown** | 当你的文档/博客语料由作者控制、包体积是硬约束，且你要 HTML/React/Octane 三个渲染器从同一份缓存 AST 输出完全一致的页面时用它——不要用它渲染不可信用户 Markdown，也不要指望它严格遵循 CommonMark。 | C（5/6） | [→](tanstack-markdown.zh.md) |
| **TanStack Highlight** | 当博客或文档只用一小撮已知语言、想要体积极小、同步执行、只带类名且服务端与客户端一致的代码高亮时用它——要 VS Code 级准确度、冷门语言或自动检测语言时不要用。 | B（6/6） | [→](tanstack-highlight.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Markdown Here](markdown-here.zh.md) | ✅ | C（4/6） | 换来在邮件编辑框里直接写 Markdown、无需运维任何服务；代价是依赖一个进展缓慢、只在受支持字段生效的扩展——当成随时可能失去的便利。 |
| [marked](marked.zh.md) | ✅ | A（5/6） | 当你需要一个快速、底层的 JS Markdown→HTML 解析器时用它——但你得自己做 XSS 消毒，且不要求严格 CommonMark。 |
| [remark](remark.zh.md) | ✅ | A（6/6） | 可编辑的语法树加 unified 插件生态；代价是一套只发 ESM、由许多小包拼成的工具链，而且输出 HTML 时不加 rehype-sanitize 就不安全。 |
| [markdown-it](markdown-it.zh.md) | ✅ | A（6/6） | 默认安全的渲染加上百个 `.use()` 插件；代价是概念比 marked 多、主要靠一名维护者，且 v15 升级删掉了深层导入、改了 linkify 默认值。 |
| [CommonMark](commonmark.zh.md) | ✅ | B（5/6） | 一个小库就给你严格的规范行为和可遍历的语法树；代价是没有 GFM、没有插件，默认也不安全：不开 safe 模式并另加消毒器，原始 HTML 会直接透传。 |
| [micromark](micromark.zh.md) | ✅ | B（6/6） | 小巧的解析器换来参考实现级的一致性和带位置的 token；代价是扩展难写、只发 ESM，而且实际上只有一位维护者。 |
| [TanStack Markdown](tanstack-markdown.zh.md) | ✅ | C（5/6） | 当你的文档/博客语料由作者控制、包体积是硬约束，且你要 HTML/React/Octane 三个渲染器从同一份缓存 AST 输出完全一致的页面时用它——不要用它渲染不可信用户 Markdown，也不要指望它严格遵循 CommonMark。 |
| [TanStack Highlight](tanstack-highlight.zh.md) | ✅ | B（6/6） | 当博客或文档只用一小撮已知语言、想要体积极小、同步执行、只带类名且服务端与客户端一致的代码高亮时用它——要 VS Code 级准确度、冷门语言或自动检测语言时不要用。 |

## 什么该放这里

主要职责是**解析、渲染或撰写 Markdown** 的工具——解析器、转换器与编辑器扩展。不含把文档解析成结构化数据供 gen-AI 消费（见 `document-parsing`），不含从文本生成图表（见 `diagramming`）。
