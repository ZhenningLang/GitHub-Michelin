---
name: chinese-novelist-skill
slug: chinese-novelist-skill
repo: https://github.com/PenglongHuang/chinese-novelist-skill
category: fiction
tags: [agent-skill, novel-writing, chinese, long-form-writing, skill-pack]
language: Markdown
license: MIT
maturity: v2.0 flow, active, 3.1k stars (as of 2026-09)
last_verified: 2026-09-19
type: skill-pack
upstream:
  pushed_at: 2026-09-06T05:26:15Z
  default_branch: master
  default_branch_sha: cb6c3e7d0563c6a685e6539ea642642ab98855d7
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:42:10Z
  overall: B
  overall_score: 2.75
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
        last_commit_age_days: 16
        active_weeks_13: 3
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
        repo_age_days: 240
        last_commit_age_days: 16
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.92
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

# chinese-novelist-skill

一个纯提示词与参考文档的技能包：让 coding agent 按「问答 → 大纲 → 逐章创作」生成 10–50 章中文小说，并带跨会话偏好记忆、中断续写和字数校验循环。

![chinese-novelist-skill — 健康度雷达](../../../../assets/health/chinese-novelist-skill.zh.svg)

## 何时使用

你是写中文网文的作者，已经在支持 `SKILL.md` 的 coding agent（Claude Code、Codex、OpenCode 等）里工作。你不想要又一个「帮我写本小说」、写到第五章就忘了前情的提示词，而想要一条可重复的流水线：三层问答先钉住题材、主角和核心冲突，再生成大纲、人物档案和机器可读的写作计划，然后进入逐章循环（写 → 润色 → 字数检查），最后跑一遍完稿校验。用 `npx skills add PenglongHuang/chinese-novelist-skill` 安装后调用 `chinese-novelist` 技能即可。

当你想要的是**一个零运行时、MIT 许可、可跨 harness 搬运的轻提示词包**时，选它而不是 [Webnovel Writer](webnovel-writer.zh.md)：没有 Python CLI、没有 SQLite／RAG 状态、不绑定 Claude Code plugin 契约。代价是放弃 Webnovel Writer 那套可查询的连续性系统，换成一摞任何 skill-capable agent 都能跟着走的 Markdown 流程与指南。它靠设定词典、大纲里的分章摘要和 `03-文风基准.md` 文风锚点维持连贯，属于提示词纪律而非索引检索。决定取舍的是**安装简单与模型／harness 可移植性，对上长篇最终需要的那套更重状态机**。

## 何时不用

