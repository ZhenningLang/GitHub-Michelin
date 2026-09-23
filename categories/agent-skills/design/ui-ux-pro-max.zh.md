---
name: UI UX Pro Max Skill
slug: ui-ux-pro-max
repo: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
category: design
tags: [ui-ux, design-intelligence, design-system, agent-skill, multi-harness]
language: Python
license: MIT
maturity: v2.8.8, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-28T02:27:08Z
  default_branch: main
  default_branch_sha: 8a81ed60272d21d4b8808f7308d49a0b1b000555
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:38:21Z
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
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 8543
        release_assets: 7
        release_tier: D
        signal_basis: releases
    longevity:
      grade: B
      raw:
        repo_age_days: 296
        last_commit_age_days: 1
        cohort: skill-pack
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 92
        top1_share: 0.232
        top3_share: 0.414
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
    responsiveness: { reason: type_na }
---

# UI UX Pro Max Skill

一个设计智能 skill pack，给你的 coding agent 注入 UI/UX 品味——一个本地检索引擎，覆盖数百条行业推理规则、UI 风格、配色方案和字体搭配，在你让它构建界面时自动触发，并附带一份交付前质量清单。

![ui-ux-pro-max — 健康度雷达](../../../assets/health/ui-ux-pro-max.zh.svg)

## 何时使用

你是一名偏后端（或全栈）的开发者，正在做一个 SaaS 产品。你让 coding agent “做一个落地页”或“做一个设置页面”，拿回来的东西技术上没错，但视觉很平庸——默认的 Tailwind 间距、emoji 当图标、没有真正的层级、和每个 AI 都会产出的同款渐变 hero。你看得出这是 AI 味儿，却没有设计词汇去说清*为什么*、也没法精确指挥怎么改。你希望 agent 自己就能做出有依据的设计决策：给金融科技和美容 spa 选出各自匹配的风格、有意图地挑配色和字体搭配、遵守 WCAG 对比度和 reduced-motion、避开已知的反模式。

UI UX Pro Max 就是把这种判断力装进 agent。你跑 `npm install -g ui-ux-pro-max-cli` 再 `uipro init --ai claude`（或 cursor、windsurf、copilot、codex、kiro……），它会落下一个 skill 目录：markdown manifest 加上一个内置的 Python `search.py`，背后是 CSV 数据库（据 README：161 条推理规则、67 种风格、161 套配色、57 组字体搭配）。之后当你发出自然的 UI/UX 请求时，skill 自动激活：做一次多域检索（产品类型 → 模式、色彩情绪、排版、反模式），生成一份可持久化到 `design-system/MASTER.md` 的设计系统，并在声称完成前跑一遍清单（WCAG AA 对比度、375–1440px 断点、focus 状态、不用 emoji 图标）。高级用户也可以直接调用 `search.py`。它完全本地运行——只依赖 Python 3，无服务端、无外部 API。[推断]

## 何时不用

