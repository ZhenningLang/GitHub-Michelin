---
name: Agent-Reach
slug: agent-reach
repo: https://github.com/Panniantong/Agent-Reach
category: deep-research
tags: [web-scraping, social-search, cli, mcp, agent-tooling, twitter, reddit, youtube, bilibili, xiaohongshu, multi-backend, content-fetch]
language: Python
license: MIT
maturity: v1.5.0 (2026-06-11), active, ~41.6k stars (as of 2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T03:34:57Z
  default_branch: main
  default_branch_sha: d1d2eda070221cf600e2517a5b028c8d4b0aa67a
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:42:51Z
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
        last_commit_age_days: 7
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 81.1
        qualifying_issues: 19
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
        repo_age_days: 211
        last_commit_age_days: 7
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 37
        top1_share: 0.832
        top3_share: 0.866
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
    adoption: { reason: ambiguous }
---

# Agent-Reach

一个「接入 / 触达」层（而非研究 agent）：一个 CLI，替你装好并路由一整套上游工具，让你的 agent 能读取和搜索 Twitter/X、Reddit、YouTube、GitHub、Bilibili、小红书、RSS 和开放网页——「零 API 费用」。

![agent-reach — 健康度雷达](../../assets/health/agent-reach.zh.svg)

## 何时使用

你在搭一套 coding-agent 或研究助手工作流（Claude Code、Cursor、或你自己的循环），反复撞到同一堵墙：agent 推理没问题，但它对实时互联网是瞎的。你想让它拉一段 YouTube 字幕、干净地读一篇博客、上 Twitter/X 搜搜大家怎么评价某个库、抓一个 Reddit 帖、读一条 Bilibili / 小红书内容——而你**不想**为此注册一打付费 API、给每个平台手写爬虫、或者每周盯着哪个又挂了。Agent-Reach 用「眼睛」层解决这件事：你跑一次安装，它就按平台甄选并装好对应的上游工具（网页用 Jina Reader、YouTube 用 yt-dlp、GitHub 用 `gh`、社交平台用 twitter-cli/bili-cli/OpenCLI、语义搜索用经 MCP 的 Exa），然后你的 agent 直接调这些工具。

相比手搓工具箱，它真正值钱的地方是**多后端路由**：每个平台是「首选 + 备选的有序后端列表」,`agent-reach doctor` 会逐通道体检并报告当前生效的后端。当某个上游方法被限流或封锁——README 给的例子是 yt-dlp 在 Bilibili 被风控封死、栈自动回退到 bili-cli——你这边零改动就能继续工作。当「可触达源的广度」和「在反爬变动里活下来」比深度结构化分析更重要时，它很合适。

## 何时不用

- **你真正想要的是 deep-research agent。** Agent-Reach 是「抓取 / 接入」层；它**不做**迭代式 search→read→verify→synthesize 循环，也不产出带引用的报告。要那条流水线，请用真正的研究 agent，比如 [deep-research](deep-research.zh.md) 或 [local-deep-research](local-deep-research.zh.md)——若两者都要，就让研究 agent 去消费 Agent-Reach 暴露出的源。
- **你需要合规、ToS 干净、账号安全、可规模化的接入。** Twitter/X、Reddit、小红书都要你自己登录态的 cookie;README 自己标注了非浏览器自动化的 **封号风险**。这是用你的凭据做爬取——不是受官方背书的 API——ToS 与封号风险由你承担。
- **你要的是浏览器「操作」而非「读取」。** 明确非目标：「读内容 vs 操作网页」——它只读。不做表单提交、登录后流程、过验证码、多账号隔离。README 自己把「动手」场景指向 BrowserAct。
- **你想要一个稳定、自包含的依赖。** 它编排了一大堆第三方 CLI / MCP server(yt-dlp、twitter-cli、bili-cli、rdt-cli、OpenCLI、mcporter、Exa)，它们的行为、鉴权和反爬姿态一直在变。它的整个价值就是**管理**这种变动——但你也因此继承了一个又宽又脆的依赖面，版本之间频繁出问题。
- **生产 / 无人值守流水线。** 依赖消费级反爬「天气」的 cookie 爬取，做交互式 agent 没问题，做承重后端就很危险。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [deep-research](deep-research.zh.md) | ✅ | 需要真正的迭代式研究 agent 时，选 deep-research。 | 真正的迭代式研究 *agent*（扇出搜索 → 阅读 → 递归深挖 → 出报告）。Agent-Reach 恰是它缺的接入层；是栈的不同层，不是替代关系。 |
| [local-deep-research](local-deep-research.zh.md) | ✅ | 需要隐私优先、带综合和引用、本地 LLM 支持的研究助手时，选 local-deep-research。 | 隐私优先的本地研究助手，带综合 + 引用，支持本地 LLM。做的是 Agent-Reach 跳过的推理；配对用，而非二选一。 |
| [Vane](vane.zh.md) | ✅ | 需要聚焦综合的研究/搜索 agent 时，选 Vane。 | 聚焦综合的研究 / 搜索 agent。同样是「负责思考」的对照——Agent-Reach 负责触达，不负责推理。 |
| [Firecrawl](../web-scraping/crawling-tools/firecrawl.zh.md) | ✅ | 需要网页抓取转 markdown 加爬取 API 时，选 Firecrawl。 | 托管 / 开源的网页抓取转 markdown + 爬取 API；单源网页提取更干净、有真 API，但付费且仅限网页——没有 Twitter/Reddit/Bilibili/小红书的社交触达。 |
| Exa / Tavily / SearXNG | 未收录 | 需要语义搜索、agent 搜索或自托管元搜索后端时，选这些搜索后端。 | 搜索后端（语义 / agent 搜索 / 自托管元搜索）。Agent-Reach 实际就经 MCP 包了 Exa；它们给你搜索，但没有逐平台的社交爬取栈。 |

## 技术栈

- **语言：** Python(3.10+)。
- **编排的上游工具：** Jina Reader（网页转 markdown）、yt-dlp（YouTube 字幕/搜索）、feedparser(RSS/Atom)、`gh` CLI(GitHub)、twitter-cli(Twitter/X)、bili-cli(Bilibili)、OpenCLI + rdt-cli(Reddit)、OpenCLI / xiaohongshu-mcp（小红书）、linkedin-mcp、原生 V2EX / 雪球 API、Whisper（小宇宙播客转录）。
- **搜索：** 经 `mcporter`（MCP）的 Exa 语义搜索，宣称免费 / 无需 key。
- **集成模型：** 装好这些 CLI / MCP server，然后由 agent 直接调用——「实际的读取和搜索由 Agent 直接调用上游工具完成」（没有统一的单一抓取包装命令）。
- **路由/体检：** 每平台一个有序的首选+备选后端列表；`agent-reach doctor` 给出逐通道状态和修复指引。

## 依赖

- **运行时：** Python ≥ 3.10；装好上游 CLI 的 shell。很多后端会 shell out 到外部二进制（`gh`、yt-dlp、twitter-cli、bili-cli、OpenCLI），部分经 `mcporter` 走 MCP server。
- **鉴权 / 状态：** 登录态平台（Twitter/X、Reddit、小红书）需要从浏览器导出的 cookie；本地存放于 `~/.agent-reach/config.yaml`（权限 600）,「不上传不外传」（原文）。小红书播客小宇宙转录需要一个免费 API key。
- **安装：** `pip install agent-reach`，然后由 agent 驱动、指向项目 `docs/install.md` 完成 setup。
- **外部服务：** Exa（经 MCP）做语义搜索；其余即被读取的公开/社交站点，受其限流与反爬约束。

## 运维难度

**中。** 首次安装外加逐平台鉴权（为每个登录站点导 cookie）比单一托管 API 要折腾，而且零配置只覆盖公开通道（网页、YouTube、RSS、公开 GitHub、Exa 搜索）。真正的成本在持续维护：这是一层薄薄地盖在众多快速变动的第三方爬虫和消费级反爬系统之上的东西，单个通道**一定**会挂，需要重新鉴权或换后端。`agent-reach doctor` 和回退路由就是为了让这件事「能扛过去」，但你运维的终归是一套爬取栈，而非消费一个稳定 API。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 82.1 小时，基于 23 个 qualifying issues/PRs。
- **维护（截至 2026-06）：** 最后 push 在 2026-06，未归档，处于 v1.5.0，活跃。对一个全部工作就是*管理上游变动*的工具来说，维护的新鲜度是承重的：它的吃老本分叉会随着爬虫失效而悄悄烂掉。[推断]
- **治理与 bus factor：** `User` 所有（Panniantong），约 43k star——一个 **bus-factor 信号**：大量采用押在单个维护者身上，没有基金会或厂商兜底。这里的风险比通常更高，因为它的价值*就是*持续维护，而非一份稳定产物。[推断]
- **年龄与 Lindy 判断：** 建于 2026-02，年龄不足 1 年——**年轻且被炒作**（几个月 43k star）。Lindy 未被证明；而且这是个 Lindy 不如*当下*上游健康度重要的类目：即便是长寿版本，也得不断重新甄选后端。[推断]
- **风险标记：** 核心风险是结构性的，而非 license（MIT 宽松）。它编排了一个又宽又脆的第三方爬虫/MCP server 面（yt-dlp、twitter-cli、bili-cli、Exa 等），外加带 ToS/封号风险的 cookie 爬取——所以「健康度」既取决于本仓库，也取决于*那些上游*。把它当交互式工具，而非承重的生产后端。[推断]

## 存疑（未验证）

- [未验证] v1.5.0 发布于 2026-06-11;`gh repo view` 显示约 41.6k stars、`pushedAt` 为 2026-06-23——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 逐平台的后端列表、回退顺序和零配置矩阵取自 README，可能随版本漂移；依赖某具体通道前请对照 `agent-reach doctor` 和当前仓库核实。
- [推断] 任一社交通道的可用性取决于上游工具健康度和目标站点的反爬姿态，二者持续变化；「零 API 费用」/「用户零操作」的故障切换是项目的表述，不是独立测得的保证。
- [推断] cookie 爬取（Twitter/X、Reddit、小红书）的封号 / ToS 风险 README 已承认，但其严重程度因情境而异，此处未量化。
- [未验证] Exa-经-MCP「免费 / 无需 key」反映 README 写作时的说法；第三方服务条款可能变化。
