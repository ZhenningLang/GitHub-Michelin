---
name: React Doctor
slug: react-doctor
repo: https://github.com/millionco/react-doctor
category: ai-code-review
tags: [react, static-analysis, agent-skill, oxlint, code-review, linter]
language: TypeScript
license: LicenseRef-Modified-MIT
maturity: oxlint-plugin-react-doctor@0.5.8, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T11:33:33Z
  default_branch: main
  default_branch_sha: e2393c4a6b842efc72d5c225273c0de918a13450
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:56:44Z
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.2
        qualifying_issues: 55
        band: relaxed_solo
        window_offset_days: 7
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: oxlint-plugin-react-doctor
        dependent_repos_count: 0
        downloads_last_month: 5826524
        graph_tier: E
        volume_tier: A
        cross_check_divergence: 1.04
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 221
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 17
        top1_share: 0.65
        top3_share: 0.935
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# React Doctor

一个面向 React 的确定性静态分析器，专抓 coding agent 写出来的烂 React 代码——既能用 `npx` 一次性审计，也能装成 agent skill、装成 oxlint/ESLint 插件，或接进 CI。

![react-doctor — 健康度雷达](../../assets/health/react-doctor.zh.svg)

## 何时使用

你是前端工程师，正让某个 coding agent（Claude Code、Cursor、Codex、OpenCode）给 Next.js 或 Vite 应用批量生成 React 组件。diff 看起来都挺合理、测试也过，但 agent 老是在不该用的地方塞 `useEffect`、拿数组下标当 key、每次 render 都重建对象，还悄悄引入只有在 review 时——甚至上线后——才发现的可访问性和安全回归。你想要一道快、可重复的关卡，精准标出这些 React 特有的错误，而不用自己逐行重读。于是你跑 `npx react-doctor@latest`，得到一份覆盖 state & effects、性能、架构、安全、可访问性的确定性审计——同样的输入永远给出同样的结论，因此可复查、也适合进 CI。

更大的价值是把回路接到 agent 自身。首轮审计后，你用 `npx react-doctor@latest install` 把它装成 agent 的 skill，这样后续改动都会对照同一套规则检查，agent 也会学着去修（并不再反复重犯）它刚犯的那些问题。由于它同时提供 oxlint 与 ESLint 插件、一个 language server，以及 VSCode/Zed 扩展，同一套规则可以同时活在你的编辑器和 GitHub Actions 的 PR 扫描里——一套一致的 React 规则贯穿 agent、编辑器和 CI，而不是每次都靠 LLM reviewer 重新判一遍代码。

## 何时不用

- **你写的不是 React。** 它就是为 React 设计的（覆盖 Next.js、Vite、TanStack、React Native、Expo）——但对 Vue、Svelte、Angular 或后端代码它什么都做不了。那些场景请换通用 reviewer。
- **你要的是任意语言、意图层面的语义审查。** React Doctor 是确定性地跑一套固定的 React 规则目录，不是一个能用自然语言推理业务逻辑、命名、架构的 LLM。要 LLM 驱动、语言无关的审查，看 [open-code-review](open-code-review.zh.md) 或 [claude-code-security-review](claude-code-security-review.zh.md)。
- **安全是你的首要诉求。** 它有安全类别，但本质是一个覆盖面广的 React linter，不是专门做漏洞/污点分析的安全 reviewer。专门的安全工具在认证、注入、数据流上会挖得更深。
- **对 license 敏感 / 需要 vendored 构建。** 它的 license 是 **Modified MIT**（不是标准 SPDX 的 MIT）：额外加了限制——尤其涉及把软件用于 AI 训练/微调，以及商业托管——所以别把它当成宽松的 MIT 依赖直接用，先读真实条款。[推断] 这在二次分发或自建竞品服务时可能要紧。
- **你需要规则稳定 / 冻结的 API。** 它还在 1.0 之前、迭代很快（多包、发版频繁）；规则和配置（`doctor.config.ts`）可能在版本间变化，所以一旦 CI 闸门依赖精确结论，请 pin 版本。
- **你不想引入一套多包工具链。** 仓库是个 Turbo monorepo（core、api、language-server、oxlint/ESLint 插件、编辑器扩展、CLI）。如果你只想 import 一个单库，它的表面积比你需要的大。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [open-code-review](open-code-review.zh.md) | ✅ | 当你需要语言无关的 LLM 对 PR 逻辑做语义判断时，选 open-code-review；当闸门必须是可重复的 React 专属 agent 易错规则时，选 React Doctor。 | LLM 驱动、语言无关的 PR 审查（阿里巴巴）；用自然语言推理逻辑。React Doctor 是确定性、仅限 React、基于规则——可重复但没有语义判断。 |
| [claude-code-security-review](claude-code-security-review.zh.md) | ✅ | 当安全漏洞推理是首要任务时，选 claude-code-security-review；当目标是覆盖 React lint、性能、可访问性和正确性时，选 React Doctor。 | 基于 Claude、聚焦安全的审查（Anthropic）；深入、语言无关的漏洞推理。React Doctor 是覆盖面广的 React linter，不是专门的安全分析器。 |
| eslint-plugin-react-hooks / react | 未收录 | 当你只要官方 React lint 规则和最小概念表面积时，选官方插件；当 agent-skill 工作流和额外的 agent 易错规则才是价值时，选 React Doctor。 | React 官方 lint 规则；React Doctor 与之有重叠，但额外提供 agent-skill 工作流、oxlint 插件，以及超出官方集的「agent 易犯错」规则。 |
| oxlint | 未收录 | 当需求只是高速 Rust linter 宿主时，选 oxlint；当你需要能经 oxlint 运行的 React 专属规则包时，选 React Doctor。 | React Doctor 为之提供插件的高速 Rust linter;oxlint 是引擎/宿主，React Doctor 供给面向 agent 的 React 专属规则包。 |
| Biome | 未收录 | 当你需要 JS/TS 一体化格式化和广覆盖 lint 时，选 Biome；当决定性需求是抓 agent 写出的 React 反模式时，选 React Doctor。 | 一体化的 Rust 格式化+lint;JS/TS lint 覆盖广，但不专门针对「抓 agent 写的 React 反模式」。 |

