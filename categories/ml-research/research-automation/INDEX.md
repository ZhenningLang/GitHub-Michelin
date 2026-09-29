# research-automation

> Category node. Pipelines and harnesses that automate the research loop itself — an agent proposes, runs and scores experiments (or whole papers).
> ← back to [ml-research](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **autoresearch** | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. | B (4/6) | [→](autoresearch.md) |
| **The AI Scientist** | Use it when you want the fully automatic idea-to-paper loop — idea generation, novelty check, experiment code, plots and a compiled LaTeX paper with an LLM review — but accept a template-bound pipeline that has been frozen since the licence changed and now constrains publishing its output. | D (4/6) | [→](ai-scientist.md) |
| **Agent Laboratory** | Use it when you want role-played LLM agents to run literature review → plan → experiments → report with per-phase human approval, MIT terms and resumable checkpoints — but it has had no code change since 2025-03 and carries an unanswered security disclosure. | C (3/6) | [→](agent-laboratory.md) |
| **RRSI** | Use it when you want to reproduce or adapt automated agent-harness search with anti-overfitting brakes (bounded tagged edits, a leakage critic, a noise floor, a token-cost rule) — but the search roles are hard-wired to Claude on Vertex AI and a run costs thousands of full benchmark episodes. | C (5/6) | [→](rrsi.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [autoresearch](autoresearch.md) | ✅ | B (4/6) | Self-contained single-GPU LLM training harness so an AI agent can iterate on train.py overnight — 5-minute experiments scored by validation bits-per-byte, keeping only loss-lowering changes. |
| [The AI Scientist](ai-scientist.md) | ✅ | D (4/6) | Use it when you want the fully automatic idea-to-paper loop — idea generation, novelty check, experiment code, plots and a compiled LaTeX paper with an LLM review — but accept a template-bound pipeline that has been frozen since the licence changed and now constrains publishing its output. |
| [Agent Laboratory](agent-laboratory.md) | ✅ | C (3/6) | Use it when you want role-played LLM agents to run literature review → plan → experiments → report with per-phase human approval, MIT terms and resumable checkpoints — but it has had no code change since 2025-03 and carries an unanswered security disclosure. |
| [RRSI](rrsi.md) | ✅ | C (5/6) | Use it when you want to reproduce or adapt automated agent-harness search with anti-overfitting brakes (bounded tagged edits, a leakage critic, a noise floor, a token-cost rule) — but the search roles are hard-wired to Claude on Vertex AI and a run costs thousands of full benchmark episodes. |

## What belongs here

Repositories whose job is to **automate the research loop itself**: LLM agents that propose changes or ideas, run the experiments, score them against a metric or a reviewer, and keep what wins — idea-to-paper pipelines ([The AI Scientist](ai-scientist.md), [Agent Laboratory](agent-laboratory.md)), an overnight single-GPU training-loop harness ([autoresearch](autoresearch.md)), and agent-harness search ([RRSI](rrsi.md)). Not interactive research assistants where a human drives (see `deep-research`), not general coding-agent orchestrators (see `agent-frameworks`), not training frameworks (see `llm-training`).
