# office-editors（办公编辑器）

> 分类节点。**交互式**办公编辑：嵌进你自己产品里的编辑器 SDK 与电子表格式数据网格，以及自托管、可对接进来的文档服务器与表格平台。与 [office-automation](../office-automation/INDEX.zh.md) 的区别：那边*写文件*，这边*给人（或 agent）一个可以编辑文件的界面*。
> ← 返回[分类路由](../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时进来 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Univer** | 当你在*做一个产品*、需要内嵌一个可以逐插件改版重写的表格/文档编辑器、且要求 Apache-2.0 时用它——但协同、xlsx 导入导出、图表、透视表在付费 Pro，1.0 线 2026-09 才发布，路线图系于单一厂商。 | A（6/6） | [→](univer.zh.md) |
| **Fortune Sheets** | 当 React 应用要一个 MIT 的即用型类 Excel 网格、并愿意自己接 op 流做持久化时用它——但它是 Luckysheet 血统、功能上限相同，无内置 xlsx 读写，且 2025-12-15 后无提交。 | B（5/6） | [→](fortune-sheets.zh.md) |
| **Handsontable** | 当内部数据录入网格需要 15 年打磨的电子表格交互（校验、条件格式、400 个公式）、且预算容得下商业授权时用它——想免费商用就换 Jspreadsheet CE 或 Fortune Sheets。 | A（5/6） | [→](handsontable.zh.md) |
| **Jspreadsheet** | 当你想要最轻的 MIT 原生 JS 网格、带列类型与 Excel 复制粘贴时用它——但要接受社区版是 Pro 产品的免费层、GitHub 发布落后于 npm 包。 | B（5/6） | [→](jspreadsheet.zh.md) |
| **Grist** | 当团队要的是一个*成品*——自托管、列即数据库字段、公式用 Python、按行权限、带 webhook 的表格平台——而不是一个可嵌入组件时用它；Apache-2.0 核心有法国政府贡献背书、月度发布活跃。 | A（5/6） | [→](grist.zh.md) |
| **ONLYOFFICE Docs** | 当你的网盘/CRM/LMS 需要「点一下 .docx 就进入带实时协同的完整编辑器」、一个 Docker 容器搞定且要真实 OOXML 保真度时用它——但它是 AGPL，社区版建议并发 ≤20，GitHub 仓库只是打包壳。 | B（6/6） | [→](onlyoffice-documentserver.zh.md) |
| **Collabora Online** | 当你运行（或对接）Nextcloud 这类支持 WOPI 的文件平台、想在浏览器里用上 LibreOffice 渲染引擎时用它——但活跃开发在 Gerrit 而非这个 GitHub 仓库，这里也没有可嵌入的 UI SDK。 | A（5/6） | [→](collabora-online.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Univer](univer.zh.md) | ✅ | A（6/6） | 嵌入式 SDK 路线：Canvas 渲染、公式引擎、表格+文档一个 Apache-2.0 全家桶、Node 无头运行——代价是协同/导入导出/图表/透视表在付费 Pro，代码库 4 年历史且系于单一厂商。 |
| [Fortune Sheets](fortune-sheets.zh.md) | ✅ | B（5/6） | Luckysheet 血统的 MIT 即插即用网格，op 流留给你的后端；免费、简单，但自 2025-12 起无人动过，xlsx 读写要另装插件。 |
| [Handsontable](handsontable.zh.md) | ✅ | A（5/6） | 15 年的 DOM 数据网格头名：最深的电子表格编辑交互、发布稳定——前提是你付钱，商用不在它的免费许可里。 |
| [Jspreadsheet](jspreadsheet.zh.md) | ✅ | B（5/6） | MIT 原生 JS 网格（前身 jExcel），列类型与 Excel 粘贴齐全，最省钱的认真选项；但社区版是 Pro 的引流入口，GitHub 版本落后 npm。 |
| [Grist](grist.zh.md) | ✅ | A（5/6） | 可自托管的「表格×数据库」*成品*：Python 公式、行级权限、webhook；你是运维它，不是嵌入它——开源核心之外还有 source-available 完整版。 |
| [ONLYOFFICE Docs](onlyoffice-documentserver.zh.md) | ✅ | B（6/6） | 一体化 AGPL 文档服务器：真实 .docx/.xlsx/.pptx 保真、内置协同、一个容器——适合网盘式「点文件进编辑器」，不适合重做产品 UI。 |
| [Collabora Online](collabora-online.zh.md) | ✅ | A（5/6） | WOPI 后面的 LibreOffice 引擎文档服务器：格式覆盖最广、C++ 团队成熟——但 GitHub 只是 issue 镜像（代码在 Gerrit），集成意味着自建 WOPI host。 |

## 收录范围

主要交付**人机交互式编辑界面**的仓库：浏览器/应用里的内嵌编辑器 SDK 与框架、带电子表格控件的数据网格组件、可自托管的文档服务器、表格类平台应用。不含无界面的程序化 Office 文件生成（→ [office-automation](../office-automation/INDEX.zh.md)），不含文档解析摄取（→ [document-parsing](../document-parsing/INDEX.zh.md)），不含归档套件（→ [document-management](../document-management/INDEX.zh.md)），不含设计/图形画布（→ [design-editors](../design-editors/INDEX.zh.md)、[diagramming](../diagramming/INDEX.zh.md)）。只有绘制语义的白板留在 [diagramming](../diagramming/INDEX.zh.md)；一旦网格长出公式、单元格类型和编辑交互，就归这里。
