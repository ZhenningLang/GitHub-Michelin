# llm-eval

> 分类节点。对提示词、agent 与 RAG 做测试、基准与安全红队扫描。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | A（6/6） | [→](promptfoo.zh.md) |
| **Pezzo** | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 | C（5/6） | [→](pezzo.zh.md) |
| **DeepEval** | 当 Python 团队想给 RAG 应用或智能体写 pytest 式回归测试，在 CI 里用忠实度、幻觉等大模型评审指标打分时用它——但每次运行都花评审 token，分数会浮动，配套看板是厂商的商业托管平台。 | A（6/6） | [→](deepeval.zh.md) |
| **Ragas** | 当你改了 RAG 链路的分块、向量模型或生成模型，需要评审大模型为每次改动打出忠实度和上下文召回／精确率时用它——但它只给分数，不提供 CI 通过／失败闸门，且自 2026-02 起再无 PR 合并。 | B（6/6） | [→](ragas.zh.md) |
| **garak** | 当模型上线前要由你签字放行，需要一套可重复的扫描，按探针给出越狱、注入、数据泄露、恶意代码生成等已知攻击的失败率时用它——但它只测模型本身，不测应用的回答质量或整套部署。 | A（6/6） | [→](garak.zh.md) |
| **Giskard OSS** | 当用 Python 3.12+ 的团队想把 RAG 或 agent 的故障钉成带大模型裁判检查的场景测试、上线前还要自动生成攻击提示词时用它——但表格模型扫描只在已不再积极维护的 v2 里，v3 正式版才发布几周。 | B（6/6） | [→](giskard.zh.md) |
| **Langfuse** | 当生产中的大模型功能需要给每个请求记嵌套调用轨迹，再加打分、提示词版本和数据集，并且要能自托管时用它——但自托管要运维 Postgres、ClickHouse、Redis 和 S3 存储，部分管理功能还走企业许可。 | A（5/6） | [→](langfuse.zh.md) |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus（HC3）、检测器和相关 AI 文本检测资源。 | E（4/6） | [→](chatgpt-comparison-detection.zh.md) |
| **SWE-bench** | 当你要用真实 GitHub issue 及其测试给 coding agent 的补丁打分时用它——每次评测都要 Docker 和大量磁盘。 | B（6/6） | [→](swe-bench.zh.md) |
| **Harvey LAB** | 当你要让 agent 做完整套法律任务来做基准——虚构案卷进、备忘录或修订稿出，由两个大模型评委按律师清单判分——时用它；需要 Podman，以及 Anthropic 和 OpenAI 两把密钥。 | B（6/6） | [→](harvey-labs.zh.md) |
| **AI-Infra-Guard** | 当审计面是整套自托管 AI 栈时用它——在线服务 CVE、MCP server、Agent Skill、越狱评测，一个腾讯出品的平台搞定，而不是只盯单个模型端点。 | B（6/6） | [→](ai-infra-guard.zh.md) |
| **iFixAi** | 当你想快速、开箱即用地审一审 agent 守没守住声明的角色、工具权限和诚实规则时用它——60 项固定检查、另一家厂商的评委、一个 A–F 等级；项目很年轻、靠大模型判分，1.8 万星和它的实际使用量对不上。 | B（4/6） | [→](ifixai.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [promptfoo](promptfoo.zh.md) | ✅ | A（6/6） | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 |
| [Pezzo](pezzo.zh.md) | ✅ | C（5/6） | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 |
| Ragas / OpenAI Evals | 部分已收录 | — | 各页对比里点到的其他 LLM 评测 / 红队框架；其中 Ragas 已收录在本分类，OpenAI Evals 尚未收录。 |
| [chatgpt-comparison-detection](chatgpt-comparison-detection.zh.md) | ✅ | E（4/6） | 面向 AI 文本对比的数据集 / 检测器资源；需要维护中的测试 runner 时选 eval framework。 |
| [AI-Infra-Guard](ai-infra-guard.zh.md) | ✅ | B（6/6） | 整套 AI 栈的安全自查平台（基础设施 CVE、MCP、Skill、越狱）；只对单个模型或自己的应用跑命令行红队时选 garak/promptfoo。 |
| [iFixAi](ifixai.zh.md) | ✅ | B（4/6） | 面向 agent 的固定治理检查清单（角色、工具权限、诚实度），由跨厂商大模型评委判分；要在 CI 里跑自己写的断言选 promptfoo，要攻击覆盖面选 garak。 |
| [Harvey LAB](harvey-labs.zh.md) | ✅ | B（6/6） | 法律 agent 基准，1,600 多道虚构案卷题、大模型评委全对才得分；测写代码的 agent 选 SWE-bench，给自家应用做回归测试选 promptfoo。 |


## 什么该放这里

主要职责是对 LLM 提示词/agent/RAG 做**评测、基准或红队**的工具。不含代码评审（见 `ai-code-review`），不含训练（见 `llm-training`）。
