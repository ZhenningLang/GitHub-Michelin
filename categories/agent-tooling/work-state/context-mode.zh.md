---
name: Context Mode
slug: context-mode
repo: https://github.com/mksglu/context-mode
category: work-state
tags: [mcp, context-window, tool-output-sandbox, session-memory, hooks, fts5, multi-platform, source-available]
language: TypeScript
license: Elastic-2.0
maturity: v1.0.x line; latest release v1.0.169 (2026-06-29), main active to 2026-09-15 — source-available (ELv2), not OSI open source
last_verified: 2026-09-15
type: tool
upstream:
  pushed_at: 2026-09-15T12:06:28Z
  default_branch: main
  default_branch_sha: 4f30f8efb63eb5dbc3fb6cff16efe2e831eaa8d4
  archived: false
health:
  schema: 1
  computed_at: 2026-09-15T15:56:11Z
  overall: D
  overall_score: 2.33
  scored_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NOASSERTION"
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
      grade: A
      raw:
        median_ttfr_hours: 158.3
        qualifying_issues: 4
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: context-mode
        dependent_repos_count: 0
        downloads_last_month: 73979
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
    longevity:
      grade: C
      raw:
        repo_age_days: 204
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 98
        top1_share: 0.788
        top3_share: 0.834
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: NOASSERTION
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
---

# Context Mode

一个 MCP server，把工具的原始输出挡在 agent 上下文窗口之外：它在隔离子进程里跑读取/抓取/日志处理（只有 stdout 回到上下文），把会话事件索引进 SQLite FTS5 让 agent 熬过 compaction，并用 hooks 把重量级工具调用「路由」进沙箱——覆盖约 18 个 agent 平台。

![context-mode — 健康度雷达](../../../assets/health/context-mode.zh.svg)

## 何时使用

你在用一个 coding agent（Claude Code、Codex、Cursor、OpenCode/Kilo、Gemini CLI……）做长链路调研：研究一个仓库、grep 一份 45 KB 的访问日志、拉 20 条 GitHub issue、截一张 Playwright 快照。这些原始 payload 会原样灌进上下文窗口，半小时后 40% 的预算就耗在了模型其实只需要「总结」的数据上。接着会话一 compact，agent 就忘了它在改哪些文件、你上一句让它干嘛。你已经厌倦了帮它照看上下文。

于是你把 Context Mode 当 MCP server 装上（Claude Code 上是一条 `/plugin` 命令，其它平台是改配置文件）。现在 agent 要处理那份日志时，它写一段小脚本调 `ctx_execute`——原始 45 KB 在隔离子进程里处理，只有 `console.log` 出来的结果（155 字节）进上下文。它的 PreToolUse/PostToolUse hooks 会自动把重量级的 Read/Bash/WebFetch 调用引导进沙箱，而每一次文件编辑、git 操作、任务和决策都写进每项目一份的 SQLite 库。compaction 触发时，一份 ≤2 KB、按优先级分层的快照把工作状态重新水化，agent 从你上一条 prompt 接着干，而不是再问一句「我们刚才在干嘛？」。你不必反复重述，就拿到明显更长的有效会话。

## 何时不用

