# app-evals

> 分类节点。给**你自己的** LLM 应用做回归测试、RAG 打分、生产轨迹与提示词版本，让一次提示词或模型改动不会悄悄变差。
> ← 返回 [llm-eval](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | A（6/6） | [→](promptfoo.zh.md) |
| **Pezzo** | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 | C（5/6） | [→](pezzo.zh.md) |
| **DeepEval** | 当 Python 团队想给 RAG 应用或智能体写 pytest 式回归测试，在 CI 里用忠实度、幻觉等大模型评审指标打分时用它——但每次运行都花评审 token，分数会浮动，配套看板是厂商的商业托管平台。 | A（6/6） | [→](deepeval.zh.md) |
| **Ragas** | 当你改了 RAG 链路的分块、向量模型或生成模型，需要评审大模型为每次改动打出忠实度和上下文召回／精确率时用它——但它只给分数，不提供 CI 通过／失败闸门，且自 2026-02 起再无 PR 合并。 | B（6/6） | [→](ragas.zh.md) |
| **Giskard OSS** | 当用 Python 3.12+ 的团队想把 RAG 或 agent 的故障钉成带大模型裁判检查的场景测试、上线前还要自动生成攻击提示词时用它——但表格模型扫描只在已不再积极维护的 v2 里，v3 正式版才发布几周。 | B（6/6） | [→](giskard.zh.md) |
| **Langfuse** | 当生产中的大模型功能需要给每个请求记嵌套调用轨迹，再加打分、提示词版本和数据集，并且要能自托管时用它——但自托管要运维 Postgres、ClickHouse、Redis 和 S3 存储，部分管理功能还走企业许可。 | A（5/6） | [→](langfuse.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [promptfoo](promptfoo.zh.md) | ✅ | A（6/6） | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 |
| [Pezzo](pezzo.zh.md) | ✅ | C（5/6） | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 |
| [DeepEval](deepeval.zh.md) | ✅ | A（6/6） | 用 pytest 把评测写成 Python 代码，配大模型评审指标覆盖 RAG 与 agent；要 CLI 跑的 YAML 套件选 promptfoo，只要 RAG 分数选 Ragas。 |
| [Ragas](ragas.zh.md) | ✅ | B（6/6） | 专给 RAG 打忠实度和上下文召回／精确率分，在 notebook 或脚本里跑；只给分数不给 CI 闸门，要闸门选 DeepEval 或 promptfoo。 |
| [Giskard OSS](giskard.zh.md) | ✅ | B（6/6） | Python 场景测试加大模型裁判检查，并为 RAG／agent 生成攻击提示词；v3 才发布几周，表格模型扫描只在不再维护的 v2 里。 |
| [Langfuse](langfuse.zh.md) | ✅ | A（5/6） | 生产轨迹加打分、提示词版本和数据集，一个可自托管应用全包；自托管要运维 Postgres、ClickHouse、Redis 和 S3，部分管理功能走企业许可。 |
| OpenAI Evals | 未收录 | — | 各页对比里点到的另一个评测框架，尚未收录。 |

## 什么该放这里

测试或观测**你自己的** LLM 应用、跨改动比较的工具：CI 里的断言套件、RAG 指标打分、场景测试，以及为它们供数的轨迹与提示词版本平台。不含对模型或 AI 栈的攻击扫描（见 `security-audits`），不含固定的公共基准（见 `benchmarks`）。
