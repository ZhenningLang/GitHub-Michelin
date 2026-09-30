---
name: fframes
slug: fframes
repo: https://github.com/dmtrKovalenko/fframes
category: video-production
tags: [video-rendering, programmatic-video, rust, gpu, svg, motion-graphics, agent-skill]
language: Rust
license: MIT
maturity: v1.1.0 (1.0 stable 2026-09-28 after betas on crates.io since 2024-04), active, 1.2k stars, repo since 2021-11 (as of 2026-09)
last_verified: 2026-09-30
type: framework
upstream:
  pushed_at: 2026-09-30T04:38:48Z
  default_branch: main
  default_branch_sha: 6454a6dc3ef39922ae804238904317a8d94f00d3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-30T11:51:04Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
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
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 1773
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 4
        top1_share: 0.882
        top3_share: 0.971
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
    adoption: { reason: ambiguous }
---

# fframes

用代码做一支两分钟的动效视频，常见做法是让无头 Chrome 一帧一帧截图，慢；交给 coding agent 写，它又看不见标题是不是被画布边缘切掉了半截。fframes 让你（或 agent）用 Rust 把每一帧写成一棵 SVG 树，在 GPU 上画出来、在进程内用 ffmpeg 的库直接编码，并且每个项目自带一组命令，把视频变成 agent 读得懂的 PNG 拼图和数字。

![fframes — 健康度雷达](../../assets/health/fframes.zh.svg)

## 何时使用

你是开发者，或者你在给 coding agent 下需求，要做的是反复出现的“代码视频”：每次发版重做一遍的发布短片、每场会议演讲一张开场卡、播客可视化、每周数字都会变的数据讲解。用基于浏览器的渲染器，这个循环很慢（打包、起 Chrome、截 300 帧、再编码）；写 composition 的 agent 还是个“瞎子”——它把 `out.mp4` 交给你，并不知道标题因为文字跑出画布，显示成了 `Quarterly revenu`。

你选 fframes，是愿意付出 Rust 加原生工具链的代价，换两样东西：一是渲染链里没有浏览器（Skia 在 Metal/Vulkan 上画 SVG，ffmpeg 的 libav 库直接链接进来，而不是另起一个 ffmpeg 进程）；二是每个项目自带一套给“看不见的作者”用的命令行——`inspect` 报出被切掉的文字、缺失的字体、非法 SVG，附带时间点和场景，出错时退出码为 2；`strip`／`onion`／`frame` 输出 PNG；`audio analyze` 报响度（LUFS）和削波。和 [Remotion](remotion.zh.md)、[HyperFrames](hyperframes.zh.md) 相比，决定性的取舍是：那两个让你写 React 或 HTML，继承浏览器的排版引擎和生态；fframes 要你写显式、啰嗦的 Rust（作者说这正是它多年没正式发布的原因，也是 agent 让它变得可用的原因），换来原生速度——它自己的基准测试在 x264 `medium` 下比 Remotion 最优配置快 1.5 倍，`ultrafast` 下快 2.85 倍——以及没有公司规模门槛的 MIT 许可。

## 怎么用起来

你的视频是一个 Rust 结构体：声明帧率、尺寸、时长和音轨表，再实现 `render_frame`——给它任意帧号，它返回一棵用 `svgr!` 宏写的 SVG 树。可以把它想成 JSX，只不过产出的是 SVG，花括号里的 `{表达式}` 是 Rust。动起来靠 `timeline!` 和弹簧（spring）辅助函数：把“第 2 秒起按某种缓动从这里移到那里”换算成当前帧的数值。fframes 替你做的：生成工程和它的命令行（`cargo fframes new`），在编译期给标记里不变的部分算哈希、不必每帧重建，经 Skia 在 GPU 上（或走 CPU 后备）把每帧光栅化，混音，再通过静态链接的 ffmpeg 库编码成 `out.mp4`。你要做的：装好原生编解码包、写帧、跑命令行。agent 路径是同一套代码，只是换了作者——`npx skills add https://fframes.studio` 装上一个 skill，带 agent 从空文件夹一路走 `timeline` → `inspect` → `strip` → `render`，靠读 PNG 和数字而不是看片来检查；`preview` 给人开一个带声音的实时 GPU 窗口，浏览器里还有一个把视频编译成 WebAssembly 的编辑器，可以拖时间轴。

![fframes — 主干用户故事](../../assets/flow/fframes.zh.svg)

