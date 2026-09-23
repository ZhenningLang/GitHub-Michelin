---
name: Concat
slug: concat
repo: https://github.com/jub0t/Concat
category: video-editing
tags: [video-editor, nle, capcut-alternative, rust, slint, offline, cross-platform, automation]
language: Rust
license: AGPL-3.0-or-later
maturity: v0.2.2 beta, ~2.9k stars, created 2026-08-25 (~25 days old), 100+ commits/week, nightly build per push (as of 2026-09)
last_verified: 2026-09-19
type: app
upstream:
  pushed_at: 2026-09-19T03:09:30Z
  default_branch: main
  default_branch_sha: e5c8662daf6d721de2fd6c4e78cb671cd6d98393
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:39:37Z
  overall: C
  overall_score: 1.83
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
        last_commit_age_days: 0
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 4.5
        qualifying_issues: 43
        band: relaxed_solo
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 11392
        release_assets: 45
        release_tier: D
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 28
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 13
        top1_share: 0.86
        top3_share: 0.96
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# Concat

用 Rust 与 Slint 界面写的原生跨平台非线性视频编辑器——离线、免账号的「CapCut 替代品」，自带 FFmpeg，字幕与文本转语音在本机运行，并在图形界面之外提供 API／CLI／server。

![Concat — 健康度雷达](../../../assets/health/concat.zh.svg)

## 何时使用

你是个人创作者或两人小团队，在笔记本上剪短视频，而两条约束排除了常见答案：原始素材不该离开本机、也不该要求订阅；同时你希望脚本或 agent 能驱动你在图形界面里打开的那个工程。CapCut（未收录）满足不了第一条，MoviePy 这类批处理库满足不了第二条——你会在一个工具里手动剪，再把剪辑重新写成另一个工具里的脚本。

你会选 Concat，因为它是少数既算原生应用、又能用自身模型编程的编辑器。仓库拆成约 15 个 crate（`concat-core`、`concat-render`、`concat-media`、`concat-effects`、`concat-speech`、`concat-vision`、`concat-project` 等），对外是 `concat-api`、`concat-cli` 与 `concat-server`（TCP 或 Unix socket 上的 JSON-RPC 行，gRPC 藏在默认关闭的 feature 后），于是同一套命令模型既服务界面也服务脚本。与 [OpenCut](opencut.zh.md) 的决定性取舍：Concat 是下载即用的原生二进制，桌面与移动端都能完全离线，且有当下就能跑的 beta；OpenCut 当前仓库是浏览器／WASM 重写，不接受外部贡献且自 2026-04 起没有发布。需要「现在就能跑、带自动化接口的原生编辑器」选 Concat；更看重社区规模与浏览器触达、不急于今天跑起来，选 OpenCut。

## 何时不用

