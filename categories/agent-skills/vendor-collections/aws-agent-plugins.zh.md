---
name: Agent Plugins for AWS
slug: aws-agent-plugins
repo: https://github.com/awslabs/agent-plugins
category: vendor-collections
tags: [agent-skills, aws, claude-code, plugin-marketplace, skill-pack]
language: Shell
license: Apache-2.0
maturity: v1.0.0 (2026-02), active, last pushed 2026-06 (~809 stars [未验证])
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-25T19:15:59Z
  default_branch: main
  default_branch_sha: 96a073a195491f2192c256ba66730b631ced03e1
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:51:44Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 8
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 28
        release_assets: 1
        release_tier: D
        signal_basis: releases
    longevity:
      grade: C
      raw:
        repo_age_days: 229
        last_commit_age_days: 8
        cohort: skill-pack
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 54
        top1_share: 0.214
        top3_share: 0.458
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
---

# Agent Plugins for AWS

AWS Labs 官方出品的插件集合，教 coding agent 如何在 AWS 上做架构、部署和运维——九个领域插件（serverless、Amplify、SageMaker、迁移、数据库、部署/成本估算等），从 Claude Code / Cursor / Codex 的 marketplace 安装。

![aws-agent-plugins — 健康度雷达](../../../assets/health/aws-agent-plugins.zh.svg)

## 何时使用

你是一名在 Claude Code（或 Cursor/Codex）里干活的开发者或平台工程师，手上的任务是 AWS 形状的：用 Lambda + API Gateway + Step Functions 搭一套 serverless API、为新架构估算成本并生成 IaC、把基础设施从 GCP 迁到 AWS、脚手架一个 Amplify 全栈应用、或者构建并部署 SageMaker 模型。基座 agent 大体懂 AWS，但总是抓着过时的服务默认值、跳过成本检查、或者手写出你还得返工修正的 CloudFormation。你想要的是 AWS 自己维护的 playbook——把各服务的最佳实践编码进去，并替你接好对应的 AWS MCP server（文档、定价、IaC）。

这个 repo 就是 vendor 源头：九个插件（`aws-serverless`、`aws-amplify`、`sagemaker-ai`、`migration-to-aws`、`databases-on-aws`、`deploy-on-aws`、`aws-transform`、`amazon-location-service`、`codebase-documentor-for-aws`）每一个都打包了触发短语驱动的 skill、MCP server 接线、以及 hooks/护栏。你添加 marketplace（`/plugin marketplace add awslabs/agent-plugins`），只装你需要的插件（如 `/plugin install deploy-on-aws@agent-plugins-for-aws`）；当 agent 识别到匹配的 AWS 任务时，skill 会按需加载。当你想把 AWS 自己的意见直接焊进 agent、而不是自己从零搭这套 skill 栈时，就用它。

## 何时不用

