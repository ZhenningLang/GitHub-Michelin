---
name: MLT
slug: mlt
repo: https://github.com/mltframework/mlt
category: editing-and-cutting
tags: [video, editing, nle, timeline, compositing, c++, ffmpeg, kdenlive, shotcut]
language: C++
license: LGPL-2.1-or-later
maturity: v7.30.x, active, ~1.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-03T22:11:16Z
  default_branch: master
  default_branch_sha: 76be5018b717d353459db4258093aff8c7d1ec7a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:48:09Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.0
        qualifying_issues: 7
        band: default
        window_offset_days: 10
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 577
        homebrew_tier: B
        release_downloads: 586031
        release_assets: 40
        release_tier: C
        signal_basis: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 5275
        last_commit_age_days: 1
        cohort: framework
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 23
        top1_share: 0.614
        top3_share: 0.846
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: C
      raw:
        spdx_id: LGPL-2.1
        permissiveness: weak_file_copyleft
        relicense_36mo: false
        content_license: null
---

# MLT


用于构建非线性视频编辑器（NLE）的多媒体框架——支持时间线轨道、片段、转场、滤镜与合成，底层实际的编解码工作全部委托给 FFmpeg/libav 完成。它不是独立的剪辑软件，而是 Shotcut 和 Kdenlive 的底层引擎。

![mlt — 健康度雷达](../../../../assets/health/mlt.zh.svg)


![MLT — health radar](../../../../assets/health/mlt.zh.svg)

## 何时使用

你正在构建一款需要时间线的视频应用：面向小众工作流的定制 NLE、按规则自动组装片段的自动化剪辑管线，或一台负责拼接与渲染序列的无头服务器。你不想从零手写时间线模型、转场引擎或滤镜图，而是想要一个已经理解轨道、片段、入出点、混音器与合成的 C++ 框架。你把项目建模成 XML 时间线，加载进 MLT，它负责逐帧精度的底层 plumbing：通过 FFmpeg 解码、应用滤镜、混合转场、编码输出。你也可以通过 C++ 或绑定接口以编程方式驱动它，在上方搭建编辑器 UI，由 MLT 处理媒体后端。如果你需要开箱即用的剪辑软件，可以直接用 Shotcut 或 Kdenlive（两者都基于 MLT）；但当你需要嵌入或扩展引擎本身时，MLT 才是该拿的层。

## 何时不用

