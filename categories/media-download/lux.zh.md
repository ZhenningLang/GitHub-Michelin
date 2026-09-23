---
name: lux
slug: lux
repo: https://github.com/iawia002/lux
category: media-download
tags: [video-download, bilibili, douyin, cli, go, downloader, single-binary]
language: Go
license: MIT
maturity: "active-but-slowing, master pushed ~2026-03, last tagged release v0.24.1 (2024-05), ~31.4k stars (2026-06)"
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-03-29T18:18:56Z
  default_branch: master
  default_branch_sha: dd00f6d258d80b6684a0b9402d7124e5c18ef42f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:35:27Z
  overall: B
  overall_score: 2.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 267
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 249
        homebrew_tier: C
        release_downloads: 560461
        release_assets: 1248
        release_tier: C
        signal_basis: homebrew+releases
    longevity:
      grade: C
      raw:
        repo_age_days: 3132
        last_commit_age_days: 267
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.333
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# lux

一个快速、简单的 Go 视频下载库 + CLI（原名 *annie*）——单个静态二进制，对中文站点（Bilibili、抖音等）覆盖很强，并支持多段并行下载。

![lux — 健康度雷达](../../assets/health/lux.zh.svg)

## 何时使用

你正在搭一台入库机、或给同事的笔记本配环境，想要一个*单文件*的视频下载器——没有 Python 解释器、不用 `pip install`、不用在多台机器间操心虚拟环境漂移。你把单个静态 `lux` 二进制丢到 PATH 上，指向一个 URL，它就帮你解析格式、并行下载分段、写出文件。因为它是 Go 二进制，能干净地交叉编译，塞进精简容器或 CI runner 时不必拖着语言运行时——当下载这一步只是更大流水线里的一个节点、你又不想伺候 Python 环境时，这正是你要的。

当来源是**中文站点**时你尤其会选它——Bilibili、抖音以及类似的站点，lux 历来在这些站点上的 extractor 比那些以西方站点为中心的工具更锋利、维护得更好。你在归档一个 Bilibili 系列、或拉抖音短片，想要多线程分段下载提速，也想要同一个二进制无论交互调用还是脚本调用都行为一致。

## 何时不用

- **你需要尽可能宽的站点覆盖和最新的 extractor。** 这是决定性的筛子。lux 支持的站点目录比 yt-dlp **更小**，extractor 修复的节奏也更慢——当某站点改了播放器或签名逻辑，通常是 yt-dlp 先被打补丁。论广度（尤其是 YouTube），默认用 yt-dlp / [youtube-dl](youtube-dl.zh.md)，把 lux 当作「中文站点 + 单二进制」的专才。[推断]
- **你押注的是长期、快周转的维护。** 贡献高度集中在单一维护者（iawia002）手上，最后一个*打 tag* 的发布（v0.24.1）来自 2024-05，尽管 master 仍有提交——一旦某个被大量使用的站点崩了而修复迟迟不到，这就是 bus-factor 和节奏风险。要给「崩→修」的循环留预算。
- **你想要一个转码器或后处理工具箱。** lux 能下载、也能合并分段，但它不是编码器——合并和任何重编码/格式转换都靠调用 **FFmpeg**。如果你真正的需求是转码，直接上 FFmpeg；lux 是「取」这一步，不是媒体处理那一步。
- **重 JS / DRM / 登录墙、且没有 extractor 的来源。** 和同类一样，它不跑浏览器，也不破解 Widevine/PlayReady、不解 CAPTCHA、不为对抗限流轮换身份。没有现成 extractor 的站点只会直接失败。
- **法律 / ToS 暴露。** 下载受版权保护的媒体、或违反站点服务条款，责任在你；很多目标站点禁止下载。在没核对法律和 ToS 前，别拿它做产品底座。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [youtube-dl](youtube-dl.zh.md) | ✅ | 需要拥有最大遗留 extractor 目录的 Python CLI 时，选 youtube-dl。 | Python CLI，拥有最大的遗留 extractor 目录（约 1000 站点）；西方站点覆盖更广，但需要 Python 运行时，且其上游 tag 落后（yt-dlp 才是活跃路径）。lux 用「广度」换来「单 Go 二进制 + 更强中文站点支持」。 |
| [yt-dlp](yt-dlp.zh.md) | ✅ | 需要事实上最活跃、覆盖最广的下载器时，选 yt-dlp。 | 事实上最活跃的下载器；extractor 覆盖最广、修复最快，基于 Python。当广度/时效比「交付单个静态二进制」更重要时选它。 |
| [you-get](you-get.zh.md) | ✅ | 需要同样擅长中文站点的 Python 下载器时，选 you-get。 | 同样在中文站点（Bilibili 等）上很强的 Python 下载器；与 lux 同一生态位，但用的是 Python 运行时而非 Go 二进制，且有自己另行维护的站点列表。 |
| [cobalt](cobalt.zh.md) | ✅ | 需要 Web/API 优先、可自托管的下载服务时，选 cobalt。 | 以 Web/API 为先、可自托管的*服务*；浏览器友好、UX 干净，但它是一个要跑的服务器，而非你能丢进脚本的单个 CLI 二进制。 |

