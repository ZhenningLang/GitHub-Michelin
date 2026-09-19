---
name: LiteLLM
slug: litellm
repo: https://github.com/BerriAI/litellm
category: api-gateway
tags: [llm-gateway, proxy, openai-compatible, cost-tracking, budgets, open-core]
language: Python
license: MIT (core) + enterprise/ commercial carve-out
maturity: v1.101.0, active, 59k stars, created 2023-07 (as of 2026-09)
last_verified: 2026-09-19
type: service
upstream:
  pushed_at: 2026-09-19T11:24:21Z
  default_branch: main
  default_branch_sha: 1f6e5b60b569d4e6def316ff30403cd0a480a740
  archived: false
health:
  schema: 1
  computed_at: 2026-09-19T11:27:36Z
  overall: A
  overall_score: 4.0
  scored_axes: 4
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
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: litellm
        dependent_repos_count: 1
        downloads_last_month: 191453852
        graph_tier: D
        volume_tier: A
        cross_check_divergence: 1.0
    longevity:
      grade: A
      raw:
        repo_age_days: 1150
        last_commit_age_days: 0
        cohort: service
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 301
        top1_share: 0.181
        top3_share: 0.382
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_window_signal }
    risk_license: { reason: license_unparsed }
---

# LiteLLM

可部署的 LLM 网关加 Python SDK：把 100 多家供应商收进一个 OpenAI 兼容 API，并补上成本追踪、预算、虚拟密钥、负载均衡、fallback、guardrails、日志与缓存。

![LiteLLM — 健康度雷达](../../assets/health/litellm.zh.svg)

## 何时使用

你是平台工程师，多个应用或团队各自拿自己的 key 直连模型供应商；你需要一个端点、按团队的虚拟密钥与预算、花费可见性，以及供应商劣化时的故障转移——又不想把这种耦合推进每个应用。这时选 LiteLLM，因为它就是为 LLM 流量做的：按模型路由、token 计费、预算与 guardrails 都是一等配置，你不必把模型语义硬塞进通用网关插件。

决定性的取舍是**用途与治理**。当 LLM 语义（模型映射、token 成本、预算执行）比 HTTP 层插件或 K8s Ingress 更重要时，选它而不是 [Kong Gateway](kong.zh.md)；当流量是服务多个产品的供应商 API key，而不是某个开发者的 coding agent 客户端或消费级登录池时，选它而不是 [Claude Code Router](claude-code-router.zh.md) 与 [CLIProxyAPI](cliproxyapi.zh.md)；当密钥与流量必须留在自有基础设施时，选它而不是 OpenRouter 这类托管中间商。治理的代价是完整功能面并非全部 MIT：`enterprise/` 采用商业许可。[未验证] 你需要的具体功能是否落在该边界内——定了再上，先查企业功能矩阵。

## 何时不用

- **需要执行 agent harness、沙箱或任务循环。** 改用 [OpenHands](../agent-frameworks/coding-agents/orchestration-and-review/openhands.zh.md) 或 [HarnessRouter](harnessrouter.zh.md)；LiteLLM 只路由模型调用，不跑 agent。
- **单供应商的小应用。** 直接用厂商 SDK（`openai`、`anthropic`）；一个带数据库和密钥管理的网关是你付了钱却用不上的开销。
- **要求整个功能面都在宽松许可下、没有商业目录。** 改用 Apache-2.0 网关如 [Kong Gateway](kong.zh.md)；LiteLLM 的 SSO、SCIM、审计日志与细粒度 RBAC 是企业许可。
- **需要 K8s 原生流量策略与插件生态。** 用 Kong 或基于 Envoy 的 AI 网关；LiteLLM 是应用层代理，不是数据面网关。
- **无法容忍跨协议语义损失或快速升级节奏。** 直接调供应商或改用托管中间商；兼容层会在 OpenAI、Anthropic、Gemini 形状之间丢字段或错位。
- **要的是单个开发者 coding agent 的路由，而不是共享网关。** 改用 [Claude Code Router](claude-code-router.zh.md)；那件事不需要预算、密钥与数据库。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| Portkey Gateway | 未收录 | 想要一个完全开源、把 guardrails/可观测做成一等能力的 LLM 网关时，评估 Portkey Gateway；当 LiteLLM 的供应商广度、成本追踪与社区规模更重要、且不要求许可完全宽松时，选 LiteLLM。 | Portkey 是同类 LLM 网关，open-core 姿态不同；LiteLLM 生态与集成更多，但企业目录边界与“持有凭据的代理”的 CVE 历史是实打实的成本。 |
| [Kong Gateway](kong.zh.md) | 已收录 | 需要一个既能处理 LLM/MCP 流量、又有 K8s Ingress 与插件生态的 HTTP/API 网关时，选 Kong；当 LLM 特有的成本、预算与模型语义才是真正需求时，选 LiteLLM。 | Kong 是成熟数据面网关，配置模型更陡，且没有原生 token 计费；LiteLLM 做 LLM 路由更简单，但属应用层，不是通用流量网关。 |
| [Claude Code Router](claude-code-router.zh.md) | 已收录 | 开发者想在本机让 coding agent 跨模型路由时，选 Router；流量属于产品、需要密钥/预算/花费记录时，选 LiteLLM。 | Router 是本地单用户工具，没有多租户控制；LiteLLM 加上数据库与治理，也必须当服务运维。 |
| [CLIProxyAPI](cliproxyapi.zh.md) | 已收录 | 要被复用的资产是消费级 CLI/OAuth 登录态时，选 CLIProxyAPI；资产是供应商 API key、需求是治理时，选 LiteLLM。 | CLIProxyAPI 把订阅变成 API 并承担账号政策风险；LiteLLM 走签发的 key、留在厂商条款内，代价是真实的基础设施。 |
| OpenRouter | 未收录 | 不想运维网关、接受托管中间商及其按 token 加价时，选 OpenRouter；凭据与花费数据必须留在自有基础设施时，选 LiteLLM。 | OpenRouter 去掉运维和数据库，链路里多一个第三方与加价；LiteLLM 保留控制权，换来 PostgreSQL、Redis 与升级工作。 |

