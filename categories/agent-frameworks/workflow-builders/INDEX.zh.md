# workflow-builders

> 分类节点。用于构建 LLM 工作流与 agentic 应用的提示词优化器、可视化平台与代码优先平台。
> ← 返回 [agent-frameworks](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **DSPy** | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 | A（6/6） | [→](dspy.zh.md) |
| **SkillOpt** | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 | B（6/6） | [→](skillopt.zh.md) |
| **AutoGPT** | 当一件每周重复的跨应用杂活（读 Gmail、查 CRM、让大模型起草、发到 Slack）要变成在画布上拖出来、或用大白话描述出来的定时 agent 时用它——但平台部分是 PolyForm Shield 许可、不是 OSI 开源，自托管还得跑一大堆服务。 | B（5/6） | [→](autogpt.zh.md) |
| **Dify** | 当团队要做好几个大模型应用（文档问答机器人、工单分诊流程），想在画布上配着知识库搭出来、一发布就有网页界面和 API 时用它——但它的许可不允许未经授权做多租户服务或去掉 logo。 | B（5/6） | [→](dify.zh.md) |
| **LangChain** | 当 Python 助手要调用你的工具，又要在 OpenAI、Claude 和本地模型之间切换、不想每家都重写工具格式和调用循环时用它——但单次提示词应用别用，要自己设计控制流时直接用 LangGraph。 | A（6/6） | [→](langchain.zh.md) |
| **Langflow** | 当你想在画布上把提示词、检索器和工具连起来，在聊天面板里马上试，再把流程当 HTTP API 或 MCP 工具调用时用它——但它的安全公告里有未认证远程代码执行，做不到每周打补丁就别把它暴露出去。 | B（6/6） | [→](langflow.zh.md) |
| **LlamaIndex** | 当 Python 应用要基于你自己的 PDF、wiki 或工单作答，想用几行代码搭好读取、切块、向量化、检索这条管线时用它——但公司重心已转向收费的 LlamaParse，开源框架成了副业。 | A（6/6） | [→](llamaindex.zh.md) |
| **Flowise** | 只在你已经跑着 Flowise 聊天流、要决定自己 fork 还是迁走时看它——但仓库已于 2026-08-13 归档、2026-08-31 停止支持，新项目请改用 Langflow 或 Dify。 | D（5/6） | [→](flowise.zh.md) |
| **Agent-Native** | 你想让产品里的 agent 真的把活干完，并愿意让一个 TypeScript 应用接管界面、服务端与 Postgres，好让按钮和工具共用同一份实现。 | C（4/6） | [→](agent-native.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [DSPy](dspy.zh.md) | ✅ | A（6/6） | 你有评测数据和指标、想让优化器编译提示词而非手工调时。 |
| [SkillOpt](skillopt.zh.md) | ✅ | B（6/6） | 当你要针对可打分基准、为冻结的 LLM 优化 Agent 的自然语言技能文档时用它——但没有可靠评测来把关每次编辑，方法就毫无信号，且它还是全新的 v0.1.0。 |
| [AutoGPT](autogpt.zh.md) | ✅ | B（5/6） | 换来大模型原生的自动化平台，定时、webhook 和应用积木都在一处；代价是带竞争限制的许可加 CLA、仍是 beta 的版本线，自托管要跑 Postgres、Redis、RabbitMQ 等一串组件。 |
| [Dify](dify.zh.md) | ✅ | B（5/6） | 换来一个自托管工作区，RAG 应用、工作流和对应 API 都在里面；代价是 Apache 外加条件的自定义许可，出品方日后还能收紧，SSO 和 RBAC 留在付费企业版里。 |
| [LangChain](langchain.zh.md) | ✅ | A（6/6） | 换来覆盖几百个模型和工具集成的统一接口，加上现成的 `create_agent` 循环；代价是抽象层的分量、每逢大版本就重组，以及被推向付费的 LangSmith。 |
| [Langflow](langflow.zh.md) | ✅ | B（6/6） | 换来 MIT 许可下的快速可视化迭代，每个节点背后都是可改的 Python；代价是能编辑流程的人就能在服务器上执行代码，流程也比代码更难评审。 |
| [Agent-Native](agent-native.zh.md) | ✅ | C（4/6） | 同一个 action 既驱动页面按钮也当 agent 工具，还附送完整应用（鉴权、SQL 状态、聊天）——代价是让框架接管你的技术栈，且它是半年大、迭代极快的 v0.x。 |

## 什么该放这里

用于构建 LLM 工作流与 agentic 应用的提示词优化器、可视化平台与代码优先平台。
