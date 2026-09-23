---
name: promptfoo
slug: promptfoo
repo: https://github.com/promptfoo/promptfoo
category: llm-eval
tags: [llm-eval, red-teaming, prompt-testing, ci-cd, rag, vulnerability-scanning, cli, local-first]
language: TypeScript
license: MIT
maturity: v0.121.x, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-29T06:10:09Z
  default_branch: main
  default_branch_sha: 6ea8783c0802ed2e001e3d253a461e64602c2968
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:27:19Z
  overall: A
  overall_score: 3.8
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
        median_ttfr_hours: 83.0
        qualifying_issues: 33
        band: relaxed_solo
        window_offset_days: 10
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: promptfoo
        dependent_repos_count: 1
        downloads_last_month: 2498046
        graph_tier: D
        volume_tier: B
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 1243
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: empty_or_gated }
---

# promptfoo

一个 local-first 的 CLI + 库，把 prompt/模型/RAG/agent 的评测变成声明式 YAML 测试套件，内置红队/漏洞扫描器，并能接进 CI/CD。

![promptfoo — 健康度雷达](../../assets/health/promptfoo.zh.svg)

## 何时使用

你是在做 LLM 功能交付的工程师——一个客服 agent、一个 RAG 回答接口、一个分类 prompt——你已经厌倦了在 playground 里肉眼看输出、觉得“差不多能用”就上线。你想要一套回归测试：固定的一组输入、能在 prompt 改动让质量下降时真正让构建失败的断言，以及一个跨 GPT、Claude、Gemini 和本地 Ollama 模型的并排视图，这样你是凭证据而不是凭感觉选型。promptfoo 用一份 `promptfooconfig.yaml` 解决这个问题：把整套评测——prompt、provider、测试用例、断言（精确匹配、JSON schema、向量相似度，或 LLM 当裁判的 `llm-rubric`）——写进配置，然后本地跑 `npx promptfoo eval`，再用 `promptfoo view` 在浏览器里看结果矩阵。把同一条命令接进 CI，质量回归就会让 PR 失败。

当安全评审来问“这个 agent 会不会被越狱 / 会不会泄露 system prompt / 会不会以错误方式处理 PII”时，你也会用它。`redteam` 这一侧会针对你的线上接口生成对抗性探针（prompt 注入、越狱、有害内容、PII，以及 OWASP-LLM 风格的若干类别），并报告哪些攻击得手——把临时的渗透测试变成每次发版前都能重复跑的扫描。因为评测在你本机、用你自己的 provider key 运行，你的 prompt 和测试数据不必离开你的环境。

## 何时不用

- **你要的是开箱即用、面向团队的托管评测平台**（自带托管看板、RBAC、历史趋势存储）。promptfoo 是 local-first；云端分享/团队功能存在，但有 SLA、带治理的平台是商业版 Promptfoo，而非开源 CLI。需要交钥匙 SaaS 时，可权衡 LangSmith / Braintrust / Langfuse。
- **你不在 Node 工具链里、也不想引入它。** 它是 TypeScript/Node 包（Node `^20.20.0 || >=22.22.0`）；虽然有 `pip install promptfoo` 包装，但引擎是 Node。如果你的栈和团队纯 Python、想要原生 fixture,DeepEval（未收录）/ Python 原生 harness 更顺手。
- **你要做严谨的学术基准测试**（MMLU/HELM 式排行榜、统计报告，几百个标准任务）。promptfoo 是为*你自己应用的*测试用例而建，不是跑标准基准电池——那种场景用 lm-evaluation-harness / HELM。
- **你指望红队扫描器当合规保证。** 它给出的是*发现项*，且攻击覆盖随版本变化；通过一次扫描是证据，不是安全的证明。把结果当成会变动的信号，而非认证。
- **你想要零配置、一个魔法分数。** 价值在于写出好的断言和测试用例；如果没人维护评测集，你得到的只是一个意义不大的绿勾。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [DeepEval](deepeval.zh.md) | ✅ | 当你要 Python 原生、pytest 风格 eval 和更深的 RAG 指标时，选 DeepEval；当语言无关 YAML 套件、模型矩阵和集成红队更重要时，选 promptfoo。 | Python 原生评测框架（pytest 风格，G-Eval/faithfulness 等指标）；更适合 Python 团队和 RAG 指标深度。promptfoo 胜在语言无关的 YAML 配置、并排模型矩阵和集成红队。 |
| [Langfuse](langfuse.zh.md) | ✅ | 当生产追踪、数据集、趋势历史和可自托管 UI 是主要平台需求时，选 Langfuse；当只要更轻的 CLI 优先 CI 回归/红队闸门时，选 promptfoo。 | 追踪/可观测性 + 评测平台（可自托管，带 UI 和数据集后端）；强在生产监控和趋势历史。promptfoo 更轻、CLI 优先、偏红队，而非可观测性后端。 |
| LangSmith | 未收录 | 当你要托管的 LangChain 中心 eval 和可观测性时，选 LangSmith；当开源、local-first 运行和框架无关 provider 是硬要求时，选 promptfoo。 | 托管的 LangChain 评测/可观测性 SaaS;LangChain 集成深、看板托管，但闭源、以云为中心。promptfoo 开源、local-first、框架无关。 |
| Braintrust | 未收录 | 当商业实验平台、托管打分、日志和打磨过的团队流程值得引入托管依赖时，选 Braintrust；当你要开放、自跑的 CLI 时，选 promptfoo。 | 商业评测/实验平台，托管打分与日志；团队 UX 打磨好。promptfoo 用开放、自跑的 CLI 换掉这套托管平台。 |
| [Garak](garak.zh.md) | ✅ | 当任务只是专门的 Python 红队扫描时，选 Garak；当红队检查需要和通用 eval 断言放在同一工作流里时，选 promptfoo。 | 专门的 LLM 漏洞扫描器（只做红队，Python）。与 promptfoo 的 `redteam` 范围重叠，但不是通用评测/断言 harness。 |
| [Giskard](giskard.zh.md) | ✅ | 当你要更广的 ML+LLM 测试和 Python 中心扫描报告模型时，选 Giskard；当 prompt 和 CI 回归工作流是中心时，选 promptfoo。 | 面向 ML+LLM 的开源测试/红队，扫描-报告模式；ML 范围更广、以 Python 为中心。promptfoo 更聚焦 prompt/CI 工作流。 |