- **你已经在用一个信任的 UI/设计 skill 或设计系统契约。** 这个 pack 对风格、配色和“规则”有强主张；把它叠在已有的品味 skill 或项目 `DESIGN.md` 之上，会制造两个事实源和互相冲突的指令。设计权威只留一个。
- **你想要一个组件库或可直接 import 的成品 UI。** 它交付的是*设计智能和生成指导*，不是 React/Vue 组件——没有东西可 `import`。产出是 agent 写出的代码加一份 markdown 设计系统，而不是打包好的 UI kit。
- **你的 harness 加载不了 skill 或跑不了 Python。** 激活依赖各平台的 skill 加载机制，检索后端需要机器上有 Python 3。在没有 skill loader 的 harness、或没有 Python 的沙箱里，光有 markdown 不会自动触发，搜索引擎也跑不起来。
- **你需要的是强制约束，而非建议。** 那份清单（对比度、断点、不用 emoji）和风格规则是 prompt 层的建议性指导，agent *应该*遵守——但它们不是硬性 gate、linter 或 CI 检查。agent 仍可能交付违反它们的东西。[推断]
- **快速迭代的单厂商上游。** 频繁发版（v2.8.x）加上行为固化在 prompt/CSV 数据里，意味着一次版本升级就可能改变哪些风格、规则或清单项生效。如需可复现的设计产出，请锁版本。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [designer-skills](designer-skills.zh.md) | ✅ | 需要本 leaf 内另一套 UI/UX 设计 skill pack，且偏纯 prompt 指导时，选 designer-skills。 | 本 leaf 内的同类 UI/UX 设计 skill pack；对比点在于它是否带检索引擎 + 规则数据库，还是纯 prompt 指导。 |
| [stitch-skills](stitch-skills.zh.md) | ✅ | 同 leaf 设计包里，更需要设计生成/转换链路时，选 stitch-skills。 | 同 leaf 的设计 skill pack；生成面不同——衡量哪个更贴合你的技术栈（HTML/Tailwind/React）和 harness。 |
| [taste-skill](taste-skill.zh.md) | ✅ | 只需要聚焦视觉*品味*/评审的 skill，而不是端到端规则库时，选 taste-skill。 | 同 leaf 中聚焦视觉*品味*/评审的 skill；与本 pack 这类偏生成的 skill 是互补而非替代关系。 |
| [make-interfaces-feel-better](make-interfaces-feel-better.zh.md) | ✅ | 主要需求是已有界面的打磨/手感，而不是产品类型到设计系统流水线时，选 make-interfaces-feel-better。 | 同 leaf 中针对已有界面打磨/手感的 skill；范围比本 pack 的“产品类型→设计系统”流水线更窄。 |
| Anthropic / 内置 agent skills 和 slash command | 未收录 | 只想用平台原生 skill/command，避免第三方 bundle 与原生设计助手重复时，选内置生态。 | 平台原生的 skill 生态；本项目是叠在其上的第三方 bundle，可能与原生设计助手重复或冲突。 |
| 手写的项目 `DESIGN.md` 设计系统 | 未收录 | 需要逐项目、可强制执行且完全自维护的设计契约时，选手写 `DESIGN.md`。 | 你自己维护的逐项目设计契约；更贴合、更稳定，但需要你自己搭建并强制执行，而不是直接拿到一套 161 条规则的起点。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 活跃且迭代快——最后 push 于 2026-06，最新 release v2.8.8，v2.8.x 发版频繁，未归档。有规整的 semver 是加分项，但快节奏意味着一次升级就可能改变哪些风格／规则／清单项生效。
- **治理与背书：** 仓库归 `Organization`（`nextlevelbuilder`）所有，但本质是单厂商项目——一个组织掌控路线图、风格与 CSV 规则数据，没有 foundation。[推断]
- **年龄与 Lindy：** 创建于 2025-11，截至 2026-06 远不足一年——年轻且被 star 重度炒热（约 97k）。Lindy 维度未经检验；star 数不是耐久信号。
- **风险标记：** 建议性约束（prompt/markdown 加一个本地 CSV 搜索步骤，而非硬闸门）；行为固化在 prompt/CSV 里 ⇒ 要可复现的设计产出就锁版本。

## 存疑（未验证）

- [未验证] 最新 release 报告为 v2.8.8（2026-06-26 发布），仓库最后 push 于 2026-06-26；license 为 MIT、主语言为 Python，均依据 2026-06-26 的 GitHub 元数据——依赖某个具体版本行为前请重新核实。
- [未验证] Star 数（2026-06-26 GitHub 显示约 96.6k）不可靠且对日期敏感；仅作参考，不作为质量信号。
- [未验证] 数据集规模（161 条推理规则、67 种 UI 风格、161 套配色、57 组字体搭配、99 条 UX 指南、25 种图表类型）以及支持的 harness 列表（Claude Code、Cursor、Windsurf、Antigravity、GitHub Copilot、Kiro、Codex CLI、Continue、Gemini CLI 等）取自项目 README，此处未独立清点/确认。
- [未验证] 安装路径是 npm 包 `ui-ux-pro-max-cli`，由它生成 skill 文件；“生成的 skill 在内部调用 `search.py`”（而非用户总是手动调用）是依据 README 描述的架构，未单独验证。
- [推断] 由于设计规则和交付前清单都活在 prompt/markdown skill 及一个本地 CSV 驱动的搜索步骤里，约束是建议性的——agent 仍可能偏离或交付不合规的 UI；“清单”项是指导而非硬性保证。
- [推断] “完全本地运行、只需 Python 3、无外部依赖”出自 README；在具体沙箱上的实际行为（Python 是否可用、生成 skill 目录的写权限）此处未确认。
