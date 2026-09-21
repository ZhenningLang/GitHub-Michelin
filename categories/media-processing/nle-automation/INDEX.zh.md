# nle-automation

> 分类节点。对已安装的视频编辑器做程序化控制：生成、修改并经由编辑器自身引擎无界面导出它的原生工程（草稿）文件——位于编辑器旁边的自动化层，而不是编辑器本身。
> ← 返回[media-processing](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Jianying Headless** | 当 macOS 上的剪映工作流需要 agent 生成**可编辑**草稿——真实多轨工程，并可用应用自己的引擎原生导出 MP4——时用它；代价是仅 5 天历史、单一维护者、绑定某一个应用版本、且仅限非商用。 | D（4/6） | [→](jianying-headless.zh.md) |
| **pyJianYingDraft** | 当 Python 管线需要产出可编辑剪映草稿时用它——跨平台、Apache-2.0、构建机上不需要装编辑器；代价是新版剪映草稿已加密、它不替你渲染、自带导出只在 Windows 加剪映 6 及更早版本上可用。 | C（5/6） | [→](pyjianyingdraft.zh.md) |
| **Jianying Editor Skill** | 当希望 agent 用自然语言搭出可编辑的剪映专业版时间线——B-roll、TTS 配音、对齐字幕、特效——时用它；但它是 8 个月大、单维护者、建在内嵌分叉上的 skill，无人值守导出还需要 Windows 加剪映 5.9 及更早版本。 | C（5/6） | [→](jianying-editor-skill.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Jianying Headless](jianying-headless.zh.md) | ✅ | D（4/6） | agent 写出可编辑剪映草稿，并用应用自己的引擎原生导出；代价是 macOS 26 加某个固定剪映版本、逐机器编译的桥接，以及非商用许可。 |
| [pyJianYingDraft](pyjianyingdraft.zh.md) | ✅ | C（5/6） | 在任何操作系统上用 Python 写剪映草稿，Apache-2.0；代价是碰不了加密草稿、不负责渲染，自带导出只支持 Windows 加剪映 6 及更早版本。 |
| [Jianying Editor Skill](jianying-editor-skill.zh.md) | ✅ | C（5/6） | 希望整条流程由 agent 用自然语言驱动、且剪映里仍能手改，选它；需要仍在维护的上游库，选 pyJianYingDraft，因为本 skill 的核心是内嵌分叉且测试很薄。 |
| 剪映专业版／CapCut（闭源应用） | 未收录 | — | 厂商打磨到位的手工剪辑；没有官方支持的自动化接口。 |

## 什么该放这里

那些主要职责是**程序化驱动一个已存在的视频编辑器**的工具：写入或修改编辑器的原生工程／草稿文件、登记工程、或经由编辑器自己的引擎导出（桥接、草稿构建器、脚本 API）。不含编辑器本身（见 [video-editing](../video-editing/INDEX.zh.md)）、不含编解码与转码工具链（见 [video-audio](../video-audio/INDEX.zh.md)）、不含生产成片的端到端生成管线（见 [video-production](../../video-production/INDEX.zh.md)）、也不含驱动图形界面的桌面自动化（见 [desktop-automation](../../desktop-automation/INDEX.zh.md)）。
