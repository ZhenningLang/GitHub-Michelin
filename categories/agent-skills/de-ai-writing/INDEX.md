# de-ai-writing

> Leaf of [agent-skills](../INDEX.md). Humanizing AI text, removing AI tells, and enforcing human-sounding prose.
> ← up to [agent-skills](../INDEX.md) · root [route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Entries in this leaf

| Entry | Use when | Health | Page |
| --- | --- | --- | --- |
| **Humanizer-zh** | A single Chinese Claude Code skill that rewrites text to strip ~24 tell-tale AI-writing patterns; a localization of blader/humanizer. | C (4/6) | [→](humanizer-zh.md) |
| **De-AI-Prompt-Enhancer-Writer-Booster-SKILL** | Chinese de-AI writing suite with `de-AI-writing` and `good-writing` SKILL folders; useful when author-style reconstruction is desired and license ambiguity is acceptable. | C (4/6) | [→](de-ai-prompt-enhancer-writer-booster-skill.md) |
| **shuorenhua** | Chinese-first de-AI rewrite skill with protected spans, scenario rules, multi-harness docs, and MIT licensing. | B (4/6) | [→](shuorenhua.md) |
| **ai-flavor-remover** | Single-file Chinese prompt snippet for removing AI flavor; author-tested only on Gemini 2.5 Pro, not an installable skill pack. | D (4/6) | [→](ai-flavor-remover.md) |
| **humanizer** | English upstream Claude Code skill for removing signs of AI-generated writing, with plugin/install docs and MIT licensing. | B (4/6) | [→](humanizer.md) |
| **stop-slop** | Compact English prose de-slop skill with hard rules and references; best for fast cleanup, not nuanced formal prose. | B (4/6) | [→](stop-slop.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Humanizer-zh](humanizer-zh.md) | ✅ | C (4/6) | Chinese-first AI-text humanizing skill; use it as the current in-index baseline. |
| [Baoyu Skills](../writing/content-production/baoyu-skills.md) | ✅ | B (4/6) | Broader Chinese content/publishing bundle; Humanizer-zh is narrower and focused on de-AI rewriting. |
| Custom voice guide | 未收录 | — | Better for one private author or brand voice; less reusable than a public skill. |
| [De-AI-Prompt-Enhancer-Writer-Booster-SKILL](de-ai-prompt-enhancer-writer-booster-skill.md) | ✅ | C (4/6) | Heavier Chinese writer-booster workflow; useful for author-style reconstruction, risky when license clarity or neutrality matters. |
| [shuorenhua](shuorenhua.md) | ✅ | B (4/6) | Best current Chinese-first, fact-preserving de-AI skill when multi-harness reuse and protected spans matter. |
| [ai-flavor-remover](ai-flavor-remover.md) | ✅ | D (4/6) | Treat as a Gemini-tested prompt specimen, not as an OSS dependency or Agent Skills package. |
| [humanizer](humanizer.md) | ✅ | B (4/6) | Strong English upstream baseline with install docs; use Chinese-localized options for Chinese prose. |
| [stop-slop](stop-slop.md) | ✅ | B (4/6) | Shortest hard-rules English de-slop rubric; more likely to over-edit formal prose. |


## What belongs here

Agent skills, prompt repos, or writing helpers whose primary job is to **remove AI writing tells**, humanize prose, preserve facts while changing voice, or enforce human-sounding editorial style.
