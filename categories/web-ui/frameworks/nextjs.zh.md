---
name: Next.js
slug: nextjs
repo: https://github.com/vercel/next.js
category: frameworks
tags: [nextjs, react, ssr, ssg, fullstack, vercel, typescript, app-router, edge]
language: TypeScript / JavaScript
license: MIT
maturity: v15.x, stable, ~138k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-06T08:21:40Z
  default_branch: canary
  default_branch_sha: 00598045032a0e5b313de7b6ef0af60ed9390c2a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:17:48Z
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
      grade: B
      raw:
        median_ttfr_hours: 23.7
        qualifying_issues: 3
        band: default
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: next
        dependent_repos_count: 345645
        downloads_last_month: 192615857
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3639
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 79
        top1_share: 0.098
        top3_share: 0.276
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

# Next.js


全栈 React 框架的默认选择，由 Vercel 创建并维护。内置 App Router、React Server Components、自动静态优化、ISR 和内置 API 层——与 Vercel 深度集成是「happy path」。


![Next.js — health radar](../../../assets/health/nextjs.zh.svg)

## 何时使用

你是一支产品团队，正在构建一个需要平衡 SEO、性能和动态交互的现代 Web 应用。你从简单的 React SPA 起步，但很快撞上了墙：搜索引擎无法索引客户端渲染的内容，首屏加载缓慢，而你的「后端」是一个需要单独部署和维护的 API 服务。你选择 Next.js，因为它让你留在 React 生态中，同时原生解决这些问题。你编写 React 组件，其中一些在服务端渲染——向浏览器发送 HTML 以实现即时首屏绘制——而另一些水合为完全可交互的客户端组件。你在同一代码库中直接添加 API 路由，因此前端和后端共享类型、工具和部署流程。你部署到 Vercel，无需配置 CDN 即可获得边缘缓存、图片优化和增量静态再生。对你来说，当需求是「React 加一个全栈框架」而不是「React 加一周架构决策」时，Next.js 是务实的选择。

## 何时不用

- **如果你需要一个没有 React 交互的、以内容为主的简单静态站点，请用 Astro 而不是 Next.js，因为** Next.js 本质上是一个 React 框架。对于博客、文档和营销站点等以静态文本为主的场景，Astro 的 Islands 架构能提供更小的包体积和更快的加载速度。
- **如果你想避免厂商锁定和 Vercel 专属部署，请用 Remix 或 Nuxt 而不是 Next.js，因为** 虽然 Next.js 采用 MIT 许可证，但部分功能（Edge Runtime、图片优化、特定缓存行为）是为 Vercel 基础设施设计的。自托管是可行的，但你会为匹配「happy path」体验而与框架搏斗。
- **如果你的团队使用 Vue、Angular 或 Svelte，请用 Nuxt、Angular 或 SvelteKit 而不是 Next.js，因为** Next.js 仅支持 React。不存在从其他框架增量迁移的路径。
- **如果你需要一个轻量的客户端 SPA，无需服务端渲染，请用 Vite + React 而不是 Next.js，因为** Next.js 的服务端渲染管线、文件系统路由和构建复杂度对简单 SPA 来说是大材小用。你会承担不必要的开销。
- **如果你不愿意接受框架的 opinionated 设计，请不要使用 Next.js，因为** Next.js 在路由、数据获取和渲染模式上高度 opinionated。与框架对抗（例如自定义路由、绕过 App Router 约定）会带来痛苦和工作区代码。
- **如果你不需要后端或 Node.js 运行时，请用静态站点生成器或 JAMstack 托管方案而不是 Next.js，因为** Next.js 需要 Node.js 运行时来支持 SSR、API 路由和中间件。即使是「静态导出」模式，与专用静态生成器相比也存在局限。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Angular](angular.zh.md) | ✅ | 全栈 TypeScript 框架，内置深度的企业级工具链和强 opinionated 设计。 | Angular 自带更多内置功能，且不限于 React 生态；Next.js 主导 React SSR/SSG 细分领域，并拥有更大的 React 就业市场。 |
| [React](react.zh.md) | ✅ | 只需要 UI 库，而不需要 Next.js 路由、SSR 或全栈约定时，选 React。 | 纯 React 提供最大灵活性和更小的包体积；Next.js 提供路由、SSR 和全栈约定，但增加了复杂度。 |
| [Vue.js](vue.zh.md) | ✅ | 需要更容易增量采纳的非 React 渐进式框架时，选 Vue。 | Vue 是框架无关的，更容易增量采纳；Next.js 仅支持 React，且更 opinionated。 |
| [Svelte](svelte.zh.md) | ✅ | 需要编译时组件模型且不想投入 React 生态时，选 Svelte。 | Svelte 对组件密集型中小应用更轻量、更简单；Next.js 拥有庞大得多的生态和更深的就业市场。 |
| [SvelteKit](sveltekit.zh.md) | ✅ | 需要围绕 Svelte 编译时模型构建的更轻量全栈框架时，选 SvelteKit。 | SvelteKit 对中小型应用更轻量、更简单；Next.js 拥有庞大得多的生态、更成熟的工具和更深的就业市场。 |
| Nuxt.js | 未收录 | 全栈 Vue 框架——Vue 生态中相当于 Next.js 的存在。 | Nuxt 面向 Vue 团队；Next.js 面向 React 团队。选择通常取决于你的 UI 框架偏好。 |
| Remix | 未收录 | 全栈 React 框架，专注于 Web 标准、渐进增强和更弱的厂商耦合。 | Remix 对部署更灵活，避免了一些 Vercel 专属功能；Next.js 拥有更多内置优化（图片、字体、脚本）和更大的社区。 |
| [Astro](astro.zh.md) | ✅ | 以内容为中心的静态站点构建工具，采用 Islands 架构并支持多框架。 | Astro 更适合静态内容站点和混合框架项目；Next.js 更适合动态、全栈且交互密集的 React 应用。 |

