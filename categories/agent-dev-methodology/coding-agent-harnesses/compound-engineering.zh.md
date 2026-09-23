---
name: Compound Engineering
slug: compound-engineering
repo: https://github.com/EveryInc/compound-engineering-plugin
category: coding-agent-harnesses
tags: [skill-pack, slash-commands, spec-driven, knowledge-capture, multi-agent-host, claude-code]
language: TypeScript
license: MIT
maturity: v3.14.3, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-29T07:48:58Z
  default_branch: main
  default_branch_sha: f8e90d11fe6c4f034ccb450f0f3302f3d33dc21a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-23T03:10:49Z
  overall: B
  overall_score: 3.25
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 348
        last_commit_age_days: 0
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 95
        top1_share: 0.658
        top3_share: 0.851
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

# Compound Engineering

一个有明确主张、以插件形式安装的 skill-pack：把一套六步循环——brainstorm → plan → work → simplify → review → compound——接进 Claude Code、Codex、Cursor 等十多种 coding agent，让每个任务都把经验沉淀回去，喂给下一个任务。

![compound-engineering — 健康度雷达](../../../assets/health/compound-engineering.zh.svg)

## 何时使用

你是一个整天泡在 coding agent 里（Claude Code、Codex、Cursor、OpenCode……）的开发者，你发现自己的会话都是一次性的：在对话里头脑风暴一个功能，agent 把它写出来，你扫一眼 diff，然后那些来之不易的上下文——你为什么否掉了方案 A、那个让你折腾一小时的坑——会在会话结束的一瞬间蒸发。下一个功能又从零开始。你想要一套*有名字、可重复*的工作流，把规划和审查前置（项目的赌注：“80% 在规划和审查，20% 在执行”），更关键的是，把每一轮循环的经验沉淀到下一轮会去读的地方。

Compound Engineering 通过你 agent 的插件市场安装（Claude Code 用 `/plugin marketplace add EveryInc/compound-engineering-plugin`），为每个阶段给你一个 slash 命令：`/ce-brainstorm`、`/ce-plan`、`/ce-work`、`/ce-simplify-code`、`/ce-code-review`、`/ce-compound`——外加 `/lfg` 自动跑完整条流水线。`/ce-compound` 这一步把本轮循环的洞见写进 `docs/solutions/`，这样下一次 `/ce-brainstorm` 和 `/ce-plan` 就是从你累积的决策出发，而不是一张白纸。当你想要一套今天就能即插即用、跨多宿主的方法论，而不是自己手搓一套 slash 命令纪律时，就用它。

## 何时不用