- **付费客户项目需要稳定性。** Concat 是只有 25 天历史的 0.2.x beta，公开 issue 里已经有 Linux／rpm 版卡顿到几乎不可用、Android 无法导入媒体的报告。改用 DaVinci Resolve（未收录），或等一个稳定的 tagged 版本，因为项目中途崩溃的代价高于你想省下的订阅费。
- **你现在就要专业特效栈——可跟踪遮罩、关键帧曲线编辑器、调整图层、速度曲线。** 这些在 Concat 自己的 roadmap 上全部未打勾。要已经发布的遮罩与曲线编辑器，去看 OpenCut v0.3.0 的功能集或商业 NLE（未收录）。
- **你只需要脚本化、可重复渲染，不需要交互式剪辑。** 图形编辑器是错的形态——批量管线用 [MoviePy](../video-audio/moviepy.zh.md)，需要在 CI 里渲染确定性组件时用 [Remotion](../../video-production/remotion.zh.md)。
- **你要自建编辑器或无头剪辑服务。** 不要为了时间线模型去 fork 一个年轻 beta；用 [MLT](../video-audio/mlt.zh.md)，也就是 Shotcut、Kdenlive 底下的 LGPL 引擎，因为它给你时间线语义，而不会让你背上一个 AGPL 应用。
- **你的组织无法接受 AGPL-3.0 义务，或无法接受发行包里的许可组合。** Concat 本体是 AGPL-3.0-or-later 加插件例外，而分发出去的 bundle 里还带 FFmpeg（GPL，含 x264）、sherpa-onnx 与 espeak-ng（GPL-3.0），以及以 GPL-3.0 选项使用的 Slint。AGPL 是硬约束时，改用 MIT 许可的编辑器，例如 [OpenCut](opencut.zh.md)。
- **剪辑只是更大管线里的一个通用环节。** Concat 没有文档化的无头渲染模式；直接驱动 [FFmpeg](../video-audio/ffmpeg.zh.md) 更合适，因为桌面应用无法当作批处理任务来调度。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [OpenCut](opencut.zh.md) | ✅ | 想要最大的开源社区、MIT 许可与规划中的插件／MCP 架构时选 OpenCut；需要今天就能离线安装运行的原生二进制时选 Concat，因为 OpenCut 仓库正在重写、不接受外部贡献，且自 2026-04 起没有发布。 | Concat：可运行的原生 beta 加自动化接口，单人维护，AGPL。OpenCut：更大的社区与宽松许可，当前没有可下载的构建。 |
| [MLT](../video-audio/mlt.zh.md) | ✅ | 你要造编辑器而不是剪辑时选 MLT；想要一个成品应用、通过 API 脚本化它的时间线而不必自己实现时选 Concat，因为 MLT 是无界面框架，且把所有编解码工作交给 FFmpeg。 | MLT：可嵌入可扩展的 LGPL 引擎，应用要你自己写。Concat：完整的 AGPL 应用，你只做脚本化。 |
| [MoviePy](../video-audio/moviepy.zh.md) | ✅ | 剪辑是可重复的 Python 批处理任务时选 MoviePy；需要人看到时间线并交互式迭代时选 Concat，因为 MoviePy 没有界面也没有预览，且维护强度已从峰值回落。 | MoviePy：可脚本化、无头，没有交互预览。Concat：有交互界面也有 API，但桌面依赖更重。 |
| CapCut（字节跳动） | 未收录 | 想要免费、打磨成熟、带云端 AI 特效且不在意账号时选 CapCut；素材不能离开本机、编辑器必须开源时选 Concat，因为 CapCut 闭源、绑定账号，并把 4K 与 AI 放在 Pro 后面。 | CapCut：特效与模板成熟，无法自托管，受云端条款约束。Concat：离线开源，特效远少。 |
| DaVinci Resolve／Premiere Pro | 未收录 | 专业剪辑师需要可跟踪遮罩、调色与成熟关键帧编辑器来完成交付时选商业 NLE；需要离线、可脚本化、免许可费地剪短视频时选 Concat，因为商业工具闭源，且其免费档是功能阉割的。 | 商业 NLE：深度与稳定。Concat：原生、离线、可自动化，但不成熟。 |

## 技术栈

- **语言／界面：** Rust workspace，约 15 个 crate 加一套 Slint 界面——`concat`、`concat-core`、`concat-render`、`concat-media`、`concat-effects`、`concat-export`、`concat-project`、`concat-speech`、`concat-vision`、`concat-text`、`concat-host`、`concat-api`、`concat-cli`、`concat-server`、`concat-android`。
- **媒体引擎：** 用 FFmpeg 库做解码、编码、封装与滤镜，并打包进发行产物；导出仅 H.264 MP4（README）。
- **本机模型：** whisper.cpp 做自动字幕；sherpa-onnx 加 espeak-ng 做文本转语音与变声；一个分割模型编译进应用，用于自动抠背景。
- **自动化接口：** `concat-api`（共享命令类型）、`concat-cli` 与 `concat-server`——TCP 或 Unix socket 上的 JSON-RPC 行，每次运行随机生成 token，另有一个默认关闭的 gRPC（tonic／prost）feature。仓库描述里宣传「支持 MCP」[未验证]：截至 2026-09-19，默认分支文件树里没有 MCP 模块。
- **CI／发布：** GitHub Actions 工作流 `ci.yml`、`build-app.yml`、`mobile.yml`、`models.yml`、`nightly.yml`、`nix.yml`、`release.yml`；每次 push 都会重建一个覆盖全平台的 `nightly` 发布。

## 依赖

