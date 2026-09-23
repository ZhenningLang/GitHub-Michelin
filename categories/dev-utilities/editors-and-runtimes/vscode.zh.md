---
name: VS Code
slug: vscode
repo: https://github.com/microsoft/vscode
category: editors-and-runtimes
tags: [code-editor, ide, electron, extensible, microsoft]
language: TypeScript
license: MIT
maturity: v1.x, active, 187k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-06T09:10:38Z
  default_branch: main
  default_branch_sha: 25d59f147995cbc2647f4d3d28a726fa0ed590c3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:11:13Z
  overall: A
  overall_score: 3.8
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: "@theia/vscode-builtin-vb"
        dependent_repos_count: 1
        downloads_last_month: 2136
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        homebrew_installs_90d: 1097
        homebrew_tier: B
        release_downloads: 798
        release_assets: 3
        release_tier: D
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 4037
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 142
        top1_share: 0.113
        top3_share: 0.21
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
---

# VS Code

Visual Studio Code——一款轻量但强大的代码编辑器，兼具编辑器的简洁与 IDE 的能力，基于 Electron 构建，可通过丰富的扩展市场进行扩展，拥有数以万计的扩展。

![VS Code — 健康度雷达](../../../assets/health/vscode.zh.svg)

## 何时使用

你是一位开发者，需要一款快速、跨平台的代码编辑器，开箱即支持数十种语言，并具备智能代码补全、调试与 Git 集成。你想要一款能随需求成长的编辑器——从简单的 Markdown 与配置文件文本编辑器，到搭配扩展后成为 TypeScript、Python 或 Rust 的完整 IDE。你需要在 macOS、Windows 和 Linux 上都能使用，且快捷键与设置可跨机器同步。选择 VS Code 而不是 Zed，因为 VS Code 拥有最大的扩展市场与最深的生态；选择 VS Code 而不是 IntelliJ IDEA，因为 VS Code 更轻、语言无关且所有功能免费。决定取舍：无与伦比的生态广度，加上跨平台一致性，却没有完整 IDE 的重量。

## 何时不用

- 如果你想要完全开源、无品牌烙印且无遥测的构建，请用 VSCodium 或“Code - OSS”而不用 VS Code，因为微软分发的 VS Code 包含专有遥测和专有扩展市场。
- 如果你需要纯终端编辑器，请用 Neovim 或 Vim 而不用 VS Code，因为 VS Code 是 GUI 应用，无法在终端运行。
- 如果你需要绝对最快的编辑器且内存占用最小，请用 Zed 或 Sublime Text 而不用 VS Code，因为基于 Electron 的应用比原生编辑器内存占用更高、启动更慢。
- 如果你需要深度集成的 JetBrains 风格 IDE 来做重度 JVM 或 Android 工作，请用 IntelliJ IDEA 而不用 VS Code，因为 IntelliJ 提供了比 VS Code 扩展更深的语言专用工具链、重构和构建系统集成。
- 如果你想要完全 MIT 许可的分发版且没有专有扩展，请用 VSCodium 而不用 VS Code，因为微软产品许可适用于分发的 VS Code 二进制文件，且部分热门扩展是专有的。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Zed](zed.zh.md) | ✅ | 高性能原生代码编辑器，支持多人协作。 | Zed 更快、Rust 原生，但生态更小；VS Code 拥有最大的扩展市场。 |
| Sublime Text | 未收录 | 快速、轻量的专有编辑器。 | Sublime 更快更轻，但专有且收费；VS Code 免费开源。 |
| Neovim | 未收录 | 带现代 Lua 配置的模态终端编辑器。 | Neovim 仅限终端，学习曲线陡峭；VS Code 以 GUI 优先，对新手友好。 |
| IntelliJ IDEA | 未收录 | 面向 JVM 和 Android 的深度语言专用 IDE。 | IntelliJ 更重、聚焦 JVM；VS Code 更轻、语言无关。 |
| VSCodium | 未收录 | 移除微软遥测的完全开源 VS Code 构建。 | VSCodium 去掉了遥测，但缺少微软扩展市场及部分专有功能。 |

## 技术栈

- **TypeScript**——编辑器核心与扩展的主要语言
- **Electron**——桌面外壳与跨平台运行时
- **Monaco Editor**——底层编辑器组件（也用于 Azure DevOps 与 GitHub）
- **Node.js**——扩展主机运行时

## 依赖

- 现代桌面操作系统（macOS、Windows、Linux）
- 充足内存（最低 8GB，大项目推荐 16GB）
- 支持 Electron 的图形栈（绝大多数现代桌面）

## 运维难度

**终端用户无运维负担**。VS Code 是消费级桌面应用——安装与更新由内置更新器或操作系统包管理器处理。对组织而言，主要关注点是管理扩展、设置同步与遥测策略。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：无法计算——no_traffic。
- **采用广度**：Grade B——npmjs.org 上月下载量 2,136（包名：@theia/vscode-builtin-vb）。
- **长青度**：Grade A——仓库已创建 4037 天。
- **治理集中度**：Grade A——前三贡献者占比 21.0%（过去 12 个月内 142 位活跃维护者）。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [未验证] 分发版 VS Code 二进制文件附带的微软产品许可可能包含超出源代码仓库 MIT 许可的条款。
- [未验证] 扩展市场中部分热门扩展是专有的，或自带独立许可条款。
- [推断] 随着微软集成更多 AI 功能（Copilot），未来 VS Code 版本可能越来越倾向于推动微软付费服务。
