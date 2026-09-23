---
name: FreshRSS
slug: freshrss
repo: https://github.com/FreshRSS/FreshRSS
category: reading-tools
tags: [reading-tools, freshrss, app]
language: PHP
license: AGPL-3.0
maturity: active, ~15,476 stars (as of 2026-07)
last_verified: 2026-07-06
type: app
upstream:
  pushed_at: 2026-07-06T11:22:52Z
  default_branch: edge
  default_branch_sha: cb13091b3722566e5cacf1592816f6552df408ae
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:59:05Z
  overall: B
  overall_score: 3.17
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 2.6
        qualifying_issues: 38
        band: relaxed_solo
        window_offset_days: 6
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: null
        canonical_package: null
        docker_pulls: 38283056
        docker_image: freshrss/freshrss
        docker_tier: B
        signal_basis: docker
    longevity:
      grade: A
      raw:
        repo_age_days: 5084
        last_commit_age_days: 2
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 34
        top1_share: 0.533
        top3_share: 0.746
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---
# FreshRSS

A free, self-hostable news aggregator…

![FreshRSS — 健康度雷达](../../assets/health/freshrss.zh.svg)

## 何时使用

你正在为一个落在 `reading-tools` 分类里的任务选择开源基础设施，需要评估一个真实仓库，而不是只在对比表里看到一个名字。当 FreshRSS 的上游描述贴合任务，并且采用现成项目比从零写胶水代码更划算时，你把它列入候选。

这个首版页面存在，是因为 FreshRSS 在 atlas backlog 里反复作为对比候选出现。请把它当作有 intake 依据的起点：先核验上游 README 和许可证，再和下方已收录的邻近页面对照，然后再决定是否引入依赖。

## 何时不用

- **你今天就需要一篇已经深度审过的 atlas 页面。** 在本页完成上游文档语义复核前，优先使用横向对比表里更成熟的已收录页面。
- **GitHub 元数据暴露了你的硬约束。** 如果许可证、归档状态或维护节奏是关键约束，优先选择本分类里核验更充分的替代品，而不是直接依赖 FreshRSS。
- **你的任务需要更窄、更专门的替代品。** 如果某个现有页面的“何时不用”已经点名你的约束，应优先按那个页面选型；本页只是较宽的首版入口。
- **你承受不了上游变动或运维未知数。** 请选择 Lindy 记录更长、运维画像更清楚的已收录项目。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Just Read](just-read.zh.md) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 FreshRSS 对照。 | FreshRSS 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |
| [NetNewsWire](netnewswire.zh.md) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 FreshRSS 对照。 | FreshRSS 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |
| 自写集成 | 未收录 | 只有需求很小、维护成本明确低于引入 FreshRSS 时，才自写。 | 自写能少一个依赖，但会失去上游项目、生态和本页记录的选型取舍。 |

## 技术栈

- **主要语言：** GitHub 元数据返回为 PHP。
- **仓库：** `FreshRSS/FreshRSS`。
- **项目形态：** atlas 路由暂归为 `app`；把它当稳定 API 契约前，请复核上游架构。
- **上游状态：** 默认分支 `edge`，最后 push `2026-07-06T11:22:52Z`，archived 为 `false`。

## 依赖

- **运行时依赖：** 本次 intake 未穷尽核验；生产使用前请检查上游依赖清单。
- **外部服务：** 本次 intake 未穷尽核验；请确认是否需要数据库、队列、云 API、浏览器运行时、GPU 或模型供应商凭据。
- **运维输入：** 至少依赖该 GitHub 仓库及其发布和更新流程。

## 运维难度

**在重读上游文档前，按未知到中等处理。** library 形态的项目可能很容易试用，但仍需要 pin 版本并审查升级。app、service、framework 形态可能隐藏数据库、worker、存储、认证、浏览器、GPU 或云厂商要求，因此请把这个首版页面当成 intake 标记，而不是完整运维手册。

## 健康度与可持续性

- **维护快照：** 截至 2026-07-06，GitHub 返回 `archived=false`，`pushed_at=2026-07-06T11:22:52Z`。
- **采用快照：** 2026-07 约 15,476 个 GitHub stars；stars 只是有噪声的采用信号。
- **许可证快照：** GitHub API 返回 `AGPL-3.0`；许可证关键时必须检查仓库内许可证文件。
- **Lindy 与治理：** 本次 intake 未完整复核。长期采用前，请继续检查组织归属、项目年龄、发布节奏和 bus factor。
- **风险信号：** 本页是从 backlog 元数据生成的首版页面。

## 存疑（未验证）

- [未验证] 这是依据 GitHub 元数据和 2026-07-06 backlog 生成的首版 intake 页面；高风险选型前，请重新阅读上游 README、文档、许可证文件和 release notes。
- [推断] 横向对比表先使用同分类已收录页面作为起点；后续语义复核应把泛化邻居替换成最接近的真实替代品。
