---
name: Clash Verge Rev
slug: clash-verge-rev
repo: https://github.com/clash-verge-rev/clash-verge-rev
category: ops-infra
tags: [proxy, clash, gui, tauri, cross-platform]
language: TypeScript
license: GPL-3.0
maturity: v1.x, active, 129k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T06:25:04Z
  default_branch: dev
  default_branch_sha: 8bf5fc1aca6d565cda8f6d455a36f1f3c97974a2
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:11:42Z
  overall: B
  overall_score: 3.17
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.3
        qualifying_issues: 3
        band: relaxed_solo
        window_offset_days: 8
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 3640
        homebrew_tier: A
        release_downloads: 42286157
        release_assets: 1705
        release_tier: A
        signal_basis: homebrew+releases
    longevity:
      grade: B
      raw:
        repo_age_days: 1036
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 53
        top1_share: 0.459
        top3_share: 0.833
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# Clash Verge Rev

一款基于 Tauri 的现代化跨平台 GUI 代理客户端，运行在 Windows、macOS 和 Linux 上，内置 mihomo（Clash Meta）内核。

![Clash Verge Rev — 健康度雷达](../../../assets/health/clash-verge-rev.zh.svg)

## 何时使用

你是一位开发者或高级用户，需要在桌面端使用灵活、基于规则的代理客户端。你考虑过原版 Clash for Windows，但该项目已归档且不再维护。你管理多个代理订阅，想要一个干净、现代的 GUI 来切换订阅、编辑规则并监控流量。你需要系统级代理集成（系统代理与 TUN 模式），并希望无需命令行配置即可运行 mihomo 内核。你选择 Clash Verge Rev，因为它是 Clash Verge 项目的活跃延续，基于 Rust/Tauri 构建，提供原生桌面体验，而非基于 Electron 的替代方案。需要跨平台客户端覆盖 Windows、macOS 和 Linux，而非仅限 macOS 的方案时，选 Clash Verge Rev 而非 ClashX 或 ClashX Pro；需要更深的 Clash 生态兼容性和熟悉的规则语法，而非下一代协议灵活平台时，选 Clash Verge Rev 而非 sing-box。


## 何时不用

- **纯移动端用户**——如果你需要 iOS 或 Android 代理客户端，用 Shadowrocket 或 Surge 代替 Clash Verge Rev，因为这是一款仅限桌面端的应用。
- **简单单代理场景**——如果你只需要一个代理且从不切换规则，直接用 mihomo CLI 或 v2rayN 代替 Clash Verge Rev，因为 GUI 开销对静态配置来说没有必要。
- **企业 MDM 环境**——如果你需要宽松许可的企业部署代理客户端，用 sing-box 或 v2rayN 代替 Clash Verge Rev，因为 GPL-3.0 copyleft 可能与企业软件分发政策冲突。[未验证]
- **不熟悉代理概念的用户**——如果你需要带引导式设置的初学者友好代理，用 Surge 等商业客户端代替 Clash Verge Rev，因为该应用假设用户已了解 Clash 规则、代理组和订阅 URL。


## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| Clash for Windows | 未收录 | 原版 Windows Clash GUI（已归档）。 | 原版 Clash for Windows 已归档；Clash Verge Rev 是采用现代 Tauri 技术栈的活跃延续。 |
| ClashX / ClashX Pro | 未收录 | macOS 原生 Clash 客户端。 | ClashX 仅限 macOS；Clash Verge Rev 跨平台且 actively maintained。 |
| Shadowrocket / Surge | 未收录 | 商业代理客户端。 | Shadowrocket（iOS）和 Surge（macOS/iOS）是付费闭源应用，平台覆盖更广。 |
| sing-box | 未收录 | 下一代代理平台，带 GUI。 | sing-box 协议更灵活，但 Clash Verge Rev 对 Clash 生态的兼容性更深。 |
| Proxifier | 未收录 | 商业按应用代理路由。 | Proxifier 是用于为特定应用路由的付费工具；Clash Verge Rev 是系统级代理客户端，支持基于规则的路由。 |

## 技术栈

- **TypeScript**——前端 UI 逻辑
- **Rust**——Tauri 运行时与系统集成
- **Tauri 2**——跨平台桌面框架
- **mihomo（Clash Meta）**——内置代理内核

## 依赖

- Windows（x64/x86）、Linux（x64/arm64）或 macOS 11+（Intel/Apple Silicon）
- 无需服务器基础设施；完全在本地运行
- 可选：WebDav 用于配置备份与同步

## 运维难度

**低**。这是一款带安装包的桌面应用。主要持续任务是更新应用、更新内置内核、以及管理订阅 URL。无需服务器或网络基础设施。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 1.3 小时，基于 3 个 qualifying issues/PRs。
- **采用广度**：无法计算——unknown。
- **长青度**：Grade B——仓库已创建 1036 天。
- **治理集中度**：Grade B——前三贡献者占比 83.3%（?）。
- **许可风险**：Grade C——GPL-3.0 许可证。
## 存疑（未验证）

- [未验证] 原版 Clash 项目及其 Windows GUI 已被归档；该延续分叉的长期稳定性取决于持续的社区支持。
- [未验证] 某些司法管辖区对代理工具的监管环境可能影响项目的可用性与更新。
- [未验证] GPL-3.0 许可条款可能与企业软件分发政策冲突；企业部署前请核实。
