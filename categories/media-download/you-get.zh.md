---
name: you-get
slug: you-get
repo: https://github.com/soimort/you-get
category: media-download
tags: [video-download, media, cli, downloader, python, bilibili, youku, youtube]
language: Python
license: MIT
maturity: "active, latest release v0.4.1743 (2025-01-04), ~56.8k stars (2026-06)"
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-04-30T05:24:16Z
  default_branch: develop
  default_branch_sha: 049548f3f3f35e67ba8d3181c71fdc71d11cf260
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:35:56Z
  overall: D
  overall_score: 1.33
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: D
      raw:
        archived: false
        last_commit_age_days: 513
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: you-get
        dependent_repos_count: 125
        downloads_last_month: 17280
        graph_tier: C
        volume_tier: D
        cross_check_divergence: null
        homebrew_installs_90d: 156
        homebrew_tier: C
        release_downloads: 405099
        release_assets: 394
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 5146
        last_commit_age_days: 513
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: issues_disabled }
    governance: { reason: unattributable }
    risk_license: { reason: license_unparsed }
---

# you-get

一个小巧的命令行程序，从 YouTube 及 100+ 个其他站点下载媒体（视频、音频、图片）；对中文视频站（Bilibili、Youku、iQIYI、腾讯视频……）的覆盖尤为出色。

![you-get — 健康度雷达](../../assets/health/you-get.zh.svg)

## 何时使用

你是做中文内容的研究者或归档者，要把 Bilibili 上的课程录像、Youku 上的几段片子，外加偶尔一个 iQIYI 或腾讯视频页面拉到本地离线看。那些主流的西方工具，要么没有针对这些站点的最新 extractor，要么把它们当二等公民对待；而你又不想为了一次性抓取去伺候一个重型下载器。于是你选 `you-get`：`pip install you-get`，然后 `you-get <url>` 列出可用的流，`you-get --itag=... <url>`（或直接默认）就抓下最佳那条。你用 `-i` 只看格式不下载、用 `-o` 指定输出目录、用 `--playlist` 拉整个列表。只有当分段需要合并时它才调 `ffmpeg`，所以从单个 URL 拿一个 MP4，除了解释器之外几乎不需要别的。

当你想要对某个中文站点*今天就能用*的最小那个东西时，你也会选它——它的吸引力在于一个紧凑的 CLI 加一份精选站点列表，而不是 youtube-dl/yt-dlp 那套穷举式的约 1000 个 extractor 目录。你把一个 URL 丢给它，它就把该站点的流布局归一化成统一的“列格式→挑选→下载”流程；而且因为它是纯 Python、没有需要常驻托管的东西，它能直接嵌进脚本或手动会话，不必先搭任何基础设施。

## 何时不用

- **你要的是最大的站点广度，或最快的 YouTube 修复。** 这是决定性的筛子。论 extractor 数量之多、以及 YouTube 改播放器/签名逻辑后修复之快，**yt-dlp**（其次是 [youtube-dl](youtube-dl.zh.md)）领先；you-get 精选而更小的目录、更慢的节奏，意味着某个非中文站点可能不被支持或会落后。要广度和 YouTube 关键任务，默认用 yt-dlp。[推断]
- **你想要保证分秒最新的维护。** 最新的打 tag 发布是 2025-01-04，提交节奏比 yt-dlp 轻；某个刚改了布局的站点，可能要等有人补 extractor 才能恢复。站点失效是这一类工具共同的失败模式，但 you-get 更小的维护者池会放大这个落差。[推断]
- **你需要转码 / 重编码。** you-get 负责下载并（通过 `ffmpeg`）*合并*分段；它不是转码器。若要重编码、换 codec 或做滤镜，那是直接用 **FFmpeg**——you-get 只负责编排抓取。
- **重 JS / DRM 锁、且没有 extractor 的站点。** 它不驱动浏览器，也不执行任意页面 JavaScript;Widevine/PlayReady DRM、逐请求 token 机制，或没有现成 extractor 的 SPA 站点，只会直接失败。
- **大规模下的地区限制、登录墙或抓取。** 它能传代理和 cookie，但不会帮你解 CAPTCHA、轮换身份或挡 IP 封禁；用单个 IP 批量下载会被限速。你抓取的媒体的法律 / ToS 风险是你的问题，不是工具的。
- **你想要一个稳定的库 API。** 它主要是 CLI;import 内部模块不受支持，会无预告变动。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [youtube-dl](youtube-dl.zh.md) | ✅ | 需要经典、覆盖很广的 Python extractor 目录，且能接受上游节奏放缓时，选 youtube-dl。 | 经典的 Python 下载器，约 1000 个站点的 extractor 目录；站点覆盖广得多，但维护放缓，且在部分中文站上历来比 you-get 更弱/更不及时。 |
| [yt-dlp](yt-dlp.zh.md) | ✅ | 要广度和 YouTube 关键任务的新鲜度，而不是 you-get 的小体积时，选 yt-dlp。 | 活跃维护的 youtube-dl 分叉；目录最广、YouTube 修复最快，选项更多（SponsorBlock、格式排序、aria2c）。要广度和 YouTube 关键任务选它；you-get 仍因体积小、聚焦中文站而有吸引力。 |
| [lux](lux.zh.md) | ✅ | Go 单二进制和自带中国站点目录比 Python 包装更重要时，选 lux。 | Go 写的单二进制下载器（原名 annie），自带对中国友好的站点列表；无需 Python 运行时、速度快，但目录更窄、收录取向不同。 |
| [cobalt](cobalt.zh.md) | ✅ | 想要自托管 Web/API 下载服务，而不是脚本型 CLI 时，选 cobalt。 | 以 Web/API 为先的下载器（可自托管的服务）；浏览器 UX 干净，但它是一个要跑的服务，而非可 pip 安装、便于脚本化的 CLI。 |

