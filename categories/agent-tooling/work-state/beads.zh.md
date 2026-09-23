---
name: beads
slug: beads
repo: https://github.com/gastownhall/beads
category: work-state
tags: [ai-agents, task-graph, agent-memory, dolt, versioned-sql, dependency-graph, cli, go, long-horizon-tasks, multi-agent]
language: Go
license: MIT
maturity: v1.x line, active as of 2026-06; author still self-describes as "alpha" (see caveats)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T00:55:01Z
  default_branch: main
  default_branch_sha: fa4dce4548d8d15d5478b9ad7e4f6ee7cbfabaa1
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:55:23Z
  overall: B
  overall_score: 3.4
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@beads/bd"
        dependent_repos_count: 0
        downloads_last_month: 22811
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        homebrew_installs_90d: 7176
        homebrew_tier: A
        release_downloads: 1352727
        release_assets: 739
        release_tier: B
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: C
      raw:
        repo_age_days: 346
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 449
        top1_share: 0.552
        top3_share: 0.724
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

# beads

beads（命令 `bd`）是一张带依赖关系、可版本控制的任务/issue 图，为 AI 编码 agent 提供持久的结构化记忆，底层由 Dolt（带版本控制的 SQL）支撑，以单个 Go 二进制（`bd`）发布；由 Steve Yegge 发起，仓库已从 `steveyegge/beads` 迁移到 `gastownhall` 组织。

![beads — 健康度雷达](../../../assets/health/beads.zh.svg)

## 何时使用

你是个独立开发者，正盯着一个编码 agent 把单个仓库做一场跨好几天的重构。每次会话被压缩、或者你重开一个新会话，agent 就忘掉它手头一半的事：两小时前在 auth 层发现的那个 bug 没了，那条“等迁移落地后再做这个”的备注从来没被持久化到任何地方，而且它会按“塞得进 token 预算的”而非“真正无阻塞的”来悄悄重排工作顺序。你一直靠一个手写的 `MEMORY.md` 来打补丁，可它根本不知道哪些任务阻塞哪些任务；一旦你让 agent 在两个分支上干活，它就会往里乱涂相互冲突的 ID。

于是你在仓库里 `bd init`，把 `bd` 二进制交给 agent。现在它的任务状态活在一张可版本控制、感知依赖关系的图里，和代码一起 commit、一起 merge —— 哈希 ID 让并行分支和多 agent 互不撞车，`bd ready` 恰好浮现那些没被阻塞的工作，`bd remember`/`bd prime` 则用 agent 真正能跨会话带走的记忆，取代那个临时的草稿文件。它离线优先、可像 git 一样分支，而这正是重点：你想要的是一张随仓库一起走的任务图，而不是一个还得登录进去的托管 tracker。

## 何时不用

- **稳定性/成熟度信号** —— 尽管有 v1.x 发布线，作者的发布博文将其描述为 "alpha" 软件，FAQ 也承认 "command flags and data formats can evolve"（截至 2026-06 维护者是否仍把 1.x 视为 alpha 未能确认）。它明确表示*不*适用于 "mission-critical production systems without a tested backup/restore plan"，也不适用于 "large enterprise deployments that need formal compatibility guarantees"。
- **人类团队 tracker** —— 没有 web UI、跨仓 dashboard、通知，也没有面向非工程人员的访问入口。这是有意为之（以此换取 agent 原生 API）。
- **跨项目工作** —— 每个数据库都是隔离的；issue 无法引用另一项目里的 issue。服务型 monorepo 或组合视图需要多个 DB 加自定义粘合代码。
- **大规模多写入** —— 嵌入模式是单写入（文件锁）；并发 agent 需要外部 Dolt server 加一套 "claim work" 约定（一种用户自定义的“谁在做什么”协议，以免两个 agent 抢同一任务）—— 这是实打实的运维开销。
- **超大 backlog** —— 据称项目自己的 FAQ 建议在超过约 10 万个 issue 后过滤导出或拆分为多个数据库（这是它的指引，未经独立基准测试）。
- **迁移/锁定** —— 导出似乎仅支持 JSONL，且未发现内置的 GitHub Issues/Jira/Linear 导入器，所以*迁出*需要自定义脚本；无论如何，你都会继承 Dolt 作为存储格式。
- **后端变动** —— 有记录的 SQLite→Dolt 以及 0.x→1.0 迁移都带 schema 修复步骤；升级并不总是无痛。
- **DB 脆弱性** —— `[未验证]` 据项目自己的文档/警告，agent 曾对 DB 执行破坏性操作（例如 `DROP TABLE`）；把它当作并非“设好就不管”，务必保留备份。
- **巴士因子** —— `[未验证]` 项目年轻，据称很大程度上由 AI 构建（"a tool that AI has built for itself"），处于一个从 `steveyegge` 改名为 `gastownhall` 的组织之下；应把单一维护者/弃坑风险视为不可忽视，尤其对于那些你无法承受重新选型成本的 mission-critical agent 工作流。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Plain markdown `MEMORY.md` / `TODO.md` | 未收录 | 零依赖、人类可读笔记比结构化更重要时，选普通 markdown。 | 零依赖且人类可读，但没有依赖关系图、没有 ready 检测、没有可安全合并的 ID —— 正是 beads 要取代的非结构化做法。 |
| GitHub Issues (+ `gh` CLI) | 未收录 | 需要带 web UI 和通知的成熟托管 tracker 时，选 GitHub Issues。 | 成熟的托管 tracker，带 web UI/通知/跨仓视图，但在线优先，不限定分支/不版本控制，缺乏面向 agent 的原生依赖图加自动 ready。 |
| Taskwarrior | 未收录 | 需要久经考验的离线 CLI 任务管理器时，选 Taskwarrior。 | 久经考验的离线 CLI 任务管理器，过滤能力丰富，但没有 SQL/版本控制后端，多 agent 合并能力较弱，也不是围绕 agent JSON 工作流构建的。 |
| Linear / Jira | 未收录 | 需要面向人类团队的同类最佳 tracker 时，选 Linear 或 Jira。 | 面向人类团队的同类最佳（工作流、dashboard、保证），但重量级、仅在线，不与代码一起版本控制，也非 agent 原生。 |
| Dolt directly (raw versioned SQL) | 未收录 | 想要版本化 SQL 且愿意自建 issue schema 和 agent 体验时，选原始 Dolt。 | 拥有同样的版本化 SQL 超能力且不带成见 schema，但你得自己搭建 issue schema、依赖逻辑、ready 检测和 agent 体验 —— beads 就是那一层有成见的封装。 |

