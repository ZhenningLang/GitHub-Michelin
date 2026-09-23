---
name: Ant Design
slug: ant-design
repo: https://github.com/ant-design/ant-design
category: component-libraries
tags: [react, ui-library, design-system, enterprise, components, typescript]
language: TypeScript
license: MIT
maturity: v5.x, stable, 98.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-06T09:03:38Z
  default_branch: master
  default_branch_sha: 3a896ca555df9ee436fd89fa3c46aa8b89580932
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:15:10Z
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
        median_ttfr_hours: 0.1
        qualifying_issues: 47
        band: default
        window_offset_days: 5
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: nuget.org
        canonical_package: antd
        dependent_repos_count: 0
        downloads_last_month: 7442
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        release_downloads: 4160
        release_assets: 74
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4169
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 74
        top1_share: 0.198
        top3_share: 0.49
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

# Ant Design

企业级 UI 设计语言和 React UI 库。在 React 生态中，它是构建管理后台、数据密集型应用和企业工具时最广泛采用的组件库之一。

![Ant Design — 健康度雷达](../../../assets/health/ant-design.zh.svg)

## 何时使用

你正在用 React 构建一个数据密集的管理后台、内部运营工具或 B2B SaaS 应用。你看过 shadcn/ui，但不想自己复制粘贴并维护每个组件文件——你需要一个能通过 npm 安装并直接导入的库。你看过 Material UI，但你需要更多开箱即用的企业级数据组件：带内置筛选的排序表格、日期范围选择器、树形控件和处理大文件列表的上传组件。你选择 Ant Design，因为它给你一整套开箱即用、无障碍的预置组件，看起来专业，无需雇佣设计师。通过 npm 安装、导入组件，你的应用立刻变得一致且精致。这套设计系统经过阿里巴巴和数千家公司的实战检验，你知道它能支撑复杂的多角色企业界面。

## 何时不用

- **如果你使用 Vue，请用 Ant Design Vue 或 Element Plus，而不是 Ant Design，因为** Ant Design 是 React 库。核心库没有官方 Vue 移植版本，React 组件无法在 Vue 项目中使用。
- **如果你的品牌需要显著偏离 Material Design 的定制视觉标识，请用 shadcn/ui 或 Tailwind UI，而不是 Ant Design，因为** Ant Design 的视觉语言很有辨识度（「Ant Design 风格」）。覆盖默认样式可能繁琐且脆弱。
- **如果包体积至关重要且你需要轻量库，请用 shadcn/ui 或 Radix UI，而不是 Ant Design，因为** 完整的 Ant Design 库体积较大。即使使用 Tree-shaking，设计令牌和 CSS 也会增加相当重量。
- **如果你需要移动优先的 consumer 应用，请用 Ionic 或 Flutter，而不是 Ant Design，因为** 虽然有 Ant Design Mobile，但主库面向桌面。consumer 移动应用更适合原生或混合框架。
- **如果你想要无样式的 headless 原语并完全掌控样式，请用 Radix UI 或 Headless UI，而不是 Ant Design，因为** Ant Design 是完整的带样式组件库。如果你想从无样式原语构建自己的设计系统，Ant Design 的抽象层级不对。
- **如果你的技术栈禁止 Less 或 CSS-in-JS，请用 shadcn/ui 或 MUI，而不是 Ant Design，因为** Ant Design 使用 Less 做主题化，需要特定构建工具才能深度定制。如果你需要 CSS Module 级隔离或 Tailwind 原生工作流，会产生摩擦。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Material UI（MUI）](material-ui.zh.md) | ✅ | 最受欢迎的 React UI 库，Material Design 风格，企业用户众多。 | MUI 在西方更普遍；Ant Design 在企业和亚太市场占主导。两者都很全面；按设计语言偏好和区域生态选择。 |
| [shadcn/ui](shadcn-ui.zh.md) | ✅ | 复制粘贴即可拥有的 React 组件，基于 Radix UI 和 Tailwind CSS。 | shadcn/ui 让你完全拥有、无 npm 依赖；Ant Design 启动更快，但锁定更深、样式灵活性更低。 |
| [Chakra UI](chakra-ui.zh.md) | ✅ | 模块化 React 组件库，注重开发者体验和无障碍。 | Chakra UI 的自定义主题更「开发者友好」；Ant Design 拥有更多企业级组件（尤其是数据表格和表单）。 |
| [Radix UI](radix-ui.zh.md) | ✅ | 无样式的 headless 原语，用于构建自己的设计系统。 | Radix 层级更低（样式自理）；Ant Design 是完整的带样式系统。 |
| Bootstrap / React-Bootstrap | 未收录 | 经典 CSS 框架加 React 包装。 | Bootstrap 更老更简单；Ant Design 更现代、组件更丰富，更适合复杂数据驱动应用。 |

## 技术栈

- **TypeScript** —— 主要语言；所有组件均带类型
- **React** —— 目标 UI 框架（Ant Design 是 React 库）
- **Less** —— 用于主题化和组件样式的 CSS 预处理器
- **CSS-in-JS** —— 内部用于动态样式（通过 `@ant-design/cssinjs`）
- **Design Tokens** —— 颜色、间距、字体的集中式令牌系统
- **Ant Design Mobile** —— 独立的 React Native / 移动端组件库（非同包）
- **dumi** —— ant.design 文档站点生成器

## 依赖

- **React** —— 必需的对等依赖（v16.8+ 支持 hooks，建议 v18+）
- **ReactDOM** —— 必需的对等依赖
- **TypeScript** —— 可选但强烈建议，用于类型安全
- **构建工具链** —— Webpack、Vite 或 esbuild，用于打包和 Less 编译
- **可选：moment.js / dayjs / date-fns** —— Ant Design 的日期组件需要日期库（推荐 dayjs 作为更轻量的替代方案）
- **可选：@ant-design/icons** —— 官方图标库（独立包）
- **可选：ant-design/charts 或 AntV** —— 数据可视化（独立生态）

## 运维难度

**低**。Ant Design 是 npm 库，不是独立服务。运维关注点仅限于：
- 保持库更新（主版本升级可能涉及组件 API 和主题化的破坏性变更）
- 通过仅导入所需组件来管理包体积
- 通过 Less 变量或 ConfigProvider 组件自定义主题
- 确保构建流程能处理 Less 编译，或使用预构建 CSS
- 监控复杂组件（表格、表单）的无障碍问题，可能需要手动调整 ARIA

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 0 天。
- **响应速度**：Grade A——中位首次响应时间 0.1 小时，基于 47 个 qualifying issues/PRs。
- **采用广度**：无法计算——registry_no_counts。
- **长青度**：Grade A——仓库已创建 4169 天。
- **治理集中度**：Grade A——前三贡献者占比 49.0%（过去 12 个月内 74 位活跃维护者）。
- **许可风险**：Grade A——MIT 许可证。

## 存疑（未验证）

- [未验证] Ant Design 用户在中国与全球其他地区的精确比例未经核实。
- [推断] Ant Design 的 CSS-in-JS 方案（通过 `@ant-design/cssinjs`）在包含大量动态样式更新的超大型应用中可能存在性能影响。
- [未验证] 所有 Ant Design 组件的无障碍审计结果未经独立验证。
- [推断] 阿里巴巴内部产品路线图对 Ant Design 开源优先级的具体影响程度未公开记录。
- [推断] Ant Design 的包体积和 CSS-in-JS 开销相对于 shadcn/ui 等轻量库的实际性能影响，取决于具体组件集和使用模式。
