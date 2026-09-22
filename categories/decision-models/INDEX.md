# decision-models

> Category node. Small self-hosted models whose job is to turn one piece of text into typed, probability-bearing decisions (yes/no, pick-one, rate-on-a-scale) instead of free-form generation — with the training and serving code included.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Kev** | Use it when you want a self-hosted, fine-tunable model that answers typed questions (yes/no, choice, rating) about one text and returns calibrated probabilities — not a hosted decision API and not a from-scratch classifier. | C (4/6) | [→](kev.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Kev](kev.md) | ✅ | C (4/6) | 0.8B–9B Jev-style decision models (LoRA on Qwen3.5) served behind a TypeSafe-compatible `/v1/systemone` — self-hosted calibration and fine-tuning, weaker world knowledge than a frontier model. |
| Jev · TypeSafe System One | 未收录 | — | Hosted decision model / decision API — the services Kev reimplements locally; neither is a repository, so neither is indexed. |

## What belongs here

Models — and the training/serving stacks that ship with them — whose **primary job is a typed decision**: classify, rank, or score a text with probabilities you can threshold. Not chat or free-form generation; not schema-constrained tool calls (see `function-calling`); not general serving engines or runtimes (see `llm-inference` / `on-device-ml`); not training frameworks (see `llm-training`).
