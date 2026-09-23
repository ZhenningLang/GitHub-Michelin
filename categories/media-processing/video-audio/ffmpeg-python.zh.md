---
name: ffmpeg-python
slug: ffmpeg-python
repo: https://github.com/kkroening/ffmpeg-python
category: video-audio
tags: [ffmpeg, python, bindings, filter-graph, video, audio, transcoding]
language: Python
license: Apache-2.0
maturity: v0.2.x, last commit 2024-08 (coasting), 11k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2024-08-04T00:07:08Z
  default_branch: master
  default_branch_sha: df129c7ba30aaa9ffffb81a48f53aa7253b0b4e6
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:38:14Z
  overall: C
  overall_score: 2.0
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1534
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: ffmpeg-python
        dependent_repos_count: 5000
        downloads_last_month: 7960226
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.05
        tier_source: registry
    longevity:
      grade: E
      raw:
        repo_age_days: 3418
        last_commit_age_days: 1534
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# ffmpeg-python

FFmpeg 的 Python 绑定，让你把复杂的滤镜图写成链式 Python 表达式，而不必手搓 `-filter_complex` 字符串——它替你拼出 FFmpeg 命令行，再去调用 `ffmpeg` 二进制。

![ffmpeg-python — 健康度雷达](../../../assets/health/ffmpeg-python.zh.svg)

## 何时使用

你是做媒体处理的 Python 开发者——裁剪片段、叠水印、拼接、归一化音频——并撞上了那堵墙：FFmpeg 的 `-filter_complex` 语法变成了只写不可读的噪声。你想把脑子里那张“先 trim 再 concat 再 overlay”的图写成可读、可逐步搭建、可分支、可复用的代码。你 `pip install ffmpeg-python`，写 `ffmpeg.input('in.mp4').hflip().output('out.mp4').run()`，或拼一个真正的 DAG：`concat(in.trim(...), in.trim(...)).overlay(overlay.hflip()).drawbox(...).output(...).run()`。库把这张节点图转成那串难搞的 `-filter_complex` 调用并执行，于是你留在 Python 里，把滤镜逻辑纳入版本控制、可测试，而不是粘进 shell 字符串。

它的最佳场景正是*复杂*滤镜图——README 的整个卖点就是别的 wrapper 能处理简单情形却缺乏复杂滤镜支持。如果你在用 Python 编排非平凡的转码/合成管线、且已懂 FFmpeg 的概念，这就是顺手的前端。[推断]

## 何时不用

- **你没装也不想装 FFmpeg。** 这是个*薄封装、靠外部进程执行*的库——它要求系统上有 `ffmpeg` 二进制；它自己不做任何编码。
- **你不在 Python 里。** 它是 Python 专用；从别的语言你会直接调 FFmpeg 或用那门语言的绑定。
- **你需要进程内的帧访问 / 解码。** 它为 FFmpeg CLI 拼命令行；要按帧拿 numpy，你应改用 PyAV（libav 绑定）或 OpenCV。[未验证]
- **你需要一个长期有维护的依赖。** 项目正**吃老本**——最后提交 2024-08，open issue 积压很大（约 525）；关键管线要把上游修复慢这件事算进去。[推断]
- **简单的一次性转换。** 如果你只需要 `ffmpeg -i a.mp4 b.mp4`，一个 `subprocess` 调用（或一个小辅助函数）比一个建图的库少不少活动部件。
- **你想要 FFmpeg 版本/功能的抽象层。** 它把你的图交给系统里装的那个 `ffmpeg`；滤镜的可用性/行为是二进制的，所以它不会替你屏蔽 FFmpeg 的版本差异。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FFmpeg](ffmpeg.zh.md)（CLI 本身） | ✅ | 需要底层引擎，且能直接管理 filtergraph 字符串时，选 FFmpeg 本身。 | 底层引擎；能力最大、是权威参照，但复杂图的 `-filter_complex` 字符串不可读——这正是本库要包的东西。 |
| [PyAV](pyav.zh.md) | ✅ | 需要对 libav* 库的 Pythonic 绑定时，选 PyAV。 | 对 libav* 库的 Pythonic 绑定——进程内解/编码与按帧访问，不靠外部进程；安装更重、比建 CLI 图更底层。 |
| [MoviePy](moviepy.zh.md) | ✅ | 需要更高层 Python 视频编辑、特效、合成、文字和友好 API 时，选 MoviePy。 | 更高层的 Python 视频编辑（特效、合成、文字），API 更友好；适合剪辑，不太是对 FFmpeg 图的薄映射。 |
| subprocess + 裸 ffmpeg | 未收录 | 需要零依赖和完全可控时，选 subprocess + 裸 ffmpeg。 | 零依赖、完全可控，但 `-filter_complex` 字符串得你自己拼和转义——这正是本库消除的痛。 |
| imageio-ffmpeg / fluent-ffmpeg | 未收录 | 需要其他语言或更窄范围的 FFmpeg 封装时，选 imageio-ffmpeg 或 fluent-ffmpeg。 | 别的语言或更窄范围的 FFmpeg 封装（Node 的 fluent-ffmpeg、Python imageio 垫片）；同为外部进程模型，体验不同。 |

