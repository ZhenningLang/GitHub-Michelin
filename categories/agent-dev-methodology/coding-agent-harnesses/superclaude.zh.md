---
name: SuperClaude Framework
slug: superclaude
repo: https://github.com/SuperClaude-Org/SuperClaude_Framework
category: coding-agent-harnesses
tags: [claude-code, slash-commands, agents, personas, behavioral-modes, mcp, config-framework]
language: Python
license: MIT
maturity: v4.3.0, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-13T16:40:33Z
  default_branch: master
  default_branch_sha: 226c45cc93b865108843a669c6545d421784b68c
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:18:03Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 67
        active_weeks_13: 1
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
        repo_age_days: 376
        last_commit_age_days: 67
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 41
        top1_share: 0.409
        top3_share: 0.812
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
    responsiveness: { reason: no_traffic }
    adoption: { reason: registry_no_counts }
---

# SuperClaude Framework

一个用 Python 安装的配置层，通过行为指令注入，给 Claude Code 装上 30 个 `/sc:` 斜杠命令、20 个专用 agent、7 种行为模式以及 MCP 接线。

![superclaude — 健康度雷达](../../../assets/health/superclaude.zh.svg)

## 何时使用

你是个常驻 Claude Code 的开发者，老在反复敲同样的长 prompt——“扮演安全审查员”“先头脑风暴再实现”“请节省 token”——你希望这些结构变成一个词的命令，而不是每个 session 都粘一大段。你跑 `pipx install superclaude && superclaude install`，于是 `/sc:brainstorm`、`/sc:implement`、`/sc:troubleshoot`、`/sc:document` 等约 30 个命令成了一等公民，外加 20 个领域 agent（安全工程师、前端架构师、深度调研 agent、PM agent），框架按上下文路由到它们。重点是你不想从零发明自己的 persona/命令脚手架——SuperClaude 给你一套有主见、开箱即用的方案，以及一个把 agent/命令 markdown 落到 `~/.claude/` 的安装器。

当你想在原始模型之上叠一层行为*模式*时它也合适：Brainstorming 模式在写码前先盘问需求、Token-Efficiency 模式应对长 session、Introspection/任务管理模式处理多步工作。装一次，就拿到整套命令+agent+模式；还能可选地通过 `superclaude mcp` 接上 8 个 MCP 服务（Context7、Serena、Playwright、Magic、Sequential-Thinking 等）。如果你的团队统一用 Claude Code、想要一套共享命令词汇表，它是一个打包好的起点，而不是 DIY 的配置仓库。

## 何时不用

- **你不用 Claude Code。** 它*只*针对 Claude Code——没有 Cursor / Codex / opencode / Droid / 通用 agent 路径。如果你的 harness 是别的，这里几乎都用不上。[推断]
- **你想要极简、完全自己掌控的配置。** 它往 `~/.claude/` 注入很大的面（30 命令 + 20 agent + 7 模式）；如果你偏好少数几条自己写、完全看得懂的命令，这是一大堆要审计和裁剪的不透明脚手架。
- **你不信任自动路由 / “自动 agent 协调”。** 行为由框架自身的分发和行为指令注入驱动；排查某个 agent 或模式*为何*触发，意味着要读 SuperClaude 叠在 Claude Code 原生机制之上的 markdown 层。
- **你想要有保证的性能收益。** 宣传称可选 MCP 带来“2-3 倍更快”“少 30-50% token”——这些是项目自己的说法，依配置而定，本页未独立基准测试。
- **变动 / 版本耦合。** v4 是近期重写，且已宣布 v5 的 TypeScript 插件系统；命令名、agent 名册和 `~/.claude/` 安装布局会随版本变，TS 重写还可能整个改掉安装模型。
- **你只需要一个能力。** 如果你只想要比如结构化头脑风暴或一个调研模式，装整套电池（还有它的 MCP 配置）比复制单个命令重得多。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Superpowers](superpowers.zh.md) | ✅ | 需要强调可复用 skills 的 Claude Code skill/plugin 集合时，选 Superpowers。 | Claude Code 的 skill/plugin 集合，强调可复用的“skills”；“给 Claude Code 一整套能力电池”这个目标有重叠，打包方式不同（plugin/skills vs 安装式命令+persona 框架）。 |
| [get-shit-done](../spec-driven-development/get-shit-done.zh.md) | ✅ | 需要面向 agent 开发的有主见工作流/命令包时，选 get-shit-done。 | 面向 agent 开发的有主见工作流/命令包；更窄、工作流优先，而非 SuperClaude 那种广覆盖的命令+agent+模式面。 |
| [Compound Engineering](compound-engineering.zh.md) | ✅ | 需要让 agent 工作复利累积的方法论加插件时，选 Compound Engineering。 | 让 agent 工作“复利累积”的方法论加插件；是带工具的开发*哲学*，而非配置注入框架。 |
| [ECC](ecc.zh.md) | ✅ | 需要上下文工程方法论，而不是可安装命令套件时，选 ECC。 | 面向 agent 的上下文工程方法论；偏概念/流程框架，而非可安装的命令套件。 |
| [12-Factor Agents](../spec-driven-development/12-factor-agents.zh.md) | ✅ | 需要构建可靠 LLM agent 的原则时，选 12-Factor Agents。 | 构建可靠 LLM agent 的原则——是你读的规范/宣言，不是装进 Claude Code 的软件。 |
| claude-code-templates / awesome-claude-code | 未收录 | 需要面向 Claude Code 的社区配置/模板集合，并按需复制粘贴时，选这些社区集合。 | 面向 Claude Code 的社区配置/模板集合；更轻、按需复制粘贴，而非 SuperClaude 那种安装式、协调好的框架。 |

