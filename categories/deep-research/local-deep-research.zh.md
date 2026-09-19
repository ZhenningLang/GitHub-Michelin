---
name: Local Deep Research
slug: local-deep-research
repo: https://github.com/LearningCircuit/local-deep-research
category: deep-research
tags: [deep-research, local-llm, privacy, self-hosted, rag, searxng, ollama]
language: Python
license: MIT
maturity: v1.7.0, active (2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-06-29T04:11:02Z
  default_branch: main
  default_branch_sha: b7e588a2e9810978d0b5c28a5a8f15873570dff6
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:18:26Z
  overall: B
  overall_score: 2.67
  scored_axes: 6
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
        median_ttfr_hours: 21.9
        qualifying_issues: 13
        band: relaxed_solo
        window_offset_days: 1
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: local-deep-research
        dependent_repos_count: 0
        downloads_last_month: 10860
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
    longevity:
      grade: C
      raw:
        repo_age_days: 509
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 47
        top1_share: 0.906
        top3_share: 0.961
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Local Deep Research

一个可自托管的深度研究助手（Web UI + API + CLI），把整套“迭代检索—综合”的循环跑在你自己的机器上，可全程用本地 LLM 和本地 SearXNG 元搜索，数据无需离开你的网络。

![local-deep-research — 健康度雷达](../../assets/health/local-deep-research.zh.svg)

## 何时使用

你是某个组织里的工程师或分析师，研究问题会碰到敏感材料——内部文档、病历或法律记录、尚未公布的产品——把这些贴进任何托管的“深度研究”SaaS 都是不可接受的。但你仍想要真正的能力：一个能在大量来源间扇出、逐篇阅读、并写出带引用报告的 agent。Local Deep Research 把这套循环放进一个你完全掌控的容器里。把 LLM 指向 Ollama 或 LM Studio，搜索用内置的 SearXNG，整条流水线——查询规划、检索、综合、引用——都跑在你自己的硬件上，而且每个用户用 SQLCipher 加密存储，连机器的管理员都读不到你的会话。

如果你的研究偏*学术或技术*而非开放网络的杂项，你也很合适：LDR 自带 arXiv、PubMed、Semantic Scholar、Wikipedia、GitHub、Wayback Machine 的一流连接器，还有一个知识库模式，把来源下载并索引成可检索的私有库。你选一个深度——从 Quick Summary（亚分钟级）到完整 Report——并可从 Web UI、REST API、CLI 驱动，或作为 MCP server 让 Claude 等 agent 把它当研究工具调用。需要云端模型时，同一套接口也能对接 OpenAI / Anthropic / Gemini;“本地”是默认，而非唯一模式。

## 何时不用

- **没有 GPU 又想要纯本地的质量。** 那些亮眼的准确率数字假设你有一块能打的本地模型（比如 3090 上跑 27B）。在纯 CPU 机器上，本地模型做研究又慢又弱；你只能退回云端 API，而那正好破坏了隐私前提。
- **你要的是一个极小的可嵌入库，而不是一个应用。** LDR 是个完整应用（Web server、队列/分发器、加密 DB、JS 前端）。如果你只想要一个“传入 query、返回报告”的函数嵌进自己的服务，脚本式工具如 [deep-research](deep-research.zh.md) vendoring 进去轻得多。
- **你想要托管、零运维的现成产品。** 它生来就是自托管——Ollama、SearXNG、数据库和升级都要你自己跑、自己维护。没有可以注册的 SaaS。
- **1.0 前的接口面频繁变动。** 它在 v1.x 一路快速迭代，功能和安全改动一直很活跃（chat 模式、凭证泄露加固直到 v1.7.0 才落地）;API、配置项和 DB schema 可能逐版变化。[推断] 把 config/schema 当作尚未冻结，并 pin 一个版本。
- **对抗式事实核查才是核心任务。** LDR 会带引用地检索并综合，但它不是逐条断言的专用核验 harness；如果你的需求是“证实或证伪这些具体断言”，一个核验优先的流水线更合适。
- **你不信自报跑分。** ~95% SimpleQA / 77% xbench-DeepSearch 是项目自己在选定硬件/模型上得出的。[未验证] 别把它当作独立结论，也别当作对你的模型选择的预测。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [deep-research](deep-research.zh.md) | ✅ | 需要可嵌入、端到端自己掌控的极简 TypeScript 脚本时，选 deep-research。 | 极简 TypeScript 脚本，端到端自己嵌、自己掌控；LLM+搜索 key 你自己接。比 LDR 轻得多，但没有 UI、没有本地 LLM/隐私套件、没有学术源连接器或加密多用户存储。 |
| [Vane](vane.zh.md) | ✅ | 需要另一个自托管研究/搜索 agent 时，选 Vane。 | 另一个自托管研究/搜索 agent;“自己跑”的目标有重叠。按源连接器、本地 LLM 支持和报告质量在你的栈上比较。 |
| [Agent-Reach](agent-reach.zh.md) | ✅ | 交付物是 web/social 触达而非带引用报告时，选 Agent-Reach。 | 聚焦在面向 web 来源的 agent 触达/reach；相邻但交付物与 LDR 的带引用研究报告不同。 |
| [GPT Researcher](gpt-researcher.zh.md) | ✅ | 需要带 Web UI 和报告导出的流行 Python 深度研究 agent 时，选 GPT Researcher。 | 流行的 Python 深度研究 agent，带 Web UI 和报告导出；默认云端 LLM 优先。LDR 更彻底地押注全本地 + 加密 + 学术源连接器。 |
| Perplexity / OpenAI Deep Research | 未收录 | 质量和零运维高于隐私/本地控制时，选托管研究 SaaS。 | 托管 SaaS，质量强、零运维——但你的查询和上下文会离开你的机器，与 LDR 的前提正相反。 |

## 技术栈

- **语言：** Python 后端；JavaScript/Node 前端，用 Vite 构建。
- **编排：** LangChain 做 LLM 接线，LangGraph 实现那套自主 agent 策略——由它决定调用哪些引擎、何时综合。
- **LLM:** 本地走 Ollama / LM Studio / llama.cpp；云端走 OpenAI / Anthropic / Google，或任何讲 OpenAI chat-completions API 的服务。
- **搜索：** SearXNG 元搜索；arXiv、PubMed、Semantic Scholar、Wikipedia、GitHub、Wayback Machine 的专用连接器；付费 API(Google、Brave、Tavily、Serper)。
- **存储 / 检索：** SQLite + SQLCipher（AES-256）按用户加密；向量库经 LangChain(FAISS、Chroma、Pinecone)。
- **接口：** Web UI、REST API、CLI，以及一个 MCP server，让 agent 把它当研究工具调用。

## 依赖

- **运行时：** Python（README 写 3.8+，请对照当前 `pyproject` 核实）；支持 AVX 的 x86-64 或 ARM64 CPU。要让纯本地 LLM 研究可用，基本需要一块 CUDA GPU。
- **你需要自己跑的外部服务：** 一个 LLM 后端（Ollama/LM Studio/llama.cpp，或一个云端 API key）和一个搜索后端（内置 SearXNG，或付费搜索 API key）。Docker 镜像会帮你编排 Ollama + SearXNG。
- **可选：** 加密数据库用的 SQLCipher；知识库/RAG 功能用的向量库后端（FAISS/Chroma/Pinecone）。
- **安装：** `pip install local-deep-research`，然后 `python -m local_deep_research.web.app`；或 `docker run` / `docker-compose`（纯 CPU 或 NVIDIA-GPU），还附带 Unraid 模板。

## 运维难度

**中。** Docker/compose 路径让首次跑起来还算合理——它能把 Ollama 和 SearXNG 和应用一起拉起来。负担在后续：模型下载和 GPU 驱动要你管，一个会被搜索引擎限速或封禁的 SearXNG 实例要你维护，一个加密的 SQLCipher 数据库（零知识 / 无密码找回语义——丢了 key 就丢了数据），以及在一个快速变动的 1.0 前应用上跨版本升级（config 和 schema 可能变）。纯云端 LLM 模式更容易搭起来，但那就交换掉了你当初选 LDR 的隐私理由。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 21.9 小时，基于 13 个 qualifying issues/PRs。
- **维护（2026-06）：** **活跃**——最近 push 在 2026-06，按版本号推进 v1.x 线（安全加固直到 v1.7.0 才落地）。它有真实的 release 节奏，不像一次性 demo。[推断]
- **治理与 bus factor:** `User` 名下（`LearningCircuit`），约 8.6k star——社区式项目，没有基金会或厂商背书。bus-factor 压力低于爆红的单人仓库，但仍属小团队。[推断]
- **年龄与 Lindy（约 1 年，2025-02 创建）：** 年轻，尚无长期 Lindy 记录；缓和信号在于它是*年轻**且**在持续发版*，而非年轻且热炒后归于沉寂。请 pin 版本——它仍是 1.0 前形态，config/schema/API 会逐版变动。
- **采用/生态：** 接口面广（Web UI + REST + CLI + MCP server，20+ 搜索连接器），但亮眼的准确率数字是在选定硬件上自报的——采用广度是真的，跑分不独立。[未验证]

## 存疑（未验证）

- [未验证] 截至 2026-06 star 约 8.6k;GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 跑分（3090 上 Qwen3.6-27B 跑出 ~95% SimpleQA;77% xbench-DeepSearch）为自报，选定模型/硬件，本页未独立复现。
- [未验证] “20+ 搜索引擎”及具体连接器清单是项目自己的表述；依赖某具体来源前请对照当前仓库核实其支持。
- [推断] Python "3.8+" 来自 README；当前发版的真实下限可能更高——pin 之前查 `pyproject.toml`。
- [推断] 作为 1.0 前快速迭代的项目，config 项、REST API 形态和 DB schema 可能逐版变化；为可复现请 pin 一个版本。
- [未验证] 项目 license 报告为 MIT；第三方依赖据称均为宽松许可（MIT/Apache-2.0/BSD），但本页未逐一审计。
