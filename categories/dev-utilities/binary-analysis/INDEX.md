# binary-analysis

> Category node. Binary inspection, reverse-engineering evidence, and candidate source reconstruction for authorized analysis.
> ← back to [dev-utilities](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **ReAgent** | Rebuild authorized C/C++ functions from Ghidra evidence with model review and your candidate tests; no equivalence proof. | C (5/6) | [→](reagent.md) |
| **Ghidra** | Understand authorized native binaries through linked instructions, C-like functions and persistent annotations; raw firmware still needs processor context. | A (6/6) | [→](ghidra.md) |
| **REA** | Inspect authorized source-unavailable apps through an agent, with local tools and evidence; native engines remain separate. | B (5/6) | [→](rea.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [ReAgent](reagent.md) | ✅ | C (5/6) | Candidate reconstruction and bounded repair with explicit validation policy; costs Ghidra setup, model calls and project-owned tests. |
| [Ghidra](ghidra.md) | ✅ | A (6/6) | Integrated native analysis and annotation workspace, at the cost of Java/native setup and human validation of inferred functions. |
| [REA](rea.md) | ✅ | B (5/6) | Agent-facing evidence across native and Electron targets, at the cost of runtime and engine integration. |

## What belongs here

Tools for inspecting source-unavailable programs, collecting reverse-engineering evidence, or rebuilding candidate source from binary analysis. General data transforms, compression, and search utilities belong in [Data Tools](../data-tools/INDEX.md).
