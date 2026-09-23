---
name: sharp
slug: sharp
repo: https://github.com/lovell/sharp
category: image-processing
tags: [media-processing, sharp, library]
language: JavaScript
license: Apache-2.0
maturity: active, ~32,428 stars (as of 2026-07)
last_verified: 2026-07-06
type: library
upstream:
  pushed_at: 2026-07-06T10:07:39Z
  default_branch: main
  default_branch_sha: 6c99758f0557607459dec23350fbf8a098c2b61d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:36:59Z
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
        last_commit_age_days: 0
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 8.9
        qualifying_issues: 18
        band: default
        window_offset_days: 12
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: sharp
        dependent_repos_count: 178353
        downloads_last_month: 335369579
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        release_downloads: 268225446
        release_assets: 628
        release_tier: A
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4782
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 12
        top1_share: 0.817
        top3_share: 0.95
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---
# sharp

High performance Node.js image processing, the fastest module to resize JPEG, PNG, WebP, AVIF and TIFF images. Uses the libvips library.

![sharp — 健康度雷达](../../../assets/health/sharp.zh.svg)

## 何时使用

你正在为一个落在 `media-processing` 分类里的任务选择开源基础设施，需要评估一个真实仓库，而不是只在对比表里看到一个名字。当 sharp 的上游描述贴合任务，并且采用现成项目比从零写胶水代码更划算时，你把它列入候选。

这个首版页面存在，是因为 sharp 在 atlas backlog 里反复作为对比候选出现。请把它当作有 intake 依据的起点：先核验上游 README 和许可证，再和下方已收录的邻近页面对照，然后再决定是否引入依赖。

## 怎么用起来

sharp 是一个 Node 包，真正处理像素的是底下的 C 库 **libvips**；sharp 把它包成一串可以链式调用的 JS 方法。`npm install` 时会自动下载适配你系统的预编译二进制，大多数 macOS / Windows / Linux 机器不需要再装别的。你做的事只有：把图片（文件路径或内存里的 Buffer）交给 `sharp()`，链式写出要做什么（缩放、转格式、旋转），最后说输出到文件还是 Buffer；解码、缩放、编码都由 sharp 完成。没有服务、没有配置，就是一个函数库。

![sharp — 主干用户故事](../../../assets/flow/sharp.zh.svg)

<!-- flow-steps:begin (generated from flows/sharp.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：安装，自动下载适配本机的预编译二进制 — `npm install sharp`
2. **你**：把图片交给 sharp：文件路径或内存 Buffer — `sharp('input.jpg')`
3. **你**：链式写出要做什么 — `.resize({ width: 200 }).jpeg({ mozjpeg: true })`
4. **你**：说明输出到哪里 — `.toFile('out.webp') / .toBuffer()`
5. **sharp**：libvips 解码原图
6. **sharp**：缩放、转换，正确处理色彩空间和透明通道
7. **sharp**：编码成目标格式，交回文件或 Buffer

**价值**：几行代码把大图转成小而适合网页的图；README 称缩放比 ImageMagick 快 4–5 倍

</details>
<!-- flow-steps:end -->

## 何时不用

- **你今天就需要一篇已经深度审过的 atlas 页面。** 在本页完成上游文档语义复核前，优先使用横向对比表里更成熟的已收录页面。
- **GitHub 元数据暴露了你的硬约束。** 如果许可证、归档状态或维护节奏是关键约束，优先选择本分类里核验更充分的替代品，而不是直接依赖 sharp。
- **你的任务需要更窄、更专门的替代品。** 如果某个现有页面的“何时不用”已经点名你的约束，应优先按那个页面选型；本页只是较宽的首版入口。
- **你承受不了上游变动或运维未知数。** 请选择 Lindy 记录更长、运维画像更清楚的已收录项目。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [ffmpeg-python](../video-audio/ffmpeg-python.zh.md) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 sharp 对照。 | sharp 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |
| [FFmpeg](../video-audio/ffmpeg.zh.md) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 sharp 对照。 | sharp 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |
| [ffsubsync](../video-audio/ffsubsync.zh.md) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 sharp 对照。 | sharp 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |
| [GStreamer](../video-audio/gstreamer.zh.md) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 sharp 对照。 | sharp 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |
| 自写集成 | 未收录 | 只有需求很小、维护成本明确低于引入 sharp 时，才自写。 | 自写能少一个依赖，但会失去上游项目、生态和本页记录的选型取舍。 |

## 技术栈

- **主要语言：** GitHub 元数据返回为 JavaScript。
- **仓库：** `lovell/sharp`。
- **项目形态：** atlas 路由暂归为 `library`；把它当稳定 API 契约前，请复核上游架构。
- **上游状态：** 默认分支 `main`，最后 push `2026-07-06T10:07:39Z`，archived 为 `false`。

## 依赖

- **运行时依赖：** 本次 intake 未穷尽核验；生产使用前请检查上游依赖清单。
- **外部服务：** 本次 intake 未穷尽核验；请确认是否需要数据库、队列、云 API、浏览器运行时、GPU 或模型供应商凭据。
- **运维输入：** 至少依赖该 GitHub 仓库及其发布和更新流程。

## 运维难度

**在重读上游文档前，按未知到中等处理。** library 形态的项目可能很容易试用，但仍需要 pin 版本并审查升级。app、service、framework 形态可能隐藏数据库、worker、存储、认证、浏览器、GPU 或云厂商要求，因此请把这个首版页面当成 intake 标记，而不是完整运维手册。

## 健康度与可持续性

- **维护快照：** 截至 2026-07-06，GitHub 返回 `archived=false`，`pushed_at=2026-07-06T10:07:39Z`。
- **采用快照：** 2026-07 约 32,428 个 GitHub stars；stars 只是有噪声的采用信号。
- **许可证快照：** GitHub API 返回 `Apache-2.0`；许可证关键时必须检查仓库内许可证文件。
- **Lindy 与治理：** 本次 intake 未完整复核。长期采用前，请继续检查组织归属、项目年龄、发布节奏和 bus factor。
- **风险信号：** 本页是从 backlog 元数据生成的首版页面。

## 存疑（未验证）

- [未验证] 这是依据 GitHub 元数据和 2026-07-06 backlog 生成的首版 intake 页面；高风险选型前，请重新阅读上游 README、文档、许可证文件和 release notes。
- [推断] 横向对比表先使用同分类已收录页面作为起点；后续语义复核应把泛化邻居替换成最接近的真实替代品。
