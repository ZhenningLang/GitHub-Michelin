---
name: HandBrake
slug: handbrake
repo: https://github.com/HandBrake/HandBrake
category: video-audio
tags: [video, transcoding, h264, h265, gui, cli, dvd, bluray, ffmpeg]
language: C
license: GPL-2.0-or-later
maturity: v1.9.x, active, ~21k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-05T13:10:33Z
  default_branch: master
  default_branch_sha: e02d1e31a9f09bdd61b2555b2e88cfb68c670231
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:38:52Z
  overall: A
  overall_score: 4.0
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 10.9
        qualifying_issues: 44
        band: relaxed_solo
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 4620
        homebrew_tier: A
        release_downloads: 59336263
        release_assets: 968
        release_tier: A
        signal_basis: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 4049
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 28
        top1_share: 0.385
        top3_share: 0.71
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# HandBrake


开源视频转码器，用于将几乎任意格式的视频转换为现代广泛支持的编解码器——基于 FFmpeg、x264 和 x265 构建，带有预设驱动的 GUI 和配套的 `HandBrakeCLI` 命令行工具。


![HandBrake — health radar](../../../assets/health/handbrake.zh.svg)

## 何时使用

你是一位媒体归档员，手头有一堆 DVD 和蓝光需要转换成现代压缩格式的库。你想要一个能处理整个工作流的工具——源扫描、标题选择、字幕/音轨挑选，并输出为标准 MP4 或 MKV 文件，带 H.264/H.265 视频和 AAC/AC3 音频。你不想手工编写 FFmpeg 命令行或写 shell 脚本。你启动 HandBrake，选一个预设（如“Fast 1080p30”“HQ 2160p60 4K”），有需要时调几个参数，然后把一批源文件排队处理。内置 GUI 提供输出设置的实时预览，而批量作业时你可以切换到 `HandBrakeCLI`，用同样的预设做无头脚本化转码。HandBrake 的优势在于：当你需要将光盘或文件源可靠、可重复地转码为少量现代输出配置时，无需动用原始 FFmpeg 的全部格式灵活性。

## 何时不用

- **你需要一个可嵌入应用的可编程库。** HandBrake 是终端用户应用，不是库。请改用 FFmpeg 的 `libav*` 或 GStreamer 的流水线 API。
- **你需要复杂的滤镜图或自定义像素/音频处理。** HandBrake 的滤镜面刻意保持精简——去隔行、降噪、裁切/缩放、字幕烧录——远不及 FFmpeg 的 `-vf`/`-af` 滤镜图语言。
- **你需要超出 MP4/MKV/WebM 配合 H.264/H.265/AV1/VP9 和 AAC/AC3/FLAC/Opus 的格式灵活性。** HandBrake 对输出格式有明确偏好，不会像 FFmpeg 那样输出 ProRes、MPEG-2 或原始 YUV。
- **你需要实时流或广播管线的实时编码。** HandBrake 是文件到文件，不支持流媒体、自适应码率阶梯或低延迟管线。
- **你发行闭源专有二进制。** HandBrake 采用 GPL-2.0-or-later 并链接 GPL 编码器（x264、x265）。[推断]
- **你需要带时间线、剪辑、转场和多轨合成的视频编辑器。** HandBrake 转码的是完整标题，不编辑。请改用 MLT/Shotcut 或 NLE。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FFmpeg](ffmpeg.zh.md) | ✅ | 需要万能编解码器/格式瑞士军刀、库嵌入或自定义滤镜图时，选 FFmpeg。 | 万能编解码器/格式瑞士军刀，拥有无限的滤镜图和库嵌入能力；学习曲线陡峭得多，且没有内置 GUI，但你能控制每个参数。 |
| [MLT](mlt.zh.md) / Shotcut | 部分已收录 | 需要基于时间线的非线性视频编辑器或合成框架时，选 MLT/Shotcut。 | 基于时间线的 NLE/合成框架；实际编解码工作仍由 FFmpeg 完成。需要剪辑而非单纯转码时用它。 |
| [GStreamer](gstreamer.zh.md) | ✅ | 需要可组合流水线框架用于应用嵌入或直播流媒体时，选 GStreamer。 | 可组合流水线框架，用于应用嵌入或直播流媒体；编程模型更陡峭，但比起文件到文件转码器，在实时和设备管线方面更灵活。 |
| AWS Elemental MediaConvert / 云转码 | 未收录 | 需要弹性、托管、按分钟计费的转码且不想承担运维负担时，选云转码。 | 托管的按分钟计费转码服务；零运维、弹性伸缩，但有厂商锁定、按分钟成本，且是 SaaS——不是你可自托管的仓库。 |
| VLC | 未收录 | 需要带少量转换功能的媒体播放器，而非专用转码器时，选 VLC。 | 主要是媒体播放器；其转换/导出功能只是配菜，不是主菜。用于偶尔的一次性导出，而非批量归档工作流。 |

## 技术栈

- **语言：** C（核心引擎），配合平台特定的 GUI 工具包（Linux 用 GTK，macOS 用 Cocoa，Windows 用 UWP/WPF）。
- **核心编码器：** FFmpeg/libavcodec（解码），x264（H.264），x265（H.265），SVT-AV1（AV1），VP9，Theora。
- **封装器：** 通过 libavformat 输出 MP4、MKV、WebM。
- **滤镜：** 内置去隔行、降噪、裁切、缩放、旋转和字幕烧录——是 FFmpeg 滤镜图能力的一个子集，通过简化 UI 暴露。
- **光学介质：** libdvdread/libdvdnav（DVD），libbluray（蓝光），可选 libdvdcss 处理 CSS 加密光盘。

## 依赖

- **运行时：** FFmpeg 库（libavcodec、libavformat、libavfilter、libswscale、libavutil），x264/x265/SVT-AV1 编码器库，libdvdread/libdvdnav/libbluray 用于光学介质。
- **可选：** libdvdcss 用于解密 CSS 保护 DVD（某些司法管辖区可能有法律限制）。
- **构建：** 基于 autotools/cmake 的构建系统；从同一源码树构建 GUI 和 `HandBrakeCLI`。
- **平台支持：** Windows、macOS、Linux。三个平台均提供官方二进制分发。

## 运维难度

**低。** HandBrake 是桌面应用：下载、安装、运行。无需配置服务器、无需管理数据库、无需守护进程。对于 CLI 批量工作流，`HandBrakeCLI` 是单一二进制，接收预设 JSON 文件或命令行标志。主要运维关注点是跟进版本更新以获取编码器改进和安全修复；没有网络服务或持久状态需要备份。

## 健康度与可持续性

- **维护：** 活跃，定期发布（截至 2026-07 为 v1.9.x）。项目自 2003 年起持续维护。[推断]
- **治理：** 社区驱动，无单一厂商或基金会支持。核心团队约 3–5 名维护者。[推断]
- **支持：** 无大型企业支持；依靠社区贡献和捐赠维持。[推断]
- **采用：** 广泛用于 DVD/蓝光归档和个人媒体转换。GitHub 约 21k stars。[推断]
- **风险标志：** GPL-2.0+ 许可证已确立。无重新授权历史。无显著近期 CVE。[推断]

## 存疑（未验证）

- [未验证] 活跃核心维护者的确切人数未从公开来源确认。
- [推断] HandBrake 链接 GPL 许可编码器（x264、x265），因此任何衍生二进制分发均受 GPL 约束。
- [推断] 项目自 2003 年起持续维护，但治理模式为志愿者驱动，无基金会支持。
