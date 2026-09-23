---
name: Svelte
slug: svelte
repo: https://github.com/sveltejs/svelte
category: frameworks
tags: [svelte, frontend, framework, compiler, reactive, typescript, no-vdom, sveltekit]
language: TypeScript
license: MIT
maturity: v5.x, active, ~82k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-03T14:17:03Z
  default_branch: main
  default_branch_sha: b1cadd1eae6a709fc5bdc596256b617986a71aaf
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:19:00Z
  overall: A
  overall_score: 4.0
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
        median_ttfr_hours: 8.1
        qualifying_issues: 37
        band: default
        window_offset_days: 7
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: svelte
        dependent_repos_count: 56439
        downloads_last_month: 20786696
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.05
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3593
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 58
        top1_share: 0.381
        top3_share: 0.709
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

# Svelte


编译时前端框架，在构建阶段将组件转换为高效的 vanilla JavaScript，消除虚拟 DOM 开销，获得更小的包体积和更快的运行时性能。


![Svelte — health radar](../../../assets/health/svelte.zh.svg)

## 何时使用

你是一支中小型团队，正在构建一个对性能和包体积有要求的 Web 应用。你评估过 React，但它的虚拟 DOM 和运行时开销意味着初始 JavaScript 负载比你期望的更大，尤其对慢网络用户而言。你评估过 Vue，但你想找更轻量、可读性更强的方案。你选择 Svelte，因为它的编译器将组件直接编译成操作 DOM 的纯 JavaScript——没有虚拟 DOM 比对，没有运行时框架重量。你的 `.svelte` 文件看起来像是增强版 HTML，JavaScript 和 CSS 默认作用域隔离，让熟悉 Web 平台的开发者很容易上手。你交付得更快，应用感觉更流畅，而且不需要学习复杂的响应式 API，因为编译器已经帮你处理了响应性。

## 何时不用

- **如果你需要尽可能庞大的生态和第三方库选择，请用 React 而不是 Svelte，因为** React 的生态系统大了一个数量级。几乎每个细分 UI 需求都有 React 库可用；而用 Svelte 时，你常常需要自己写组件，或通过兼容层包裹 React 库。
- **如果你需要快速、低成本地招聘前端开发者，请用 React 或 Vue 而不是 Svelte，因为** Svelte 的人才池明显更小。在大多数就业市场，找到有经验的 Svelte 开发者比找 React 或 Vue 开发者更难。
- **如果你需要成熟的 meta-framework，带深度 SSR/SSG 和托管集成，请用 Next.js 或 Nuxt 而不是 Svelte，因为** 虽然 SvelteKit 存在且在不断改进，但它的生态和托管集成比 Next.js 小。如果你的团队已经在 Vercel 上运行，Next.js 有更深度的一流支持。
- **如果你对框架范式迁移风险敏感，请用 Vue 或 React 而不是 Svelte，因为** Svelte 5 引入了 runes，与 Svelte 4 基于标签的响应性模型有显著差异。这引起了社区摩擦，也意味着现有 Svelte 4 代码需要迁移成本。
- **如果你需要深度企业级工具、内置依赖注入和严格的架构主张，请用 Angular 而不是 Svelte，因为** Svelte 有意保持轻量且不做强制规定。它不会自带 CLI 脚手架模块系统、表单验证或 HTTP 客户端。
- **如果你需要把框架渐进式混入一个已有的庞大 React 或 Vue 代码库，请用 React 或 Vue 而不是 Svelte，因为** 虽然 Svelte 可以被嵌入，但用于渐进式迁移的工具链和社区实践不如 React 或 Vue 成熟。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [React](react.zh.md) | ✅ | 需要生态最大、招聘池最广的主流 UI 库时，选 React。 | React 的库和招聘池 vastly 更大；Svelte 对中小型应用更快、更简单，包体积更小。 |
| [Vue.js](vue.zh.md) | ✅ | 需要渐进式框架、温和学习曲线和更强第三方集成时，选 Vue。 | Vue 更容易招到人，第三方集成更多；Svelte 编译出的包更小，运行时开销更低。 |
| [Angular](angular.zh.md) | ✅ | 企业级、有主见的框架，与 TypeScript 深度集成。 | Angular 为大型团队内置了一切；Svelte 更轻更快，但缺乏企业级工具深度和 CLI 脚手架。 |
| [Next.js](nextjs.zh.md) | ✅ | 需要全栈 React、成熟 SSR/SSG 和 Vercel 深度集成时，选 Next.js。 | Next.js 主导 React meta-framework 领域；SvelteKit 是 Svelte 的对应方案，但生态和集成更小。 |
| [SvelteKit](sveltekit.zh.md) | ✅ | 基于 Svelte 构建的官方 meta-framework（类似 React 的 Next.js）。 | SvelteKit 是全栈 Svelte 的自然搭档；仅在不需要 SSR、路由或后端时才单独用 Svelte。 |
| Solid.js | 未收录 | 细粒度响应式 UI 库，无虚拟 DOM，性能极佳。 | Solid 更聚焦性能，社区更小；Svelte 生态更大，有 SvelteKit，学习曲线更温和。 |

