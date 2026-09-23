---
name: uv
slug: uv
repo: https://github.com/astral-sh/uv
category: python-tooling
tags: [python, packaging, dependency-manager, rust, cli]
language: Rust
license: Apache-2.0
maturity: v0.x, active, 87k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T08:47:56Z
  default_branch: main
  default_branch_sha: 648f5a3bd2be7c6e8465863693d4e625462fcbc1
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:56:35Z
  overall: A
  overall_score: 3.83
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
        median_ttfr_hours: 3.3
        qualifying_issues: 53
        band: relaxed_solo
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: uv
        dependent_repos_count: 2
        downloads_last_month: 128564586
        graph_tier: D
        volume_tier: A
        cross_check_divergence: 1.04
        homebrew_installs_90d: 523657
        homebrew_tier: A
        release_downloads: 630576062
        release_assets: 4180
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1086
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 152
        top1_share: 0.36
        top3_share: 0.632
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

# uv

用 Rust 编写的极速 Python 包与项目管理器，旨在以单一工具加通用锁文件替代 pip、pip-tools、pipx、poetry、pyenv 等。

![uv — 健康度雷达](../../assets/health/uv.zh.svg)

## 何时使用

你是一位 Python 开发者，厌倦了等待 `pip install` 解析依赖，或疲于在多个工具间切换——pip 安装、pip-tools 锁定、pipx 管理 CLI 工具、pyenv 管理 Python 版本、poetry 管理项目。你考虑过 Poetry 的成熟项目管理和发布工作流，但你想要更快、更统一的体验，用单一工具和通用锁文件即可。你选择 uv，因为它用基于 Rust 的 CLI 替代了整个工具栈，比 pip 快 10–100 倍安装包、管理 Python 版本、运行带内联依赖元数据的脚本，并产出可入 Git 的锁文件。需要现代解析器和锁文件，而非旧版依赖算法时，选 uv 而非 pip；优先考虑安装速度和统一 CLI，而非成熟发布工作流时，选 uv 而非 Poetry；管理纯 Python 包，而非需要预编译二进制分发的科学栈时，选 uv 而非 Conda。你正在启动新 Python 项目或现代化现有项目，想要最快、最可靠的打包体验。


## 何时不用

- **如果你需要成熟、久经考验的生态**——如果你需要 20 余年稳定性和边缘情况覆盖的打包工具，用 pip + virtualenv 代替 uv，因为 uv 相对较新（2023 年创建），某些依赖解析的边缘情况或平台特定构建可能仍不如 pip 或 poetry 平滑。
- **如果你依赖 poetry 的特有功能**——如果你需要 Poetry 的 `pyproject.toml` extras、插件和构建后端生态，用 Poetry 代替 uv，因为迁移现有 poetry 项目可能需要手动调整，且尚未完全实现功能对等。[未验证]
- **如果你需要 conda-forge 或科学计算二进制包**——如果你需要预编译二进制分发用于科学栈（NumPy、带 CUDA 的 PyTorch），用 Conda 或 Mamba 代替 uv，因为 uv 是 pip 的替代，不是 Conda 的替代，不处理科学计算二进制分发。
- **如果你在使用没有 Rust 工具链的冷门平台**——如果你需要面向小众架构、无预编译二进制的包管理器，用 pip + 源码构建代替 uv，因为 uv 为常见平台提供预编译二进制，但小众架构可能需要从源码构建。
- **如果你的团队还没准备好改变工作流**——如果你有稳定的老项目，pip/virtualenv 工作流根深蒂固且没有迁移预算，用 pip + pip-tools 代替 uv，因为 uv 引入了新的命令（`uv pip`、`uv run`、`uv lock`），对于重视稳定性胜过速度的团队，学习曲线可能不值得。


## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| pip | 未收录 | Python 默认包安装器。 | pip 通用且稳定，但慢；uv 快 10–100 倍，自带现代解析器和锁文件。 |
| Poetry | 未收录 | Python 依赖管理与打包工具。 | Poetry 的项目管理与发布工作流更成熟；uv 更快但较新，功能对等仍在追赶。 |
| pdm | 未收录 | 支持 PEP 582 的 Python 包管理器。 | pdm 现代且规范合规；uv 更快，但可能缺少一些 pdm 特有的工作流功能。 |
| Conda | 未收录 | 面向任意语言的跨平台包管理器，尤其适合科学 Python。 | Conda 处理科学计算二进制分发；uv 仅限 Python，不能替代 Conda 的二进制打包能力。 |

## 技术栈

- **Rust**——主要实现语言，追求性能与内存安全
- **PubGrub**——依赖解析算法（cargo 与 dart 也在使用）
- **PEP 517/518/621/660**——现代 Python 打包标准支持

## 依赖

- 受支持的平台（macOS、Linux、Windows；x86_64 与 ARM64）
- 安装无需 Python 运行时（自包含 Rust 二进制）
- 要管理的 Python 解释器（uv 可为你安装）

## 运维难度

**低**。单一静态二进制——通过 `curl`、Homebrew 或 PyPI 安装。无守护进程、无后台服务。对团队而言，主要成本是工作流迁移与培训。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 3.3 小时，基于 53 个 qualifying issues/PRs。
- **采用广度**：Grade A——pypi.org 上月下载量 128,564,586（包名：uv）。
- **长青度**：Grade B——仓库已创建 1086 天。
- **治理集中度**：Grade A——前三贡献者占比 63.2%（过去 12 个月内 152 位活跃维护者）。
- **许可风险**：Grade A——Apache-2.0 许可证。
## 存疑（未验证）

- [未验证] 实际加速倍数因平台、缓存状态和网络条件而异；10–100 倍是项目自身的基准测试声明。
- [未验证] 截至验证日期，uv 尚未完全实现与 Poetry 的构建和发布工作流的功能对等。
- [推断] 鉴于 Astral 的融资模式，随着产品成熟，可能会引入商业层级或功能阉割。
