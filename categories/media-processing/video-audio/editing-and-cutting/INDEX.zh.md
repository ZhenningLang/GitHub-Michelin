# editing-and-cutting

> [video-audio](../INDEX.zh.md) 的子分类。程序化剪辑与剪切：用代码组装或裁剪时间线的库、可以用来搭编辑器的时线引擎，以及替你决定**切点在哪**的工具。
> ← 返回 [video-audio](../INDEX.zh.md) · 根 [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **MoviePy** | 当你要用脚本批量截取、加字幕、合成一批片段，而 FFmpeg 的滤镜字符串已经没人看得懂时用它——但维护处于滑行状态：2025-05 之后没有新版本，README 还在招维护者。 | B（6/6） | [→](moviepy.zh.md) |
| **MLT** | 当你要造一个视频编辑器，或做一条需要精确到帧的时间线（轨道、滤镜、转场）、经 FFmpeg 渲染的自动化流水线时用它——但它是框架不是应用，只想剪片请用 Shotcut 或 Kdenlive。 | B（6/6） | [→](mlt.zh.md) |
| **Auto-Editor** | 命令行粗剪工具：按响度（或画面运动）给每个时间点打标签，带缓冲地剪掉静音段；也可以不输出成片，而是导出 Premiere／Resolve／Final Cut／ShotCut／Kdenlive 可导入的时间线。 | A（6/6） | [→](auto-editor.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [MoviePy](moviepy.zh.md) | ✅ | B（6/6） | 剪辑写成普通 Python 对象、每帧都是 NumPy 数组；代价是永远重编码、吞吐低于直接用 FFmpeg，维护者很少、响应很慢。 |
| [Auto-Editor](auto-editor.zh.md) | ✅ | A（6/6） | 从素材里推导切点（响度或运动）并把结果交回 NLE 当时间线时选它；要在 Python 里执行你已经定好的切点，选 [MoviePy](moviepy.zh.md)。 |
| [MLT](mlt.zh.md) | ✅ | B（6/6） | Shotcut 和 Kdenlive 背后的时间线引擎，可从 melt、XML、C/C++ 进入；代价是没有 Python 优先的 API，围绕剪辑而非直播管线设计，约六成提交出自一位主导者。 |
| [Concat](../../video-editing/concat.zh.md) | ✅ | C（6/6） | 需要人在一个恰好可脚本化的 GUI 里剪时选 Concat；需要在管线里无头运行时选本子类，因为桌面编辑器没法当批处理任务排期。 |

## 什么该放这里

职责是**用代码组装或决定一次剪辑**的库与引擎：程序化剪辑／合成 API、用来造编辑器的时线框架，以及替人选切点的前置工具。不含它们底下的编解码／转码层（见 [transcoding-and-pipelines](../transcoding-and-pipelines/INDEX.zh.md)），不含成品图形化编辑器（见 [video-editing](../../video-editing/INDEX.zh.md)），也不含对别人家编辑器做自动化（见 [nle-automation](../../nle-automation/INDEX.zh.md)）。