## 技术栈

- Go（约 95%）
- Dolt —— 版本控制的 SQL 后端，通过 CGO 在进程内嵌入
- JSONL —— 导出/迁移格式
- CLI 二进制 `bd`
- 通过 Homebrew / npm(`@beads/bd`)/ shell 安装脚本分发

## 依赖

- **Dolt 后端** —— 在默认预编译二进制中以进程内嵌入（嵌入模式无需单独安装 Dolt）。`CGO_ENABLED=0` 构建仅支持 server 模式，需要外部 `dolt sql-server`。
- **Server（多写入）模式** —— 一个外部 Dolt SQL server 进程，加上 host/port/凭据配置。
- **可选** —— 一个 git remote，用于把 `.beads` 数据库随仓库一起同步（`bd dolt push/pull`）。

## 运维难度

**中等。** 单二进制嵌入模式确实低摩擦（`bd init` 即可开始；Dolt 跑在进程内；数据存于 `.beads/embeddeddolt/`）。难度上升是因为：嵌入模式是单写入（文件锁），所以任何真正的多 agent/多写入部署都意味着要搭建并运维一个带凭据的外部 Dolt SQL server;Dolt 数据库必须有意识地备份和同步（没有托管服务）；存在有记录的 schema 迁移变动（SQLite 时代以及 v0.63→v1.0 升级需要修复步骤）；而且作者警告 agent 在历史上曾对 DB 有破坏性行为，所以备份/恢复的卫生工作得靠你自己。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 70.9 小时，基于 9 个 qualifying issues/PRs。
- **维护** —— 截至 2026-06 最后 push 在 2026-06，处于 v1.x 发布线：活跃开发中。但作者仍自称其为「alpha」，FAQ 也警告 flag/数据格式可能演进，所以应视为活跃但易变，而非已稳定。[推断]
- **治理 / 巴士因子** —— `[未验证]` 由 Steve Yegge 发起；仓库已从 `steveyegge/beads` 迁到 `gastownhall` 组织。纸面上组织封装降低了字面意义上的单人巴士因子，但它据称很大程度由 AI 构建（「a tool AI built for itself」）、该组织看似为此专设——对你无法重新选型的东西，真实的巴士因子 / 弃坑风险不可忽视。
- **年龄与 Lindy** —— 创建于 2025-10，截至 2026-06 不足一年：太年轻，给不出 Lindy 裁决。高 star 增速（约 2.4 万）是热度驱动的关注，而非长寿履历——别把 star 读作持久性。[推断]
- **风险旗标** —— `[未验证]` MIT（无重新授权历史）。真正的旗标在运维侧：作者警告 agent 曾执行破坏性 DB 操作（`DROP TABLE`），Dolt 是被锁定的存储格式且仅支持 JSONL 导出，还有记录在案的 SQLite→Dolt / 0.x→1.0 迁移变动。务必保留备份；这不是「设好就不管」。

## 存疑（未验证）

- **Stars** —— 仓库页面显示约 24.8k，而一篇第三方文章引用的是 18.7k；两者未对齐。`[未验证]`
- **发布日期** —— WebFetch 返回的 1.0.x 发布日期标为 2024 年，这与 2026 年的活跃开发相矛盾；年份几乎肯定是被读错了。把具体发布日期和 "bi-weekly cadence" 说法都按 `[未验证]` 处理。
- **分发** —— Dolt 是否被打包进*每一个*安装器（brew/npm/脚本），还是仅限启用 CGO 的预编译二进制，属于推断而非确认。`[未验证]`
- **"Alpha" 标签** —— 来自作者的发布博文；截至 2026-06 维护者是否仍把 1.0.x 视为 alpha 未能确认。`[未验证]`
- **性能/规模声明** —— 数千个 issue 下亚 100ms，以及 10 万+ 的指引，都是项目自己 FAQ 的声明，未经独立基准测试。`[未验证]`
- **迁移/后端细节** —— 仅 JSONL 导出、缺少内置 GitHub/Jira/Linear 导入器，以及有记录的 SQLite→Dolt、0.x→1.0 迁移/修复步骤，均来自项目自己的文档，未经独立验证。`[未验证]`
- 一篇独立的第三方评述（starlog.is）无法抓取（HTTP 403），所以以上取舍主要依赖项目自己的 README/FAQ/博客加二手摘要。`[未验证]`
