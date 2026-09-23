---
name: youtube-transcript-api
slug: youtube-transcript-api
repo: https://github.com/jdepoix/youtube-transcript-api
category: media-download
tags: [youtube, transcript, subtitles, captions, scraping, python, library]
language: Python
license: MIT
maturity: v1.2.4, active, ~7.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-05-19T18:17:07Z
  default_branch: master
  default_branch_sha: 72d79711ec4db95262660029b4d63298b0820502
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:36:17Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 13
        active_weeks_13: 1
        carve_out: mature_library_lindy
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 14.8
        qualifying_issues: 4
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: youtube-transcript-api
        dependent_repos_count: 205
        downloads_last_month: 16400197
        graph_tier: C
        volume_tier: A
        cross_check_divergence: 1.04
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3077
        last_commit_age_days: 13
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 4
        top1_share: 0.765
        top3_share: 0.941
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# youtube-transcript-api

一个 Python 库，获取 YouTube 视频的字幕/转写文本（含自动生成的）——无需 API key、无需无头浏览器——靠调用 YouTube 网页端用的那个未公开端点。

![youtube-transcript-api — 健康度雷达](../../assets/health/youtube-transcript-api.zh.svg)

## 何时使用

你在搭一条对 YouTube 视频做摘要或建索引的流水线——一个 RAG 语料库、一个「把这场演讲 TL;DR 一下」的机器人、一个能在数百份讲座转写里检索的研究工具——你要的是口述文本，不是音频。官方 YouTube Data API 不经 OAuth 和频道所有权不会把完整字幕文本给你，而起一套 Selenium 去爬播放器既慢又脆。你 `pip install youtube-transcript-api`，然后 `YouTubeTranscriptApi().fetch(video_id)` 就把带时间戳的转写作为普通对象返回，可以直接喂给 LLM 或某个格式化器（SRT/WebVTT/JSON/纯文本）。你能指定偏好语言列表、在手动与自动生成轨道间回退，甚至让 YouTube 把转写翻译成另一种语言——全都几行代码、免 key 搞定。

它作为一块*积木*最闪光：它是某个更大应用底下的「转写获取」层，用在 notebook 和批处理任务里，让你以最少仪式从一个视频 ID 拿到带时间戳的文本。当你从自己的机器或住宅 IP 跑它时，免鉴权路径「就是能用」。

## 何时不用

- **没有代理的云 / 数据中心 IP。** YouTube 主动封禁来自 AWS/GCP/Azure 网段的请求；在服务器上你会撞 IP 封禁，需要走（住宅）代理——这个库内置 Webshare/通用代理支持正是因为这点，但对可靠的云端使用，这已是*必需*而非锦上添花。
- **你需要稳定、有契约的 API。** 它骑在一个**未公开**端点上。维护者直说：若 YouTube 改了实现，不保证它明天不会失效——别拿它去建一个你输不起「某天突然崩」的东西。
- **年龄限制 / 需登录的视频。** 针对受限内容的 Cookie/鉴权访问已被 YouTube API 变更拖累，无法可靠获取。[未验证]
- **关闭了字幕的视频。** 若上传者关了字幕又没有自动生成轨道，就没什么可取的——它自己不转写音频。
- **对 ToS 敏感 / 大规模高频抓取。** 对着未公开端点做海量抽取处于灰色地带，会招致限流/封禁；要走获许可的批量访问，你得换一套（往往付费/带代理的）策略。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [yt-dlp](yt-dlp.zh.md)（`--write-auto-subs`） | ✅ | 需要更广谱且也能拉字幕轨道的下载器时，选 yt-dlp。 | 这个重量级下载器也能拉字幕轨道；面广得多（多站点的媒体 + 字幕）但更重、偏 CLI——本库是聚焦、进程内、只取转写的 Python 调用。 |
| YouTube Data API v3（Captions） | 未收录 | 需要官方契约 API 且具备所需所有权/OAuth 时，选 YouTube Data API captions。 | 官方且有契约，但需要 OAuth，且字幕*下载*要频道所有权——你一般取不到任意第三方的字幕文本，而这正是本库的生态位。 |
| [Selenium](../web-automation/browser-driver-frameworks/selenium.zh.md) / Playwright 爬取 | 部分已收录 | 必须驱动真实播放器，且能接受成本和脆弱性时，选浏览器爬取。 | 真实浏览器能扛住一些播放器本身能扛的变更，但慢、吃资源、脆。本库完全绕开浏览器。Playwright 未单独收录。 |
| [Whisper](../media-processing/video-audio/whisper.zh.md)（转写音频） | ✅ | 没有字幕轨道、需要从音频生成转写时，选 Whisper。 | 当没有字幕轨道时从音频*生成*转写；算力大得多，也不与 YouTube 自家字幕时间戳对齐，但能处理关掉字幕的视频。 |

