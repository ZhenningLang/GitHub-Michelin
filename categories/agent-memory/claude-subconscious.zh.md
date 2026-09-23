---
name: Claude Subconscious
slug: claude-subconscious
repo: https://github.com/letta-ai/claude-subconscious
category: agent-memory
tags: [claude-code, letta, plugin, cross-session-memory, hooks, demo]
language: TypeScript
license: MIT
maturity: v2.1.1, active demo (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-05-13T00:56:41Z
  default_branch: main
  default_branch_sha: 795046e5e5e4edc2d44e0bc21cda9cbd8f4169bb
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:39:12Z
  overall: C
  overall_score: 2.2
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 12
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: C
      raw:
        repo_age_days: 252
        last_commit_age_days: 12
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.739
        top3_share: 0.958
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
    responsiveness: { reason: no_window_signal }
---

# Claude Subconscious

一个 Claude Code 插件：在后台跑一个 Letta agent，观察你的会话、积累长期记忆块，再通过 hook 把跨会话的指引“低语”回每一次 prompt。

![claude-subconscious — 健康度雷达](../../assets/health/claude-subconscious.zh.svg)

## 何时使用

你是 Claude Code 的重度用户，每个会话都在反复解释同样的事——你惯用的测试 runner、这个仓库用的是 pnpm 不是 npm、你上周做的某个架构决定它又“忘了”。Claude Code 的上下文在每个会话结束时就消失，于是同样的纠正一遍遍重来。你想要一个能在会话之间**累积**的记忆层，而不必手工维护一份巨大的 CLAUDE.md。Claude Subconscious 以插件形式安装，接好四个 Claude Code hook：会话结束时它异步把完整 transcript 发给一个 Letta agent（在分离的 worker 里跑，因此从不阻塞你）,agent 读你的文件、更新八个持久记忆块（`user_preferences`、`project_context`、`pending_items`、`tool_guidelines` 等），下一次 `UserPromptSubmit` 时它再通过 stdout 注入相关记忆和“低语”指引——全程不碰 CLAUDE.md。

当你本就生活在 Letta 生态里（或正想找个理由试一试）、并把它当作探索性的、单人开发的便利层时最合适：一个共享的“agent 大脑”服务多个项目，每个项目在 `.letta/claude/` 下各自保存会话记账。如果你想**亲眼看看**一个 subconscious 式后台记忆 agent 接进真实编码循环里是什么感觉，这是一个基于 Letta Code SDK、可读性不错的参考实现。

## 何时不用

- **生产 / 团队使用。** 作者明确写明这是“基于 Letta Code SDK 构建的 demo 应用，不打算用于生产”，并让你改用 Letta Code。不要在它上面搭团队工作流。
- **你不用 Claude Code。** 它从头到尾是个 Claude Code 插件，依赖 Claude Code 的 hook 生命周期（`SessionStart` / `UserPromptSubmit` / `PreToolUse` / `Stop`）。它**不是**一个 LLM 无关、框架无关的记忆库；如果你要在自己的 agent 代码里嵌记忆，选 [Mem0](mem0.zh.md) 或 [Memori](memori.zh.md)。
- **你无法依赖外部 Letta 服务。** 它需要 `LETTA_API_KEY` 和一个可达的 Letta 后端（云端 `api.letta.com` 或自托管）。没有后端就没有记忆。这是每个会话边界上的硬网络依赖。
- **涉密、不能外发的代码。** Stop hook 会把你的**完整会话 transcript** 发给 Letta agent，且 agent 能读你的文件（默认只读，但 `full` 模式会授予 bash 执行和 sub-agent 派生）。指向敏感仓库前请三思。
- **你要确定性、可审计、完全自托管、无第三方大脑的记忆。** 记忆存在 Letta agent 里，而非你完全掌控的本地存储；行为依赖 agent 模型和 Letta API 语义。
- **对延迟 / 配额敏感的工作流。** 每次会话开始、prompt、结束都会触达 Letta API；按 README，指引“需要好几个会话”才变得有用。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Mem0](mem0.zh.md) | ✅ | 可移植的应用内嵌记忆比 Claude Code 插件更重要时，选 Mem0。 | 框架无关、可嵌进你自己 agent 的记忆**库/API**（Python/TS，任意 LLM）；不是 Claude Code 插件、也不是后台“低语”agent。要可移植、偏生产的记忆选它。 |
| [Memori](memori.zh.md) | ✅ | 需要 SQL 原生记忆后端而非 Claude Code hook 时，选 Memori。 | SQL 原生的开源 agent 记忆引擎；同样 LLM/框架无关、可自托管。形态不同：是记忆后端，不是绑定 Claude Code 的插件。 |
| Letta Code | 未收录 | 想要同团队完整编码 agent 产品而不是这个 demo 时，选 Letta Code。 | 同团队的生产版本——Letta 平台上的完整编码 agent。README 明确推荐用它替代本 demo 做真实使用。 |
| CLAUDE.md（内置） | 未收录 | 手动、确定的项目记忆已经足够时，选 CLAUDE.md。 | 手动、确定、零依赖的项目记忆。没有后台学习、没有跨项目大脑；靠你手工维护。Claude Subconscious 刻意不写这里。 |
| [Cipher](https://github.com/campfirein/cipher) | 未收录 | 跨 IDE/CLI 的 MCP 记忆层比 Claude-only hook 更重要时，选 Cipher。 | 基于 MCP 的编码 agent 记忆层（经 MCP 跨 IDE/CLI 通用）；客户端支持比单工具插件更广。 |

## 技术栈

- **语言：** TypeScript（按 GitHub 约占仓库 85%；另有少量 C#、JavaScript、PowerShell）。[未验证] 语言占比是 GitHub linguist 估算。
- **运行时：** Node.js（TypeScript hook 脚本：`session_start.ts`、`sync_letta_memory.ts`、`pretool_sync.ts`、`send_messages_to_letta.ts`）。
- **集成面：** Claude Code 插件 + 四个 hook(`SessionStart`、`UserPromptSubmit`、`PreToolUse`、`Stop`)；内容以 stdout XML 标签注入（`<letta_message>`、`<letta_memory_blocks>`、`<letta_memory_update>`）。
- **记忆后端：** 经 `@letta-ai/letta-code-sdk` 的 Letta agent；八个记忆块；多项目“一个 agent，多个项目”模型。
- **模型：** Letta 暴露的任意 LLM 提供商（OpenAI / Anthropic / Google / 等），通过 `LETTA_MODEL` 选择。

## 依赖

- **Claude Code**（必需；README 未指定版本）。
- **Node.js**（必需；未指定版本）。
- **`@letta-ai/letta-code-sdk`**（作为依赖安装）。
- **一个 Letta 后端**——云端（`api.letta.com`）或经 `LETTA_BASE_URL` 自托管。
- **`LETTA_API_KEY`**（必需；来自 app.letta.com）。用非默认模型时可能还需提供商 key。
- **磁盘状态：** `.letta/claude/conversations.json`、`.letta/claude/session-{id}.json`、`$TMPDIR/letta-claude-sync-$UID/` 下的临时日志；全局配置在 `~/.letta/claude-subconscious/config.json`。[推断] 全局配置路径据 README 描述推断。

## 运维难度

**安装很轻，但拖着一条外部服务的尾巴。** 安装是两行插件命令（`/plugin marketplace add …` 再 `/plugin install …`）加设一个 `LETTA_API_KEY`。难点不在搭建复杂度而在运营依赖：你现在在每个会话边界都被绑定到某个 Letta 服务器的可用性、配额和延迟上，而一个分离的后台 worker（120s 超时）在带外做 transcript 同步——那里失败对前台是静默的。自托管 Letta 以去掉云依赖会把运维难度抬到**中**。Linux 上有针对 tmpfs 跨设备错误的 `TMPDIR` 变通做法。

## 健康度与可持续性

- **响应速度**：无法计算——unknown。
- **维护——放缓，demo 阶段（截至 2026-06）。** 最新发布 v2.1.1（2026-03-30，「Bug fixes」）；最后推送 2026-05-13——到 2026-06 已有一两个月没动静，近期无活动。未归档，但节奏读起来像在一个 demo 上滑行，而非在做活跃的产品开发。
- **治理与背书——厂商 demo（Letta）。** 归在 `letta-ai` 名下，即 Letta 平台背后的同一团队；背书是真的，但这个仓库明确是 *demo*，团队让你用 Letta Code 做生产。组织不会消失，但它没有动力去加固这个 demo。[推断]
- **年龄与 Lindy——年轻且明示不用于生产。** 2026-01 创建，约 5 个月（截至 2026-06）。无历史沉淀，且作者声明不作生产用途；Lindy 不适用——这是参考实现，不是可持久的押注。
- **风险信号——外部大脑依赖 + transcript 出域。** MIT（无重许可风险），但每个会话边界都要触达 Letta 后端（云端或自托管），Stop hook 会把完整 transcript 发出本机，记忆存在第三方 agent 里而非你自有的存储。主导风险是明示的 demo 定位、硬网络依赖与数据出域。

## 存疑（未验证）

- [未验证] 最新 release v2.1.1("Bug fixes")，发布于 2026-03-30；仓库 push 于 2026-05-13——日期据 2026-06-26 的 `gh repo view`。
- [未验证] 截至 2026-06 约 2.8k stars——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 语言占比（TypeScript ~85.5%、C# ~10.3% 等）是 GitHub 估算；C# 部分 README 未解释，可能是工具/示例代码。
- [推断] README 未声明所需的 Node.js 与 Claude Code 最低版本；版本兼容性视为未验证。
- [推断] “八个记忆块”的命名与全局配置路径取自 README/架构描述，未独立查阅源码核实。
- [未验证] “不打算用于生产”是作者自述；无任何成熟度/SLA 主张被独立验证。
