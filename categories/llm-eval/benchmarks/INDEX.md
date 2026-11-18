# benchmarks

> Category node. Fixed public task sets, corpora and grading harnesses for ranking models, agents or harnesses against each other.
> ← back to [llm-eval](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus (HC3), detectors, and related AI-text detection resources. | E (4/6) | [→](chatgpt-comparison-detection.md) |
| **SWE-bench** | Use it when you need to grade coding-agent patches against real GitHub issues and their tests — each evaluation run needs Docker and a lot of disk. | B (6/6) | [→](swe-bench.md) |
| **Harvey LAB** | Use it when you need to benchmark an agent on long legal assignments — a synthetic case file in, a memo or markup out, graded by two LLM judges against a lawyer's checklist; needs Podman and both Anthropic and OpenAI keys. | B (6/6) | [→](harvey-labs.md) |
| **g-harness-evals** | Use it when you must pick an agent harness (Claude Code, Codex, OpenClaw, Hermes Agent, Pi) and want same-model, cost-per-solved-task rankings whose every number you can recheck keylessly — but it is one author's young, conflict-disclosed study on pinned versions and easy public tasks. | C (5/6) | [→](g-harness-evals.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [chatgpt-comparison-detection](chatgpt-comparison-detection.md) | ✅ | E (4/6) | Dataset/detector resources for AI-text comparison; use eval frameworks when you need a maintained test runner. |
| [g-harness-evals](g-harness-evals.md) | ✅ | C (5/6) | Fixed-model harness comparison ranked by paired cost per solved task with preregistration and receipts; pick SWE-bench to compare models, promptfoo to test your own app. |
| [Harvey LAB](harvey-labs.md) | ✅ | B (6/6) | Legal-agent benchmark with 1,600+ synthetic matter tasks and all-or-nothing LLM-judge grading; pick SWE-bench for coding agents or promptfoo for your own app's regression tests. |
| [SWE-bench](swe-bench.md) | ✅ | B (6/6) | Standardized real-GitHub-issue corpus graded by the repos' own tests; heavy Docker and disk per run, and it ranks models/agents rather than testing your app. |

## What belongs here

Repos whose primary asset is a **shared task set or corpus plus its grading**, used to compare systems: coding-issue benchmarks, domain-agent benchmarks, harness comparisons, AI-text detection corpora. Not tests you write for your own app (see `app-evals`), not security scans (see `security-audits`), not inference-speed benchmarks (see `llm-inference`).
