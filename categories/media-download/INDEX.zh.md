# media-download

> 分类节点。通过 CLI 或库从流媒体站点下载音视频。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **youtube-dl** | 当脚本或老流水线已经钉着 youtube-dl、要靠它约 1000 个站点 extractor 按模板文件名拉取媒体时用它——但最后一个打 tag 的发布还是 2021.12.17，master 自 2025-11 起也无提交，涉及 YouTube 请默认用 yt-dlp 分叉。 | B（6/6） | [→](youtube-dl.zh.md) |
| **you-get** | 当你想要一个极简 Python CLI 从 YouTube 和大量中文站点（B 站/优酷）抓取音视频时用它——比 yt-dlp 更轻。 | D（3/6） | [→](you-get.zh.md) |
| **cobalt** | 当你想自托管一个页面、让网络里任何人粘个社交平台链接就拿到视频或音频、没有广告和追踪器时用它——但 API 是 AGPL-3.0，Web 前端是禁止商用的 CC-BY-NC-SA，它也不是可脚本化的 CLI。 | C（5/6） | [→](cobalt.zh.md) |
| **lux** | 当你想用一个静态 Go 单文件下载视频、尤其是 Bilibili、抖音这类中文站点，并塞进精简容器或 CI runner 时用它——但站点覆盖比 yt-dlp 窄、修复更慢，master 自 2025-12 起已无提交。 | B（5/6） | [→](lux.zh.md) |
| **youtube-transcript-api** | 当你想免密钥地为 RAG／摘要管线取回带时间戳的 YouTube 字幕时用它——但它依赖未公开接口、随时可能失效，且云端／机房 IP 现已必须配付费住宅代理。 | B（6/6） | [→](youtube-transcript-api.zh.md) |
| **bulk-downloader-for-reddit** | 当你想用脚本归档某个子版块、用户或自己收藏的帖子——媒体文件连同标题、得分、评论树——走 Reddit OAuth API 时用它——但列表上限约 1000 帖无法绕过，近期登录失败问题未修，最后一次发布还在 2023 年。 | D（4/6） | [→](bulk-downloader-for-reddit.zh.md) |
| **yt-dlp** | 当你要把数千个站点里的视频、播客或整个播放列表存成合并好的单个文件，或让定时任务只抓新上传时用它——但它解不了 DRM 流，而且完整支持 YouTube 现在需要装一个 JavaScript 运行时。 | A（6/6） | [→](yt-dlp.zh.md) |
| **gallery-dl** | 当你想把约 390 个受支持站点上某位画师、某个标签搜索或某个账号的原图全部存下来，并且重跑时只拉新文件时用它——但 2026 年一次 DMCA 通知后开发已迁到 Codeberg，GitHub 仓库只剩发版提交。 | B（6/6） | [→](gallery-dl.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [youtube-dl](youtube-dl.zh.md) | ✅ | B（6/6） | 换来一个 Unlicense 许可、选项大家都熟的 CLI；代价是时效——pip 装到的仍是 2021 年的版本，站点一改就比 yt-dlp 修得慢。 |
| [you-get](you-get.zh.md) | ✅ | D（3/6） | 当你想要一个极简 Python CLI 从 YouTube 和大量中文站点（B 站/优酷）抓取音视频时用它——比 yt-dlp 更轻。 |
| [cobalt](cobalt.zh.md) | ✅ | C（5/6） | 换来一个友好的浏览器前端，不用每台机器装 CLI；代价是网络 copyleft 义务、不可商用的前端，以及 2026-04 以来的提交停顿——做流水线请用 yt-dlp。 |
| [lux](lux.zh.md) | ✅ | B（5/6） | 换来零运行时部署和分段并行下载；代价是覆盖广度和修复速度，维护高度集中在一人，合并分段仍要 FFmpeg。 |
| [youtube-transcript-api](youtube-transcript-api.zh.md) | ✅ | B（6/6） | 当你想免密钥地为 RAG／摘要管线取回带时间戳的 YouTube 字幕时用它——但它依赖未公开接口、随时可能失效，且云端／机房 IP 现已必须配付费住宅代理。 |
| [bulk-downloader-for-reddit](bulk-downloader-for-reddit.zh.md) | ✅ | D（4/6） | 换来一条命令、按目录模板可复现的 Reddit 备份；代价是 API 的历史深度硬上限，修复只落在未发布的 development 分支。 |
| [yt-dlp](yt-dlp.zh.md) | ✅ | A（6/6） | 站点一变，提取器大约按月修好，挑格式、用 ffmpeg 合并、下载存档都是内置的；代价是依赖一支志愿者团队，而且站点一改就得跟着更新。 |
| 其他下载器 / 更活跃的分叉 | 未收录 | — | 各页对比里点到的其他下载器与分叉。 |

## 什么该放这里

主要职责是**从流媒体/托管站点抓取媒体**的工具（提取器、下载器）。不含媒体转码/编码（见 `media-processing`），不含通用文件服务器（见 `document-management`）。
