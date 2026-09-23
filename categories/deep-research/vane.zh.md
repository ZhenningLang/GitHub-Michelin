---
name: Vane
slug: vane
repo: https://github.com/ItzCrazyKns/Vane
category: deep-research
tags: [ai-search, answering-engine, searxng, rag, self-hosted, perplexica]
language: TypeScript
license: MIT
maturity: v1.12.2, active (2026-04)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-04-11T14:33:06Z
  default_branch: master
  default_branch_sha: 7dc5d088f7262fbc5e39037f84940a8a2193c5fb
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:43:14Z
  overall: B
  overall_score: 2.8
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
        last_commit_age_days: 21
        active_weeks_13: 1
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 134.3
        qualifying_issues: 5
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 896
        last_commit_age_days: 21
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 9
        top1_share: 0.971
        top3_share: 0.984
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

# Vane

自托管、注重隐私的 AI 应答引擎：用 SearxNG 做联网搜索 + 你自选的本地或云端 LLM，返回带引用的答案——同一作者 Perplexica 项目的继任/改名版。

![vane — 健康度雷达](../../assets/health/vane.zh.svg)

## 何时使用

你是开发者或小团队，想要一个完全自己掌控的、自托管的「Perplexity 式」应答框：你输入一个问题，它去搜实时网页、读取头部来源、写出带引用的答案，而不是甩给你十条蓝色链接。关键是，你不希望查询离开自己的机器，也不想被绑死在某个闭源模型上：Vane 以单个 Docker 容器运行，联网搜索走你自己的 SearxNG 实例，LLM 则可指向本地 Ollama、OpenAI 兼容端点、Claude、Gemini 或 Groq。你可以为每次查询选 Speed / Balanced / Quality 模式，在延迟和深度之间取舍，把来源限定为网页 / 学术 / 讨论，甚至上传文档对其提问。整套东西自带打磨过的 Web UI、搜索历史和小组件——它是你部署的产品，不是你接线的库。

如果你之前跑过 Perplexica、想要它的维护续作，那也很合适：Vane 是同一作者对该项目的演进，所以心智模型（SearxNG + 对结果做 RAG + 会引用来源的 LLM）可以直接迁移，只是叠加了刷新的 UI、provider 列表和三档深度控制。

## 何时不用

- **你要的是可编程的研究管线，而非聊天应用。** Vane 是面向终端用户的 Web 产品（Next.js UI + chat API）。如果你想从自己的 agent 里调用 deep-research、把它嵌进后端、或拿到结构化 JSON 输出，那么像 [deep-research](deep-research.zh.md) 这种 SDK 优先的工具更合适——Vane 没有公开的「research 作为库」的接口面。[推断]
- **你无法或不愿运行 SearxNG。** 联网搜索依赖一个开启 JSON 输出的可用 SearxNG 实例；如果你托管不了（或公共实例不稳定），核心环路就断了。这是实打实的运维面，不是一个配置开关。
- **你想要真正离线 / 完全本地的「深度研究」。** 即便用本地 Ollama 模型，Vane 仍会经 SearxNG 触达实时网页；它不是为 [local-deep-research](local-deep-research.zh.md) 那种气隙、仅本地语料的工作流设计的。
- **你需要穷尽式、长程的迭代研究。** Vane 的 Quality 模式比 Speed 更深，但它本质仍是为「快速给出带引用答案」调优的交互式应答引擎——不是那种扇出几十个子查询、连续几分钟递归下钻的长自治循环。
- **你需要开箱即用的多用户鉴权 / SaaS 托管。** 鉴权和账户体系在 roadmap 上，尚未交付；现在它是单租户自托管应用。[未验证] 任何多租户部署都按 DIY 对待。
- **你受不了快速演进的单一维护者改名项目。** Vane 承接了 Perplexica 的血统和势头，但它本质是近期改名、主要由一位作者维护的项目；API/UI 抖动和 bus-factor 风险都存在。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [deep-research](deep-research.zh.md) | ✅ | 需要从代码里调用的极简 TypeScript 引擎/SDK 时，选 deep-research。 | 极简的 TypeScript 深度研究*引擎/SDK*，从代码里调用并调参（breadth/depth）;Vane 是完整的自托管 UI 产品，不是可嵌入的库。 |
| [local-deep-research](local-deep-research.zh.md) | ✅ | 需要 Python、本地优先、可离线研究本地语料时，选 local-deep-research。 | Python，偏本地优先，能离线对本地语料做研究；Vane 始终经 SearxNG 触达实时网页，并以打磨过的 Web 应用形态交付。 |
| [Agent-Reach](agent-reach.zh.md) | ✅ | 你其实需要 reach/触达式自动化而不是应答引擎时，选 Agent-Reach。 | 不同细分（agent reach / 触达式自动化）；不是 SearxNG 应答引擎。只有把两者混淆时才需对比。 |
| Perplexica | 未收录 | 需要 Vane 的同作者直接前身时，选 Perplexica。 | Vane 的直接前身，同一作者，同样的 SearxNG+RAG 内核。选 Vane = 选被维护的续作。 |
| [GPT Researcher](gpt-researcher.zh.md) | ✅ | 需要会写长报告的 Python 自治研究 agent 时，选 GPT Researcher。 | Python 自治研究 agent，产出长报告；更偏报告生成、少交互式带引用应答体验，无内建聊天产品。 |
| Morphic / Perplexity（托管） | 未收录 | 需要托管/闭源应答引擎时，选 Morphic 或 Perplexity。 | 托管/闭源应答引擎；无自托管、无 provider 选择，与 Vane 的隐私/自托管主张正相反。 |

