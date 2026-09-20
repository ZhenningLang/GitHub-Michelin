---
name: OpenSandbox
slug: opensandbox
repo: https://github.com/opensandbox-group/OpenSandbox
category: sandboxing
tags: [sandbox, agent-runtime, code-execution, isolation, kubernetes, docker, microvm]
language: Python
license: Apache-2.0
maturity: v0.x (python SDK v0.1.13), active, ~11.7k stars (as of 2026-06)
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-06-29T11:31:31Z
  default_branch: main
  default_branch_sha: 032790072b3efb69a75a2917e26259df49cf7138
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:25:00Z
  overall: B
  overall_score: 3.4
  scored_axes: 5
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
        median_ttfr_hours: 26.4
        qualifying_issues: 32
        band: default
        window_offset_days: 0
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: D
      raw:
        repo_age_days: 198
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 71
        top1_share: 0.393
        top3_share: 0.631
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
    adoption: { reason: ambiguous }
---

# OpenSandbox

面向 AI agent 的通用、安全沙箱运行时与平台——多语言 SDK、一套统一的沙箱协议，以及 Docker/Kubernetes 后端，用于在隔离环境里运行不可信的 agent 生成代码、GUI/浏览器自动化，以及 RL/评测负载。

![opensandbox — 健康度雷达](../../assets/health/opensandbox.zh.svg)

## 何时使用

你在做一个 coding agent（或一个 agent 评测 harness），撞上了所有这类项目都会撞的那堵墙：模型想跑 shell 命令、写文件、`pip install`、执行它刚生成的任意代码——而你不能让这些碰到你的宿主机或其他租户。你一直在拿裸 Docker `exec`、自己手搓的文件系统 API 和一些吓人的网络配置硬拼，到了笔记本之外就撑不住。于是你转向 OpenSandbox：`pip install opensandbox`，指向一个运行时（开发用本地 Docker，机群规模用 Kubernetes 运行时），就得到一套统一 API，用来创建沙箱、跑命令、把文件搬进搬出、跑内置的 Code Interpreter——还带每沙箱出口管控和凭据保险库，让工作负载永远看不到你真正的 secret。同一段 SDK 调用，无论你在单机还是在集群上调度成千上万个沙箱，都一样能用。

当隔离强度是硬性要求而非事后补丁时，你也会选它：它能把沙箱跑在安全容器运行时（gVisor、Kata Containers、Firecracker microVM）上而非普通容器里，还暴露一个统一 ingress 网关和一套你可以用自定义运行时扩展的沙箱协议。如果你在对比托管的代码执行 API、但又想自托管运行时——把 agent 的代码执行留在自己的基础设施内——这正是瞄准这个缺口的那类平台。

## 何时不用

- **你只是要在本地跑一个可信脚本。** 如果代码是你自己的、可信的，一个普通 Docker 容器或子进程，远比一个带 server、运行时和协议的完整沙箱平台轻得多。
- **你能用托管的代码执行 API、又不想运维基础设施。** 托管沙箱服务（E2B、Daytona、各家 code-interpreter API）把运维负担整个拿走；OpenSandbox 是你要自己跑、还得一直跑下去的东西。
- **你今天就需要一个久经沙场、多年验证的依赖。** 该仓库 2025-12 才创建——只有几个月大。几个月大的项目却有极高 star，是炒作信号，而非 Lindy/履历信号；API 和沙箱协议可能仍会变动。[推断]
- **你的隔离要求需要某个你必须自己认证的、经过审计的特定运行时。** OpenSandbox 能驱动 gVisor/Kata/Firecracker，但你仍要自己负责配置并验证隔离是否满足你的威胁模型——把它们集成进来的平台，不能替代那份审查。[未验证]
- **你不跑 Kubernetes 或 Docker、也不想跑。** 运行时就是 Docker 和 Kubernetes；没有 serverless/免基础设施模式——编排层是你要自己运维的。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [E2B](e2b.zh.md) | ✅ | 想要沙箱以「可托管也可自托管」的 SDK 形态交付、还带解释器与桌面能力，选 E2B；平台本身必须自托管且可扩展，选 OpenSandbox。 | E2B 主打打磨过的托管产品与 AWS／GCP 的 Terraform 自托管；OpenSandbox 主打自托管优先的平台与可扩展的沙箱协议。两者都把「底下跑哪种沙箱技术」藏起来，只是押注谁来运维它。 |
| [Agent Substrate](substrate.zh.md) | ✅ | agent 长生命周期、大量时间闲置、成本问题在 pod 密度与快照恢复，选 Substrate；任务是「现在就把这段代码隔离跑掉」，选 OpenSandbox。 | Substrate 用暂停／恢复多路复用有状态会话；OpenSandbox 暴露一次性执行沙箱。重叠只在隔离层——密度与按需执行之别。 |
| [gVisor](gvisor.zh.md) | ✅ | 想要不依赖虚拟机的系统调用级隔离、并自己写沙箱生命周期，选 gVisor；想要那套生命周期、SDK 与策略一起交付，选 OpenSandbox。 | 作为 runtime class 使用的用户态内核；它是 OpenSandbox 这类平台可以驱动的隔离原语，不是平台。 |
| [Kata Containers](kata-containers.zh.md) | ✅ | 想让 Kubernetes 给每个 pod 一台轻量虚拟机里的真内核，选 Kata；想要沙箱 API 而不是 runtime class，选 OpenSandbox。 | Kata 是节点级虚拟机隔离加完整的容器管理器集成；OpenSandbox 是它这类运行时之上的 API／生命周期层。 |
| [Firecracker](firecracker.zh.md) | ✅ | 你在自建沙箱层、想要极简的 KVM microVM 原语，选 Firecracker；想要以产品形态拿到沙箱，选 OpenSandbox。 | Firecracker 止步于 microVM 边界；OpenSandbox 必须在某个此类原语之上解决镜像、调度、生命周期与策略。 |
| Daytona | 未收录 | 需要面向 agent 的托管优先开发环境／沙箱平台，选 Daytona；平台必须自托管，选 OpenSandbox。 | 相邻产品形态（开发环境而非 agent 代码执行协议）；本批未收录——按待办记录，而不是以能力为由判为范围外。 |
| 普通 Docker／containerd | 未收录 | 普通容器够用时选 Docker 或 containerd；负载不可信、需要沙箱协议、凭据保险库与出口策略时选 OpenSandbox。 | 你正在替换的基线（containerd／runc 的选型不在本页范围）：你拿到的是一个容器，不是沙箱平台。 |
| Jupyter Kernel Gateway／nsjail | 未收录 | 需要窄而单一用途的代码执行或隔离管线时选它们；想要它外面那层面向 agent 的平台，选 OpenSandbox。 | 单一用途原语，没有多租户平台层；对本分类属范围外，而不是可收录的同层项目。 |

