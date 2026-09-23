---
name: dbskill
slug: dbskill
repo: https://github.com/dontbesilent2025/dbskill
category: knowledge-content
tags: [agent-skills, business-diagnosis, claude-code, chinese, content-creation]
language: JavaScript
license: CC-BY-NC-4.0
maturity: v2.14.2, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-29T03:58:40Z
  default_branch: main
  default_branch_sha: 096f726a20407901ca517cfc42509f96232fd0ea
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:49:23Z
  overall: C
  overall_score: 2.0
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 16
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 5226
        release_assets: 63
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 186
        last_commit_age_days: 16
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 3
        top1_share: 0.948
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: type_na }
    risk_license: { reason: license_unparsed }
---

# dbskill

一套个人精选的中文 agent 技能包（约 21 个 `/dbs-*` 命令），聚焦商业模式诊断、内容创作与个人决策，可通过插件市场或 `skills` CLI 安装进 Claude Code 等 harness。

![dbskill — 健康度雷达](../../../../assets/health/dbskill.zh.svg)

## 何时使用

你是一名独立创业者、个人创作者或一人公司操盘手，主要面向中文市场，平时把 Claude Code（或 Codex / Cursor / Trae Solo）当作思考搭子。你反复问 agent 这类问题——“我这个商业模式到底跑不跑得通”“为什么这条内容没量”“下一个 90 天目标该定什么”——但每次拿到的都是泛泛而谈、一股 AI 味的建议，因为 agent 手上没有可以锚定的、有观点的框架。dbskill 给你装进一套连贯的商业诊断技能：`/dbs-diagnosis`（商业模式拆解）、`/dbs-benchmark`（对标分析）、`/dbs-content` 与 `/dbs-content-system`（内容诊断 + 结构化内容工程系统）、`/dbs-hook` 与 `/dbs-xhs-title`（短视频开头、小红书标题公式）、`/dbs-action`（执行力诊断）、`/dbs-decision`（个人决策系统），还有状态管理命令（`/dbs-save`、`/dbs-restore`、`/dbs-report`），让一次诊断会话可以持久化、可恢复。

当你想要的是**这位作者本人的**方法论——命令背后的框架、案例库和约 4000+ 条知识原子——而不是自己从零搭一套 prompt 时，就用它。安装一次（`claude plugin marketplace add dontbesilent2025/dbskill`，或 `npx -y skills add dontbesilent2025/dbskill -g --all`），技能就会通过你 harness 的原生技能机制按需加载。

## 何时不用

- **你不在中文商业语境里。** 技能、知识原子和案例素材主要是中文，框架还依赖中国特有渠道（小红书标题、短视频钩子）。离开这个语境，大部分价值就蒸发了。
- **你想要通用的 SDLC / 编码纪律，而非商业教练。** 这是一个关于商业、内容、决策的领域包——不是 TDD、重构或 agent 工程。把它和编码方法论包搭配用，别指望两者重叠。
- **你已经有一套自己信任的诊断框架。** dbskill 观点很强（阿德勒式执行模型、“慢即是快”的摩擦资产论、固定标题模板）。叠在已有教练 prompt 栈之上会引入互相打架的建议——只选一个事实源。
- **你在不受支持 / 自制的 harness 上。** 它通过 Claude Code / Codex / Cursor / Trae Solo 的技能加载机制激活；没有 loader，markdown 不会自动触发。
- **商用 / 产品化用途。** 采用 CC BY-NC 4.0 许可——商业使用需作者另行授权，无法自由打包进付费产品。[未验证]
- **你需要稳定性。** 单一作者维护、v2.x、发布频繁；框架措辞和命令路由会随版本变动。依赖具体行为就锁版本。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [antfu/skills](../engineering-workflows/antfu-skills.zh.md) | ✅ | 需要编码或 devtools 个人技能，而非商业诊断时，选 antfu/skills。 | 一位维护者的个人编码/devtools 技能；工程味、英文优先。dbskill 是商业诊断的领域包，不是代码工作流。 |
| [Dimillian/Skills](../engineering-workflows/dimillian-skills.zh.md) | ✅ | 需要 iOS/Swift 软件开发帮助，而非商业教练时，选 Dimillian/Skills。 | 一位 iOS/Swift 开发者的个人技能；软件向。领域不重叠——按你要编码帮助还是商业教练来选。 |
| [awesome-claude-code-subagents](../../subagent-collections/awesome-claude-code-subagents.zh.md) | ✅ | 需要覆盖众多技术角色的大型 subagent 合集时，选 awesome-claude-code-subagents。 | 一个覆盖众多技术角色的大型 subagent 合集；重广度而非单一鲜明声音。dbskill 是单作者、窄而深的商业方法论。 |
| 通用 LLM 商业教练 prompt | 未收录 | 只需要临时商业教练、且不需要精选框架或持久化状态时，选临时 prompt。 | 临时 prompt 没有精选框架、案例库或持久化；dbskill 在连贯的作者声音背后带了约 4000 条知识原子和状态命令。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 活跃——最后 push 于 2026-06，处于 v2.14.2，发版频繁，仅约 10 个 open issue。它确实打 tag 发版，因此版本可 pin。是活跃而非半荒废。
- **治理与 bus factor：** 单作者的 `User` 仓库（dontbesilent2025）；全部价值——框架、案例库、约 4000 条知识原子——都是一位创作者的方法论，背后无基金会或团队。一人 pack 却有约 7k star，是 bus-factor 风险信号；延续性系于该作者。
- **年龄与 Lindy 判断：** 创建于 2026-03，截至 2026-06 仅约 3 个月——非常年轻且热度高，没有存续记录。应视为未经验证；其框架是作者的观点，而非经时间检验的标准。仅凭年龄即未通过 Lindy 检验。
- **风险标记：** 采用 **CC BY-NC 4.0** 许可——仅限非商用，未经另行授权不能打包进付费产品（GitHub 把许可证报告为 `Other`/`NOASSERTION`）。绑定中文市场，且仅为建议性（prompt 级教练，无强制）。

## 存疑（未验证）

- [未验证] 许可证在 README 中声明为 CC BY-NC 4.0（“本项目采用 CC BY-NC 4.0 许可证”）；GitHub API 把许可证报告为 `Other` / `NOASSERTION`，因为 CC 许可不在其 SPDX 识别集内——商用前请核对 LICENSE/README。
- [未验证] 最新发布报告为 v2.14.2（2026-06-05 发布），仓库最后 push 为 2026-06-05，均为 2026-06-26 时的 GitHub 元数据；依赖某个具体版本的技能或行为前请重新核验。
- [未验证] Star 数（2026-06-26 GitHub 显示约 6,969）不可靠且对日期敏感；仅作参考，不作质量信号。
- [未验证] 技能清单（约 21 个 `/dbs-*` 命令）、“4,176 条知识原子” 与 “12 份方法论文档” 的数量，以及受支持 harness 列表（Claude Code、Codex、Cursor、Trae Solo、Grok Build）均来自项目 README；此处未独立确认，且会随版本变动。
- [未验证] GitHub 把主语言报告为 JavaScript，但 README 把交付物描述为技能 markdown / JSONL 知识文件加构建/打包脚本，而非可运行应用；应按 skill-pack 而非 CLI 对待。
- [推断] 由于行为存在于 agent 加载的 prompt/markdown 技能里，这些框架是建议性的——agent 仍可能偏离；产出是教练 prompt，而非有保证的商业结果。
