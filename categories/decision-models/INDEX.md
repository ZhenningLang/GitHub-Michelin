# decision-models

> Category node. Small self-hosted models whose job is to turn one piece of text into typed, probability-bearing decisions (yes/no, pick-one, rate-on-a-scale) instead of free-form generation — with the training and serving code included.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Kev** | Use it when you want a self-hosted, fine-tunable model that answers typed questions (yes/no, choice, rating) about one text and returns calibrated probabilities — not a hosted decision API and not a from-scratch classifier. | C (5/6) | [→](kev.md) |
| **Simple Jev** | Use it when you already serve an open chat model and want the Jev-style typed-decision contract (`/v1/classifier`) without training a decision model — accepting the base model's judgement and uncalibrated confidence. | C (4/6) | [→](simple-jev.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Kev](kev.md) | ✅ | C (5/6) | 0.8B–9B Jev-style decision models (LoRA on Qwen3.5) served behind a TypeSafe-compatible `/v1/systemone` — self-hosted calibration and fine-tuning, weaker world knowledge than a frontier model. |
| [Simple Jev](simple-jev.md) | ✅ | C (4/6) | A server that turns any compatible open chat model into the same typed-decision API by reading answer-label logits from one shared prefill — no trained checkpoint, no published accuracy. |
| Jev · TypeSafe System One | 未收录 | — | Hosted decision model / decision API — the services Kev and Simple Jev reimplement locally; the hosted services are not repositories, so they are not indexed. |

## What belongs here

Models — and the training/serving stacks that ship with them — whose **primary job is a typed decision**: classify, rank, or score a text with probabilities you can threshold. Not chat or free-form generation; not schema-constrained tool calls (see `function-calling`); not general serving engines or runtimes (see `llm-inference` / `on-device-ml`); not training frameworks (see `llm-training`).