- **你需要 OSI 认证的开源协议。** 它是 **Elastic License 2.0（source-available 源码可见）**，不是 MIT/Apache——你可以用、fork、改，但**不能**把它作为托管/受管服务对外提供，也不能重新授权。如果你的合规要求宽松开源协议，这是硬性卡点。
- **你的平台没有 hook 支持。** 只有开了 hooks 才能逼近宣传的「~98% 节省」。Antigravity IDE 和 Zed 没有 hooks——靠手工拷贝的指令文件约束，合规率约 60%，一次未路由的 `curl`/Playwright 调用就能灌进 56 KB、抹掉整段会话的节省。即便 Cursor/Kiro 也缺可用的 SessionStart，所以那里还拿不到 compaction 后的状态**恢复**。
- **你不想让任意代码执行进入回路。** 整个机制就是 agent 在 `ctx_execute`/`ctx_batch_execute` 里**写并跑脚本**。这些会继承进程的文件系统访问权（项目根目录守卫只是文件**读取**的纵深防御，不是 OS 沙箱）——批准一个 execute 工具就等于批准任意代码。请保持主机层沙箱开启。
- **你想要零运动部件。** 它需要 Node.js ≥ 22.5（或 Bun）和可用的 SQLite（`node:sqlite` / `bun:sqlite` / `better-sqlite3` 原生插件）；**Linux + Node < 22.5 不受支持**，旧 glibc/Windows 还可能撞上原生编译摩擦。它也会带来每次工具调用的 hook 开销，并在你的 prompt 里塞一段路由块。
- **你想要可保证、与模型无关的数字。** 「98% 削减 / 30 分钟 → 3 小时」是项目自己的 benchmark，随工作负载浮动；仅靠指令文件的平台会低得多。
- **你只需要任务/issue 跟踪或一个持久知识库。** 它优化的是**上下文**和**会话恢复**，不是依赖感知的任务图（[beads](beads.zh.md)），也不是 spec/PM 工作流（[CCPM](ccpm.zh.md)）。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [beads](beads.zh.md) | ✅ | 需要面向 agent 的依赖感知、版本化任务图时，选 beads。 | 面向 agent 的依赖感知、版本化任务/issue **图**（Dolt 支撑）。解决的是「哪些工作就绪且跨会话被记住」，不是「把原始工具输出挡在上下文外」。互补而非替代。 |
| [CCPM](ccpm.zh.md) | ✅ | 需要 Claude-Code spec→issue 项目管理工作流时，选 CCPM。 | 一套 Claude-Code 的 spec→issue PM 工作流（用 GitHub Issues 当后端）。管的是**做什么**；Context Mode 管的是**多少数据进窗口**。不同层。 |
| [Planning with Files](planning-with-files.zh.md) | ✅ | 基于 markdown 文件的规划/状态约定已经够用时，选 Planning with Files。 | 基于文件的规划/状态约定（磁盘上的 markdown 计划）。轻量、与工具无关；没有沙箱、FTS5 检索或 hook 强制路由。 |
| Token-Saver-MCP / MCP 输出截断类 server | 未收录 | 只需要压缩工具 payload 时，选 Token-Saver-MCP 或同类 MCP server。 | 同样压缩工具 payload 的其它 MCP server；更窄（截断/摘要）且通常单平台，相比之下 Context Mode 是 execute 沙箱 + 会话连续性 + 17 平台路由。 |
| agent 内置 compaction（`/compact`、自动摘要） | 未收录 | 免费零安装的摘要压缩已经够用时，选 agent 内置 compaction。 | 免费、零安装，但是有损摘要，没有结构化事件账本、没有 FTS5 检索、没有工具输出沙箱——正是 Context Mode 瞄准的缺口。 |
| RAG / 向量记忆库（如 Mem0、Letta） | 未收录 | 需要 embedding 驱动的持久跨会话语义记忆时，选 RAG 或向量记忆库。 | 用 embedding 做持久的跨会话**语义**记忆；更重、需 server/DB 支撑，面向长期知识——Context Mode 的 FTS5 库是每项目、本地优先、为会话内恢复调校的。 |

## 技术栈

- **语言：** TypeScript / Node.js（CLI + MCP server，npm 上以 `context-mode` 分发）。
- **运行时：** Node.js ≥ 22.5 或 Bun；`ctx_execute` 提供 12 种沙箱运行时（JS、TS、Python、Shell、Ruby、Go、Rust、PHP、Perl、R、Elixir、C#）。
- **存储 / 检索：** SQLite 配 **FTS5** 全文索引、**BM25** 排序（外加 Porter 词干、trigram 子串、reciprocal-rank-fusion 重排）；后端自动选择——`bun:sqlite`、`node:sqlite`（Node ≥ 22.5），否则 `better-sqlite3`。
- **集成：** Model Context Protocol（MCP）server，暴露 11 个 `ctx_*` 工具；agent **hooks**（PreToolUse/PostToolUse/UserPromptSubmit/PreCompact/SessionStart/Stop）做路由与会话捕获。
- **接入面：** 约 18 个平台适配器（Claude Code、Gemini/Qwen/Kimi CLI、VS Code 与 JetBrains Copilot、Copilot CLI、Cursor、OpenCode、KiloCode、OpenClaw/Pi、Codex CLI、Antigravity IDE+CLI、Kiro、Zed、Pi Agent、OMP）。

## 依赖

- **必需：** Node.js ≥ 22.5（或 Bun）和一条可用的 SQLite 路径（内置 `node:sqlite`/`bun:sqlite`，或 `better-sqlite3` 原生插件 ~`^12.6.2`）。Linux + Node < 22.5 明确不受支持。
- **宿主 agent：** 一个支持 MCP 的 agent；完整路由/连续性还要求该 agent 支持 hooks（各平台能力差异很大——见 README 兼容性矩阵）。
- **可选：** 托管的 "Insight" 看板（`context-mode.com/insight`）做组织级分析——一个独立的、面向网络的服务，与本地的核心分开。
- **核心无需外部 DB/server：** SQLite 库放在家目录下（`~/.context-mode/` / `CONTEXT_MODE_DIR`）。

