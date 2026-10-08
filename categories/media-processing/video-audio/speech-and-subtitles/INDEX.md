# speech-and-subtitles

> Leaf of [video-audio](../INDEX.md). Speech and subtitle machinery around video: transcription models, subtitle re-timing, and agent-facing video/audio understanding that surfaces transcripts and frames.
> ← up to [video-audio](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OpenAI Whisper** | Use it when hours of multilingual recordings need searchable transcripts and .srt subtitles produced on your own machine instead of a per-minute cloud API — but there is no streaming mode, so live captions need whisper.cpp or faster-whisper. | A (5/6) | [→](whisper.md) |
| **ffsubsync** | A language-agnostic CLI that automatically re-times an out-of-sync subtitle file against the video (or a reference subtitle), aligning speech segments via FFT cross-correlation. | B (5/6) | [→](ffsubsync.md) |
| **claude-video** | Agent-facing `/watch` workflow that downloads videos, extracts frames, gets captions/transcripts, and hands visual/audio evidence to Claude or another skill host. | C (6/6) | [→](claude-video.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OpenAI Whisper](whisper.md) | ✅ | A (5/6) | OpenAI's reference implementation and open weights, in exchange for the slow PyTorch path (large needs ~10 GB VRAM), no speaker diarization, and hallucinated text over silence or music unless you gate it. |
| [ffsubsync](ffsubsync.md) | ✅ | B (5/6) | Pick it when subtitles exist but their timing is off by a global offset; pick [OpenAI Whisper](whisper.md) when there are no subtitles at all, because ffsubsync aligns existing text rather than producing it. |
| [claude-video](claude-video.md) | ✅ | C (6/6) | Pick it when an agent needs to *watch* a video (frames plus captions as evidence); pick [OpenAI Whisper](whisper.md) when the transcript alone is the deliverable, because claude-video is a harness workflow, not an ASR engine. |

## What belongs here

Speech and subtitle machinery in a video pipeline: ASR/transcription, subtitle alignment and re-timing, and agent-facing video understanding whose output is transcripts and frames. Not speech synthesis or voice cloning (see [speech](../../../speech/INDEX.md)), not editing or cutting libraries (see [editing-and-cutting](../editing-and-cutting/INDEX.md)), and not codec/transcode tooling (see [transcoding-and-pipelines](../transcoding-and-pipelines/INDEX.md)).