## 技术栈

- **语言：** TypeScript / Node.js（CLI 命令为 `promptfoo` 和 `pf`）。
- **核心库（依 package.json,v0.121.17）:** `commander`(CLI)、`express` + `compression`/`cors`（本地 Web 查看器服务）、`drizzle-orm` + `@libsql/client`（本地 SQLite 评测存储）、`ajv`/`ajv-formats`（JSON-schema 断言）、`@anthropic-ai/sdk` 和 `ai` SDK 及众多 provider 客户端、`@opentelemetry/*`（追踪）、`chokidar`/`execa`/`chalk`（CLI 基建）。
- **配置面：** 声明式 `promptfooconfig.yaml`(prompts、providers、tests、assertions、`redteam`)；也可作为库使用或接进 CI。
- **断言类型：** 确定性（equals/contains/regex/JSON-schema）、相似度（embeddings）、模型评分（`llm-rubric`,LLM 当裁判）。

## 依赖

- **运行时：** Node.js `^20.20.0 || >=22.22.0`（依 `engines`）。无需部署数据库——它用本地 libsql/SQLite 文件存评测历史。
- **安装：** `npm install -g promptfoo`、`brew install promptfoo`，或用 `npx promptfoo@latest` 零安装运行；另有 `pip install promptfoo` 包装（底层仍需 Node）。[推断]
- **外部服务：** 你要评测的 LLM provider——你自备 API key（OpenAI/Anthropic/Azure/Bedrock/Google/Ollama 等）；本地模型经 Ollama 需自带运行时。
- **可选：** 相似度断言需要 embeddings provider；只有选用托管分享/团队功能时才需要云账号。

## 运维难度

**低。** 核心循环基本无需运维：安装或 `npx`、写一份 YAML、配好 provider 环境变量、跑 `eval` 和 `view`。状态是一个本地文件，Web UI 是一个按需启动的内置 Express 服务，CI 用法就是在 job 里跑同一条 CLI。难度升到**低到中**仅在于：为团队自托管分享、在 CI 里管理大量 provider 凭据/限流，或维护庞大的红队配置——而你的评测成本会变成真实的 provider API 花费，这才是要盯的，而非基础设施。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 83.0 小时，基于 33 个 qualifying issues/PRs。
- **维护——非常活跃（截至 2026-06）。** 仓库 2026-06 有推送；发版节奏快（包约 0.121.x，2026-06-16 观测到 0.121.17）。版本号上仍处 1.0 之前，但持续在发版，并非原地踏步。未归档。[未验证]
- **治理与背书——单一厂商（Promptfoo）。** 由商业版 Promptfoo 背后的公司以 Organization 持有；路线图由厂商掌控，而非基金会治理。这个开源 CLI 是一家创投型公司的核心资产，对推进势头是利好，但也把存续绑在了公司的商业走向上。[推断]
- **年龄与 Lindy——中等，但在本品类里算耐久。** 创建于 2023-04，约 3 年且持续活跃——是较早、采用度较高的开源 LLM 评测工具之一，已经熬过了「周末写个评测脚本」那一波。绝对意义上仍年轻，但在这个快速变动的细分里是合理的 Lindy 选择。[推断]
- **采用与生态。** 约 22k star，provider 覆盖广，有 CI 集成和 code-scan action；README 里「被 OpenAI/Anthropic 使用、1000 万+ 用户」是厂商营销，未经独立证实。就项目规模而言文档尚可，issue tracker 活跃（约 361 个未决）。
- **风险标记——open-core。** MIT 下 local-first 的开源 CLI，受治理/带 SLA 的平台（托管看板、RBAC、趋势历史）留给商业档——若你的需求漂向团队治理，就要盯这条常见的 open-core 分界线。此处不断言重新授权或显著 CVE 历史。

## 存疑（未验证）

- [未验证] 观测到 `promptfoo` 包最新版本为 0.121.17，发布于 2026-06-16（独立的 `code-scan-action` 单独发版，如 0.1.8）。发版节奏快，pin 之前请重新核实。
- [未验证] 截至 2026-06 star 约 22.6k——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] README 称其“为服务 1000 万+ 生产用户的 LLM 应用提供支撑”，并“被 OpenAI 和 Anthropic 使用”——这些是项目自身的营销表述，本页未独立证实。
- [推断] `pip install promptfoo` 这条路是 Node 包的薄包装；真正的引擎和 `engines` 约束都是 Node——若纯 Python 部署很关键，请对照当前文档确认。
- [推断] 具体红队攻击类别（OWASP-LLM 覆盖、越狱/PII 插件）和支持的 provider 列表随版本变动；依赖某具体攻击或 provider 前请核对当前文档。
- [未验证] 许可证依仓库元数据读作 MIT；对比表（DeepEval/Langfuse/LangSmith/Braintrust/Garak/Giskard 的定位）是基于通用认知的判断，非逐项实测对比。
