# video-audio

> Category node. Audio/video decode, encode, transcode, mux, subtitle, and pipeline tools.
> ← back to [media-processing](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FFmpeg** | The universal audio/video framework — `ffmpeg`/`ffprobe`/`ffplay` CLIs plus the `libav*` libraries that decode, encode, transcode, mux, demux, and filter virtually any media format in existence. | A (4/6) | [→](ffmpeg.md) |
| **ffmpeg-python** | Python bindings for FFmpeg that let you build complex filter graphs as chained Python expressions instead of hand-writing `-filter_complex` strings — it constructs the FFmpeg command line for you and shells out to the `ffmpeg` binary. | C (4/6) | [→](ffmpeg-python.md) |
| **ffsubsync** | A language-agnostic CLI that automatically re-times an out-of-sync subtitle file against the video (or a reference subtitle), aligning speech segments via FFT cross-correlation. | B (5/6) | [→](ffsubsync.md) |
| **GStreamer** | A pipeline-based multimedia framework for building real-time audio/video processing applications — not a CLI tool, but a graph of pluggable elements you wire together in code. | A (4/6) | [→](gstreamer.md) |
| **HandBrake** | Open-source video transcoder for converting video from nearly any format to modern, widely supported codecs — built on FFmpeg, x264, and x265 with a preset-driven GUI and a matching `HandBrakeCLI` command-line tool. | A (5/6) | [→](handbrake.md) |
| **m3u8** | A Python parser and serializer for HLS (HTTP Live Streaming) `.m3u8` playlists — load a playlist from a URL, file, or string into a typed object model, inspect/modify segments and variants, and dump it back out (RFC 8216). | C (3/6) | [→](m3u8.md) |
| **MLT** | A multimedia framework for building non-linear video editors (NLEs) — timeline tracks, clips, transitions, filters, and compositing, with the actual codec work delegated to FFmpeg/libav underneath. Not a standalone editor; it's the engine that powers Shotcut and Kdenlive. | B (6/6) | [→](mlt.md) |
| **MoviePy** | A Python library for programmatic video editing — cutting, concatenating, compositing, text overlays, and effects — that builds FFmpeg commands under the hood but presents a higher-level, friendlier API. | B (6/6) | [→](moviepy.md) |
| **PyAV** | Pythonic bindings to FFmpeg's `libav*` libraries — in-process decode/encode with frame-by-frame access to NumPy arrays and Python bytes, no subprocess spawning. | A (6/6) | [→](pyav.md) |
| **OpenAI Whisper** | OpenAI's general-purpose automatic speech recognition model that transcribes and translates audio to English across 99 languages, with multiple size/quality tradeoffs. | A (5/6) | [→](whisper.md) |
| **claude-video** | Agent-facing `/watch` workflow that downloads videos, extracts frames, gets captions/transcripts, and hands visual/audio evidence to Claude or another skill host. | C (6/6) | [→](claude-video.md) |
| **Auto-Editor** | A CLI first-pass editor that labels every moment by loudness (or motion), cuts the silent stretches with a margin, and can export an importable timeline for Premiere/Resolve/Final Cut/ShotCut/Kdenlive instead of a rendered file. | A (6/6) | [→](auto-editor.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [claude-video](claude-video.md) | ✅ | C (6/6) | Video-understanding helper for agents; choose FFmpeg/MoviePy for production editing or Whisper for transcription-only work. |
| [Auto-Editor](auto-editor.md) | ✅ | A (6/6) | Pick it when the recurring job is "delete the dead air and hand me a timeline"; FFmpeg costs you the decision logic, HandBrake cannot detect silence at all, and MoviePy is a library you would have to program. |


## What belongs here

Audio/video decode, encode, transcode, mux, subtitle, and pipeline tools.
