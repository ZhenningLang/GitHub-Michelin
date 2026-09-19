---
name: USDAD
slug: usdad
repo: https://github.com/halloffamer11/USDAD
category: spec-driven-development
tags: [spec-driven, multi-agent, context-engineering, human-in-the-loop, methodology, cursor]
language: Markdown
license: MIT
maturity: methodology artifact, 1 commit, 0 stars (as of 2026-07)
last_verified: 2026-07-17
type: skill-pack
upstream:
  pushed_at: 2026-04-27T12:42:50Z
  default_branch: main
  default_branch_sha: 34a20b7f0468b921a80d362ab9bd4f4338e3f881
  archived: false
health:
  schema: 1
  computed_at: 2026-07-16T18:07:26Z
  overall: C
  overall_score: 2.0
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 80
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 80
        last_commit_age_days: 80
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
    adoption: { reason: no_package_structural }
---

# USDAD

一套文档优先、规格驱动的方法论，用共享 steering 与项目上下文文件协调 planner、adversary、architect、executor；它是供你裁剪的方法论原稿，不是可安装的运行时。

![USDAD — 健康度雷达](../../../assets/health/usdad.zh.svg)

## 何时使用

你正在带一个会跨多个会话、模型或 coding tool 的 agent 辅助项目，反复遇到的是上下文漂移：一个 agent 改写了需求，另一个忘了架构约束，团队还没压测方案就开始实现。你希望规格一直是共享事实源，并明确分出起草、对抗式审查、综合定稿和按任务执行四种职责，每一步都保留人工批准点。

当你想直接读懂并改造方法论原稿，而不是采用厂商 CLI 或大型预制插件时，USDAD 才有优势。它最有辨识度的选择是三层上下文：可复用的全局 steering、项目级的 requirements/design/tasks/context，以及承担头脑风暴和验收的人工界面。

## 何时不用

- **你需要能创建并校验项目规格的 CLI。** 改用 [Spec Kit](spec-kit.zh.md)；USDAD 提供 Markdown 约定与提示词，但没有可执行生成器、schema 校验器或版本化命令行。
- **你想给多种 coding-agent harness 直接装上 brainstorm 到 TDD 的工作流。** 改用 [Superpowers](../coding-agent-harnesses/superpowers.zh.md)；它已打包可运行 skills 和平台清单，而 USDAD 需要手工复制与改造。
- **你需要机器校验的 intent、交接 schema、freshness gate 和带测试的维护脚本。** 改用 [PURE](pure-agentic.zh.md)；PURE 把类似的文件纪律做成 schema 与 Shell 工具，USDAD 仍以文字约定为主。
- **你只是在修一个小问题或做一次性原型。** 改用简短的 `AGENTS.md` 加项目已有测试与 CI；USDAD 的 planner/adversary/architect 流程和持久 context ledger 可能得不偿失。
- **你想模拟包含 PM、架构、开发、QA 的完整软件组织。** 改评 BMAD-METHOD；USDAD 刻意采用更小的四 persona 规划与执行模型。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Spec Kit](spec-kit.zh.md) | 已收录 | 如果维护中的 CLI 和自动生成规格流程比直接掌控方法论文档更重要，选 Spec Kit；如果要亲自改上下文模型和角色提示词，选 USDAD。 | Spec Kit 多了可执行工具和厂商支持；USDAD 更小、更透明，但自动化与约束都要自己补。 |
| [Superpowers](../coding-agent-harnesses/superpowers.zh.md) | 已收录 | 如果要即插即用地驱动 brainstorm、计划、TDD 和验证，选 Superpowers；如果决定性需求是持久项目上下文与对抗式规格审查，选 USDAD。 | Superpowers 更容易装到多种 harness；USDAD 的 requirements/design/tasks/context 结构更显式，却没有 loader。 |
| [PURE](pure-agentic.zh.md) | 已收录 | 如果 intent schema、registry、phase gate 和测试脚本必须成为可执行控制，选 PURE；如果紧凑的文字型 spec 方法已够用，选 USDAD。 | PURE 的机器治理和运维面更完整；USDAD 更容易读，但落地依赖人工纪律。 |
| [Get Shit Done](get-shit-done.zh.md) | 已收录 | 如果核心需求是 fresh-context 分阶段执行和已安装命令，选 GSD；但本索引对应的 canonical 仓库已冻结，而 USDAD 从一开始就是静态方法论工件。 | GSD 自动化了更多交付循环，但已收录上游归档；USDAD 不绑运行时，也不提供编排。 |
| BMAD-METHOD | 未收录 | 如果要覆盖更广的软件组织角色，选 BMAD-METHOD；如果四个明确 persona 和较小上下文层级更容易掌控，选 USDAD。 | BMAD 的生命周期角色更广，代价是流程与提示词面积更大；USDAD 更窄，也更少自动化。 |

## 健康度与可持续性

- **维护，截至 2026-07：** 公开仓库只有一个 2026-04-27 的提交，没有 tag release、issue 活动，且未归档。应把它视为已发布的方法论快照，而不是持续发布的软件线。
- **治理与 bus factor：** 仓库由一个 GitHub 用户拥有并独立贡献，没有公开治理或继任机制。后续更新依赖单一作者。
- **年龄与 Lindy：** 公开仓库不足三个月。README 称方法形成于 2025 年的实际项目，但公开工件本身没有长期维护记录，耐久性尚未得到证明。
- **采用信号：** README 点名两个相关应用仓库，但方法论仓库为 0 star，也没有外部贡献轨迹。这不能说明内容质量差，却没有提供独立采用证据。
- **风险姿态：** MIT 许可宽松，也没有运行时供应链。主要风险是流程效果：提示词和文档能引导 agent，却不会机械执行这些规则。

## 存疑（未验证）

- [未验证] README 称 USDAD 用于构建 `ffb_calcs` 与 `ffb`；本次未审计这两个仓库是否忠实采用方法，也未核验交付结果。
- [未验证] 本次没有找到独立 benchmark 或受控比较来验证它对质量、连续性和多模型协作的收益。
- [推断] 项目交付的是指令与模板，而非可执行 gate；agent 是否遵循取决于模型和 harness，行为不受保证。
- [推断] 该仓库也可能是作者有意发布的完整历史工件，而非已放弃项目；仅凭单提交历史无法区分两种状态。