## 技术栈

- **语言：** Python（README 声称 Python 3.7.4+，更老的 3.5/3.6/3.7 支持正被逐步淘汰）。[未验证]
- **架构：** 一个核心下载器 + 按站点划分的 **extractor** 模块（`you_get.extractors.*`）；每个 extractor 把某个站点的流发现归一化成统一接口。
- **后处理：** 调用 `ffmpeg`（≥1.0）合并/拼接多段流；可选 `rtmpdump` 处理 RTMP 源。you-get 本身不转码。
- **分发：** PyPI 包（`you-get`）、一个自包含脚本，以及各 OS 包管理器构建。

## 依赖

- **运行时：** 抓取单文件流只硬性需要一个 Python 解释器。无服务、无数据库、无守护进程。
- **可选二进制（你自己装）：** `ffmpeg`（≥1.0）——只要下载到的是需要合并的多段流就需要它，这相当常见；`rtmpdump` 处理 RTMP 流。
- **网络：** 到目标站点的出站 HTTP(S)；登录受限内容可选配代理（`-x` / `--http-proxy`、SOCKS）和 cookie 文件。
- **没有后端要跑：** 它执行完就退出——没东西要托管。

## 运维难度

**跑起来低，维持“还能用”的脆弱度中等。** 安装和调用都极简单：`pip install you-get`、一条命令、完事——零基础设施，PATH 上有 `ffmpeg` 就能覆盖合并场景。持续成本和这一类下载器一样：目标站点改流布局，过时的 extractor 就会悄悄开始报错或返回错误格式。you-get 相对 yt-dlp 更轻的维护节奏，意味着某个刚崩的站点的修复可能拖后，所以实际的维护活是保持最新（`pip install -U you-get`，或跟 master），并随时准备为当前崩掉的站点回退到别的工具。一次性和中文站抓取很舒服；但面向多站点的长期流水线，要给“崩→修”的循环留预算。

## 健康度与可持续性

- **响应速度**：无法计算——issues_disabled。
- **维护——缓慢但未死（最近一次 push 约 2026-04，最后一个打 tag 的发布是 2025-01-04，截至 2026-06）。** 未归档；master 分支仍有提交，但打 tag 发布的节奏很轻、落后于 yt-dlp。对抽取器工具来说这正是现实风险——刚崩的站点可能要等补丁 [推断]。跟 master，别钉死旧 tag。
- **治理与 bus factor——单人维护风险。** `User` 所有（`soimort/you-get`），约 56k star：庞大的采用压在一个很小/单人的维护者池上，这既解释了更慢的节奏，本身也是 bus factor 风险。背后没有基金会或厂商 [推断]。
- **年龄与 Lindy 判断——老且仍在动 ⇒ 中等 Lindy。** 创建于 2012 年（约 14 岁），2026 年仍在提交：长期存活是实打实的正面信号，但这里的「仍活跃」很*单薄*（发版慢、维护者池轻），所以是中等而非强 Lindy 押注——比废弃工具稳，比快速迭代的 yt-dlp 弱。
- **风险标记。** MIT 许可，无 relicense/开放核心顾虑。长期风险是运维性而非法律性的：非中文站点的抽取器过时，以及下载本身的法律/ToS 暴露。它的差异化价值（中文站覆盖强）也正是它的小生境——广度关键的任务默认用 yt-dlp。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 56.8k GitHub star;star 数对时间敏感且不可靠——仅供参考。
- [未验证] 最新发布是 v0.4.1743，日期 2025-01-04（依据仓库）；"active" 反映已发布的版本和仓库的持续存在——决策时请重新确认当前提交/推送活跃度，其节奏比 yt-dlp 轻。
- [未验证] License 为 MIT——仓库的 `LICENSE.txt` 是标准 MIT 协议文本（GitHub 界面可能因其分类器显示 "NOASSERTION"；文件本身是 MIT）。若 license 条款对你的用途至关重要，请确认 LICENSE 文件。
- [未验证] README 声称的 Python 支持范围（3.7.4+，更老版本正被淘汰）和受支持站点列表随时间变化；请对照当前仓库和 `you-get` 的 extractor 列表核实。
- [推断] “在中文站上比 youtube-dl 强”和“目录比 yt-dlp 更小、维护更不积极”是社区普遍看法，此处未实测——决策时请就你需要的具体站点重新确认。
- [推断] `ffmpeg` 专门用于合并分段流；某次下载是否触发合并取决于站点/格式——请就你的目标站点核实。
