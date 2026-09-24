---
name: PyAV
slug: pyav
repo: https://github.com/PyAV-Org/PyAV
category: transcoding-and-pipelines
tags: [python, ffmpeg, libav, video, audio, decoding, encoding, frames, bindings]
language: Python / Cython
license: MIT
maturity: v14.0.x, active, ~5k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-02T06:21:32Z
  default_branch: main
  default_branch_sha: 54a4395bb4cdd9cdd53ff6216c50b69f6475c13d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:39:27Z
  overall: A
  overall_score: 3.5
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
        last_commit_age_days: 5
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 13.4
        qualifying_issues: 10
        band: default
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: av
        dependent_repos_count: 2332
        downloads_last_month: 25049996
        graph_tier: B
        volume_tier: A
        cross_check_divergence: null
        release_downloads: 2199
        release_assets: 166
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5049
        last_commit_age_days: 5
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 26
        top1_share: 0.816
        top3_share: 0.891
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-3-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# PyAV


面向 FFmpeg 的 libav* 库的 Pythonic 绑定——在进程内完成解码/编码，可逐帧访问 NumPy 数组和 Python bytes，无需生成子进程。


![PyAV — health radar](../../../../assets/health/pyav.zh.svg)

## 何时使用

你是一名 Python 机器学习工程师，正在为训练管线预处理视频：你需要从一段高分辨率 MP4 中读取帧，可选择性地调整尺寸或转换色彩空间，然后把它们作为 NumPy 数组喂进 PyTorch。为每个视频调用一次 `ffmpeg` 子进程太慢，而且让你失去了帧级别的控制；你需要在同一个 Python 进程内以编程方式访问每一帧解码结果。你执行 `pip install av`，用 `av.open('input.mp4')` 打开视频，在 `container.decode(video=0)` 上迭代，每一帧都能通过 `.to_ndarray(format='rgb24')` 拿到真正的 NumPy 数组——你可以直接做批次化和归一化。你也可以用它来编码：创建输出容器，添加一条 `codec='libx264'` 的视频流，然后把数组直接写回文件。它的最佳位置就在这个边界上：当你需要 FFmpeg 的格式/编解码器覆盖度，但又想留在 Python 世界里拥有帧级别的控制力时。

## 何时不用

- **你只是需要做简单的转码或滤镜图。** 用 [ffmpeg-python](ffmpeg-python.zh.md) 或者直接调用 FFmpeg CLI——PyAV 更底层、安装更重。
- **你不想编译 Cython 扩展。** PyAV 需要针对 FFmpeg 头文件编译 Cython 扩展；常用平台有预编译 wheel，但特殊环境可能需要完整的构建工具链。[推断]
- **你需要一个高级视频编辑器。** PyAV 是轻薄的 libav 包装器，不是时间线编辑器——开箱即用没有剪辑、合成、文字叠加或特效。
- **你不是在 Python 里工作。** 这是 Python 专用绑定。
- **你需要库级别的硬件加速编解码。** PyAV 确实暴露了一些硬件上下文，但 API 面比原生 FFmpeg 窄；请确认你的具体编解码器/GPU 路径是否受支持。[未验证]
- **你需要 Python < 3.8。** PyAV 要求 Python 3.8+。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FFmpeg](ffmpeg.zh.md) | ✅ | 需要通用 CLI 或 C 库时，选 FFmpeg。 | 通用 CLI 与 C 库；能力最强，但 API 陡峭，且没有原生 Python 帧访问，需要自己包装。 |
| [ffmpeg-python](ffmpeg-python.zh.md) | ✅ | 需要可读地构造 Python 滤镜图并生成子进程调用 CLI 时，选 ffmpeg-python。 | 用 Python 可读地构造 DAG 并生成子进程调用 ffmpeg CLI；无需编译，但也没有进程内帧访问。 |
| [MoviePy](../editing-and-cutting/moviepy.zh.md) | ✅ | 需要更高层的 Python 视频编辑、特效或合成时，选 MoviePy。 | 更高层的 Python 视频编辑（特效、合成、文字），API 更友好；适合编辑，但直接帧控制力较弱。 |
| [GStreamer](gstreamer.zh.md) | ✅ | 需要实时、嵌入应用的媒体管线框架时，选 GStreamer。 | 面向实时应用的管线式多媒体框架；学习曲线陡峭，在流式/嵌入式场景强于批量帧处理。 |
| [HandBrake](handbrake.zh.md) | ✅ | 需要预设驱动的终端用户转码应用时，选 HandBrake。 | 终端用户转码应用（GUI + CLI）；远比原生 libav 窄，不是库，也不适合帧级脚本化。 |
| OpenCV | 未收录 | 需要计算机视觉管线及其自有视频 I/O 时，选 OpenCV。 | 计算机视觉库，自带视频 I/O；适合采集和简单读写，但编解码器/格式覆盖度远不及 FFmpeg/libav。 |
| imageio-ffmpeg | 未收录 | 需要轻量 shim 在 imageio 中通过 FFmpeg 读取视频帧时，选 imageio-ffmpeg。 | 在 imageio 中通过 FFmpeg 读取视频帧的轻量 shim；比 PyAV 的直接 libav 绑定更简单，但控制力更弱。 |