## 技术栈

- **语言：** Python（依仓库 `primaryLanguage`）。
- **CLI / 安装器：** `click`（命令行界面）、`rich`（终端输出）、`pytest`（在 `pyproject.toml` 里声明为运行时依赖，少见——通常是开发依赖）。[推断]
- **分发：** PyPI 包 `superclaude`（用 `pipx` 安装）；也以 `@bifrost_inc/superclaude` 发布到 npm；另有 `./install.sh` 的 git 路径。
- **载荷：** 把 agent/命令/模式的 markdown 定义安装进 `~/.claude/agents/` 及相关 Claude Code 配置位置；行为指令注入是核心机制（无独立运行时服务）。
- **可选集成：** 通过 `superclaude mcp` 接线的 8 个 MCP 服务——Context7、Sequential-Thinking、Serena、Playwright、Magic、Morphllm-Fast-Apply、Chrome DevTools、Tavily。

## 依赖

- **运行时：** Python ≥ 3.10（依 `pyproject.toml` 的 `requires-python`）。真正的前置条件是一个可用的 Claude Code 安装——没有它，框架是惰性的。
- **Python 依赖（v4.3.0）:** `click` ≥ 8.0.0、`rich` ≥ 13.0.0、`pytest` ≥ 7.0.0。
- **安装：** `pipx install superclaude` 然后 `superclaude install`；或克隆后 `./install.sh`；或 `npm i -g @bifrost_inc/superclaude`。
- **可选：** 那 8 个 MCP 服务各自带自己的 Node/Python 运行时和（部分）API key——通过 `superclaude mcp` 单独安装，不打包在内。

## 运维难度

**低。** 这是一个客户端的开发工具配置，不是部署的服务：`pipx install` + `superclaude install` 把文件写进 `~/.claude/` 就完事——没有服务器、没有数据存储、没有要常驻维护的编排。维护负担来自：(a) 升级后重跑 `superclaude install` 并调和 `~/.claude/` 配置的改动；(b) 可选 MCP 服务，它们带自己的运行时/key，是最可能出问题的部分；(c) 与一个正处在 v4→v5（TypeScript）过渡期、快速变动的项目耦合，这会改变安装布局。生产环境里没有什么要扩容或监控的。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）：** 活跃维护——仓库 push 于 2026-06-13，最新 release v4.3.0（2026-03-22），未归档。v4 是近期重写、已宣布 v5（TypeScript 插件），因此推进很快、并非 coasting——但安装布局会在 v4→v5 过渡中变化。
- **治理与背书：** Organization 持有（SuperClaude-Org）——是社区/组织结构而非单一账号，这在 bus-factor 上比单用户仓库略好。未公布基金会或商业厂商背书；实质上是社区维护的框架。
- **年龄与 Lindy（2026-06）：** 创建于 2025-06，约 1 岁，约 23k star。年轻，且正处重写中段（v4 刚出、v5 已宣布），意味着你今天采用的契约可能熬不过下一个大版本。Lindy 裁决：**按年龄看属未经验证**——现在可用，但请 pin 版本，并预期命令/agent 名册与安装模型的抖动。
- **风险标记：** MIT（无 relicense）。锁定在于**只支持 Claude Code** [推断]——几乎没有东西能迁到别的 harness。可选 MCP 服务是最可能出问题的面（各带运行时/key）。未审 CVE。

## 存疑（未验证）

- [未验证] “30 命令 / 20 agent / 7 模式 / 8 MCP 服务”的数量来自项目 README/发布说明；具体名册随版本变动——请对照你那个版本实际安装的文件核实。
- [未验证] 最新发布 v4.3.0 于 2026-03-22；仓库 `pushedAt` 为 2026-06-13（活跃）；截至 2026-06 star 约 23.4k——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 性能说法（“2-3 倍更快”“少 30-50% token”）是项目对可选 MCP 的自我表述，依配置而定；无独立基准测试。
- [推断] `pytest` 出现在运行时 `dependencies`（而非仅开发依赖）取自所抓取的 `pyproject.toml`；可能是有意为之（安装器自测）或打包上的小问题。
- [推断] “只支持 Claude Code”是从 README 表述和 `~/.claude/` 安装目标推断的；没有记录其它 agent 的支持，但未提及不等于证明没有。
- [未验证] 已宣布的 v5.0 TypeScript 插件系统是路线图，尚未发布；时间点以及是否保留当前安装模型都未确认。
