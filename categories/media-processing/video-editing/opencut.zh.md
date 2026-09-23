---
name: OpenCut
slug: opencut
repo: https://github.com/OpenCut-app/OpenCut
category: video-editing
tags: [video-editor, nle, capcut-alternative, typescript, rust, wasm, browser, rewrite-in-progress]
language: TypeScript
license: MIT
maturity: v0.3.0 (2026-04-15), ~89.8k stars, ground-up rewrite in progress, contributions closed, no default-branch commits in the 13 weeks to 2026-09 (as of 2026-09)
last_verified: 2026-09-19
type: app
upstream:
  pushed_at: 2026-08-10T16:38:36Z
  default_branch: main
  default_branch_sha: 400f097becba5db0fbc305d5a65348cb81c20356
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:48:29Z
  overall: B
  overall_score: 2.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 52
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 44.8
        qualifying_issues: 29
        band: relaxed_solo
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 457
        last_commit_age_days: 52
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 10
        top1_share: 0.961
        top3_share: 0.982
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
    adoption: { reason: no_package_structural }
---

# OpenCut

MIT 许可的网页、桌面与移动端视频编辑器，在开源 CapCut 替代品里社区最大——目前正在从零重写，而它 README 让你当下使用的版本在另一个已归档的 `opencut-classic` 仓库里。

![OpenCut — 健康度雷达](../../../assets/health/opencut.zh.svg)

## 何时使用

你在评估开源的 CapCut 替代品，OpenCut 是第一个跳出来的结果：89.8k star、MIT 许可、可自托管的浏览器编辑器，还有一个 Discord。star 数回答不了的问题是：它是不是你这个季度能采用的东西。

OpenCut 是一个面向网页、桌面与移动端的 TypeScript 编辑器。截至 2026-09-19，它的 README 明说项目「正在从零重写」，把编辑器 API、一等公民的第三方插件、Rust 核心、MCP server、无头模式与编辑器内脚本面板都列为「即将到来」，并声明在架构设计期间不接收外部贡献。README 让你真正拿来用的是另一个已归档的 `OpenCut-app/opencut-classic` 仓库。想跟进或基于下一代架构开发时选 OpenCut 仓库——Rust／wgpu 合成器编译到 WASM、每秒 120,000 tick 的 `MediaTime` 时间算术、v0.3.0 中描述的 GPUI 桌面壳；需要主分支当下就能安装运行的原生离线编辑器时，选 [Concat](concat.zh.md)。

## 何时不用

- **你今天就要一个能用于实际工作的编辑器。** 重写期间这个仓库不产出任何可用东西，最新 tagged 版本是 v0.3.0（2026-04-15）。要能跑的原生 beta 用 [Concat](concat.zh.md)；确实要浏览器版本、且接受它已被冻结，用已归档的 `opencut-classic`。
- **你想提 PR。** README 声明项目尚未准备好接收外部贡献；去有公开审查流程的项目贡献，或等架构宣布稳定。
- **你需要可靠的发布节奏或稳定的扩展 API。** 编辑器 API、插件系统、MCP server 与无头模式在 README 里都还是「即将到来」，而 GitHub 的提交活跃统计显示截至 2026-09-13 的 13 周内默认分支没有提交 [推断]。
- **编辑器必须在普通硬件上完全离线运行。** OpenCut 通过 WASM 合成器在浏览器里渲染，网页端经 OpenNext 部署；需要自带编解码器、不依赖浏览器的原生二进制时，用 [Concat](concat.zh.md)。
- **你只需要由代码生成、确定性的视频。** 时间线编辑器是错的层次——需要 CI 里渲染 React 组合时用 [Remotion](../../video-production/remotion.zh.md)，自己造编辑器时用 [MLT](../video-audio/mlt.zh.md)。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Concat](concat.zh.md) | ✅ | 想今天就能装上原生编辑器开剪——离线、自带 FFmpeg／Whisper、有 API／CLI／server——选 Concat；更看重社区规模、MIT 许可与规划中的插件／MCP 架构而非可运行构建时选 OpenCut，因为 OpenCut 仓库正在重写且不接受贡献。 | Concat：现在可运行、原生、AGPL、单人维护。OpenCut：宽松许可与庞大社区，当前该仓库没有可下载产物。 |
| [MLT](../video-audio/mlt.zh.md) | ✅ | 你在造编辑器而不是用编辑器时选 MLT；只想跟进架构时看 OpenCut，因为 MLT 是成熟的 LGPL 引擎、已在为落地编辑器提供动力，而 OpenCut 的重写没有公布日期。 | MLT：经证实的引擎，无界面，LGPL。OpenCut：完整应用与浏览器触达，但未发货。 |
| [Remotion](../../video-production/remotion.zh.md) | ✅ | 视频由代码批量生成且必须确定性时选 Remotion；人在时间线上交互剪辑时选 OpenCut，因为 Remotion 没有时间线界面，而 OpenCut 不是渲染框架。 | Remotion：代码定义的视频与成熟渲染器。OpenCut：面向人的交互式时间线剪辑。 |
| CapCut（字节跳动） | 未收录 | 想要打磨成熟、带云端 AI 的免费编辑器且不在意账号时选 CapCut；许可与自托管比现成打磨更重要时选 OpenCut，因为 CapCut 闭源，并把 4K 与 AI 放在 Pro 后面。 | CapCut：特效成熟、绑定云端、闭源。OpenCut：MIT 可自托管，但当前不发货。 |
| DaVinci Resolve／Premiere Pro | 未收录 | 专业剪辑师需要可跟踪遮罩、调色与成熟关键帧编辑器来完成交付时选商业 NLE；你要自建或自托管开源编辑器、而不是完成一部影片时选 OpenCut，因为商业工具闭源且不可嵌入。 | 商业 NLE：深度与稳定。OpenCut：开放许可与浏览器触达，架构仍在进行中。 |

