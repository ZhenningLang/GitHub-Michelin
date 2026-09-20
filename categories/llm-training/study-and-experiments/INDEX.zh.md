# study-and-experiments

> 分类节点。LLM 训练的课程与从零参考实现——用来读、用来重跑、用来学会各阶段的学习材料，不是依赖。
> ← 返回[llm-training](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **MiniMind** | 当你想用约 3.2k 行手写 PyTorch 把 64M LLM 端到端训一遍（分词器、预训练、SFT、LoRA、MoE、DPO/GRPO 与 Tool Call RL），且接受产出是教学产物而不是可用模型时用它。 | A（5/6） | [→](minimind.zh.md) |
| **nanoGPT** | 当你要最经典的极简 GPT-2 训练参考（约 670 行可读代码、支持 MPS/CPU、checkpoint 与 OpenAI 的 GPT-2 权重互通），且接受它只到预训练、并已被上游宣布由 nanochat 取代时用它。 | C（4/6） | [→](nanogpt.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [MiniMind](minimind.zh.md) | ✅ | A（5/6） | 预训练→SFT→RL 整条链路手写且便宜到真的能跑一遍；但 64M 且中文优先意味着产不出可用模型，两次破坏性重构也意味着必须锁 commit。 |
| [nanoGPT](nanogpt.zh.md) | ✅ | C（4/6） | 读它来从「所有实现都被拿来对照的那份参考」学 GPT 训练，并能加载真实 GPT-2 权重；但它已废弃、单人维护、只有 DDP，且没有 SFT 与 RL。 |

## 什么该放这里

关于 LLM 训练的教学与研究产物：跟练课程、从零参考实现，其价值在可读的机制而不在产出的模型。可以读、可以重跑，不要依赖。框架、库与生产训练器放在父分类。
