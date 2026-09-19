# study-and-experiments

> Category node. Courses and from-scratch reference implementations of LLM training — study material you read and re-run to learn the stages, not dependencies.
> ← back to [llm-training](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **MiniMind** | Use it when you want to train a 64M LLM end to end — tokenizer, pretrain, SFT, LoRA, MoE, DPO/GRPO and tool-call RL — in ~3.2k hand-written PyTorch lines you can read in an afternoon, and accept that the resulting model is a teaching artifact rather than a usable one. | A (5/6) | [→](minimind.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [MiniMind](minimind.md) | ✅ | A (5/6) | The whole pretrain→SFT→RL chain hand-written and cheap enough to actually run; but 64M and Chinese-first means no usable output, and two breaking rewrites mean you pin a commit. |

## What belongs here

Teaching and study artifacts about LLM training: build-along courses and from-scratch reference implementations whose value is the readable mechanism, not the artifact they produce. Read and re-run them; do not depend on them. Frameworks, libraries and production trainers live in the parent category.
