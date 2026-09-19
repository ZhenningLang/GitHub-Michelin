# llm-training

> Category node. Fine-tune or reinforcement-train LLMs and multi-step agents.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **LlamaFactory** | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. | B (6/6) | [→](llamafactory.md) |
| **Unsloth** | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. | A (6/6) | [→](unsloth.md) |
| **ART (Agent Reinforcement Trainer)** | Train multi-step LLM agents on real tasks with GRPO reinforcement learning via a client-server loop, using RULER (LLM-as-judge) for zero-label reward generation. | B (5/6) | [→](art.md) |
| **Agent Lightning** | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. | B (5/6) | [→](agent-lightning.md) |
| **Colossal-AI** | Use it when you must train/fine-tune large models across many GPUs with tensor/pipeline/ZeRO parallelism — overkill for single-GPU LoRA. | B (5/6) | [→](colossalai.md) |
| **Hugging Face TRL** | Train transformer language models with reinforcement learning. | A (6/6) | [→](trl.md) |
| **torchtune** | PyTorch native post-training library | B (5/6) | [→](torchtune.md) |
| **Axolotl** | Go ahead and axolotl questions | B (6/6) | [→](axolotl.md) |
| **verl** | verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework | B (6/6) | [→](verl.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [LlamaFactory](llamafactory.md) | ✅ | B (6/6) | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. |
| [Unsloth](unsloth.md) | ✅ | A (6/6) | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. |
| [ART (Agent Reinforcement Trainer)](art.md) | ✅ | B (5/6) | Train multi-step LLM agents on real tasks with GRPO reinforcement learning via a client-server loop, using RULER (LLM-as-judge) for zero-label reward generation. |
| [Agent Lightning](agent-lightning.md) | ✅ | B (5/6) | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. |
| [Colossal-AI](colossalai.md) | ✅ | B (5/6) | Use it when you must train/fine-tune large models across many GPUs with tensor/pipeline/ZeRO parallelism — overkill for single-GPU LoRA. |
| axolotl / torchtune / HF TRL / verl | 未收录 | — | other fine-tuning / RL trainers named in the pages |

## What belongs here

Tools and frameworks whose primary job is to **train, fine-tune, or RL-optimize** LLMs or agents.
Not inference runtimes (see `on-device-ml`), not agent build/run frameworks (see `agent-frameworks`).
