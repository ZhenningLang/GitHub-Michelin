---
name: RustDesk
slug: rustdesk
repo: https://github.com/rustdesk/rustdesk
category: ops-infra
tags: [remote-desktop, self-hosted, rust, p2p, cross-platform, flutter, remote-control]
language: Rust
license: AGPL-3.0
maturity: active, ~117.4k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T09:05:11Z
  default_branch: master
  default_branch_sha: 28930c04635ffbc487175b2b0d62e64fd40ba892
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:13:57Z
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 2.9
        qualifying_issues: 9
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 7952
        homebrew_tier: A
        release_downloads: 73098075
        release_assets: 735
        release_tier: A
        signal_basis: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 2185
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 135
        top1_share: 0.255
        top3_share: 0.563
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

# RustDesk

一款开源远程桌面应用，专为自托管设计，作为 TeamViewer 和 AnyDesk 的替代方案——用 Rust 构建，Flutter UI，支持 P2P 连接和自建中继服务器。

![RustDesk — 健康度雷达](../../../assets/health/rustdesk.zh.svg)

## 何时使用

你是开发者或系统管理员，需要远程访问自己的机器——家里服务器、办公室工作站或家人的 PC——并且你想拥有基础设施，而非租用。你选 RustDesk 而不选 TeamViewer 或 AnyDesk，是因为你不愿支付订阅费，也不想把屏幕数据经过不可控的第三方云端。你选它而不选 Chrome Remote Desktop，是因为你需要自托管选项，而非被锁定在 Google 账户里。你选它而不选 TightVNC 或 TigerVNC，是因为你需要现代加密、NAT 穿透和开箱即用的移动端客户端，而非局域网里的原始 VNC 协议。你在两端装上 RustDesk，可选地在一台 VPS 上搭一个小中继服务器，然后端到端加密直连。它支持 Windows、macOS、Linux、Android 和 iOS，支持文件传输、剪贴板同步和多显示器，Flutter UI 在每个平台都有原生感。

## 何时不用

- 如果你需要企业级支持、SLA 或合规认证，请用 TeamViewer 或 AnyDesk 企业版，而不用 RustDesk，因为 RustDesk 是社区驱动项目，没有正式支持合同、保障响应时间或合规文档。
- 如果你想要完全云端托管、零配置的解决方案，请用 Chrome Remote Desktop 或 TeamViewer，而不用 RustDesk，因为 RustDesk 的核心价值是自托管；如果你只想装完就忘，管理中继服务器是额外的负担。
- 如果你需要高级会话录制、审计日志或细粒度 RBAC，请用 TeamViewer 企业版等企业远程访问平台，而不用 RustDesk，因为 RustDesk 仅提供基础访问控制和密码保护。
- 如果你需要高性能远程游戏或视频剪辑，请用 Sunshine + Moonlight，而不用 RustDesk，因为 RustDesk 并未针对低延迟游戏或高帧率视频剪辑远程化优化。
- 如果你需要 Linux 上无缝的 Wayland 支持，请用 Chrome Remote Desktop 或其他替代方案，而不用 RustDesk，因为 RustDesk 的 Linux 支持历史上在 X11 上更强。[推断]
- 如果 AGPL-3.0 与你们的用例不兼容，请用 TightVNC 或其他宽松许可的替代方案，而不用 RustDesk，因为 AGPL-3.0 可能限制你在专有场景下的集成、分发或修改。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| TeamViewer | 未收录 | 需要自托管、开源远程桌面时选 RustDesk；需要商业、云端托管的远程桌面，带企业支持和跨平台可靠性时，再选 TeamViewer。 | 商业云端托管远程桌面，带企业支持、会话录制和合规；需付费订阅，数据经过其云端。 |
| AnyDesk | 未收录 | 需要自托管、开源远程桌面时选 RustDesk；需要轻量、快速的专有远程桌面，个人版免费时，再选 AnyDesk。 | 轻量专有远程桌面，个人版免费；快速简单，但闭源且依赖云端。 |
| Chrome Remote Desktop | 未收录 | 需要自托管、开源远程桌面时选 RustDesk；需要免费、基于浏览器的远程桌面，绑定 Google 账户时，再选 Chrome Remote Desktop。 | 免费、基于浏览器的远程桌面，绑定 Google 账户；极简单，但需 Google 生态，无自托管。 |
| TightVNC / TigerVNC | 未收录 | 需要自托管、带现代加密的开源远程桌面时选 RustDesk；需要传统 VNC 服务器，用于局域网访问，默认无加密时，再选 TightVNC。 | 传统 VNC，用于局域网访问；简单且协议标准，但缺乏现代加密、NAT 穿透和移动端客户端，需额外配置。 |
| Sunshine + Moonlight | 未收录 | 需要通用自托管远程桌面时选 RustDesk；需要低延迟游戏串流或高帧率远程桌面时，再选 Sunshine + Moonlight。 | 开源游戏串流主机（Sunshine）和客户端（Moonlight），针对低延迟高 FPS 优化；用例比通用远程桌面更窄。 |