## 技术栈

- **语言：** TypeScript(ESM,`"type": "module"`)。
- **Monorepo:** Turbo 管理的多包——`core`、`api`、`language-server`、`oxlint-plugin-react-doctor`、`eslint-plugin-react-doctor`、`react-doctor`(CLI)、`vscode-react-doctor`、`zed-react-doctor`、`deslop-cli`、`deslop-js`、`website`。
- **Lint 引擎：** 同时提供 **oxlint** 插件和 **ESLint** 插件（最新发布是 `oxlint-plugin-react-doctor@0.5.8`）。
- **编辑器/IDE:** 一个 language server，外加 VSCode 与 Zed 扩展。
- **分发：** CLI 走 `npx react-doctor@latest`;agent skill 走 `npx react-doctor@latest install`;CI 走 `npx react-doctor@latest ci install`（GitHub Actions PR 扫描）。配置在 `doctor.config.ts`。
- **构建/开发工具：** vite-plus、Changesets（发版）、ts-json-schema-generator。

## 依赖

- **运行时：** Node.js + 包运行器（`npx`/pnpm）。没有数据库或要托管的服务——它是本地/CLI 静态分析器。
- **引擎：** 走 oxlint 插件路径时需要 oxlint；走 ESLint 插件路径时需要 ESLint。[推断] 通过 CLI 的核心分析不需要单独引擎，但插件路径需要其宿主 linter。
- **项目：** 一个现成的 React/TypeScript 代码库可供扫描（声明支持 Next.js、Vite、TanStack、React Native、Expo）。
- **安装：** 一次性审计零常驻安装（`npx react-doctor@latest`）;skill/CI 安装器会往你的仓库/agent 写入配置和 skill 文件。

## 运维难度

**低。** 常见用法就是一条 `npx` 命令，没有要部署、托管或维护的东西——无服务、无数据存储、确定性输出，天然适合接进 CI。难度只会轻微上升：把它接成 GitHub Actions 闸门、调 `doctor.config.ts`，或把 oxlint/ESLint 插件并进既有 lint 配置时，需要 pin 版本和调和配置。它 1.0 之前、多包的特性意味着：一旦 CI 闸门依赖精确结论，就该 pin 版本。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 0.2 小时，基于 55 个 qualifying issues/PRs。
- **维护（2026-06）：** [推断] 维护活跃——仓库最近 push 在 2026-06-25，插件 `oxlint-plugin-react-doctor@0.5.8` 于 2026-06-20 发布，通过 Changesets 频繁做多包发布。约 13k star 下未关闭 issue 约 44，偏低。截至 2026-06 势头健康。
- **治理与背书：** [推断] 归属 `millionco` 组织（Million.js 背后的团队，一个有名的 React 性能项目），因此背后是一个成型的 React 工具链组织与品牌，而非孤身爱好者——bus-factor 低于单人维护仓库。但仍是单一厂商，非基金会治理。
- **年龄与 Lindy：** [推断] 创建于 2026-02，截至 2026-06 约 4 个月——**非常年轻；无 Lindy 记录。** 它在 1.0 之前、在一个多包 monorepo 上快速迭代，所以规则目录和 `doctor.config.ts` 可能在版本间变动；一旦 CI 闸门依赖精确结论，请 pin 版本。
- **风险标记：** [推断] **许可证是最突出的标记**——`LicenseRef-Modified-MIT`（gh 报为「Other」），额外加了围绕 AI 训练/微调和商业托管的非标准限制。在二次分发或自建竞品服务时，**别**把它当宽松 MIT；请读真实 LICENSE。未观察到 CVE。

## 存疑（未验证）

- [未验证] star 约 13.1k（截至 2026-06）;GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 最新发布 `oxlint-plugin-react-doctor@0.5.8` 于 2026-06-20；仓库最后 push 于 2026-06-25。各子包（CLI、core）版本可能与该插件 tag 不同。
- [未验证] 此处未穷举完整规则目录；README 列了类别（state & effects、性能、架构、安全、可访问性）和一个示例规则（`react-doctor/no-array-index-as-key`）——具体规则集请对照当前仓库核实。
- [推断] 「Modified MIT」license 加了非标准限制（AI 训练/微调、商业托管）;`gh` 把 license 报为「Other」。涉及 license 影响时，请以阅读真实 LICENSE 为准，别假定是 MIT。
- [推断] agent-skill 的「学习」指 agent 读取已安装的规则/skill 文件并据此修复，而非模型权重训练；不同 agent 上的行为不保证一致。
- [未验证] 框架支持声明（Next.js/Vite/TanStack/React Native/Expo）来自项目自述，未经独立基准验证。
