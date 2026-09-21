---
name: FFmpeg
slug: ffmpeg
repo: https://github.com/FFmpeg/FFmpeg
category: transcoding-and-pipelines
tags: [video, audio, transcoding, codecs, muxing, filtering, multimedia, cli, libav]
language: C
license: LGPL-2.1-or-later
maturity: "active, LGPL-2.1+ core with optional GPL parts, ~61.5k stars (2026-06)"
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2026-06-29T11:25:33Z
  default_branch: master
  default_branch_sha: 3f6bf150cb018334809bec029325b28cff8a5a9a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:24:42Z
  overall: A
  overall_score: 4.0
  scored_axes: 3
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 5559
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 108
        top1_share: 0.207
        top3_share: 0.457
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: issues_disabled }
    adoption: { reason: ambiguous }
    risk_license: { reason: license_unparsed }
---

# FFmpeg

通用音视频框架——`ffmpeg`/`ffprobe`/`ffplay` 命令行工具，加上 `libav*` 系列库，几乎能解码、编码、转码、封装、解封装、滤镜处理世面上一切媒体格式。

![ffmpeg — 健康度雷达](../../../../assets/health/ffmpeg.zh.svg)

## 何时使用

你是后端工程师，要搭一条媒体管线：用户上传任意视频（手机拍的 H.264、一份 ProRes 母版、某个上古 AVI、一个 10-bit HEVC 文件），你需要产出可预期的网页可播放成品——MP4 里的 H.264/AAC，再加几条 HLS 码率档和一张缩略图。你不想去搞懂每种容器和编码的内部细节，只想要一个工具：吃进来的什么都认，吐出去的严格按你的规格。于是你 `ffmpeg -i input.mov -c:v libx264 -crf 22 -c:a aac -movflags +faststart out.mp4`，先用 `ffprobe -show_streams -of json` 探源以便按分辨率/编码/时长分支，需要归一化时再加 `-vf scale=1280:-2,fps=30`。要转封装（只换壳不重编）就用 `-c copy`，几乎不耗 CPU；要缩略图就 `-ss` 跳转抓一帧。抽音轨、烧字幕、拼接分段、生成 HLS/DASH、把裸帧 pipe 给另一个进程——同一个二进制全包了。

你也会把 FFmpeg 当库用，而不只是命令行：当你要把媒体处理嵌进应用里时，`libavformat`/`libavcodec`/`libavfilter`/`libswscale` 提供可编程的解封装/解码/滤镜/编码，不必为每个请求 fork 子进程。它是你已经在用的大半个媒体栈底下事实上的引擎（浏览器、播放器、NLE、云转码服务都建在它之上或挨着它），所以建在它上面，等于建在整个行业都依赖的那套格式覆盖面上。

## 何时不用

