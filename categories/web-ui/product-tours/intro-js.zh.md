---
name: Intro.js
slug: intro-js
repo: https://github.com/usablica/intro.js
category: product-tours
tags: [product-tour, onboarding, walkthrough, feature-highlight, spotlight, commercial, licensing]
language: JavaScript
license: AGPL-3.0
maturity: v7.x, active, ~22k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-01-04T18:23:52Z
  default_branch: master
  default_branch_sha: b50a24316febe87e9ee430542587c6ece5ab4cad
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:19:45Z
  overall: B
  overall_score: 3.2
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
        last_commit_age_days: 1
        active_weeks_13: 6
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.0
        qualifying_issues: 22
        band: default
        window_offset_days: 1
        source: pr
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: intro.js
        dependent_repos_count: 1272
        downloads_last_month: 696730
        graph_tier: B
        volume_tier: B
        cross_check_divergence: 1.04
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4944
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Intro.js


一款成熟、框架无关的 JavaScript 库，用于分步产品引导、功能高亮与用户 onboarding——它是现存最古老、使用最广的引导库之一，但附带**双协议授权**（非商用采用 AGPL-3.0，商用/闭源需购买商业授权），这一点在绝大多数选型决策中都是决定性门槛。


![Intro.js — health radar](../../../assets/health/intro-js.zh.svg)

## 何时使用

你是某开源教育平台的前端开发者，需要引导新用户熟悉界面：在仪表盘上放一个欢迎提示，高亮“创建课程”按钮，再一步一步带用户走完评分工作流——每一步都带进度指示器和键盘导航。你的站点是原生 HTML 和原生 JS，没有 React，也没有 Vue，你想要一个不需要框架绑定、没有运行时依赖的引导库。你还想要详尽的文档和丰富的示例，以便快速上手。于是你选了 Intro.js：加一个 `<script>` 标签或 `npm install intro.js`，给 DOM 元素加上 `data-intro` 和 `data-step` 属性，调用 `introJs().start()`，它就渲染出引导遮罩、提示气泡和进度条——没有构建工具的麻烦，也没有框架锁定。

当你需要自动播放的引导、编程式步骤控制，或者跨页面导航仍能持久化的多页引导流程时，你也会选它。因为它自 2013 年起就在持续维护，API 稳定、文档全面，这对需要理解和扩展引导逻辑的新贡献者团队来说尤为重要。

## 何时不用

- **你在构建商用或闭源产品，且没有购买商业授权。** Intro.js 在非商用场景下采用 AGPL-3.0，商用必须购买付费授权。这不是脚注——而是具有法律约束力的要求，已有公司因把它当作“GitHub 上就是免费”而陷入合规纠纷。[未验证]
- **你想要完全宽松（MIT）的授权，不想面对授权摩擦。** Driver.js 和 Shepherd.js 都是 MIT 授权，可以完全避开 AGPL/商业授权的分叉。如果你的法务团队对 copyleft 敏感，或者你不想在团队成员间追踪授权合规，请直接选它们。
- **包体积是你的绝对硬约束。** Intro.js gzip 后约 10KB——比 Driver.js（约 5KB）大，与 Shepherd.js 相当。如果只是对单个元素做一次高亮，这个开销可能不划算。
- **SPA 里高度动态/异步的 DOM。** 步骤靠选择器锚定元素。如果元素还不存在（路由未挂载、数据仍在加载、虚拟列表、模态框正在动画进入），引导就会指向空或乱跳。你得自己写定时/`MutationObserver` 胶水去等元素，并在滚动/缩放时重新定位。[推断]
- **严格的无障碍/键盘/读屏要求。** 遮罩加聚光式引导是公认的 a11y 雷区（焦点陷阱、注入气泡上的 `aria-*`、键盘导航、reduced-motion）。请对照你的 WCAG 标准核实当前版本的无障碍行为，别假设它已经处理好了。[未验证]
- **你需要的是完整的 onboarding/采用*平台*，而不只是引导。** Intro.js 只渲染引导；它没有人群分层、没有埋点分析、没有 A/B 定向、没有 checklist、也没有问卷。要这些，你要的是 Appcues / Userflow / Userpilot（商业产品）——或者自己搭那层状态/ feature-flag。
- **你需要开箱即用的深度引导分支/条件流程。** 复杂的多路径引导（按用户操作分支、跳步、稍后续接）能做，但要靠你自己的代码编排；这个库给的是步骤加一套命令式 API，而不是一个流程引擎。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Driver.js](driver-js.zh.md) | ✅ | 需要 MIT 授权、更轻、零依赖的替代品时，选 Driver.js。 | MIT 授权，包体积更小（约 5KB），零依赖；但内置功能和定位选项比 Intro.js 少。 |
| [Shepherd.js](shepherd-js.zh.md) | ✅ | 需要 MIT 授权、API 更丰富、定位选项更多的引导库时，选 Shepherd.js。 | MIT 授权，内置步骤/定位选项更多、API 更丰富；用 Floating UI / popper 风格定位，比 Driver.js 更重。 |
| [Reactour](reactour.zh.md) / [react-joyride](react-joyride.zh.md) | ✅ | 需要 React 专属的 hooks 或 JSX 原生引导组件时，选 Reactour / react-joyride。 | React 专属组件（hooks/JSX 原生）；在 React 内 DX 更好，但被框架锁定，对比 Intro.js 的 vanilla 内核。 |
| Appcues / Userflow / Userpilot | 未收录 | 需要商业无代码 onboarding **平台**时，选 Appcues、Userflow 或 Userpilot。 | 商业平台——分层、分析、定向、checklist、问卷；不是开源仓库，有持续的 SaaS 订阅成本。 |
| Bootstrap Tour | 未收录 | 新项目不要选 Bootstrap Tour；它已弃用且不再维护。 | 已弃用；曾是依赖 Bootstrap 的引导插件，现已不再维护。 |

