# photo-editing

> 分类节点。你自己运行的开源照片编辑软件——RAW 冲洗、用于挑片和无损编辑的照片图库、位图图像编辑器——用来替代按月租用的 Lightroom 或 Photoshop。
> ← 返回[分类导航](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类下的项目

| 项目 | 何时使用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LightCraft** | 想在本机用上 Lightroom 那套挑片、冲洗、导出的流程又不交订阅，还想让智能体通过 MCP／CLI 来操作时用它——代价是它只有九天大、尚在 1.0 之前，相机色彩靠估算，RAW 格式覆盖也还薄。 | B（5/6） | [→](lightcraft.zh.md) |
| **PhotoCraft** | 没有 Photoshop 席位、又要离线改分层 PSD 时用它——调整图层、蒙版和文字保持可编辑，命令行／MCP 驱动同一个引擎——但它是一个九天大、由 agent 写成的早期 alpha，团队自评日常专业可用度约 25–35%。 | B（6/6） | [→](photocraft.zh.md) |

## 横向对比

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LightCraft](lightcraft.zh.md) | ✅ | B（5/6） | MIT 或 Apache-2.0 许可、纯 Rust 的 Lightroom 式图库加 RAW 冲洗，带 MCP／CLI 命令接口；很年轻、主要由 AI 智能体写成，没有实测色彩校准，CR3 只支持一部分。 |
| [PhotoCraft](photocraft.zh.md) | ✅ | B（6/6） | 离线、长得像 Photoshop 的 Rust 编辑器，原生 PSD 图层，带 CLI／MCP 接口；代价是极其年轻、一两天一个版本、不兼容 AI 和 Photoshop 插件，净室声明也无法核实。 |
| darktable · RawTherapee | 未收录 | — | 成熟的 GPL-3.0 RAW 冲洗软件，机型覆盖和色彩科学都强得多，但工作流陌生、没有智能体接口——已在 LightCraft 的对比表里权衡，尚未收录。 |
| Adobe Lightroom · Photoshop | 非仓库 | — | 闭源订阅产品——形态上不在收录范围，在各页面里作为替代品点名。 |

## 本分类收什么

主要职责是**编辑照片**的仓库：冲洗相机 RAW 文件、为挑片和无损编辑管理照片图库，或者按像素／图层做位图编辑。不收自托管的照片备份与分享服务器（见 `document-management`，Immich 在那里）；不收矢量插画或 UI 设计画布（见 `design-editors`）；不收 AI 生图；不收在代码里调用的计算机视觉库（见 `computer-vision`）。
