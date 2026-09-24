# workflow-builders

> 分类节点。用于构建 LLM 工作流与 agentic 应用的提示词优化器、可视化平台与代码优先平台。
> ← 返回 [agent-frameworks](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **DSPy** | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 | A（6/6） | [→](dspy.zh.md) |
| **SkillOpt** | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 | B（6/6） | [→](skillopt.zh.md) |
| **AutoGPT** | 当你需要一个用于创建、部署和管理持续运行 AI 智能体以自动化复杂工作流的平台时用它——但它未声明许可，且自托管需要大量资源。 | B（5/6） | [→](autogpt.zh.md) |
| **Dify** | 当你想要一个生产就绪的、用于构建 agentic 工作流的低代码可视化平台，内置 RAG 与 MCP 支持时用它——但商用前请核实许可。 | B（5/6） | [→](dify.zh.md) |
| **LangChain** | 当你需要一个代码优先的框架来组合 LLM agent、工具与记忆，并拥有庞大的集成生态时用它——但简单单 prompt 应用别用它。 | A（5/6） | [→](langchain.zh.md) |
| **Langflow** | 可视化拖拽平台，用于构建和部署 LLM 工作流与智能体，内置 API 和 MCP 服务器；可视化流比代码更难做 diff/审查。 | B（6/6） | [→](langflow.zh.md) |
| **LlamaIndex** | LlamaIndex is the leading document agent and OCR platform | A（6/6） | [→](llamaindex.zh.md) |
| **Flowise** | Build AI Agents, Visually | D（5/6） | [→](flowise.zh.md) |
| **Agent-Native** | 你想让产品里的 agent 真的把活干完，并愿意让一个 TypeScript 应用接管界面、服务端与 Postgres，好让按钮和工具共用同一份实现。 | C（4/6） | [→](agent-native.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [DSPy](dspy.zh.md) | ✅ | A（6/6） | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 |
| [SkillOpt](skillopt.zh.md) | ✅ | B（6/6） | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 |
| [AutoGPT](autogpt.zh.md) | ✅ | B（5/6） | 当你需要一个用于创建、部署和管理持续运行 AI 智能体以自动化复杂工作流的平台时用它——但它未声明许可，且自托管需要大量资源。 |
| [Dify](dify.zh.md) | ✅ | B（5/6） | 当你想要一个生产就绪的、用于构建 agentic 工作流的低代码可视化平台，内置 RAG 与 MCP 支持时用它——但商用前请核实许可。 |
| [LangChain](langchain.zh.md) | ✅ | A（5/6） | 当你需要一个代码优先的框架来组合 LLM agent、工具与记忆，并拥有庞大的集成生态时用它——但简单单 prompt 应用别用它。 |
| [Langflow](langflow.zh.md) | ✅ | B（6/6） | 可视化拖拽平台，用于构建和部署 LLM 工作流与智能体，内置 API 和 MCP 服务器；可视化流比代码更难做 diff/审查。 |
| [Agent-Native](agent-native.zh.md) | ✅ | C（4/6） | 同一个 action 既驱动页面按钮也当 agent 工具，还附送完整应用（鉴权、SQL 状态、聊天）——代价是让框架接管你的技术栈，且它是半年大、迭代极快的 v0.x。 |

## 什么该放这里

用于构建 LLM 工作流与 agentic 应用的提示词优化器、可视化平台与代码优先平台。
