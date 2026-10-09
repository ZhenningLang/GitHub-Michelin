# agent-sdks

> 分类节点。写代码来构建 agent（或 agent 团队）时使用的库与框架，跑在你自己的程序里。
> ← 返回 [agent-runtimes](../INDEX.zh.md) · 根：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **AgentScope** | 要把多智能体 LLM 应用作为生产服务交付，需要沙箱工具、权限闸门、tracing 和人工介入时。 | B（6/6） | [→](agentscope.zh.md) |
| **AutoGen** | 当你已有跑在 AutoGen AgentChat 或 Core 运行时上的 Python／.NET 多 agent 系统、重写的风险更大时留着用它——但它已进入维护模式，新项目请从 Microsoft Agent Framework 起步。 | B（5/6） | [→](autogen.zh.md) |
| **CrewAI** | 当一件知识型工作天然按角色拆分（研究员、分析师、写手），而你宁愿声明智能体和任务、不想亲手连图时用它——但交接由提示词决定，核心包一装就拉进一大串依赖。 | A（6/6） | [→](crewai.zh.md) |
| **LangGraph** | 当智能体要跑几分钟甚至几天，中途得等人审批、或者要扛过重启接着跑时用它——但循环要一个节点一个节点地拼，官方自托管生产服务器还需要 LangSmith 许可证。 | A（6/6） | [→](langgraph.zh.md) |
| **Microsoft Agent Framework** | 想要微软对 AutoGen + Semantic Kernel 的接班品：先给会自己循环的 agent，生产需要时再上带类型的图工作流和 .NET 对等支持。 | A（6/6） | [→](agent-framework.zh.md) |
| **OpenAI Agents SDK** | 当产品已经跑在 OpenAI 模型上，想用几个原语就拿到工具循环、智能体交接和追踪时用它——但运行没有 Temporal 这类基础设施就扛不过崩溃，非 OpenAI 厂商只能走 beta 适配器。 | A（6/6） | [→](openai-agents-sdk.zh.md) |
| **Pydantic AI** | 当 Python 服务里需要一步大模型调用、返回经 Pydantic 校验的类型，还想用一个字符串就换模型厂商时用它——但它只支持 Python，API 九个月里就从 V1 升到了 V2。 | A（6/6） | [→](pydantic-ai.zh.md) |
| **smolagents** | 当你想要 Hugging Face 出的极简、透明、写代码行动的 agent 循环时用它——不是重型生产 agent 操作系统。 | B（6/6） | [→](smolagents.zh.md) |
| **Harness SDK** | 想要一次调用就有能用的 agent——调好的 prompt、shell／文件／web 工具、代码沙箱、子代理、记忆与会话——而且 Python 与 TypeScript 同接口、每个默认值都可覆盖时用它。 | A（6/6） | [→](harness-sdk.zh.md) |
| **TanStack AI** | 在 TypeScript 应用里做 AI 界面——流式聊天、带类型的工具、媒体与 agent，横跨七个前端框架——想要一套 provider 无关的类型契约、且完全不绑平台层时用它。 | B（6/6） | [→](tanstack-ai.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [AgentScope](agentscope.zh.md) | ✅ | B（6/6） | 要把多智能体 LLM 应用作为生产服务交付，需要沙箱工具、权限闸门、tracing 和人工介入时。 |
| [smolagents](smolagents.zh.md) | ✅ | B（6/6） | 当你想要 Hugging Face 出的极简、透明、写代码行动的 agent 循环时用它——不是重型生产 agent 操作系统。 |
| [Harness SDK](harness-sdk.zh.md) | ✅ | A（6/6） | 一次调用拿到调好的默认 agent，Python 与 TypeScript 同接口；代价是控制流归模型、组装层还在 0.x。 |

## 什么该放这里

写代码来构建 agent（或 agent 团队）时使用的库与框架，跑在你自己的程序里。