- **你需要能撑过几十章、且可查询可审计的连续性。** 改用 [Webnovel Writer](webnovel-writer.zh.md)，因为它维护显式的故事契约加上可检索索引，而本技能包依赖 agent 每章重读大纲摘要——它自己的 issue 列表里就有段落重复（`#31`、`#25`）、陷入循环（`#32`）和续写失效（`#22`）的报告。
- **你的任务是非虚构写作或带事实核查闸门的文章生产。** 改用 [writing-agent](../content-production/writing-agent.zh.md)；本技能包是小说生成器，没有证据账本、引用步骤或事实闸门。
- **你要的是一套多任务技能合集，而不是单一用途的小说生成器。** 改用 [Baoyu Skills](../content-production/baoyu-skills.zh.md) 或 [huashu-skills](../content-production/huashu-skills.zh.md)；它们除了写作还覆盖翻译、排版、配图和发布，而本技能包只产出一个小说项目文件夹。
- **去 AI 味是你对任意文本单独跑的、可复用的一步。** 改用专门去 AI 味的技能，例如 [Humanizer-zh](../de-ai-writing/humanizer-zh.zh.md)；本技能包里的「去 AI 味」只是嵌在逐章流程里的一段要点清单，没有独立的重写入口。
- **你不在 skill-capable 的 coding agent 里工作，或你要写的不是中文。** 改用独立桌面编辑器（如 novelWriter，未收录）或普通对话模型；本技能包自身没有运行时，提示词、模板和示例都以中文为先。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Webnovel Writer](webnovel-writer.zh.md) | ✅ | 想要零运行时、MIT、可跨 harness 搬运的提示词包，选 chinese-novelist-skill；长篇连载需要可查询的连续性状态和审稿闸门，选 Webnovel Writer。 | 轻包哪里都能装、可读可改，但放弃检索、章节提交和审计轨迹——它的连贯性只取决于 agent 每次重读大纲的质量。 |
| [writing-agent](../content-production/writing-agent.zh.md) | ✅ | 要带钩子、人物一致的分章小说选 chinese-novelist-skill；要一篇带证据账本、经事实核查的中文文章，选 writing-agent。 | 虚构对非虚构：本包优化悬念、对话占比和 3000–5000 字章节；writing-agent 优化有出处的断言和去 AI 味编辑闸门。 |
| [Baoyu Skills](../content-production/baoyu-skills.zh.md) | ✅ | 整个任务就是一本分章小说，选 chinese-novelist-skill；需要通用中文内容与排版工具箱、自己拼装小说流程，选 Baoyu Skills。 | 窄而专断对宽而可组合：本包给现成分章流水线，Baoyu 给许多小技能但没有小说专用状态。 |
| [huashu-skills](../content-production/huashu-skills.zh.md) | ✅ | 要聚焦、许可宽松的小说生成器，选 chinese-novelist-skill；只有能接受其许可含糊、且想要一站式创作者工具箱时，才选 huashu-skills。 | 许可清晰度与范围：这里 MIT 且只做一件事，那边是 NOASSERTION 且更宽也更重。 |
| novelWriter | 未收录 | 想要不涉及 LLM 的独立跨平台桌面应用来写作和组织小说，选 novelWriter；要让 agent 生成初稿，选 chinese-novelist-skill。 | 本地编辑器可控、无模型成本，对上自动写作依赖你的 agent、模型预算和上下文窗口。 |

## 健康度与可持续性

- **维护（2026-09-19）：** 活跃、未归档；默认分支最后推送于 2026-09-06。历史很短——创建于 2026-01-25，约八个月——38 个 commit。**GitHub release 数为零**；README 里的「v2.0」指的是一个已合并的 PR，唯一的 git tag 是 `v1.0`。
- **治理／巴士系数：** 实际上只有一个人。贡献者 API 显示 `PenglongHuang`（36 个 commit）加 `Aziteee`（2 个）；项目靠爱发电捐助，路线图背后没有基金会或厂商。[推断]
- **年龄／Lindy：** 不到一年拿下 3.1k star、451 fork 是关注度，不是存活证明。按本索引的 Lindy 先验，在它跨若干年持续发布之前，应把这种快速涨星当作炒作风险。
- **采用信号：** 451 个 fork 说明有人在复制和改造，但 fork 是意图而非生产使用；没有验证到依赖方或下游生态。
- **风险标记：** MIT `LICENSE` 直到 2026-09-06 才补上，项目大半生命周期没有明确许可证。开放的 issue 描述了内容重复（`#31`、`#25`）、文风失控（`#30`）、陷入循环（`#32`）和续写失效（`#22`）——这些质量报告削弱了 README「自动校验」的说法。

## 存疑（未验证）

- [推断] 上述 issue 早于或横跨 v2 重写；本文把它们当作方向性的质量证据，而不是当前流程的实测失败率。
- [未验证] 每章的「连贯性检查」是否有效，本次未复现；源码检查显示 Phase 4 的自动校验与重写循环只以字数为闸门，连贯性只是 Phase 3 里的一条人工指令。
- [未验证] 「适配主流 coding agent」的说法取自 README；本次只验证了 `npx skills add` 安装路径，没有验证它在每个点名 harness 里的行为。
- [未验证] 实际文字质量、重复率和 3000–5000 字章节是否贴合大纲，本次未测试；也没有找到独立基准。
- [未验证] 项目没有包管理器足迹（它是 Markdown 技能而非发布的库），因此采用度只能从 star 和 fork 推断。
