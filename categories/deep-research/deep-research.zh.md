---
name: deep-research
slug: deep-research
repo: https://github.com/dzhng/deep-research
category: deep-research
tags: [research-agent, firecrawl, vercel-ai-sdk, typescript, iterative-search]
language: TypeScript
license: MIT
maturity: untagged (no GitHub releases), active, last pushed 2026-04 (as of 2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-04-11T23:58:25Z
  default_branch: main
  default_branch_sha: 1f8f3e285bbc23e80b98a66a64effab9069f3ad4
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:07:08Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 164
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: B
      raw:
        repo_age_days: 596
        last_commit_age_days: 164
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
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    adoption: { reason: no_package_structural }
---

# deep-research

一个刻意做到极简（约 500 行）的 TypeScript 深度研究 agent：通过 Firecrawl 递归地扇出搜索查询、抓取结果、提炼 learnings，再合成带引用的 Markdown 报告——它的定位是「最简单、可读的参考实现」，而非一个产品。

![deep-research — 健康度雷达](../../assets/health/deep-research.zh.svg)

## 何时使用

你是想*真正搞懂*一个深度研究循环到底怎么跑的工程师——breadth/depth 递归、查询生成、learning 提炼、后续方向合成——而你宁可读 500 行 TypeScript，也不愿去逆向一个 5 万行的框架。你把它指向一个主题，在 CLI 里回答两个提示（`breadth` 3–10、`depth` 1–5），它就通过 Firecrawl 生成 SERP 查询、抓取页面、蒸馏出 learnings，然后要么继续向下递归，要么写出一份带来源的 `report.md`。因为整套逻辑能装进脑子里，它是理想的 fork 起点：换模型、改 prompt、接上你自己的抓取器都很容易。

如果你已经有 Firecrawl key 和一个 OpenAI 兼容端点，只想要一个可脚本化的 agent——从命令行或一个很薄的 Express API 把问题变成带来源的报告，而不用搭数据库、向量库或 UI——它也很合适。默认路径用 OpenAI 的 `o3-mini` 推理模型，检测到 Fireworks key 时自动切到 DeepSeek R1，并接受任意 OpenAI 兼容的 base URL（OpenRouter、Gemini 兼容网关等），所以你能保留自己的模型/供应商选择。

## 何时不用

- **你要一个开箱即用的产品或 UI。** 这是一个 CLI/脚本加一个极简 Express 端点，没有鉴权、历史记录或前端。想要托管式问答引擎请看 [Vane](vane.zh.md) 或某个 SaaS。
- **你需要完全本地 / 私有 / 离线的研究。** 它硬依赖 Firecrawl API 做搜索+抓取，默认还要云端 LLM。要在隔网、加密、本地 LLM 上检索私有文档，用 [local-deep-research](local-deep-research.zh.md)。
- **你想免 API 费读社交平台（Twitter/Reddit/YouTube/GitHub）。** 那是另一类访问问题，见 [Agent-Reach](agent-reach.zh.md)。
- **你需要生产级稳健性。** 没有 release tag，版本仍是 `0.0.1`，刻意只有约 500 行——错误处理极简，没有限流/重试/成本控制方案，基本没有测试覆盖。把它当参考/fork 底座，而不是一个被维护的依赖。
- **你想避免逐次云端开销。** Firecrawl 额度 + 每个递归层的推理模型调用，在高 breadth/depth 下会迅速变贵，且没有内建预算上限。[推断]
- **你在意弃坑/维护风险。** 它是单作者的 demo 仓库，活跃度呈阵发式，没有 release/changelog 节奏。别把业务关键管线直接架在它之上。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Vane](vane.zh.md) | ✅ | 需要可用产品/UI 形态的 TypeScript 问答引擎时，选 Vane。 | 同为 TypeScript 的 AI 问答引擎，目标是做成可用的产品/UI;deep-research 是约 500 行、供你 fork 的裸 agent，而非可直接当服务跑。 |
| [local-deep-research](local-deep-research.zh.md) | ✅ | 需要 Python、本地优先且加密的研究助手时，选 local-deep-research。 | Python，本地优先且加密，10+ 搜索后端（含本地文档），可完全跑在本地 LLM 上；deep-research 默认是云 LLM + Firecrawl，范围也小得多。 |
| [Agent-Reach](agent-reach.zh.md) | ✅ | 需要读社交/网络平台而非综合研究时，选 Agent-Reach。 | Python CLI，专注「读」社交/网络平台（Twitter/Reddit/YouTube/GitHub）且号称「零 API 费」；不是做迭代式综合的研究 agent。 |
| [GPT Researcher](gpt-researcher.zh.md) | ✅ | 需要功能面更大的 Python 研究 agent、报告类型和 Web UI 时，选 GPT Researcher。 | Python，功能面大得多（多检索器、多报告类型、Web UI）;deep-research 用全部这些广度换来一个可读的极简内核。 |
| [Open Deep Research(LangChain / HF)](open-deep-research.zh.md) | ✅ | 框架背书、生态和工具链更重要时，选 Open Deep Research。 | 有框架背书的参考 agent，生态与工具链更大；比这个近乎单文件的实现更难读、更难改造。 |

