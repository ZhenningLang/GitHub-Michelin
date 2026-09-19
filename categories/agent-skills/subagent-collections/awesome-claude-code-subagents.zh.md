---
name: awesome-claude-code-subagents
slug: awesome-claude-code-subagents
repo: https://github.com/VoltAgent/awesome-claude-code-subagents
category: subagent-collections
tags: [subagents, claude-code, agent-personas, skill-pack, voltagent]
language: Shell
license: MIT
maturity: no tagged release, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-24T06:28:05Z
  default_branch: main
  default_branch_sha: c193ad45419c13ceb49a43740186f680ad5ea264
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T10:47:03Z
  overall: A
  overall_score: 3.5
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 9
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 338
        last_commit_age_days: 9
        cohort: skill-pack
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 33
        top1_share: 0.466
        top3_share: 0.859
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

# awesome-claude-code-subagents

一套精选的 100+ 个 Claude Code subagent 定义合集——每个角色一个 markdown persona（backend-developer、code-reviewer、security-auditor……），丢进 `~/.claude/agents/` 后 Claude Code 就能把活委派给对应领域专家。

![awesome-claude-code-subagents — 健康度雷达](../../../assets/health/awesome-claude-code-subagents.zh.svg)

## 何时使用

你是一名在真实代码库上用 Claude Code 的开发者，越来越希望 agent 能有更窄、更锋利的 persona 来分派任务——diff 交给专门的 `code-reviewer`、API 工作交给 `backend-developer`、上线前过一遍 `security-auditor`——而不是让一个万能 agent 在同一个上下文窗口里把所有事都干完。自己写这些 subagent 文件很繁琐：要琢磨 frontmatter（`name` / `description` / `tools` / `model`）、把激活触发词写得让 Claude Code 能正确自动委派、再为每个领域起草一段带 checklist 的长角色提示。你更想从一套已被验证过的集合起步，再做删减。

这个 repo 提供的正是这套起步集：154+ 个 subagent markdown 文件，按 10 个类别组织（核心开发、语言专家、基础设施、质量与安全、数据与 AI、开发者体验、专项领域、商业与产品、元/编排、研究与分析）。每个文件都是带标准 frontmatter 和详细角色描述的真实 persona——不是指向别处的链接。安装方式有四种：Claude 插件市场、交互式 `install-agents.sh`、手动拷进 `~/.claude/agents/`、或 `curl`。装好后，Claude Code 可以靠匹配 `description` 自动委派给某个 subagent，你也可以显式调用（“让 code-reviewer subagent 看看我最近的提交”）。当你想快速拿到广覆盖的角色集、并愿意收敛到自己真正会用的那几个时，就用它。

## 何时不用

