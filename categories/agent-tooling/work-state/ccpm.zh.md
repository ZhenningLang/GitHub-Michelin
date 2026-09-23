---
name: CCPM
slug: ccpm
repo: https://github.com/automazeio/ccpm
category: work-state
tags: [spec-driven, project-management, github-issues, git-worktrees, parallel-agents, agent-skill, prd, epics, claude-code, shell]
language: Shell
license: MIT
maturity: v2 (Agent Skills compatible), active; last push 2026-03, no tagged GitHub releases (as of 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-03-18T12:15:24Z
  default_branch: main
  default_branch_sha: 7d7e4623bc6d4c0c9ba66ca6bfecd7e5261dc697
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:55:24Z
  overall: C
  overall_score: 2.25
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 188
        active_weeks_13: 0
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
        repo_age_days: 400
        last_commit_age_days: 188
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

# CCPM

一个 spec-driven 的项目管理 skill（bash 脚本 + skill 提示词），把 PRD 转成 GitHub Issues，并借助 git worktree 让多个编码 agent 并行干活——项目状态存在 markdown 文件里，而不是聊天记录里。

![ccpm — 健康度雷达](../../../assets/health/ccpm.zh.svg)

## 何时使用

你在带一个大到单次 agent 会话装不下的功能——一个你大致圈定了范围但还没写规格的多文件子系统。你一直在“vibe-coding”它：你描述想要什么，agent 猜，你过三条消息再纠正，等上下文窗口一压缩，半数决策背后的“为什么”就没了。当你想开第二个 agent 在另一分支上并行推进时，两个 agent 互相踩脚，你花在对账上的时间比建设还多。你想要“先写下来”的纪律，再加上一种不引发合并混乱的扇出方式。

于是你把 harness 指向 CCPM 这个 skill，说“咱们规划一下支付功能”。它带你从 brainstorm 走到一份落在 `.claude/prds/` 下的 PRD，把它解析成技术 epic，再把 epic 拆成带 `depends_on` / `parallel` / `conflicts_with` 标签的任务，然后把这些任务同步成 GitHub Issues——而 Issues 就成了整支队伍（人或 agent）共读的事实源。接着你说“开始做 issue 1234”，它会拉起一个 git worktree，让一个 agent 在隔离环境里专攻这条流，而另一个 agent 处理互不冲突的另一条。确定性查询（"standup"“哪些被卡住了”）以纯 bash 脚本跑出，所以状态是一次脚本调用，而不是一次幻觉。每个提交都能回溯到一份成文规格，这正是重点：你要的是有据可查的意图加上合并安全的并行，而不是更快地丢失上下文。

## 何时不用

- **小规模 / 单条流的活。** 改一个文件、或一次会话能装下的任务，不需要 PRD → epic → issue 的仪式；CCPM 的 5 阶段纪律在某个规模之下纯属负担。
- **没有 GitHub，或不能用 GitHub Issues。** Issues 是强制的事实源——必须有 `gh` 鉴权和一个 GitHub 仓库。没有 GitLab/Gitea/Jira 后端；如果你们的工作记录在别处，它就不合适。
- **想要给人类团队用的看板。** 这是给 agent 和工程师用的流程工具，不是 PM 仪表盘——除了 GitHub Issues 本身提供的之外，没有 board、sprint、通知或非工程师 UI。
- **超大 epic。** 工作流默认每个 epic 大致上限 ≤10 个任务；很大的工程需要手动拆成多个 epic。
- **你不信那些头条数字。** 营销口径的数据（“上下文切换减少 89%”“bug 减少 75%”“最高 3 倍提速”、内部 4/4-对-0/4 的 eval）都是自报、未经独立复现——为了**工作流**采纳，别为了百分比采纳。[未验证]
- **成熟度 / 变动风险。** 没有打 tag 的 release，且刚经历 v1→v2（"Agent Skills"）重构，意味着 skill 表面和文件布局仍可能随版本漂移；需要稳定就钉死某个 commit。
- **对 worktree 不友好的工程。** 并行执行依赖 git worktree；带大量 submodule、生成产物、或环境无法在 worktree 检出后存活的仓库，会和这套并行模型对着干。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [beads](beads.zh.md) | ✅ | 需要给 agent 持久记忆的版本化 SQL 任务图时，选 beads。 | 一个版本化 SQL 的任务**图**，给 agent 持久记忆；依赖/就绪检测后端更强，但没有 PRD→epic→GitHub-Issues 的规格流水线，也没有基于 worktree 的并行编排。CCPM 偏流程 + GitHub 原生；beads 偏存储原生的任务引擎。 |
| [Planning with Files](planning-with-files.zh.md) | ✅ | 需要更轻的 markdown 文件规划模式时，选 Planning with Files。 | 更轻的“用文件做规划”模式（计划以 agent 读写的 markdown 存在）；在“状态存文件、不存聊天”上重叠，但没有 GitHub-Issues 同步、没有强制的 PRD/epic 阶段、没有并行 worktree 扇出。 |
| [Entire](../session-history/entire-cli.zh.md) | ✅ | 需要本类目里另一种 agent 工作追踪机制时，选 Entire。 | 本类目里另一种 agent 工作追踪思路；机制不同——若两者都进了候选名单，直接对比。 |
| 手搓 GitHub Projects / Issues + `gh` | 未收录 | 想用同一个 GitHub Issues 后端但不要 CCPM 的规格纪律时，选手搓 GitHub Issues。 | 就是 CCPM 在驱动的同一后端，只是没有那套带主见的 PRD→epic→任务拆解、worktree 准备或 bash 状态脚本——规格纪律和并行约定得你自己手搓。 |
| Taskmaster（claude-task-master） | 未收录 | 需要另一种流行的 PRD 转任务 agent 工作流时，选 Taskmaster。 | 同样流行的 PRD-转任务 agent 工作流；也把规格解析成任务，但它是自带的任务存储/CLI，而不是把 GitHub Issues + git worktree 当作共享事实源。 |
| 纯 `MEMORY.md` / `TODO.md` | 未收录 | 零依赖和人类可读性比依赖元数据更重要时，选普通 markdown。 | 零依赖、人可读，但没有依赖元数据、没有 GitHub 同步、没有并行流隔离——正是 CCPM 要替换的无结构基线。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— 截至 2026-06 最后 push 在 2026-03，即距上次提交约 3 个月、且无 tagged release；近期的 v1→v2（「Agent Skills」）重构说明有真实维护，但数月空档意味着它在滑行而非快速迭代。仅约 4 个未关 issue——backlog 很低，但要结合约 8k 这个不算高的 star 数一起看。[推断]
- **治理 / 巴士因子** —— `Organization` 所有（`automazeio`），多少缓解了单维护者风险，但它仍是个小型厂商主导的 skill 仓库，而非基金会项目；路线图由运营 automaze 的人说了算，没有可指认的正式治理。[推断]
- **年龄与 Lindy** —— 创建于 2025-08，截至 2026-06 不足一年，且已经历过一次破坏性重构（v1→v2）：太年轻，给不出 Lindy 裁决，接口面仍在沉淀——需要稳定就钉死某个 commit。
- **风险旗标** —— `[未验证]` MIT，无重新授权历史。对 GitHub Issues + `gh` 的硬依赖是一个锁定面（没有 GitLab/Jira 后端），而头条指标（「上下文切换减少 89%」「bug 减少 75%」「3 倍提速」）都是自报、未经独立复现——为工作流而采纳，别为百分比而采纳。

## 存疑（未验证）

- [未验证] 各项量化指标——“上下文切换时间减少 89%”“bug 率降低 75%”“最高 3 倍提速”“5–8 个并行任务对 1 个”，以及 4/4-对-0/4 / 4/4-对-2/4 的 eval 分数——均出自项目自家 README，未经独立复现。
- [未验证] 截至 2026-06 的 star 数约 8.2k（fork 约 833）；GitHub star 不可靠且对日期敏感，仅作参考。
- [推断] 归类为 `skill-pack`，因为该仓库交付的是 bash 脚本加 skill/提示词 markdown、按 agentskills.io 标准分发，而非可部署的 service/library——因此刻意省略「技术栈 / 依赖 / 运维难度」三节。
- [未验证] “与 harness 无关”/兼容 Claude Code、Codex、OpenCode、Factory、Amp、Cursor、Droid 是 README 的说法；在各非 Claude harness 上的真实行为未经独立验证，且 LLM/agent 行为从不被保证。
- [未验证] “14 个确定性 bash 脚本”、每个 epic ≤10 任务的默认上限、`gh-sub-issue` 的可选回退、以及 v1 在独立分支的细节，均来自 README/文档，本次未逐一实地核查。
- [未验证] 未发现打 tag 的 GitHub release（`latestRelease: null`）；“v2”指的是 Agent Skills 重构，而非某个 SemVer tag——版本管理是非正式的，文件布局可能漂移。
- [推断] CCPM 把 PRD/epic 存在 `.claude/` 目录路径下，这暗示其源自 Claude Code 的约定，尽管它对外宣称与 harness 无关；依赖前请先核对你所用 harness 下的路径布局。
