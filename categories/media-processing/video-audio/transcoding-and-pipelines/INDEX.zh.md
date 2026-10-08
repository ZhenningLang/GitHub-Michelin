# transcoding-and-pipelines

> [video-audio](../INDEX.zh.md) 的子分类。编解码、封装与管线层工具：FFmpeg CLI 及其绑定、进程内 libav 访问、实时元素图、预设转码器，以及 HLS 清单解析。
> ← 返回 [video-audio](../INDEX.zh.md) · 根 [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **FFmpeg** | 通用音视频框架——`ffmpeg`/`ffprobe`/`ffplay` 命令行工具，加上 `libav*` 系列库，几乎能解码、编码、转码、封装、解封装、滤镜处理世面上一切媒体格式。 | A（4/6） | [→](ffmpeg.zh.md) |
| **ffmpeg-python** | 当你在 Python 里要拼 trim、concat、overlay 这类滤镜图、手写 -filter_complex 已经读不懂时用它——但它只是替已安装的 ffmpeg 二进制拼命令行，拿不到逐帧数据，且自 2022 年起已停止演进。 | C（4/6） | [→](ffmpeg-python.zh.md) |
| **GStreamer** | 当摄像头、车载屏或分析盒子要在你自己的 C、Rust 或 Python 程序里全天候跑“采集—叠加—编码—推流”管线，并能在运行中改参数时用它——但只是一次性转码文件的话，FFmpeg 命令行代码少得多。 | A（4/6） | [→](gstreamer.zh.md) |
| **HandBrake** | 当一堆手机视频、录屏或无加密光盘要压成更小、到处能播的 MP4/MKV，并想在图形界面或 HandBrakeCLI 里选个有名字的预设就完事时用它——但它永远重编码，也打不开有拷贝保护的光盘。 | A（5/6） | [→](handbrake.zh.md) |
| **PyAV** | 当 Python 代码要在同一进程里拿到每一帧解码后的画面和时间戳、并转成 NumPy 数组（比如做机器学习预处理或自定义编码）时用它——但 ffmpeg 命令已经能干完的活，用 PyAV 只会多出工作量。 | A（6/6） | [→](pyav.zh.md) |
| **m3u8** | 当 Python 代码要把 HLS .m3u8 播放列表（分片、变体流、密钥、不连续点）当类型化对象读取、检查或改写，而不是拿正则去抠时用它——但它只处理播放列表文本，不碰媒体本身，且自 2025-01 起无新提交。 | C（4/6） | [→](m3u8.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.zh.md) | ✅ | A（4/6） | 需要任何格式进、任何格式出、并且接受自己写命令行时选它；需要帧数据留在 Python 进程内而不是子进程时，选 [PyAV](pyav.zh.md)。 |
| [PyAV](pyav.zh.md) | ✅ | A（6/6） | 在进程内调用 FFmpeg 库、逐帧访问；代价是每一到三个月一个破坏 API 的大版本，当前版本要求 Python 3.12+，而且大部分提交出自一位维护者。 |
| [GStreamer](gstreamer.zh.md) | ✅ | A（4/6） | 用可插拔元素搭出能在运行时调整、可走硬件加速的实时管线；代价是学习曲线陡（caps 协商、pad、状态），插件打包还因发行版和板卡而异。 |
| [HandBrake](handbrake.zh.md) | ✅ | A（5/6） | 不用学编码参数就能转出好结果，图形界面和无头命令行都有；代价是不能只换封装、不能拼接剪辑，也没有可嵌进自己应用的稳定库 API。 |
| [m3u8](m3u8.zh.md) | ✅ | C（4/6） | 换来一个小巧、遵循 RFC 8216 的解析与回写往返；分片的下载、解密、封装仍要靠 HTTP 客户端或 FFmpeg，DASH 还得另找解析器。 |

## 什么该放这里

编解码、封装与管线层工具：转码／编码 CLI 及其语言绑定、进程内 libav 访问、实时元素图、预设转码应用、流媒体清单解析器。不含剪辑／创作 API 与切点决策工具（见 [editing-and-cutting](../editing-and-cutting/INDEX.zh.md)），不含转写与字幕机制（见 [speech-and-subtitles](../speech-and-subtitles/INDEX.zh.md)），也不含图形化编辑器（见 [video-editing](../../video-editing/INDEX.zh.md)）。