<!-- flow-steps:begin (generated from flows/fframes.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：装好系统编解码库和项目生成器 — `cargo install --locked cargo-fframes`
2. **你**：用模板生成一个视频项目 — `cargo fframes new my-video`
3. **fframes**：生成 Rust 工程：视频本体、现成命令行、编进二进制的素材目录 — 组件：`cargo-fframes`
4. **你**：用 Rust 把每一帧写成 SVG 树，按时间给数值做动画 — `svgr! · timeline!`
5. **你**：发起最终渲染 — `cargo run --release -- render`
6. **fframes**：在 GPU（Metal 或 Vulkan）上画出每一帧，静态标记直接复用缓存 — 组件：`Skia 渲染器`
7. **fframes**：在进程内用链接进来的 libav 库编码，写出 out.mp4 — `out.mp4` — 组件：`fframes-media（libav）`

**价值**：代码直接出 MP4，中间没有浏览器——不用再让无头 Chrome 一帧帧截图

</details>
<!-- flow-steps:end -->

## 何时不用

- **你的团队（或 agent）写的是 Web，不是 Rust。** 这里的一帧是带 SVG 宏的 Rust 代码，没有 HTML/CSS 排版、没有 npm 组件生态、没有 DOM。改用 [HyperFrames](hyperframes.zh.md)（纯 HTML 加可 seek 的动画库，Apache-2.0）或 [Remotion](remotion.zh.md)（React 组件，生态最大），因为对多数团队来说，能在视频里复用现成网页 UI、CSS 弹性布局和 React 图表，比 1.5–3 倍的渲染提速更值钱。
- **你现在就要云端大规模并行渲染。** fframes 在它运行的那台机器上渲染，不带分布式渲染器。成千上万个变体要在不用你盯着的基础设施上并行出片时，选 [Remotion](remotion.zh.md)（`@remotion/lambda`）或 [HyperFrames](hyperframes.zh.md)（它的 AWS Lambda 包）。
- **你的构建机装不了原生 C/C++ 工具链。** 每个项目都要链接 Skia 和 ffmpeg：macOS/Linux 的 arm64/x86_64 下载预编译库（约一分钟），其他目标或特性组合从源码编译（最长约 20 分钟），Windows 要另下 FFmpeg 9 共享库再装 LLVM；源码构建的缓存挪到另一种 CPU 上可能直接 `SIGILL` 崩溃，除非打开 `build-portable`。它的 issue 历史大半是构建故障（ffmpeg 5 头文件、Xcode 27 的 `_Traits`）。如果你的 CI 是锁死的容器，Node 渲染器（[HyperFrames](hyperframes.zh.md)）安装更轻。
- **你要把编译好的渲染器发给客户，又不能接受 GPL 义务。** fframes 本身是 MIT，但在 macOS/Linux 上生成的项目默认打开 `h264` + `libav-agree-gpl`，把 libx264 静态链接进二进制；分发这个二进制会把 GPL 条款一起带过去 [推断]。改成不含 GPL 编解码器的构建（VPX／Opus，或 VideoToolbox 这类平台编码器），或者只在自己服务器上渲染，并交给法务评审。
- **你要的是带教学词汇的数学／图示动画。** Manim（未收录）有 LaTeX、函数图像、几何图元和庞大的教育社区；fframes 只给你原始 SVG 和时间轴，这些图元得自己重造。
- **你主要是剪辑、拼接已有素材。** fframes 是用代码合成画面；裁剪、拼接、叠加录好的片段，用 [MoviePy](../media-processing/video-audio/editing-and-cutting/moviepy.zh.md) 或直接驱动 [FFmpeg](../media-processing/video-audio/transcoding-and-pipelines/ffmpeg.zh.md)。
- **你要押一个多人维护、API 长期稳定的底座做产品。** 1.0 在 2026-09-28 才发布，此前许可证改过两次（见健康度一节），一个作者占了约九成提交。要用就锁死精确版本、给 API 变动留预算，或者选 [Remotion](remotion.zh.md)——靠付费许可养活的公司已经把 v4 发版列车跑了好几年。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Remotion](remotion.zh.md) | ✅ | React 团队要最成熟的代码转视频引擎、要 Lambda 并行和组件生态时选 Remotion；在自己的 GPU 机器上渲染、要无公司规模门槛的 MIT 许可、在乎渲染耗时胜过复用网页组件时选 fframes，因为 fframes 用 Skia 加链接进来的 libav 换掉了浏览器。 | Remotion 有六年稳定性、React 复用和云渲染，但带 source-available 许可门槛和 Chrome 逐帧截图；fframes 自测默认对默认快 1.41 倍、最优对最优在 x264 `medium` 下快 1.5 倍（`ultrafast` 下 2.85 倍），代价是 Rust 的啰嗦和原生构建的折腾。 |
| [HyperFrames](hyperframes.zh.md) | ✅ | 让 coding agent 用它本来就写得顺的纯 HTML 做视频、在 CI 或 Lambda 上按 Apache-2.0 渲染时选 HyperFrames；agent 的产出要在没有浏览器的情况下被检查、还要原生地快速出片时选 fframes，因为 fframes 把 `inspect`／`strip`／`audio analyze` 做成了每个项目里的一等命令。 | HyperFrames 保留网页排版引擎、动画库和只要 Node 的安装；fframes 为速度丢掉浏览器，换来一条 Rust/C 工具链。两者都以 agent 为先；HyperFrames 有厂商（HeyGen）背书，fframes 是单人作者。 |
| Motion Canvas | 未收录 | 手工打磨讲解动画、想要 TypeScript 生成器 API 加实时可视化编辑器时选 Motion Canvas；画面要由代码或 agent 批量、以原生速度渲染、还要自带音频分析时选 fframes，因为 Motion Canvas 以交互式编辑器驱动的工作流为中心。本轮标签批次未收录。 | Motion Canvas（MIT，约 1.9 万 star，最近推送 2026-07）对 TS 用户和设计师更友好；fframes 无头渲染更快，但除了它的 WASM 时间轴编辑器，没有同等的可视化创作工具。 |
| Manim | 未收录 | 视频是数学或算法讲解、需要 LaTeX、函数图像和几何图元时选 Manim；做品牌动效、社交短片、带配乐的数据视频时选 fframes，因为 Manim 的场景词汇是为教学设计的，而 fframes 给你的是原始 SVG。本轮标签批次未收录。 | Manim（MIT，约 4.1 万 star，活跃）有庞大的教育社区和 Python 的顺手；fframes 有 GPU 渲染、进程内编码和给 agent 的质检工具，但没有数学图元。 |
| [MoviePy](../media-processing/video-audio/editing-and-cutting/moviepy.zh.md) | ✅ | 任务是用脚本剪辑现成片段——裁剪、拼接、叠字——时选 MoviePy；每一帧都由代码生成时选 fframes，因为 fframes 是帧渲染器，MoviePy 是作用于已解码素材的剪辑库。 | MoviePy 纯 Python、上手平缓，但逐帧重绘时慢；fframes 生成图形快，代价是 Rust 和原生构建配置。 |

