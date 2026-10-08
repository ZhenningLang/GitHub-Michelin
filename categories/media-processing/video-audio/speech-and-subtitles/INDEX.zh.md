# speech-and-subtitles

> [video-audio](../INDEX.zh.md) 的子分类。视频链路里的语音与字幕机制：转写模型、字幕重新对齐，以及把字幕和抽帧交给 agent 的视频／音频理解。
> ← 返回 [video-audio](../INDEX.zh.md) · 根 [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenAI Whisper** | 当几百小时多语言录音需要在自己机器上转出可检索的文字稿和 .srt 字幕、而不是按分钟付费给云端 API 时用它——但它没有流式模式，实时字幕请用 whisper.cpp 或 faster-whisper。 | A（5/6） | [→](whisper.zh.md) |
| **ffsubsync** | 一个语言无关的命令行工具，把时间轴对不上的字幕文件自动重新对齐到视频（或一份参考字幕）上，靠 FFT 互相关来对齐语音段。 | B（5/6） | [→](ffsubsync.zh.md) |
| **claude-video** | 面向 agent 的 `/watch` 工作流：下载视频、抽帧、获取字幕 / 转录，并把视觉 / 音频证据交给 Claude 或其他 skill host。 | C（6/6） | [→](claude-video.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenAI Whisper](whisper.zh.md) | ✅ | A（5/6） | OpenAI 的参考实现和公开权重；代价是 PyTorch 慢路径（large 要约 10 GB 显存）、不区分说话人，静音或音乐段不先过滤就会编出文字。 |
| [ffsubsync](ffsubsync.zh.md) | ✅ | B（5/6） | 已经有字幕、只是整体时间轴偏移时选它；完全没有字幕时选 [OpenAI Whisper](whisper.zh.md)，因为 ffsubsync 是对齐已有文本而不是生成文本。 |
| [claude-video](claude-video.zh.md) | ✅ | C（6/6） | agent 需要**看**视频（抽帧加字幕作为证据）时选它；只要转录文本作为交付物时选 [OpenAI Whisper](whisper.zh.md)，因为 claude-video 是 harness 工作流而不是 ASR 引擎。 |

## 什么该放这里

视频管线里的语音与字幕机制：ASR／转写、字幕对齐与重定时，以及输出为字幕和抽帧的 agent 视频理解。不含语音合成与声音克隆（见 [speech](../../../speech/INDEX.zh.md)），不含剪辑／剪切库（见 [editing-and-cutting](../editing-and-cutting/INDEX.zh.md)），也不含编解码／转码工具（见 [transcoding-and-pipelines](../transcoding-and-pipelines/INDEX.zh.md)）。
