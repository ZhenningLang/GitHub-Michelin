---
name: VMAF
slug: vmaf
repo: https://github.com/Netflix/vmaf
category: quality-metrics
tags: [video-quality, perceptual-metric, libvmaf, ffmpeg, encoding, c, python]
language: C
license: BSD-2-Clause-Patent
maturity: libvmaf v3.2.0, active (2026-06), 5.4k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-23T17:29:19Z
  default_branch: master
  default_branch_sha: 60016fbd50671a68856701d8ad578e8bd0387dd4
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:37:46Z
  overall: A
  overall_score: 3.6
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
        last_commit_age_days: 6
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 11.1
        qualifying_issues: 6
        band: default
        window_offset_days: 5
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: formulae.brew.sh
        canonical_package: libvmaf
        dependent_repos_count: 11
        downloads_last_month: 58378
        graph_tier: D
        volume_tier: B
        cross_check_divergence: null
        homebrew_installs_90d: 196149
        homebrew_tier: A
        release_downloads: 40043
        release_assets: 34
        release_tier: D
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 3879
        last_commit_age_days: 6
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 15
        top1_share: 0.772
        top3_share: 0.87
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# VMAF

Netflix 的、获 Emmy 奖的感知视频质量指标——一个 C 库 `libvmaf`（外加一个 `vmaf` CLI 和一个 Python wrapper），用来评估失真/编码后的视频相对参考在人眼看来有多好，同时还实现了 PSNR、SSIM、MS-SSIM、PSNR-HVS、CIEDE2000 以及 CAMBI 色带检测器。

![vmaf — 健康度雷达](../../../assets/health/vmaf.zh.svg)

## 何时使用

你是视频工程师，在调编码阶梯，而你真正在意的问题不是“码率掉了”，而是“画质是不是以观众会察觉的方式掉了”。裸 PSNR/SSIM 与人眼所见相关性差，于是你转向 VMAF：拿一个参考片段和一个编码后片段，跑 `vmaf` CLI（或把 `libvmaf` 接进你的管线，或用 FFmpeg 内建的 `libvmaf` 滤镜），得到一个 0–100 的感知分数，用它在不同 codec、preset、分辨率间比较以选定工作点。它是 codec/编码器评测的事实标准指标——AOM 在其通用测试条件（CTC）里指定了它——所以报告 VMAF 能让你的结果与更广社区可比。

当你想从一份单一、优化过的实现里拿到*不止一个*指标时也会用它：`libvmaf` 把 PSNR/SSIM/MS-SSIM/CIEDE2000 和 CAMBI（色带）收在一个接口背后，并支持在你自己的内容上训练/验证自定义 VMAF 模型。

## 何时不用

- **无参考 / 在线质量监控。** VMAF 是**全参考**的——它需要原始无损源与失真视频并排。对于你拿不到参考的实际线上流，它不适用（无参考指标是另一族）。
- **你想要一个绝对的“好/坏”阈值。** VMAF 是个*相对*比较工具；分数取决于模型、内容和观看假设——Netflix 自己就发多个模型（v0、新的 v1）并警告 enhancement-gain 作弊（故有 NEG 模式）。当作比较用，而非绝对的通过/不通过。[推断]
- **你在给静态图像 / 音频打分。** 它专门针对视频质量。
- **你需要零编译、纯 Python 的安装。** 核心是用 Meson/Ninja 构建的 C 库；Python wrapper 驱动它，但你是在编译（或用预编译二进制/Docker），而非只 `pip install` 纯 Python。[未验证]
- **你无法接受带专利条款的许可。** 它是 BSD+Patent（2020 年从 Apache-2.0 重新授权）——宽松且*带明确专利授予*；对多数人没问题，但若你所在组织对专利条款有特定政策请通读。
- **你在不对自己内容做验证的情况下优化某个指标。** VMAF 在特定数据集上训练；对非典型内容（屏幕内容、HDR 边角情况）请先验证或训练一个模型再信那个数字。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| PSNR / SSIM（独立） | 未收录 | 需要经典、便宜的信号保真基线时，选 PSNR 或 SSIM。 | 经典的信号保真指标；便宜、无处不在，但与感知质量相关性差——VMAF 正因它们不够用而存在（而 libvmaf 也照样内含它们）。 |
| [FFmpeg](../video-audio/transcoding-and-pipelines/ffmpeg.zh.md) | ✅ | 需要在媒体管线里把 `libvmaf` 作为滤镜运行时，选 FFmpeg。 | 把 `libvmaf` 作为滤镜集成——对多数用户而言这才是你在管线里真正跑 VMAF 的方式；FFmpeg 是宿主，VMAF 是其中的指标引擎。 |
| [SSIMULACRA2](ssimulacra2.zh.md) | ✅ | 需要来自 JPEG XL 生态的更新开源感知指标时，选 SSIMULACRA2。 | 一个更新的开源感知指标（出自 JPEG XL 生态），在图像/视频质量上渐获关注；另一种感知打分器，模型谱系不同。 |
| Netflix VMAF 云/SaaS 打分 | 未收录 | 偏好托管质量打分服务而不是自跑 libvmaf 时，选 Netflix VMAF 云/SaaS 打分。 | 托管的质量打分服务；不是仓库——比自跑 libvmaf 省事，但有厂商依赖。 |
| AVQT / 专有指标 | 未收录 | 工作流要求厂商感知指标时，选 AVQT 或专有指标。 | 厂商感知指标（如 Apple 的 AVQT）；目标相近，实现与生态封闭。 |

