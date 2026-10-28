# harness-evolution

> Category node. Evolve agent harnesses or external resources rather than train model weights.
> ← back to [workflow-builders](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Gear** | Evolve sealed agent resources with durable evaluations and a configured acceptance gate; research mode is not independent validation. | B (4/6) | [→](gear.md) |
| **PenguinHarness** | Version and evaluate harness changes with a fixed model and benchmark; training-score gains still need unseen-task checks. | B (6/6) | [→](penguin-harness.md) |
| **Hermit** | Compare evolution methods over external agent adapters; version feedback and state without changing model weights, but validate improvement separately. | C (6/6) | [→](hermit.md) |
| **Harness²** | Adapt a frozen-model agent's whole harness on the current task without ground-truth feedback; repeated probes cost extra, and finals-only adoption can regress. | C (5/6) | [→](harness2.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Gear](gear.md) | ✅ | B (4/6) | Runtime-enforced candidate evidence and budgets; requires native target adapters, credible scorers and isolated execution. |
| [PenguinHarness](penguin-harness.md) | ✅ | B (6/6) | Version and evaluate harness changes with a fixed model and benchmark; training-score gains still need unseen-task checks. |
| [Hermit](hermit.md) | ✅ | C (6/6) | Common adapter-training lifecycle and host export; structure checks are not performance gates, and sandbox support is platform-dependent. |
| [Harness²](harness2.md) | ✅ | C (5/6) | Recursive task-time harness editing and per-domain experience; no baseline-in-pool guarantee, and executor isolation is your responsibility. |

## What belongs here

Evolve agent harnesses or external resources rather than train model weights. Single-skill document optimization and general prompt compilation remain in the parent category.
