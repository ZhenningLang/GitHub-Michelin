# diagramming

> 分类节点。从文本生成图表（diagrams-as-code），用于 Markdown、文档和 Web。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Mermaid** | 当你想把图表写成可进版本库的纯文本（流程图/时序图/ER），在 Markdown 和文档里渲染时用它——不适合像素级精确排版。 | A（6/6） | [→](mermaid.zh.md) |
| **flowchart.js** | 当你想把简单流程图写成可 git diff 的文本、在浏览器里渲成 SVG 时用它——它只渲染不编辑，依赖老旧的 Raphael.js，复杂图会力不从心。 | B（5/6） | [→](flowchart-js.zh.md) |
| **bpmn-js** | 当业务分析师需要在你的 Web 应用里编辑或查看合规的 BPMN 2.0 流程图时用它——但其许可证强制保留不可移除的 bpmn.io 水印，白标前务必先确认条款。 | A（5/6） | [→](bpmn-js.zh.md) |
| **Excalidraw** | 当你想要手绘风格的协作白板来画草图、线框和架构流程时用它——但它存为 JSON 而非纯文本，所以不能在 Git 里 diff。 | A（6/6） | [→](excalidraw.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Mermaid](mermaid.zh.md) | ✅ | A（6/6） | 处处可渲染的纯文本图表；以布局控制力换取可移植性。 |
| [flowchart.js](flowchart-js.zh.md) | ✅ | B（5/6） | 当你想把简单流程图写成可 git diff 的文本、在浏览器里渲成 SVG 时用它——它只渲染不编辑，依赖老旧的 Raphael.js，复杂图会力不从心。 |
| [bpmn-js](bpmn-js.zh.md) | ✅ | A（5/6） | 当业务分析师需要在你的 Web 应用里编辑或查看合规的 BPMN 2.0 流程图时用它——但其许可证强制保留不可移除的 bpmn.io 水印，白标前务必先确认条款。 |
| [Excalidraw](excalidraw.zh.md) | ✅ | A（6/6） | 手绘风格协作白板，用于画草图和线框；存为 JSON 而非纯文本，不能在 Git 里 diff。 |
| Graphviz / PlantUML / D2 / draw.io / Excalidraw | 未收录 | — | 各页对比里点到的其他图引擎/编辑器（布局更可控或所见即所得）。 |

## 什么该放这里

主要职责是**把文本变成图表**（diagrams-as-code）或渲染图表的库/工具。不含以自由白板为主用途的应用，不含 UI 动画（见 `frontend-animation`）。
