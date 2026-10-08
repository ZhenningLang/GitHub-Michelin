---
name: MoviePy
slug: moviepy
repo: https://github.com/Zulko/moviepy
category: editing-and-cutting
tags: [video, python, editing, compositing, ffmpeg, effects, text, animation]
language: Python
license: MIT
maturity: v2.2.1 (2025-05-21), maintained at low cadence, ~15k stars (as of 2026-10)
last_verified: 2026-10-08
type: library
upstream:
  pushed_at: 2026-08-26T06:17:08Z
  default_branch: master
  default_branch_sha: 211e4b15f6ce4f34a6a9efbfff40590e43a68f77
  archived: false
health:
  schema: 1
  computed_at: 2026-10-08T08:22:22Z
  overall: B
  overall_score: 3.17
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
        last_commit_age_days: 43
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 228.3
        qualifying_issues: 10
        band: default
        window_offset_days: 2
        source: pr
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: moviepy
        dependent_repos_count: 5431
        downloads_last_month: 4336274
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4805
        last_commit_age_days: 43
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.5
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
---

# MoviePy


你要把 200 段素材各截一段、打上标题、再拼成几个版本，FFmpeg 的 `-filter_complex` 写到第三层叠加就没人看得懂了。MoviePy 让你用普通的 Python 对象写这段剪辑——片段、截取、叠加、导出——读帧和编码交给它背后的 FFmpeg。


![MoviePy — health radar](../../../../assets/health/moviepy.zh.svg)

## 何时使用

你是数据科学家或内容自动化工程师，手里一文件夹录像，外加一张表写着要做什么：“每段保留 00:10–00:20，音量降到 80%，正中间打上讲者名字，输出 `result.mp4`”。用裸 FFmpeg，每个文件都是一串 `-ss 10 -t 10 -i … -filter_complex "[0:v]drawtext=…[v];[0:a]volume=0.8[a]" -map "[v]" -map "[a]"`，等第二次要加交叉淡化时，团队里已经没人读得懂这条命令。你 `pip install moviepy`，写 `VideoFileClip("in.mp4").subclipped(10, 20).with_volume_scaled(0.8)`，用 `CompositeVideoClip` 叠一层 `TextClip`，再在循环里调 `write_videofile`。每一帧都是 NumPy 数组，所以自定义特效就是几行 Python，不用去 FFmpeg 手册里找滤镜。

当你写的是一次“剪辑”（片段、图层、时间点、转场），而不是滤镜图或逐包解码循环时，选它而不是 ffmpeg-python 或 PyAV；当整条管线本来就在 Python 里时，选它而不是 Remotion。代价是速度：MoviePy 会把每一帧解码进 Python 再重新编码，一旦瓶颈变成吞吐量而不是写代码的时间，它就不对了。

## 怎么用起来

MoviePy 把媒体变成 Python 对象。打开文件时，它启动一个 FFmpeg 进程，把原始帧（未压缩的像素网格）经管道流进 NumPy 数组，于是每个像素都能在代码里摸到。片段是“惰性配方”：`subclipped`、`with_volume_scaled`、`with_position`、`with_effects` 都返回一个新片段，只记录“第 t 秒那一帧该怎么算出来”，此刻什么都不计算。调用 `write_videofile` 时，MoviePy 沿时间线逐帧走一遍，向 `CompositeVideoClip` 的每一层要像素、叠好，再经管道送进第二个 FFmpeg 进程编码成文件——像描图台上每一帧都重新手描一遍。你决定剪什么（哪些片段、哪几秒、哪些图层和特效）；MoviePy 负责帧时序、合成、混音和 FFmpeg 那一套管道。FFmpeg 本身由 `imageio-ffmpeg` 在首次使用时下载，常规用法不用再装别的。

![moviepy — 主干用户故事](../../../../assets/flow/moviepy.zh.svg)

