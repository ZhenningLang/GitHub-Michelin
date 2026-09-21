# speech-and-subtitles

> [video-audio](../INDEX.zh.md) 的子分类。视频链路里的语音与字幕机制：转写模型、字幕重新对齐，以及把字幕和抽帧交给 agent 的视频／音频理解。
> ← 返回 [video-audio](../INDEX.zh.md) · 根 [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenAI Whisper** | OpenAI 的通用自动语音识别模型，支持 99 种语言的转写与英译，提供多种尺寸/质量权衡。 | B（5/6） | [→](whisper.zh.md) |
| **ffsubsync** | 一个语言无关的命令行工具，把时间轴对不上的字幕文件自动重新对齐到视频（或一份参考字幕）上，靠 FFT 互相关来对齐语音段。 | B（5/6） | [→](ffsubsync.zh.md) |
| **claude-video** | 面向 agent 的 `/watch` 工作流：下载视频、抽帧、获取字幕 / 转录，并把视觉 / 音频证据交给 Claude 或其他 skill host。 | C（4/6） | [→](claude-video.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenAI Whisper](whisper.zh.md) | ✅ | B（5/6） | 你要的就是转写文本、并且想自己控制模型尺寸／质量时选它；转写只是下一步的输入时，选带转写的命令行路径（例如 [Auto-Editor](../editing-and-cutting/auto-editor.zh.md) 的 `whisper` 子命令）。 |
| [ffsubsync](ffsubsync.zh.md) | ✅ | B（5/6） | 已经有字幕、只是整体时间轴偏移时选它；完全没有字幕时选 [OpenAI Whisper](whisper.zh.md)，因为 ffsubsync 是对齐已有文本而不是生成文本。 |
| [claude-video](claude-video.zh.md) | ✅ | C（4/6） | agent 需要**看**视频（抽帧加字幕作为证据）时选它；只要转录文本作为交付物时选 [OpenAI Whisper](whisper.zh.md)，因为 claude-video 是 harness 工作流而不是 ASR 引擎。 |
| [Auto-Editor](../editing-and-cutting/auto-editor.zh.md) | ✅ | B（6/6） | 转写的用途是驱动剪切（`--edit word:` / `--edit subtitle`）时选它；只要转录质量旋钮、别的都不要时，选 [OpenAI Whisper](whisper.zh.md)。 |

## 什么该放这里

视频管线里的语音与字幕机制：ASR／转写、字幕对齐与重定时，以及输出为字幕和抽帧的 agent 视频理解。不含语音合成与声音克隆（见 [speech](../../../speech/INDEX.zh.md)），不含剪辑／剪切库（见 [editing-and-cutting](../editing-and-cutting/INDEX.zh.md)），也不含编解码／转码工具（见 [transcoding-and-pipelines](../transcoding-and-pipelines/INDEX.zh.md)）。