## 技术栈

- **语言：** 网页应用是 TypeScript，时间线／合成核心是编译到 WebAssembly 的 Rust（`rust/crates/compositor`、`effects`、`masks`、`gpu`、`time`）；`apps/desktop` 是独立的 GPUI + Rust 壳，v0.3.0 称其尚处早期。
- **渲染：** v0.3.0 用编译到 WASM 的 Rust／wgpu 合成器替换了 WebGL 渲染器；时间用整数 tick（`MediaTime`，每秒 120,000 tick），帧率是 `{numerator, denominator}` 有理数类型。
- **工具链：** 用 `proto` 固定工具链、用 `moon` 跑任务（`moon run web:dev`、`api:dev`、`desktop:dev`）；网页端可经 OpenNext 部署到 Cloudflare Workers（`wrangler.jsonc`、`open-next.config.ts`）。
- **工程模型：** `SceneTracks` 用显式的 `overlay`、`main`、`audio` 字段表达轨道；截至 v0.3.0 存储迁移已到 v25。

## 依赖

- **使用托管版编辑器：** 支持 GPU 加速的现代浏览器；检测不到 GPU 渲染时 OpenCut 会给出提示。
- **自行构建或自托管：** 由 `proto` 管理的 Node.js 工具链（`.prototools`）加 Moon 跑任务、用于合成器的 Rust 到 WASM 工具链，以及可选的 Cloudflare Workers 账号用于 OpenNext 部署。
- **桌面壳：** 带 GPUI 的 Rust 工具链；`apps/desktop` 被描述为只有构建脚手架、尚无功能。
- 运行浏览器编辑器不需要数据库或服务端组件；classic 版本把工程存在浏览器里。

## 运维难度

**中。** 用托管产品无需安装，但你从这个仓库采用的是一套要自己构建的 monorepo：`proto use`，然后 `moon run web:dev`／`api:dev`／`desktop:dev`，合成器还要 Rust 到 WASM 工具链，桌面端另有独立构建路径。自托管到 Cloudflare Workers 有文档但很年轻。更大的运维风险不在搭建成本，而在项目状态：没有可跟随的发布节奏、贡献通道关闭，README 把真要用的场景都导向已归档的 classic 构建。

## 健康度与可持续性

- **维护（2026-09）：** 默认分支已停滞。GitHub 提交活跃统计显示截至 2026-09-13 的 13 周内没有提交，最近一次 push 是 2026-08-10，最新 tagged 版本是 2026-04-15 的 v0.3.0。
- **治理／bus factor：** 组织所有（`OpenCut-app`），赞助方包括 fal.ai，但高度集中——榜首贡献者（`mazeincoding`）有 1,058 次提交，第二名 71 次；重写期间有意关闭外部贡献。
- **背书与 Lindy——关注度大，当前无产出。** 创建于 2025-06-22，约 15 个月大，89.8k star 与 8.9k fork；采用是真的，但「年龄 × 仍活跃」里「仍活跃」这一半当下不成立。
- **采用与生态：** 这是该细分领域最大的社区——Discord、378 个未关 issue、一个托管服务。注意托管服务跑的是已归档的 classic 构建，而不是本仓库的成果。
- **风险信号：** MIT 许可，未发现 CLA 或改许可历史，所以许可不是风险；风险是重写陷阱——`opencut-classic` 被拆出并归档（最近 push 2026-05-17），而重写没有公布日期，于是一个极受欢迎的仓库可以长期处于「什么都下载不到」的状态。

## 存疑（未验证）

- [未验证] 记录的最近 push（2026-08-10）之后开发是否恢复；仓库状态检查于 2026-09-19。
- [未验证] v0.3.0 的发布说明描述了 Rust／wgpu WASM 合成器、`MediaTime` 与 GPUI 桌面壳；本页未做构建验证。
- [推断] 89.8k star 是拆分前项目的遗产：拆出的 `opencut-classic` 只有 251 star，这暗示本仓库保留了原始历史与受众。
- [未验证] opencut.app 仍在提供 classic 版本，这一说法来自本仓库 README，并非检查过部署。
- [未验证] star、fork 与 issue 数（89,808／8,871／378 个未关）是 2026-09-19 的 GitHub 时点数据。
- [推断] 「13 周无提交」读自 GitHub 的 commit-activity 端点，该端点可能滞后或排除非默认分支的工作；`pushed_at` 为 2026-08-10。