## 技术栈

- **语言：** Python（支持一系列现代 3.x 版本；用 Poetry 打包）。
- **传输：** 直接对 YouTube 未公开的网页端转写端点发 HTTP 请求——无无头浏览器、无官方 API 客户端。
- **接口面：** 一套对象 API（`YouTubeTranscriptApi().fetch(...)`、列举/翻译转写）外加格式化器（JSON、WebVTT、SRT、CSV、纯文本）和代理配置（Webshare + 通用）。

## 依赖

- **运行时：** Python 3.x 和一个 HTTP 栈（`requests` 一类）。无 API key、无浏览器、无数据库。
- **网络：** 对 YouTube 的出站访问；云/数据中心部署时，（住宅）**代理**实际上是必需的，以躲开 IP 封禁。
- **可选：** Webshare 代理集成是一等公民；也支持通用 HTTP/HTTPS 代理配置。
- **无服务要跑**——它是你 import 进来的进程内库。

## 运维难度

**低到中。** 作为库没什么要部署——`pip install`、import、调用。运维重量全在*保持不被封*：从笔记本/住宅 IP 上零摩擦；从服务器上你必须接好并付费用上轮换代理、处理间歇封禁，并在 YouTube 改端点、调用开始失败时准备好更新这个包（或等修复）。把它当作一个会按别人时间表崩的依赖，据此设计重试与回退。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 28.4 小时，基于 11 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-05；v1.2.4 于 2026-01 发布，2025–2026 间发布节奏稳定——处于**活跃**。未归档。1.x 线是一套相对较新、仍在维护的 API。
- **治理 / bus factor。** 单一维护者项目（jdepoix）外加一长串贡献者。bus-factor 风险存在，但项目在其生命周期里已多次吸收 YouTube 侧的崩坏，这才是这里相关的存活信号。[推断]
- **年龄与 Lindy 判断。** 约 8 年（2018-04 创建）且仍在活跃维护⇒ **强 Lindy** 信号——它反复挺过了 YouTube 的变更，对一个骑在未公开端点上的工具而言，这是耐久性的最好证据。
- **采用度。** 约 7.8k star，并被广泛用作 LLM/RAG 和研究工具里的转写层——真实采用度很广。[未验证]
- **风险标记。** 结构性风险**不是**治理或许可（干净 MIT）——而是**未公开端点依赖**：YouTube 单方面一改就可能让它失效，且云端使用现在依赖第三方代理。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 7.8k star、v1.2.4（2026-01）——数字对时间敏感，仅供参考。
- [未验证] 年龄限制/需登录访问的当前状态随 YouTube API 变更而移动；截至本日未确认可用。
- [推断] 大规模抽取的 ToS/法律姿态，是对未公开端点的推断，并非法律意见或确认引用的 YouTube 政策。
- [推断] 「挺过 YouTube 变更」的耐久性是从维护历史推断，并非对未来不崩的保证。
