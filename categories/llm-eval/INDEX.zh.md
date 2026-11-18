# llm-eval

> 分类节点。对提示词、agent 与 RAG 做测试、基准与安全红队扫描。
> 按**被测对象是什么**拆成子分类：你自己的 LLM 应用质量随改动的变化、模型／agent／整套 AI 栈的安全与治理状况，或拿固定公开题集给模型、agent、harness 排名。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **应用评测** | 你在改自家 LLM 应用的提示词、检索或模型，需要回归测试、RAG 打分，或生产轨迹与提示词版本来看哪里坏了。 | [→](app-evals/INDEX.zh.md) |
| **安全审计** | 上线或审查前，你要证明模型、agent 或整套 AI 栈扛得住已知攻击，并守在声明的角色和权限里。 | [→](security-audits/INDEX.zh.md) |
| **基准与数据集** | 你要在固定的公共题集或语料上比较模型、agent 或 harness，而不是测试自己的应用。 | [→](benchmarks/INDEX.zh.md) |

## 对比矩阵

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [应用评测](app-evals/INDEX.zh.md) | 子分类 | promptfoo、DeepEval、Ragas、Giskard、Langfuse、Pezzo——为自家应用写的测试与轨迹；分数来自要付费、会浮动的大模型评审。 |
| [安全审计](security-audits/INDEX.zh.md) | 子分类 | garak、AI-Infra-Guard、iFixAi——用固定的攻击或治理清单审模型、agent 或整套栈；审的是安全状况，不是应用回答质量。 |
| [基准与数据集](benchmarks/INDEX.zh.md) | 子分类 | SWE-bench、Harvey LAB、g-harness-evals、HC3——现成题集与判分，用来排名；跑起来重，结论只和题目组成一样可靠。 |

## 什么该放这里

主要职责是对 LLM 提示词/agent/RAG 做**评测、基准或红队**的工具。不含代码评审（见 `ai-code-review`），不含训练（见 `llm-training`）。按测什么选子分类：测你自己的应用（`app-evals`）、测它会不会被攻破或越权（`security-audits`）、测它在公共题集上排第几（`benchmarks`）。
