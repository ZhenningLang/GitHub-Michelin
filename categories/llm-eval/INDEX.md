# llm-eval

> Category node. Test, benchmark, and security-scan (red-team) prompts, agents, and RAG systems.
> Split into sub-categories by **what is under test**: your own LLM app's quality over time, the security and governance posture of a model, agent or AI stack, or a fixed public task set used to rank models, agents or harnesses against each other.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories

| Sub-category | Enter when | Route |
| --- | --- | --- |
| **App Evals** | You change prompts, retrieval or models in your own LLM app and need regression tests, RAG scores, or production traces and prompt versions to see what broke. | [→](app-evals/INDEX.md) |
| **Security Audits** | Before launch or review you must show a model, agent or AI stack resists known attacks and stays inside its declared roles and permissions. | [→](security-audits/INDEX.md) |
| **Benchmarks** | You need to compare models, agents or harnesses on a fixed public task set or corpus, not test your own app. | [→](benchmarks/INDEX.md) |

## Comparison matrix

| Option | Type | One-line tradeoff |
| --- | --- | --- |
| [App Evals](app-evals/INDEX.md) | Sub-category | promptfoo, DeepEval, Ragas, Giskard, Langfuse, Pezzo — tests and traces you author for your own app; scores come from LLM judges you pay for and that wobble. |
| [Security Audits](security-audits/INDEX.md) | Sub-category | garak, AI-Infra-Guard, iFixAi — fixed attack or governance catalogs against a model, agent or whole stack; they audit posture, not your app's answer quality. |
| [Benchmarks](benchmarks/INDEX.md) | Sub-category | SWE-bench, Harvey LAB, g-harness-evals, HC3 — ready-made task sets and grading for ranking; heavy to run and only as good as their task mix. |

## What belongs here

Tools whose primary job is to **evaluate, benchmark, or red-team** LLM prompts/agents/RAG. Not code review (see `ai-code-review`), not training (see `llm-training`). Pick a sub-category by what you are testing: your own app (`app-evals`), whether it can be attacked or breaks its rules (`security-audits`), or how it ranks on a shared task set (`benchmarks`).
