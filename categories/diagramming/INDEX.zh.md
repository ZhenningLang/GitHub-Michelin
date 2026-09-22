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
| **draw.io** | 图需要精确摆放、需要官方云／UML／BPMN 形状库、产物还要交给同事编辑时用它——`.drawio` 是纯文本 XML，能进 git diff，应用可完全离线运行。 | B（6/6） | [→](drawio.zh.md) |
| **D2** | 当版本化的文本图要在 CI 里用你指定的布局引擎渲染时用它——MPL-2.0 是文件级 copyleft，而且没有宿主平台替你渲染。 | B（5/6） | [→](d2.zh.md) |
| **PlantUML** | 当 DSL 必须覆盖多种 UML 与非 UML 图型、且能接受 Java 或服务端渲染时用它——再分发前先看 `LICENSES.md`。 | B（6/6） | [→](plantuml.zh.md) |
| **PR Lens** | 当 agent 写的 diff 大到靠滚动无法建立方向感时用它——让改动被画出来，并在每次 push 时重画，直接落在 PR 里。 | C（6/6） | [→](pr-lens.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Mermaid](mermaid.zh.md) | ✅ | A（6/6） | 处处可渲染的纯文本图表；以布局控制力换取可移植性。 |
| [flowchart.js](flowchart-js.zh.md) | ✅ | B（5/6） | 当你想把简单流程图写成可 git diff 的文本、在浏览器里渲成 SVG 时用它——它只渲染不编辑，依赖老旧的 Raphael.js，复杂图会力不从心。 |
| [bpmn-js](bpmn-js.zh.md) | ✅ | A（5/6） | 当业务分析师需要在你的 Web 应用里编辑或查看合规的 BPMN 2.0 流程图时用它——但其许可证强制保留不可移除的 bpmn.io 水印，白标前务必先确认条款。 |
| [Excalidraw](excalidraw.zh.md) | ✅ | A（6/6） | 手绘风格协作白板，用于画草图和线框；存为 JSON 而非纯文本，不能在 Git 里 diff。 |
| [draw.io](drawio.zh.md) | ✅ | B（6/6） | 摆放必须精确、形状要用官方云／UML 形状集、产物还要交给别人改时选它；图要保持文本用 Mermaid，要的就是草稿观感用 Excalidraw。 |
| [D2](d2.zh.md) | ✅ | B（5/6） | 声明式图语言，布局引擎可换、输出格式多；MPL-2.0 是文件级 copyleft，宿主平台内建渲染远少于 Mermaid。 |
| [PlantUML](plantuml.zh.md) | ✅ | B（6/6） | 文本 DSL 覆盖广而严的 UML，通常由 Java 或服务端渲染；注意 `LICENSES.md`——API 标 LGPL-3.0，而上游默认是 GPL-3.0-or-later 另加若干宽松构建选项。 |
| [PR Lens](pr-lens.zh.md) | ✅ | C（6/6） | 从 diff 推导并贴在 PR 评论里的图，每次 push 重画；代价是每次 push 一次模型调用，且图源不能手编。 |
| Graphviz | 未收录 | — | 布局引擎本体（dot／neato）真实且活跃（16.1.0，2026-09-04），但规范仓库在 GitLab；`tools/upstream_snapshot.py` 与 `tools/health.py` 只读 GitHub，因此按现行契约拿不到上游快照和健康度雷达。 |

## 什么该放这里

主要职责是**把文本变成图表**（diagrams-as-code）或渲染图表的库/工具。不含以自由白板为主用途的应用，不含 UI 动画（见 `frontend-animation`）。