## 技术栈

- **TypeScript** —— 主要实现语言；Svelte 提供一流 TS 支持
- **基于编译器** —— 无虚拟 DOM；编译器在构建时将 `.svelte` 文件转换为高效的 vanilla JavaScript
- **Runes（Svelte 5）** —— 细粒度显式响应式系统，使用 `$state`、`$derived`、`$effect` 等
- **Vite** —— 默认且推荐的构建工具（SvelteKit 基于 Vite）
- **CSS 作用域** —— 样式默认组件级作用域，无需额外配置
- **SvelteKit** —— 可选的 meta-framework，增加路由、SSR、服务端端点和部署目标适配器

## 依赖

- **Node.js** —— 用于编译器、构建工具和 SvelteKit（建议 LTS）
- **现代浏览器** —— Svelte 编译到 evergreen JavaScript；无需加载运行时框架
- **可选：SvelteKit** —— 如需 SSR、文件系统路由、API 端点和静态站点生成
- **可选：TypeScript** —— 完全支持但可选；纯 JavaScript 也能正常工作
- **构建工具**：Vite 是默认选择；Rollup 或 Webpack 可用于自定义场景

## 运维难度

**低**。Svelte 应用编译为静态 JavaScript，可部署到任何 CDN 或静态托管服务。编译器和 Vite 处理构建管线。复杂度来自：
- 需要 SSR 并运行 SvelteKit，这要求 Node.js 服务器或边缘 Runtime（如 Vercel、Cloudflare Workers）
- 从 Svelte 4 升级到 Svelte 5，需要将 `$:` 标签的响应式逻辑重写成 runes
- 需要自定义编译器插件或预处理器（如 Pug、Sass 或自定义转换）
- 将 Svelte 组件嵌入非 Svelte 应用，需要管理构建边界

## 健康度与可持续性

- **维护活跃度**：活跃 —— Svelte 5 于 2024 年底发布，核心团队持续定期发版。编译器和 SvelteKit 都在持续开发中。
- **治理集中度**：由 Rich Harris 创始者主导，现受雇于 Vercel。Bus factor 为中等 —— 社区热情高，但核心团队集中。治理模式是 benevolent-dictator 风格，而非基金会驱动。
- **背书与长青度**：Vercel 雇佣 Rich Harris 并资助 Svelte 开发。这是强劲的背书信号，但 Vercel 同时也拥有 Next.js，形成双框架动态，资源分配并不透明。[推断] 项目约 8 年的年龄 × 仍活跃，给出中等 Lindy 信号 —— 它已建立，但不如 React 或 Angular 悠久。
- **采用广度与生态**：稳步增长，但比 React 小一个数量级。著名生产用户包括 The New York Times 和 Apple（部分产品）。SvelteKit 正在成熟，但第三方集成比 Next.js 或 Nuxt 少。文档质量高。
- **风险旗标**：Svelte 5 的 runes 与 Svelte 4 的 `$:` 标签相比引入了显著范式转变，给现有代码库带来了真实的迁移摩擦。无 relicense 历史（MIT 保持稳定）。无显著 CVE。较小的生态系统意味着经过实战检验的第三方解决方案更少。

## 存疑（未验证）

- [未验证] 与 React 或 Vue 相比的确切包体积缩减幅度因应用和构建优化配置而异。
- [推断] Svelte 开发者就业市场相对于 React 的规模是从职位发布和社区调查推断的，并非硬数据。
- [未验证] 生产部署中使用 SvelteKit 与独立 Svelte 的确切比例未经独立核实。
- [未验证] Apple 和 The New York Times 在生产中使用 Svelte 的程度基于公开案例和会议演讲，而非独立审计。
- [推断] 从 Svelte 4 到 Svelte 5 runes 的实际社区摩擦和迁移工作量基于开发者报告和社交媒体情绪，而非测量数据。
