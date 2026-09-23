---
name: shadcn/ui
slug: shadcn-ui
repo: https://github.com/shadcn-ui/ui
category: component-libraries
tags: [react, components, tailwind, radix, design-system, ui-library, accessibility, nextjs]
language: TypeScript
license: MIT
maturity: active, ~117.7k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-03T12:29:04Z
  default_branch: main
  default_branch_sha: d0fae528221011f75a8c64a917073904c2847493
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:16:20Z
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 41.2
        qualifying_issues: 30
        band: default
        window_offset_days: 10
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@shadcn/react"
        dependent_repos_count: 0
        downloads_last_month: 6084607
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.04
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1357
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 74
        top1_share: 0.773
        top3_share: 0.798
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

# shadcn/ui

一套精心设计、无障碍的 React 组件，以及一种代码分发平台——你把组件复制进项目，完全拥有它们。基于 Tailwind CSS 和 Radix UI 原语构建。

![shadcn/ui — 健康度雷达](../../../assets/health/shadcn-ui.zh.svg)

## 何时使用

你是一名 React 开发者，正在开发新产品，需要一套可靠、无障碍的 UI 基础。你考虑过 Material UI，但它的主题系统强迫你覆盖那些你无法控制的层级，而且它的视觉语言 unmistakably 是 Google 风格。你考虑过 Radix UI，但它只是无样式原语——你仍需从零构建每个按钮、对话框和下拉菜单。你选择 shadcn/ui，因为它取两者之长：它给你开箱即好看、预先打磨好的组件，却以源文件形式复制进你的仓库，让你完全拥有。你运行 `npx shadcn@latest add button dialog`，组件便进入你的代码库，使用 Tailwind CSS 做样式，Radix UI 处理无障碍和行为。你免费获得键盘导航、ARIA 属性和焦点管理，而视觉层由你完全自定义，无需等待库更新。

当你想要一个留在仓库里、不在 `node_modules` 里的设计系统时，你也会选它。因为 shadcn/ui 是复制-拥有模式，没有运行时依赖需要版本锁定，也不用担心上游破坏性变更。如果上游加了新组件，你可以选择性采用；如果你需要定制变体，直接编辑复制进来的文件即可。这就是你选 shadcn/ui 而不是 Chakra UI 或 MUI 的原因——你想拥有每个像素，却不想从零重建原语。

## 何时不用

- **如果你使用 Vue、Angular 或 Svelte，请用 Vuetify、Angular Material 或 Skeleton UI，而不是 shadcn/ui，因为** shadcn/ui 仅限 React，该生态没有针对这些框架的等价复制-拥有组件体系。
- **如果你想要零配置、从不碰组件代码的 UI kit，请用 Material UI 或 Chakra UI，而不是 shadcn/ui，因为** shadcn/ui 要求你在仓库里拥有并维护组件文件。导入 `<Button>` 后从不看实现的方式，不是这个模型的玩法。
- **如果你需要严格的企业级设计系统与治理，请用 Ant Design 或 MUI，而不是 shadcn/ui，因为** shadcn/ui 是起点，不是受治理的设计系统。它不强制 token 使用、组件使用规则或跨团队视觉一致性——你必须自己建立治理。
- **如果你已经深度绑定另一个组件库，请继续使用那个库，而不是迁移到 shadcn/ui，因为** 从 Material UI、Ant Design 或 Chakra 迁移意味着逐个替换组件，并在 Tailwind 里重建主题层。回报是所有权，但迁移成本真实存在。
- **如果你需要开箱即用的复杂数据网格或图表组件，请用 AG Grid、TanStack Table 或 Recharts，而不是 shadcn/ui，因为** shadcn/ui 提供原语和基础表格模式；重型数据网格、透视表或图表终究需要集成专用库。
- **如果你不用 Tailwind CSS，请用 Chakra UI 或 MUI，而不是 shadcn/ui，因为** 组件用 Tailwind 工具类样式；如果你的项目用 CSS-in-JS、Styled Components 或纯 CSS，需要把整个样式层重新接线。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [Material UI（MUI）](material-ui.zh.md) | ✅ | 需要全面、Google Material 主题且拥有庞大企业生态的组件库时，选 MUI。 | 全面、Google-Material 主题的 React 组件库，企业采用广泛，有付费支持；比 shadcn/ui 更重、更有主见。 |
| [Chakra UI](chakra-ui.zh.md) | ✅ | 需要更简单、基于 styled-system 且 DX 好的 React 组件库时，选 Chakra UI。 | 简单、基于 styled-system 的 React 库，DX 好，主题 API 一致；文件级可定制性不如 shadcn/ui 的复制-拥有模式。 |
| [Ant Design](ant-design.zh.md) | ✅ | 需要全功能企业级 UI 框架和大量内置组件时，选 Ant Design。 | 全功能企业级 UI 框架，组件集庞大，社区以中文为先；比 shadcn/ui 更重，也不那么 Tailwind 原生。 |
| [Radix UI](radix-ui.zh.md) | ✅ | 需要无样式、headless 原语，并计划从零自建样式层时，选 Radix UI。 | 无样式、headless 无障碍原语；shadcn/ui 在 Radix 之上加了 Tailwind 样式和分发工作流。 |
| Headless UI | 未收录 | 需要 Tailwind 团队出品的无样式组件时，选 Headless UI。 | Tailwind 团队维护的无样式组件；原语比 Radix 少，没有内置的「复制到自有」分发系统。 |