- **你需要一个开箱即用的视频剪辑软件。** MLT 是框架，不是应用。如果你想打开就能剪辑，直接用 Shotcut、Kdenlive 或其他 NLE，而不是直接使用 MLT。
- **你只需要批量转码或格式转换。** MLT 会增加你根本不需要的时间线复杂度。对于纯解码/编码/转码，直接用 [FFmpeg](../transcoding-and-pipelines/ffmpeg.zh.md)——它更快、更简单，社区支持也广得多。
- **你需要实时流处理或持久化媒体管线。** MLT 面向离线/顺序时间线渲染，而非实时流处理。实时管线请考虑 GStreamer。
- **你想要一个原生 Python、友好的视频编辑 API。** MLT 的主要接口是 C++ 加 XML 项目描述。如果以 Python 优先的编程化剪辑为目标，考虑 MoviePy 或 PyAV。
- **你在构建专有闭源产品，需要对 LGPL 链接边界有绝对把握。** MLT 采用 LGPL-2.1+；虽然以库形式链接通常被 LGPL 允许，但动态链接与静态链接的边界以及插件-滤镜组合必须针对你的具体分发模式进行审查。若许可纯净度是硬约束，请先与法务核实。 [未验证]
- **你需要庞大的社区、丰富的教程或快速的问题响应。** MLT 的社区比 FFmpeg 更小、更垂直；排错可能需要读源码或翻邮件列表。 [推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FFmpeg](../transcoding-and-pipelines/ffmpeg.zh.md) | ✅ | 用 FFmpeg 做原始解码/编码/转码/滤镜管线；用 MLT 当需要在其之上叠加时间线语义时。 | 通用媒体瑞士军刀；API 陡峭，且有 LGPL/GPL 构建授权陷阱。MLT 坐在它之上，提供编辑级时间线语义。 |
| [GStreamer](../transcoding-and-pipelines/gstreamer.zh.md) | ✅ | 用 GStreamer 做实时、持久化、嵌入应用的管线；用 MLT 做离线时间线式剪辑/合成。 | 面向实时/流媒体与嵌入应用的管线/元件图框架；编程模型更重，但实时场景更灵活。 |
| [HandBrake](../transcoding-and-pipelines/handbrake.zh.md) | ✅ | 用 HandBrake 做终端用户预设驱动转码；用 MLT 做程序化时间线编辑。 | 预设驱动的 GUI 与 CLI，用于翻录/转码为现代 MP4/MKV；终端用户应用，不是库，远比原生 FFmpeg 窄。 |
| [MoviePy](moviepy.zh.md) | ✅ | 用 MoviePy 做友好的 Python API 批量视频编辑；用 MLT 做需要编辑精度的 C++ 时间线框架。 | 友好的 Python API 用于程序化视频编辑——剪辑、合成、文字、特效——但纯离线批处理，对大文件比原生 FFmpeg 慢。 |
| [PyAV](../transcoding-and-pipelines/pyav.zh.md) | ✅ | 用 PyAV 做 Pythonic 的 FFmpeg 绑定；用 MLT 做时间线模型与编辑语义。 | Pythonic 绑定到 FFmpeg 的 libav*；给你 Python 里的编解码级控制，但无时间线或 NLE 抽象。 |
| Shotcut | 未收录 | Shotcut 基于 MLT 构建。需要开箱即用的开源 NLE 时选 Shotcut；需要嵌入或扩展引擎时直接用 MLT。 | 基于 MLT 构建的开源 NLE；需要编辑器而非框架时选它。 |
| Kdenlive | 未收录 | Kdenlive 基于 MLT 构建。需要 KDE 集成 NLE 时选 Kdenlive；需要引擎时直接用 MLT。 | 另一款基于 MLT 构建的开源 NLE；KDE/Qt 集成，某些方面功能比 Shotcut 多，但仍是应用而非库。 |
| DaVinci Resolve | 未收录 | 用 DaVinci Resolve 做专业级调色、特效与剪辑——它是商业 NLE，不是开源框架。 | 专业商业 NLE，带世界级调色；有免费版但非开源，也不能作为库嵌入。 |
| Premiere Pro | 未收录 | 用 Premiere Pro 做 Adobe 生态专业剪辑；作为可嵌入的开源框架，它不具备可比性。 | 商业 Adobe NLE；仅订阅制、闭源，属于 Creative Cloud 工作流的一环。 |
| OpenTimelineIO | 未收录 | 用 OpenTimelineIO 做应用间时间线交换（Adobe 格式）；用 MLT 做实际渲染与播放引擎。 | Adobe 主导的时间线交换格式——解决「从 A 软件导出时间线到 B 软件」，而非渲染或播放本身。 |

## 技术栈

- **语言：** C++（核心框架），带 C 绑定及部分语言封装器。
- **编解码引擎：** FFmpeg/libav——MLT 把所有实际的解码/编码/封装/滤镜工作都委托给 FFmpeg 的库（`libavformat`、`libavcodec`、`libavfilter` 等）。
- **时间线模型：** 基于 XML 的项目格式，描述轨道、片段（producer）、转场以及可链式挂载在片段/轨道上的滤镜（property）。
- **模块/插件：** producer、filter、transition、consumer 的插件系统——自带 FFmpeg、SDL、OpenGL 等后端。
- **构建：** CMake 构建系统；跨平台（Linux、macOS、Windows）。

## 依赖