<!-- flow-steps:begin (generated from flows/moviepy.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：装上库，FFmpeg 二进制首次使用时自动下载 — `pip install moviepy`
2. **你**：打开素材，写下要截哪段、音量怎么调 — `VideoFileClip("in.mp4").subclipped(10, 20).with_volume_scaled(0.8)`
3. **你**：用 TextClip 做标题，叠到片段上 — `CompositeVideoClip([clip, txt_clip])`
4. **你**：指定输出文件 — `final_video.write_videofile("result.mp4")`
5. **MoviePy**：从 FFmpeg 把源帧流进 NumPy 数组，只取剪辑用到的那几秒 — 组件：`FFMPEG_VideoReader`
6. **MoviePy**：逐帧按时间 t 合成各图层，同时混好音频 — 组件：`CompositeVideoClip`
7. **MoviePy**：把帧经管道送进 FFmpeg 编码，写出文件 — 组件：`FFMPEG_VideoWriter`

**价值**：多图层剪辑写成可读的 Python，能对几百个文件循环跑，不用手写滤镜图

</details>
<!-- flow-steps:end -->

## 何时不用

- **⚠ 维护处于滑行状态（截至 2026-10）。** 最新发布是 2025-05-21 的 v2.2.1；2025 年 9 月以来默认分支只进了文档修正，README 里自己挂着“Maintainers wanted!”。没有被弃——仍有 issue 进来、偶尔有人回——但如果你需要 bug 按期修好，改用更贴近 FFmpeg、自身代码更少的 [PyAV](../transcoding-and-pipelines/pyav.zh.md) 或 [ffmpeg-python](../transcoding-and-pipelines/ffmpeg-python.zh.md)。
- **只要截取或拼接、不想重编码。** MoviePy 永远解码再重编码，对单纯裁剪来说又慢又有损。改用 [FFmpeg](../transcoding-and-pipelines/ffmpeg.zh.md) 的流复制（`-c copy`）。
- **吞吐量比写代码的时间更重要。** 每帧都经过 Python，按 README 的原话，比直接用 FFmpeg 慢。长片或高分辨率素材的批量转码，用 FFmpeg 或 [HandBrake](../transcoding-and-pipelines/handbrake.zh.md)。
- **直播或低延迟媒体。** MoviePy 只做文件进、文件出。摄像头流、RTSP/WebRTC 或任何要持续运行的场景，用 [GStreamer](../transcoding-and-pipelines/gstreamer.zh.md)。
- **你的代码、教程或大模型生成的片段是 MoviePy 1.x 写法。** v2.0 破坏了 API：`moviepy.editor` 没了，`subclip` 改成 `subclipped`，`clip.fx(...)` 改成 `with_effects([...])`，而 v1 已不再维护。按上游“updating to v2”指南预留迁移工作量，而不是锁死 `moviepy<2`。
- **你要时间线剪辑器或图形界面。** MoviePy 没有工程文件、没有边预览边剪、没有撤销。要真正的非线性剪辑，用 [MLT](mlt.zh.md) / Shotcut。
- **技术栈是 Web/React，视频本质是模板化界面。** 用把 React 组件渲染成视频的 [Remotion](../../../video-production/remotion.zh.md)，别在 Python 里重搭版式。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FFmpeg](../transcoding-and-pipelines/ffmpeg.zh.md) | ✅ | 一条命令能表达的裁剪、拼接、转码，直接用 FFmpeg；只有当剪辑带图层和时间点、以后还要回头读时，才换 MoviePy。 | 最快，还能流复制不损画质；代价是滤镜图语法，叠加超过几层就难以维护。 |
| [ffmpeg-python](../transcoding-and-pipelines/ffmpeg-python.zh.md) | ✅ | 想要 FFmpeg 的速度、又想从 Python 生成命令，选 ffmpeg-python；需要逐帧 Python 特效或片段/图层模型时选 MoviePy。 | 帧不进 Python，所以快；但你仍然在用 FFmpeg 滤镜思考，而不是片段。 |
| [PyAV](../transcoding-and-pipelines/pyav.zh.md) | ✅ | 要在单进程里自定义解码/编码循环或按包控制，选 PyAV；想要合成和文字、又不想自己写循环，选 MoviePy。 | 进程内 libav 绑定、不起子进程；更底层，剪辑概念得自己搭。 |
| [Remotion](../../../video-production/remotion.zh.md) | ✅ | 视频是设计出来的版式（图表、字幕、品牌模板）且团队写 React，选 Remotion；管线和数据在 Python、输入是现成素材，留在 MoviePy。 | Web 级排版和预览工具；多出 Node、无头浏览器，以及面向公司的单独许可条款。 |
| [MLT](mlt.zh.md) / Shotcut | 部分已收录 | 由人在多轨时间线上剪，选 MLT/Shotcut；每条视频都不该有人手动碰时，选 MoviePy。 | 真正的非线性剪辑引擎，有工程文件；更重，也不是为“用 Python 代码写剪辑”设计的。 |
| OpenCV | 未收录 | 帧是计算机视觉的输入时用 OpenCV；产出是一段剪好的视频时用 MoviePy。 | 逐帧图像处理很强；没有片段、音频、图层、转场的概念。 |

