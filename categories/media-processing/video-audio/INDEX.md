# video-audio

> Category node. Audio/video codec, editing and speech tooling, split by capability: transcoding pipelines, programmatic editing and cutting, and speech/subtitle machinery.
> ← back to [media-processing](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Category | Use when | Route |
|---|---|---|
| **transcoding-and-pipelines** | Codec/container work: the FFmpeg CLI and its bindings, in-process libav access, real-time element graphs, preset transcoders, HLS manifest parsing. | [→](transcoding-and-pipelines/INDEX.md) |
| **editing-and-cutting** | Composing or deciding an edit in code: programmatic cutting/compositing libraries, timeline engines to build editors on, and tools that pick where the cuts go. | [→](editing-and-cutting/INDEX.md) |
| **speech-and-subtitles** | Transcription, subtitle re-timing, and agent-facing video understanding that surfaces transcripts and frames. | [→](speech-and-subtitles/INDEX.md) |

## What belongs here

Audio/video tooling below the application layer: decode, encode, transcode, mux, subtitle, and pipeline tools, plus the libraries and frameworks that edit media programmatically. Split into three leaves above when the leaf reached the fanout cap (`MAX_FANOUT`, default 12 pages). Not end-user GUI editors (see [video-editing](../video-editing/INDEX.md)), not programmatic control of someone else's editor (see [nle-automation](../nle-automation/INDEX.md)), and not end-to-end video generation (see [video-production](../../video-production/INDEX.md)).
