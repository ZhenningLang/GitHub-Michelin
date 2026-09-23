---
name: oMLX
slug: omlx
repo: https://github.com/jundot/omlx
category: local-runtimes
tags: [llm-serving, inference-server, apple-silicon, mlx, kv-cache, openai-api, macos]
language: Python
license: Apache-2.0
maturity: "v0.4.4, active (2026-06); ~17.2k stars (API-verified count; adoption meaning unverified/suspicious — anomalous for a ~4-month single-maintainer repo), created 2026-02 (very young), owner=User"
last_verified: 2026-06-28
type: framework
upstream:
  pushed_at: 2026-06-29T07:11:17Z
  default_branch: main
  default_branch_sha: 60dcaf4ed6975fb1212f56744e234615f1d6f940
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:28:48Z
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 7.4
        qualifying_issues: 27
        band: default
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: null
        canonical_package: null
        release_downloads: 604296
        release_assets: 275
        release_tier: C
        signal_basis: releases
    longevity:
      grade: D
      raw:
        repo_age_days: 221
        last_commit_age_days: 0
        cohort: framework
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: empty_or_gated }
---

# oMLX

一个只跑在 Apple Silicon 上的 LLM 推理服务器（基于 Apple 的 MLX），带 continuous batching 和「热内存 + 冷 SSD」分层 KV 缓存，从 macOS 菜单栏管理——目标是让本地模型在 Claude Code 这类日常编码 agent 上真正可用。

![omlx — 健康度雷达](../../../assets/health/omlx.zh.svg)

## 何时使用

你是一名用 M 系列 Mac（M1/M2/M3/M4）的开发者，想跑本地 LLM 做真正的编码工作——把 Claude Code、OpenCode、Codex 或 Copilot 接到一个本地 OpenAI 兼容端点，而不是按 token 付费。你反复撞上的问题是：朴素的本地服务器每次请求都重算 KV 缓存，于是长上下文的编码会话慢如蜗牛，而你又不想守着一个终端。你装上 oMLX（一个 `.dmg` 应用或 `brew install omlx`），把它指向一个装满 MLX 模型的目录，它就在 `http://localhost:8000/v1` 上以 continuous batching 服务这些模型，并配一套**分层 KV 缓存**——热块留在内存、冷块卸载到 SSD（safetensors）；下次请求命中相同前缀时从磁盘恢复（哪怕服务器重启过），而不是从头重算。一个原生 Swift 菜单栏应用让你启停、pin 模型、设每模型 TTL、看吞吐，全程不用开终端。

当你想用一个 Mac 本地服务器同时承载文本 LLM、视觉语言模型（VLM）、OCR 模型、embedding 和 reranker 时也会选它，配 LRU 淘汰和内存上限，免得一台笔记本 OOM；还有一个 admin 面板做模型下载（从 HuggingFace）、每模型采样设置和一键 benchmark。它整个卖点就是「为单台 Mac 优化的本地 LLM 服务」，而不是集群级服务。

## 何时不用