- **目标平台：** Windows（x86_64、arm64）、macOS（Intel、Apple Silicon）、Linux（x86_64、arm64；tar.gz／AppImage／deb／rpm）、Android arm64。iOS／iPadOS 只能侧载，README 标注为未测试。
- **系统门槛（README）：** 2013 年及以后的任意 64 位 CPU、4 GB 内存、500 MB 应用体积加上最小的字幕模型；4K 时间线建议 6 核与 16 GB。
- **GPU 可选**——Metal（macOS）、DirectX 12（Windows）或 Vulkan（Linux）；没有可用 GPU 时窗口与监看回落到 CPU。
- **可选模型首次使用时下载**，之后不再需要网络：字幕模型 78–488 MB（取决于 Whisper 规格）、文本转语音 132 MB 或 349 MB、人像抠图 15 MB、物体抠图 179 MB、抠图笔刷 40 MB。
- 没有账号、没有服务端、没有数据库。macOS 构建未签名，首次运行需要 `xattr -dr com.apple.quarantine`。

## 运维难度

**使用低、分发中。** 对用户来说它就是普通的桌面／移动应用：下载压缩包、运行二进制、让它拉一次模型。把可执行文件旁边放一个 `portable` 目录，设置、最近记录与模型就都留在移动介质上，用户目录不写任何东西。没有服务、密钥或数据库要运维。负担在发布与管理侧：未签名的 macOS／Windows 产物会触发系统警告；安装包混合 AGPL 与 GPL 组件，修改后再分发需要许可审查；从源码构建要拉 Rust 工具链以及本机 FFmpeg／whisper／sherpa 依赖。在受管机器上，逐机器的模型下载是你必须预置或供应的状态。

## 健康度与可持续性

- **维护（2026-09）：** 相对其年龄算高频。创建于 2026-08-25；GitHub 周提交统计显示前四周分别为 142、106、89、111 次提交，每次 push 都出 nightly，抽查的 PR 合并速度以小时计（#140 于 15:15 开、15:43 合）。
- **治理／bus factor——一个人。** `jub0t` 占约 490 次提交中的 427 次；第二名贡献者 46 次，其余均不超过 4 次，watcher 只有 22 个。路线图背后没有基金会或厂商。
- **背书与 Lindy——太年轻，还谈不上 Lindy 先验。** 25 天里攒到 2.8k star 与 253 fork 是关注度，不是记录；按本索引的先验，年轻且被热炒的仓库是风险信号，而它还没有「年龄 × 仍活跃」的历史可供衡量。
- **采用与生态——早期。** 下载量与 star 是主体；API／CLI／server crate 与插件例外描述的是一个计划中的自动化生态，而非已建成的生态，文档也只有 README／ROADMAP／TODO 加各 crate 的 README。
- **风险信号：** 版权经 CLA 集中持有，并公开了商业许可通道（open-core 形态）；AGPL-3.0-or-later 加插件例外，而打包产物里还含 GPL 组件；`TRADEMARK.md` 限制名称与标识使用；分发以 nightly 为主，最新 tagged 版本是 v0.2.2。

## 存疑（未验证）

- [未验证] 仓库描述与插件例外里的「支持 MCP」在默认分支文件树（756 个路径，检查于 2026-09-19）中找不到对应 MCP 模块；实际存在的可脚本化接口是 JSON-RPC／gRPC。依赖该集成前请自行确认。
- [未验证] README 的平台矩阵（Android「已支持」、iOS／iPadOS「待测试」）为作者自述；本页没有在任何平台上运行过二进制。
- [推断] 合并速度的结论来自四个 PR（#140、#141、#142、#144），样本很小，说明不了审查深度或一致性。
- [未验证] star、fork、issue 与提交数（2,854／253／44 个未关／约 490）是 2026-09-19 的 GitHub 时点数据，会变动。
- [未验证] 打包内含的 FFmpeg（GPL，含 x264）、sherpa-onnx／espeak-ng（GPL-3.0）与 Slint 的 GPL-3.0 选项在再分发时的兼容性，本页未做法律审查；`THIRD_PARTY_NOTICES.md` 与 `LICENSE-EXCEPTIONS.md` 均为作者提供。
- [推断] 各 crate 的职责由仓库树中的 crate 名称推断，并非来自构建文档。
