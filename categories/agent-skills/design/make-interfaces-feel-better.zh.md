---
name: make-interfaces-feel-better
slug: make-interfaces-feel-better
repo: https://github.com/jakubkrehel/make-interfaces-feel-better
category: design
tags: [skills, ui-polish, micro-interactions, css, animations, typography, claude-code]
language: Markdown
license: MIT
maturity: no tagged release, active (last pushed 2026-04; ~1.9k stars [未验证])
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-04-19T15:27:44Z
  default_branch: main
  default_branch_sha: 384562064fcdd99778fcbafd8729626fe6aab02f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:46:30Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 24
        active_weeks_13: 4
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 194
        last_commit_age_days: 24
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
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
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# make-interfaces-feel-better

一个单一、聚焦的 agent skill，把约 16 条具体的 UI 打磨原则——同心圆角、可中断过渡、等宽数字、入场/出场动画、视觉对齐、字体平滑——注入你的 coding agent，让它交付的界面「感觉」做完了，而不只是「功能正确」。

![make-interfaces-feel-better — 健康度雷达](../../../assets/health/make-interfaces-feel-better.zh.svg)

## 何时使用

你是一名前端开发（或 vibe-coder），用 Claude Code 写一个组件或页面，代码功能上没问题，但成品显得廉价：弹窗的内圆角没有嵌进外圆角里；数字跳动时因为字体不是等宽而抖动；hover 动画无法被打断、于是显得卡顿；图标直接弹出、没有入场过渡；明明用一道克制的描边会更利落，却用了阴影。你知道「哪里不对」，但不想在每条 prompt 里手写同一份 15 项的「让它更精致」清单。于是你装上 `make-interfaces-feel-better`,agent 加载一份 `SKILL.md`，把这些细节作为有命名、带代码的规则带进来（含具体数值，如按下时 `scale(0.96)`、约 100ms 错峰延迟），外加一份它能对着刚写好的 diff 自查的 review checklist。

你专门在「差距是工艺级细节、而非方向」时用它。它不替你选配色、不帮你发明布局——它把那些小而机械的修正（排版、表面、动画、性能）编码下来，这正是「看着像 LLM 生成」的界面和「显得是有意为之」的界面之间的分水岭。该 skill 源自作者的「Details that make interfaces feel better」一文，并拆成四个子文件（`typography.md`、`surfaces.md`、`animations.md`、`performance.md`），agent 按需读取以获取更深指引。[推断]

## 何时不用