## 技术栈

- **语言：** JavaScript（ES5+），编译成一个 JS bundle（npm 上发布 ESM + UMD 两种构建）。
- **渲染：** 纯 DOM + CSS——直接向页面注入遮罩、提示气泡和高亮聚光，相对目标元素定位，并暴露命令式 `introJs()` API（`start()`、`goToStep()`、`exit()` 以及生命周期回调）。
- **依赖：** 运行时零依赖——纯 JavaScript 库，无任何框架依赖或外部库。
- **主题：** 通过 CSS class 覆盖和自定义主题来定制样式，以贴合宿主设计系统。

## 依赖

- **运行时：** 无。一个 `<script>` 标签（CDN/UMD）或 `npm install intro.js` 导入即可；它完全在浏览器端运行，无后端、无服务。
- **构建（应用作者侧）：** 一个能解析该 npm 包的打包器（Vite/webpack/esbuild/Rollup），同时导入它的 JS 和 CSS；可无框架使用，也可嵌入任意框架（React、Vue、Angular、Svelte）。
- **浏览器：** 现代常青浏览器；具体的最低/旧版支持取决于版本——请对照你的目标浏览器矩阵核实。

## 运维难度

**低。** 这是个客户端库，不是服务——没有任何东西要部署或运维。这里的“运维“只是：加上依赖、把 JS+CSS 打进你的 bundle，就完事了；没有服务器、没有数据存储、没有扩容问题。真正的成本在于你自己应用里的**集成/维护**：定义步骤、在 UI 变化时让选择器保持同步（你一改类名或重构 DOM，引导就会无声地坏掉）、处理 SPA 时序、做主题。这些都不是运维负担——而是你自己拥有并要测试的前端代码。

**授权**才是实质上的运维/政策考量：如果你在商用产品中使用 Intro.js，必须购买并追踪商业授权，且法务/合规团队必须知晓 AGPL 的边界。这是一个 MIT 授权替代品（Driver.js、Shepherd.js）不会带来的持续性流程成本。

## 健康度与可持续性

- **维护（2026-07）。** 活跃于 v7.x，持续发版；GitHub 约 22k star，长期社区使用。未归档。[未验证]
- **年龄与 Lindy 判断。** 2013 年创建（约 13 年）且**仍在活跃维护**⇒ 一个**非常强劲的 Lindy** 信号——JavaScript 生态里最长寿、最经实战检验的引导库之一。用年龄 × 仍活跃来看：授权模式才是对冲风险，年龄本身不是。[推断]
- **治理 / bus factor。** 由 `usablica`（原作者 Afshin Mehrabani 的组织）维护。该项目比许多竞争对手活得更久，贡献者基础也比单维护者项目更广泛。[未验证]
- **采用度与生态。** 在 Web 上被广泛采用；文档详尽、示例丰富、社区认知度高。由于授权模式，商业采用被分成“已购买授权的用户”和“迁移到 MIT 替代品的用户”两类。[推断]
- **风险标记。** **双协议授权**（AGPL-3.0 / 商业授权）是首要风险标记。已有公司因忽视商业授权要求而陷入合规纠纷。在承诺前请核实当前定价与条款；确认你的使用场景属于非商用豁免，还是需要付费授权。[未验证]

## 存疑（未验证）

- [未验证] 截至 2026-07 约 22k GitHub star——star 数对时间敏感，作为健康度代理并不可靠，仅供参考。
- [未验证] bundle 体积（“约 10KB gzip”）是近似值，随版本/构建而变（ESM 还是 UMD、含不含 CSS）——请对照你实际的构建去测量。
- [未验证] 商业授权价格引述为约 $20–50 一次性或订阅（视方案而定）——请在预算前直接到 Intro.js 官网核实当前定价。
- [未验证] 双协议授权模式及其执行史基于对项目授权条款的一般了解；在依赖这一区别前，请直接确认当前的授权文本与商业条款。
- [推断] SPA 时序/动态 DOM 的摩擦，以及 a11y/键盘/读屏行为，都是从遮罩式引导库的一般工作方式推断而来——请对照你为具体应用锁定的版本和 WCAG 标准核实。
- [推断] “治理 / bus factor”和“更广泛的贡献者基础”判断基于 GitHub 可见度与项目 longevity，而非对贡献者分布或治理文档的详细分析。
