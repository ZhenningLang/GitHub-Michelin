# model-editing

> Category node. Change what a model does by editing its saved weights — abliteration and related model surgery — instead of training it.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Heretic** | Use it when an aligned open model refuses prompts that are legitimate for your work, and you want the refusal direction ablated out automatically with a measured quality tradeoff — one GPU, no training data, AGPL tooling. | B (6/6) | [→](heretic.md) |
| **Remove Refusals with Transformers** | Use it when you want the shortest readable pure-`transformers` recipe for refusal removal — two Apache-2.0 scripts to read and adapt, with no optimizer, export or maintenance. | C (5/6) | [→](remove-refusals-with-transformers.md) |
| **abliterator** | Use it when you want to script and inspect abliteration yourself against TransformerLens hooks — activation caching, direction scoring, weight patching — accepting a repo dormant since 2024-06. | D (4/6) | [→](abliterator.md) |
| **ErisForge** | Use it when you want a pip-installable library that can ablate *or add* a behavior direction on chosen decoder layers, score refusals and save the model — accepting a single-maintainer project with no `LICENSE` file. | "?" (2/6) | [→](erisforge.md) |
| **deccp** | Use it only for its Chinese-censorship focus: a Qwen2 un-censoring PoC with a hand-checked dataset and writeup, explicitly unsupported by its author. | C (4/6) | [→](deccp.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Heretic](heretic.md) | ✅ | B (6/6) | Automatic abliteration of dense/MoE transformer models: ~200 Optuna trials balance refusal rate against KL divergence, then you pick a Pareto point and export; AGPL-3.0, single maintainer, needs a GPU. |
| [Remove Refusals with Transformers](remove-refusals-with-transformers.md) | ✅ | C (5/6) | The minimal Apache-2.0 pure-`transformers` reference: compute a refusal direction and orthogonalize the weights in two readable scripts; no optimizer, no export, idle since 2025-11. |
| [abliterator](abliterator.md) | ✅ | D (4/6) | TransformerLens-based library for scripted activation caching, per-hook refusal directions and weight patching; full control under MIT, but dormant since 2024-06 with no model export. |
| [ErisForge](erisforge.md) | ✅ | "?" (2/6) | pip-installable library to ablate or augment a behavior direction on chosen decoder layers, with refusal scoring and Hub save; single maintainer, no `LICENSE` file, older dependency pins. |
| [deccp](deccp.md) | ✅ | C (4/6) | Qwen2-specific Chinese-censorship un-alignment PoC with a curated dataset, eval scripts and a writeup; author-declared unsupported and dormant since 2025-04. |

## What belongs here

Tools that change a model's behavior or footprint by editing its saved weights — directional ablation (abliteration), weight merging, and quantization-based surgery. Not training or fine-tuning (see `llm-training`), and not inference runtimes or serving engines (see `llm-inference` / `on-device-ml`).