## 运维难度

**低到中。** 在 Claude Code 上是两行 `/plugin` 安装，自动注册 hook，还有个 `ctx-doctor` 校验运行时/hooks/FTS5——确实低摩擦。换平台难度上升：多数平台要手工编辑 MCP + 多事件 hook 配置（各有各的坑——Codex 的 feature flag、OpenCode/Kilo 的 plugin-vs-MCP 重复坑、Cursor 被拒的 SessionStart、无 hook 的降级方案）。原生 SQLite 这块大体能自愈，但旧 glibc/Windows/Alpine 可能要 C++ 工具链。日常维护很轻（本地 SQLite、`ctx upgrade`），但跨版本升级时各平台 hook 配置的同步要你自己扛。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 158.3 小时，基于 4 个 qualifying issues/PRs（单维护者放宽档，2026-09）。
- **维护** —— commit 仍然过度活跃（最近 push 2026-09-15，6 月底以来 100+ commit），但发布渠道已停滞：最新 release／npm 版本仍停在 v1.0.169（2026-06-29），落后 `main` 约 2.5 个月（截至 2026-09）。churn 风险双向存在——main 跑得快，而守在 npm 线上的用户已经不再跟得上它。
- **治理 / 巴士因子** —— `[推断]` 单作者（`User` 所有）项目；一人维护的仓库却有约 2.3 万 star，是巴士因子警示。它在 context-mode.com 提供托管的「Insight」看板，暗示背后有商业意图，但没有可指认的基金会或团队治理——路线图由一个人定。
- **年龄与 Lindy** —— 创建于 2026-02，截至 2026-09 约 7 个月，尽管挂着 v1.0.x 标号、还拿过一次 Hacker News 第一：在 Lindy 视角下未经检验。把 star / HN 热度当作关注度，而非持久性。
- **风险旗标** —— **重新授权 / open-core 风险是头条**：它是 **Elastic License 2.0（源码可见，非 OSI 开源）**——不能作为托管服务对外提供、不能重新授权，若你需要宽松开源协议，这是硬性卡点。另需注意它在设计上允许任意代码执行（`ctx_execute`），且在「数据不出本机」的核心宣称之外又带一个托管分析面。[未验证]

## 存疑（未验证）

- **stars / 采用度** — `[未验证]` `gh` 报告约 23.0k stars／1.7k forks（2026-09-15）；GitHub stars 不可靠且对日期敏感。README 里「Used across teams at Microsoft/Google/Meta…」的徽章只有 logo、无引用来源——当作营销，而非已验证的部署。
- **协议归类** — `[推断]` SPDX `Elastic-2.0`；ELv2 是 source-available，**不是** OSI 认证的开源协议。仓库 README 自己也称其 "source-available"。依赖前先对照你组织的合规政策。
- **节省 / 续航 benchmark** — `[未验证]` 98% 削减、「315 KB → 5.4 KB」、「~30 分钟 → ~3 小时」都是项目自家 benchmark；实际节省取决于工作负载以及 hooks 是否启用（仅指令文件 ≈ 60%）。
- **「Nothing leaves your machine」声明** — `[未验证]` README 称核心无 telemetry/云同步，但又提供托管的 `ctx_insight` 组织分析看板（`context-mode.com/insight`）；核心的本地化行为是项目自述，未经独立审计。
- **平台能力矩阵** — `[未验证]` 各平台 hook 覆盖、「Full/High/Partial」会话连续性评级、以及平台数量（截至 2026-09 约 18 个）均来自 README，且会随版本变动；依赖某项能力前请核对你具体的客户端 + 版本。
- **最新版本 / 日期** — `[未验证]` v1.0.169（2026-06-29），据 npm／GitHub releases；main 活跃至 2026-09-15，据当日 `gh`；「发布停滞 vs commit 活跃」的分歧本身可能很快消解（一发新版即失效）。
- **成熟度** — `[推断]` 尽管有 v1.0.x 标号和一次 Hacker News #1 时刻，项目仍年轻且高速演进（频繁 point release、大量未关的平台集成 issue）；对你无法重新换装的工作流，应把单维护者 / churn 风险视为不可忽视。
