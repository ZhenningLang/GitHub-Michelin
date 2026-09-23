# social-simulation

> Category node. Simulate societies of LLM agents — social-media worlds, opinion-dynamics experiments, and rehearsal sandboxes that let simulated crowds react before real people do.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **MiroFish** | Packaged upload→simulate→report "swarm intelligence" prediction app: seed a document, get a prediction report and an interactive simulated world. | C (5/6) | [→](mirofish.md) |
| **OASIS** | CAMEL-AI's pip-installable social-media simulation framework (Twitter/Reddit-like, up to a claimed 1M agents) for code-first studies of information spread and polarization. | B (6/6) | [→](oasis.md) |
| **AgentSociety** | Tsinghua FIB-Lab's LLM-native social-science simulation platform with Ray distribution, experiment replay, and DuckDB tracing. | B (5/6) | [→](agentsociety.md) |
| **generative_agents** | The original 2023 Stanford "Smallville" research prototype (memory stream / reflection / planning) — study the founding architecture, don't build on it. | D (3/6) | [→](generative-agents.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [MiroFish](mirofish.md) | ✅ | C (5/6) | Finished product (upload→report) but AGPL-3.0 + Zep Cloud dependency + unvalidated prediction claims. |
| [OASIS](oasis.md) | ✅ | B (6/6) | Apache-2.0 engine with social-media feed fidelity and published cost model; you build the pipeline yourself. |
| [AgentSociety](agentsociety.md) | ✅ | B (5/6) | Research-grade replay/distribution for experiments; heavier stack, framework-only. |
| [generative_agents](generative-agents.md) | ✅ | D (3/6) | The field's founding reference, frozen since 2024-08; teaching/study value only. |

## What belongs here

Projects whose primary job is to **simulate societies of LLM agents** — social-media platforms, urban environments, or embodied worlds — to observe emergent collective behavior.
Not general agent build/run frameworks (see `agent-frameworks`), not deep-research pipelines (see `deep-research`), not single-agent memory (see `agent-memory`).
