---
name: youtube-dl
slug: youtube-dl
repo: https://github.com/ytdl-org/youtube-dl
category: media-download
tags: [video-download, youtube, cli, media, extractor, python, downloader]
language: Python
license: Unlicense
maturity: "active-but-slowing, last tagged release 2021.12.17, master still pushed ~2026-02, ~140.6k stars (2026-06)"
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-02-19T16:45:25Z
  default_branch: master
  default_branch_sha: 956b8c585591b401a543e409accb163eeaaa1193
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:36:01Z
  overall: B
  overall_score: 2.83
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 301
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 33.7
        qualifying_issues: 3
        band: relaxed_solo
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: youtube_dl
        dependent_repos_count: 3990
        downloads_last_month: 151625
        graph_tier: B
        volume_tier: C
        cross_check_divergence: 1.01
        release_downloads: 62785626
        release_assets: 990
        release_tier: A
        signal_basis: releases
        tier_source: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 5805
        last_commit_age_days: 301
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Unlicense
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# youtube-dl

一个命令行程序，从 YouTube 及约 1000 个其他站点下载视频和音频；靠一套打包在同一个 Python 包里的按站点划分的“extractor（抽取器）”插件驱动。

![youtube-dl — 健康度雷达](../../assets/health/youtube-dl.zh.svg)

## 何时使用

你在写一个小型的归档或入库脚本——把几场会议演讲、一个播客的历史合集、或一份课程播放列表拉到本地，交给后续做转写或重编码的流水线。你想要一个能写进 `requirements.txt`、能从 cron 或 Makefile 里调用、并通过输出模板返回可预测文件名（`-o '%(uploader)s/%(title)s.%(ext)s'`）的单一 CLI。于是你选 `youtube-dl`：一次 `pip install`、一条命令搞定，PATH 上可选装 `ffmpeg` 用于 `--extract-audio`/`--merge-output-format`，它就帮你解析格式、挑最佳流、写出文件。因为它是纯 Python、没有需要常驻的服务，它能直接嵌进现有自动化，而不必先搭基础设施。

当来源根本不是 YouTube 时你也会用它——它的价值在于 extractor 目录（约 1000 个站点：Vimeo、SoundCloud、通用 HTML5 `<video>`，以及大量地区性和小众站点）。你把一个 URL 丢给它，只要存在对应 extractor，它就把该站点的各种怪癖（鉴权、分页、manifest 解析）归一化成统一的 `--list-formats` / 格式选择接口，于是你的脚本可以对每个受支持的站点一视同仁地处理。

## 何时不用

- **你需要它今天还能真的在 YouTube 上工作。** 这是决定性的筛子。youtube-dl 最后一个*打了 tag* 的发布是 2021.12.17,master 分支的更新也已明显放缓；真正在积极维护的分叉 **yt-dlp** 修复速度快得多，也是大多数人在 YouTube 改播放器/签名逻辑后实际会去跑的那个。任何对 YouTube 有硬依赖的场景，默认用 yt-dlp，把 youtube-dl 当作遗留上游。[推断]
- **重 JS / SPA、且没有 extractor 的站点。** 它不跑浏览器，也不执行任意页面 JavaScript；那些把媒体锁在重客户端 JS、DRM（Widevine/PlayReady）或逐请求 token 机制背后、又没有现成 extractor 的站点，只会直接失败。它不是 headless 浏览器爬虫。
- **大规模下的地区限制、登录墙或限流。** 它能传 cookie/代理，但不会帮你解 CAPTCHA、轮换身份或挡 IP 封禁；用单个 IP 批量下载会被限速或封掉。绕地区/ToS 是你的问题，不是工具的。
- **法律 / ToS 暴露。** 下载受版权保护的媒体、或违反站点服务条款，责任在你；很多目标站点禁止下载，而 youtube-dl 本身在 2020 年也曾遭遇 GitHub 仓库被 DMCA 下架（后被恢复）。在没核对法律和 ToS 前，别拿它做产品底座。
- **直播、超大扇出或高并发。** 直播抓取、大规模分段 HLS/DASH、海量并行任务在这里都很脆；yt-dlp 和专用工具处理得更好。
- **你想要一个带稳定性保证的库 API。** 它能被 import(`youtube_dl.YoutubeDL`)，但内部 API 和 extractor 行为会无预告变动且容易崩——做脚本没问题，作为内嵌依赖有风险。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [yt-dlp](yt-dlp.zh.md) | ✅ | 只要任务主要依赖 YouTube 且没有钉死原版的兼容理由，默认选 yt-dlp。 | youtube-dl 的活跃维护分叉；extractor 修复更快、选项更多（SponsorBlock、更好的格式排序、aria2c 集成），CLI 基本可直接替换。就 YouTube 而言它是事实上的继任者——除非你有理由钉死上游，否则选它。 |
| [you-get](you-get.zh.md) | ✅ | 想要更简单的 Python 下载器，并接受更窄的站点目录时，选 you-get。 | Python 下载器，自带站点列表；UX 更简单，但 extractor 目录比 youtube-dl/yt-dlp 更小、跟进更不积极。 |
| [lux](lux.zh.md) | ✅ | Go 单二进制比 Python 生态和 extractor 广度更重要时，选 lux。 | Go 写的单二进制下载器（原名 annie）；无需 Python 运行时、速度快，但站点列表更窄、收录取向不同。 |
| [cobalt](cobalt.zh.md) | ✅ | 想要自托管 Web/API 服务，而不是本地 CLI 时，选 cobalt。 | 以 Web/API 为先的下载器（可自托管的服务）；浏览器友好、UX 干净，但它是一个要跑的服务，不是可 pip 安装、便于脚本化的 CLI。 |
| [gallery-dl](gallery-dl.zh.md) | ✅ | 目标是图片/图集站点，而不是视频抽取时，选 gallery-dl。 | 专攻*图片/图集*站点（booru、社交媒体图集），而非视频；与视频抽取互补，不是替代。 |