## 技术栈

- Rust workspace（生成的项目用 edition 2024）：`fframes` 核心 crate（视频／场景／时间轴／音频 API，`fframes::cli`）、`svgr-macro`（编译期 SVG 宏）、`fframes-media`（经 `ffmpeg-sys-fframes` 绑定 ffmpeg）、`fframes-skia-renderer`、`fframes-native-player`（实时预览）、`cargo-fframes`（项目生成器）、`webvtt-parser`。
- 渲染：Skia 跑在 Metal（macOS）或 Vulkan（Linux/Windows）上，另有 CPU 后端；SVG 解析与渲染走 `svgr`/`usvgr` 0.46，即作者自己维护的 linebender/resvg 分叉（MPL-2.0）。着色器图层接受 SkSL 或直接粘贴的 Shadertoy GLSL。
- 编码：静态链接 ffmpeg 的 libav（macOS/Linux 的 arm64/x86_64 有预编译 FFmpeg 包，其他平台源码构建，Windows 用 FFmpeg 9 共享库）。编解码器由 Cargo feature 选择（`h264`、`h265`、`vpx`、`opus`、`aac`，硬件加速 `videotoolbox`／`vaapi`／`nvidia`／`qsv`），并要显式打开 `libav-agree-gpl`／`libav-agree-nonfree`。
- 编辑器：ReScript/TypeScript 写的浏览器编辑器，运行编译成 WebAssembly 的视频（只有改编辑器本身才需要 Node + pnpm）。
- agent 入口：`skills/fframes-video`（SKILL.md 加 API、设计、音频参考文档），用 `npx skills add https://fframes.studio` 安装。

## 依赖

- Rust 工具链（rustup）和 Cargo；`cargo install --locked cargo-fframes`。
- 链接 ffmpeg 所需的系统包——macOS：`pkg-config ffmpeg x264 x265 opus nasm ninja`（Homebrew）；Debian：`yasm nasm ffmpeg libx264-dev libx265-dev libopus-dev libclang-dev clang ninja-build libvpx-dev libasound2-dev`；Windows：通过 `FFMPEG_DIR` 或 vcpkg 提供 FFmpeg 9 共享库，再加 LLVM（`LIBCLANG_PATH`）。
- 默认 Skia 后端和预览窗口需要支持 Metal 或 Vulkan 的 GPU；`--backend cpu` 可以不要 GPU（没有预览，更慢）。
- 首次构建要联网下载预编译 Skia/FFmpeg 包（否则就是漫长的源码构建）。
- 不需要服务器、数据库或云账号；渲染就是一个本地二进制。