## 技术栈

- **React** —— 底层 UI 库；Next.js 是一个 React 框架
- **TypeScript / JavaScript** —— 主要开发语言；对 TS 提供一流支持
- **Node.js** —— SSR、API 路由、中间件和构建流程的运行时
- **Turbopack** —— 基于 Rust 的打包器，Webpack 的继任者，用于开发环境（截至 v15，生产构建仍使用 Webpack，Turbopack 目标指向生产环境）
- **React Server Components** —— App Router（v13+）中的服务端组件渲染，实现零客户端 JS 的服务器 UI
- **Edge Runtime** —— 轻量级 V8 隔离环境，用于 Edge API 路由、中间件和 Vercel Edge Functions
- **内置优化** —— 图片优化（`next/image`）、字体优化（`next/font`）和脚本优化（`next/script`）
- **ISR（增量静态再生）** —— 混合静态/动态渲染，在后台更新页面而无需完整重建

## 依赖

- **Node.js（建议 LTS）** —— 构建、开发服务器、SSR 和 API 路由必需
- **React 18+** —— peer dependency；Next.js 是 React 框架，不能脱离 React 使用
- **包管理器** —— npm、yarn、pnpm 或 bun
- **可选：Vercel** —— 用于「happy path」部署，所有功能（Edge、图片优化、ISR）开箱即用
- **可选：Docker / 容器平台** —— 用于生产环境自托管 Node.js 服务器
- **可选：数据库 / ORM** —— 用于全栈数据层（常用组合包括 Prisma、Drizzle、Mongoose 等）
- **可选：Redis / 缓存层** —— 用于自托管场景中的 ISR 重验证、会话存储或速率限制

## 运维难度

**中到高**。Next.js 是一个全栈框架，拥有复杂的构建系统和多种渲染模式（SSG、SSR、ISR、客户端、Edge）。部署在 Vercel 上是「happy path」——几乎零配置，自带边缘缓存、图片优化和 Serverless 弹性伸缩。自托管则显著增加复杂度：
- 必须为 SSR、API 路由和中间件运行 Node.js 服务器；静态导出模式存在，但会牺牲大量功能
- ISR 需要持久化缓存和失效策略；自托管意味着你自己管理这些
- 图片优化（`next/image`）在 Vercel 的边缘基础设施上表现最佳；自托管需要自定义 loader 或兼容的图片优化服务
- 中间件和 Edge API 路由需要兼容 V8 隔离环境的运行时（Node.js 18+ 或自定义 Edge Runtime）
- 大型应用构建时间可能很长；Turbopack 提升了开发速度，但生产构建优化仍然是计算密集型任务
- App Router（v13+）引入了新的概念（Server Components、Server Actions、Parallel Routes），增加了心智负担和迁移成本

## 健康度与可持续性

- **维护活跃度**：由 Vercel 积极维护，发布节奏快。默认分支为 `canary`，大版本约每年发布一次。仓库保持一致的日常活动。
- **治理集中度**：单厂商治理——Vercel 掌控路线图并雇佣核心维护者。MIT 许可证允许 fork，但生态（模板、教程、部署指南）以 Vercel 为中心。
- **背书与长青度**：Vercel 是资金充足的公司，Next.js 是其旗舰开源项目。首次发布于 2016 年（约 8 年历史），作为 React 框架拥有强大的 Lindy 先验——足够古老，经历了多次范式转变，仍然活跃维护。
- **采用广度与生态**：全栈 React 框架的绝对主导者，拥有约 138k GitHub stars 和庞大的生产环境采用量。在 React 元框架中， starter 模板、第三方集成和就业市场均为最大。
- **风险标记**：厂商锁定张力——部分功能为 Vercel 优化，自托管时性能下降或需要额外配置。App Router 迁移（v13+）曾引发争议，对使用 Pages Router 的团队造成干扰。无重新许可历史（保持 MIT）。

## 存疑（未验证）

- [推断] 自托管与部署在 Vercel 上时 Next.js 功能降级的确切比例未经独立基准测试。
- [未验证] 截至 2026-07 约 138k GitHub stars；star 数量是近似值且随时间变化。
- [未验证] Turbopack 的生产就绪程度和相对于 Webpack 的构建时间性能提升基于 Vercel 的市场宣传，可能因应用而异。
- [推断] 现有团队迁移到 App Router 的摩擦程度严重依赖 Pages Router 的使用模式和第三方库兼容性。
- [推断] React Server Components 和 Server Actions 的未来方向可能显著改变 Next.js 的架构；App Router 模型在生产环境大规模场景下的长期稳定性仍在验证中。