- **你需要生产级、久经检验的服务——而这是一个非常年轻、单一维护者的项目。** 2026-02 创建（截至 2026-06 约 4 个月），由一位主导作者撑起，**未经证明**、track record 很薄。任何你必须依赖的场景，都该优先选成熟栈：**vLLM**、**TGI** 或 **[Modular MAX](../serving-engines/modular.zh.md)**。把 oMLX 当作「有潜力但很早期」。[推断]
- **你不在 Apple Silicon 上。** oMLX **仅限 macOS**、**仅限 Apple Silicon**（要求 macOS 15.0+ 和 M 系列芯片），基于 Apple 的 MLX。没有 Linux/NVIDIA/AMD 路径——服务器 GPU 请用 vLLM / TGI / TensorRT-LLM / MAX。
- **你要在集群 / 多节点规模上服务。** 这是单机、单 Mac 的服务器，带 LRU 模型淘汰和内存上限——不是横向扩展、多 GPU 机群、带自动扩缩的引擎。
- **SSD 卸载缓存的取舍你接受不了。** 从磁盘恢复 KV 块**在命中时**比重算快，但它带来 I/O 延迟和 SSD 磨损，且收益取决于前缀命中率；遇到冷的/全新的 prompt 你照样付正常 prefill。别把这个缓存当成免费的。
- **你无法独立核实它的宣称。** benchmark 和「分层缓存能扛重启」是项目自己的表述，而**一个约 4 个月仓库上的约 17k star 计数**——这个数字本身经 API 核实——是一个反常的人气信号，其采用度含义未经核实、可疑；在把工作流押上去之前，先验证它对你的模型确实有效。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Ollama](ollama.zh.md) | ✅ | 需要默认的跨平台本地 LLM 运行器和庞大模型库时，选 Ollama。 | 默认的 Mac/跨平台本地 LLM 运行器（基于 llama.cpp），生态和模型库极大；OS 支持更广，但没有 Apple-MLX 后端，缓存机制也比 oMLX 的热/冷分层 KV 缓存简单。 |
| LM Studio | 未收录 | 需要带 OpenAI 兼容服务器的精致桌面应用时，选 LM Studio。 | 打磨精良的本地模型桌面应用（Mac/Win/Linux），带 OpenAI 兼容服务器；GUI 闭源，不是 Apple-MLX 原生的开源服务器。 |
| mlx-lm（`mlx_lm.server`） | 未收录 | 需要 Apple 自家 MLX LLM 工具包和极简服务器时，选 mlx-lm。 | Apple 自家的 MLX LLM 工具包，带一个极简 OpenAI 兼容服务器——oMLX 正是**建在** mlx-lm 的 BatchGenerator 之上；mlx-lm 更底层，没有菜单栏应用、分层 SSD 缓存、多模型 LRU 和 admin 面板。 |
| [llama.cpp](llama-cpp.zh.md) | ✅ | 需要可移植的 C/C++ GGUF 推理引擎、并希望靠 Metal 跑 Mac 时，选 llama.cpp。 | 可移植的 C/C++ 推理引擎（GGUF），靠 Metal 也能在 Mac 上跑、到处都能跑；可移植性和成熟度都顶，但不是 MLX 原生，也没有内建的 macOS 菜单栏/admin 管理层。 |
| [vLLM](../serving-engines/vllm.zh.md) | ✅ | 需要事实标准的数据中心 LLM 服务引擎，而不是 Mac 本地服务器时，选 vLLM。 | 事实标准的数据中心 LLM 服务引擎（PagedAttention、continuous batching），社区庞大；偏 NVIDIA/Linux——不是 Mac/Apple Silicon 本地服务器。 |
| [Text Generation Inference (TGI)](../serving-engines/text-generation-inference.zh.md) | ✅ | 需要 Hugging Face 生产服务器、紧密 HF 集成和规模验证时，选 TGI。 | Hugging Face 的生产服务器，与 HF 贴合紧密、在规模上久经检验；面向服务器 GPU，不是 Mac 本地栈。 |
| [SGLang](../serving-engines/sglang.zh.md) | ✅ | 需要面向服务器 GPU 的高吞吐服务和 RadixAttention 前缀缓存时，选 SGLang。 | 高吞吐服务引擎，带 RadixAttention 前缀缓存；面向服务器 GPU、运维更复杂，不是单 Mac 菜单栏应用。 |
| [Modular Platform (MAX + Mojo)](../serving-engines/modular.zh.md) | ✅ | 需要服务器级跨厂商引擎和 Mojo kernel 语言时，选 Modular Platform。 | 厂商自建的跨厂商 GPU/CPU 服务引擎 + Mojo kernel 语言；一个大得多、服务器级、单一厂商的平台——与 Mac 本地服务器是不同的层和量级。 |
| [Ray Serve](../serving-engines/ray-serve.zh.md) | ✅ | 需要可扩展 Python 模型服务、多模型组合和自动扩缩容时，选 Ray Serve。 | 通用可扩展的 Python 模型服务框架，支持多模型组合和自动扩缩容；基于 Ray，运维要求高，不是 Mac 本地服务器。 |

## 技术栈

- **语言：** Python 3.10+（服务器/引擎）加一个原生 **Swift / SwiftUI** 菜单栏应用（明确**不是** Electron）。
- **推理后端：** Apple 的 **MLX**，经 **mlx-lm**；continuous batching 走 mlx-lm 的 `BatchGenerator`。
- **KV 缓存：** 块式、两层缓存（热 RAM + 冷 SSD，存为 **safetensors**），带前缀共享与 Copy-on-Write，自述「受 vLLM 启发」。
- **API：** `http://localhost:8000/v1` 上的 OpenAI 兼容 REST；内建 admin 面板（`/admin`）做监控、模型管理、chat、benchmark；可选 MCP 支持。
- **模型覆盖：** 文本 LLM、VLM、OCR 模型、embedding、reranker；面板内建 HuggingFace 模型下载器。

## 依赖

