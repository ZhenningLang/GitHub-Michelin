# transcoding-and-pipelines

> Leaf of [video-audio](../INDEX.md). Codec-, container- and pipeline-level tooling: the FFmpeg CLI and its bindings, in-process libav access, real-time element graphs, preset transcoders, and HLS manifest parsing.
> ← up to [video-audio](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **FFmpeg** | The universal audio/video framework — `ffmpeg`/`ffprobe`/`ffplay` CLIs plus the `libav*` libraries that decode, encode, transcode, mux, demux, and filter virtually any media format in existence. | A (4/6) | [→](ffmpeg.md) |
| **ffmpeg-python** | Use it when Python code builds trim, concat and overlay filter graphs that would be unreadable as -filter_complex strings — but it only assembles a command line for an installed ffmpeg binary, gives no per-frame access, and has been feature-frozen since 2022. | C (4/6) | [→](ffmpeg-python.md) |
| **GStreamer** | Use it when a camera, kiosk or analytics box must run a capture-overlay-encode-stream pipeline around the clock inside your own C, Rust or Python program, changing settings live — but for one-shot file transcodes the FFmpeg CLI is far less code. | A (4/6) | [→](gstreamer.md) |
| **HandBrake** | Use it when a pile of phone videos, screen recordings or unencrypted discs must become smaller MP4/MKV files that play everywhere, chosen by a named preset in a GUI or HandBrakeCLI — but it always re-encodes and will not open copy-protected discs. | A (5/6) | [→](handbrake.md) |
| **PyAV** | Use it when Python code needs each decoded video frame, with its timestamp, as a NumPy array inside the same process — for ML preprocessing or custom encoding — but if the ffmpeg command already does the job, PyAV only adds work. | A (6/6) | [→](pyav.md) |
| **m3u8** | Use it when Python code must read, inspect or rewrite HLS .m3u8 playlists — segments, variants, keys, discontinuities — as typed objects instead of regexes — but it touches only the manifest text, never the media, and has been quiet since 2025-01. | C (4/6) | [→](m3u8.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [FFmpeg](ffmpeg.md) | ✅ | A (4/6) | Pick it when any format must go in or out and you accept writing the command line; pick [PyAV](pyav.md) when you need frames inside a Python process instead of a subprocess. |
| [PyAV](pyav.md) | ✅ | A (6/6) | In-process FFmpeg libraries with frame-level access, paid for with a major release every one to three months that breaks APIs, Python 3.12+ on current versions, and one maintainer writing most commits. |
| [GStreamer](gstreamer.md) | ✅ | A (4/6) | Live, hardware-accelerated pipelines built from pluggable elements and steered at runtime; the price is a steep learning curve — caps negotiation, pads, states — and plugin packaging that varies per distro and board. |
| [HandBrake](handbrake.md) | ✅ | A (5/6) | Good transcodes without learning encoder flags, from a GUI or a headless CLI, in exchange for no remuxing, no joining or editing, and no stable library API to embed in your own app. |
| [m3u8](m3u8.md) | ✅ | C (4/6) | Buys a small RFC 8216 parse-and-dump round trip; you still need an HTTP client or FFmpeg for the segments, and a separate parser for DASH. |

## What belongs here

Codec, container and pipeline tooling: transcoding/encoding CLIs and their language bindings, in-process libav access, real-time element graphs, preset transcode apps, and streaming-manifest parsers. Not editing/authoring APIs or cut-decision tools (see [editing-and-cutting](../editing-and-cutting/INDEX.md)), not transcription or subtitle machinery (see [speech-and-subtitles](../speech-and-subtitles/INDEX.md)), and not GUI editors (see [video-editing](../../video-editing/INDEX.md)).