## 技术栈

- **语言：** Rust（核心引擎与网络层），Flutter/Dart 跨平台 UI 层覆盖桌面端和移动端。
- **网络：** P2P 加 NAT 穿透（打洞），直连失败时回退到中继服务器；通过 TLS 1.3 加密。
- **UI：** Flutter 单代码库覆盖 Windows、macOS、Linux、Android 和 iOS，平台原生渲染。
- **媒体：** 自定义视频编解码管线，用于屏幕捕获和远程显示；支持多显示器和分辨率。
- **构建：** Rust 编译为原生二进制；Flutter 打包 UI 资源。支持 Flatpak 等分发格式。

## 依赖

- **客户端硬件：** 带屏幕和网络连接的设备，运行 Windows、macOS、Linux、Android 或 iOS。客户端为本地安装的原生二进制。
- **服务器/中继（可选）：** 纯 P2P 不需要服务器。要回退中继或常驻访问，需要一台小型 VPS 或服务器运行 `rustdesk-server` 中继和 ID/注册服务。最低配置约 1 CPU、512 MB 内存、modest 带宽。
- **网络：** 两端需要互联网访问（或局域网用于直接 P2P）。中继服务器需要公网 IP 和开放端口（TCP/UDP）。防火墙和 NAT 必须允许连接路径。
- **无外部数据库：** 中继服务器不需要数据库；它是一个轻量级有状态守护进程。

## 运维难度

**低**（直接 P2P 个人使用）：两端装客户端，交换 ID 和密码，连接。**中**（自建中继）：需要在 VPS 上部署 `rustdesk-server` 二进制（或 Docker 容器），开放所需端口，若想用品牌中继还要配置 DNS/SSL。主要运维关注点是：
- **安全：** 必须管理中继服务器访问、持续打补丁、轮换密钥/密码。默认配置使用简单密码保护；生产环境请考虑额外加固（fail2ban、VPN 覆盖、基于密钥的认证）。
- **NAT/防火墙穿透：** 某些企业网络会阻断 P2P 流量，迫使所有连接走中继——此时中继成为带宽瓶颈。
- **更新：** 客户端和中继必须保持版本兼容；版本不匹配可能导致连接失败。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 6.6 小时，基于 15 个 qualifying issues/PRs。
- **采用广度**：无法计算——unknown。
- **长青度**：Grade A——仓库已创建 2,104 天。
- **治理集中度**：Grade A——前三贡献者占比 53.3%（?）。
- **许可风险**：Grade D——AGPL-3.0 许可证。
## 存疑（未验证）

- [未验证] 截至 2026-07-01 约 117.4k GitHub star；star 数为近似值且对时间敏感。
- [未验证] 中继服务器资源需求和确切端口号系据典型自托管指南推断；生产部署请核实当前 `rustdesk-server` 文档。
- [未验证] TLS 1.3 和加密细节系据项目描述概括；安全审查前请确认当前加密协议和密钥管理。
- [未验证] Wayland 支持状态及特定合成器兼容性仍在演进；部署前请在目标 Linux 发行版上测试。
- [推断] 会话录制、审计日志和 RBAC 不是核心功能；如果合规要求这些，需要用额外工具补充 RustDesk。
- [推断] P2P 打洞成功率因网络拓扑（对称 NAT、企业防火墙）而异；在受限环境中请计划好中继回退。
