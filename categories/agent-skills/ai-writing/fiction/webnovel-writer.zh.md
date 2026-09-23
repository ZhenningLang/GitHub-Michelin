---
name: Webnovel Writer
slug: webnovel-writer
repo: https://github.com/lingfengQAQ/webnovel-writer
category: fiction
tags: [claude-code, novel-writing, long-form-writing, rag, continuity, story-memory]
language: Python
license: GPL-3.0
maturity: v6.2.1, active, 5.6k stars (as of 2026-07)
last_verified: 2026-07-13
type: tool
upstream:
  pushed_at: 2026-07-07T06:06:39Z
  default_branch: master
  default_branch_sha: 59654ccaa17f240c5ae41fe51db9443284f8ca1f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:42:28Z
  overall: C
  overall_score: 2.0
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 5
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 13.3
        qualifying_issues: 6
        band: relaxed_solo
        window_offset_days: 0
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 42
        release_assets: 7
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 263
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
---

# Webnovel Writer

一个运行在 Claude Code 内的长篇中文网文创作插件：把故事事实、章节提交、检索、审查和只读面板串成连续性工作流，而非一次性续写提示词。

![Webnovel Writer — 健康度雷达](../../../../assets/health/webnovel-writer.zh.svg)

## 何时使用

你是已在 Claude Code 写连载小说的作者，写到几十章后模型开始让人物动机、时间线、世界规则和伏笔互相矛盾。你需要每章都经过上下文准备、起草、审查、事实提取、章节提交，以及派生状态、索引和摘要投影。此时选 Webnovel Writer，而不是通用写作提示词，因为它在项目内保存可追溯的故事系统和可查询的连续性状态，不会把每章当成孤立对话。

你接受 Claude Code 插件式流程，初始化一本书后用 `init`、`plan`、`write`、`review`、`query`、`learn`、`dashboard` 和 `doctor` 推进连载。语义 RAG 是可选项：没有 embedding 凭据时会回退到 BM25，仍可走本地关键词检索。

## 何时不用

- **你需要独立桌面小说编辑器，或根本不用 Claude Code。**改选 [novelWriter](https://github.com/vkbo/novelWriter) 或 [Manuskript](https://github.com/olivierkes/manuskript)：它们面向独立长篇写作，而本项目是 Claude Code 插件。
- **你只写短篇、单篇文章或一次性营销文案。**改用聚焦的起草提示词或小型写作技能；故事合同、章节提交、SQLite 索引、投影与审查闸门只有在“连贯性”真是核心问题时才值得这份配置成本。
- **你的政策不允许正文上下文发送给外部 embedding 或 rerank API。**改用纯本地检索栈，或接受本项目的 BM25 回退；其文档里的语义 RAG 配置使用兼容接口的外部 embedding 和 rerank 端点。
- **你要分发未经 GPL 评估的专有组合衍生品。**改选宽松许可的替代品，或先取得法务意见；本仓库是 GPL-3.0。
- **你需要独立基准证明它能处理某个具体篇幅。**把项目宣称的 200 万字体量标为未验证，并用代表性书稿试跑；本次调研未发现公开基准。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Humanizer-zh](../de-ai-writing/humanizer-zh.zh.md) | ✅ | 长篇故事事实和章节连续性失控时选 Webnovel Writer；只需润色中文文案时选 Humanizer-zh。 | Webnovel Writer 维护项目状态并跑多阶段写作流程；Humanizer-zh 是轻量的建议式改写技能。 |
| [Baoyu Skills](../content-production/baoyu-skills.zh.md) | ✅ | 要小说专用、带状态的连载流程时选 Webnovel Writer；要宽泛的写作与排版技能集合时选 Baoyu Skills。 | 聚焦插件带来合同、索引与审查开销；通用技能包更轻，但不提供小说连续性系统。 |
| novelWriter | 未收录 | 必须使用跨平台、本地桌面编辑器时选 novelWriter；希望 Claude Code 主动规划、起草并核对连载时选本页项目。 | novelWriter 避开模型、提供商和插件耦合；Webnovel Writer 加入 agent 驱动的检索与审查。 |
| Manuskript | 未收录 | 想要独立大纲与写作应用时选 Manuskript；章节事实必须进入 agent 可读状态系统时选本页项目。 | Manuskript 保持桌面作者工作流；Webnovel Writer 依赖 Claude Code 与 Python 工具。 |

## 技术栈

- **核心：**Python 3.10 以上的 Claude Code 插件，包含 Skills、Agents、Hooks 和 Python CLI。
- **状态：**`.story-system` 合同与章节提交，配合 JSON、SQLite 索引、向量、摘要和记忆投影。
- **面板：**FastAPI、Uvicorn、Watchdog、SSE，以及随包提供的 React/Vite 前端。
- **检索：**BM25，加上通过 OpenAI 兼容端点提供的可选向量、rerank、混合和图混合路径。

## 依赖

- **必需：**Claude Code 插件运行环境和 Python 3.10 以上。
- **Python 包：**`aiohttp`、`filelock`、`pydantic`；面板额外使用 FastAPI、Uvicorn、HTTPX 和 Watchdog。
- **可选语义 RAG：**兼容的 embedding 与 rerank 服务，以及对应 API 凭据。没有 embedding key 时，文档说明会回退到 BM25。
- **仅前端开发：**Node.js/npm；日常使用时发布包已带构建后的面板资源。

## 运维难度

**中。**安装本身是 Claude Code Marketplace 插件加 Python 依赖，但一本实际书稿会持有合同、生成的 SQLite/JSON 状态、备份与可选外部 RAG 凭据。本地面板默认绑定 loopback，不过维护长篇书稿仍要有备份和升级纪律。

## 健康度与可持续性

- **维护快照（2026-07-13）：**未归档，且仍在活跃更新；`v6.2.1` 和默认分支均于 2026-07-07 更新。
- **治理与 bus factor：**GitHub contributor API 显示一位人类贡献者加自动化账号。项目自述为业余维护，因此单维护者中断是实质风险。[推断]
- **年龄与 Lindy：**创建于 2026-01，约六个月的历史不足以建立长期耐久性信号，即使早期关注度很高。
- **采用与风险：**约 5.6k stars、981 forks 只说明关注度，不能证明其连续性或规模宣称对特定书稿有效。GPL-3.0 是衍生分发时的决定性法律约束。

## 存疑（未验证）

- [未验证] “支持 200 万字体量连载”的说法来自项目描述；本次未发现独立压测或公开基准。
- [未验证] 当前发布说明中“774 个测试通过”的说法来自维护者，未在本地复跑。
- [未验证] 向量、rerank 和图混合检索的实际质量取决于所选外部服务和书稿；本次只从资料核对到 BM25 回退路径。
- [推断] 贡献者列表由一位作者主导且项目不足一年，因此为长篇书稿采用它时，fork 能力和本地备份比 star 数更重要。