- **你要从流媒体站点下载。** FFmpeg 不是下载器。它能读 HTTP/HLS URL，但从 YouTube 之类抽取视频是 `youtube-dl` / `yt-dlp` 的活（URL 解析、清晰度选择、限速）。别拿 FFmpeg 去重造这套。
- **你要分发闭源专有二进制——先看清这个许可证陷阱。** 核心是 LGPL-2.1+，但你一旦用 GPL 编码器（x264、x265）构建，或传了 `--enable-gpl`，产出的二进制就变成 **GPL**；而 `--enable-nonfree` 会让它在法律上**不可再分发**。要做商业/闭源分发，你必须管住自己的构建 flag 和编码器集合（或单独获得编码器授权）。这是团队在 FFmpeg 许可证上最常踩的坑。[未验证]
- **你想要一套精简稳定的 API 和平缓的学习曲线。** 命令行的 flag 语法（流选择符、滤镜图、按流 `-c:v:0`）出了名地陡，C 库又是低层的，且大版本间 API 会变。要么预留真金白银的时间，要么把它包起来。
- **你要在大规模上解析不可信输入却不做沙箱。** FFmpeg 的解封装/解码器是一片用 C 写的、历史上 CVE 密集的攻击面；不加沙箱直接喂对抗性文件很危险。请隔离（seccomp/容器/独立进程）、锁版本、勤打补丁。
- **你只是想在 Python 里转几次码。** 别手拼 argv 字符串——用 [ffmpeg-python](https://github.com/kkroening/ffmpeg-python) 或 `PyAV` 在同一引擎上套个更清爽的接口。
- **你需要的是视频编辑器 / NLE。** FFmpeg 是变换引擎，不是时间线编辑器。要剪辑、多轨编辑、做特效，请用 NLE，或在它之上的框架如 MLT/Shotcut。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [GStreamer](gstreamer.zh.md) | ✅ | 需要面向实时流和应用内嵌媒体的管线/元件图框架时，选 GStreamer。 | 管线/元件图框架，面向实时流和应用内嵌媒体；做实时应用和设备管线时更可组合，但编程模型比“调一个命令行”重得多——而且它底层往往照样用 FFmpeg/libav。 |
| libav(avconv) | 未收录 | 只有在维护仍带 `avconv` 的旧系统时，才考虑 libav。 | 2011 年从 FFmpeg 分出的历史分叉；后来合并回去、基本已死。老发行版带 `avconv`；任何新工作都用 FFmpeg，别用 libav。 |
| [HandBrake](handbrake.zh.md) | ✅ | 需要面向终端用户的 GUI/CLI 转码应用时，选 HandBrake。 | 面向终端用户的转码应用（GUI + `HandBrakeCLI`），建在 FFmpeg/x264/x265 之上；预设驱动的“把这个转成 MP4/MKV”体验很好，但格式/滤镜面比裸 FFmpeg 窄得多，且不是库。 |
| [MLT](../editing-and-cutting/mlt.zh.md) / Shotcut | 部分已收录 | 需要带时间线模型的编辑/合成多媒体框架时，选 MLT/Shotcut。 | 带时间线模型、做编辑/合成的多媒体*框架*；真正的编解码活仍交给底下的 FFmpeg——当你要的是编辑器/NLE 而非转码器时才选它。 |
| AWS Elemental MediaConvert / 云转码 | 未收录 | 需要零运维、弹性伸缩且接受按分钟付费时，选云转码。 | 托管、按分钟计费的转码服务（内部常源自 FFmpeg）；零运维、弹性扩展，但有厂商锁定、按分钟成本，且是 SaaS——不是你能自托管的仓库。 |

## 技术栈

- **语言：** C（约 89%）加手写汇编（约 8%），用于编解码/缩放热路径的 SIMD 优化（x86/ARM 等）。
- **命令行：** `ffmpeg`（转码/封装/滤镜）、`ffprobe`（以文本/JSON 探查流与容器）、`ffplay`（基于 SDL 的测试播放器）。
- **库：** `libavformat`（封装/解封装 + 协议）、`libavcodec`（编/解码）、`libavfilter`（滤镜图）、`libavutil`、`libswscale`（缩放/像素格式转换）、`libswresample`（音频重采样）、`libavdevice`。
- **构建：** 自带的 `configure` 脚本（非 autoconf）+ `make`；编解码/特性集在构建时由 `--enable-*` / `--disable-*` flag 选定。

## 依赖

- **核心构建：** C 工具链、`make`、汇编器（x86 SIMD 需 `nasm`/`yasm`）。FFmpeg 自带的编解码器（原生解码器 + 内建编码器）不需要任何外部库。
- **可选外部编码器/库（构建时自选）:** `libx264` / `libx265`（H.264/HEVC——**GPL**，会把构建拉进 GPL）、`libvpx`(VP8/VP9)、`libaom`/`SVT-AV1`(AV1)、`libfdk-aac` / 原生 AAC、`libopus`、`libvorbis`、`libdav1d`、`libass`（字幕）、`zlib`/`openssl`（协议/TLS）。最终二进制的许可证取决于你链了其中哪些。
- **硬件加速（可选）:** NVENC/NVDEC(NVIDIA)、QSV(Intel Quick Sync)、VA-API、AMF、VideoToolbox(macOS)、V4L2 M2M——各自需要厂商驱动/SDK 在位，并通过 configure flag 启用。
- **安装路径：** 发行版包（常是裁剪过的 / LGPL 构建）、官方静态构建、Docker 镜像、源码。打包构建启用了哪些编码器随发行版/许可证政策而变。[未验证]

## 运维难度

**中。** 作为被服务调用的命令行，运维上很简单——静态二进制、无守护进程、无数据存储。真正的负担在别处：(1)**构建组合**——配好对的 `--enable-*` 集合、编码器和硬件后端，并让这份构建的许可证对你的分发干净；(2)**资源控制**——转码吃 CPU/GPU 和内存，你需要并发上限、超时和单任务配额，否则会把机器打满；(3)**输入加固**——不可信媒体应在锁定且已打补丁的版本里沙箱运行，因为解封装器有 CVE 攻击面；(4)**正确性排查**——音视频同步、像素格式、色彩/HDR 元数据、滤镜图顺序都很微妙，且同一条命令在不同 FFmpeg 大版本间行为可能不同。自托管这个二进制很容易；跑一支*安全、可预期、许可证干净*的转码集群才是那个“中等偏难”的部分。

## 健康度与可持续性

- **响应速度**：无法计算——issues_disabled。
- **维护——活跃且连续（最近一次 push 在 2026-06）。** 数十年不间断开发、规律发版；在任何媒体栈里都属于维护最稳定的项目之一 [未验证]。GitHub 镜像上约 3 个 open issue 反映的是上游跟踪走它自己的邮件列表/bug tracker，而非项目闲置。
- **治理与 bus factor——成熟而广泛的社区。** `Org` 所有（`FFmpeg/`）——一个长期存在的多贡献者项目，既非单人维护，也非某个厂商的单一路线图；其 bus factor 风险之低，几乎是开源能给到的下限 [推断]。（注意历史上 2011 年的 libav 分叉，后来合并回去、归于无关——FFmpeg 是存活下来的那条线。）
- **年龄与 Lindy 判断——老且仍活跃 ⇒ 能给到的最强 Lindy 押注。** 2011 年上 GitHub（源头可追到约 2000 年），2026 年仍在发版，且是大半个媒体栈（浏览器、播放器、NLE、云转码）底下事实上的引擎。这是媒体类里最稳的寿命押注——建在它上面，等于建在整个行业都依赖的东西上。
- **风险标记——陷阱在许可证，而非可持续性。** LGPL-2.1+ 核心，但 `--enable-gpl`（x264/x265）会让构建变 GPL，`--enable-nonfree` 会让它**不可再分发**：对闭源分发是个承重 flag，你必须在构建期管住 [未验证]。此外还有一片大、历史上 CVE 密集的 C 解析器攻击面——不可信输入的管线请沙箱化并打补丁。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 61.5k GitHub star、状态“活跃”;README 称代码库“主要为 LGPL 许可，可选组件为 GPL 许可”。star 数对时间敏感，仅供参考。
- [未验证] **许可证条件（承重）:** 核心文件为 LGPL-2.1-or-later；可选 GPL 部分（含部分 x86 优化和 libavfilter 里 30+ 个滤镜）需显式传 `--enable-gpl`，这会让构建变 GPL-2.0+。链接 x264/x265 等 GPL 外部库同样强制 GPL。`--enable-nonfree` 允许引入本不兼容的库（如某些编码器）但会让产出二进制**不可再分发**;`--enable-version3` 升到 (L)GPL v3。分发前请对照 `LICENSE.md` 核实确切组件清单。
- [推断] 语言占比（C 约 89%、汇编约 8%）是 GitHub linguist 的统计，会随时间变化，视为近似值。
- [推断] CVE/安全的说法源自 FFmpeg 作为大型 C 不可信二进制格式解析器的历史，是对攻击面的推断，而非针对某个当前具体漏洞的断言。
- [推断] *打包*（发行版/静态）构建启用了哪些编码器、因而其有效许可证如何，随来源而变；请核实你实际分发的那份构建，别假设等于上游默认。