- **你已经有一套成熟的自定义工作流。** 如果你已经搭好了自己的 skills/命令和 memory 约定（你自己的 plan→TDD→review→复盘链），再塞进 27 个有强主张的 `/ce-*` 命令，基本只是增加面和一套竞争性约定——README 明说它“opinionated by design”，不会迁就每种工作流。
- **你不想在仓库里多一个 `docs/solutions/` 知识目录。** “compound”的收益依赖把经验作为文件 commit 进去；如果这不符合你的仓库卫生，或者你没法 commit agent 生成的文档，这套循环就失去了复利优势，只剩下普通的 plan/review 提示词。
- **你需要确定性的、可审计的闸门（CI 必过、schema 审查、安全）。** 这是一组*引导* LLM 走完各阶段的提示词资产；review/simplify 步骤是模型判断，不是 linter、类型检查或测试闸门。把你真正的 CI/护栏单独接好——别把 `/ce-code-review` 当合并闸门。
- **你只需要单个能力，而非一整套方法论。** 如果你只是想要一个好用的 plan 命令或一个 code-review 提示词，引入一个完整的六阶段、多宿主插件，比抄一个 skill 重得多。
- **对厂商/理念锁定的容忍度低。** 这些阶段、命名和“80/20 规划”论点是 Every 的编辑主张；你继承的是他们的节奏，以及他们有权拒绝不符合其愿景的贡献。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Superpowers](superpowers.zh.md) | ✅ | 需要面向 Claude Code、能力面广的大型通用 skill 库时，选 Superpowers。 | 面向 Claude Code 的大型通用 skill 库（能力面广）；Compound Engineering 是更紧凑、有明确主张的六步*循环*，且带一个显式的知识沉淀步骤。 |
| [SuperClaude Framework](superclaude.zh.md) | ✅ | 需要主要面向 Claude、配置和 slash 命令更丰富的 persona/命令框架时，选 SuperClaude Framework。 | persona/命令框架，配置和 slash 命令丰富，主要面向 Claude；CE 更精简、呈循环形态，且明确多宿主（Codex/Cursor/Kimi/Droid/……）。 |
| [get-shit-done](../spec-driven-development/get-shit-done.zh.md) | ✅ | 需要另一套偏交付阶段循环的有主张 agent 工作流/skill-pack 时，选 get-shit-done。 | 另一个有主张的 agent 工作流/skill-pack；plan-execute 精神有重叠——对比命令粒度，以及它是否像 CE 的 `/ce-compound` 一样持久化经验。 |
| [ECC](ecc.zh.md) | ✅ | ECC 的上下文工程词汇和持久化模型更贴合团队时，选 ECC。 | 本分类下的同类方法论；对构建循环的框定不同——按哪套工作流词汇和持久化模型适合你来选。 |
| [12-Factor Agents](../spec-driven-development/12-factor-agents.zh.md) | ✅ | 需要构建 agent 的设计*原则*，而不是可安装的逐会话循环时，选 12-Factor Agents。 | 一套构建 agent 的设计*原则*（文档/宣言），不是可安装的逐会话循环；CE 是你在干活时调用的、可运行的插件。 |
| [Spec Kit](../spec-driven-development/spec-kit.zh.md) | ✅ | 需要 spec 驱动开发工具包（spec→plan→tasks）和自带 CLI 时，选 Spec Kit。 | spec 驱动开发工具包（spec→plan→tasks），自带 CLI；规划优先的气质相近，但较少涉及 CE 那种跨众多宿主的逐循环经验沉淀。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 活跃维护——最后 push 在 2026-06，最新 release `v3.14.3`（2026-06-24），未归档。较高的发版节奏（v3.x 线上的 semantic-release）说明这是个活项目，而非 coasting。
- **治理与背书：** Organization 持有（EveryInc / 「Every」），即一家媒体+软件公司的编辑型产品，而非基金会或单干爱好者。路线图是 Every 的强主张（「opinionated by design」，会拒绝不合愿景的贡献）——背后有真实组织的厂商型治理，但你得继承他们的节奏。
- **年龄与 Lindy（2026-06）：** 创建于 2025-10，约 8 个月。非常年轻；已经到 v3 大版本，说明迭代飞快，也意味着安装模型/命令集仍在抖动。Lindy 裁决：**按年龄看属未经验证**——为当下价值采用，预期 API/命令漂移，别假定长期稳定。
- **风险标记：** MIT 许可，未见 open-core 闸门或 relicense 历史。复利收益与把 `docs/solutions/` 知识目录 commit 进仓库绑定——是对其约定的软锁定，可逆但真实。[未验证] 所审材料中未发现 CVE 或弃用通知。

## 存疑（未验证）

- [未验证] gh 元数据（2026-06-26）:license MIT，主语言 TypeScript，最新 release `compound-engineering-v3.14.3` 发布于 2026-06-24，未归档。star 约 22.0k——GitHub star 不可靠且对时间敏感，仅供参考。
- [推断] 归类为 **skill-pack**：据 `package.json`，该仓库 `private: true`、无已发布的 npm CLI 二进制，且 TypeScript（占仓库 87.5%）是纯开发期工具——为各宿主生成插件清单的转换器（依赖：`citty`、`js-yaml`、semantic-release）。真正交付的价值是 `skills/` 里的 markdown skill/提示词资产，因此技术栈/依赖/运维三节有意省略。README 自己也写道“the Bun CLI remains for repository development and converter maintenance, not normal installation”——若出现运行时二进制请重新核实。
- [未验证] “27 个 skill”以及命名命令（`/ce-brainstorm`、`/ce-plan`、`/ce-work`、`/ce-simplify-code`、`/ce-code-review`、`/ce-compound`、`/lfg`）来自截至 2026-06-26 的 README；确切集合和命名随版本变动——依赖某个具体命令前请核对当前 `skills/` 目录。
- [未验证] 支持宿主列表（Claude Code、Cursor、Codex App/CLI、Kimi Code、GitHub Copilot、Factory Droid、Qwen Code、OpenCode、Pi、Antigravity CLI）和安装语法来自 README；各宿主转换清单的保真度未经独立验证。
- [推断] `/ce-compound` 把经验写入 `docs/solutions/` 是 README 描述的持久化机制；实际落盘路径和格式可能随 skill 版本不同而不同。
- [未验证] 未收录替代品行（Spec Kit）以及同分类兄弟项的相对定位，反映的是截至 2026-06-26 各自 README 的框定，而非实测对比。
