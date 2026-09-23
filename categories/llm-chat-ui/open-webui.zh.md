---
name: Open WebUI
slug: open-webui
repo: https://github.com/open-webui/open-webui
category: llm-chat-ui
tags: [self-hosted, ai-chat, ollama, rag, openai, mcp]
language: Python
license: NOASSERTION
maturity: v0.x, active, 144k stars (as of 2026-07)
last_verified: 2026-07-01
type: app
upstream:
  pushed_at: 2026-07-02T17:38:23Z
  default_branch: main
  default_branch_sha: ecd48e2f718220a6400ecf49eafd4867a38feb10
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:26:18Z
  overall: B
  overall_score: 3.2
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
      grade: A
      raw:
        median_ttfr_hours: 0.0
        qualifying_issues: 12
        band: relaxed_solo
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: open-webui
        dependent_repos_count: 0
        downloads_last_month: 1340107
        graph_tier: E
        volume_tier: B
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 1082
        last_commit_age_days: 1
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 144
        top1_share: 0.655
        top3_share: 0.865
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Open WebUI

一款可扩展、功能丰富、用户友好的自托管 AI 平台，可完全离线运行，支持 Ollama、OpenAI 兼容 API 及内置 RAG。

![Open WebUI — 健康度雷达](../../assets/health/open-webui.zh.svg)

## 何时使用

你是一位注重隐私的开发者或小团队，想为本地与远程大模型搭建一个自托管聊天界面。你选择 Open WebUI 而不是 ChatGPT 或 Claude 网页版等专有云服务，是因为它让你的数据留在自己的硬件上，支持离线运行，且除基础设施外无额外成本。你选择它而不是 [NextChat](nextchat.zh.md)，是因为你需要文档上传做 RAG、内置推理引擎和更丰富的开箱功能；NextChat 更轻、部署更快，但缺乏 RAG 和许多高级功能。你选择它而不是 LibreChat，是因为你想要更简单、离线优先的部署，无需处理可能增加运维复杂度的插件生态。你用 Docker 运行它，连接 Ollama 做本地模型或 OpenAI 兼容 API 做远程模型，即可获得一个精致的 Web UI，支持对话历史、社区扩展性，且没有第三方数据泄露风险。

## 何时不用

- **如果你需要高级 RBAC、团队配额和管理治理**——请用 [HiveChat](../team-chat/hivechat.zh.md) 或 Dify 等平台而不是 Open WebUI，因为 Open WebUI 默认偏单用户，缺乏成熟的团队管理功能。
- **如果你希望零运维负担**——请直接用 ChatGPT、Claude 网页版或托管 API 而不是 Open WebUI，因为 Open WebUI 需要运行并维护 Docker 容器、管理模型文件并持续更新应用。
- **如果你需要企业 SSO、审计追踪和 SLA 保障**——请用 Azure OpenAI、Dify Enterprise 或托管 LLM 服务等商业平台而不是 Open WebUI，因为 Open WebUI 缺乏企业级管理后台、合规认证和 SLA 支持。
- **如果你需要原生移动应用体验**——请用 ChatGPT 或 Claude 的移动 App 而不是 Open WebUI，因为 Open WebUI 基于 Web，没有提供原生移动应用及其通知和离线缓存能力。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [NextChat](nextchat.zh.md) | ✅ | 轻量、可自部署的聊天前端。 | NextChat 更轻、部署更快；Open WebUI 更重，但内置 RAG 且功能更多。 |
| [HiveChat](../team-chat/hivechat.zh.md) | ✅ | 管理员统管的团队聊天，带配额。 | HiveChat 面向 RBAC 团队管理；Open WebUI 面向个人 / 小团体使用。 |
| [LibreChat](librechat.zh.md) | ✅ | 另一款自托管聊天前端。 | LibreChat 插件生态更广，但尚未收录。 |
| Lobe Chat | 未收录 | 设计优先的聊天前端。 | Lobe Chat 强调视觉精致与插件市场；Open WebUI 强调离线运行。 |
| ChatGPT / Claude 网页版 | 未收录 | 闭源云端聊天。 | 专有且需联网；Open WebUI 可自托管、支持离线。 |

## 技术栈

- **Python**——后端与 API 层
- **SvelteKit**——前端框架
- **Docker**——主要部署方式
- **Ollama**——本地大模型运行时集成

## 依赖

- Docker 运行时用于部署
- Ollama（用于本地模型）或 OpenAI 兼容 API key（用于远程模型）
- 托管应用的设备或服务器
- 可选：向量数据库用于 RAG 文档摄入

## 运维难度

**低到中等**。单个 Docker 容器承载核心应用。主要负担是保持 Ollama 模型文件更新（大体积下载）以及管理 RAG 文档上传。对单用户来说简单；对小团队来说，可能需要配置认证并管理资源使用。

## 健康度与可持续性
- **维护活跃度**：Grade A——最近 13 周中 13 周有提交；最后提交距今 1 天。
- **响应速度**：Grade A——中位首次响应时间 0.0 小时，基于 12 个 qualifying issues/PRs。
- **采用广度**：Grade B——pypi.org 上月下载量 1,340,107（包名：open-webui）。
- **长青度**：Grade B——仓库已创建 1082 天。
- **治理集中度**：Grade C——前三贡献者占比 86.5%（?）。
- **许可风险**：无法计算——unknown。
## 存疑（未验证）

- [未验证] GitHub API 返回的许可为 `NOASSERTION`，商用前必须核实实际许可条款。
- [未验证] 开源版与潜在付费版的企业功能及可用性尚未确认。
- [推断] 约 3 年的仓库拥有 144k star，可能包含大量炒作驱动的增长；请在目标环境中验证生产级采用情况。
