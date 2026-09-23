---
name: Agency-Agents
slug: agency-agents
repo: https://github.com/msitarzewski/agency-agents
category: subagent-collections
tags: [subagents, personas, claude-code, agent-collection, multi-tool]
language: Shell
license: MIT
maturity: no tagged release, active (pushed 2026-06-22)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-29T00:32:10Z
  default_branch: main
  default_branch_sha: a597cb6d9e41b3c117ca791538764c8ccbe52119
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:51:08Z
  overall: A
  overall_score: 3.75
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
        last_commit_age_days: 1
        active_weeks_13: 11
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
        repo_age_days: 344
        last_commit_age_days: 1
        cohort: skill-pack
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 99
        top1_share: 0.284
        top3_share: 0.454
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

# Agency-Agents

约 232 个专业 subagent 人格（persona）的精选集合（markdown），覆盖 16 个职能「部门」——工程、设计、营销、安全、游戏开发、GIS 等——并附带 install/convert 脚本，可部署到 Claude Code 及另外约 11 个 agent harness。

![agency-agents — 健康度雷达](../../../assets/health/agency-agents.zh.svg)

## 何时使用

你是个人开发者或小团队，在用 Claude Code，反复手写同一批临时 system prompt：这个任务要个「前端工程师」人格，那个要「安全架构师」，再下一个要「代码评审员」。你想要一个现成的角色化 subagent 库，直接丢进 `~/.claude/agents/` 按名调用，而不是每次都手搓人格。Agency-Agents 给你一大袋——232 个按部门组织的 markdown agent 文件——每个都有 frontmatter（`name`、`description`、color）、明确使命、领域规则、交付物示例、工作流和成功指标，让 harness 派发到它时行为保持一致。

当你想一次性获得跨多领域的广度时（不只是编码——还覆盖销售、财务、支持、空间计算、GIS），以及想让同一批人格跨工具跟着你走时，尤其适合用它。仓库附带 `scripts/install.sh`（交互式选择器，自动探测已装工具，支持 `--division`/`--agent`/`--dry-run`/`--no-interactive`）和 `scripts/convert.sh`（生成各工具格式），目标包括 Claude Code、Cursor、Aider、Windsurf、OpenCode、Gemini CLI、Copilot、Codex、Kimi、Qwen 等——一次安装、只挑你需要的部门。

## 何时不用

- **你已维护着精选的 subagent/skill 集合。** 232 个人格面太大；全部丢进 `~/.claude/agents/` 会塞满 agent 选择器，并可能与你已有的命名冲突。要么选择性安装（`--division`/`--agent`），否则就是拿策展换了堆量。
- **你要的是深度与方法论而非广度。** 这些是角色*人格*（身份+工作流+成功指标），不是强制的 SDLC 纪律。若真实需求是 brainstorm→plan→TDD→verify 的严谨度，方法论包比人格目录更合适。
- **你不信「battle-tested / production-ready」的宣传。** README 宣称交付物经过验证，但仓库内没有测试框架或 QA 流程 [推断]；人格从高风险（事故响应、安全）到刻意俏皮（一个「Whimsy Injector」）都有，232 个文件质量不均。
- **你需要强制力而非建议。** 和任何 prompt pack 一样，行为是建议性的——markdown 塑造 subagent 的框架，但 harness/模型仍可忽略。没有硬保证。
- **跨工具保真度重要且你不在 Claude Code 上。** 规范格式是 Claude 风格 `.md`；转换器会输出其它工具格式，但对 11 个非 Claude harness 的转换保真度此处未独立核实。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [wshobson/agents](wshobson-agents.zh.md) | ✅ | 需要更聚焦工程角色的 Claude Code subagent 集合时，选 wshobson/agents。 | 另一个大型 Claude Code subagent 集合，偏编码。Agency-Agents 更广（还含 16 个非编码部门）且带多工具转换器；wshobson 更聚焦工程角色。按你要跨域广度还是更紧凑的纯开发集来选。 |
| [awesome-claude-code-subagents](awesome-claude-code-subagents.zh.md) | ✅ | 需要同 leaf 下的大型精选 subagent 目录时，选 awesome-claude-code-subagents。 | 同 leaf 下另一个大型精选 subagent 目录。按策展理念、以及你真正想装多少人格 vs 仅浏览来对比。 |
| [antfu/skills](../personal-collections/engineering-workflows/antfu-skills.zh.md) | ✅ | 需要个人 skills 工作流而不是角色人格时，选 antfu/skills。 | 个人 *skills* 集合（任务工作流），不是角色人格——消费单位不同。skills 解决「怎么做 X」，人格解决「扮演 Y」。 |
| Anthropic 官方/内置 agent 示例 | 未收录 | 只需要平台自带的 subagent 示例时，选 Anthropic 官方或内置示例。 | 平台自带的 subagent 示例；Agency-Agents 是第三方批量目录叠在其上，名称与角色可能与原生重叠或重复。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— 活跃：最后推送 2026-06，未归档（截至 2026-06），但没有可 pin 的 tagged release——你跟的是一条移动的分支。节奏看上去活跃；232 个人格的面意味着各文件维护程度不一。
- **治理与 bus factor** —— 单维护者的个人仓库（`User` 所有，`msitarzewski`），star 数极高（截至 2026-06 约 11.6 万）。一个 `User` 所有、star 数如此之大的仓库本身就是 **bus-factor 旗标**：路线图和多工具转换器都由一个人把控，背后没有团队或组织——关注度与单点故障并存。
- **年龄与 Lindy** —— 创建于 2025-10，截至 2026-06 约 0.7 年：相对其热度还很年轻，Lindy 上未经验证。高 star 反映覆盖面而非耐久度——把长寿当作尚未确立。
- **采用与风险旗标** —— MIT 许可（复用清晰）。「battle-tested / production-ready」是宣传话术，仓库内无测试或 QA 证据；人格质量不均（事故响应与「Whimsy Injector」并存），对约 11 个非 Claude harness 的跨工具转换保真度未经核实。建议选择性安装，而非一次性把 232 个全丢进去。

## 存疑（未验证）

- [未验证] License 为 MIT、主语言为 Shell（install/convert 脚本），据 GitHub 元数据（2026-06-26）；仓库最后 push 于 2026-06-22，未报告 tagged release——固定行为前请重新核实。
- [未验证] Star 数（GitHub 上 2026-06-26 约 11.6 万）不可靠且对日期敏感；仅作参考，非质量信号。
- [未验证] Agent 数量（约 232）与 16 部门拆分来自 README/landing page，此处未逐文件计数核实；实际 `agents/` 目录可能不同且会随时间变化。
- [未验证] 支持目标列表（Claude Code、Copilot、Antigravity/Gemini、Gemini CLI、OpenCode、Cursor、Aider、Windsurf、OpenClaw、Qwen、Kimi、Codex）来自 README；各工具的转换保真度此处未核实。
- [推断]「battle-tested / production-ready」是宣传话术，仓库内无测试或 QA 证据；人格质量不均（高风险角色与俏皮角色并存）。
- [推断] 因行为存于由 harness 加载的 markdown 人格，强制力是建议性的——subagent 仍可偏离；使命与「规则」是 prompt 级指令，非硬保证。
