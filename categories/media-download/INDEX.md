# media-download

> Category node. Download video/audio from streaming sites via CLI or library.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **youtube-dl** | Use it when a script or legacy pipeline already pins youtube-dl to pull media through its ~1000 site extractors with templated filenames — but the last tagged release is 2021.12.17 and master is quiet since 2025-11, so default to the yt-dlp fork for YouTube. | B (6/6) | [→](youtube-dl.md) |
| **you-get** | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. | D (3/6) | [→](you-get.md) |
| **cobalt** | Use it when you want a self-hosted page where anyone on your network pastes a social-media link and gets the video or audio, ad- and tracker-free — but the API is AGPL-3.0, the web UI is non-commercial CC-BY-NC-SA, and it is no scriptable CLI. | C (5/6) | [→](cobalt.md) |
| **lux** | Use it when you want one static Go binary to fetch videos, especially from Chinese sites like Bilibili and Douyin, inside a slim container or CI runner — but it covers fewer sites than yt-dlp, fixes ship slower, and master is quiet since 2025-12. | B (5/6) | [→](lux.md) |
| **youtube-transcript-api** | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. | B (6/6) | [→](youtube-transcript-api.md) |
| **bulk-downloader-for-reddit** | Use it when you want a scriptable OAuth archive of a subreddit, user or your saved posts — media plus titles, scores and comment trees — but listings cap at ~1000 posts, login failures are open, and the last release is from 2023. | D (4/6) | [→](bulk-downloader-for-reddit.md) |
| **yt-dlp** | Use it when you need a video, podcast or playlist from thousands of sites saved as one merged file, or a cron job fetching only new uploads — but it cannot decrypt DRM, and full YouTube support now needs a JavaScript runtime. | A (6/6) | [→](yt-dlp.md) |
| **gallery-dl** | Use it when you want every original image from an artist's page, tag search or account on ~390 supported sites, with reruns fetching only new files — but after a 2026 DMCA notice development moved to Codeberg; GitHub only gets release bumps. | B (6/6) | [→](gallery-dl.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [youtube-dl](youtube-dl.md) | ✅ | B (6/6) | Buys an Unlicense CLI with an option set everyone knows; costs freshness — pip still installs a 2021 build, so site breakage outlasts yt-dlp's fixes. |
| [you-get](you-get.md) | ✅ | D (3/6) | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. |
| [cobalt](cobalt.md) | ✅ | C (5/6) | Buys a friendly browser front end with no CLI to install per machine; costs network-copyleft obligations, a non-commercial UI, and a commit pause since 2026-04 — pipelines want yt-dlp. |
| [lux](lux.md) | ✅ | B (5/6) | Buys zero-runtime deployment and parallel segment downloads; costs breadth and repair speed, one dominant maintainer, and FFmpeg still needed for merging. |
| [youtube-transcript-api](youtube-transcript-api.md) | ✅ | B (6/6) | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. |
| [bulk-downloader-for-reddit](bulk-downloader-for-reddit.md) | ✅ | D (4/6) | Buys a reproducible, folder-templated Reddit backup from one CLI; costs the API's hard history ceiling and fixes that live only on an unreleased development branch. |
| [yt-dlp](yt-dlp.md) | ✅ | A (6/6) | Extractors fixed about monthly as sites change, with format selection, ffmpeg merging and download archives built in; you depend on a volunteer team and on keeping yt-dlp updated as sites break it. |
| Other downloaders / more-active forks | 未收录 | — | Alternative downloaders and forks named across the pages. |

## What belongs here

Tools whose primary job is **fetching media from streaming/hosting sites** (extractors, downloaders). Not media transcoding/encoding (see `media-processing`), not generic file servers (see `document-management`).
