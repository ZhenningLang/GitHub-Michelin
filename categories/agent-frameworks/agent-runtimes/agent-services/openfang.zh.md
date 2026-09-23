---
name: OpenFang
slug: openfang
repo: https://github.com/RightNow-AI/openfang
category: agent-services
tags: [autonomous-agents, agent-os, rust, mcp, scheduler, channels, self-hosted]
language: Rust
license: Apache-2.0 OR MIT
maturity: v0.6.9, pre-1.0, active (2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-25T08:13:28Z
  default_branch: main
  default_branch_sha: acf2587e46be174c10200489c9a2d23a39a98aeb
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:32:12Z
  overall: C
  overall_score: 2.2
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
        last_commit_age_days: 133
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 87084
        release_assets: 2262
        release_tier: D
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 210
        last_commit_age_days: 133
        cohort: framework
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 64
        top1_share: 0.582
        top3_share: 0.653
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

# OpenFang

一个用 Rust 写的“智能体操作系统”，以单个自包含二进制交付：它让自治智能体（"Hands"）按计划运行——7×24、无需你逐次提示——内置 kernel、调度器、WASM 工具沙箱、MCP 支持，以及 40 个消息渠道适配器。

![openfang — 健康度雷达](../../../../assets/health/openfang.zh.svg)

## 何时使用

你是单干的创始人或小型运维团队，想要一个“按定时器干活”的智能体，而不是一个要你在对话框里盯着喂的。比如：每天早上抓取线索并按你的 ICP 打分、对竞品跑一轮 OSINT 变更检测、起草并定时发布 X/Twitter 内容，或让研究智能体交叉比对多源资料、给你一份带引用的简报——全部在你掌控的机器上无人值守运行。你不想把一个 Python 框架、一个 cron 守护进程、一个队列、一个仪表盘、再加上每个渠道的 webhook 胶水拼在一起；你想要一个进程，里面已经备好调度器、持久化、渠道适配器和护栏。OpenFang 用“操作系统”而非“库”的形态解决这件事：你 `openfang init`、放入一个 Hand（一份 `HAND.toml` 清单 + 系统提示 + skill 文档 + 审批门），它就按计划运行，通过 Telegram/Discord/Slack/WhatsApp 跟你对话，并把每个动作记入防篡改的审计链。

当你在意体积和自托管时它也合适。整套就是一个约 32 MB 的 Rust 二进制、空闲内存很低，所以放在小 VPS 或 homelab 机器上是可行的——换成笨重的 Python 智能体栈就会觉得不对劲；WASM 沙箱加上基于能力（capability）的访问控制，也给“让智能体去碰开放网络和你的账号”提供了一套安全说法。如果你正从 OpenClaw 迁移，OpenFang 明确在拉拢这部分人，提供迁移路径。[推断]

## 何时不用

- **你要的是会话式、在环路内的编排库，而不是一个 OS。** 如果你在自己的应用里搭一个请求/响应式智能体、需要对 LLM 调用图做细粒度控制，那么 [DSPy](../../workflow-builders/dspy.zh.md)、LangGraph 或 [AgentScope](../agent-sdks/agentscope.zh.md) 这类库更贴合——OpenFang 自己占有运行时、调度器和进程模型，正好是“嵌进我的服务里”的反面。
- **你需要成熟、API 稳定的底座。** 它明确处于 pre-1.0:README 警告会有粗糙之处、minor 版本之间会破坏兼容，生产环境请 pin 到具体 commit。今天就把业务关键管线建在它上面，意味着要承受频繁变动。
- **单厂商、年轻项目风险。** 2026-02 创建，由一家公司（RightNow）主导；一个约 4 个月、单组织的项目带有弃坑和方向骤变的风险，这是多维护者基金会项目没有的。[推断]
- **你不信它的跑分/特性叙事。** README 以自跑对比开场（冷启动、空闲内存、“16 个安全系统”、“唯一带渠道适配器的”）。这些都是第一方、未经审计的——别在没有自测的情况下据此选型。[未验证]
- **你需要团队能扩展的语言/运行时。** 它从头到尾是 Rust；如果团队里没人写 Rust，那么在内置 Hand 之外（而非仅做配置）自己写新工具/Hand 的成本会很高。
- **合规/数据驻留，或规模化多租户 SaaS。** 它面向自托管的单运营者/小团队自治、基于 SQLite 的本地持久化；它不是托管的、横向扩展的多租户控制面。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [DSPy](../../workflow-builders/dspy.zh.md) | ✅ | 需要用于“编程”和优化 LLM 管线的 Python 框架时，选 DSPy。 | 一个用于“编程”（并优化）LLM 管线的 Python 框架；你把它嵌进自己的应用。OpenFang 是反过来的：一个自己掌管调度与执行的自治运行时/OS，而非你去调用的库。 |
| [AgentScope](../agent-sdks/agentscope.zh.md) | ✅ | 需要面向开发者、显式控制多智能体应用的框架时，选 AgentScope。 | 面向开发者、用显式控制构建/编排多智能体应用的框架；OpenFang 用这份控制权，换来一个内置渠道与护栏、按计划驱动、开箱即用的 OS。 |
| [Symphony](symphony.zh.md) | ✅ | 需要由跟踪器驱动 coding-agent 编排的同类框架时，选 Symphony。 | 本类目同门；编排哲学不同——选智能体框架时可直接对比。 |
| [claude-octopus](../../coding-agents/orchestration-and-review/claude-octopus.zh.md) | ✅ | 需要更窄的 Claude-centric 同类项目时，选 claude-octopus。 | 同门；更窄的、以 Claude 为中心的工具，对比 OpenFang 那套覆盖广的 27 provider、OS 形态的范围。 |
| [LangGraph](../agent-sdks/langgraph.zh.md) | ✅ | 需要在自有服务里构建有状态、交互式智能体图时，选 LangGraph。 | 在你自己服务里做有状态、交互式智能体图的 Python 默认选择；无内置调度器/渠道/二进制分发。OpenFang 把这一切反转成独立 OS。 |
| [OpenClaw](../personal-assistants/openclaw.zh.md) | ✅ | 需要 OpenFang 给自己设的对标对象及迁移来源时，选 OpenClaw。 | OpenFang 给自己设的对标对象，并提供从它迁移的路径；OpenFang 声称体积更小、有 OS 叙事。请自行核实该对比。 |
| [CrewAI](../agent-sdks/crewai.zh.md) / [AutoGen](../agent-sdks/autogen.zh.md) | ✅ | 需要面向角色/会话的 Python 多智能体框架来做应用内工作流时，选 CrewAI 或 AutoGen。 | 面向角色/会话的多智能体 Python 框架，用于应用内工作流；不是单二进制自治运行时。 |

## 技术栈

- **语言：** Rust（主语言，按字节约 91%），仪表盘用 HTML/JS/CSS，桌面端用 Tauri 2.0；另有少量 Python/Shell/PowerShell 安装脚本。
- **结构：** 一个约 14 crate 的 Cargo workspace——kernel（编排/调度/RBAC）、runtime（智能体循环、LLM 驱动、工具、WASM 沙箱、MCP）、api（REST/WS/SSE,OpenAI 兼容）、channels、memory、wire（P2P 协议）、CLI、desktop、migrate（crate 数/LOC 依 README）。
- **数据存储：** SQLite 持久化，加用于记忆的向量嵌入。
- **沙箱/安全：** WASM 工具沙箱、基于能力的访问控制、Merkle 哈希链审计、Ed25519 签名、提示注入扫描、SSRF 防护。
- **LLM/MCP:** 支持 Model Context Protocol；众多 provider 驱动（Anthropic、OpenAI、Gemini、Groq、DeepSeek、Ollama、vLLM 等——README 称 27 provider / 123+ 模型）。
- **渠道：** 约 40 个消息适配器（Telegram、Discord、Slack、WhatsApp 经 QR 网关、Signal、Matrix、Email、Teams 等）。

## 依赖

- **运行时：** 单个自包含二进制（README 称约 32 MB）；启动无需外部服务。通过 `curl … | sh`（macOS/Linux）或 PowerShell（Windows）安装。
- **可选：** 仅 WhatsApp Web（QR）网关需要 Node.js ≥ 18，该网关默认监听 3009 端口；仪表盘默认 4200 端口。
- **从源码构建：** 需要较新的 Rust 工具链 / Cargo（workspace 很大，全量构建并不轻量）。
- **外部：** 你路由到的 LLM provider 的 API key；本地模型则需 Ollama/vLLM 端点。

## 运维难度

**跑起来低，认真运营则中。** 顺路径确实很轻：一个二进制，`openfang init` / `openfang start`，一个本地仪表盘——更像跑一个 CLI 守护进程，而非部署 Python ML 栈，小体积也适合 VPS 或 homelab。一旦它开始干真活，难度就上来：你现在要为一个无人值守、对着真实账号和开放网络行动的智能体负责，因此必须配置审批门、收敛能力范围、管理密钥/API key、盯审计日志——再加上 pre-1.0 状态，升级时要 pin 到已知良好的 commit 并预留破坏性变更的成本。从源码构建或自己写新的 Rust 工具/Hand，对非 Rust 团队会推向**高**。

## 健康度与可持续性

- **响应速度**：无法计算——unknown。
- **维护——活跃，pre-1.0（截至 2026-06）。** 最后推送 2026-06；最新发布 v0.6.9（2026-05，针对 RUSTSEC 公告的安全补丁）；未归档。在被积极开发，但明确处于 pre-1.0，minor 版本之间要预期破坏性变更。
- **治理与背书——单一厂商。** 由一家公司（RightNow / `RightNow-AI`）主导，而非基金会或多组织社区；路线图与延续性都系于该厂商。单厂商的 pre-1.0 项目带有方向骤变与弃坑风险，这是基金会项目所没有的。
- **年龄与 Lindy——非常年轻、未经证明。** 2026-02 创建，约 4 个月（截至 2026-06）。无历史沉淀；牢牢属于「年轻且被热捧」，而非 Lindy 安全——别在没承受 churn 准备的情况下把业务关键管线押在它上面。
- **风险信号——第一方跑分 + 年轻单厂商。** 所有招牌数字（冷启动、内存、「27 provider / 40 渠道」、LOC）都是未经审计的 README 口径；许可为双授权 MIT OR Apache-2.0（无重许可历史）。主导风险是年轻 + 单厂商集中，而非许可。

## 存疑（未验证）

- [未验证] 截至 2026-06 star 约 17.9k——智能体框架领域的 GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 所有跑分数字（冷启动约 180 ms、空闲内存约 40 MB、安装体积约 32 MB）以及“16 个安全系统 / 40 渠道 / 27 provider / 123+ 模型 / 14 crate / 137k LOC / 1,767+ 测试”均为 README 第一方数据，未经独立审计。
- [未验证] “唯一带消息渠道适配器的框架”以及与 LangGraph/CrewAI/AutoGen/OpenClaw 的延迟/内存对照都是项目自己的叙事；未找到第三方验证。
- [推断] 许可证为双授权 MIT OR Apache-2.0（仓库里 LICENSE-MIT 与 LICENSE-APACHE 并存；GitHub API 只暴露 Apache-2.0）——请确认条款对你的用途可接受。
- [推断] 单厂商（RightNow）,2026-02 创建；对这么年轻的项目，维护广度与长期方向尚未被证明。
- [未验证] v0.6.9 发布于 2026-05-12（"security patches"，修 RUSTSEC 公告）是撰写时的最新版本；可能已有更新版本。
- [推断] 具体的 crate/组件布局、provider 列表与渠道列表均按 README 概括；依赖某个具体 provider/渠道/Hand 前请对照当前仓库核实。
