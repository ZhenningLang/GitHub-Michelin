# social-simulation

> 分类节点。模拟由 LLM agent 组成的社会——社交媒体世界、舆论动力学实验，以及让虚拟人群先反应一遍的推演沙盒。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **MiroFish** | 打包好的「上传→模拟→报告」群体智能预测应用：喂一份文档，拿回预测报告和可交互的模拟世界。 | C（5/6） | [→](mirofish.zh.md) |
| **OASIS** | CAMEL-AI 出品的 pip 可装社交媒体模拟框架（类 Twitter/Reddit，号称最高百万 agent），用代码研究信息传播与极化。 | B（6/6） | [→](oasis.zh.md) |
| **AgentSociety** | 清华 FIB Lab 的 LLM 原生社会科学模拟平台：Ray 分布式、实验回放、DuckDB 追踪。 | B（5/6） | [→](agentsociety.zh.md) |
| **generative_agents** | 2023 年斯坦福「Smallville」原版研究原型（memory stream / reflection / planning）——学开创性架构用，别在上面盖楼。 | D（3/6） | [→](generative-agents.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [MiroFish](mirofish.zh.md) | ✅ | C（5/6） | 成品（上传→报告），但 AGPL-3.0 + Zep Cloud 依赖 + 预测能力未经验证。 |
| [OASIS](oasis.zh.md) | ✅ | B（6/6） | Apache-2.0 引擎，社交媒体信息流保真、公布成本模型；流水线要自己搭。 |
| [AgentSociety](agentsociety.zh.md) | ✅ | B（5/6） | 科研级回放/分布式实验能力；技术栈更重、纯框架。 |
| [generative_agents](generative-agents.zh.md) | ✅ | D（3/6） | 领域开创性参考实现，2024-08 起冻结；只剩教学/研究价值。 |

## 什么该放这里

主要职责是**模拟 LLM agent 社会**的项目——社交媒体平台、城市环境或具身世界——用来观察涌现的群体行为。
不含通用 agent 构建/运行框架（见 `agent-frameworks`），不含深度调研流水线（见 `deep-research`），不含单 agent 记忆（见 `agent-memory`）。
