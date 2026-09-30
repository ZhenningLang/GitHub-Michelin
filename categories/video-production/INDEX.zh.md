# video-production

> 分类节点。AI 编排的端到端视频制作——由编码助手内的 agent 驱动研究、脚本撰写、素材生成、合成与渲染。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenMontage** | 当你想让 AI 编程助手从一句自然语言描述出发，完成研究、脚本、素材生成、合成与渲染，产出完整视频（解说、预告片、动画、纪录片蒙太奇）时使用。 | B（5/6） | [→](open-montage.zh.md) |
| **HyperFrames** | 当你需要确定性、代码形态的视频——HTML composition 在 CI 里渲染成 MP4——并希望 agent skill 覆盖整条生产回路时用它；它是渲染引擎，不是生成式视频模型。 | B（6/6） | [→](hyperframes.zh.md) |
| **anything2explainer** | 当你想让 Claude Code / Codex skill 把一个主题做成带配音的 MG 科普讲解视频（中文或英文）时用它——9 阶段多 agent 流水线带人工确认点和量化 QC；固定黑底风格，PolyForm 非商用许可。 | C（3/5） | [→](anything2explainer.zh.md) |
| **Hypit** | 当你想让 agent 把某条特定爆款视频克隆成可编辑、词锚定的 SVML workflow，并通过换脸/换词/换 B-roll 批量出变体时用它——agent 优先、非 OSI 许可证、非常年轻。 | C（4/6） | [→](hypit.zh.md) |
| **Remotion** | 当 React 优先的团队需要久经验证的程序化视频——composition 即 React 组件、带成熟 Lambda 云渲染——且接受 source-available 许可证（3 人以下公司免费）时用它。 | A（4/6） | [→](remotion.zh.md) |
| **MoneyPrinterTurbo** | 当你需要一台可自托管的 MIT 家电（WebUI + API），把主题变成近零边际成本的口播库存素材短视频时用它——不做克隆，不需要 agent。 | B（6/6） | [→](moneyprinter-turbo.zh.md) |
| **video-shotcraft** | 当 coding agent 应该把你的产品或网页做成电影感宣传片——150+ 张镜头配方卡、一支已验收的 36.2 秒 Remotion 模板、真实页面截图、2.5D 运镜与卡点音效——并在本机渲染时用它；仅约 2 个月历史、无 tagged release，且面向 Remotion 那个带资格门槛的许可。 | B（5/6） | [→](video-shotcraft.zh.md) |
| **OpenCreator** | 当双语频道或本地化台要把*这一条*视频做字幕、配音、竖屏重切，同一项目里还要写稿和生成，并且已经有 Codex 登录时用它——不是从零做片的管线，也没有 Linux 桌面版。 | B（6/6） | [→](open-creator.zh.md) |
| **video-use** | 当 coding agent 该对着一文件夹素材、靠打包转写稿来剪——先确认方案再 ffmpeg——而不是生成底片时用它；硬依赖 ElevenLabs Scribe，22 次提交却有 2.7 万 star。 | B（4/5） | [→](video-use.zh.md) |
| **SeeCut** | 当 coding agent 该把真人/数字人口播 A-roll 精剪成高网感动效短视频时用它：画面铺真证据截图，每版都要过一个能看视频的 AI 评委（agy 调 Gemini），交付成片加可选的剪映分层草稿；PolyForm 非商用，验证时仅 4 天龄。 | D（4/6） | [→](seecut.zh.md) |
| **fframes** | 当代码或 agent 写的动效视频要在自己的 GPU 上、不经浏览器快速渲染时用它——Rust + SVG 写帧、链接 libav 编码，每个项目自带给“看不见的作者”检查画面和响度的命令行；MIT 许可，但要原生工具链，1.0 在 2026-09-28 才发布，单人维护。 | B（4/6） | [→](fframes.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenMontage](open-montage.zh.md) | ✅ | B（5/6） | 当你想让 AI 编程助手从一句自然语言描述出发，完成研究、脚本、素材生成、合成与渲染，产出完整视频（解说、预告片、动画、纪录片蒙太奇）时使用。 |
| [HyperFrames](hyperframes.zh.md) | ✅ | B（6/6） | 确定性的 HTML 转 MP4 渲染，带 20 个 agent skill，Apache-2.0 许可；它是引擎层，不是带治理的管线，也不是生成式画面。 |
| [anything2explainer](anything2explainer.zh.md) | ✅ | C（3/5） | Claude Code / Codex skill-pack，带完整讲解片制作方法（调研→解说词→分镜→并行构建→QC）和一条样片作质量标尺；固定 MG 风格，仅 8 天龄，PolyForm 非商用许可。 |
| [video-shotcraft](video-shotcraft.zh.md) | ✅ | B（5/6） | 当成片是用真实界面截图做成的产品宣传片、且希望审美来自一套镜头库时选它——但产出的是 Remotion composition，引擎那个「3 人以上需付费」的许可门槛会跟着你的交付物走，而且它没有任何 tag。 |
| [Remotion](remotion.zh.md) | ✅ | A（4/6） | React 组件式创作加成熟的 Lambda 渲染，但采用 source-available 许可、超公司规模阈值需付费；OpenMontage 内嵌的正是这一类引擎。 |
| [Hypit](hypit.zh.md) | ✅ | C（4/6） | agent 优先的爆款视频克隆，产出词锚定 SVML workflow、生成层可插拔；非 OSI 许可证，验证时仅 7 周龄，生成按付费模型 API 计费。 |
| [MoneyPrinterTurbo](moneyprinter-turbo.zh.md) | ✅ | B（6/6） | 主题→口播库存素材短视频的 MIT WebUI/API 家电；边际成本近零、画面通用、单维护者 bus factor。 |
| [OpenCreator](open-creator.zh.md) | ✅ | B（6/6） | 本机 Codex 原生创作者桌面，已交付长处是把现成视频做翻译／配音／竖屏；生成和写作共用同一项目。必须 Codex 登录，无 Linux 桌面，嵌套 GPL 的 KrillinAI 核心。 |
| [video-use](video-use.zh.md) | ✅ | B（4/5） | 给现成 take 用的 coding-agent 剪辑器：打包 Scribe 转写、策略门、ffmpeg 渲染。MIT skill-pack，硬依赖 ElevenLabs，22 次提交／约 2.7 万 star。 |
| [SeeCut](seecut.zh.md) | ✅ | D（4/6） | 剪已有 A-roll：看片 AI 评委循环加 HyperFrames 渲染；硬依赖 agy/Google 账号、PolyForm 非商用、仅 4 天龄——对比 video-use 的纯转写 MIT 剪辑或 HyperFrames 的纯引擎 Apache。 |
| [fframes](fframes.zh.md) | ✅ | B（4/6） | Rust + SVG 写帧、Skia 在 GPU 上画、经链接的 libav 编码，带给 agent 用的 inspect／strip／audio analyze 命令；MIT，自测比 Remotion 最优配置快约 1.5 倍，代价是原生构建工具链、没有云渲染、1.0 仅两天、巴士因子为 1。 |
| Runway / Pika / HeyGen | 未收录 | — | 闭源 SaaS——一键生成更快，但无管线定制、无 agent 审批门、无开源扩展性。 |
| DaVinci Resolve / Premiere Pro | 未收录 | — | 专业非线性剪辑软件——面向人工剪辑师，非 agent 驱动；需要帧级手动控制与传统后期团队时选它。 |


## 什么该放这里

主要职责是 **agent 驱动或 AI 编排的视频制作** 的工具与框架——从提示/创意到成片，涵盖研究、脚本、素材生成、合成、渲染的端到端管线。包含多管线系统、质量门、供应商选择与预算治理。不含传统媒体处理框架（见 `media-processing`），不含独立视频生成 SaaS 落地页，不含通用设计/HTML 生成器（见 `ai-design-generation`）。