## 健康度与可持续性

- **维护状态（2026-07）。** PyAV 维护活跃，最近提交仅 1 天前，过去 13 周中有 10 周活跃。社区响应迅速，issue 中位首次响应时间约 6.3 小时。项目处于持续迭代中。
- **治理与 bus factor。** 治理健康度为 D，虽然过去 12 个月有 26 位活跃贡献者，但前 1 位贡献者占比高达 77%，前 3 位占比 86%，存在集中度风险。核心维护者 Mike Boers 占主导地位，若其退出可能显著影响项目节奏。这是一个需要关注的 bus factor 风险。
- **背书与长期性。** PyAV 自 2013 年左右启动（约 13.6 年历史），MIT 许可证，从未变更。作为 FFmpeg/libav 的 Python 绑定，其价值与 FFmpeg 生态绑定紧密，只要 FFmpeg 继续被广泛使用，PyAV 就有持续的必要性。Lindy 效应正面：一个长期存在且仍在活跃的项目，比新兴替代品更可靠。
- **采用与生态。** PyPI 包名为 `av`，月下载量约 2700 万，2332 个依赖仓库。在 Python 视频处理领域是事实标准，被许多 ML 训练管线、CV 工具链依赖。生态位明确，替代方案（如 imageio-ffmpeg）控制力更弱。
- **风险标志。** 许可证为 MIT（宽松），无重新授权历史。风险主要在于：1）治理集中度（C 级）；2）绑定 FFmpeg 的 API 变更，需跟踪 FFmpeg 版本兼容性。整体风险较低，但建议评估核心维护者的持续投入。

## 技术栈

- **语言：** Python（约 55%）搭配 Cython（约 40%）编写编译扩展，包装 `libavcodec`、`libavformat`、`libavfilter`、`libavutil`、`libswscale`。
- **绑定模式：** Cython `.pyx` 文件直接包装 FFmpeg 的 C API——进程内运行，不生成子进程。
- **核心包装库：** `libavcodec`（编码/解码）、`libavformat`（封装/解封装）、`libavfilter`（滤镜图）、`libavutil`、`libswscale`（像素格式转换）。
- **可选集成：** NumPy 用于 `ndarray` 帧访问；Pillow 用于图像互操作。

## 依赖

- **运行时：** Python 3.8+，以及编译时链接的 FFmpeg 库（`libavcodec`、`libavformat` 等）。预编译 wheel 捆绑了常用库；从源码构建需要 FFmpeg 开发头文件和 C 编译器。
- **Python 依赖：** `numpy` 强烈建议安装，用于数组访问；`Pillow` 可选，用于图像转换。
- **无服务/数据库：** 它是进程内库；你自备媒体文件和 Python 环境。

## 运维难度

**对库本身为低到中，但取决于构建环境。** 从预编译 wheel 安装只需 `pip install av`——非常轻松。真正的负担在你的平台没有 wheel 时：你需要 C 编译器、FFmpeg 开发头文件/库，并且 PyAV 与 FFmpeg 版本要匹配。容器化环境（Docker）和 CI 必须确保构建依赖已就绪，或者锁定到支持 wheel 的基础镜像。一旦安装完成，运维很直接——它是库调用，无守护进程，无数据存储。

## 存疑（未验证）

- [未验证] 截至 2026-07 约 5k star 且状态活跃；star 数具有时效性。
- [未验证] v14.0.x 成熟度与 Python 3.8+ 要求综合自 README 和 PyPI 元数据，未通过实际安装重新验证。
- [推断] 硬件加速支持（NVENC、VAAPI 等）推断自 FFmpeg 的通用能力；本回合未确认 PyAV 针对各硬件路径的具体 API 面。
- [推断] 预编译 wheel 覆盖范围推断自常见平台（manylinux、macOS、Windows）；特殊 Linux 发行版或 ARM 变体可能需要源码构建。