## 技术栈

- **语言：** 纯 Python；无编译扩展——它生成命令行参数并用 `subprocess` 调起 FFmpeg。
- **核心思路：** 一个节点图/DAG 构造器，`input`/滤镜/`output` 节点链式（fluent 或函数式）连接，编译成一条 `-filter_complex` 命令行。
- **接口面：** 与 FFmpeg 滤镜对应的滤镜函数，加上 `.run()`、`.compile()`（查看参数）和 async/overwrite/quiet 等选项。

## 依赖

- **运行时：** Python，加上装好且在 PATH 上的 **FFmpeg 二进制**——硬性外部依赖；没有它库就没用。
- **Python 依赖：** 极少（历史上有 `future` 用于 Py2/3）；经 `pip install ffmpeg-python` 安装。
- **无服务/数据库：** 它是驱动本地进程的客户端库；媒体文件和 FFmpeg 安装由你自备。

## 运维难度

**库本身低，FFmpeg“看情况”。** 安装和使用 `ffmpeg-python` 很简单（`pip install`）。运维分量在 FFmpeg 本身：在各环境里准备好二进制（及你需要的编解码器/授权）、锁版本以让滤镜行为可复现，以及实际转码的 CPU/GPU 成本。这个 wrapper 不引入运行时基础设施，但也不给你任何对 FFmpeg 版本/编解码差异的隔离——排查一次失败的运行往往是读生成的命令行（`.compile()`）再对着你的 FFmpeg 复现。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** **吃老本。** 最后提交 2024-08（停滞约 2 年），open issue 积压很大（约 525）——未归档、未死，但显然不在被主动推进。当作功能冻结看待。[推断]
- **治理 / bus factor。** 单维护者（`kkroening`）的 `User` 仓库。一个单作者、正停滞的库拿 11k star，是个 **bus-factor 标记**：流行且有用，但背后没有团队或组织。高 open issue 数加上提交缓慢更印证了这点。
- **年龄与 Lindy 判断。** 2017-05 创建，约 9 岁；API *稳定且久经验证*（它只是包 FFmpeg 的命令拼装，这部分变化不大），所以即便停滞仍可用——但“老 + 吃老本”是弱 Lindy，而非强。[推断]
- **采用与生态。** 用得非常广（11k star，常见于教程/StackOverflow 回答）；对简单到中等的图它实际上是社区标准，这缓冲了维护缓慢。[推断]
- **风险标记。** 维护速度是主要一项——open PR/issue 滞留，别指望快速修复；还有隐含的 FFmpeg 版本耦合（wrapper 不会替你挡）。Apache-2.0 许可宽松且清晰（已从仓库核实）。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 11k star / 946 fork、约 525 个 open issue；计数对时间敏感，issue 数更多反映积压而非危险。
- [未验证] 本轮 API 未返回 GitHub tagged release；tag（`v0.2.x`）在 PyPI 上存在——锁版本前应对照 PyPI 确认具体版本。
- [推断] “吃老本 / 功能冻结”是从 2024-08 最后提交日期加 open issue 积压推断的，并非维护者声明。
- [未验证] 确切的滤镜覆盖、async 支持和 Python 版本下限取自 README/一般认知，未重读 manifest。
- [未验证] 与 PyAV/MoviePy 的能力对比取自对生态的一般认知，本轮未再核验。