- **硬件/OS：** 一台 **Apple Silicon** Mac（M1/M2/M3/M4），跑 **macOS 15.0+（Sequoia）**——硬性要求，不支持其它平台。
- **运行时：** Python **3.10+**；可经预构建 `.dmg` 应用、Homebrew（`brew tap jundot/omlx`）或源码 `pip install -e .` 安装。可选 `[mcp]` extra 启用 Model Context Protocol。
- **模型：** 你自带 **MLX 格式**模型（如来自 HuggingFace）；面板可下载它们。
- **存储：** 冷 KV 缓存层（safetensors 块）需要 SSD 余量；RAM 是约束性资源（默认上限 = 系统 RAM − 8 GB）。[推断]

## 运维难度

**低（就其单 Mac 范围而言）。** 顺路径是 `.dmg` 拖拽安装或 `brew install omlx`，然后 `omlx start`（或 `brew services`），再把客户端指向 `localhost:8000/v1`；菜单栏应用负责启停、崩溃自动重启和 Sparkle 自动更新，admin 面板做模型下载和每模型设置且无需重启。没有集群、数据存储或 GPU 驱动机群要运维。真正的运维负担是本地、笔记本形态的：管理 RAM 压力和模型淘汰以免 OOM、调热/冷缓存和 SSD 用量，以及它是一个**年轻、快速演进的项目**（dev/rc tag、频繁发布），行为可能 release 间变动。没有多节点运维，因为根本没有多节点模式。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 6.0 小时，基于 19 个 qualifying issues/PRs。
- **维护（2026-06）。** 最后 push 于 2026-06-28；v0.4.4 于 2026-06-16 发布，rc/dev tag 频繁——**非常活跃**，不是吃老本。未归档。[推断]
- **治理 / bus factor（2026-06）——标记。** owner 是**单个 User 账号**（`jundot`），且提交历史由一位作者主导（约 1.2k commit），外部小贡献者是长尾。这是一个**单一维护者 / 高 bus-factor** 项目：作者一旦停手，项目很可能停滞。[推断]
- **年龄与 Lindy（2026-06）——Lindy 不通过。** 2026-02 创建（约 0.4 年）。**太年轻**，扛不起任何 Lindy 先验；不论多活跃，长期存活完全未经证明。用年龄 × 仍活跃来看：活跃是好事，但约 4 个月不算 track record。[推断]
- **采用度——可疑人气标记。** 一个约 4 个月、单一维护者的仓库上有约 17.2k star：这个计数经 API 核实，但其采用度含义是**反常的**——这种 star 增速与项目年龄、贡献者基数、约 624 个 open issue / 约 91 个 watcher 严重不成比例。把这个计数对采用/检验程度的含义当作 **[未验证]** 且可疑——可能是对 Mac 本地 LLM 服务器的真实爆火兴趣，也可能是可见度高峰——且**不要**把它读成生产就绪。[未验证]
- **许可证与背书。** Apache-2.0（经仓库 badge 和 GitHub API 确认）。没有背书组织或基金会；非正式资助（一个「Buy Me a Coffee」链接），这进一步放大 bus-factor 风险。尚无 relicense 历史（太年轻，还来不及有）。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06-28（经 GitHub API），约 17.2k star / 约 1.46k fork / 约 624 open issue / 约 91 watcher。star 计数本身经 API 核实，但其采用度含义对一个**约 4 个月的单一维护者仓库而言反常**，被标记为未经核实/可疑的人气信号——仅供参考，不作为采用度或质量证据。
- [未验证] 核心宣称——continuous batching、「热 RAM/冷 SSD 分层 KV 缓存能扛服务器重启」、前缀缓存命中收益、「受 vLLM 启发」的块管理，以及公开的 benchmark——都是项目自己的 README/官网表述，本页**未独立验证或跑 benchmark**。
- [未验证]「Claude Code 优化」（token 计数缩放、SSE keep-alive）和一键 agent 集成在 README 里有描述，但本页未对这些工具实测验证。
- [推断] SSD 卸载的延迟/磨损取舍和 RAM 上限默认值（系统 RAM − 8 GB）是从 README 描述推断的，非实测。
- [推断] Apple-Silicon-only / macOS-15+ / Python-3.10+ 要求取自 README 安装说明；精确的最小依赖集由仓库 `pyproject.toml` 在构建时决定，本页未逐条枚举。
- [推断] bus-factor 判断是从 owner 类型（User）和贡献者分布（一位主导作者）推断的，非来自某份治理文档的明文。