## 技术栈

- **语言：** TypeScript，编译为 JavaScript；所有组件带类型，支持 tree-shaking。
- **样式：** Tailwind CSS 工具类负责全部视觉样式；没有单独的 CSS 文件或 CSS-in-JS 运行时。
- **原语：** 基于 Radix UI 原语实现无障碍（ARIA、键盘导航、焦点捕获、portal 行为）与交互（对话框、下拉菜单、手风琴等）。
- **分发：** CLI（`npx shadcn@latest add <component>`）把源文件复制到你项目的 `components/ui/` 目录；组件库本身不作为 npm 依赖存在。
- **框架支持：** 针对 Next.js 和 React 18+ 优化；也支持 Vite、Remix 和其他 React 框架。

## 依赖

- **运行时：** React 18+ 和 Tailwind CSS 项目。组件假设 Tailwind 已配置且工具类在构建中可用。
- **库依赖：** 复制进来的组件可能引入少量 Radix UI 子包和 `clsx` / `tailwind-merge` 做类名合并；这些是你已经在管理的正常运行时依赖。
- **无后端：** 客户端 UI 库，无需服务器、数据库或服务。
- **构建集成：** 你的打包器（Vite、Next.js、webpack）必须处理 Tailwind CSS 和 TypeScript/JSX 组件文件。

## 运维难度

**低。** 除了正常的 React 构建管线，没有额外东西要部署或运维。运维负担在于**复制组件的维护**：升级 shadcn/ui CLI 或添加新组件时，可能需要调和样式变更或 Tailwind 配置更新。因为组件活在仓库里，发现 bug 时你必须自己 patch——不能简单在 `package.json` 里升版本。好处是你永远不会被上游发布节奏卡住。对小团队而言，复制-拥有模式摩擦很小；对大型组织多团队而言，可能需要自建内部分发机制，以保持组件变体一致性。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 1 天。
- **响应速度**：Grade A——中位首次响应时间 41.2 小时，基于 30 个 qualifying issues/PRs。
- **采用广度**：Grade A——npmjs.org 上月下载量 6,084,607（包名：@shadcn/react）。
- **长青度**：Grade B——仓库已创建 1357 天。
- **治理集中度**：无法计算——unknown。
- **许可风险**：Grade A——MIT 许可证。
## 存疑（未验证）

- [未验证] 截至 2026-07-01 约 117.7k GitHub star；star 数为近似值且对时间敏感。
- [未验证] React 版本兼容性和框架支持（Next.js、Vite、Remix）随 CLI 版本变动；安装前请核实当前文档。
- [未验证] `npx shadcn` CLI 分发模式和可安装组件注册表正在快速演进；可安装组件集合及其选项可能变化。
- [推断] 复制-拥有模式意味着你需要自行把上游修复合并到本地组件文件中；没有自动补丁机制。
- [推断] 大型组织可能难以在多个团队各自复制和修改组件的情况下保持一致性；需要内部治理。
- [推断] 虽然原语本身无障碍，但最终应用的无障碍程度取决于你如何在自己的代码中组合和配置这些复制进来的组件。
- [推断] Next.js 和 React 18+ 之外的框架支持因 CLI 版本而异，可能需要手动配置。