## 技术栈

- **语言：** Python（跑在系统 Python 解释器上；README 历来声称支持极宽的范围，包括 Python 2.6/2.7 和 3.2+）。[未验证]
- **架构：** 一个核心下载器 + 一大批按站点划分的 **extractor** 类；格式选择、输出模板、后处理器叠在其上。
- **后处理：** 调用外部二进制——`ffmpeg`/`avconv` 做音频抽取、remux 和合并；`rtmpdump` 处理 RTMP；`mplayer`/`mpv` 处理部分 MMS/RTSP 源。
- **分发：** 单个自包含的 Python zip/脚本，外加 PyPI 打包和各 OS 包管理器构建。

## 依赖

- **运行时：** 跑基本下载只硬性需要一个 Python 解释器。无服务、无数据库、无守护进程。
- **可选二进制（你自己装）：** `ffmpeg`（或 `avconv`）用于 `--extract-audio` / 格式合并——大多数“给我一个 MP3/MP4”的工作流都需要；`rtmpdump` 处理 RTMP 流；`mplayer`/`mpv` 处理 MMS/RTSP。
- **网络：** 到目标站点的出站 HTTP(S)；登录受限内容可选配代理和 cookie 文件（`--cookies`）。
- **没有后端要跑：** 不像基于服务的下载器，这里没东西要托管——它执行完就退出。

## 运维难度

**跑起来低，但维持“还能用”的脆弱度高。** 安装和调用都极简单：`pip install youtube-dl`（或下载二进制）、一条命令、完事——零基础设施。代价在上游：由于 YouTube 等站点频繁改播放器和签名逻辑，过时的 youtube-dl 会悄悄开始报错或返回错误格式，而放缓的发布节奏意味着修复可能拖上数周、甚至不来。实际的运维负担是*保持最新*——钉死某个版本就等于接受会崩，跟 master/nightly 或干脆换 yt-dlp 通常才是真正的维护活。一次性脚本无所谓；但任何长期对 YouTube 跑的东西，都要给“崩→修”的循环留预算。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 9.9 小时，基于 10 个 qualifying issues/PRs。
- **维护——吃老本；活跃路径在分叉上（最近一次 push 约 2026-02，最后一个打 tag 的发布是 2021.12.17，截至 2026-06）。** 未归档、master 仍偶有提交，但面对一个快速变动的目标（YouTube 改播放器/签名），打 tag 发布落下 4 年以上正是决定性信号：上游落后，yt-dlp 才发修复。把 youtube-dl 当遗留上游看待 [推断]。
- **治理与继任。** `Org` 所有（`ytdl-org/`）——一个社区组织，没有厂商或基金会。路线图的势头实际上已迁移到 **yt-dlp** 分叉，后者如今是 YouTube 抽取的事实继任者；项目的寿命是通过那个分叉延续，而非原来的 tag 线 [推断]。
- **年龄与 Lindy 判断——老且历经验证，但证明的是*耐久*而非*时效*。** 创建于 2010 年（约 16 岁），约 140k star：本索引里 Lindy 最强的工具之一，还挺过了 2020 年 GitHub DMCA 下架（后被恢复）。但年龄证明的是这个*点子*会长存，而非上游二进制今天还能在 YouTube 上工作——论时效，「年龄 × 仍活跃」会把你指向 yt-dlp。
- **风险标记。** Unlicense（公共领域）——无 copyleft/relicense 摩擦。真正的风险是 2020 年那段 DMCA 法律历史、下载本身的法律/ToS 暴露，以及最重要的——上游 tag 上的抽取器过时。任何对 YouTube 有硬依赖的场景，默认用 yt-dlp。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 140.6k GitHub star；star 数对时间敏感且不可靠——仅供参考。
- [未验证] 最后一个*打 tag* 的发布是 2021.12.17；master 分支据称在 2026-02 前后仍有提交（"nightly"/master 构建才是保持最新的那个）。tag 与 master 之间的落差是关键维护信号——依赖前请核实当前 master 活跃度。
- [推断] “yt-dlp 是更活跃的分叉、且在 YouTube 上是事实继任者”是社区普遍看法；把“默认用 yt-dlp”当作推断，决策时请重新确认两个项目各自的活跃度。
- [未验证] README 声称的 Python 支持范围（2.6/2.7/3.2+）和“约 1000 站点”数字来自项目文档且随时间变化；请对照当前仓库和 `--list-extractors` 核实。
- [未验证] 2020 年 GitHub DMCA 下架及后续恢复是被报道的历史，此处未重新核验；请自行检查仓库现状和相关法律背景。
- [推断] License 为 Unlicense（公共领域）依据仓库；若 license 条款对你的用途至关重要，请确认 LICENSE 文件。
