---
name: Anime.js
slug: anime
repo: https://github.com/juliangarnier/anime
category: frontend-animation
tags: [animation, javascript, svg, timeline, scroll, easing, web]
language: JavaScript
license: MIT
maturity: v4.5.0, active (2026-06)
last_verified: 2026-06-26
type: library
upstream:
  pushed_at: 2026-06-22T15:28:21Z
  default_branch: master
  default_branch_sha: 2c9cf8ea00329f6768c7d7902252ed977d75ce42
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:18:50Z
  overall: B
  overall_score: 3.0
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 44
        active_weeks_13: 1
        carve_out: mature_library_lindy
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: animejs
        dependent_repos_count: 7272
        downloads_last_month: 3732175
        graph_tier: B
        volume_tier: B
        cross_check_divergence: 1.01
        release_downloads: 130
        release_assets: 3
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 3845
        last_commit_age_days: 44
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.965
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# Anime.js

一个体积小、零依赖的 JavaScript 动画引擎，通过统一的 `animate()` API 驱动 CSS 属性、SVG、DOM 属性和普通 JS 对象，内置时间线、错峰（stagger）、弹簧缓动、滚动联动播放，以及可拖拽（draggable）模块。

![anime — 健康度雷达](../../assets/health/anime.zh.svg)

## 何时使用

你是一名前端开发者，正在做一个营销站点或产品落地页，设计稿要求一连串编排好的动效：主标题逐字错峰入场、SVG logo 描边绘制、若干元素随滚动进入视口时animate、还有一张可以带物理惯性甩动的卡片。你不想为此引入一个绑定到某个 UI 框架的重型动效库，也不想手写 `requestAnimationFrame` 循环和缓动数学。于是你选用 Anime.js：基础场景一句 `animate(targets, { translateX: 250, ease: 'outElastic', loop: true })` 就够；序列变复杂时，用 `createTimeline()` 配合偏移量来编排，而不是去拼一堆 `setTimeout`。因为它是框架无关的原生 JS、运行时零依赖，所以能直接落进普通 `<script>`、Vite/webpack 打包，或 React/Vue/Svelte 任意一种而无需适配层；而 v4 的模块化构建让你只 import 真正用到的 `animate`、`stagger`、`svg`、`scroll` 等片段，保持体积精简。

它同样适合处理 CSS 引擎不便触及的动画：把任意 JS 对象的数值补间出来喂给 canvas 或图表、把一条 SVG path 形变（morph）成另一条、跑运动路径动画，或让时间线随滚动位置 scrub。v4 重写把这些能力拆成独立模块（Timer、Animation、Timeline、Animatable、Draggable、Scope、ScrollObserver、SVG、Text），让你在保持体积轻的同时，又能在某个具体页面需要时取用更重的特性。

## 何时不用

- **你已经身处 React 优先的声明式动效世界。** 如果你的应用把动画当作 JSX 状态来组织（挂载/卸载过渡、布局动画、手势弹簧），那么 Framer Motion 或 `react-spring` 这类 React 原生库会比对 ref 命令式调用 `animate()` 更顺手。（二者在此均 `未收录`）
- **你需要完整的 3D / WebGL 场景动画。** Anime.js 提供 Three.js 适配器来「驱动数值」，但它本身不是 3D 引擎；要做场景图、材质、相机，应该用 Three.js / GSAP+WebGL，而非本库。
- **你需要最广、最久经考验的插件生态和商业支持。** GSAP 的插件目录更深（MorphSVG、ScrollTrigger、SplitText、物理插件）且行业沉淀久；若你需要这种广度或付费支持，Anime.js 较轻的能力面可能不够。
- **纯 CSS keyframes 已经够用。** 对于简单 hover、loading、一次性过渡，CSS `@keyframes` / `transition` 没有 JS 开销、也无需打包任何库——只有在需要排序、动态数值或运行时控制时，才动用 JS 动画。
- **你被一个长期存活的 v3 代码库锁住。** v4 是一次显著的 API 与模块重写，迁移既有 v3 动画并非原地升版本号，存在真实的重构成本。
- **严格的旧浏览器要求。** 本库面向现代常青浏览器；若你必须支持非常老旧的引擎，请在投入前先核实你依赖的特性集是否可用。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| GSAP (GreenSock) | 未收录 | 当插件广度、ScrollTrigger/MorphSVG 类能力和商业支持是决定因素时，选 GSAP；当你要更小、MIT、零依赖、框架无关的动画器时，选 Anime.js。 | 生态更大、更成熟（ScrollTrigger、MorphSVG、物理插件）并有商业支持，心智占有率高。Anime.js 更小、MIT 许可、零依赖，且 v4 已完全模块化。 |
| Motion / Framer Motion | 未收录 | 当你要 React 优先的声明式组件动画时，选 Motion 或 Framer Motion；当命令式、框架无关的编排更合适时，选 Anime.js。 | 声明式、React 优先（也有 vanilla `motion` 核心），在组件驱动的应用里更地道。Anime.js 是命令式、框架无关——当你不活在 React 渲染模型里时更合适。 |
| Motion One | 未收录 | 当最小的 WAAPI 运行时是优先级时，选 Motion One；当时间线、拖拽、SVG、滚动和文本辅助值得更大能力面时，选 Anime.js。 | 极小、基于 WAAPI 的动画器，体积非常小。Anime.js 内置更多能力（时间线、拖拽、SVG 形变、滚动、文本），代价是体积更大但仍属轻量。 |
| Web Animations API (WAAPI) | 未收录 | 当你要零依赖且能接受底层代码时，选原生 WAAPI；当你需要时间线、stagger、SVG 和更顺手的序列编排时，选 Anime.js。 | 浏览器原生 API，无需打包任何库；更底层，没有时间线/stagger/SVG-morph 的语法糖。Anime.js v4 内含 WAAPI 适配器并在其上叠加易用层。 |
| CSS `@keyframes` / transitions | 未收录 | 简单 hover、loading 或一次性效果选 CSS transition/keyframes；只有需要运行时控制、序列或动态数值时，才选 Anime.js。 | 零 JS，简单场景对 GPU 友好；但无法做序列、动态数值或运行时控制。Anime.js 用于需要 JS 驱动编排的场景。 |
| Velocity.js | 未收录 | 只有维护既有 jQuery 时代代码库、需要兼容遗留动画时，才选 Velocity.js；新写现代 vanilla 动画选 Anime.js。 | jQuery 时代的老牌 JS 动画器，如今基本停止维护。Anime.js 是其活跃维护的现代等价物。 |

