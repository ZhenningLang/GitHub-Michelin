# benchmarks

> 分类节点。用固定的公共题集、语料和判分环境，给模型、agent 或 harness 互相排名。
> ← 返回 [llm-eval](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **chatgpt-comparison-detection** | Human ChatGPT Comparison Corpus（HC3）、检测器和相关 AI 文本检测资源。 | E（4/6） | [→](chatgpt-comparison-detection.zh.md) |
| **SWE-bench** | 当你要用真实 GitHub issue 及其测试给 coding agent 的补丁打分时用它——每次评测都要 Docker 和大量磁盘。 | B（6/6） | [→](swe-bench.zh.md) |
| **Harvey LAB** | 当你要让 agent 做完整套法律任务来做基准——虚构案卷进、备忘录或修订稿出，由两个大模型评委按律师清单判分——时用它；需要 Podman，以及 Anthropic 和 OpenAI 两把密钥。 | B（6/6） | [→](harvey-labs.zh.md) |
| **g-harness-evals** | 当你要在 Claude Code、Codex、OpenClaw、Hermes Agent、Pi 之间选一个 agent harness，想看同模型下按每题成本排出、每个数字都能免 key 复核的结果时用它——但这是一位作者的年轻研究，有已披露的利益关系，只覆盖固定版本和偏简单的公开任务。 | C（5/6） | [→](g-harness-evals.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [chatgpt-comparison-detection](chatgpt-comparison-detection.zh.md) | ✅ | E（4/6） | 面向 AI 文本对比的数据集 / 检测器资源；需要维护中的测试 runner 时选 eval framework。 |
| [g-harness-evals](g-harness-evals.zh.md) | ✅ | C（5/6） | 固定模型、按成对每题成本排名的 harness 对比，带预注册和回执；要比模型选 SWE-bench，要测自己的应用选 promptfoo。 |
| [Harvey LAB](harvey-labs.zh.md) | ✅ | B（6/6） | 法律 agent 基准，1,600 多道虚构案卷题、大模型评委全对才得分；测写代码的 agent 选 SWE-bench，给自家应用做回归测试选 promptfoo。 |
| [SWE-bench](swe-bench.zh.md) | ✅ | B（6/6） | 以真实 GitHub issue 为标准题库、用仓库自带测试判分；每次运行吃 Docker 和大量磁盘，用来给模型／agent 排名，不测你自己的应用。 |

## 什么该放这里

主要资产是**共享题集或语料加判分方式**、用来比较系统的仓库：编码 issue 基准、领域 agent 基准、harness 对比、AI 文本检测语料。不含你为自家应用写的测试（见 `app-evals`），不含安全扫描（见 `security-audits`），不含推理速度基准（见 `llm-inference`）。
