# behavior-overlays

> Category node. Change an agent's response style, code-writing habits or the context it reads, without adopting a general engineering workflow or domain-knowledge pack.
> ← up to [engineering](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this category

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **caveman** | Brevity skill plus optional local proxy: shrinks what a coding agent says and, if wrapped, what it reads, while leaving code, commands, and errors intact. | D (6/6) | [→](caveman.md) |
| **i-have-adhd** | A 10-rule response-style skill that makes a coding agent lead with the action, number steps, restate progress every turn, and drop the preamble and closer — one ruleset across roughly 15 harnesses. | A (4/5) | [→](i-have-adhd.md) |
| **Ponytail** | An always-on "lazy senior dev" ruleset: the coding agent maps what the change must reach, then takes the first rung that works (skip → reuse → stdlib → installed dep → one line) and returns the smallest complete diff, ending each reply with what it skipped. Lifecycle hooks, a session-start codebase map, review/audit commands, ~20 harness adapters. | B (5/6) | [→](ponytail.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [caveman](caveman.md) | ✅ | D (6/6) | Token-spend overlay: MIT skill shortens replies; optional BSL proxy shrinks logs/JSON/diffs the agent rereads. |
| [i-have-adhd](i-have-adhd.md) | ✅ | A (4/5) | Overlay for a reader with a short working memory; shapes how the agent talks, not what it knows — pick caveman when token spend is the problem. |
| [Ponytail](ponytail.md) | ✅ | B (5/6) | The code-side shrinker: forces the smallest complete change via a reuse-first ladder, with intensity levels and a model-run review/audit; pick caveman/i-have-adhd when the fat thing to cut is prose, not code. |

## What belongs here

Behavior and context overlays for an existing coding-agent setup: response shape, brevity, reuse-first code-writing rules and optional compression of what the agent reads. General engineering workflows and software-domain guidance remain in [engineering](../INDEX.md); scientific methods belong in [scientific-workflows](../scientific-workflows/INDEX.md).