- **你已经在跑更宽的设计 skill 包。** 如果已加载 [taste-skill](taste-skill.zh.md) 或 [designer-skills](designer-skills.zh.md)，你会在动效、排版、anti-slop 上拿到重叠（甚至冲突）的指令——本 skill 更窄（只做细节打磨），叠在上面有双重路由的风险。按你需要的层级选其一。
- **你要的是设计*方向*，不是细节。** 它不会选配色、不会搭设计系统、不做 UX 调研、不评 IA。如果你的页面平淡是因为缺概念，一份打磨清单救不了它——去找更宽的包。
- **你的 harness 没有 skill 加载机制。** 它通过 agent 的 skill 机制激活（README 给出 `npx skills add jakubkrehel/make-interfaces-feel-better`）。在没有 loader 的 harness 上，这份 markdown 只是一篇文章，不会自动对你的 diff 生效。
- **强制力是建议性的。** 规则活在 prompt/markdown 里，agent 仍可能跳过或错用。「用等宽数字」是一条指令，不是 lint 门禁——若要硬保证，请配一个真正的 CSS/UI linter。[推断]
- **单作者、无 release、更新节奏偏低。** 最近一次 push 是 2026-04，无 tagged 版本；它是一份薄而有主见、绑定单篇文章的产物。若那篇文章的主张不合你的设计语言，这个 skill 不会迁就。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [taste-skill](taste-skill.zh.md) | ✅ | 页面方向仍平淡、需要更宽的 anti-slop 视觉品味包时，选 taste-skill。 | 更宽的「anti-slop 视觉品味」包：推断设计方向、映射完整的色/字/间距系统、铺 GSAP 动效骨架。本 skill 更窄——机械的细节打磨，不定方向。页面平淡时用 taste-skill；方向已 OK 但不够精细时用本 skill。 |
| [designer-skills](designer-skills.zh.md) | ✅ | 需要完整设计生命周期套装，而不是单一工艺细节清单时，选 designer-skills。 | 完整设计*生命周期*套装（97 个 skill：调研、IA、设计系统、批评）。偏重、偏流程；本 skill 是单一工艺细节清单，几乎零仪式。 |
| [ui-ux-pro-max](ui-ux-pro-max.zh.md) | ✅ | 需要更大的端到端 UI/UX skill 套装时，选 ui-ux-pro-max。 | 更大的 UI/UX skill 套装，面向端到端界面质量。比表面积：本 skill 是一份紧凑的、源自文章的规则集，不是多 skill 系统。 |
| [stitch-skills](stitch-skills.zh.md) | ✅ | 想比较同叶目录里更偏设计生成/转换链路的包时，选 stitch-skills。 | 同叶目录的设计 skill 包；比较各自「强制 vs 建议」的阶段，以及动效/排版指引是否重叠。 |
| 写在自己 `CLAUDE.md` / prompt 里的手写设计清单 | 未收录 | 想完全自维护规则、避免引入第三方 skill 包时，选手写设计清单。 | DIY 方案；同样是建议性的，但由你维护。本 skill 把一份已知好用的细节清单打包，省得你每个项目重新推导。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 节奏低、可能已沉寂——最后 push 于 2026-04（截至 2026-06 约停 2 个月），无打 tag 的 release。对一份薄、绑定单篇文章、本就「做完了」的产物，这尚可接受，但别指望持续迭代。
- **治理 / bus factor：** 单作者、`User` 所有的仓库（`jakubkrehel`），约 1.9k stars。它是一个人从自己「Details that make interfaces feel better」一文里结晶出的主张——无团队、无组织。
- **年龄与 Lindy 判断：** 非常年轻（创建于 2026-03）——在 Lindy 维度上**未经验证**，但赌注很低：它是一份静态的、机械的 CSS/UX 细节清单，所谓「过时」多半是设计主张变旧，而非会失效。窄而冻结的产物对 Lindy 的敏感度低于运行时依赖。
- **风险旗标：** 仅建议性（agent 可跳过的 markdown；要硬保证请配真正的 CSS/UI linter）；license 是 README 声称的 MIT，仓库无 `LICENSE` 文件、GitHub license API 返回 404——依赖前请确认 license。

## 存疑（未验证）

- [未验证] README 称 license 为 MIT，但仓库根目录没有 `LICENSE` 文件、GitHub license API 返回 404——这里的 SPDX id 来自 README 声明，而非检测到的 license 文件；依赖前请确认。
- [未验证] GitHub 未报告主语言（内容是 markdown skill）;`language: Markdown` 是编辑选择，不是 GitHub 检测到的字段。
- [未验证] star 数（2026-06-26 在 GitHub 上约 1.9k）不可靠且随时间变化；仅作参考，不作质量信号。
- [未验证] skill 结构（一个 `SKILL.md` 加 `typography.md` / `surfaces.md` / `animations.md` / `performance.md`）以及「约 16 条原则」「14 项 checklist」的计数，来自 2026-06-26 对仓库 tree 的检查和对 `SKILL.md` 的一次抓取阅读；请以当前文件为准，而非依赖这些计数。
- [未验证] 安装命令 `npx skills add jakubkrehel/make-interfaces-feel-better` 引自 README；各 harness（Claude Code vs 其他）的实际激活保真度此处未独立确认。
- [推断] 由于行为活在 agent 加载的 markdown 里，「规则」和「checklist」是建议性的 prompt 指令，而非强制门禁——agent 可以偏离。
