# llm-training

> 分类节点。微调或强化训练 LLM 与多步 agent。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
|---|---|---|
| **Study & Experiments** | 当你想通过读一遍或重跑一遍从零实现来搞懂 LLM 训练到底怎么做，而不是把某个训练器当作依赖引入时。 | [→](study-and-experiments/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **LlamaFactory** | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 | B（6/6） | [→](llamafactory.zh.md) |
| **Unsloth** | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 | A（6/6） | [→](unsloth.zh.md) |
| **ART (Agent Reinforcement Trainer)** | 通过客户端-服务端循环用 GRPO 强化学习训练多步 LLM agent，并用 RULER（LLM 充当裁判）实现零标注奖励生成。 | B（5/6） | [→](art.zh.md) |
| **Agent Lightning** | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 | B（5/6） | [→](agent-lightning.zh.md) |
| **Colossal-AI** | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 | B（5/6） | [→](colossalai.zh.md) |
| **Hugging Face TRL** | Train transformer language models with reinforcement learning. | A（6/6） | [→](trl.zh.md) |
| **torchtune** | PyTorch native post-training library | B（5/6） | [→](torchtune.zh.md) |
| **Axolotl** | Go ahead and axolotl questions | B（6/6） | [→](axolotl.zh.md) |
| **verl** | verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework | B（6/6） | [→](verl.zh.md) |
| **Soup** | 当一份 YAML 要把微调从 JSONL 一路带到可服务、可导出的模型，而底座装不进你的显卡时用它——当配置契约必须跨版本稳定、或模型本就装得下且要追求速度时不用。 | B（6/6） | [→](soup.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LlamaFactory](llamafactory.zh.md) | ✅ | B（6/6） | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 |
| [Unsloth](unsloth.zh.md) | ✅ | A（6/6） | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 |
| [ART (Agent Reinforcement Trainer)](art.zh.md) | ✅ | B（5/6） | 通过客户端-服务端循环用 GRPO 强化学习训练多步 LLM agent，并用 RULER（LLM 充当裁判）实现零标注奖励生成。 |
| [Agent Lightning](agent-lightning.zh.md) | ✅ | B（5/6） | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 |
| [Colossal-AI](colossalai.zh.md) | ✅ | B（5/6） | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 |
| [Soup](soup.zh.md) | ✅ | B（6/6） | 当一份 YAML 要把微调从 JSONL 一路带到可服务、可导出的模型，而底座装不进你的显卡时用它——当配置契约必须跨版本稳定、或模型本就装得下且要追求速度时不用。 |
| [Hugging Face TRL](trl.zh.md) | ✅ | A（6/6） | 接入 transformers 技术栈的 SFT / DPO / GRPO 训练器；管线本来就在 Hugging Face 生态里时优先选它。 |
| [verl](verl.zh.md) | ✅ | B（6/6） | 面向大规模 RL 后训练的框架（HybridFlow），核心是把 rollout 与训练分开；不是开箱即用的 SFT 训练器。 |

## 什么该放这里

主要职责是**训练、微调或 RL 优化** LLM 或 agent 的工具与框架。
不含推理运行时（见 `on-device-ml`），不含 agent 构建/运行框架（见 `agent-frameworks`）。
教学材料——可以读但不能依赖的课程与从零参考实现——放 **Study & Experiments**，不进上面的项目表。
