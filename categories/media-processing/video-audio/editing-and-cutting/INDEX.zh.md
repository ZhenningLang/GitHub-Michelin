# editing-and-cutting

> [video-audio](../INDEX.zh.md) 的子分类。程序化剪辑与剪切：用代码组装或裁剪时间线的库、可以用来搭编辑器的时线引擎，以及替你决定**切点在哪**的工具。
> ← 返回 [video-audio](../INDEX.zh.md) · 根 [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **MoviePy** | 一个用于程序化视频编辑的 Python 库——剪辑、拼接、合成、文字叠加、特效——在底层拼装 FFmpeg 命令，但对外提供更高层、更友好的 API。 | B（6/6） | [→](moviepy.zh.md) |
| **MLT** | 用于构建非线性视频编辑器（NLE）的多媒体框架——支持时间线轨道、片段、转场、滤镜与合成，底层实际的编解码工作全部委托给 FFmpeg/libav 完成。它不是独立的剪辑软件，而是 Shotcut 和 Kdenlive 的底层引擎。 | B（6/6） | [→](mlt.zh.md) |
| **Auto-Editor** | 命令行粗剪工具：按响度（或画面运动）给每个时间点打标签，带缓冲地剪掉静音段；也可以不输出成片，而是导出 Premiere／Resolve／Final Cut／ShotCut／Kdenlive 可导入的时间线。 | A（6/6） | [→](auto-editor.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [MoviePy](moviepy.zh.md) | ✅ | B（6/6） | 剪辑是你用 Python 表达的批处理任务、时间线已知时选它；时间线本身是未知量（静音在哪）时，选 [Auto-Editor](auto-editor.zh.md)。 |
| [Auto-Editor](auto-editor.zh.md) | ✅ | A（6/6） | 从素材里推导切点（响度或运动）并把结果交回 NLE 当时间线时选它；要在 Python 里执行你已经定好的切点，选 [MoviePy](moviepy.zh.md)。 |
| [MLT](mlt.zh.md) | ✅ | B（6/6） | 你在**造**编辑器、需要带转场和滤镜的时间线模型时选它；只需要渲染一份固定合成时选 [MoviePy](moviepy.zh.md)，因为 MLT 是框架而不是成品 API。 |
| [Concat](../../video-editing/concat.zh.md) | ✅ | C（6/6） | 需要人在一个恰好可脚本化的 GUI 里剪时选 Concat；需要在管线里无头运行时选本子类，因为桌面编辑器没法当批处理任务排期。 |

## 什么该放这里

职责是**用代码组装或决定一次剪辑**的库与引擎：程序化剪辑／合成 API、用来造编辑器的时线框架，以及替人选切点的前置工具。不含它们底下的编解码／转码层（见 [transcoding-and-pipelines](../transcoding-and-pipelines/INDEX.zh.md)），不含成品图形化编辑器（见 [video-editing](../../video-editing/INDEX.zh.md)），也不含对别人家编辑器做自动化（见 [nle-automation](../../nle-automation/INDEX.zh.md)）。
