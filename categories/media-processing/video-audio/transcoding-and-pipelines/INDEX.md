# transcoding-and-pipelines

> Leaf of [video-audio](../INDEX.md). Codec-, container- and pipeline-level tooling: the FFmpeg CLI and its bindings, in-process libav access, real-time element graphs, preset transcoders, and HLS manifest parsing.
> ← up to [video-audio](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FFmpeg** | The universal audio/video framework — `ffmpeg`/`ffprobe`/`ffplay` CLIs plus the `libav*` libraries that decode, encode, transcode, mux, demux, and filter virtually any media format in existence. | A (4/6) | [→](ffmpeg.md) |
| **ffmpeg-python** | Python bindings for FFmpeg that let you build complex filter graphs as chained Python expressions instead of hand-writing `-filter_complex` strings — it constructs the FFmpeg command line for you and shells out to the `ffmpeg` binary. | C (4/6) | [→](ffmpeg-python.md) |
| **GStreamer** | A pipeline-based multimedia framework for building real-time audio/video processing applications — not a CLI tool, but a graph of pluggable elements you wire together in code. | A (4/6) | [→](gstreamer.md) |
| **HandBrake** | Open-source video transcoder for converting video from nearly any format to modern, widely supported codecs — built on FFmpeg, x264, and x265 with a preset-driven GUI and a matching `HandBrakeCLI` command-line tool. | A (5/6) | [→](handbrake.md) |
| **PyAV** | Pythonic bindings to FFmpeg's `libav*` libraries — in-process decode/encode with frame-by-frame access to NumPy arrays and Python bytes, no subprocess spawning. | A (6/6) | [→](pyav.md) |
| **m3u8** | A Python parser and serializer for HLS (HTTP Live Streaming) `.m3u8` playlists — load a playlist from a URL, file, or string into a typed object model, inspect/modify segments and variants, and dump it back out (RFC 8216). | C (3/6) | [→](m3u8.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.md) | ✅ | A (4/6) | Pick it when any format must go in or out and you accept writing the command line; pick [PyAV](pyav.md) when you need frames inside a Python process instead of a subprocess. |
| [PyAV](pyav.md) | ✅ | A (6/6) | Pick it for in-process frame access with NumPy interop; the price is a heavier install (Cython against FFmpeg headers) and libav-level APIs rather than convenience. |
| [GStreamer](gstreamer.md) | ✅ | A (4/6) | Pick it for a long-running real-time or embedded pipeline; pick [ffmpeg-python](ffmpeg-python.md) when the job is a batch command you want to express in Python. |
| [HandBrake](handbrake.md) | ✅ | A (5/6) | Pick it for preset-driven rips and transcodes with a GUI or `HandBrakeCLI`; it is an end-user application, so reach for FFmpeg when you need to script the filter graph itself. |
| [m3u8](m3u8.md) | ✅ | C (3/6) | Pick it to parse or rewrite HLS playlists as typed objects; for downloading or muxing the segments themselves use [FFmpeg](ffmpeg.md). |

## What belongs here

Codec, container and pipeline tooling: transcoding/encoding CLIs and their language bindings, in-process libav access, real-time element graphs, preset transcode apps, and streaming-manifest parsers. Not editing/authoring APIs or cut-decision tools (see [editing-and-cutting](../editing-and-cutting/INDEX.md)), not transcription or subtitle machinery (see [speech-and-subtitles](../speech-and-subtitles/INDEX.md)), and not GUI editors (see [video-editing](../../video-editing/INDEX.md)).
