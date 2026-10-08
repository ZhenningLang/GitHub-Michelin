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
| **Unsloth** | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 | B（5/6） | [→](unsloth.zh.md) |
| **ART (Agent Reinforcement Trainer)** | 通过客户端-服务端循环用 GRPO 强化学习训练多步 LLM agent，并用 RULER（LLM 充当裁判）实现零标注奖励生成。 | C（5/6） | [→](art.zh.md) |
| **Agent Lightning** | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 | B（5/6） | [→](agent-lightning.zh.md) |
| **Colossal-AI** | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 | B（6/6） | [→](colossalai.zh.md) |
| **Hugging Face TRL** | 当你的技术栈本来就是 transformers + datasets + PEFT，想用 Python 调用经过测试的 SFT、DPO、GRPO 训练器类时用它——但在多机上对 70B 以上或 MoE 模型做 RL，生成吞吐得靠 verl。 | A（6/6） | [→](trl.zh.md) |
| **torchtune** | 当你要把现有的 torchtune LoRA/QLoRA 或 DPO 流水线锁在 v0.6.1 继续跑，或想读纯 PyTorch 写成的微调训练循环时用它——但 Meta 已于 2025 年 7 月停止功能开发，新项目不要拿它起步。 | B（6/6） | [→](torchtune.zh.md) |
| **Axolotl** | 当团队要反复在多张 GPU 上做微调（LoRA、全参、DPO），想把每次训练写进一个 YAML 而不是手拼 transformers、PEFT 和 DeepSpeed 胶水时用它——但单张消费级显卡、要界面或要写自定义训练循环时不适合。 | B（6/6） | [→](axolotl.zh.md) |
| **verl** | 当你要在 GPU 集群上对 7B 到 235B 的模型跑 PPO、GRPO 或 DAPO，且每一步都是生成耗时压过训练时用它——但只做 SFT/DPO 或只有一张消费级显卡时，它的搭建成本远高于 TRL 或 Unsloth。 | B（6/6） | [→](verl.zh.md) |
| **Soup** | 当一份 YAML 要把微调从 JSONL 一路带到可服务、可导出的模型，而底座装不进你的显卡时用它——当配置契约必须跨版本稳定、或模型本就装得下且要追求速度时不用。 | B（6/6） | [→](soup.zh.md) |
| **Miles** | 当你在多节点 GPU 上用 SGLang 生成、Megatron 训练去做大 MoE 模型的强化学习，并需要训推两侧保持一致时用它——单卡、只做 SFT、推理栈是 vLLM 或要求 API 稳定时不用。 | B（5/6） | [→](miles.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [LlamaFactory](llamafactory.zh.md) | ✅ | B（6/6） | 面向 100+ LLM/VLM 的零代码统一微调框架，自带 Gradio Web UI(LlamaBoard)，覆盖 LoRA/QLoRA/全量微调及 SFT→RLHF 全链路。 |
| [Unsloth](unsloth.zh.md) | ✅ | B（5/6） | 基于自定义 Triton kernel 的单卡 LoRA/QLoRA/RL 微调工具，号称在 500+ 开源 LLM 上约 2x 提速并大幅省显存。 |
| [ART (Agent Reinforcement Trainer)](art.zh.md) | ✅ | C（5/6） | 通过客户端-服务端循环用 GRPO 强化学习训练多步 LLM agent，并用 RULER（LLM 充当裁判）实现零标注奖励生成。 |
| [Agent Lightning](agent-lightning.zh.md) | ✅ | B（5/6） | 微软出品的强化学习/优化训练器，把 agent 执行与训练后端解耦，几乎零改动地优化任意框架（LangChain、AutoGen、OpenAI SDK 等）构建的 agent。 |
| [Colossal-AI](colossalai.zh.md) | ✅ | B（6/6） | 当你需要用张量/流水线/ZeRO 并行在多 GPU 上训练/微调大模型时用它——单卡 LoRA 用它是杀鸡用牛刀。 |
| [Soup](soup.zh.md) | ✅ | B（6/6） | 当一份 YAML 要把微调从 JSONL 一路带到可服务、可导出的模型，而底座装不进你的显卡时用它——当配置契约必须跨版本稳定、或模型本就装得下且要追求速度时不用。 |
| [Miles](miles.zh.md) | ✅ | B（5/6） | 当你在多节点 GPU 上用 SGLang 生成、Megatron 训练去做大 MoE 模型的强化学习，并需要训推两侧保持一致时用它——单卡、只做 SFT、推理栈是 vLLM 或要求 API 稳定时不用。 |
| [Hugging Face TRL](trl.zh.md) | ✅ | A（6/6） | 一句 pip install 加同一套 Accelerate 启动就拿到最广的后训练方法；代价是 API 变得快：两周一版，vLLM 支持是滚动窗口，补丁版本仍在修“训练悄悄出错”。 |
| [verl](verl.zh.md) | ✅ | B（6/6） | 按角色分配 GPU、生成走 vLLM/SGLang、训练走 FSDP/Megatron，换来真正的多机 RL 吞吐；代价是要搭 Ray 集群、小版本常带迁移，每个配方都得锁版本。 |

## 什么该放这里

主要职责是**训练、微调或 RL 优化** LLM 或 agent 的工具与框架。
不含推理运行时（见 `on-device-ml`），不含 agent 构建/运行框架（见 `agent-frameworks`）。
教学材料——可以读但不能依赖的课程与从零参考实现——放 **Study & Experiments**，不进上面的项目表。
