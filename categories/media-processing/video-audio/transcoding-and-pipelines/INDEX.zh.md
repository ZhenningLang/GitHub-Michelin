# transcoding-and-pipelines

> [video-audio](../INDEX.zh.md) 的子分类。编解码、封装与管线层工具：FFmpeg CLI 及其绑定、进程内 libav 访问、实时元素图、预设转码器，以及 HLS 清单解析。
> ← 返回 [video-audio](../INDEX.zh.md) · 根 [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **FFmpeg** | 通用音视频框架——`ffmpeg`/`ffprobe`/`ffplay` 命令行工具，加上 `libav*` 系列库，几乎能解码、编码、转码、封装、解封装、滤镜处理世面上一切媒体格式。 | A（3/6） | [→](ffmpeg.zh.md) |
| **ffmpeg-python** | FFmpeg 的 Python 绑定，让你把复杂的滤镜图写成链式 Python 表达式，而不必手搓 `-filter_complex` 字符串——它替你拼出 FFmpeg 命令行，再去调用 `ffmpeg` 二进制。 | C（4/6） | [→](ffmpeg-python.zh.md) |
| **GStreamer** | 面向实时音视频处理应用的管线式多媒体框架——不是 CLI 工具，而是一个由可插拔元素在代码中串联而成的图（graph）。 | A（4/6） | [→](gstreamer.zh.md) |
| **HandBrake** | 开源视频转码器，用于将几乎任意格式的视频转换为现代广泛支持的编解码器——基于 FFmpeg、x264 和 x265 构建，带有预设驱动的 GUI 和配套的 `HandBrakeCLI` 命令行工具。 | A（4/6） | [→](handbrake.zh.md) |
| **PyAV** | 面向 FFmpeg 的 libav* 库的 Pythonic 绑定——在进程内完成解码/编码，可逐帧访问 NumPy 数组和 Python bytes，无需生成子进程。 | A（6/6） | [→](pyav.zh.md) |
| **m3u8** | 一个面向 HLS（HTTP Live Streaming）`.m3u8` 播放列表的 Python 解析器与序列化器——把来自 URL、文件或字符串的播放列表加载成一个类型化对象模型，查看/修改 segment 与变体，再 dump 回去（RFC 8216）。 | C（3/6） | [→](m3u8.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.zh.md) | ✅ | A（3/6） | 需要任何格式进、任何格式出、并且接受自己写命令行时选它；需要帧数据留在 Python 进程内而不是子进程时，选 [PyAV](pyav.zh.md)。 |
| [PyAV](pyav.zh.md) | ✅ | A（6/6） | 需要进程内逐帧访问并与 NumPy 互操作时选它；代价是安装更重（要对着 FFmpeg 头文件编译 Cython），而且拿到的是 libav 级 API 而非便利封装。 |
| [GStreamer](gstreamer.zh.md) | ✅ | A（4/6） | 需要长时间运行的实时或嵌入式管线时选它；任务只是「一条想用 Python 表达的批处理命令」时，选 [ffmpeg-python](ffmpeg-python.zh.md)。 |
| [HandBrake](handbrake.zh.md) | ✅ | A（4/6） | 需要预设驱动的转码、并且要 GUI 或 `HandBrakeCLI` 时选它；它是面向最终用户的应用，要自己掌控滤镜图就回到 FFmpeg。 |
| [m3u8](m3u8.zh.md) | ✅ | C（3/6） | 需要把 HLS 播放列表当类型化对象解析或改写时选它；要真正下载或封装分片，用 [FFmpeg](ffmpeg.zh.md)。 |

## 什么该放这里

编解码、封装与管线层工具：转码／编码 CLI 及其语言绑定、进程内 libav 访问、实时元素图、预设转码应用、流媒体清单解析器。不含剪辑／创作 API 与切点决策工具（见 [editing-and-cutting](../editing-and-cutting/INDEX.zh.md)），不含转写与字幕机制（见 [speech-and-subtitles](../speech-and-subtitles/INDEX.zh.md)），也不含图形化编辑器（见 [video-editing](../../video-editing/INDEX.zh.md)）。
