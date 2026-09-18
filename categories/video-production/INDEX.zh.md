# video-production

> 分类节点。AI 编排的端到端视频制作——由编码助手内的 agent 驱动研究、脚本撰写、素材生成、合成与渲染。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenMontage** | 当你想让 AI 编程助手从一句自然语言描述出发，完成研究、脚本、素材生成、合成与渲染，产出完整视频（解说、预告片、动画、纪录片蒙太奇）时使用。 | C（6/6） | [→](open-montage.zh.md) |
| **HyperFrames** | 当你需要确定性、代码形态的视频——HTML composition 在 CI 里渲染成 MP4——并希望 agent skill 覆盖整条生产回路时用它；它是渲染引擎，不是生成式视频模型。 | B（6/6） | [→](hyperframes.zh.md) |
| **anything2explainer** | 当你想让 Claude Code / Codex skill 把一个主题做成带配音的 MG 科普讲解视频（中文或英文）时用它——9 阶段多 agent 流水线带人工确认点和量化 QC；固定黑底风格，PolyForm 非商用许可。 | C（3/6） | [→](anything2explainer.zh.md) |
| **Hypit** | 当你想让 agent 把某条特定爆款视频克隆成可编辑、词锚定的 SVML workflow，并通过换脸/换词/换 B-roll 批量出变体时用它——agent 优先、非 OSI 许可证、非常年轻。 | B（4/6） | [→](hypit.zh.md) |
| **Remotion** | 当 React 优先的团队需要久经验证的程序化视频——composition 即 React 组件、带成熟 Lambda 云渲染——且接受 source-available 许可证（3 人以下公司免费）时用它。 | A（4/6） | [→](remotion.zh.md) |
| **MoneyPrinterTurbo** | 当你需要一台可自托管的 MIT 家电（WebUI + API），把主题变成近零边际成本的口播库存素材短视频时用它——不做克隆，不需要 agent。 | A（4/6） | [→](moneyprinter-turbo.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenMontage](open-montage.zh.md) | ✅ | C（6/6） | 当你想让 AI 编程助手从一句自然语言描述出发，完成研究、脚本、素材生成、合成与渲染，产出完整视频（解说、预告片、动画、纪录片蒙太奇）时使用。 |
| [HyperFrames](hyperframes.zh.md) | ✅ | B（6/6） | 确定性的 HTML 转 MP4 渲染，带 20 个 agent skill，Apache-2.0 许可；它是引擎层，不是带治理的管线，也不是生成式画面。 |
| [anything2explainer](anything2explainer.zh.md) | ✅ | C（3/6） | Claude Code / Codex skill-pack，带完整讲解片制作方法（调研→解说词→分镜→并行构建→QC）和一条样片作质量标尺；固定 MG 风格，仅 8 天龄，PolyForm 非商用许可。 |
| [Remotion](remotion.zh.md) | ✅ | A（4/6） | React 组件式创作加成熟的 Lambda 渲染，但采用 source-available 许可、超公司规模阈值需付费；OpenMontage 内嵌的正是这一类引擎。 |
| [Hypit](hypit.zh.md) | ✅ | B（4/6） | agent 优先的爆款视频克隆，产出词锚定 SVML workflow、生成层可插拔；非 OSI 许可证，验证时仅 7 周龄，生成按付费模型 API 计费。 |
| [MoneyPrinterTurbo](moneyprinter-turbo.zh.md) | ✅ | A（4/6） | 主题→口播库存素材短视频的 MIT WebUI/API 家电；边际成本近零、画面通用、单维护者 bus factor。 |
| Runway / Pika / HeyGen | 未收录 | — | 闭源 SaaS——一键生成更快，但无管线定制、无 agent 审批门、无开源扩展性。 |
| DaVinci Resolve / Premiere Pro | 未收录 | — | 专业非线性剪辑软件——面向人工剪辑师，非 agent 驱动；需要帧级手动控制与传统后期团队时选它。 |


## 什么该放这里

主要职责是 **agent 驱动或 AI 编排的视频制作** 的工具与框架——从提示/创意到成片，涵盖研究、脚本、素材生成、合成、渲染的端到端管线。包含多管线系统、质量门、供应商选择与预算治理。不含传统媒体处理框架（见 `media-processing`），不含独立视频生成 SaaS 落地页，不含通用设计/HTML 生成器（见 `ai-design-generation`）。
