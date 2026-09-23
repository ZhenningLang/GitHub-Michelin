---
name: Angular
slug: angular
repo: https://github.com/angular/angular
category: frameworks
tags: [web-framework, typescript, spa, pwa, enterprise, frontend]
language: TypeScript
license: MIT
maturity: v19.x, stable, 100.4k stars (as of 2026-07)
last_verified: 2026-07-01
type: framework
upstream:
  pushed_at: 2026-07-01T21:10:34Z
  default_branch: main
  default_branch_sha: b126dc9726789ad5ca3b26e497725e6a05031ed3
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:16:33Z
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.0
        qualifying_issues: 28
        band: default
        window_offset_days: 11
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@angular/core"
        dependent_repos_count: 768558
        downloads_last_month: 20872075
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.05
        release_downloads: 324
        release_assets: 6
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4387
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 89
        top1_share: 0.162
        top3_share: 0.36
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

# Angular

用于构建移动端和桌面端 Web 应用的综合性开发平台。基于 TypeScript，由 Google 构建和维护，专注于企业级应用。

![Angular — 健康度雷达](../../../assets/health/angular.zh.svg)

## 何时使用

你是一支企业团队，正在构建一个大型、复杂的 Web 应用，包含数十个页面、严格的编码规范，并对长期可维护性有要求。你评估过 React，但它「自带一切」的哲学意味着你需要花数周时间选择和拼接路由、状态管理和表单验证库。你评估过 Vue，但它更温和的学习曲线对大型团队而言内置结构不足。你选择 Angular，因为它自带你所需的一切：功能强大的 CLI 脚手架、响应式表单系统、HTTP 客户端、支持懒加载的路由器以及一流的 TypeScript 体验。你不想花数周时间评估和拼接第三方库来解决路由、状态管理或表单验证。Angular 的 opinionated 结构意味着新员工能更快上手，因为代码库遵循可预测的模式；而 Google 的长期背书让你有信心该框架在五年后仍会被维护。

## 何时不用

- **如果你需要落地页、博客或不足 10 个屏幕的简单 CRUD，请用 Vite + React 或 Vue，而不是 Angular，因为** Angular 的样板代码和构建复杂度对小型项目是大材小用。更轻的栈能让你更快交付。
- **如果你的团队回避 TypeScript，请用纯 React 或 Vue，而不是 Angular，因为** Angular 深度原生依赖 TypeScript。如果你的团队偏好纯 JavaScript，或觉得 TS 装饰器和复杂类型是负担，摩擦将持续存在。
- **如果你需要快速原型验证或快速 MVP，请用 Next.js 或 Vue，而不是 Angular，因为** Angular 严格的模块系统、构建流程和样板代码会拖慢快速迭代。更轻的框架更适合黑客马拉松和原型。
- **如果你需要 SEO 优先的静态站点，请用 Next.js 或 Nuxt，而不是 Angular，因为** 虽然 Angular 支持 SSR（Angular Universal），但在静态站点生成方面不如 Next.js 或 Nuxt 无缝。如果你的内容以静态为主且对 SEO 至关重要，那些框架是更好的选择。
- **如果你需要异构微前端，请用基于 React 的微前端配合模块联邦，而不是 Angular，因为** Angular 的 zone.js 和 Ivy 编译器在与非 Angular 微前端混合时会产生集成摩擦。如果你的架构需要混合框架的 shell，复杂度是真实存在的。
- **如果包体积对低带宽或移动优先市场至关重要，请用 Svelte 或 Preact，而不是 Angular，因为** Angular 核心框架比 React 或 Vue 更大。面向低带宽或移动优先的新兴市场的应用，初始加载体积可能是个问题。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [React](react.zh.md) | ✅ | 需要最大 UI 生态和「就是 JavaScript」理念时，选 React。 | React 更灵活，就业市场更大；Angular 更 opinionated，自带更多内置工具，减少决策疲劳。 |
| [Vue.js](vue.zh.md) | ✅ | 需要渐进式框架、更温和的学习曲线和优秀文档时，选 Vue。 | Vue 更容易增量采纳；Angular 要求全面投入，但回报是企业级更强的结构性。 |
| [Svelte](svelte.zh.md) | ✅ | 需要编译时组件、极小运行时开销和无虚拟 DOM 时，选 Svelte。 | Svelte 对中小型应用更快更简单；Angular 拥有更深的企业支持、更多第三方集成和更长的记录。 |
| [SvelteKit](sveltekit.zh.md) | ✅ | 需要 Svelte 的全栈 meta-framework，而不是单独组件框架时，选 SvelteKit。 | SvelteKit 围绕 Svelte 增加路由、SSR 和应用约定；Angular 仍更企业级、更 opinionated，也更久经验证。 |
| [Next.js](nextjs.zh.md) | ✅ | 需要 React 生态 SSR/SSG 和主流全栈框架时，选 Next.js。 | Next.js 是 React 生态 SSR/SEO 的默认选择；Angular Universal 存在，但在该细分领域不占主导。 |
| [shadcn/ui](../component-libraries/shadcn-ui.zh.md) | ✅ | 组件分发模式，不是框架——通常在 React 内部使用。 | 并非直接替代品；shadcn/ui 关注组件所有权，Angular 是完整应用框架。 |
| [Lit](lit.zh.md) | ✅ | 基于标准的 Web Components 构建库，运行时极小。 | Lit 用于构建可互操作的组件，而非完整 SPA；Angular 是带路由、依赖注入和 CLI 的完整框架。如果设计系统需要跨框架工作，选 Lit。 |