- **你已经在维护自己的 subagent/skills。** 154 个 persona 是很大的审计面；把它们叠到一套你已经信任的 agent 集上，会带来 `description` 触发词重叠和自动委派不可预测。请有意识地只采纳一个子集，而不是整包装上。
- **你不在 Claude Code 上。** 这些文件用的是 Claude Code 的 subagent 格式和 `~/.claude/agents/` 加载机制。在 Cursor、OpenCode、Codex、Droid 或自研 harness 上没有原生 loader 认这套格式——不经改造的话 markdown 本身不会自动触发。[推断]
- **你想要被强制执行的行为。** subagent 就是一段提示；它的 checklist 和“务必做 X”都是模型可以偏离的建议性指令，不是硬闸门。别把 "security-auditor" 当成真扫描器或 CI 检查的替代品。
- **触发冲突对你很关键。** 几十个 agent 的 `description` 字段都在争自动委派，某个任务到底触发哪个并不总是显而易见；装得越多，路由越难推理。[推断]
- **维护 / 固定版本。** 没有 tagged release，你跟的是 `main`。一次新提交可能新增、改名或改写 agent，从而改变路由方式。把你依赖的文件 vendor 下来，别盲目重新拉取。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [wshobson/agents](wshobson-agents.zh.md) | ✅ | 需要另一套大型 Claude Code subagent 合集时，选 wshobson/agents。 | 另一套大型 Claude Code subagent 合集。按各自覆盖的角色、frontmatter 约定、以及每个 persona 提示的主张强度来比——两者都是“丢进 `~/.claude/agents/`”的包，所以按覆盖面和提示质量选，而不是按格式。 |
| [antfu-skills](../personal-collections/engineering-workflows/antfu-skills.zh.md) / [dimillian-skills](../personal-collections/engineering-workflows/dimillian-skills.zh.md) / [khazix-skills](../personal-collections/knowledge-content/khazix-skills.zh.md) | ✅ | 需要个人 skill 合集而不是 subagent persona 时，选对应个人集合。 | 个人 *skill* 合集（`Skill` 工具格式），不是 subagent persona。消费单元不同——skill 是按需加载的流程，subagent 是被委派的子对话。想把行为加载进主 agent 用前者，想要独立的委派专家用本项目。 |
| gstack…… | 未收录 | 已收录的都不合适时，选本族里其余的个人 skill 合集。 | 与已收录集合的消费单元相同，但本页尚无对应页面，覆盖面与维护情况未评估。 |
| Anthropic 内置 subagent 文档 / 自己手写的 agent | 未收录 | 需要自己创作 subagent 的原生方式时，选内置文档或手写 agent。 | 自己创作 subagent 的原生方式。本 repo 是叠在同一机制上的第三方起步集，因此可能与你已写的 agent 重复或冲突。 |
| [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) / SDLC 方法论包 | 部分已收录 | 需要给单个 agent 加 brainstorm→plan→TDD→verify 工作流纪律时，选 Superpowers 或同类方法论包。 | 那类包给单个 agent 装的是*工作流纪律*（brainstorm→plan→TDD→verify）；本项目装的是一*组角色专家*。正交——可以同时用，但解决的是不同问题。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— [未验证] 最近一次 push 在 2026-06，未归档，open issue 很少（约 2 个）；截至 2026-06 提交活动是当前的，因此读作**活跃维护**。没有 tag release 意味着你跟的是会动的 `main`，而非固定切片。
- **治理与 bus factor** —— [推断] 组织所有（`VoltAgent`）；这类单仓 persona 合集通常靠一小撮维护者，约 22k star（2026-06）代表热度而非治理保证。无基金会背书。
- **年龄与 Lindy** —— [推断] 创建于 2025-07，截至 2026-06 约 1 岁：年轻且被热捧，**还谈不上 Lindy 赌注**。它所针对的 `~/.claude/agents/` subagent 格式本身就很新；在把它定为标准前，把寿命当作未经证实。
- **风险标记** —— [推断] 无版本的 `main` 是主要的变动风险——一次 push 可能改名或改写 persona、并改变自动委派的路由。未见 relicense/CVE 信号；全仓 MIT。

## 存疑（未验证）

- [未验证] 2026-06-26 的 GitHub 元数据：license MIT，主语言 Shell（来自安装脚本），无 tagged release（`latestRelease` 为 null），最后 push 于 2026-06-24，未归档——依赖当前内容前请重新核验。
- [未验证] star 数（2026-06-26 GitHub 显示约 22.4k）不可靠且对日期敏感；仅作参考，别当质量信号。
- [未验证] agent 数量在 repo 描述里写 "100+"、在 README/站点文案里写 “154+ 跨 10 类”；确切数量和类别拆分会随 `main` 漂移，本页未逐文件清点。
- [未验证] frontmatter schema（`name` / `description` / `tools` / `model`，其中 `model` 路由到 opus/sonnet/haiku）以及自动委派 vs 显式调用的行为均来自 README；逐个 agent 的保真度和实际路由未独立实测。
- [推断] 因为每个 subagent 都是 Claude Code 加载的一段提示，其 checklist 和听起来“强制”的步骤都是建议性的——模型可以偏离；它们不是被强制保证的。
- [推断] 安装/加载是 Claude-Code 专属的；在其他 harness 上使用需要格式改造，未确认可原样工作。
