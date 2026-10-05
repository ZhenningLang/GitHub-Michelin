# learning-resources

> Category node. Curated reading paths and resource lists you read rather than run — a maintained order over the primary sources of a field, with a stated bar for what earns an entry — plus tutorial collections of example apps you run once and copy from.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **AI Engineering Hub** | Use it when you need a running example of a specific LLM stack combination — a local-model RAG app, a CrewAI crew with web fallback, an MCP server — to copy glue code from; it is MIT demo code with no tests and many stale folders, not something to depend on. | A (5/6) | [→](ai-engineering-hub.md) |
| **AI Performance Engineering Resources** | Use it when you need to learn or reference GPU/AI performance engineering and want the canonical source per mechanism in dependency order — one request → one GPU → kernels → engines → distributed serving — instead of a pile of blog posts. | C (3/5) | [→](gpu-perf-engineering-resources.md) |
| **HowToLiveLonger** | Use it when you want everyday habits — diet, drinks, sleep, exercise, weight — ranked on one page by the change in all-cause mortality some study reported, each number linked to its source, to decide what to change first; not for drug or supplement decisions. | C (3/5) | [→](how-to-live-longer.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [AI Engineering Hub](ai-engineering-hub.md) | ✅ | A (5/6) | ~115 self-contained Streamlit/notebook demos, each wiring a named model, framework, vector store and vendor API together under MIT — but no tests or CI, 93 folders untouched for a year, unpinned deps, and vendor-centric content from a newsletter team. |
| [AI Performance Engineering Resources](gpu-perf-engineering-resources.md) | ✅ | C (3/5) | An ordered 124-link path over papers, official vendor documentation and implementing repositories, with a source bar that keeps out summaries and unsourced performance numbers — but nothing here runs, and the path is NVIDIA-shaped for the kernel half. |
| [HowToLiveLonger](how-to-live-longer.md) | ✅ | C (3/5) | One Chinese-first page of about twenty habits with a percent-mortality figure each and a source link per number — but the figures are single observational studies, ~60% of links are news or Q&A reposts, and the content has been frozen since 2024-01. |

## What belongs here

Repositories whose product is a **reading path** rather than a runnable artifact: curated lists, learning curricula and reference collections whose value is the *selection and order* they impose on other people's papers, specs and repositories. Tutorial collections whose folders are runnable demo apps also belong here when their value is learning and copying rather than depending on them. Not the primary sources themselves (a paper's reference implementation belongs in its own domain category, e.g. `llm-inference`); not AI tutoring systems (see `education-tutoring`); not awesome-lists of installable agent skills (see `agent-skills`).
