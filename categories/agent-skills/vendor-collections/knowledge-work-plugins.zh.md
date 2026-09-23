---
name: Anthropic Knowledge Work Plugins
slug: knowledge-work-plugins
repo: https://github.com/anthropics/knowledge-work-plugins
category: vendor-collections
tags: [knowledge-work, claude, plugins, skills, anthropic, office-tasks]
language: Python
license: Apache-2.0
maturity: active, no tagged releases, ~22.1k stars (as of 2026-06)
last_verified: 2026-06-28
type: skill-pack
upstream:
  pushed_at: 2026-06-29T09:02:53Z
  default_branch: main
  default_branch_sha: fe25f964fdfdcfe347d444b2d7cfb33a5b2cfaa5
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:53:36Z
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
        last_commit_age_days: 1
        active_weeks_13: 13
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
        repo_age_days: 242
        last_commit_age_days: 1
        cohort: skill-pack
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 30
        top1_share: 0.401
        top3_share: 0.641
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# Anthropic Knowledge Work Plugins

Anthropic 官方的一组 plugin/skill 合集，面向**知识工作**——文档、沟通、调研与日常办公任务——可安装进 Claude，而非面向写代码的工作流。

![knowledge-work-plugins — 健康度雷达](../../../assets/health/knowledge-work-plugins.zh.svg)

## 何时使用

你是一名知识工作者，或者你在为一支知识工作团队配置工具，你的一天是文档、幻灯片、简报、收件箱整理、调研摘要和进度沟通，而不是写代码。你反复在向 Claude 解释同一类办公流程（“把这些笔记变成一页纸”“起草本周更新”“总结这条调研线索”“根据这份简报搭一个 ppt 提纲”），你想要面向这类任务的官方、厂商维护的构件，而不是手搓 prompt 或一个来路不明的社区合集。你打开这个仓库，把需要的 plugin/skill 安装进 Claude，得到一套 Anthropic 维护、为知识工作任务调校的基线——而不是大多数 agent 插件合集所假定的偏写代码的栈。

你尤其会在以下情况选它：想要 Anthropic 第一方面里**知识工作**这一片——带已知 provenance 和 Apache-2.0 许可的办公/沟通/调研流程，作为你去更广或第三方合集采购之前的自然起点。采纳贴合你办公流程的部分，其余略过。

## 何时不用

- **你不在 Claude 系 harness 上。** 它绑定 Claude/Anthropic 的 loader 与 skill/plugin 格式；在 OpenCode、Codex、Droid、Cursor 或自建 agent 上没有安装器可消费它，你得逐个文件手动移植——失去一步安装这个核心价值。[推断]
- **你的工作是写代码，而非知识工作。** 这个合集的范围是文档/沟通/调研/办公任务。要 language-server 集成、code-review/commit/PR 工作流或脚手架，应去偏写代码的合集——见 [Claude Plugins（官方）](claude-plugins-official.zh.md) 和 [Anthropic Skills](anthropic-skills.zh.md)，而非本仓库。
- **你已有一套自己信任的精选 skill/command 体系。** 这些 plugin/skill 自带 description 与路由；叠加到已有方法论栈上容易重叠、重复触发。每个职责只保留一个事实源。
- **你需要固定、稳定的行为。** 没有打 tag 的 release[未验证]；你安装的是 `main` 上的内容，一次 pull 可能改变某个 plugin 的行为。需要可复现就 vendor 到具体 commit，并在更新后重新核对。
- **你在押注这个面的长期稳定。** 创建于 2026-01，这是一个**非常年轻**（截至 2026-06 约 0.5 岁）、清单与结构很可能仍在变动的项目；这里的耐久信号是 Anthropic 的背书，而非一份成型的 track record。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Anthropic Skills](anthropic-skills.zh.md) | ✅ | 需要更广的独立 skills 基线时，选 Anthropic Skills。 | Anthropic 独立的 *skills* 仓库（自包含的 `SKILL.md` 目录），更广、不限于知识工作——含文档 skill，但也含前端/画布/MCP 编写。要通用 skill 基线用它；要专门的知识工作切片用本仓库。 |
| [Claude Plugins（官方）](claude-plugins-official.zh.md) | ✅ | 写代码相关的第一方插件覆盖更重要时，选 Claude Plugins。 | Anthropic 第一方的 *Claude Code* 插件市场，偏写代码（LSP、code-review、PR/commit 包）。本仓库面向知识工作；按你的任务是办公/沟通/调研还是开发者工作流来选。 |
| 第三方/社区知识工作合集 | 未收录 | 更大、迭代更快比第一方来源担保更重要时，选社区知识工作合集。 | 更大、迭代更快的办公/沟通合集，但没有 Anthropic 的精选与 provenance 保证。本仓库是第一方基线；社区合集在更高信任成本下做延伸。 |
| 自己写 skill/plugin | 不适用 | 最高贴合度比厂商维护的知识工作构件更重要时，选自写 skill/plugin。 | 贴合度最高、零外部依赖，但放弃厂商维护的知识工作构件与已知 provenance。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— [未验证] 最近一次 push 在 2026-06，未归档；截至 2026-06 活动是当前的，故**活跃维护**。无 tag release；跟 `main`。
- **治理与背书** —— [推断] 组织所有，且由 **Anthropic 自己**背书——第一方、provenance 已知、Apache-2.0。Anthropic 官方背书是一个**强耐久信号**，实质上抵消了项目的年轻，尽管路线图仍由厂商定或转向。
- **年龄与 Lindy** —— [推断] 创建于 2026-01，截至 2026-06 仅约 0.5 岁：**非常年轻，Lindy 未经验证**。仅凭年龄这会是个弱下注；是厂商背书让它在如此年轻下仍可信——押的是 provenance，不是 track record。
- **采用/生态** —— [推断] 约 22.1k star（2026-06），对一个约 0.5 岁的仓库算高，与第一方曝光相符，但在这个年龄清单与结构很可能仍在沉淀。
- **风险标记** —— [推断] 绑定 Claude/Anthropic 生态（无跨 harness loader）；非常年轻，plugin 集合与路由预计会有变动。

## 存疑（未验证）

- [未验证] star 数（2026-06 GitHub 约 22.1k）不可靠且随时间变化；当作热度提示，而非质量信号。
- [未验证] 截至 2026-06-28 无打 tag 的 release；安装跟随 `main`，行为可能在没有版本 bump 的情况下变化。
- [未验证] GitHub 元数据显示主语言为 Python；仓库很可能混合 Python 辅助脚本与 Markdown skill/plugin 定义——语言标签是指示性的，不代表构建目标。
- [未验证] 创建于 2026-01、由 Anthropic 组织（官方）所有；年龄（约 0.5 岁）、年轻与活跃 push 状态来自 2026-06-28 的 GitHub 元数据——依赖具体细节前请重新核对。
- [未验证] 确切的 plugin/skill 清单、安装命令，以及它面向哪些 Claude 面（Claude Code / Claude.ai / API），本页未逐项枚举——请读取实时仓库 README 与目录树，而非依赖摘要。
- [推断] 因为行为存在于由 agent 加载的 plugin/skill 指令中，约束是建议性的——agent 仍可能偏离；它们描述流程，并不硬保证结果。
