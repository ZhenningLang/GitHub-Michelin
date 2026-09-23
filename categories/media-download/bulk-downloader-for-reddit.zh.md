---
name: bulk-downloader-for-reddit
slug: bulk-downloader-for-reddit
repo: https://github.com/Serene-Arc/bulk-downloader-for-reddit
category: media-download
tags: [reddit, downloader, archiver, scraping, yt-dlp, python, cli]
language: Python
license: GPL-3.0
maturity: v2.6.2 (2023-01), commits ongoing to 2026-04, ~2.6k stars (as of 2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-04-12T02:28:43Z
  default_branch: master
  default_branch_sha: 8c293a46843c818bea2c2013db38191867993a14
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:35:17Z
  overall: D
  overall_score: 0.5
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1331
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 31160
        release_assets: 60
        release_tier: D
        signal_basis: releases
    longevity:
      grade: E
      raw:
        repo_age_days: 3022
        last_commit_age_days: 1331
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# bulk-downloader-for-reddit

一个命令行工具（BDFR），从 Reddit 下载媒体并/或归档元数据——子版块、multireddit、用户、收藏/点赞的帖子，或直接链接——经由官方 Reddit OAuth API。

![bulk-downloader-for-reddit — 健康度雷达](../../assets/health/bulk-downloader-for-reddit.zh.svg)

## 何时使用

你在一个子版块转私前抢救性归档它，或者备份你自己收藏/点赞过的帖子，又或者从几个社区攒一份个人的图片和视频数据集。你不想点开成百上千个帖子，而且你既要*文件*（图片、相册、Redgifs/Imgur/YouTube 上的片段），也要*上下文*（帖子标题、得分、评论树）落到磁盘上，按一个可预期的目录布局。你注册一个 Reddit API 应用拿到 OAuth 凭据，然后跑 `bdfr download ./out --subreddit pics --limit 200 --sort top`，或 `bdfr clone ./out --user me --upvoted` 把文件和元数据一并抓下。BDFR 用自带解析器加 yt-dlp 把每个帖子的链接解出来，按你控制的模板命名文件，按哈希去重，并留一份日志，让重跑是增量的，而非把所有东西重下一遍。

当你想要一份*可脚本化、可复现*的 Reddit 归档时，它是对的选择——三种模式（`download` 只下文件、`archive` 只下元数据、`clone` 两者都要）、用于可重复任务的 YAML 配置，以及一套你能钉死的目录/命名方案——而不是用某个浏览器扩展一次性抓一把。

## 何时不用

- **你想从单个来源拉超过约 1000 个帖子。** 这是 Reddit API 的硬上限（列表上限约 1000），README 直说：「我们绕不过去。」要做深历史归档你得换路子（比如 Pushshift 式数据转储，在其仍可用时）。
- **你想要一份忠实、可浏览的 Reddit 克隆。** `clone` 取的是原始数据，不是可导航的副本——没有渲染好的站点，评论树也不保证完整。
- **你不能 / 不愿注册 Reddit API 凭据。** 鉴权访问用 OAuth2；没有 API 应用，许多操作不可用。
- **你需要一个持续维护、频繁发版的工具。** 最后一个打标版本（v2.6.2）来自 2023 年初；提交还在继续，但发版节奏实质上停滞了——你可能在跑 `master` 而非某个加持过的版本（见健康度）。
- **位于 BDFR/yt-dlp 解析不了的站点的内容。** 它能处理 Imgur、Redgifs、相册、YouTube，以及「yt-dlp 支持的一切」，但某个不支持或刚改过的宿主，对那些链接就会直接失败。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [gallery-dl](gallery-dl.zh.md) | ✅ | 需要包含 Reddit 的广谱多站点媒体下载器时，选 gallery-dl。 | 面广的多站点媒体下载器（Reddit 只是其一）；跨网的*文件*下载很强，但在 Reddit 专属的元数据/评论归档和「下载/归档/克隆」三模式上更弱。 |
| redditdownloader（shadowmoose） | 未收录 | 需要另一个带网页 UI 的专用 Reddit 下载器时，选 redditdownloader。 | 另一个专用 Reddit 下载器，带网页 UI；对非 CLI 用户更友好，但 BDFR 可脚本化的 CLI + YAML 配置更适合自动化。[未验证] |
| Pushshift 转储 / PRAW 脚本 | 未收录 | 想绕开工具、直接用数据转储或 API 自建时，选 Pushshift 转储或 PRAW 脚本。 | 直接上数据转储或自己调 API，绕开工具和约 1000 上限（转储），但都得自己造——BDFR 帮你打包好了解析器、去重、命名和日志。 |
| [yt-dlp](yt-dlp.zh.md)（直接用） | ✅ | 只需要下载单个宿主媒体链接时，选 yt-dlp 直接调用。 | BDFR 底层*用* yt-dlp 处理宿主媒体；直接调 yt-dlp 对单条链接有效，但缺少 Reddit 来源枚举、元数据归档和去重。 |

## 技术栈

- **语言：** Python 3.9+。
- **Reddit 访问：** 官方 Reddit API 走 OAuth2（PRAW 式客户端），用于枚举帖子与元数据。
- **媒体解析：** 内置各站点解析器（Imgur、Redgifs、Reddit 相册/视频、Vidble、Erome……）外加 **yt-dlp** 作为通用回退。
- **输出：** 模板化文件命名、基于哈希的去重、结构化日志；用于可重复运行的 YAML 配置；三种模式（download / archive / clone）。

## 依赖

- **运行时：** Python 3.9+，经 `pip install bdfr` / pipx 安装（Arch 上有 AUR 包）。
- **凭据：** 一个 Reddit API 应用（OAuth2 客户端）用于鉴权访问。
- **打包的库：** yt-dlp 和各站点解析器代码；Reddit API 客户端。[推断]
- **无数据库 / 无服务**——它把文件和日志写到本地磁盘；状态就是磁盘上的输出 + 日志。

## 运维难度

**低。** 就是 `pip`/pipx 安装加一次性的 Reddit API 应用注册，然后一条 CLI 调用（或一个 cron 的 YAML 任务）。没有服务器、数据存储或队列要运维；增量日志让重跑便宜、近似幂等。现实摩擦在运维层面而非基建：要尊重约 1000 帖的上限、宿主一改时解析器偶有崩坏，以及你可能在跑未发布的 `master` 代码，所以保持更新并验证它仍能用是你自己的事。

## 健康度与可持续性

- **维护活跃度**：Grade E——最近 13 周中 0 周有提交；最后提交距今 1250 天。
- **响应速度**：无法计算——no_traffic。
- **采用广度**：Grade E——未记录 registry package/download 信号。
- **长青度**：Grade E——仓库已创建 2941 天。
- **治理集中度**：无法计算——unattributable。
- **许可风险**：Grade C——GPL-3.0 许可证。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 2.6k star，最后标签为 v2.6.2（2023-01）——数字对时间敏感；到 2026-04 的提交活动来自 API，但「在维护但不发版」是一个判断。
- [未验证] 确切的 Reddit API 客户端（PRAW 还是自定义 OAuth 客户端）与当前精确的解析器清单，是从 README 推断，本轮未对照清单核实。
- [推断] 多数操作需要 OAuth 凭据是 Reddit API 的标准姿态；具体哪些功能免鉴权可用，此处未验证。
- [推断] 对不支持/变动站点的逐宿主失败，是从「解析器 + yt-dlp」架构推断，并非实测枚举。
