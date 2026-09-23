# de-ai-writing

> Leaf of [ai-writing](../INDEX.md). Humanizing AI text, removing AI tells, and enforcing human-sounding prose.
> ← up to [ai-writing](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Entries in this leaf

| Entry | Use when | Health | Page |
| --- | --- | --- | --- |
| **Humanizer-zh** | Chinese editor skill that de-slops existing prose while keeping facts, hedges, and author stance; 31 checkpoints, not an AI detector. | C (4/5) | [→](humanizer-zh.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | Chinese de-AI writing suite with `de-AI-writing` and `good-writing` SKILL folders; useful when author-style reconstruction is desired and license ambiguity is acceptable. | C (4/5) | [→](de-ai-prompt-enhancer-writer-booster-skill.md) |
| **shuorenhua** | Chinese-first de-AI rewrite skill with protected spans, scenario rules, multi-harness docs, and MIT licensing. | C (5/6) | [→](shuorenhua.md) |
| **ai-flavor-remover** | Single-file Chinese prompt snippet for removing AI flavor; author-tested only on Gemini 2.5 Pro, not an installable skill pack. | D (4/6) | [→](ai-flavor-remover.md) |
| **humanizer** | English upstream Claude Code skill for removing signs of AI-generated writing, with plugin/install docs and MIT licensing. | B (5/6) | [→](humanizer.md) |
| **stop-slop** | Compact English prose de-slop skill with hard rules and references; best for fast cleanup, not nuanced formal prose. | B (4/5) | [→](stop-slop.md) |
| **avoid-ai-writing** | English-first de-AI skill that ships a runnable zero-dependency npm detector, a CI/pre-commit gate on finding count, and a human-control corpus publishing its own false-positive rate. | B (5/6) | [→](avoid-ai-writing.md) |
| **no-ai-slop** | English editor skill whose first rule is preserving the writer's own voice; minimum effective edits against 20+ named AI patterns, an eval.md self-check loop, and a detect mode that quotes evidence instead of guessing authorship. | C (5/6) | [→](no-ai-slop.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Humanizer-zh](humanizer-zh.md) | ✅ | C (4/5) | Chinese editor brief: strip template prose, keep facts and hedges; Claude-first, not a detector. |
| [Baoyu Skills](../content-production/baoyu-skills.md) | ✅ | B (4/5) | Broader Chinese content/publishing bundle; Humanizer-zh is narrower and focused on de-AI rewriting. |
| Custom voice guide | 未收录 | — | Better for one private author or brand voice; less reusable than a public skill. |
| [De-AI-Prompt-Enhancer-Writer-Booster-SKILL](de-ai-prompt-enhancer-writer-booster-skill.md) | ✅ | C (4/5) | Heavier Chinese writer-booster workflow; useful for author-style reconstruction, risky when license clarity or neutrality matters. |
| [shuorenhua](shuorenhua.md) | ✅ | C (5/6) | Best current Chinese-first, fact-preserving de-AI skill when multi-harness reuse and protected spans matter. |
| [ai-flavor-remover](ai-flavor-remover.md) | ✅ | D (4/6) | Treat as a Gemini-tested prompt specimen, not as an OSS dependency or Agent Skills package. |
| [humanizer](humanizer.md) | ✅ | B (5/6) | Strong English upstream baseline with install docs; use Chinese-localized options for Chinese prose. |
| [stop-slop](stop-slop.md) | ✅ | B (4/5) | Shortest hard-rules English de-slop rubric; more likely to over-edit formal prose. |
| [avoid-ai-writing](avoid-ai-writing.md) | ✅ | B (5/6) | Most engineered English option: pick it when the de-AI pass must produce a CI-gateable finding count, not when you need a score to label authorship. |
| [no-ai-slop](no-ai-slop.md) | ✅ | C (5/6) | Voice-preservation-first editor skill with a detect mode that quotes evidence; pick it when the draft must still sound like its author after the pass. |


## What belongs here

Agent skills, prompt repos, or writing helpers whose primary job is to **remove AI writing tells**, humanize prose, preserve facts while changing voice, or enforce human-sounding editorial style.