## 技术栈

- **TypeScript** —— 主要语言；Angular 是最早全面拥抱 TS 的框架之一
- **RxJS** —— 异步操作和状态管理的响应式编程库
- **Zone.js** —— 变更检测机制（正逐步被 Signals 取代）
- **Angular CLI** —— 基于 Webpack / esbuild 的构建、测试和脚手架工具链
- **Angular Universal** —— 服务端渲染（SSR）和静态站点生成（SSG）
- **Angular Material** —— 官方 Material Design 组件库
- **Ivy** —— 新一代编译和渲染管线
- **Signals** —— 现代细粒度响应式系统（v16+ 引入，逐步取代 zone.js）

## 依赖

- **Node.js** —— CLI 和构建工具的 Runtime（建议 LTS）
- **TypeScript** —— 框架围绕 TS 设计；使用纯 JS 不现实
- **现代浏览器** —— Angular 支持 evergreen 浏览器；已放弃 IE11 支持
- **可选：Angular Universal** —— 如需 SSR，需 Node.js 服务器
- **可选：Angular Material** —— 如需预置 Material Design 组件（非必需）
- **可选：NgRx / Akita / NGXS** —— 复杂状态管理，超出 RxJS 服务的能力
- **构建工具**：CLI 封装了 Webpack / esbuild / Vite，但高级场景可能需要自定义 builder

## 运维难度

**低到中**。Angular 应用是静态 SPA（或 SSR 应用），可部署到任何 CDN 或 Web 服务器。CLI 处理构建管线、Tree-shaking 和优化。复杂度来自：
- 需要自定义 Webpack 配置（如微前端或遗留模块联邦）
- 启用 SSR 后必须运行 Node.js 服务器
- 管理包含多个 Angular 应用的 monorepo（常用 Nx 解决）
- 升级主版本（Angular 6 个月一个主版本周期，意味着每年需升级）

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 0.0 小时，基于 28 个 qualifying issues/PRs。
- **采用广度**：Grade A——npmjs.org 上月下载量 20,872,075（包名：@angular/core）。
- **长青度**：Grade A——仓库已创建 4387 天。
- **治理集中度**：Grade A——前三贡献者占比 36.0%（?）。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [推断] Angular 从 zone.js 到 Signals 的迁移时间线，以及 Google 内部使用 Angular 的应用比例，未经核实。
- [未验证] 企业级生产部署的确切数量及其规模未经独立审计。
- [未验证] Angular 相对于 React 和 Vue 在新项目启动中的市场份额，是从职位发布和社区调查推断的，而非硬数据。
- [推断] 与非 Angular shell 的微前端集成是可行的，但具体摩擦程度取决于模块联邦配置。
- [推断] Angular 包体积相对于 React 或 Vue 的实际性能影响因应用和优化策略而异。
