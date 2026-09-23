---
name: Pezzo
slug: pezzo
repo: https://github.com/pezzolabs/pezzo
category: llm-eval
tags: [llmops, prompt-management, observability, prompt-versioning, self-hosted, typescript]
language: TypeScript
license: Apache-2.0
maturity: v0.9.2, likely stalled (last real commit ~2025-06), ~3.2k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2026-03-31T02:03:01Z
  default_branch: main
  default_branch_sha: 886d38b50bd7d8af723eb12e7d815e1e2b625c87
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:27:13Z
  overall: C
  overall_score: 2.4
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 32
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: "@pezzo/client"
        dependent_repos_count: 1
        downloads_last_month: 1879
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 1249
        last_commit_age_days: 32
        cohort: app
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
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# Pezzo

一个开源、可自托管的 LLMOps 平台，做 prompt 管理、版本化、可观测性和成本/延迟监控——一个集中编写 prompt 并观察它们在生产中表现的地方。

![pezzo — 健康度雷达](../../assets/health/pezzo.zh.svg)

## 何时使用

你是某个小型产品团队的开发，团队刚开始发 LLM 功能，而你的 prompt 以内联字符串散落在代码各处——没人知道哪个版本在线、你看不到一次调用花了多少钱或耗时多久，改一个 prompt 就要重新部署。你自托管 Pezzo（Docker Compose：Postgres + ClickHouse + Redis），把 prompt 搬进它的 UI，在那里它们被版本化、可不改代码就编辑，并用 Node 或 Python SDK 给应用埋点。现在每个 LLM 请求都被追踪——prompt 版本、token、成本、延迟、错误——汇在一个可观测性看板里，你可以从 UI 把一个 prompt 向前或回滚，缓存还能削减重复调用的花费。它面向那些想要一个自托管的 prompt + 监控统一控制面、而不愿把 prompt 注册表、追踪工具和成本看板分别拼起来的团队。

## 何时不用

- **这个项目看起来已停滞——别把新栈押在它上面。** 它最后一次实质提交似乎在约 2025 年中；对一个年轻的 VC 背书创业仓库而言，这是严重的废弃风险。采用前请核实当前活跃度，并假设你可能最终要自己维护它。[推断]
- **你想要托管服务。** Pezzo 曾提供托管的“Pezzo Cloud”，但对一个公司走向不确定的 OSS 项目，自托管才是稳妥假设——别指望云端层会一直存在。[推断]
- **你需要重量级的 eval / 实验平台。** Pezzo 以 prompt 管理 + 可观测性为中心；严谨的离线 eval、数据集驱动打分和 A/B 实验在为此而生的工具里更强（LangSmith、Langfuse、Helicone）。
- **你不想跑三个数据存储。** 自托管需要 Postgres、ClickHouse 和 Redis——对小团队来说是不轻的基础设施，相比托管替代品。
- **你需要广泛、最新的 SDK/提供方覆盖。** SDK 当时是 Node/Python，部分集成在进行中；在一个停滞项目上，预期会有缺口和无人维护的提供方支持。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Langfuse](langfuse.zh.md) | ✅ | 新建开源 LLM 可观测性、prompt 管理和 eval 平台时，选 Langfuse；只有已有 Pezzo 自托管栈且愿意自己接手维护时，才保留 Pezzo。 | 开源的 LLM 可观测性 + prompt 管理 + eval，维护活跃、社区强；大体上是当下 Pezzo 这一生态位更健康的接棒者。 |
| Helicone | 未收录 | 当日志、成本追踪、缓存和代理式接入是主需求时，选 Helicone；只有 Pezzo 的 prompt 版本 UI 已经契合且能接受停滞风险时，才保留 Pezzo。 | 开源的 LLM 可观测性/代理，聚焦日志、成本和缓存；采用更轻（基于代理），prompt 管理叙事更窄。 |
| LangSmith（LangChain） | 未收录 | 当托管追踪、eval、prompt hub 和 LangChain 集成比自托管 OSS 更重要时，选 LangSmith；只有不能用 SaaS 且能自维护时，才保留 Pezzo。 | 托管的追踪 + eval + prompt hub，深度集成 LangChain；托管且功能丰富，但闭源/SaaS，不能自托管 OSS。 |
| PromptLayer | 未收录 | 当你要托管的 prompt 注册表和请求日志时，选 PromptLayer；只有明确需要自托管 prompt 管理且接受疑似停滞代码库时，才保留 Pezzo。 | prompt 注册表 + 请求日志；prompt 管理范围有重叠，托管为先。 |

