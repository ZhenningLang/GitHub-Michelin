---
name: Deno
slug: deno
repo: https://github.com/denoland/deno
category: editors-and-runtimes
tags: [javascript, typescript, runtime, secure-by-default, webassembly]
language: Rust
license: MIT
maturity: v2.x, stable, 107.3k stars (as of 2026-07)
last_verified: 2026-07-01
type: tool
upstream:
  pushed_at: 2026-07-06T09:16:36Z
  default_branch: main
  default_branch_sha: 34e593a462d1bb1b6e525ae8ee1534738b9a4b2e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:10:42Z
  overall: A
  overall_score: 4.0
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 16.5
        qualifying_issues: 18
        band: relaxed_solo
        window_offset_days: 1
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: crates.io
        canonical_package: deno_core
        dependent_repos_count: 396
        downloads_last_month: 7904610
        graph_tier: C
        volume_tier: A
        cross_check_divergence: 4.85
        homebrew_installs_90d: 155642
        homebrew_tier: A
        release_downloads: 35229439
        release_assets: 2628
        release_tier: A
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3053
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 93
        top1_share: 0.354
        top3_share: 0.609
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

# Deno

一款现代 JavaScript、TypeScript 和 WebAssembly 运行时，具备安全默认设置和出色的开发者体验。基于 V8、Rust 和 Tokio 构建。

![Deno — 健康度雷达](../../../assets/health/deno.zh.svg)

## 何时使用

你正在选择 JavaScript/TypeScript 运行时来构建新的服务端项目或 CLI 工具，想要现代、安全的工具链。你选 Deno 而不是 Node.js，因为厌倦了 `node_modules` 膨胀、`package.json` 依赖地狱，以及对外部工具（ts-node、nodemon、eslint、prettier）的需求。你想要一个将 TypeScript 视为一等公民、内置格式化、代码检查和测试、并默认强制执行安全权限的运行时。你选 Deno 而不是 Bun，因为 Deno 拥有标准 OSI 许可证（MIT）、更长的 track record（8 年对比 5 年），以及更强的 WebAssembly 集成。你用一条 shell 命令安装 Deno，直接运行 `.ts` 文件，准备好时编译成独立二进制。Deno 的标准库和 npm 兼容性意味着你可以带着现有包一起迁移，同时享受现代工具链。

## 何时不用

- 如果你已有带原生 Node.js 插件、C++ 绑定或深层 `node-gyp` 依赖的 Node.js 单体应用，请使用 Node.js 而不是 Deno，因为带有原生模块的复杂项目不太可能平滑迁移。
- 如果你依赖依赖 Node.js 特定 API 或 post-install 脚本的 npm 包，请使用 Node.js 而不是 Deno，因为某些包在 Deno 的 npm 兼容层下可能无法运行。
- 如果你的整个团队都熟悉 Node.js 而没有人有 Deno 经验，且项目是短期的，请使用 Node.js 而不是 Deno，因为 onboarding 期间的生产力下降可能超过收益。
- 如果你需要在 V8 层面进行性能优化，请继续使用 Node.js 而不是 Deno，因为两者使用相同的 V8 引擎，CPU 密集型性能没有差异。
- 如果你希望拥有完全可移植的无服务器代码，而不被专有边缘运行时锁定，请使用 Node.js 或 Cloudflare Workers 而不是 Deno，因为 Deno Deploy 是专有服务。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| Node.js | 未收录 | 现任 JS/TS 运行时，拥有最大的生态。 | Node.js 拥有最深的 npm 生态和最广泛的托管支持；Deno 提供更干净、更安全的开发者体验，但社区更小。 |
| [Bun](bun.zh.md) | ✅ | 快速的全能 JS 运行时，内置打包器和包管理器。 | Bun 也很快且将 TypeScript 视为一等公民，但比 Deno 更年轻、未经充分检验。 |
| [Supabase](../../databases/database-engines/supabase.zh.md) | ✅ | 使用 Deno 作为边缘函数运行时。 | 不是运行时本身的对比，但展示了 Deno 在无服务器边缘场景的生产级使用。 |
| Wasmer / Wasmtime | 未收录 | 纯 WebAssembly 运行时。 | 这些是用于 Wasm 模块的，不是 JS/TS 应用；Deno 可以运行 Wasm，但主要是 JS 运行时。 |

## 技术栈

- **Rust**——核心运行时、HTTP 服务器和沙箱层
- **V8**——JavaScript 引擎（与 Node.js 和 Chrome 相同）
- **Tokio**——Rust 的异步运行时，驱动 Deno 的 I/O
- **TypeScript**——一等语言支持（内部转译）
- **WebAssembly**——支持在 JS/TS 旁边运行 Wasm 模块

## 依赖

- Deno 二进制文件（单一可执行文件，无需外部运行时）
- 编译时：生成独立二进制需要 C++ 链接器（Deno 使用 `deno compile`）
- 可选：通过 `npm:` 标识符使用 npm 包，或通过 JSR（JavaScript Registry）使用包
- Deno 原生项目不需要 `node_modules` 或 `package.json`

## 运维难度

**低**。Deno 是可在主流操作系统上运行的单一二进制文件。部署时，可以直接运行 `deno run`，用 `deno compile` 编译为独立二进制，或部署到 Deno Deploy（托管边缘）。内置工具链（test、fmt、lint、bench）减少了对单独 devDependencies 的需求。没有 `node_modules` 膨胀简化了 CI/CD 缓存和 Docker 镜像大小。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 1 天。
- **响应速度**：Grade A——中位首次响应时间 16.5 小时，基于 18 个 qualifying issues/PRs。
- **采用广度**：Grade A——crates.io 上月下载量 7,904,610（包名：deno_core）。
- **长青度**：Grade A——仓库已创建 3053 天。
- **治理集中度**：Grade A——前三贡献者占比 60.9%（?）。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [未验证] Deno Land Inc. 已获得风险投资；具体融资轮次和投资者尚未从一手来源核实。
- [推断] Deno Deploy 的专有边缘运行时可能产生激励，使未来优先发展 Deno 特定 API 而非标准 Web 兼容性。
- [未验证] 除 Supabase 外的生产级部署数量和企业用户尚未核实。
