# deep-research

> 分类节点。迭代式多源研究 agent：搜索、抓取、综合成报告。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **deep-research** | 想要一个极简可读、约 500 行的 TypeScript 深度研究 agent 作为 fork 底座时用它。 | B（4/6） | [→](deep-research.zh.md) |
| **Vane** | 想要一个自托管、注重隐私的「Perplexity 式」带引用应答引擎，接你自己的 SearxNG 和自选 LLM 时用它。 | B（5/6） | [→](vane.zh.md) |
| **Local Deep Research** | 当你需要一个自托管、可纯本地运行的深度研究 agent、把敏感查询留在自己机器上时用它。 | B（6/6） | [→](local-deep-research.zh.md) |
| **Agent-Reach** | 当你的 agent 需要免付费 API 地读取和搜索网页与社交平台内容时用它。 | B（5/6） | [→](agent-reach.zh.md) |
| **MiroThinker** | 当你想要一个可在自有 GPU 上研究改造的自托管开源深研 Agent 时用它——但它要 GPU 集群加付费外部 API，且不到一岁、毫无 Lindy 沉淀。 | C（5/6） | [→](mirothinker.zh.md) |
| **GPT Researcher** | An autonomous agent that conducts deep research on any data using any LLM providers | A（6/6） | [→](gpt-researcher.zh.md) |
| **Open Deep Research** | 当你需要在 `deep-research` 分类中评估 Open Deep Research 时用它。 | D（5/6） | [→](open-deep-research.zh.md) |
| **STORM** | An LLM-powered knowledge curation system that researches a topic and generates a full-length report with citations. | B（6/6） | [→](storm.zh.md) |
| **node-DeepResearch** | Keep searching, reading webpages, reasoning until it finds the answer (or exceeding the token budget) | B（4/6） | [→](node-deepresearch.zh.md) |
| **Hyperresearch** | 当你在 Claude Code 里、需要一份引用逐条核验的高风险研究报告时用它——16 步对抗式流水线加持久来源 vault；时间与 token 开销都重，且只支持 Claude Code。 | B（5/6） | [→](hyperresearch.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [deep-research](deep-research.zh.md) | ✅ | B（4/6） | 想要一个极简可读、约 500 行的 TypeScript 深度研究 agent 作为 fork 底座时用它。 |
| [Vane](vane.zh.md) | ✅ | B（5/6） | 想要一个自托管、注重隐私的「Perplexity 式」带引用应答引擎，接你自己的 SearxNG 和自选 LLM 时用它。 |
| [Local Deep Research](local-deep-research.zh.md) | ✅ | B（6/6） | 当你需要一个自托管、可纯本地运行的深度研究 agent、把敏感查询留在自己机器上时用它。 |
| [Agent-Reach](agent-reach.zh.md) | ✅ | B（5/6） | 当你的 agent 需要免付费 API 地读取和搜索网页与社交平台内容时用它。 |
| [MiroThinker](mirothinker.zh.md) | ✅ | C（5/6） | 当你想要一个可在自有 GPU 上研究改造的自托管开源深研 Agent 时用它——但它要 GPU 集群加付费外部 API，且不到一岁、毫无 Lindy 沉淀。 |
| [Hyperresearch](hyperresearch.zh.md) | ✅ | B（5/6） | 锁死 Claude Code 的 16 步研究流水线，带对抗式 critic、引用核验和持久 vault；pre-1.0 churn 明显，且榜单领先宣称是自测 projection。 |
| Perplexity / OpenAI Deep Research | 未收录 | — | 各页对比里点到的其他深度研究 agent / 服务。 |

## 什么该放这里

主要职责是**迭代式 web / 多源研究**（搜索、抓取、综合）的 agent。不含一次性 RAG 索引（见 `rag-retrieval`），不含通用 agent 框架（见 `agent-frameworks`）。