## 技术栈

- **语言：** TypeScript（主），另有 Python SDK。
- **后端：** Node.js（NestJS 风格的服务）；一个 GraphQL API（提及 GraphQL codegen 工具链）。
- **前端：** React Web 控制台。
- **数据存储：** PostgreSQL（核心数据）、ClickHouse（高吞吐请求/遥测数据）、Redis（缓存/队列）。
- **部署：** 本地/自托管用 Docker Compose；提供 Node 和 Python SDK。

## 依赖

- **数据存储（你来跑）：** PostgreSQL + ClickHouse + Redis——三个服务，通常经提供的 Docker Compose。
- **运行时：** 平台需要 Node.js 18+；自托管路径需要容器运行时（Docker）。
- **LLM 提供方：** 你自己的提供方/API key；Pezzo 封装/观测这些调用（具体提供方覆盖未经验证，且在停滞项目上无人维护）。
- **SDK：** 嵌入你应用的 Node 或 Python SDK，用于采集追踪并取 prompt 版本。

## 运维难度

**中到高。** 第一天经 Docker Compose 部署还算可上手，但你运维的是一个有状态的多服务应用：Postgres + ClickHouse + Redis 要备份、升级和监控，外加 API/控制台。ClickHouse 尤其是要在有量时跑好的真基础设施。更大的运维风险是项目疑似停滞（见健康度）：在一个无人维护的代码库上，你要自己接手安全补丁、依赖升级和 bug 修复，这把“中等”的部署投入变成一个无限期的维护承诺。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** **疑似停滞。** GitHub 的 `pushed_at` 显示 2026-03，但默认分支上最后一次*实质提交*似乎在约 2025-06——大约一年无活动。最新 release v0.9.2（1.0 前）。未归档，但节奏看起来是死了，而非吃老本。[推断]
- **治理 / 背书。** 一个 VC 风格的创业项目（pezzolabs / pezzo.ai），核心团队很小。单一公司主导加疑似停摆是高 bus-factor 风险——若公司转向或收缩，OSS 仓库和任何云端层都有风险。[推断]
- **年龄与 Lindy 判断。** 2023-04 创建，约 3 年但**疑似已不再活跃**——这**通不过 Lindy**：年龄只在仍活跃时才算数，而停滞项目趋向废弃而非耐久。[推断]
- **采用度。** 约 3.2k star / 约 276 fork 反映了真实的早期兴趣，但停滞仓库意味着社区和生态很可能正漂向维护活跃的替代品（Langfuse、Helicone）。[未验证]
- **风险标记。** Apache-2.0（许可干净，未发现 relicense）。主导标记是**不活跃/废弃风险**与**单一创业公司依赖**——除非你准备好 fork 并自己接管，否则两者都指向选一个维护中的替代品。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 3.2k star / 约 276 fork、版本 v0.9.2；计数对时间敏感。
- [推断] “疑似停滞 / 约一年无活动”是从 GitHub `pushed_at`（2026-03）与默认分支最后一次实质提交（约 2025-06-28）之间的不一致推断的——`pushed_at` 可能被分支/tag 活动顶高而无实质改动。依赖该项目前请确认当前提交历史。
- [推断] NestJS 后端、React 前端和 GraphQL API 是从 README/工具链引用推断的，未在此通过读源码布局确认。
- [未验证] 支持的 LLM 提供方与确切的 SDK/集成覆盖在所查材料中未详述——若重要请对照仓库核实。
- [推断] 鉴于公司疑似不活跃，Pezzo Cloud 托管层的当前状态不确定；请把云端选项视为不保证会持续。
