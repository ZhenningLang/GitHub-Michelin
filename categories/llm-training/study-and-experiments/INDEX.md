# study-and-experiments

> Category node. Courses and from-scratch reference implementations of LLM training — study material you read and re-run to learn the stages, not dependencies.
> ← back to [llm-training](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **MiniMind** | Use it when you want to train a 64M LLM end to end — tokenizer, pretrain, SFT, LoRA, MoE, DPO/GRPO and tool-call RL — in ~3.2k hand-written PyTorch lines you can read in an afternoon, and accept that the resulting model is a teaching artifact rather than a usable one. | A (5/6) | [→](minimind.md) |
| **nanoGPT** | Use it when you want the canonical minimal GPT-2 training reference — ~670 readable lines, MPS/CPU paths, checkpoints that interoperate with OpenAI's GPT-2 weights — and accept that it stops at pretraining and is deprecated upstream in favour of nanochat. | C (4/6) | [→](nanogpt.md) |
| **Train LLM From Scratch** | Use it when you want every alignment stage — SFT, reward model, DPO/ORPO/KTO, PPO, GRPO — hand-written in plain PyTorch on one small English GPT and scored on one GSM8K table, and accept GPU-only scripts with hard-coded `/ephemeral` paths and no usable model at the end. | A (4/6) | [→](train-llm-from-scratch.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [MiniMind](minimind.md) | ✅ | A (5/6) | The whole pretrain→SFT→RL chain hand-written and cheap enough to actually run; but 64M and Chinese-first means no usable output, and two breaking rewrites mean you pin a commit. |
| [nanoGPT](nanogpt.md) | ✅ | C (4/6) | Read it to learn GPT training from the reference everything else is measured against, and to load real GPT-2 weights; but it is deprecated, single-maintainer, DDP-only, and has no SFT or RL. |
| [Train LLM From Scratch](train-llm-from-scratch.md) | ✅ | A (4/6) | The broadest from-scratch alignment menu (reward model + PPO, DPO, GRPO) with zero `transformers`/`trl` imports; but a single, intermittently active maintainer, no releases or code CI, and paths written for the author's cloud box. |

## What belongs here

Teaching and study artifacts about LLM training: build-along courses and from-scratch reference implementations whose value is the readable mechanism, not the artifact they produce. Read and re-run them; do not depend on them. Frameworks, libraries and production trainers live in the parent category.
