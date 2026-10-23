# source-workflows

> Source-focused research workflows: reach platforms, rank community evidence, trace original passages, or audit citations.
> ← back to [deep-research](../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **imozuru** | Trace unfamiliar-field claims back to original passages in Claude Code; get checked extracts rather than a synthesized report. | C (4/5) | [→](imozuru.md) |
| **Agent-Reach** | Use it when your agent needs to read and search web plus social platforms without paid APIs. | B (5/6) | [→](agent-reach.md) |
| **Hyperresearch** | Use it when you're in Claude Code and need a high-stakes, citation-audited research report — a 16-step adversarial pipeline plus a persistent source vault; heavy on time and tokens, Claude-Code-only. | B (5/6) | [→](hyperresearch.md) |
| **last30days** | Use it when you want your agent to brief you on what Reddit, X, YouTube, HN and Polymarket said about a topic in the last 30 days, ranked by engagement — but it loads a ~258 KB skill prompt per call and leans on scraping and browser-session cookies. | B (6/6) | [→](last30days.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [imozuru](imozuru.md) | ✅ | C (4/5) | Original-source reading trail with quote matching; Japanese-first, ten days old, and not a network sandbox. |
| [Agent-Reach](agent-reach.md) | ✅ | B (5/6) | Platform access tools for your own workflow; no iterative synthesis or cited report. |
| [Hyperresearch](hyperresearch.md) | ✅ | B (5/6) | Claude-Code-locked 16-step research pipeline with adversarial critics, cite-checking, and a persistent vault; pre-1.0 churn and its leaderboard claim is a self-run projection. |
| [last30days](last30days.md) | ✅ | B (6/6) | Slash-command skill that fuses 30 days of Reddit/X/YouTube/HN/Polymarket signal into one cited brief; young, hyped, context-heavy, and dependent on scraping. |

## What belongs here

Choose this branch when **source access, evidence selection, or verification** decides the workflow: reading platforms your agent cannot reach, ranking recent community reactions, tracing a claim to original passages, or auditing citations against a reusable source vault. These tools work within an existing agent host; their outputs differ, from raw content to checked extracts and audited reports. A report output alone does not exclude Hyperresearch: its deciding tradeoff is the source-auditing workflow, not a standalone research runtime.

Stay in the [parent category](../INDEX.md) when choosing a research engine, application, model-backed runtime, or scientific workbench to plan and execute the overall investigation. This split follows the task capability, not implementation language or project name. Single-source crawl infrastructure belongs in [web-scraping](../../web-scraping/INDEX.md), not here.
