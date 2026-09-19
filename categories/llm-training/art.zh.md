---
name: ART (Agent Reinforcement Trainer)
slug: art
repo: https://github.com/OpenPipe/ART
category: llm-training
tags: [rl, grpo, agents, multi-step, lora, vllm, unsloth, reward-modeling, llm-as-judge]
language: Python
license: Apache-2.0
maturity: v0.5.x, active (2026-03 latest release seen; 2026-06)
last_verified: 2026-06-26
type: framework
upstream:
  pushed_at: 2026-06-29T01:04:19Z
  default_branch: main
  default_branch_sha: b2347d248320b4560641ea1ab6a10520f6a68477
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:43:29Z
  overall: B
  overall_score: 2.6
  scored_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 2
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 129.2
        qualifying_issues: 8
        band: default
        window_offset_days: 10
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 480
        last_commit_age_days: 2
        cohort: framework
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 21
        top1_share: 0.344
        top3_share: 0.738
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: true
        content_license: null
  unknowns:
    adoption: { reason: ambiguous }
---

# ART (Agent Reinforcement Trainer)

ART 是 OpenPipe 开源的框架，用 GRPO 强化学习在真实任务上训练多步 LLM agent；它把客户端-服务端训练循环与 RULER（一个无需标注数据、由 LLM 充当裁判的奖励函数）配在一起。

![art — 健康度雷达](../../assets/health/llm-training-art.zh.svg)

## 何时使用

你是一名工程师，已经搭好了一个多步 agent——比如一个邮件检索 agent，它会发起多次工具调用、读取结果、再决定下一步——但靠改 prompt、换更大的底座模型已经到了天花板。这个 agent 对得够多到能演示，却不够可靠到能上线：它会选错检索方式、过早放弃，或者在证据本可检索到时硬编一个答案。你手里没有一份标注好的「正确轨迹」数据集，而为每一种失败模式手写奖励函数本身又是一个项目。

ART 正是为这种场景而生。你把 agent 代码继续留在 Python 里，把它的模型调用经由 ART 的 OpenAI 兼容客户端路由；ART 会把每一次 rollout 记录成一条 *轨迹*（完整的多轮消息序列）。它不强迫你写奖励函数，而是由 RULER（Relative Universal LLM-Elicited Rewards）为每个任务生成多条轨迹，再用 LLM 充当裁判对它们做 *相对排序*——由于 GRPO 只需要相对分数，这个信号就够用。随后服务端跑 GRPO（基于 Unsloth/vLLM，用 LoRA）产出新的适配器，热加载回 vLLM，循环往复直到 agent 收敛。OpenPipe 自家的 ART·E 演示称一个 Qwen 2.5 14B 邮件 agent 在其任务上达到甚至超过某个大得多的闭源模型 [未验证——厂商基准]。由于客户端可以跑在你的笔记本上、训练发生在 GPU 机器（本地或临时/托管 GPU 环境），你能拿到「边干边学」的 RL，而不必自建训练集群。

## 何时不用

- **你只需要 SFT / 指令微调。** ART 是面向 *agentic、多步* 任务的 RL 框架。如果你只想在静态数据集上做监督微调，[LLaMA-Factory](llamafactory.zh.md) 或 [Unsloth](unsloth.zh.md) 更合适（而且 ART 本来就构建在 Unsloth 之上）。
- **你没有可用的奖励信号或任务环境。** GRPO 需要大量可被打分的 rollout。如果你的任务无法反复执行并被评判（哪怕由 LLM 来评），RL 帮不了你，得先有一个可评估的环境。
- **你承担不起裁判成本。** RULER 对每组轨迹都要调用 LLM 裁判。大规模训练时这笔 API 成本是实打实的；文档建议用更便宜的裁判模型（如 Qwen3 32B）来缓解 [未验证]。
- **你需要某个不被支持的特定模型。** ART 面向 Unsloth 支持的 vLLM/HF-transformers 因果语言模型；Gemma 3 被明确列为不支持。超出这个范围的情况都不确定。
- **你想要开箱即用、无需 GPU 的产品。** 无服务器/托管路径降低了运维，但核心流程仍假设有 GPU 训练、且 agent 要你自己埋点。如果重度依赖 OpenPipe/W&B 托管方案，还存在锁定风险。
- **你需要一套冻结、保守的依赖栈。** 它依托快速演进的栈（vLLM、Unsloth、TRL、torchtune）并频繁发版；上游变动带来的破坏是需要考虑的维护成本 [推断]。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Unsloth](unsloth.zh.md) | ✅ | 需求是更快的单卡 LoRA／SFT 或单轮 GRPO，而不是多步 agent rollout 循环时，选 Unsloth。 | Unsloth 是 ART 底层使用的训练效率层；ART 额外加入 agentic GRPO 与 RULER 奖励编排。 |
| [agent-lightning](agent-lightning.zh.md) | ✅ | 给现有 agent 做最小代码改动的 RL 比 ART 内置 RULER 奖励路径更重要时，选 agent-lightning。 | 它是概念上最接近的同类：都从执行中训练 agent，但集成方式和奖励工具不同。 |
| [LLaMA-Factory](llamafactory.zh.md) | ✅ | 想通过配置和 UI 工作流覆盖广泛模型的 SFT/DPO/PPO 微调时，选 LLaMA-Factory。 | 通用微调广度更强；在 ART 专精的已部署多步 agent rollout 循环上更弱。 |
| HF TRL | 未收录 | 想要底层 GRPO/PPO/DPO trainer，且能自己接 agent rollout 循环时，选 HF TRL。 | 控制力和通用性更强，但奖励、推理服务和编排都要自己拼。 |
| [verl](verl.zh.md) | ✅ | 大规模训练下的高吞吐分布式 RLHF/RL 是主需求时，选 verl。 | 扩展性更强但运维更重，也不聚焦单工程师给 agent 埋点的易用性。 |
| [torchtune](torchtune.zh.md) | ✅ | PyTorch 原生微调／RL 配方已经足够，完整 agent-RL 框架反而过重时，选 torchtune。 | 它是这个生态里的构件，而不是完整的 agent-rollout 训练框架。 |

