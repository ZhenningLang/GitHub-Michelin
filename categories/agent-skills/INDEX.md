# agent-skills

> Category node. Agent skills, skill packs, prompt workflows, subagent personas, and harness configs — organized by task so an agent can choose a skill or skill combination.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Sub-categories (by task)

| Leaf | What's inside | Route |
|---|---|---|
| **engineering** | Code quality, web performance, testing, and scientific/eng workflows. | [→](engineering/INDEX.md) |
| **design** | Design taste / UI-UX judgment — critique, anti-slop, visual generation. | [→](design/INDEX.md) |
| **slides-ppt** | Presentation and slide-deck skills for agent-generated decks. | [→](slides-ppt/INDEX.md) |
| **visual-content** | Social cards, article illustrations, covers, and other visual-content skills. | [→](visual-content/INDEX.md) |
| **de-ai-writing** | Humanizing AI text, removing AI tells, and enforcing human-sounding prose. | [→](de-ai-writing/INDEX.md) |
| **writing** | Translation, long-form writing workflows, editorial and publishing pipelines. | [→](writing/INDEX.md) |
| **security** | Security review, threat modeling, cybersecurity playbooks. | [→](security/INDEX.md) |
| **context-engineering** | Structuring, compressing, and routing what an agent reads. | [→](context-engineering/INDEX.md) |
| **prompt-engineering** | Writing, generating, and collecting prompts for any AI tool — generator skills, community prompt libraries, and knowledge bases. | [→](prompt-engineering/INDEX.md) |
| **vendor-collections** | Official / vendor-published first-party skill & plugin bundles. | [→](vendor-collections/INDEX.md) |
| **subagent-collections** | Ready-made subagent definitions / personas to drop into a harness. | [→](subagent-collections/INDEX.md) |
| **personal-collections** | The long tail: one author's curated skills, subagents, or harness config. | [→](personal-collections/INDEX.md) |

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **book-to-skill** | Use it when you want to turn technical book PDFs (and other document formats) into installable agent skills for Claude Code, Copilot CLI, or Amp. | B (6/6) | [→](book-to-skill.md) |
| **distilly** | Use it when you want to distill one person's chat logs, documents, and interviews into an installable agent skill that answers in their judgment and voice. | B (4/6) | [→](distilly.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [book-to-skill](book-to-skill.md) | ✅ | B (6/6) | Converts technical books and documents into installable agent skills; batch tool, not a live RAG system. |
| [Docling](../document-parsing/docling.md) | ✅ | A (6/6) | General document parser for RAG pipelines; book-to-skill is specifically a skill-generator for agent harnesses. |
| [NotebookLM Claude Code Skill](context-engineering/notebooklm-skill.md) | ✅ | C (4/6) | Queries an external Google service; book-to-skill works on local PDFs with no external dependency. |
| LlamaIndex / RAG pipelines | 未收录 | — | Full RAG with embeddings and dynamic retrieval; more infrastructure than a static skill generator. |
| [distilly](distilly.md) | ✅ | B (4/6) | Generates a person-specific work/persona skill from your private source material; no retrieval layer, and its only automated fidelity gate is keyword-level. |

## What belongs here

A deliberately crowded field — agent **skills / prompts / subagent personas / harness configs**, where no
single one is "the" answer. Organize primary leaves by task when the job is clear (slides, visual
content, writing, engineering, context), and keep provenance leaves for vendor, personal, or subagent
collections. Self-balancing: a leaf that outgrows the fanout splits further.
