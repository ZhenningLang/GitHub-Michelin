---
name: gstack
slug: gstack
repo: https://github.com/garrytan/gstack
category: engineering-workflows
tags: [claude-code, slash-commands, subagent-personas, sdlc-workflow, harness-config]
language: TypeScript
license: MIT
maturity: no tagged release, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-25T16:42:45Z
  default_branch: main
  default_branch_sha: 11de390be1be6849eb9a15f91ff4922dd16c589a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T10:45:43Z
  overall: B
  overall_score: 3.0
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 8
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 114
        last_commit_age_days: 8
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 76
        top1_share: 0.769
        top3_share: 0.797
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

# gstack

Garry Tan 的私人 Claude Code 配置：约 23 个带强烈个人主张的 slash-command 技能，扮演一支虚拟工程团队（CEO 复盘、设计师、工程经理、发布经理、文档工程师、QA、安全官），驱动「规划 → 构建 → 评审 → 发布 → 复盘」的闭环。

![gstack — 健康度雷达](../../../../assets/health/gstack.zh.svg)

## 何时使用

你是一名长期泡在 Claude Code 里的独立开发者或小团队成员，平时把「团队」该做的活儿全在脑子里走一遍：判断一个功能值不值得做、写代码前先锁架构、过一遍设计、自己给自己做 QA，再写发布说明、上线。你希望把这整条流水线变成有名字、可重复的步骤，而不是每个 session 重打一遍临时 prompt。你把 gstack 克隆进 `~/.claude/skills/`、跑它的 `./setup`，于是就有了 `/office-hours`（产品拷问）、`/plan-eng-review`（锁架构）、`/review`、`/qa`、`/cso`（安全审计）、`/ship`、`/document-release`、`/retro` 这些 slash 命令——每一个都是从某个角色视角审视当前工作的 persona。

当你宁愿整套搬来一个人久经实战的端到端 harness，也不想自己一条条命令攒技能栈时，就用它。它明确就是「Garry Tan 本人的做法」——他每天在用的、带主张的软件工厂工作流——所以价值在于这 23 条命令里沉淀的*品味与编排顺序*，而不是一个通用工具箱。装一次后，命令通过 Claude Code 原生的技能加载机制激活；`setup` 还能把同一批命令分发到它检测到的其它 agent（Codex CLI、OpenCode、Cursor、Droid 等）[未验证]。

## 何时不用

