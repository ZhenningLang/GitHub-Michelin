---
name: Funtool
slug: funtool
repo: https://github.com/cixingguangming55555/wechat-bot
category: api-gateway
tags: [claude-code, nvidia, llm-proxy, windows, binary-only]
language: JavaScript
license: MIT
maturity: binary-only current artifacts, 2.5k stars (as of 2026-07)
last_verified: 2026-07-17
type: tool
upstream:
  pushed_at: 2026-02-09T06:38:04Z
  default_branch: master
  default_branch_sha: 2afcb9d8d527a49cf684f9ba33853f23aa722e7b
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:58:36Z
  overall: C
  overall_score: 1.8
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
        last_commit_age_days: 225
        active_weeks_13: 0
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
        repo_age_days: 2409
        last_commit_age_days: 225
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
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
---

# Funtool

一个面向 Windows 的 Claude Code 与 NVIDIA 模型代理工具；尽管仓库名是 `wechat-bot`，当前用途并不是微信机器人，而且当前代理产物是不可审计的可执行文件。

![Funtool — 健康度雷达](../../assets/health/funtool.zh.svg)

## 何时使用

你是 Windows 开发者，想让 Claude Code 走 Funtool 文档指定的 NVIDIA 模型通道，并且更看重拿到一个预打包可执行文件，而不是自己组装代理栈。你能把它限制在一次性或低信任工作站中，接受当前实现无法从源码审计，同时外部微信公众号文档所描述的流程正好符合你的任务。

只有“Windows + Claude Code + NVIDIA”这条精确路径是决定条件时，才在 LiteLLM 或 claude-code-router 之上选择 Funtool。如果源码可审计、跨平台部署、团队治理或供应商广度更重要，应选择下方替代品。

## 何时不用

- **你必须审计代理、锁定依赖或从源码重建。** 改用 LiteLLM；Funtool 当前核心是不可见源码的 EXE，仓库没有提供代码评审或可复现构建所需的实现。
- **你需要由文本配置控制的跨平台 Claude Code 路由层。** 改用 claude-code-router；Funtool 绑定 Windows 二进制和仓库外的操作文档。
- **你需要把多个 CLI 凭据统一暴露为 OpenAI 兼容 API。** 改用 CLIProxyAPI；Funtool 聚焦文档指定的 Claude Code 与 NVIDIA 通道，不是通用 CLI 账号网关。
- **你需要多用户管理、额度、渠道配置或共享 Web 控制面。** 改用 New API；Funtool 是本地二进制工作流，不是有团队治理能力的网关。
- **你只想从桌面界面切换 coding agent 的供应商和凭据。** 改用 [CC Switch](../agent-frameworks/coding-agents/orchestration-and-review/cc-switch.zh.md)；它管理 agent 配置，而 Funtool 会把模型代理可执行文件放进请求链路。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [LiteLLM](litellm.zh.md) | 已收录 | 需要可审查、供应商无关的团队代理时，选 LiteLLM；只有预打包 Windows NVIDIA 通道比源码访问更重要时，才选 Funtool。 | LiteLLM 增加 Python 部署与配置工作，但公开网关逻辑并覆盖更多供应商；Funtool 降低窄场景的启动成本，代价是信任二进制。 |
| [claude-code-router](claude-code-router.zh.md) | 已收录 | 需要跨平台、配置驱动的 Claude Code 路由时，选 claude-code-router；只有外部文档描述的 Windows 二进制流程完全命中任务时，才选 Funtool。 | claude-code-router 更容易审查和自动化；Funtool 打包了更多目标流程，却无法从已发布仓库独立重建。 |
| [CLIProxyAPI](cliproxyapi.zh.md) | 已收录 | 需要把多个 CLI 账号变成可复用 API 门面时，选 CLIProxyAPI；任务明确是让 Claude Code 访问其支持的 NVIDIA 通道时，才选 Funtool。 | CLIProxyAPI 解决更宽的账号转 API 问题，也带来更多服务配置；Funtool 更窄，并偏桌面使用。 |
| New API | 未收录 | 需要用户、额度、渠道和管理控制的共享网关时，选 New API；只做单机 Windows 配置且不需要治理时，才考虑 Funtool。 | New API 的服务与数据库运维面更大，但提供团队控制；Funtool 表面基础设施更少，运作透明度也低得多。 |
| [CC Switch](../agent-frameworks/coding-agents/orchestration-and-review/cc-switch.zh.md) | 已收录 | 需要可视化切换 coding agent 供应商和凭据时，选 CC Switch；请求必须经过 Funtool 的 NVIDIA 代理路径时，才选 Funtool。 | CC Switch 是配置管理器，不是 API 网关；Funtool 改变请求路由，却把不可审计 EXE 引入信任边界。 |

