# editing-workflows

> 对已有素材或参考片做转写剪辑、翻译配音与变体编辑。
> ← 返回[video-production](../INDEX.zh.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Hypit** | 当你想让 agent 把某条特定爆款视频克隆成可编辑、词锚定的 SVML workflow，并通过换脸/换词/换 B-roll 批量出变体时用它——agent 优先、非 OSI 许可证、非常年轻。 | C（4/6） | [→](hypit.zh.md) |
| **OpenCreator** | 当双语频道或本地化台要把*这一条*视频做字幕、配音、竖屏重切，同一项目里还要写稿和生成，并且已经有 Codex 登录时用它——不是从零做片的管线，也没有 Linux 桌面版。 | B（6/6） | [→](open-creator.zh.md) |
| **video-use** | 当 coding agent 该对着一文件夹素材、靠打包转写稿来剪——先确认方案再 ffmpeg——而不是生成底片时用它；硬依赖 ElevenLabs Scribe，22 次提交却有 2.7 万 star。 | B（4/5） | [→](video-use.zh.md) |
| **SeeCut** | 当 coding agent 该把真人/数字人口播 A-roll 精剪成高网感动效短视频时用它：画面铺真证据截图，每版都要过一个能看视频的 AI 评委（agy 调 Gemini），交付成片加可选的剪映分层草稿；PolyForm 非商用，验证时仅 4 天龄。 | D（4/6） | [→](seecut.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Hypit](hypit.zh.md) | ✅ | C（4/6） | agent 优先的爆款视频克隆，产出词锚定 SVML workflow、生成层可插拔；非 OSI 许可证，验证时仅 7 周龄，生成按付费模型 API 计费。 |
| [OpenCreator](open-creator.zh.md) | ✅ | B（6/6） | 本机 Codex 原生创作者桌面，已交付长处是把现成视频做翻译／配音／竖屏；生成和写作共用同一项目。必须 Codex 登录，无 Linux 桌面，嵌套 GPL 的 KrillinAI 核心。 |
| [video-use](video-use.zh.md) | ✅ | B（4/5） | 给现成 take 用的 coding-agent 剪辑器：打包 Scribe 转写、策略门、ffmpeg 渲染。MIT skill-pack，硬依赖 ElevenLabs，22 次提交／约 2.7 万 star。 |
| [SeeCut](seecut.zh.md) | ✅ | D（4/6） | 剪已有 A-roll：看片 AI 评委循环加 HyperFrames 渲染；硬依赖 agy/Google 账号、PolyForm 非商用、仅 4 天龄——对比 video-use 的纯转写 MIT 剪辑或 HyperFrames 的纯引擎 Apache。 |

## 什么该放这里

对已有素材或参考片做转写剪辑、翻译配音与变体编辑。