## 运维难度

**中。** 日常就是在一个 crate 里跑 `cargo run --release -- <command>`，后续构建几秒钟。成本在原生层：每个操作系统各自的编解码包；只有在预编译目标上首次构建才快；Windows 专属的 FFmpeg/LLVM 接线；跨 CPU 缓存构建要开 `build-portable` 以免 `SIGILL`；还有 Metal/Vulkan 的 GPU 驱动。工具链升级以前就弄坏过构建（Skia 绑定里的 Xcode 27 `_Traits` 问题，1.0.3 改为分发预编译 Metal 二进制后修复）。没有要运维的服务，但要在另一台机器上复现渲染，就得复现这整条工具链。

## 健康度与可持续性

- **维护（2026-09-30）：** 眼下非常活跃——v1.0.0 到 v1.1.0 在 2026-09-28 至 2026-09-30 间连发，最近推送 2026-09-30，只有 3 个 open issue，新 issue 当天就有维护者回复。但此前多年是一段漫长的 beta（crates.io 自 2024-04 起发 beta，中间常有数月空档），所以现在的节奏是发布周的冲劲，还不是被证明过的持续节奏 [推断]。
- **治理／巴士因子：** 个人仓库（owner 类型为 User）；默认分支 228 次提交里 dmtrKovalenko 占 208 次，其余是一长串一两次提交的贡献者。渲染器建立在作者自己的 resvg 分叉（`svgr`）上，他自己说需要把上游修复手工再打一遍。巴士因子为 1。
- **背书与 Lindy：** 仓库建于 2021-11（首个提交是 2021-09 的 “POC”），断断续续开发约 5 年，但稳定 API 只有两天。按本索引的先验，作为产品它仍然年轻——想法的年龄不等于契约的年龄。资金来源只有一个 GitHub Sponsor 链接，背后没有公司或基金会。
- **采用度：** 1,231 star／20 fork；`fframes` 在 crates.io 累计下载 3.8 万（被几十个预发布版本抬高），近 90 天约 1 千；`cargo-fframes` 在 2026-09-28 首次发布。除作者自己的视频和示例外，没有公开记录的知名生产用户。
- **风险信号：** 许可证历史——GPLv3（2022）→ 带“禁止换名分发”条款的 BSD-3 变体（2025-02）→ MIT（2026-09-28，PR #144），所以锁定在 1.0 之前某个 beta 上的项目，适用条款可能和今天的版本不同。默认生成的项目会链接 GPL 的 x264。未关闭的 bug 涉及输出正确性（H.264 B 帧输入丢失末尾帧、BT.709 颜色），2025 年报告的音频嗡嗡声问题仍未关闭。

## 存疑（未验证）

- [未验证] 基准数据（x264 `medium` 下比 Remotion 最优配置快 1.50 倍、`ultrafast` 下 2.85 倍、默认对默认 1.41 倍）来自项目自己在一台 Apple M4 Max 上跑的 `render-bench/vs-remotion`；本页没有复现，README 自己也说 Linux/x86 结果可能不同。
- [未验证] README 称 Skia “比内置 CPU 后端快约 10 倍”；但项目自己那个文字密集的基准里，CPU 后端几乎一样快（6.80 秒对 6.29 秒），差距高度取决于画面内容。
- [未验证] “128 秒发布视频 48 分钟 vibe 出来、36 秒渲染完”，以及 “render --draft 约一秒编码半尺寸的一个场景”，都是作者说法，未复现。
- [推断] “分发用默认模板（`h264` + `libav-agree-gpl`，静态链接 libx264）构建的二进制会触发 GPL 义务”是根据 feature 开关和 FFmpeg 许可规则做的解读，不是法律意见；渲染出来的视频文件本身不属于 GPL 覆盖的对象。
- [推断] “发布周的冲劲，还不是被证明过的持续节奏”是根据发版日期集中在 2026-09-28 至 30 日、此前 beta 发布稀疏推断的；未来节奏未知。
- [未验证] Windows 支持只读了 README（FFmpeg 9 共享库、关掉编解码 feature），没有实测。
- [未验证] 2024 年 emoji 渲染是已知问题（#65，已关闭）；当前 emoji 支持情况未测试。
- [未验证] star、fork、下载量和提交数是 2026-09-30 从 GitHub 和 crates.io 读到的时点数据。
- [未验证] 雷达的采用度轴是 `?`：评分器找到几个候选包、没有一个通过它的噪声过滤；`fframes` crate 自己在 crates.io 的数字（累计 38,170、近期 1,038 次下载）写在了健康度一节，但没有回填进机器评分。