## 技术栈

- **语言：** 核心是 **C**（`libvmaf`），用 **Meson + Ninja** 构建；x86 SIMD 优化（AVX2/AVX-512）的定点实现以提速。
- **接口：** 独立的 `vmaf` 命令行工具、`libvmaf` C API，以及一个用于训练/测试/验证及数据集/绘图工具的 **Python** 库。
- **集成：** 作为 FFmpeg 滤镜随发（`--enable-libvmaf`）；提供 Dockerfile；支持 Windows 构建。
- **模型：** 可替换的模型文件（v0 旧版、截至 2026-06 的新 **v1**），外加一个 NEG（No Enhancement Gain）模式以抵抗增强作弊。

## 依赖

- **构建：** 一套 C 工具链加 **Meson 和 Ninja** 来构建 `libvmaf`/CLI；或用预编译二进制 / 提供的 Docker 镜像。
- **Python 工具：** Python wrapper 需要 Python 及其自身依赖（numpy/scipy 一类的科学栈）来做模型训练/验证/绘图。
- **运行时：** 参考帧 + 失真视频帧（通常经 FFmpeg）和一个模型文件；没有要跑的数据库或网络服务。
- **可选宿主：** FFmpeg，若你把 VMAF 当 FFmpeg 滤镜跑而非用独立工具。

## 运维难度

**中。** 概念上的用法很简单（喂参考 + 失真，拿分数），但*工程*有真实的棱角：构建 C 库（Meson/Ninja）或找对预编译二进制、为你的内容与报告语境选定并锁住正确的**模型**（v0 vs v1、NEG vs 默认）、确保帧对齐/同分辨率，以及给大目录打分的算力成本。多数团队靠经 FFmpeg 或 Docker 跑来绕开构建。微妙的运维风险是*方法论上的*——选错模型或跨模型版本比较分数，会悄无声息地让结论失效。

## 健康度与可持续性

- **维护活跃度**：Grade A——最近 13 周中 7 周有提交；最后提交距今 6 天。
- **响应速度**：Grade A——中位首次响应时间 11.1 小时，基于 6 个 qualifying issues/PRs。
- **采用广度**：Grade A——formulae.brew.sh 上月下载量 58,378（包名：libvmaf）。
- **长青度**：Grade A——仓库已创建 3879 天。
- **治理集中度**：Grade C——前三贡献者占比 87.0%（过去 12 个月内 15 位活跃维护者）。
- **许可风险**：BSD-2-Clause-Patent（宽松）——健康度雷达该轴记为 `?`，因为 GitHub 对该仓库报 NOASSERTION，许可信息以本页 frontmatter 为准而非机器块。

## 存疑（未验证）

- [未验证] 截至 2026-06 约 5.4k star / 822 fork；star 数对时间敏感，不是维护信号。
- [推断] 许可为 BSD-2-Clause-Patent：仓库 LICENSE 文件写明“BSD+Patent / SPDX BSD-2-Clause-Patent”，README 记录了 2020-02 从 Apache-2.0 的重新授权——GitHub API 报 `NOASSERTION`，故 SPDX id 取自读文件。
- [未验证] 确切的构建工具与 Python 依赖集合（Meson/Ninja 版本、科学栈）取自 README/推断，本轮未重读 manifest。
- [推断] “选错模型会悄悄让比较失效”和“非典型内容要先验证”是从多模型/NEG 设计与 README 自身告诫做出的方法论推断，而非测得的失败。
- [未验证] 对 SSIMULACRA2 / AVQT / SaaS 打分器的描述取自对生态的一般认知，本轮未再核验。
