---
name: Background Agents (Open-Inspect)
slug: background-agents
repo: https://github.com/ColeMurray/background-agents
category: orchestration-and-review
tags: [coding-agent, background-jobs, sandbox, cloudflare, github-app, multi-repo, automation]
language: TypeScript
license: MIT
maturity: v0.1.0 private workspace, active, 3354 stars, no GitHub Releases (as of 2026-10-13)
last_verified: 2026-10-13
type: app
upstream:
  pushed_at: 2026-10-13T16:39:16Z
  default_branch: main
  default_branch_sha: 31d199996e4cc33fcc1f80c08785820db2f05537
  archived: false
health:
  schema: 1
  computed_at: 2026-10-13T16:46:52Z
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 10.6
        qualifying_issues: 29
        band: relaxed_solo
        window_offset_days: 10
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 261
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 68
        top1_share: 0.741
        top3_share: 0.924
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
    adoption: { reason: no_package_structural }
---

# Background Agents (Open-Inspect)

同事合上电脑，交给编程助手的任务就停了；CI 作业又不能让其他人随时接着提问。Open-Inspect 把工作留在云沙箱，提供自托管的共享会话界面和集成触发入口。

![Background Agents — 健康度雷达](../../../../assets/health/background-agents.zh.svg)

## 何时使用

你运营的是一个可信工程组织：Linear 工单需要在请求人离线时继续修复，同事还得查看进度、追加要求，却不能接管他的终端。Open-Inspect 在后台运行沙箱会话，向协作者推送进度，提供网页、Slack、GitHub、Linear、定时任务和 webhook 入口。共享会话、每会话至多十个仓库和可复用的沙箱生命周期足以抵消独立控制面的成本时，才选它而不是本地编程 CLI。

只有能运维身份、GitHub App、模型凭据、沙箱提供商和单租户信任模型时才选它。主要部署指南使用 Cloudflare，也有 AWS 控制面的文档路径；它面向内部工程自动化，不是开箱即用的个人助手。

## 何时不用