## 技术栈

- **网关服务：** Python ≥3.10 上的 FastAPI/Uvicorn，配 Pydantic 与 HTTPX/AIOHTTP；另有 TypeScript 管理 UI。
- **可选 Rust 核心：** 仓库描述为 “Rust core with Python SDK”；Rust 路径经 Maturin/PyO3 编入 wheel，但文档标注为默认关闭的 opt-in beta，只覆盖部分路由——认证、配置、路由、日志与成本追踪仍由 Python 完成。[未验证] 它在你的部署中的成熟度。
- **状态：** PostgreSQL（经 Prisma）存虚拟密钥、预算与花费；Redis 用于多 worker 协调、限流与缓存。
- **安装与分发：** `pip`/`uv`、Docker、Docker Compose 与 Helm；配置是一份 `config.yaml` 加 master key 与 salt key。

## 依赖

- **PostgreSQL**：使用管理 UI、虚拟密钥、预算或花费追踪时需要；纯无状态代理可不接。
- **Redis**：多于一个 worker 或 pod 时需要，否则限流、预算、密钥撤销与缓存会按 worker 分裂。
- **`LITELLM_MASTER_KEY`**，以及使用数据库时固定的 **`LITELLM_SALT_KEY`**——更换 salt 会让已存凭据无法解密。
- **所有上游供应商的 API key**。LiteLLM 持有它们，因此它天然是高价值凭据库。
- **容器主机或 K8s 集群**（若部署代理本身而非嵌入 SDK）。

## 运维难度

**中到高。** 单容器、单 worker 的代理起来很快，但让 LiteLLM 值得选的正是那套引入状态的功能：PostgreSQL 迁移、多 worker 下的 Redis 一致性、master/salt key 保管、逐供应商凭据轮换。项目自己的生产指南是一 pod 一 worker 再横向扩展，近期 issue 也暴露了运维尖角——Slack 告警任务泄漏并可能 OOM（#41357）、分区 spend 表迁移失败（#41548）、Prisma 空闲连接不释放（#41420）、协议桥字段丢失或错位（#41954）。发版节奏很快（约每周一个 minor），而且因为代理集中持有供应商凭据，升级与攻击面管理是长期工作，不是一次性事项。

## 健康度与可持续性

- **维护活跃度（截至 2026-09）：** 最新稳定版 v1.101.0（2026-09-15），近约 30 天 23 个 release，官方约每周一个 minor——高度活跃。
- **治理与 bus factor：** contributors API 返回 1,731 条记录与约 5.1 万次归属提交，但其中含匿名作者、机器人与重复身份；前三账号合计约 51.5%，与 BerriAI 创始人高度吻合。属厂商主导而非社区治理。[推断]
- **背景与长青度：** 项目始于 2023-07，由商业厂商 BerriAI 支持并设有付费企业版。有资金的厂商带来长青度与真实支持路径，同时也意味着路线图与许可决策服务于该商业利益。[推断]
- **采用度：** 约 59k stars、11.6k forks，watchers 234——本页最强的采用信号；仓库体量很大（约 1.66 GB），这对 clone 与归档本身就是一条轻度运维提示。
- **风险旗：** 2024-02-15 从纯 MIT 改为 MIT 加 `enterprise/` 商业 carve-out（未对既有非企业代码重新许可）；贡献者必须签 CLA；仓库公布 14 个安全公告（3 critical、5 high），包括认证绕过、SQL 注入与 SSRF 凭据泄露。一个高速迭代、集中持有全部供应商密钥的代理，天然是高价值目标。

## 存疑（未验证）

- [未验证] 你需要的功能具体哪些落在 `enterprise/` 内；边界读自许可证与企业文档，未逐功能实测。
- [未验证] 安全公告（共 14 个，3 critical，含被报告的认证绕过、SQL 注入与 SSRF 凭据泄露）读自 GitHub advisories，未独立复现，也未逐一映射到当前版本。
- [未验证] “Rust core” 的真实成熟度；文档标为 opt-in beta，但它覆盖多少路由本文未做基准测试。
- [未验证] 独立自然人贡献者数未知——contributors API 混入匿名、机器人与重复条目，因此上面的 bus factor 份额只是近似。
- [推断] 由于 LiteLLM 有厂商背景与付费企业版，路线图与许可优先级会倾向服务该商业利益；这是取舍，不是缺陷。
- [未验证] 本页没有部署该代理，因此上文 PostgreSQL/Redis 故障模式与迁移问题取自文档与 issue tracker，而非复现结果。