## 技术栈

- **语言：** TypeScript（仓库约 98%）；通过 `tsx` 跑在 Node.js 22.x 上。
- **LLM 层：** Vercel AI SDK（`ai`）配 `@ai-sdk/openai` 与 `@ai-sdk/fireworks` provider；默认模型 `o3-mini`，有 Fireworks key 时自动切到 DeepSeek R1；支持 OpenAI 兼容 base URL。
- **搜索/抓取：** Firecrawl(`@mendable/firecrawl-js`)，可通过 `FIRECRAWL_BASE_URL` 自托管。
- **结构/校验：** `zod` 做带类型的结构化输出；`js-tiktoken` 做 token 计数；`p-limit` 做有界并发；`lodash-es`、`uuid` 工具。
- **入口：** 交互式 CLI（`npm start`）加一个很薄的 `express` + `cors` HTTP API(`npm run api`)；输出写成 `report.md` / `answer.md`。

## 依赖

- **运行时：** Node.js 22.x(`engines` pin 22.x)；通过 `tsx` 运行（无构建步骤），或用自带的 Docker 镜像 / `docker compose`。
- **外部服务（必需）:** 一个 Firecrawl API key（`FIRECRAWL_KEY`）用于搜索+抓取，以及一个 LLM key——`OPENAI_KEY`（OpenAI / 兼容）和/或用于 DeepSeek R1 的 `FIREWORKS_KEY`。可选 `OPENAI_ENDPOINT` / `FIRECRAWL_BASE_URL` 接自定义/自托管端点。
- **无数据库/向量库/队列**——状态在进程内；报告落在本地文件系统。
- **安装：** clone、`npm install`、配 `.env` key、`npm start`。Docker 路径：`docker compose up -d` 后 `docker exec -it deep-research npm run docker`。

## 运维难度

**跑起来低，负责任地运营则低到中。** 跑通一次研究很轻松：clone、加两个 API key、`npm start`。没有基础设施要管——没有 DB、UI、编排。运营风险在*成本与可靠性*，而非部署：高 `breadth`×`depth` 会把 Firecrawl 抓取和推理模型调用成倍放大，且没有内建预算上限或稳健的重试/限流处理，所以在任何无人值守/批量使用前，你大概率得自己加护栏。当 fork 底座没问题；当常驻独立服务则欠打磨。[推断]

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）：** 最近 push 在 2026-04；没有任何 GitHub release/tag，`package.json` 仍是 `0.0.1`。活跃度是**阵发式单作者**——介于 coasting 与 active 之间，不是一个被稳定维护的依赖。[推断]
- **治理与 bus factor:** `User` 名下的单人 demo 仓库、约 19k star——典型的 **bus-factor 警示**：曝光高、只有一个人、背后没有组织或 release 节奏。[推断]
- **年龄与 Lindy（约 1 年，2025-02 创建）：** 年轻且热门。star 给它带来的是关注度而非耐久性——太新，过不了 Lindy 门槛；按设计它就是供 fork 的参考实现，而非可长期押注的对象。[推断]
- **风险标记：** 无 semver/changelog 纪律、错误处理极简、无成本控制方案；当 fork 底座，而非可以 pin 了就忘的被维护上游。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 star 约 19.2k——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 「约 500 行」与「最简单的实现」是项目 README 自己的表述，本页未独立测量。
- [未验证] 默认模型 `o3-mini` 及自动切到 DeepSeek R1 的行为出自 README；距上次 push（2026-04）以来当前默认值可能已变。
- [未验证] 不存在 GitHub release/tag;`package.json` 版本为 `0.0.1`（读自 `main`），因此没有稳定的版本化产物可 pin。
- [推断] 单次运行的云端成本可能随 breadth/depth 陡增；没有官方成本控制特性的文档，所以「高设置下变贵」是从架构推断的。
- [推断] 维护是阵发式单作者；「active」反映的是 2026-04 的一次 push，而非有保证的持续节奏。
- [未验证] 内部 `package.json` 的 name 是 `open-deep-research`，而仓库/显示名是 `deep-research`；仓库 URL 与常用称呼是 `dzhng/deep-research`。
