---
name: soul.md
slug: soul-md
repo: https://github.com/aeonfun/soul.md
category: context-engineering
tags: [agent-skill, context-engineering, soul-md, skill-pack]
language: JavaScript
license: MIT
maturity: active, ~616 stars (as of 2026-07)
last_verified: 2026-07-16
type: skill-pack
upstream:
  pushed_at: 2026-07-16T05:44:05Z
  default_branch: main
  default_branch_sha: af63feec7dacb0fd91cf9eaffeb608b275ad0e0a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:43:59Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 15
        active_weeks_13: 8
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
        repo_age_days: 232
        last_commit_age_days: 15
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 6
        top1_share: 0.898
        top3_share: 0.949
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
# soul.md

The best way to build a personality for your agent. Let Claude Code / OpenClaw ingest your data & build your AI soul.

![soul-md — 健康度雷达](../../../assets/health/soul-md.zh.svg)

## 何时使用

你已经有一个 digital identity 的素材，想用结构化 Agent Skill 文件夹告诉模型如何 embody 它：`SOUL.md` 写 worldview，`STYLE.md` 写 voice，`MEMORY.md` 保连续性，`data/` 放原始资料，`examples/` 放好 / 坏输出校准。目标是持久 persona package，而不是一次性 prompt 时，选 soul.md。

当前上游 tree 没有根目录 README；操作 contract 来自 `SKILL.md`、`MEMORY.md`、templates 和 examples。它更适合能读取本地文件、维护 identity / context 文件夹的 agent runtime。

## 何时不用

- **你需要有来源引用的答案。** 对上传文档做 retrieval 时，[NotebookLM Claude Code Skill](notebooklm-skill.zh.md) 更合适。
- **你要从零研究并创建 persona。** [nuwa-skill](nuwa-skill.zh.md) 提供研究 / 蒸馏 pipeline；soul.md 假设你能填好 identity 文件。
- **你在模拟未经同意的私人个体。** 这个文件结构让克隆变容易；这是隐私和授权风险，不只是技术任务。
- **你不想要 role embodiment。** soul.md 明确要求 agent 保持角色并避免“as an AI”框架；需要中性助手行为时不要用它。
- **你不能管理持久文件。** memory 和 calibration 模型依赖本地文件长期读取和维护。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [nuwa-skill](nuwa-skill.zh.md) | ✅ | 需要研究并蒸馏公开人物或主题成 skill 时选 nuwa。 | nuwa 是 creation pipeline；soul.md 是 identity 文件层级和运行 contract。 |
| [tacit-mining](tacit-mining.zh.md) | ✅ | 目标是通过对话发现当前用户自己的隐性判断规则时选 tacit-mining。 | tacit-mining 提取规则；soul.md 包装更完整的人格和 memory。 |
| 自写 voice guide | 未收录 | 只需要窄品牌 / 作者 voice，不需要完整 identity embodiment 时自写。 | 更小、更安全；持久性和校准能力弱于 soul.md。 |
| 一次性角色扮演 prompt | 未收录 | 仅用于 disposable 实验。 | 成本低，但没有文件层级、source priority、memory 和 anti-pattern calibration。 |


## 健康度与可持续性

- **维护快照（2026-07-16）：** GitHub 返回 `archived=false`，`pushed_at=2026-07-16T05:44:05Z`；health 将维护评为 A。
- **采用快照：** 2026-07 约 616 个 GitHub stars；对年轻 identity-template 仓库来说规模小但相关。
- **许可证快照：** 已核验根目录 `LICENSE` 为 MIT；GitHub contents 也显示 `SKILL.md`、`MEMORY.md`、`SOUL.template.md`、`STYLE.template.md`、`data/` 和 `examples/`。
- **Lindy / 治理：** health 中 longevity 为 C；由于提交活动集中，governance 为 D。
- **风险信号：** persona embodiment 可能造成过度自信模仿、隐私问题，或在用户不维护 identity folder 时产生 stale memory。

## 存疑（未验证）

- [未验证] 已核验的 `main` tree 没有根目录 README；本页依据 `SKILL.md`、templates、根目录内容和 LICENSE 写成。
- [未验证] 没有用真实 agent 运行 identity folder 来评估示例质量。
- [推断] 最适合包装你拥有或获授权建模的 identity，不适合开放式研究或 retrieval。