## 技术栈

- **语言/运行时：** Python（PyPI 包 `openpipe-art`）。
- **算法：** GRPO（Group Relative Policy Optimization）。
- **奖励：** RULER——LLM 充当裁判，对每个任务的多条轨迹做相对排序/0–1 打分；无需标注数据。
- **训练/推理：** Unsloth + LoRA 做微调；vLLM 服务当前适配器；底层栈含 TRL 与 torchtune。
- **架构：** 客户端-服务端。客户端暴露 OpenAI 兼容接口并记录轨迹；GPU 服务端跑推理 + GRPO 训练，并把新的 LoRA 适配器热切换进 vLLM。
- **集成：** LangGraph、MCP 服务器（MCP·RL）、W&B（托管/无服务器训练）、Langfuse 与 OpenPipe 做可观测。

## 依赖

- 核心 ML：PyTorch、transformers、PEFT（LoRA）。
- 训练/服务：Unsloth、vLLM、TRL、torchtune。
- 一个供 RULER 使用的裁判 LLM（可以是更便宜的托管/本地模型）。
- 训练服务端的 GPU（本地、云端，或经由 W&B 路径的托管/临时 GPU）。
- 模型：多数 Unsloth 支持的 vLLM/HF-transformers 因果语言模型（Qwen、Llama、GPT-OSS 等）；不支持 Gemma 3。

## 运维难度

**中 → 高。** 概念模型（客户端记录轨迹、服务端训练、适配器热重载）很干净，托管/无服务器的 W&B 路径能把基础设施从你身上卸掉。但自托管意味着要运维一台 GPU 训练机外加一套快速演进的 vLLM/Unsloth/TRL 栈、要给自己的 agent 和任务环境埋点，还要管理 RULER 裁判的成本与可靠性（组太小会导致排序不稳定；生产中建议开 `swallow_exceptions=True`）。这比一次性的 SFT 作业要重不少。

## 健康度与可持续性

- **响应速度**：Grade B——中位首次响应时间 129.2 小时，基于 8 个 qualifying issues/PRs。
- **维护——活跃（截至 2026-06）。** 仓库 2026-06 有推送；最新 release v0.5.17 据称 2026-03-13，在一套快速演进的栈上频繁发版。处于 1.0 之前，预期会有 API 变动，以及来自上游（vLLM/Unsloth/TRL/torchtune）churn 的破坏。未归档。[未验证]
- **治理与背书——单一厂商（OpenPipe）。** 由 OpenPipe 以 Organization 持有，这是一家创投型公司，其托管/无服务器 RL 方案（与 W&B 配合）是变现路径。路线图与 RULER 奖励工具由厂商驱动；存续绑在 OpenPipe 的商业走向上，重度依赖托管路径还有锁定风险。[推断]
- **年龄与 Lindy——年轻 / 未经检验。** 创建于 2025-03，约 1 年。尚无 Lindy 履历；这是对 agent-RL 走向主流、以及 OpenPipe 持续投入的早期押注，而非押在耐久性上。
- **采用与生态。** 约 10k star，有若干集成（LangGraph、MCP·RL、W&B、Langfuse）；招牌的 ART·E「击败 o3」与「便宜 40% / 快 28%」是 OpenPipe 自家的基准/营销，未经独立证实。构建在 Unsloth/vLLM/TRL/torchtune 之上，因此既继承了该生态的覆盖面，也继承了它的不稳定。
- **风险标记——厂商锁定 + 快变依赖。** Apache-2.0，不断言重新授权/CVE 历史。真正的标记：朝 OpenPipe/W&B 的托管路径锁定、快速上游栈带来的破坏，以及 v0.x 的 API churn。

## 存疑（未验证）

- ART·E「在邮件检索上击败 o3」是 OpenPipe 在自家任务上发布的基准——视作 [未验证] 厂商声明。
- 「成本降 40% / 训练快 28%」出自 OpenPipe/W&B 对托管路径的市场宣传 [未验证]。
- 该生态的 star/fork 数不可靠；某次（约 2026-10 风格）快照显示约 1 万 star / 约 900 fork，最新版本 v0.5.17（2026-03-13）[未验证]，以抓取时为准。
- 确切的最低 GPU/显存要求文档未明确说明 [未验证]。
