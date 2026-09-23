# office-automation

> 分类节点。程序化创建、读取、编辑**原生** Office 文档（`.docx`／`.xlsx`／`.pptx`）——管道的生成侧，面向脚本也面向 agent。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OfficeCLI** | 当 agent 必须在一台没有 Python 也没有 Office 的机器上读写、创建全部三个 Office 格式，并且需要**看见**渲染结果时用它——但它只有 6 个月、98% 单人作者、没有公开测试套件，且默认开启自动更新并会改写你的 agent skill 目录。 | B（6/6） | [→](officecli.zh.md) |
| **python-docx** | 当 Python 服务需要就地创建或编辑 Word `.docx`、且要一个能锁版本、已存活 13 年的 MIT 依赖时用它——但没有渲染能力，且脚注／尾注自 2014 年起一直未实现。 | B（5/6） | [→](python-docx.zh.md) |
| **python-pptx** | 当你必须用 Python 生成或编辑原生 `.pptx`、且交付物要能在 PowerPoint 里打开时用它——但它自 2024-08-07 起未再发版，动画（2017）和 SmartArt（2014）从未实现。 | C（4/6） | [→](python-pptx.zh.md) |
| **XlsxWriter** | 当 Python 服务从数据生成新的 `.xlsx`、且你要零依赖加 13 年稳定性时用它——但它只写，无法打开已有工作簿，也不计算公式。 | B（6/6） | [→](xlsxwriter.zh.md) |
| **Office-Word-MCP-Server** | 只有当既有 LLM 集成已经绑定它那约 55 个 Word tool schema 时才用它——仓库已于 2025-12-31 归档，作者批量归档了约 15 个 MCP server；新工作请用 OfficeCLI，或自己封装 python-docx。 | C（6/6） | [→](office-word-mcp-server.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OfficeCLI](officecli.zh.md) | ✅ | B（6/6） | 三格式加渲染回看闭环装进一个无依赖二进制；代价是 6 个月的单人代码库、无公开测试，以及默认开启、会改写 agent skill 目录的自动更新。 |
| [python-docx](python-docx.zh.md) | ✅ | B（5/6） | 大多数 agent skill 包装的那个稳定、可锁版本的 Word 层；只有 Word、无渲染、有十年未补的功能缺口。 |
| [python-pptx](python-pptx.zh.md) | ✅ | C（4/6） | 唯一成熟的 MIT `.pptx` 生成库；自 2024-08 起滑行，没有动画和 SmartArt API。 |
| [XlsxWriter](xlsxwriter.zh.md) | ✅ | B（6/6） | 零依赖、生产级稳定、维护活跃的表格生成；只写，且不求值公式。 |
| [Office-Word-MCP-Server](office-word-mcp-server.zh.md) | ✅ | C（6/6） | MCP 原生的 Word 编辑，带 python-docx 缺的脚注支持；已归档、只有 Word，且它的 PDF 工具需要真实安装 MS Word。 |
| [Pandoc](../markdown-tools/pandoc.zh.md) | ✅ | B（6/6） | 一次调用把 Markdown 导出成 `.docx`／`.pptx`，用 reference doc 控样式；无法就地编辑已有 Office 文件。 |
| [MarkItDown](../document-parsing/markitdown.zh.md) | ✅ | B（6/6） | 相反方向：Office → Markdown 供 LLM 摄取，只读，且按设计在格式上有损。 |
| openpyxl | 未收录 | — | XlsxWriter 的读写型 `.xlsx` 对手；未收录是因为它的规范仓库在 Heptapod（Mercurial）而非 GitHub，而本索引的健康度／上游快照工具只支持 GitHub。 |
| Office-PowerPoint-MCP-Server | 未收录 | — | Word MCP server 的 `.pptx` 姊妹项目（1,852 star）；被同一作者于 2025-12-31 归档，所以除了这条说明之外不提供额外选型价值。 |
| LibreOffice headless／Aspose／Apache POI | 未收录 | — | 这些页面里点名的转换引擎、商业与 JVM 路线；与面向 agent 的 OOXML 编辑器不在同一抽象层。 |


## 什么该放这里

主职是**生成或修改原生 Office 文件**（`.docx`／`.xlsx`／`.pptx`）的工具和库——无论被脚本、CLI，还是被 agent 通过 MCP 调用。不包括：文档 → Markdown 摄取（见 [document-parsing](../document-parsing/INDEX.zh.md)）、OCR（见 [ocr](../ocr/INDEX.zh.md)）、对文书做归档与全文检索（见 [document-management](../document-management/INDEX.zh.md)），以及产物不是 Office 文件的 HTML／视觉 deck 生成（见 [ai-design-generation](../ai-design-generation/INDEX.zh.md) 和 [agent-skills/slides-ppt](../agent-skills/slides-ppt/INDEX.zh.md)）。Pandoc 这类单向转换器留在各自的格式分类里，在此处交叉链接。
