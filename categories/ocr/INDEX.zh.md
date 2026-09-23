# ocr

> 分类节点。光学字符识别引擎——图像/扫描件转文本。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Tesseract** | 当你需要离线、可嵌入、覆盖 100+ 语言、面向清晰印刷文本的 OCR 时用它——不适合野外照片或手写。 | "?"（2/6） | [→](tesseract.zh.md) |
| **LaTeX-OCR (pix2tex)** | 当你要把数学公式图片转成 LaTeX（pix2tex）时用它——只管公式、已放缓，VLM 可能更强。 | C（4/6） | [→](latex-ocr.zh.md) |
| **Laravel OCR** | 当现有 Laravel 应用需要统一接入 Tesseract 与云 OCR，并用模板／正则抽取和持久化业务字段时用它；不适合多页扫描 PDF 或版面感知 OCR，且仓库缺少许可证正文。 | D（5/6） | [→](laravel-ocr.zh.md) |
| **PaddleOCR** | 当杂乱输入需要现代 detection+recognition、中日韩强项或表格／版式结构，而你能背负 PaddleX、推理引擎与模型下载时用它。 | A（6/6） | [→](paddleocr.zh.md) |
| **EasyOCR** | 当 PyTorch OCR 栈加不错的场景文字默认效果比自己搭预处理更省事时用它——项目最近一次实质发版是 2024-09。 | B（5/6） | [→](easyocr.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Tesseract](tesseract.zh.md) | ✅ | "?"（2/6） | 面向清晰印刷文本的成熟离线 OCR 引擎；对版面、手写、野外照片较弱。 |
| [LaTeX-OCR (pix2tex)](latex-ocr.zh.md) | ✅ | C（4/6） | 当你要把数学公式图片转成 LaTeX（pix2tex）时用它——只管公式、已放缓，VLM 可能更强。 |
| [Laravel OCR](laravel-ocr.zh.md) | ✅ | D（5/6） | Laravel 原生 OCR driver 切换，加模板／正则业务抽取；能省应用接线，但 PDF／版面处理浅、workflow 未完整接通，且仓库没有许可证正文。 |
| [PaddleOCR](paddleocr.zh.md) | ✅ | A（6/6） | 深度学习 OCR 加文档结构解析，还有 VLM 路线；这里是能力面最宽的，也是依赖最重的（PaddleX、推理引擎、模型下载）。 |
| [EasyOCR](easyocr.zh.md) | ✅ | B（5/6） | 开箱即用的 PyTorch OCR，80+ 语言、场景文字默认效果不错；但最近一次实质发版是 2024-09、约 55 个 PR 未合，应当按「正在漂移」而不是「稳定」读它。 |
| TrOCR | 未收录 | — | 面向裁剪文字行的研究模型线；这个名字还没有对应到规范仓库。 |
| Cloud Vision / Textract | 非仓库 | — | 托管商业 OCR API（Google、AWS）：没有源码、不能自托管、按页计费。 |

## 什么该放这里

主要职责是**识别图像/扫描件中文字**的引擎/库。不含面向 gen-AI 的文档版面与表格解析（见 `document-parsing`），不含文档归档/检索（见 `document-management`）。
