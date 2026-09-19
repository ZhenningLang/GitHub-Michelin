# media-download

> Category node. Download video/audio from streaming sites via CLI or library.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **youtube-dl** | Use it when you need a battle-tested CLI/library to download video & audio from YouTube and 1000+ sites — but prefer the active yt-dlp fork for hot sites. | B (6/6) | [→](youtube-dl.md) |
| **you-get** | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. | D (3/6) | [→](you-get.md) |
| **cobalt** | Use it when you want a clean self-hostable web-UI + API media saver with no ads/trackers — not a scriptable CLI. | B (5/6) | [→](cobalt.md) |
| **lux** | Use it when you want a fast single-binary Go downloader, strong on Chinese video sites — smaller coverage and slower updates than yt-dlp. | B (5/6) | [→](lux.md) |
| **youtube-transcript-api** | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. | A (6/6) | [→](youtube-transcript-api.md) |
| **bulk-downloader-for-reddit** | Use it when you want a scriptable, reproducible Reddit archive of files plus metadata via OAuth — but Reddit's ~1000-post listing cap is unbypassable, and releases have stalled since early 2023 (GPL-3.0). | D (4/6) | [→](bulk-downloader-for-reddit.md) |
| **yt-dlp** | Use it when you need an actively maintained CLI to download video & audio from YouTube and thousands of other sites — the de-facto successor to youtube-dl with faster fixes and more features. | A (6/6) | [→](yt-dlp.md) |
| **gallery-dl** | Command-line program to download image galleries and collections from several image hosting sites | B (6/6) | [→](gallery-dl.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [youtube-dl](youtube-dl.md) | ✅ | B (6/6) | Battle-tested extractor for 1000+ sites; upstream has slowed, so treat yt-dlp as the live fork for YouTube. |
| [you-get](you-get.md) | ✅ | D (3/6) | Use it when you want a tiny Python CLI to grab video/audio from YouTube and many Chinese sites (Bilibili/Youku) — lighter than yt-dlp. |
| [cobalt](cobalt.md) | ✅ | B (5/6) | Use it when you want a clean self-hostable web-UI + API media saver with no ads/trackers — not a scriptable CLI. |
| [lux](lux.md) | ✅ | B (5/6) | Use it when you want a fast single-binary Go downloader, strong on Chinese video sites — smaller coverage and slower updates than yt-dlp. |
| [youtube-transcript-api](youtube-transcript-api.md) | ✅ | A (6/6) | Use it when you need timestamped YouTube transcripts key-free for a RAG/summarization pipeline — but it rides an undocumented endpoint that can break anytime, and cloud/datacenter IPs now require paid residential proxies. |
| [bulk-downloader-for-reddit](bulk-downloader-for-reddit.md) | ✅ | D (4/6) | Use it when you want a scriptable, reproducible Reddit archive of files plus metadata via OAuth — but Reddit's ~1000-post listing cap is unbypassable, and releases have stalled since early 2023 (GPL-3.0). |
| [yt-dlp](yt-dlp.md) | ✅ | A (6/6) | Actively maintained CLI for downloading video/audio from YouTube and thousands of sites; de-facto successor to youtube-dl with faster extractor fixes and modern features. |
| Other downloaders / more-active forks | 未收录 | — | Alternative downloaders and forks named across the pages. |

## What belongs here

Tools whose primary job is **fetching media from streaming/hosting sites** (extractors, downloaders). Not media transcoding/encoding (see `media-processing`), not generic file servers (see `document-management`).