## 技术栈

- **仓库元数据：** GitHub 将主要语言标为 JavaScript，但当前可用版本以可执行文件分发，没有对应的可审查源码。
- **当前产品面：** 面向 Windows，把 Claude Code 请求路由到文档指定的 NVIDIA 模型通道；尽管仓库名如此，它目前不是微信机器人。
- **分发方式：** GitHub 报告仓库约 932 MiB，主要反映长期累积的二进制历史。`funtool/` 中两份当前 NVIDIA 代理 EXE 约为 4.9 MiB 与 8.3 MiB，其实现无法从仓库检查。
- **文档：** 操作说明位于仓库外的微信公众号内容中，可执行文件、文档和版本历史分散在不同载体。

## 依赖

- 能运行所分发 EXE 的受支持 Windows 环境。
- Claude Code，以及目标 NVIDIA 模型服务所需的访问凭据或账号配置。
- 访问模型端点和外部配置文档的网络连接。
- 对预构建发布产物的信任；仓库没有提供可替代该产物的当前核心源码和本地审查构建路径。

## 运维难度

**启动低，可信运维高。** 预打包 Windows 可执行文件可以减少首次配置，但运维负担会转移到产物来源、端点与凭据处理、外部文档的版本匹配，以及没有源码时的故障定位。约 932 MiB 的仓库历史也使 clone 与归档比小型源码代理更重，不过当前两份代理 EXE 本身小得多。应把它限制为窄信任边界内的工作站工具，不要把它当作透明的共享基础设施。

## 健康度与可持续性

- **产物姿态，截至 2026-07：** 该仓库没有 GitHub Releases；可用代理产物直接提交在默认分支。后续运行依赖上游继续发布兼容的 Windows 二进制，而不是用户自行构建或维护代码。
- **采用信号：** 截至 2026-07 约有 2.5k 个 GitHub star，说明项目获得关注，但 star 不能回答可审计性、许可证或发布来源问题。
- **许可证风险：** GitHub 将仓库根许可证识别为 MIT；该授权是否有意覆盖当前不透明 EXE，无法从源码、构建元数据或独立二进制声明确认。
- **Lindy 与治理：** 现有发布面不足以确认项目年龄、持续发版记录和维护者冗余。[推断] 即使当前流程方便，只分发二进制也使它不适合作为长期共享基础设施的耐久押注。

## 存疑（未验证）

- [未验证] 仓库中的 MIT 文本可能不覆盖当前不透明 EXE；再分发或商业依赖前，应取得上游明确说明。
- [未验证] 当前 EXE 对应的源码不可用于审计，因此无法从仓库独立核验其内置依赖、凭据处理、遥测和更新行为。
- [未验证] 微信公众号文档与仓库内二进制产物分别维护；本文无法确认说明内容与当前 EXE 是否精确匹配。
- [推断] 一个约 932 MiB、累积多份不透明二进制的仓库，比小型源码构建代理带来更高的 clone、供应链和故障响应负担，但本页没有执行二进制分析。