- **你已经有一套自己信任的命令/技能体系。** gstack 主张强、人格化（一个会质疑你路线图的 CEO、一个会锁架构的工程经理）。把它叠在已有工作流之上会产生互相打架的 slash 命令和双重路由——只能留一个事实源。
- **你想要可 import 的运行时/库/CLI。** 它的交付物是一袋 prompt 定义的技能，不是 API 或服务。脱离支持它的 agent harness，这些 markdown 什么都不做。
- **你不在被支持的 harness 上。** 它靠 Claude Code 的技能加载器激活（并声称能自动检测约 10 个其它 agent）。在自制或不被支持的 agent 上，没有加载器来触发这些命令。
- **你不想要这套安装足迹。** setup 会克隆进 `~/.claude/skills/`、按技能建符号链接目录、可能写 `.gstack/` 状态，还会自启一个「browse 守护进程」；team 模式会把 `.claude/` 与 `CLAUDE.md` 提交进你的仓库。这比丢几个 `.md` 文件重得多。
- **单一维护者、一个人的品味。** 这是某位创始人的私人配置，没有打 tag 的发布；命令及其行为可能随任意一次 push 变动，且工作流编码的是他的偏好，不是社区标准。
- **是建议而非强制。** 这里的「评审」「锁定」都是 prompt 级指令，agent 仍可忽略；没有任何一项是 CI 里的硬闸门。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Superpowers](../../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) | ✅ | 需要跨 harness 的 SDLC 技能库，而不是单个创始人的角色循环时，选 Superpowers。 | 可组合的 SDLC 技能库（brainstorm → plan → TDD → verify），以跨 harness 插件形式分发。更偏 TDD/测试先行的纪律，且走 marketplace 安装；gstack 是某位创始人*基于角色*的命令集（CEO/设计师/QA 等 persona），为他每天的工厂量身调过，而非通用方法论。 |
| [antfu/skills](antfu-skills.zh.md) | ✅ | 需要另一份个人 Claude Code 技能集，且其工作流假设更贴近你时，选 antfu/skills。 | 另一份私人 Claude Code 技能集；按各自作者编排了什么工作流、对你环境假设多少来比较。 |
| [Dimillian/Skills](dimillian-skills.zh.md) | ✅ | 作者品味和命令路由方式更合适时，选 Dimillian/Skills。 | 私人技能集；按作者品味与命令的路由方式来选。 |
| [wshobson/agents](../../subagent-collections/wshobson-agents.zh.md) | ✅ | 需要更宽的 subagent/persona 目录时，选 wshobson/agents。 | 体量较大的 subagent/persona 集合；目录更广，对比 gstack 更聚焦的创始人主张工厂闭环。 |
| 自己从零写命令 | 未收录 | 最高贴合度比维护成本更重要时，选自己从零写命令。 | 贴合度最高、零 lock-in，但每个 persona 和编排顺序都得你自己写、自己维护。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 活跃——最后 push 于 2026-06，但有约 743 个 open issue 且**没有打 tag 的 release**，因此没有可 pin 的版本，你跟的是移动的 `main`。活跃度高，但对一份个人配置而言 open issue 积压偏大。
- **治理与 bus factor：** 这是最突出的风险信号——一个 `User` 所有的个人仓库（Garry Tan），却背着约 117k star 和约 743 个 open issue，单一维护者，背后无基金会/团队。这是极端的 bus-factor 集中：巨大的采用量全压在一个人的品味与可用性上。工作流编码的是他的偏好，而非社区标准。
- **年龄与 Lindy 判断：** 创建于 2026-03，截至 2026-06 仅约 3 个月——非常年轻且热度极高（star 数远超项目历史）。热度不等于 Lindy：没有存续记录，破坏性变更可能在任意一次 push 落地。未经验证。
- **采用度提示：** 约 117k star 更多反映病毒式关注，而非久经实战的稳定性；在无 release、issue 积压沉重的情况下，应把采用量当作人气信号，而非成熟度信号。
- **风险标记：** 安装足迹重（克隆进 `~/.claude/skills/`、建符号链接、写 `.gstack/` 状态、自启 browse 守护进程；team 模式会提交 `.claude/`+`CLAUDE.md`）。仅为建议性——「评审」「锁定」都是 prompt 级，而非 CI 闸门。

## 存疑（未验证）

- [未验证] 截至 2026-06-26，GitHub 元数据显示 license 为 MIT、主语言 TypeScript；仓库最近一次 push 在 2026-06-25；未报告任何 GitHub release/tag（`latestRelease: null`），因此没有可固定的稳定版本——依赖具体命令行为前请重新核验。
- [未验证] Star 数（2026-06-26 GitHub 约 11.6 万）不可靠且对日期敏感，仅作参考，不代表质量。
- [未验证] 「23 个工具」/命令列表（如 `/office-hours`、`/plan-eng-review`、`/review`、`/qa`、`/cso`、`/ship`、`/document-release`、`/retro`）取自项目 README；确切集合与命名会随仓库变化，应以当前 `skills/` 目录为准，而非本页。
- [未验证] 声称通过 `./setup --host` 自动检测支持约 10 个 AI 编码 agent（Codex CLI、OpenCode、Cursor、Factory Droid、Slate、Kiro、Hermes、GBrain 等），来自 README；各 agent 的实际激活保真度未在此独立确认。
- [未验证] 安装/运行要求（Git、Bun v1.0+、Windows 下可选 Node、自启的「browse 守护进程」、记忆功能可选用 Supabase/PGLite）取自 README，未通过实际运行 setup 验证。
- [推断] 由于行为存在于 agent 加载的 prompt/markdown 技能中，每个「评审」「锁定」「闸门」都是建议性的——agent 可以偏离；请当作指引，而非强制控制。
- [推断] 作为某人无发布版本的私人配置，破坏性变更可能在任意一次 push 落地；若需稳定，请固化你测试过的版本。
