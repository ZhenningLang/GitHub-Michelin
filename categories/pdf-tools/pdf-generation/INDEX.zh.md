# pdf-generation

> 分类节点。在代码里创建新 PDF——从零绘制、从 HTML 或组件生成，或把导入的页面拼成新文档。
> ← 返回[pdf-tools](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **pdf-lib** | 当你要用同一份 TypeScript 代码在浏览器、Node、Deno 或 React Native 里创建、填写或合并 PDF、且不能有原生依赖时用它——但上游自 2021-11 起冻结，新项目应改用有人维护的 fork `@cantoo/pdf-lib`。 | C（4/6） | [→](pdf-lib.zh.md) |
| **jsPDF** | 当 Web 应用需要一个“下载 PDF”按钮，在浏览器里按坐标摆放文字和图片生成收据、标签、票据或证书时用它——但它改不了已有 PDF，`html()` 遇到现代 CSS 也会走样。 | B（5/6） | [→](jspdf.zh.md) |
| **pdfcn** | 要用 shadcn CLI 把带主题的 React PDF 组件和整页文档模板（发票、报告、面单）复制进项目、底下跑 Takumi 或 Forme 时用它——只生成新 PDF。 | B（6/6） | [→](pdfcn.zh.md) |
| **FPDI** | 当基于 FPDF／TCPDF／tFPDF 的 PHP 应用要把已有 PDF 的页面当模板导入时用它——免费解析器不支持加密文件与压缩交叉引用流。 | A（5/6） | [→](fpdi.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [pdf-lib](pdf-lib.zh.md) | ✅ | C（4/6） | 换来一个带类型、纯 JS、月下载量数千万的 PDF 写入库；代价是不能渲染、不能 HTML 转 PDF、浏览器包约 500KB，且上游的 bug 永远不会修。 |
| [jsPDF](jspdf.zh.md) | ✅ | B（5/6） | 不需要后端、可离线生成 PDF，在 JS 方案里历史最久；代价是每个坐标都得手算、没有自动分页排版，靠少数几位维护者、近来主要只发安全修复。 |
| [pdfcn](pdfcn.zh.md) | ✅ | B（6/6） | 用 shadcn CLI 复制进项目的 React PDF 组件与整页模板，坐在 Takumi/Forme WASM 引擎上；无版本可锁，只生成不编辑。 |
| [FPDI](fpdi.zh.md) | ✅ | A（5/6） | 在 PHP 写入库里把已有 PDF 的页面当模板导入；免费解析器不支持加密 PDF 与压缩交叉引用流。 |

## 什么该放这里

主要职责是**用应用代码产出一份新 PDF** 的库：绘图 API、HTML／组件转 PDF、把已有页面导入新文档。pdf-lib 也能改已有文件，但重心在创建。不含对已有文件的原地改写或签名（见 `pdf-transform-signing`）。
