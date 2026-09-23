---
name: Bun
slug: bun
repo: https://github.com/oven-sh/bun
category: editors-and-runtimes
tags: [javascript, typescript, runtime, bundler, test-runner, package-manager]
language: Rust
license: NOASSERTION
maturity: v1.x, stable, 93.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T09:04:41Z
  default_branch: main
  default_branch_sha: 9f29e551236e048e2da3950c05b0deedc43059d0
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:10:38Z
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
      grade: A
      raw:
        median_ttfr_hours: 0.1
        qualifying_issues: 28
        band: relaxed_solo
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: bun-types
        dependent_repos_count: 3705
        downloads_last_month: 54257858
        graph_tier: B
        volume_tier: A
        cross_check_divergence: 1.02
        homebrew_installs_90d: 17627
        homebrew_tier: A
        release_downloads: 116679289
        release_assets: 2128
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 1988
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 63
        top1_share: 0.564
        top3_share: 0.846
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Bun

一款极速一体化的 JavaScript 与 TypeScript 工具集——将运行时、打包器、测试运行器和包管理器集成在单个二进制文件中。

![Bun — 健康度雷达](../../../assets/health/bun.zh.svg)

## 何时使用

你正在选择 JavaScript 或 TypeScript 运行时与工具链，而速度和集成度是决定性因素。你选 Bun 而不是 Node.js，因为厌倦了 Node.js 工具链的臃肿：一个运行时、一个打包器、一个测试框架、再加上一个包管理器。你想要一个单一、极速的二进制文件来搞定一切——`bun run` 直接执行 TypeScript，`bun test` 做内置测试，`bun build` 打包，`bun install` 管理依赖——全部比 Node.js 的等价工具快得多。你选 Bun 而不是 Deno，因为你看重 JavaScriptCore 引擎相比 V8 更快的启动时间和更低的内存占用，且你想要一体化的工具集，而非 Deno 以安全权限为核心的模式。

## 何时不用

- 如果你依赖原生 Node.js 插件或复杂的 C++ 绑定，请使用 Node.js 而不是 Bun，因为 Bun 目标是兼容 Node.js，但某些原生模块和 `node-gyp` 依赖可能无法直接运行。
- 如果你需要成熟的生态工具链和深度 npm 兼容性，请使用 Node.js 或 Deno 而不是 Bun，因为 Bun 较年轻，某些带 post-install 脚本或深入 Node.js 内部的 npm 包可能出现异常。
- 如果你要求完全受管的开源许可证，请使用 Deno 或 Node.js 而不是 Bun，因为 Bun 采用自定义许可证（NOASSERTION），并非标准的 MIT 或 Apache-2.0 等 OSI 认证许可证。
- 如果你已在 Node.js 工具链上深度投入，CI/CD、Docker 镜像和团队经验全是 Node 原生，请使用 Node.js 而不是 Bun，因为迁移成本可能超过性能收益。
- 如果你需要以 WebAssembly 为优先的运行时支持，请使用 Deno 而不是 Bun，因为 Deno 在 WebAssembly 集成和原生模块支持上更强。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| Node.js | 未收录 | 拥有最庞大生态的既有 JS/TS 运行时。 | Node.js 生态最深、托管支持最广；Bun 更快但较年轻、尚未充分验证。 |
| [Deno](deno.zh.md) | ✅ | 具备安全默认设置和内置工具链的现代 JS/TS 运行时。 | Deno 更成熟，采用标准 OSI 许可证；Bun 更快、工具更集成，但许可证模糊。 |
| [Tauri](tauri.zh.md) | ✅ | 非运行时对比，但两者都是基于 Rust 的开发工具。 | Tauri 构建桌面应用，Bun 运行 JS/TS。互补而非竞争。 |
| pnpm / Yarn | 未收录 | 拥有成熟工作区功能的专用包管理器。 | pnpm 和 Yarn 在工作区与 monorepo 上功能深厚；Bun 的包管理器很快，但可能缺少一些高级特性。 |

## 技术栈

- **Rust** — 核心运行时与打包器实现
- **JavaScriptCore（JSC）** — 驱动 Bun 的 JavaScript 引擎，以启动快著称
- **TypeScript** — 原生语言支持（内部转译）
- **Zig** — 部分底层系统实现
- **SQLite** — 嵌入用于包管理元数据

## 依赖

- Bun 二进制文件（单个可执行文件，无需外部运行时）
- macOS、Linux 或 Windows（x64/ARM64）
- 如需 npm 兼容：现有 `package.json` 与 `node_modules` 可直接使用
- 典型使用场景无需后端或数据库服务器

## 运维难度

**低。** Bun 是单个二进制文件，可通过 shell 脚本、npm 或系统包管理器安装。无需维护服务器。运维负担主要在于保持二进制更新，并验证你的依赖树在 npm 兼容性上是否有边缘情况。CI/CD 中将 `node` 替换为 `bun` 通常很直接，但需针对原生模块做边缘测试。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 0.1 小时，基于 28 个 qualifying issues/PRs。
- **采用广度**：无法计算——unknown。
- **长青度**：Grade A——仓库已创建 1988 天。
- **治理集中度**：Grade B——前三贡献者占比 84.6%（过去 12 个月内 63 位活跃维护者）。
- **许可风险**：无法计算——unknown。
## 存疑（未验证）

- [未验证] Bun 的准确许可证条款尚模糊；未标注标准 SPDX 许可证，商用或嵌入式部署可能存在使用限制。
- [推断] 原生 Node.js 插件兼容性正在改善，但复杂的 `node-gyp` 依赖仍可能不兼容。
- [未验证] 生产部署与企业用户的准确数量尚未从一手来源核实。
- [推断] Oven 的风险投资与商业模式可能影响开源路线图；需关注是否出现商业层级功能或重新许可。
