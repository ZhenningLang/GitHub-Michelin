# llm-training

> Category node. Fine-tune or reinforcement-train LLMs and multi-step agents.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
|---|---|---|
| **Study & Experiments** | You want to learn how LLM training actually works by reading or re-running a from-scratch implementation, rather than adopting a trainer as a dependency. | [→](study-and-experiments/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **LlamaFactory** | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. | B (6/6) | [→](llamafactory.md) |
| **Unsloth** | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. | B (5/6) | [→](unsloth.md) |
| **ART (Agent Reinforcement Trainer)** | Train multi-step LLM agents on real tasks with GRPO reinforcement learning via a client-server loop, using RULER (LLM-as-judge) for zero-label reward generation. | C (5/6) | [→](art.md) |
| **Agent Lightning** | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. | B (5/6) | [→](agent-lightning.md) |
| **Colossal-AI** | Use it when you must train/fine-tune large models across many GPUs with tensor/pipeline/ZeRO parallelism — overkill for single-GPU LoRA. | B (6/6) | [→](colossalai.md) |
| **Hugging Face TRL** | Use it when your stack is already transformers + datasets + PEFT and you want SFT, DPO or GRPO as tested trainer classes you drive from Python — but multi-node RL on 70B+ or MoE models needs verl's rollout throughput. | A (6/6) | [→](trl.md) |
| **torchtune** | Use it when you keep an existing torchtune LoRA/QLoRA or DPO pipeline pinned at v0.6.1, or want to read fine-tuning methods written as plain-PyTorch training loops — but Meta stopped feature development in July 2025, so do not start new projects on it. | B (6/6) | [→](torchtune.md) |
| **Axolotl** | Use it when a team running repeated multi-GPU fine-tunes (LoRA, full, DPO) wants each run declared in one YAML file instead of hand-wired transformers, PEFT and DeepSpeed glue — but not for a single consumer GPU, a UI, or custom training loops. | B (6/6) | [→](axolotl.md) |
| **verl** | Use it when you run PPO, GRPO or DAPO on 7B–235B models across a GPU cluster and generation time dominates each step — but for SFT/DPO only, or one consumer GPU, it is far more setup than TRL or Unsloth. | B (6/6) | [→](verl.md) |
| **Soup** | Use it when one YAML must take a fine-tune from JSONL to a served, exported model and the base does not fit your GPU — not when the config contract must stay stable across upgrades or the model already fits resident and you want speed. | B (6/6) | [→](soup.md) |
| **Miles** | Use it when you RL-train a large MoE model on multi-node GPUs with SGLang rollout + Megatron training and need train/inference kept in step — not for single-GPU, SFT-only, vLLM-based stacks or a stable API. | B (5/6) | [→](miles.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [LlamaFactory](llamafactory.md) | ✅ | B (6/6) | Zero-code unified fine-tuning framework for 100+ LLMs/VLMs with a Gradio web UI (LlamaBoard), covering LoRA/QLoRA/full tuning and the full SFT→RLHF stack. |
| [Unsloth](unsloth.md) | ✅ | B (5/6) | Triton-kernel-accelerated single-GPU LoRA/QLoRA/RL fine-tuning that trains 500+ open LLMs ~2x faster with large VRAM savings. |
| [ART (Agent Reinforcement Trainer)](art.md) | ✅ | C (5/6) | Train multi-step LLM agents on real tasks with GRPO reinforcement learning via a client-server loop, using RULER (LLM-as-judge) for zero-label reward generation. |
| [Agent Lightning](agent-lightning.md) | ✅ | B (5/6) | Microsoft RL/optimization trainer that improves agents built in any framework (LangChain, AutoGen, OpenAI SDK…) with near-zero code changes by decoupling agent execution from the training backend. |
| [Colossal-AI](colossalai.md) | ✅ | B (6/6) | Use it when you must train/fine-tune large models across many GPUs with tensor/pipeline/ZeRO parallelism — overkill for single-GPU LoRA. |
| [Soup](soup.md) | ✅ | B (6/6) | Use it when one YAML must take a fine-tune from JSONL to a served, exported model and the base does not fit your GPU — not when the config contract must stay stable across upgrades or the model already fits resident and you want speed. |
| [Miles](miles.md) | ✅ | B (5/6) | Use it when you RL-train a large MoE model on multi-node GPUs with SGLang rollout + Megatron training and need train/inference kept in step — not for single-GPU, SFT-only, vLLM-based stacks or a stable API. |
| [Hugging Face TRL](trl.md) | ✅ | A (6/6) | The widest set of post-training methods behind one pip install and one Accelerate launch, paid for with a fast-moving API: biweekly releases, a rolling vLLM window, and patches that still fix silently wrong training. |
| [verl](verl.md) | ✅ | B (6/6) | Per-role GPU placement, vLLM/SGLang rollouts and FSDP/Megatron training buy real multi-node RL throughput; you pay with a Ray cluster, migrations every few minor releases, and pinning a version per recipe. |

## What belongs here

Tools and frameworks whose primary job is to **train, fine-tune, or RL-optimize** LLMs or agents.
Not inference runtimes (see `on-device-ml`), not agent build/run frameworks (see `agent-frameworks`).
Teaching material — courses and from-scratch reference implementations you read rather than depend on —
goes in **Study & Experiments**, not in the project table above.
