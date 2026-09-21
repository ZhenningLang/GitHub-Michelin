# video-audio

> 分类节点。音视频解码、编码、转码、封装、字幕与管线工具。
> ← 返回[media-processing](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **FFmpeg** | 通用音视频框架——`ffmpeg`/`ffprobe`/`ffplay` 命令行工具，加上 `libav*` 系列库，几乎能解码、编码、转码、封装、解封装、滤镜处理世面上一切媒体格式。 | A（3/6） | [→](ffmpeg.zh.md) |
| **ffmpeg-python** | FFmpeg 的 Python 绑定，让你把复杂的滤镜图写成链式 Python 表达式，而不必手搓 `-filter_complex` 字符串——它替你拼出 FFmpeg 命令行，再去调用 `ffmpeg` 二进制。 | C（4/6） | [→](ffmpeg-python.zh.md) |
| **ffsubsync** | 一个语言无关的命令行工具，把时间轴对不上的字幕文件自动重新对齐到视频（或一份参考字幕）上，靠 FFT 互相关来对齐语音段。 | B（5/6） | [→](ffsubsync.zh.md) |
| **GStreamer** | 面向实时音视频处理应用的管线式多媒体框架——不是 CLI 工具，而是一个由可插拔元素在代码中串联而成的图（graph）。 | A（4/6） | [→](gstreamer.zh.md) |
| **HandBrake** | 开源视频转码器，用于将几乎任意格式的视频转换为现代广泛支持的编解码器——基于 FFmpeg、x264 和 x265 构建，带有预设驱动的 GUI 和配套的 `HandBrakeCLI` 命令行工具。 | A（4/6） | [→](handbrake.zh.md) |
| **m3u8** | 一个面向 HLS（HTTP Live Streaming）`.m3u8` 播放列表的 Python 解析器与序列化器——把来自 URL、文件或字符串的播放列表加载成一个类型化对象模型，查看/修改 segment 与变体，再 dump 回去（RFC 8216）。 | C（3/6） | [→](m3u8.zh.md) |
| **MLT** | 用于构建非线性视频编辑器（NLE）的多媒体框架——支持时间线轨道、片段、转场、滤镜与合成，底层实际的编解码工作全部委托给 FFmpeg/libav 完成。它不是独立的剪辑软件，而是 Shotcut 和 Kdenlive 的底层引擎。 | B（5/6） | [→](mlt.zh.md) |
| **MoviePy** | 一个用于程序化视频编辑的 Python 库——剪辑、拼接、合成、文字叠加、特效——在底层拼装 FFmpeg 命令，但对外提供更高层、更友好的 API。 | B（5/6） | [→](moviepy.zh.md) |
| **Auto-Editor** | 当第一遍剪辑是机械活时用它——一条命令按响度剪掉静音（也可按说的话来剪），然后要么渲染出剪好的文件，要么导出 Premiere / Resolve / Final Cut 能打开的工程——但它是单维护者的无界面 CLI，PyPI 渠道已停发。 | B（6/6） | [→](auto-editor.zh.md) |
| **PyAV** | 面向 FFmpeg 的 libav* 库的 Pythonic 绑定——在进程内完成解码/编码，可逐帧访问 NumPy 数组和 Python bytes，无需生成子进程。 | A（6/6） | [→](pyav.zh.md) |
| **OpenAI Whisper** | OpenAI 的通用自动语音识别模型，支持 99 种语言的转写与英译，提供多种尺寸/质量权衡。 | B（5/6） | [→](whisper.zh.md) |
| **claude-video** | 面向 agent 的 `/watch` 工作流：下载视频、抽帧、获取字幕 / 转录，并把视觉 / 音频证据交给 Claude 或其他 skill host。 | C（4/6） | [→](claude-video.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [claude-video](claude-video.zh.md) | ✅ | C（4/6） | 面向 agent 的视频理解 helper；视频生产 / 剪辑看 FFmpeg / MoviePy，只转录看 Whisper。 |
| [Auto-Editor](auto-editor.zh.md) | ✅ | B（6/6） | 想让工具自己找出并剪掉静音、且结果可能要交回 NLE 当时间线，选它；已经清楚切点、只需要执行者，选 FFmpeg / MoviePy。 |


## 什么该放这里

音视频解码、编码、转码、封装、字幕与管线工具。
