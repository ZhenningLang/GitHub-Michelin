---
name: shaping-skills
slug: shaping-skills
repo: https://github.com/rjs/shaping-skills
category: engineering-workflows
tags: [skills, shape-up, product-shaping, breadboarding, claude-code]
language: Shell
license: NOASSERTION
maturity: no tagged releases, last pushed 2026-04 (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-04-10T10:12:59Z
  default_branch: main
  default_branch_sha: d8b65d7733c71e9bf436f0c2e4da60e5214a96d9
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:49:03Z
  overall: E
  overall_score: 0.25
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 1
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 236
        last_commit_age_days: 1
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
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# shaping-skills

Ryan Singer 的个人 Claude Code 技能包，把 Shape Up 的「shaping（塑形）」流程——框定问题、breadboarding 梳理交互、产出 framing/kickoff 文档——带进 coding agent，让 AI 在写任何代码之前先帮你想清楚「要做什么」。

![shaping-skills — 健康度雷达](../../../../assets/health/shaping-skills.zh.svg)

## 何时使用

你是一个产品同学或独立开发者，正用 Claude Code 推敲一个还很模糊的想法，却总撞同一堵墙：对话里有不少好思考，但始终落不成一份 builder 能直接动手的东西。你从一个含糊的问题直接跳到「那就开干吧」，跳过了把「问题」和「方案」分开的那一步，最后做出来的东西解决的是错的问题。你希望 AI 像一个 shaping 搭子——逼你先把问题框清楚，把粗略方案画成相互连接的 affordance（而不是像素级的精美界面），然后才产出一份团队能直接执行的紧凑文档。

这个包以一组按需技能给你这种能力：`/framing-doc` 和 `/kickoff-doc` 把一段有效对话蒸馏成「问题框定」或「builder 参考」文档；`/shaping` 在进入实现前把问题和方案一起迭代；`/breadboarding` 按 Shape Up 的方式把系统拆成 places、affordances 以及它们之间的连线。`hooks/shaping-ripple.sh` 脚本做一次涟漪/副作用检查。安装方式是 clone 仓库后把各技能目录软链到 `~/.claude/skills/`——之后任务匹配时，方法论通过 Claude Code 原生技能加载器激活。

## 何时不用

- **你已经有一套信任的规划/spec 方法论。** Shaping 与「先头脑风暴再写计划」类技能包（如 Superpowers 的 `brainstorming` + `writing-plans`）直接重叠。叠两套有主张的「先定义再开干」流程会导致路由冲突——shaping/planning 只能有一个事实源。
- **你要的是代码，不是问题定义。** 这个包刻意停在实现*之前*；它产出 framing/kickoff 文档，不产出可运行代码或测试。如果你要的是 build loop（TDD、调试、重构），它不覆盖。
- **「garbage in, garbage out」对你是硬伤。** 文档类技能只对你给的素材做格式化和蒸馏；README 明确说它们不判断你的思考好不好——糟糕的对话只会得到一份排版精美的糟糕文档。
- **你不在 Claude Code 上。** 激活依赖 Claude Code 的 `~/.claude/skills/` 软链 + 原生技能加载器；换个 harness 没有加载器来调起这些技能，光有 markdown 不会自动触发。[推断]
- **你需要稳定性或维护保证。** 个人仓库，无 tagged release，最后 push 在 2026-04，无 license 文件；作者明确标注 solo 技能（`/shaping`、`/breadboarding`）更实验、更未经实战。把它当作一个人的工作配置，而非维护中的产品。
- **强制力只是建议级。** 行为活在 agent 按需加载的 prompt/markdown 技能里；shaping 纪律是 agent 仍可跳过的建议，不是硬闸门。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [antfu/skills](antfu-skills.zh.md) | ✅ | 需要 Vue/Vite 前端实现栈规则，而不是上游问题塑形时，选 antfu/skills。 | 同为个人精选 Claude Code 技能集，但面向 Vue/Vite 前端*实现*栈（测试写法、ESLint、UnoCSS）。两者正交：shaping-skills 在代码上游（问题/方案定义），antfu/skills 在下游（代码怎么写）。 |
| [Dimillian/Skills](dimillian-skills.zh.md) | ✅ | 任务偏实现或平台约定，而非产品塑形时，选 Dimillian/Skills。 | 另一位个人开发者的 Claude Code 技能集；按领域对比——Dimillian 偏实现/平台约定，shaping-skills 偏产品塑形与文档产出。 |
| [gstack](gstack.zh.md) | ✅ | 需要个人 harness/persona 配置，而不是 Shape Up 塑形词汇时，选 gstack。 | 本叶子下的个人 harness/技能集，侧重点不同。交叉确认各自塑形 vs 构建的生命周期阶段。 |
| [Superpowers](../../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) | ✅ | 需要完整 SDLC 技能库的 brainstorm 和计划环节时，选 Superpowers。 | 一个完整 SDLC 技能库，其前端（拷问想法、写计划）与 shaping 意图重叠，但框成通用软件头脑风暴，而非 Shape Up 的「问题/方案/breadboard」词汇体系。 |
| Shape Up 原书 / BaseCamp 官方材料 | 未收录 | 需要源方法论文本、不是可安装 agent skill 时，选原书或官方材料。 | 作为文字的源方法论，不是可安装的 agent 技能——这个包是某个人把它在 Claude Code 里落地的实现。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— 最后推送 2026-04，未归档（截至 2026-06）：安静了一两个月，没有打 tag 的 release。看上去是「一个人最近还在动的工作配置」，而非「吃老本」或废弃——但节奏偏低，且作者明确标注 solo 技能为实验性。
- **治理与 bus factor** —— 单维护者的个人仓库（`User` 所有，Ryan Singer），约 1.4k stars。是一个人把 Shape Up 落地的实现；没有团队或组织兜底。当作 fork 自管，而非维护中的产品。
- **年龄与 Lindy** —— 创建于 2026-01，截至 2026-06 约 0 年：年轻，Lindy 上未经验证。Shape Up *方法论*本身很成熟，但这套技能封装是新的、经实战不多——为方法而采用，但要清楚外壳是新的。
- **风险旗标** —— 截至 2026-06 未检测到 license（`NOASSERTION`）：复用/再分发权利不清，请与作者确认。技能清单与 SKILL.md 大小写可能变动；强制仅为建议级。

## 存疑（未验证）

- [未验证] 截至 2026-06-26，GitHub 元数据未暴露 license 文件或 `licenseInfo`（此处记为 SPDX `NOASSERTION`）；缺显式 license 时，复用/再分发权利不明——依赖前先向作者确认。
- [未验证] 仓库无 tagged release，按 GitHub 元数据（2026-06-26）最后 push 在 2026-04-10；主语言报告为 Shell。依赖当前行为前请重新核验时效。
- [未验证] Star 数（2026-06-26 GitHub 约 1.4k）不可靠且对日期敏感；仅作参考，不作质量信号。
- [未验证] 技能清单（`framing-doc`、`kickoff-doc`、`shaping`、`breadboarding`，外加一个 `breadboard-reflection` 目录和 `hooks/shaping-ripple.sh`）读自仓库树；SKILL.md 文件名大小写不一且集合可能变动——以实时仓库树为准，勿信本清单。
- [未验证] 作者识别为 Ryan Singer（rjs）、以及 solo 技能「更实验、更未经实战」的说法均取自 README，此处未独立核实。
- [推断] 因技能是 Claude Code 加载的 prompt/markdown，shaping 纪律是建议级——agent 可偏离；这里的「技能」塑造行为，并不强制行为。