## 技术栈

- **语言：** JavaScript（原生；无 TypeScript 运行时要求，对外提供类型定义）。
- **可驱动的目标：** CSS 属性、SVG 元素、DOM/HTML 属性，以及任意 JavaScript 对象数值。
- **v4 模块：** `Timer`、`Animation`（`animate`）、`Timeline`（`createTimeline`）、`Animatable`、`Draggable`、`Scope`、`ScrollObserver`（滚动联动）、`SVG`（`morphTo`、`createDrawable`、`createMotionPath`）、`Text`（`splitText`、`scrambleText`），外加 `stagger`、弹簧/内置缓动，以及 WAAPI 适配器。另提供 Three.js 适配器用于驱动 3D 数值。
- **构建/分发：** 模块化 ESM 支持 tree-shaking；UMD/IIFE 包供 `<script>` 使用。npm 包名为 `animejs`。
- **依赖：** 运行时零依赖——引擎自包含。

## 依赖

- **运行时：** 浏览器 DOM 环境（若仅补间普通对象，则任意 JS 运行时即可）。无外部运行时依赖。
- **安装：** `npm install animejs`（包名 `animejs`，v4.5.0），或通过 `<script>` / CDN 加载 UMD/IIFE 构建。
- **构建工具：** 消费端无强制要求；任意打包器（Vite、webpack、esbuild、Rollup）或不打包都可用。框架集成（React/Vue/Svelte）无需专用适配器——在 effect/生命周期钩子里调用 API 即可。

## 运维难度

**低。** 这是一个纯客户端库，没有服务端、没有数据存储、没有需要运维的基础设施——「运维」就缩减为分发一个 JS 包。采用成本主要在学习 v4 模块 API，以及对老用户而言迁移 v3 代码（一次非平凡的重构，而非升版本号）。性能/维护负担是常规前端那种：尽量把重动画移出主线程、留意 layout thrash、锁定主版本以避免意外的 API 漂移。

## 健康度与可持续性

- **响应速度**：无法计算——unknown。
- **维护（2026-06）。** 最后 push 于 2026-06；v4.5.0（2026-06-22）紧随 v4 大版本重写——处于**活跃**，未归档。约 110 的低 open issue 数，对这么广泛使用的库而言是健康的。[推断]
- **治理 / bus factor。** 一个**单作者、`User` 个人账号所有的仓库**（`juliangarnier/anime`），约 70k star——典型的 bus-factor 标记：巨大的采用度压在一个维护者身上，背后没有基金会或厂商。[推断]
- **年龄与 Lindy 判断。** 约 10 年（2016-03 创建）且**仍在活跃发布**（刚完成一次完整的 v4 重写）⇒ **强 Lindy** 信号——十年存续加一个全新大版本，是停滞项目的反面，这大大缓和了单维护者的担忧。[推断]
- **采用度。** 非常强（约 70k star，MIT，零依赖，框架无关，npm 包名 `animejs`）——命令式 Web 动画的默认档次选择。[未验证]
- **风险标记。** 未发现 relicense 或 open-core（全程 MIT）。具体代价是 **v3→v4 迁移**——一次真实的 API/模块重写，而非原地升版本；请锁定主版本。[推断]

## 存疑（未验证）

- [未验证] star 数据报告约 70.4k（截至 2026-06）；最新发布 v4.5.0 于 2026-06-22（据 GitHub API）。GitHub star 不可靠且对日期敏感——仅作参考，请对照仓库重新核实。
- [未验证] v4 模块清单（Timer / Animation / Timeline / Animatable / Draggable / Scope / ScrollObserver / SVG / Text，WAAPI + Three.js 适配器）取自文档站结构；在依赖某个具体模块前，请对照当前文档核实确切集合与 import 路径。
- [未验证]「运行时零依赖」是从 npm 元数据无 `dependencies` 字段推断而来；请对照你所装版本的 `package.json` 确认。
- [未验证] 所读 README/文档页未声明打包体积与浏览器支持矩阵；在做预算前请从构建产物或 bundlephobia 核实实际 gzip 体积与支持范围。
- [推断] 横向对比的结论（GSAP 生态广度、Framer Motion 的 React 契合度、Motion One 的 WAAPI 体积、Velocity.js 已停维护）是基于对这些库的一般认知所做的判断，并非此处实测——请重新核对各替代方案的现状。
- [未验证] v3→v4 的迁移成本被描述为一次真实重构，依据是它属于 API/模块重写；确切的破坏性变更面应对照项目迁移指南核实。