## 技术栈

- **语言：** Go——编译成单个静态二进制；既可作 CLI，也可作为可 import 的库（`github.com/iawia002/lux`）。[未验证]
- **架构：** 一个核心下载器 + 按站点划分的 **extractor** 包；其上叠加多线程/多分段下载与进度展示。
- **后处理：** 调用 **FFmpeg** 合并分段流、做格式转换——lux 自身不转码。
- **分发：** 各 OS/arch 的预编译二进制（GitHub releases），外加 `go install` 和常见包管理器。

## 依赖

- **运行时：** 跑下载只硬性需要那个 Go 二进制。无服务、无数据库、无守护进程。
- **FFmpeg（可选但常需）：** 把多分段下载合并成一个文件、以及格式转换都需要它；大多数「给我一个 MP4」的工作流要在 PATH 上装它。[未验证]
- **网络：** 到目标站点的出站 HTTP(S)；支持 cookie 和代理，用于登录受限或地区受限内容。
- **没有后端要跑：** 执行完即退出——没东西要托管。

## 运维难度

**跑起来低；维护风险在上游，而非运维上。** 部署极简——拷一个静态二进制，可选地把 FFmpeg 放进 PATH，完事；无运行时、无基础设施，容器化也干净。真正的代价是每个下载器都有的那种脆弱：当某个受支持站点改了内部逻辑，过时的 lux 会悄悄报错或返回错误格式，而 lux 较慢的 extractor 节奏加上单维护者 bus factor，意味着某个小众站点的修复可能拖延。一次性、以中文站点为主的任务无所谓；但若要在很多站点上做硬覆盖，请把它和（或退回到）一个更快迭代的工具搭配使用。

## 健康度与可持续性

- **响应速度**：无法计算——unknown。
- **维护——活跃但放缓；发布落后于 master（master 约 2026-03 push，最后一个打 tag 的发布 v0.24.1 在 2024-05，截至 2026-06）。** 未归档、默认分支仍有提交，但面对一个移动的目标（站点改播放器），距上一个 tag 发布约 2 年的落差正是要盯的信号：在依赖它覆盖很多站点前，先核实它是真活跃还是在吃老本。[推断]
- **治理与 bus factor——单维护者的 `User` 仓库（iawia002）。** 归属一个个人账号，而非组织或基金会，贡献高度集中在 owner（iawia002 约 497 次，紧随其后者约 14 次）。这是实打实的 bus-factor 标记：路线图和 extractor 维护在很大程度上系于一人。[推断]
- **年龄与 Lindy——创建于 2018 年（约 8 岁），约 31.4k star：年龄和采用度都不错。** 一个多年、仍在收提交的项目跨过了基本的 Lindy 门槛——这个*点子*和代码库已经存续（它早于 *annie* 改名）。但对下载器而言，耐久风险不在年龄，而在 **extractor 过时/节奏**：老且活跃对核心是宽慰，但不保证任意某个站点今天还能下。
- **风险标记——MIT，无 relicense 历史。** 宽松许可，未见 copyleft/relicense 摩擦。当前风险就是上面那个节奏/bus-factor，以及下载本身普遍的法律/ToS 暴露。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 31.4k GitHub star;star 数对时间敏感，仅供参考。
- [未验证] master 最近一次 push 约 2026-03，最后一个打 tag 的发布是 v0.24.1（2024-05），依据仓库的 releases;tag 与 master 的落差是关键维护信号——依赖前请重新确认当前提交活跃度、以及是否有更新的发布。
- [推断]「站点覆盖比 yt-dlp 更小、extractor 更新更慢」是普遍认知，并非此处核过的计数；决策时请查当前支持站点列表和近期 extractor 提交。
- [推断] 单维护者/bus-factor 判断由 `User` 所有的仓库和贡献集中度数据（iawia002 约 497 vs 次位约 14）推断而来；若此点至关重要，请重新核对贡献者图谱。
- [未验证] 合并/转换需 FFmpeg、以及并行多分段下载的说法来自项目文档；若任一点至关重要，请对照当前 README 并自行跑一遍确认。
- [推断] License 为 MIT 依据仓库元数据；若 license 条款对你的用途至关重要，请确认 LICENSE 文件。