## 技术栈

- **语言：** Python ≥ 3.9（见 `pyproject.toml`）。
- **核心思路：** 片段是惰性对象（`VideoFileClip`、`ImageClip`、`TextClip`、`CompositeVideoClip`、`AudioFileClip`），帧是 NumPy 数组；v2 用效果对象加 `with_effects` 取代了 v1 的函数式特效。
- **I/O：** FFmpeg 子进程以原始视频格式经管道读帧，输出也同样经管道编码；`ffplay` 只用于预览。
- **图像处理：** v2.2.1 发布版用 Pillow 渲染文字和处理图像；默认分支在 2025-08 合入了重新引入 `opencv-python-headless` 的改动，用于加速缩放/旋转，尚未进入正式发布版。

## 依赖

- **Python 包（v2.2.1）：** `numpy`、`pillow`（`<12.0`）、`imageio`、`imageio_ffmpeg`、`decorator`、`proglog`、`python-dotenv`。默认分支另加 `opencv-python-headless`。
- **FFmpeg：** 首次使用时由 `imageio-ffmpeg` 自动下载；要用自己的版本，设 `FFMPEG_BINARY`（环境变量或 `.env`）。v2.0 起不再使用 ImageMagick。
- **字体：** `TextClip` 要传字体文件路径（如 `font="Arial.ttf"`），所以渲染机器上必须真有这个字体。
- **无服务、无数据库。** 客户端库；只吃 CPU 和输出所需的磁盘。

## 运维难度

**低。** 一般 `pip install moviepy` 就装完了，因为 FFmpeg 二进制会随之下载。实际踩坑在这些地方：渲染耗时（每帧过 Python，长视频受 CPU 限制）、高分辨率多图层合成时的内存、开发机上有而容器里没有的字体，以及照搬旧示例时撞上的 v1→v2 API 断裂。没有服务器、守护进程或状态要维护。

## 健康度与可持续性

- **维护（2026-10）。** 滑行。最新发布是 v2.2.1（2025-05-21）；默认分支最近的提交是文档修正（2026-07、2026-08），2025 年 10 月以来只合并了两个 PR。雷达上维护 B、响应 C（首次响应中位数 228.3 小时，约 9.5 天）与此一致。
- **治理 / bus factor。** 仓库挂在原作者 Zulko 的个人账号下；README 列了四位活跃维护者，并公开求助。雷达统计过去 12 个月只有 2 位活跃维护者（治理 C），项目依赖一个很小的志愿者群体。
- **年龄与 Lindy。** 2013 年创建，约 13 岁，2024 年落地了一次大的 v2 重写——长寿 A。“老且仍活着”给出中等 Lindy 先验；维护者梯队太薄，是它算不上强信号的原因。
- **采用。** 非常高：PyPI 上月下载量 4,336,274、依赖仓库 5,431 个（采用 A），外加大量教程。采用量大让它不太可能突然消失，但换不来更快的修复。
- **风险标记。** MIT，无改许可历史（风险/许可 A）。真正的风险是 v1→v2 断裂导致网上示例分裂，以及遇到 bug 时上游响应慢。

## 存疑（未验证）

- [未验证] 截至 2026-10-08 约 15k star、约 2.1k fork；数字易变、对日期敏感。
- [推断] “滑行”是从提交历史、发布日期和 README 的求维护者声明读出来的，不是维护者对项目前景的表态。
- [未验证] OpenCV 带来的加速幅度（缩放/旋转“最多 10 倍”）是该 PR 作者的说法，本页未做基准测试，且尚未进入正式发布版。
- [推断] “永远重编码”是由架构推出的（帧经过 NumPy 再送进编码器）；本页读过的文档里没找到无损直通模式。