- **你需要多租户 SaaS，或按个人 GitHub 权限授权。**改用逐组织独立部署或明确隔离租户的平台。Open-Inspect 已有团队、仓库授权和会话级 GitHub 凭据，但仍共享 App 安装、不比较个人 GitHub 权限，团队读取控制默认是 `shadow`，已签发令牌不能立即撤销。见所读版本的[安全模型](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/README.md#security-model-single-tenant-only)。
- **你是个人开发者，或只需终端结对编程。**改选 [OpenCode](../terminal-agents/opencode.zh.md)；Terraform、GitHub App、OAuth、云控制面和沙箱凭据的成本，对本地工作流不成比例。
- **你的政策禁止云沙箱提供商。**改用 OpenCode 这类本地 agent，或评估自管的 [OpenHands](openhands.zh.md)；文档中的沙箱路径使用 Modal、Daytona、Vercel Sandbox、OpenComputer 或 E2B。AWS 托管可去掉 Cloudflare 依赖，不能去掉沙箱提供商的运维责任。
- **你只需一个可审计的 CI 事件产生补丁。**改用 GitHub Actions 加 OpenCode；会话平台的凭据缓存、快照、secret 作用域、机器人和定时任务增加了需要管理的访问路径。
- **你需要有长期版本线和正式发布的生产平台。**改选更成熟的托管或自管方案；本项目较新，审查时没有 GitHub Releases，workspace 版本为 `0.1.0`。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [OpenCode](../terminal-agents/opencode.zh.md) | ✅ | 本地由开发者操作的 coding agent 选 OpenCode；可信团队的后台会话和集成足以证明云控制面成本合理时选 Open-Inspect。 | OpenCode 避开基础设施和共享凭据；Open-Inspect 加入沙箱调度、集成和多仓库自动化。 |
| [OpenHands](openhands.zh.md) | ✅ | 个人或小团队想从本地后端开始时选 OpenHands 的 Agent Canvas；组织级沙箱生命周期和可归属的后台工作足以证明单租户配置成本合理时选 Open-Inspect。 | Agent Canvas 从一台机器开始，再加远程和自动化后端；Open-Inspect 从云基础设施和共享 GitHub App 信任边界开始。 |
| GitHub Actions 加 agent CLI | 非仓库 | 窄而可审计的事件流足够时选 CI 触发的 agent 脚本；需要交互会话、实时协作和可复用沙箱生命周期时选 Open-Inspect。 | 这是组合模式，不是单个仓库；脚本的控制面更小，但会话界面与沙箱复用要自行实现。 |
| [CC Switch](cc-switch.zh.md) | ✅ | 一个人在桌面管理已安装 agent 时选 CC Switch；组织级云端执行与异步自动化时选 Open-Inspect。 | CC Switch 是低运维、本地工具；Open-Inspect 引入凭据、沙箱、数据平面运维和共享信任边界。 |

## 快速上手

按所读版本的[部署指南](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/docs/GETTING_STARTED.md)，准备 Node 24 以上、Terraform 1.14 以上和 Modal 的 Python 工具，fork 仓库，执行 `npm install`、`npm run build -w @open-inspect/shared`，在提供的 Terraform 文件中配置云账号和 GitHub App。在 `terraform/environments/production` 执行 `terraform init -backend-config=backend.tfvars`、`terraform apply`；这些命令创建会计费的云基础设施，不是本地演示。按照指南的 `npm run rbac:bootstrap-owner` 流程初始化工作区 Owner，创建团队、授予仓库、添加模型凭据，并在依赖团队私有读取前明确启用 `teams_enforcement = "on"`。网页中选择团队和仓库，输入编程任务，平台启动沙箱并推送助手的工作过程，也提供从会话创建拉取请求的功能。你承担托管、沙箱和模型费用，定义访问范围，并在合并前审查改动；启动成功或健康端点返回正常都不代表授权策略正确。

![background-agents — 主干用户故事](../../../../assets/flow/background-agents.zh.svg)

<!-- flow-steps:begin (generated from flows/background-agents.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：部署控制面，配置 GitHub App 和沙箱凭据 — `terraform apply`
2. **你**：创建团队，授予仓库并添加模型凭据
3. **你**：选择团队和仓库，在网页发送编程任务
4. **Background Agents (Open-Inspect)**：启动沙箱、检出仓库并派发提示词 — 组件：`控制面`
5. **Background Agents (Open-Inspect)**：向共享会话推送助手的工作进度 — 组件：`会话事件流`

**价值**：请求人离线后，编程工作仍在共享云会话继续

</details>
<!-- flow-steps:end -->

## 技术要点

- **先持久化，沙箱就绪再派发。**[`session/message-queue.ts:422–580`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/session/message-queue.ts#L422-L580) 检查模型提供商与执行器兼容性，在沙箱启动时延后派发，并把创建沙箱放到后台，避免机器人 HTTP 请求一直等待。它先认领已存储的提示词，再通过 WebSocket 发送；发送失败则恢复待处理状态并终止无响应沙箱。这是队列恢复机制，不代表任意工具副作用都恰好执行一次。
- **可回放的会话历史。**[`session/event-stream.ts:21–107`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/session/event-stream.ts#L21-L107) 用时间线游标读取事件仓库，排除心跳，限制回放与历史分页大小。客户端重新连接可恢复近期进度，不必让请求人的标签页一直开着；格式损坏的已存事件会被跳过，因此界面回放不保证审计导出的完整性。
- **签发凭据时重新解析仓库范围。**[`source-control/session-scope.ts`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/source-control/session-scope.ts) 重读会话归属和已存仓库成员；[`source-control/repository-scope.ts`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/source-control/repository-scope.ts) 解析数字 ID，并与当前团队授权取交集。身份缺失直接拒绝，不扩大范围。它收窄 GitHub 安装凭据，但缓存令牌与文件系统快照仍有独立的撤销边界，GitLab 仍使用部署级 PAT。

## 技术栈

- **控制面：**Cloudflare Workers、Durable Objects、D1、KV、R2、SQLite、WebSockets 上的 TypeScript。
- **Web：**Next.js 16、React 19、Tailwind CSS、Radix UI，依据 `packages/web/package.json`。
- **沙箱运行时：**OpenCode 或 Claude Agent 执行器、Node.js、Python、Bun、Git、GitHub CLI、`agent-browser`、无头 Chromium。
- **基础设施：**Terraform，以及 Modal、Daytona、Vercel Sandbox、OpenComputer、E2B 集成；部分沙箱配置用 Python。`docs/AWS_BRING_UP.md` 还描述 EC2 上的 Node 控制面，使用 Docker Compose、EBS、S3、Caddy 而非 Cloudflare。

## 依赖

- **部署核心：**Node.js 24 以上（`package.json` 的 engines）、npm、Terraform 1.14 以上；Cloudflare 路径另外要求 Wrangler、Cloudflare 凭据，以及 Modal 所需的 Python 3.12 以上和 uv。AWS 路径则要求 AWS CLI、Session Manager 和对应账号。
- **源码管理：**GitHub App/OAuth 配置，并刻意收窄安装范围。
- **沙箱：**一个支持的沙箱提供商及其凭据、资源。
- **模型与集成：**为所选模型和执行器配置凭据；指南中关闭机器人的核心路径并不强制要求 Anthropic API key。可选的 Slack、Linear 分类器、Google 登录、Sentry、webhook 需要额外凭据；订阅路径仍需提供商登录与资格。

## 运维难度

**高。**这是含身份、GitHub 安装凭据、secrets 注入、worker 状态、云沙箱、webhook 和仓库生命周期脚本的分布式控制面。README 自己把部署限制为一个可信租户；安全运行意味着收窄 GitHub App 范围、入口、secret 范围和自动化权限。

## 健康度与可持续性

- **维护快照（2026-10-13）：**未归档，默认分支提交 `31d1999` 来自当天；GitHub 显示 3354 stars，但 stars 不是安装量。工作区版本仍为 `0.1.0`，没有 GitHub Releases。
- **治理与 bus factor：**仓库由个人账号拥有，贡献活动高度集中于 ColeMurray。项目正在活跃开发，但关键维护者风险实质存在。[推断]
- **年龄与 Lindy：**创建于 2026-01，且没有 GitHub Releases，因此尚无长期运维史或稳定发布线信号。
- **实测覆盖：**综合 B 覆盖 5/6 轴。采用量仍是 `? / no_package_structural`；根工作区为私有包，评分器未找到规范包或安装信号。这表示未测到，不表示没有用户，也不是许可证豁免。
- **安全与运维风险：**团队授权与会话级凭据不会把可信单租户产品变成多租户 SaaS。团队读取控制默认 `shadow`，快照可能保留凭据，都要求明确的部署审查。

## 存疑（未验证）

- [未验证：未部署云基础设施] 沙箱后端、AWS、Cloudflare 部署与订阅登录只核过源码，没有独立运行或安全审计。
- [推断：依据是共享安装、shadow 默认与快照凭据边界] 应从受限内部试点开始，而非开放大量仓库访问权；源码阅读不能证明生产隔离性。