## 技术栈

- **语言：** 主语言为 Python；项目提供 Python、Java/Kotlin、JavaScript/TypeScript、C#/.NET、Go 的 SDK。
- **运行时：** Docker（本地）和用于分布式调度的 Kubernetes 运行时/控制器。
- **隔离：** 集成安全容器运行时——gVisor、Kata Containers、Firecracker microVM——以加强宿主/工作负载分离。
- **接口面：** `osb` CLI、一个 MCP server 集成、带每沙箱出口管控的统一 ingress 网关、一个凭据保险库，以及 `specs/` 里一份文档化的沙箱协议（生命周期 + 执行 API）。
- **内置：** Command、Filesystem、Code Interpreter 环境；带 Claude Code、Chrome/Playwright 浏览器自动化、VNC/VS Code 桌面的示例。

## 依赖

- **你必须跑的运行时：** 一个容器运行时——本地用 Docker，规模化用 Kubernetes 集群（外加 OpenSandbox 的生命周期 server/控制器）。这是承重依赖。
- **可选安全运行时：** 想要强于普通容器的隔离，则需 gVisor、Kata Containers 或 Firecracker——每个都带自己的宿主/内核配置。
- **SDK 安装：** `pip install opensandbox`（Python）、`com.alibaba.opensandbox` 下的 Maven/Gradle 制品、`@alibaba-group/opensandbox`（npm）、一个 .NET 包，以及一个 Go module。CLI 是 `opensandbox-cli`。
- **网络：** ingress 网关和出口管控假定由你提供周边网络管道。

## 运维难度

**中到高。** 本地 Docker 路径对开发友好。生产则是一个真要运维的平台：一个生命周期 server、一个 Kubernetes 控制器、一个 ingress 网关、出口策略和一个凭据保险库——若还要强隔离，再加上 gVisor/Kata/Firecracker 的宿主级配置（内核特性、节点配置）。你跑的是一个多组件分布式系统，它的全部职责就是安全地执行不可信代码，所以把隔离、网络和 secret 处理弄对才是难点，而且是安全攸关的。项目带 OpenSSF Best Practices 徽章和一份 GOVERNANCE.md，这有帮助，但其运维面天生比单一二进制或托管 API 要大。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 26.4 小时，基于 32 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06-27；多个组件版本 tag 于 2026-06-25（python SDK v0.1.13、java v1.0.15）——**非常活跃**的开发。未归档。[推断]
- **背书与治理（2026-06）。** 源自阿里巴巴（仓库自身的徽章/链接指向 `github.com/alibaba/OpenSandbox`），现位于 `opensandbox-group` 组织下，带 GOVERNANCE.md、一条 OpenSSF Best Practices 记录和一项 CNCF Landscape 收录——这些是朝向开放、多维护者治理、由一家大厂商背书的信号。[未验证]
- **年龄 × Lindy（2026-06）。** 2025-12 创建——约 6 个月大。这是一个**年轻项目**；Lindy 还不给它加分。几个月大的仓库却有约 11.7k star，是很强的炒作/注意力信号，但说明不了寿命。把 API/协议稳定性当成未经验证。[推断]
- **采用度与生态。** 广的 SDK 覆盖（5 种语言）、MCP 集成和 CNCF Landscape 在场，都表明真实的生态野心；在这个年龄上，生产用户证据稀薄且未经验证。[未验证]
- **风险标记。** 年轻是主要一项——API 变动和履历未证。单一大厂商起源（阿里巴巴）尽管有多维护者的说法，仍是治理上的考量；若你要依赖它，请核实决策实际是怎么做出的。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 11.7k star、python SDK v0.1.13——star 与版本号对时间敏感、随版本变动，仅供参考。
- [未验证] “安全容器运行时”支持（gVisor/Kata/Firecracker）是 README 的声称；每种的确切成熟度、配置负担和隔离保证未对源码核实。
- [推断] 阿里巴巴起源由 README 徽章/链接指向 `github.com/alibaba/OpenSandbox` 推断得出；规范仓库现位于 `opensandbox-group` 下。确切的归属/转移与治理实况未确认。
- [推断] “几个月大 + 极高 star”按 read-repo 方法论被当作炒作/风险信号，而非质量定论；项目可能成熟，但其 Lindy 履历目前并不存在。
- [未验证] 与 E2B/Daytona 的对比反映总体定位，而非逐项实测基准。
