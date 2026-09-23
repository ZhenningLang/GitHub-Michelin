# model-editing

> Category node. Change what a model does by editing its saved weights — abliteration and related model surgery — instead of training it.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Heretic** | Use it when an aligned open model refuses prompts that are legitimate for your work, and you want the refusal direction ablated out automatically with a measured quality tradeoff — one GPU, no training data, AGPL tooling. | B (6/6) | [→](heretic.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Heretic](heretic.md) | ✅ | B (6/6) | Automatic abliteration of dense/MoE transformer models: ~200 Optuna trials balance refusal rate against KL divergence, then you pick a Pareto point and export; AGPL-3.0, single maintainer, needs a GPU. |

## What belongs here

Tools that change a model's behavior or footprint by editing its saved weights — directional ablation (abliteration), weight merging, and quantization-based surgery. Not training or fine-tuning (see `llm-training`), and not inference runtimes or serving engines (see `llm-inference` / `on-device-ml`).
