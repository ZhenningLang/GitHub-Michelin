# llm-eval

> 分类节点。对提示词、agent 与 RAG 做测试、基准与安全红队扫描。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | A（5/6） | [→](promptfoo.zh.md) |
| **Pezzo** | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 | C（5/6） | [→](pezzo.zh.md) |
| **DeepEval** | The LLM Evaluation Framework | A（6/6） | [→](deepeval.zh.md) |
| **Ragas** | Supercharge Your LLM Application Evaluations 🚀 | B（6/6） | [→](ragas.zh.md) |
| **garak** | the LLM vulnerability scanner | A（6/6） | [→](garak.zh.md) |
| **Giskard OSS** | 🐢 Open-Source Evaluation & Testing library for LLM Agents | B（6/6） | [→](giskard.zh.md) |
| **Langfuse** | 🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 | A（5/6） | [→](langfuse.zh.md) |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus（HC3）、检测器和相关 AI 文本检测资源。 | E（4/6） | [→](chatgpt-comparison-detection.zh.md) |
| **SWE-bench** | 当你要用真实 GitHub issue 及其测试给 coding agent 的补丁打分时用它——每次评测都要 Docker 和大量磁盘。 | B（6/6） | [→](swe-bench.zh.md) |
| **AI-Infra-Guard** | 当审计面是整套自托管 AI 栈时用它——在线服务 CVE、MCP server、Agent Skill、越狱评测，一个腾讯出品的平台搞定，而不是只盯单个模型端点。 | B（6/6） | [→](ai-infra-guard.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [promptfoo](promptfoo.zh.md) | ✅ | A（5/6） | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 |
| [Pezzo](pezzo.zh.md) | ✅ | C（5/6） | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 |
| Ragas / OpenAI Evals | 部分已收录 | — | 各页对比里点到的其他 LLM 评测 / 红队框架；其中 Ragas 已收录在本分类，OpenAI Evals 尚未收录。 |
| [chatgpt-comparison-detection](chatgpt-comparison-detection.zh.md) | ✅ | E（4/6） | 面向 AI 文本对比的数据集 / 检测器资源；需要维护中的测试 runner 时选 eval framework。 |
| [AI-Infra-Guard](ai-infra-guard.zh.md) | ✅ | B（6/6） | 整套 AI 栈的安全自查平台（基础设施 CVE、MCP、Skill、越狱）；只对单个模型或自己的应用跑命令行红队时选 garak/promptfoo。 |


## 什么该放这里

主要职责是对 LLM 提示词/agent/RAG 做**评测、基准或红队**的工具。不含代码评审（见 `ai-code-review`），不含训练（见 `llm-training`）。
