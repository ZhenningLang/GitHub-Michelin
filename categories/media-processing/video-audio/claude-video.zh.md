---
name: claude-video
slug: claude-video
repo: https://github.com/bradautomates/claude-video
category: video-audio
tags: [video-audio, video-understanding, agent-skill, app]
language: Python
license: MIT
maturity: active, ~8,688 stars (as of 2026-07)
last_verified: 2026-07-16
type: app
upstream:
  pushed_at: 2026-07-01T01:26:49Z
  default_branch: main
  default_branch_sha: 83da59fa78c3eee9e20f515fe75c438bb5166efd
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:38:05Z
  overall: C
  overall_score: 2.17
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
        last_commit_age_days: 84
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 220.5
        qualifying_issues: 23
        band: relaxed_solo
        window_offset_days: 4
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 20475
        release_assets: 5
        release_tier: D
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 151
        last_commit_age_days: 84
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
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
# claude-video

Give Claude the ability to watch any video. /watch downloads, extracts frames, transcribes, hands it all to Claude.

![claude-video — 健康度雷达](../../../assets/health/claude-video.zh.svg)

## 何时使用

你需要 agent 回答关于视频的问题，而不是生成或剪辑视频。Claude / Codex / Cursor 需要拿到视频 URL 或本地文件，抽帧、获取字幕或转录，并把视觉 / 音频证据交给模型来回答时，选 claude-video。

它适合分析发布视频、总结课程、从屏幕录制诊断 bug、把 playlist 变成笔记，或询问“2:30 发生了什么”。上游 `/watch` 命令封装了 `yt-dlp`、`ffmpeg`、字幕提取、可选 Whisper fallback、frame budget、去重，以及 skill / plugin 安装路径。

## 何时不用

- **你需要视频生成、剪辑、转码或生产流水线。** 用 [MoviePy](moviepy.zh.md)、[FFmpeg](ffmpeg.zh.md)、[MLT](mlt.zh.md) 或视频生产工具；claude-video 是视频理解 helper。
- **你只需要纯转录。** 画面不重要时，[OpenAI Whisper](whisper.zh.md)、原生字幕或专用 ASR pipeline 更简单。
- **你不能运行 shell 工具或安装 `yt-dlp` / `ffmpeg`。** 工作流依赖本地命令执行；claude.ai web 也需要启用 code execution / file creation。
- **视频源禁止下载或权限不清。** `yt-dlp` 支持不等于你拥有访问、下载或再分发权限。
- **你要对长视频全程做密集视觉回忆。** capped modes 会稀疏覆盖；上游建议用 `--start` / `--end` 聚焦重跑，或用成本更高的 uncapped `token-burner`。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [FFmpeg](ffmpeg.zh.md) | ✅ | 需要底层解码、转码、滤镜控制时选 FFmpeg。 | FFmpeg 是引擎；claude-video 把媒体提取包装成 agent 可用的视频理解流程。 |
| [OpenAI Whisper](whisper.zh.md) | ✅ | 任务只有 speech-to-text 时选 Whisper。 | Whisper 处理音频文字；claude-video 把 transcript、frames 和 agent prompt 组合起来。 |
| [MoviePy](moviepy.zh.md) | ✅ | 需要程序化剪辑 / 合成时选 MoviePy。 | MoviePy 产出编辑后的视频；claude-video 读取视频做分析。 |
| 自写 yt-dlp + ffmpeg 脚本 | 未收录 | 不需要 agent skill packaging，只要固定 ingestion pipeline 时自写。 | 自写脚本更小、更确定；claude-video 已处理 agent-facing UX 和 frame budget。 |


## 技术栈

- **Python skill runtime**——`skills/watch/scripts/` 包含媒体编排代码。
- **Agent packaging**——上游包含 Claude Code plugin metadata、Codex / Agent Skills plugin manifests、`skills/watch/SKILL.md` 和 `.skill` bundle 构建脚本。
- **Media pipeline**——`yt-dlp` 下载 / 提取字幕，`ffmpeg` 抽帧 / 抽音频，可选 Whisper backend 转录无字幕音频。

## 依赖

- **本地 shell 执行**，用于 `yt-dlp`、`ffmpeg`、Python 脚本和临时工作目录。
- **可选 Whisper API key**——上游偏好 Groq `whisper-large-v3`，OpenAI `whisper-1` 是替代；很多公开视频可用原生字幕避免付费转录。
- **Agent image-reading context**——抽出的 frames 会进 Claude / agent 上下文，所以成本和 context budget 随帧数、分辨率增长。
- **平台 package manager**——首次 setup 可能在 macOS 调 Homebrew，或在 Linux / Windows 打印安装命令。

## 运维难度

**个人使用低，团队工作流中等。** plugin / skills 安装不复杂，但团队稳定使用需要 PATH / 工具安装、API key 处理、临时文件清理、frame / image token 成本控制，以及视频源权限策略。


## 健康度与可持续性

- **维护快照（2026-07-16）：** GitHub 返回 `archived=false`，`pushed_at=2026-07-01T01:26:49Z`；health 将 maintenance 评为 B、responsiveness 评为 B。
- **采用快照：** 2026-07 约 8,688 个 GitHub stars；作为年轻 repo 关注度很强，但 health scorer 没有可用的 package-download 轴。
- **许可证快照：** 已人工核验根目录 `LICENSE` 为 MIT；当前 health block 将 `risk_license` 评为 `A`，与人工核验一致。
- **Lindy / 治理：** 项目很年轻，health 中 longevity 为 D；治理因单维护者集中为 D。
- **风险信号：** 依赖第三方视频源行为、本地媒体工具、可选转录供应商和多模态 token 成本。

## 存疑（未验证）

- [未验证] README 中的 extraction timing benchmark 本次没有本地复现。
- [未验证] URL 支持依赖 `yt-dlp` 和源站行为，后者可能变化。
- [推断] 它更适合 agent-assisted video understanding；如果主需求是确定性的媒体 ingestion / storage pipeline，自写管线可能更合适。
