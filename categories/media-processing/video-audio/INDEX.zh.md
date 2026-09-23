# video-audio

> 分类节点。音视频编解码、剪辑与语音工具，按能力拆开：转码管线、程序化剪辑与剪切、语音与字幕机制。
> ← 返回[media-processing](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 分类 | 何时用 | 路由 |
|---|---|---|
| **transcoding-and-pipelines** | 编解码与封装层工作：FFmpeg CLI 及其绑定、进程内 libav 访问、实时元素图、预设转码器、HLS 清单解析。 | [→](transcoding-and-pipelines/INDEX.zh.md) |
| **editing-and-cutting** | 用代码组装或决定一次剪辑：程序化剪辑／合成库、可用来造编辑器的时线引擎，以及替人挑切点的工具。 | [→](editing-and-cutting/INDEX.zh.md) |
| **speech-and-subtitles** | 转写、字幕重定时，以及把字幕和抽帧交给 agent 的视频理解。 | [→](speech-and-subtitles/INDEX.zh.md) |

## 什么该放这里

应用层之下的音视频工具：解码、编码、转码、封装、字幕与管线工具，以及用代码剪辑媒体的库与框架。叶子达到 fanout 上限（`MAX_FANOUT`，默认 12 个项目）后，按上面的三个子分类拆开。不含面向最终用户的图形化编辑器（见 [video-editing](../video-editing/INDEX.zh.md)）、不含对别人家编辑器做程序化控制（见 [nle-automation](../nle-automation/INDEX.zh.md)）、也不含端到端视频生成（见 [video-production](../../video-production/INDEX.zh.md)）。
