# llm-eval

> 分类节点。对提示词、agent 与 RAG 做测试、基准与安全红队扫描。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **promptfoo** | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 | A（6/6） | [→](promptfoo.zh.md) |
| **Pezzo** | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 | C（4/6） | [→](pezzo.zh.md) |
| **DeepEval** | The LLM Evaluation Framework | A（6/6） | [→](deepeval.zh.md) |
| **Ragas** | Supercharge Your LLM Application Evaluations 🚀 | B（6/6） | [→](ragas.zh.md) |
| **garak** | the LLM vulnerability scanner | A（6/6） | [→](garak.zh.md) |
| **Giskard OSS** | 🐢 Open-Source Evaluation & Testing library for LLM Agents | B（6/6） | [→](giskard.zh.md) |
| **Langfuse** | 🪢 Open source AI engineering platform: LLM evals, observability, metrics, prompt management, playground, datasets. Integrates with OpenTelemetry, LangChain, OpenAI SDK, LiteLLM, and more. 🍊YC W23 | A（5/6） | [→](langfuse.zh.md) |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus（HC3）、检测器和相关 AI 文本检测资源。 | E（4/6） | [→](chatgpt-comparison-detection.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [promptfoo](promptfoo.zh.md) | ✅ | A（6/6） | 当你要用声明式 YAML 给自己的 LLM 应用做评测+红队并接进 CI 时用它。 |
| [Pezzo](pezzo.zh.md) | ✅ | C（4/6） | 当小团队想要一个自托管的统一控制台来做 prompt 版本管理加成本／延迟可观测时用它——但它自 2025 年中起疑似停更，请做好自己维护的准备。 |
| DeepEval / Ragas / OpenAI Evals / Giskard | 未收录 | — | 各页对比里点到的其他 LLM 评测 / 红队框架。 |
| [chatgpt-comparison-detection](chatgpt-comparison-detection.zh.md) | ✅ | E（4/6） | 面向 AI 文本对比的数据集 / 检测器资源；需要维护中的测试 runner 时选 eval framework。 |


## 什么该放这里

主要职责是对 LLM 提示词/agent/RAG 做**评测、基准或红队**的工具。不含代码评审（见 `ai-code-review`），不含训练（见 `llm-training`）。