- **运行时：** FFmpeg 库（libavformat、libavcodec、libavfilter、libavutil、libswscale、libswresample）——核心编解码工作完全委托给 FFmpeg。
- **可选后端：** SDL2（用于预览/播放显示）、OpenGL（用于 GPU 加速合成）、Jack/PulseAudio/ALSA（用于 Linux 音频输出）。
- **构建工具：** C++ 编译器、CMake、FFmpeg 开发头文件与库。
- **语言绑定：** C++ 为原生接口；其他语言访问取决于社区绑定（例如通过发行版提供的 `mlt` Python 绑定）。 [未验证]

## 运维难度

**中等。** MLT 本身是库/框架，不是可部署的服务——你需要把它链接或嵌入到自己的应用里。运维负担主要在周边构建与集成：（1）**FFmpeg 依赖管理**——你需要兼容的 FFmpeg 构建（版本匹配很重要），且 MLT 的功能集取决于 FFmpeg 的编译选项；（2）**插件可用性**——并非所有转场/滤镜类型都可用，取决于构建标志与可选依赖；（3）**时间线正确性**——逐帧精度的剪辑、转场时机与滤镜顺序需要谨慎构造 XML 或编程逻辑；（4）**资源管理**——渲染时间线跟任何视频管线一样消耗 CPU/GPU 与内存，因此需要并发控制与输出 staging。基于 MLT 自托管应用的难度取决于你在其上构建的应用本身；框架本身稳定，但对终端用户并非「开箱即用」。

## 健康度与可持续性

- **维护——活跃且长寿。** 截至 2026 年中为 v7.30.x，多年来持续发布。项目自 2000 年代初以来一直存在，并继续推出更新。 [未验证]
- **治理与 bus factor——小型核心团队。** 项目由一小群 dedicated 贡献者维护，而非大型基金会；bus factor  modest，但项目已在数十年间证明了自己的韧性。 [推断]
- **背书与寿命——无大型企业或基金会背书。** MLT 由社区驱动；它能存活是因为它是多个可见下游项目（Shotcut、Kdenlive）的共享引擎。这种生态依赖是它的保险——只要编辑器还需要它，它就会被维护。 [推断]
- **年龄与 Lindy 判断——老而活跃，Lindy 信号强劲。** 一个在视频领域被持续维护约 20 余年的项目，比年轻替代者更安全。MLT 的寿命因它作为多款知名编辑器后端的位置而得到强化。 [推断]
- **采用度——小众但根深蒂固。** 你选择 MLT 不是因为它 star 多（约 1.5k），而是因为 Shotcut 和 Kdenlive 都依赖它。对专业框架而言，这种生产用户验证比原始 popularity 更有意义。 [推断]
- **风险旗标——稳定的 LGPL-2.1+，无 relicense 历史。** 无已知 relicense 风波、无 open-core 阉割、无 CLA 要求。主要风险是社区规模相对 FFmpeg 较小——补丁和 niche 功能可能推进较慢。 [未验证]

## 存疑（未验证）

- [未验证] v7.30.x 与约 1.5k stars（截至 2026-07）；具体 star 数与最新版本标签具有时效性。
- [未验证] LGPL-2.1-or-later 在专有闭源产品中的动态链接与静态链接边界——请针对你的分发模式与法务核实。
- [未验证] Python 及其他语言绑定的可用性与维护状态因平台/发行版而异；在绑定策略上投入前，请先检查目标环境。
- [未验证] OpenTimelineIO 与 MLT 的精确关系——两者都面向时间线，但 OTIO 聚焦交换，而 MLT 聚焦渲染；直接对比仅为近似。
- [推断] Bus factor 与具体维护者人数是从 GitHub 活动模式与项目历史推断的，并非来自公开的治理文档。
- [推断] 「约 20 余年」的年龄估算为近似值；MLT 的早期历史早于 GitHub 广泛普及之前。