## 技术栈

- **语言：** TypeScript（按 GitHub 语言统计约占仓库 98%+）。
- **框架：** Next.js（同时承载 UI 与 API 路由——`/api/chat`、`/api/search`、`/api/providers`）。
- **搜索后端：** SearxNG（跨多引擎的元搜索，以 JSON 形式查询结果）。
- **LLM 集成：** 可插拔 provider——Ollama（本地）、OpenAI、Anthropic Claude、Google Gemini、Groq，以及 OpenAI-API 兼容服务器（README 还提到 Lemonade）。
- **检索：** 对抓取的网页结果做 RAG；用嵌入模型对用户上传文件做语义搜索。
- **持久化：** 通过 Docker 卷在本地存储 chats/messages 与上传文件；ORM 是 Drizzle。[推断] README 未明确底层 DB 引擎（SQLite 还是其它）。
- **样式：** Tailwind CSS。

## 依赖

- **运行时：** Docker（推荐）——单镜像 `itzcrazykns1337/vane:latest`，暴露 3000 端口并挂持久卷 `-v vane-data:/home/vane/data`。
- **非 Docker:** Node.js + npm(`npm i` → `npm run build` → `npm run start`)，外加自行安装、开启 JSON 输出的 SearxNG。
- **外部服务：** 联网搜索基本上必需一个可达的 SearxNG 实例。
- **模型：** 至少配置一个 LLM provider——本地 Ollama 安装，或 OpenAI / Claude / Gemini / Groq / OpenAI 兼容端点的 API key。
- **一键托管：** README 列出 Sealos、RepoCloud、ClawCloud、Hostinger 作为部署目标。

## 运维难度

**低到中。** Docker 顺路径确实是一行命令，指向一个云 LLM API key 就能在几分钟内得到可用的应答引擎。当你自托管整套栈时难度升到**中**：你得搭起并维护一个 SearxNG 实例（引擎会被限流/封禁、必须开启 JSON 输出），如果走全本地还要再跑并配资源给 Ollama 模型（内存/显存、模型拉取）。升级跟随一个快速演进的单镜像，所以需要稳定就 pin 版本；另外要备份数据卷，因为搜索历史/对话都存在那里。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 59.6 小时，基于 11 个 qualifying issues/PRs。
- **维护（2026-06）：** **活跃**——最新 release v1.12.2 约在 2026-04，push 约 2026-04，已是两位数小版本的成熟版本线。稳定推进，不是 coasting。[推断]
- **治理与 bus factor:** `User` 名下（`ItzCrazyKns`），约 35k star——一个 **bus-factor 警示**：极高曝光，背后基本是**一位维护者**。它又是近期改名的项目，单人主导下的 API/UI 抖动是现实风险。[推断]
- **年龄与 Lindy（约 2 年，含 Perplexica 血统，自 2024-04 起算）：** 尽管「Vane」是新名字，*代码库*承接了 Perplexica 约 2 年的历史与势头——这份血统才是这里的 Lindy 信号，而非改名日期。够老且活跃，整体偏正面，但被单人维护这一点拉回一些。[推断]
- **风险标记：** 多用户鉴权仍在 roadmap、尚未交付（按单租户对待）；快速演进的单镜像发布意味着要 pin 版本并备份数据卷。[未验证]

## 存疑（未验证）

- [未验证] 最新发布 v1.12.2（约 2026-04-10 发布）,`pushedAt` 约 2026-04-11；截至 2026-06 star 约 35.5k——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 确切的 provider 列表（尤其是 "Lemonade" 和完整的 OpenAI 兼容服务器集合）以及一键托管列表来自 README；依赖某具体 provider 前请对照当前仓库核实。
- [推断] 持久化层用 Drizzle ORM，但 README 未明确点名底层数据库引擎（从单文件数据卷推测可能是 SQLite，未确认）。
- [未验证] 鉴权 / 多用户支持被描述为 roadmap，尚未交付；当前部署应按单租户对待。
- [推断] Vane 是同一作者（ItzCrazyKns）Perplexica 的改名/继任版；README 未用明文陈述改名历史，系据共享作者、topics（`perplexica`）与架构推断。
- [推断] 「Quality 模式做更深研究」相对 Speed/Balanced 是项目对延迟/深度取舍的表述；每个模式具体的子查询数或迭代次数未见文档说明。