- **你已经有一套信得过的、精挑的 AWS skill/命令栈。** 这些插件自带触发短语和 MCP 接线；叠在既有方法论之上会导致同一个 AWS 任务上路由重叠、双重触发。每个关注点只保留一个事实源。
- **你不在受支持的 harness 上。** 安装路径是 Claude Code（≥2.1.29）、Cursor（≥2.5）、Codex（仓库本地 marketplace）；Kiro 是经第三方转换器的实验性支持。在不受支持的 agent 上没有 loader 来触发 skill，光有 markdown 不会自动激活。
- **vendor 在引导你转向——注意成熟度提示。** README 把更新的 **Agent Toolkit for AWS** 指为生产环境推荐路径，而本 repo「继续接受贡献」；把它当成仍在维护、但可能已被取代的产物，而非长期旗舰。[未验证]
- **你想要云中立或非 AWS 的指导。** 每个插件都是 AWS 生态风味（AWS MCP server、AWS 服务、AWS 定价），会主动把方案往 AWS 上偏——做多云或厂商中立架构时这不是你想要的。
- **你想要一个可运行的工具/CLI/库。** 没有任何东西可以 `import` 或独立运行——它是塑造 agent 行为的 skill 定义、MCP 配置和 hooks。脱离受支持的 agent（且没配好 AWS 凭证）它什么都不做。
- **是建议性的，不是强制的。** 行为活在 agent 加载的 markdown skill 里；「最佳实践」步骤是 prompt 级指令，不是硬保证——agent 仍可能偏离，或以 playbook 没料到的方式调用 AWS API。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Anthropic Skills](anthropic-skills.zh.md) | ✅ | 需要云中立、任务通用的一方 skill 时，选 Anthropic Skills。 | Anthropic 第一方的通用 skill（文档生成、前端、编写规范）。云中立、任务通用；本 AWS repo 更窄、锁定生态，但在 AWS 架构/部署/运维上深得多。价值单元不同。 |
| [Claude Plugins (official)](claude-plugins-official.zh.md) | ✅ | 需要 Anthropic 宽口径官方插件或 marketplace 目录时，选 Claude Plugins。 | Anthropic 宽口径的官方插件/marketplace 目录；通用。本 repo 是基于同一插件机制叠加的单 vendor（AWS）领域集合——按你要的是 AWS 深度还是通用插件集来选。 |
| [MiniMax skills](minimax-skills.zh.md) | ✅ | 需要另一家 vendor 的模型/媒体/多模态 skill 集合时，选 MiniMax skills。 | 另一家 vendor 的 skill 集合，绑定其模型/harness；有「官方起步 skill」的重叠目标但没有 AWS 领域内容。混用前先核对格式/loader 兼容性。 |
| AWS 官方 MCP server（独立） | 未收录 | 只需要底层 AWS MCP 数据源而不需要打包 skill/playbook 时，选 AWS 官方 MCP server。 | 底层的 AWS MCP server（文档、定价、IaC）不靠这些插件也能接；你能拿到数据源，但拿不到打包好的 skill、触发短语和护栏。更多组装、更少意见。 |
| 自己写 AWS skill | n/a | 需要最高贴合度且愿意自行维护 AWS playbook 和接线时，选自写 skill。 | 贴合度最高、不依赖 marketplace，但你放弃了 AWS 维护的 playbook 和 MCP 接线，得自己保持各服务最佳实践常新。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— [未验证] 最近一次 push 在 2026-06，未归档，open issue 很少（约 12 个）；v1.0.0 于 2026-02 打标签且活动截至 2026-06 是当前的，故**活跃维护**——并且在本 leaf 里独一份地发布了真正带版本号的 release，而非跟 `main`。
- **治理与背书** —— [推断] 组织所有，由 **AWS Labs** 背书——provenance 强，但单厂商且锁定 AWS 生态；路线图跟随 AWS 的优先级，而非中立基金会。
- **年龄与 Lindy** —— [推断] 创建于 2026-02，截至 2026-06 仅约 4 个月：**全新，尚无 Lindy 履历**。耐久性未经证实。
- **风险标记** —— [未验证] **厂商在引导转向**：README 把更新的「Agent Toolkit for AWS」指为生产推荐路径，而本 repo「继续接受贡献」——把它当作可能已被取代的产物，而非长期旗舰。约 809 star（2026-06）偏少，与其新近度一致。

## 存疑（未验证）

- [未验证] 最新 release 打标签 `1.0.0`（发布于 2026-02-18），仓库最后 push 于 2026-06-25；license 为 Apache-2.0、主语言为 Shell（据 2026-06-26 的 GitHub 元数据）——依赖某具体版本行为前请重新核验。主语言「Shell」反映的是工具脚本；skill 内容主要是 Markdown。
- [未验证] star 数（2026-06-26 的 GitHub 约 809）不可靠且对日期敏感；仅作参考，不是质量信号。
- [未验证] 九插件清单（amazon-location-service、aws-amplify、aws-serverless、aws-transform、codebase-documentor-for-aws、databases-on-aws、deploy-on-aws、migration-to-aws、sagemaker-ai）是 2026-06-26 对 `plugins/` 的快照；集合、触发短语和路由会在 `main` 上变化——请读实时目录。
- [未验证] 受支持 harness 清单及版本下限（Claude Code ≥2.1.29、Cursor ≥2.5、Codex 仓库本地、Kiro 经第三方转换器的实验性支持）以及 marketplace/安装标识（`agent-plugins-for-aws`，如 `deploy-on-aws@agent-plugins-for-aws`）均来自 README；确切名称与激活保真度可能变化——以当前文档为准。
- [未验证] README 据称推荐用更新的「Agent Toolkit for AWS」做生产用途，同时本 repo 继续接受贡献；确切的生命周期/弃用状态在此未独立确认。
- [未验证] 前置条件（已配置 AWS CLI/凭证、用于文档/定价/IaC 的 AWS MCP server）在 README 中有描述；实际所需权限范围、以及哪个插件需要哪个 MCP server，未逐插件验证。
- [推断] 因为行为活在 agent 加载的 markdown skill 里，强制力是建议性的——agent 可以偏离；「最佳实践」和护栏步骤是 prompt/hook 级指令，不是硬保证，且仍可能触发带成本/状态副作用的真实 AWS API 调用。
