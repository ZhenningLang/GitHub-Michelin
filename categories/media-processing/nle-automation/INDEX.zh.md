# nle-automation

> 分类节点。对已安装的视频编辑器做程序化控制：生成、修改并经由编辑器自身引擎无界面导出它的原生工程（草稿）文件——位于编辑器旁边的自动化层，而不是编辑器本身。
> ← 返回[media-processing](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Jianying Headless** | 当 macOS 上的剪映工作流需要 agent 生成**可编辑**草稿——真实多轨工程，并可用应用自己的引擎原生导出 MP4——时用它；代价是仅 5 天历史、单一维护者、绑定某一个应用版本、且仅限非商用。 | D（4/6） | [→](jianying-headless.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Jianying Headless](jianying-headless.zh.md) | ✅ | D（4/6） | agent 写出可编辑剪映草稿，并用应用自己的引擎原生导出；代价是 macOS 26 加某个固定剪映版本、逐机器编译的桥接，以及非商用许可。 |
| pyJianYingDraft | 未收录 | — | 纯 Python 写草稿、不依赖应用；但它不能渲染，也覆盖不了加密的草稿格式。 |
| 剪映专业版／CapCut（闭源应用） | 未收录 | — | 厂商打磨到位的手工剪辑；没有官方支持的自动化接口。 |

## 什么该放这里

那些主要职责是**程序化驱动一个已存在的视频编辑器**的工具：写入或修改编辑器的原生工程／草稿文件、登记工程、或经由编辑器自己的引擎导出（桥接、草稿构建器、脚本 API）。不含编辑器本身（见 [video-editing](../video-editing/INDEX.zh.md)）、不含编解码与转码工具链（见 [video-audio](../video-audio/INDEX.zh.md)）、不含生产成片的端到端生成管线（见 [video-production](../../video-production/INDEX.zh.md)）、也不含驱动图形界面的桌面自动化（见 [desktop-automation](../../desktop-automation/INDEX.zh.md)）。
