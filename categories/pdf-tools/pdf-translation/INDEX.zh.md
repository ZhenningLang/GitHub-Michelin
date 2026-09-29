# pdf-translation

> 分类节点。翻译 PDF 并保住版式、公式与分栏。
> ← 返回[pdf-tools](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **PDFMathTranslate** | 科研 PDF 必须保住公式和双栏再翻译时用它——CLI/GUI/Docker，翻译后端多；AGPL，且 1.x 钉着旧版 BabelDOC。 | C（5/6） | [→](pdfmathtranslate.zh.md) |
| **BabelDOC** | 要嵌入或调试当前 0.6 的保留排版 PDF 翻译引擎时用它——不是面向用户的成品；AGPL，只接 OpenAI，API 不受支持。 | C（6/6） | [→](babeldoc.zh.md) |
| **PDFMathTranslate-next** | 要把 BabelDOC 0.6 当 CLI/网页来跑、默认走硅基流动免费通道时用它——AGPL，Google/Bing 已撤，最后推送 2026-05。 | D（4/6） | [→](pdfmathtranslate-next.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [PDFMathTranslate](pdfmathtranslate.zh.md) | ✅ | C（5/6） | 面向用户的论文 PDF 翻译，保住版式；翻译后端多，但是 AGPL，且 1.x 钉死 BabelDOC `<0.3`。 |
| [BabelDOC](babeldoc.zh.md) | ✅ | C（6/6） | 沉浸式翻译在用的保留排版翻译引擎；只接 OpenAI，API 声明为内部，当前 0.6 不是 pdf2zh 1.x 装到的那版。 |
| [PDFMathTranslate-next](pdfmathtranslate-next.zh.md) | ✅ | D（4/6） | BabelDOC 0.6 的官方成品包装；默认硅基流动免费通道，Google/Bing 已弃用，自 2026-05 起安静。 |

## 什么该放这里

保留排版的 PDF 翻译工具及其底层引擎（BabelDOC 及 PDFMathTranslate 系列前端）。不含把 PDF 拍扁成文本的双语电子书 CLI（见 `reading-tools`）。
