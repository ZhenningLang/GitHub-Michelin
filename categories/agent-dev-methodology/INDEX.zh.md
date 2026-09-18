# agent-dev-methodology

> 分类节点。塑造 agent **如何**构建软件的框架与方法论——spec 驱动、上下文工程、persona/命令体系。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **12-Factor Agents** | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 | B（4/6） | [→](12-factor-agents.zh.md) |
| **Superpowers** | 当你想给编程 agent 装一套即插即用的「头脑风暴→计划→TDD→验证」SDLC 方法论时用它。 | B（4/6） | [→](superpowers.zh.md) |
| **SuperClaude Framework** | 当你常驻 Claude Code、想一次装好现成的命令、agent 和行为模式框架时用它。 | B（4/6） | [→](superclaude.zh.md) |
| **Get Shit Done (GSD)** | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 | C（6/6） | [→](get-shit-done.zh.md) |
| **Compound Engineering** | 当你想要一套即插即用的 brainstorm→plan→work→review→compound 循环、并把经验跨会话沉淀复用时，就用它。 | B（4/6） | [→](compound-engineering.zh.md) |
| **ECC** | 当你想要一套有人维护、开箱即全的 Claude Code 底座（skill、agent、hook、memory 加安全扫描）时用它。 | B（6/6） | [→](ecc.zh.md) |
| **Spec Kit** | 当你想要 GitHub 出品的面向 AI 编码智能体的 spec-driven 开发方法论时用它——但它极其年轻，且与 GitHub 生态深度绑定。 | B（5/6） | [→](spec-kit.zh.md) |
| **Spec-Anchored Agentic Development** | 当永久 capability spec 和持续 spec-to-code conformance 比广泛 harness 支持更重要时用它；bundle 仅面向 Claude Code，而且项目只有十多天历史。 | B（3/6） | [→](spec-anchored-agentic-development.zh.md) |
| **USDAD** | 当你要可编辑、文字优先的 planner／adversary／architect／executor 方法论原稿时用它；它是单提交文档工件，不是可安装 runtime 或强制执行的工作流。 | C（4/6） | [→](usdad.zh.md) |
| **QUAD Framework** | 只在法务审查后研究它的四 Circles 组织模型和部署语料；软件采用专有许可，项目已不活跃，公开安装器与 submodule 路径也不完整。 | D（4/6） | [→](quad.zh.md) |
| **LTBL Experiment** | 只把它当作三个上下文质量实现组的未完成索引；它不是可运行软件、带评分的 benchmark，也没有发布胜负结论。 | D（4/6） | [→](ltbl-experiment.zh.md) |
| **PURE** | 当 coding-agent intent lineage 必须落进 Git 跟踪的 spec、schema、registry、phase gate 和带测试 Shell 脚本时用它；它仍是单维护者的早期 v0.1 框架。 | C（5/6） | [→](pure-agentic.zh.md) |
| **Learn Claude Code** | 当你想通过亲手重建全部 17 个机制来搞懂 Claude Code 式 agent harness 的原理时用它——但它是课程，不是可 import 的库，也不是生产级 CLI。 | B（5/6） | [→](learn-claude-code.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [12-Factor Agents](12-factor-agents.zh.md) | ✅ | B（4/6） | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 |
| [Superpowers](superpowers.zh.md) | ✅ | B（4/6） | 当你想给编程 agent 装一套即插即用的「头脑风暴→计划→TDD→验证」SDLC 方法论时用它。 |
| [SuperClaude Framework](superclaude.zh.md) | ✅ | B（4/6） | 当你常驻 Claude Code、想一次装好现成的命令、agent 和行为模式框架时用它。 |
| [Get Shit Done (GSD)](get-shit-done.zh.md) | ✅ | C（6/6） | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 |
| [Compound Engineering](compound-engineering.zh.md) | ✅ | B（4/6） | 当你想要一套即插即用的 brainstorm→plan→work→review→compound 循环、并把经验跨会话沉淀复用时，就用它。 |
| [ECC](ecc.zh.md) | ✅ | B（6/6） | 当你想要一套有人维护、开箱即全的 Claude Code 底座（skill、agent、hook、memory 加安全扫描）时用它。 |
| [Spec Kit](spec-kit.zh.md) | ✅ | B（5/6） | GitHub 出品的面向 AI 编码智能体的 spec-driven 开发方法论；极其年轻，与 GitHub 生态深度绑定。 |
| [Spec-Anchored Agentic Development](spec-anchored-agentic-development.zh.md) | ✅ | B（3/6） | 永久 capability spec 加持续 spec-to-code conformance，但 bundle 仅面向 Claude Code，几乎没有采用历史。 |
| [USDAD](usdad.zh.md) | ✅ | C（4/6） | 可编辑的 planner／adversary／architect／executor 方法论文档，不是可安装 runtime，也不会机械执行流程。 |
| [QUAD Framework](quad.zh.md) | ✅ | D（4/6） | 覆盖较广的四 Circles 组织与部署参考，但软件采用专有许可，项目已不活跃，公开内容也不完整。 |
| [LTBL Experiment](ltbl-experiment.zh.md) | ✅ | D（4/6） | 未完成的实验索引，不是可运行软件、带评分的 benchmark，也不能证明某种方法胜出。 |
| [PURE](pure-agentic.zh.md) | ✅ | C（5/6） | 原生存入 Git 的 intent、schema、registry、handoff 与 phase-gate 机制；比纯文字方法更可执行，但仍很早期。 |
| [Learn Claude Code](learn-claude-code.zh.md) | ✅ | B（5/6） | 17 章动手课，逐机制复刻 Claude Code 式 harness；教的是内部原理，但它是课程，不是依赖包也不是产品。 |
| BMAD Method / Agent OS / SWE-bench / LTBL 实现组 / Beam | 未收录 | — | 各页提到的重角色方法、benchmark 基础设施与实现仓库。 |

## 什么该放这里

面向 agent 驱动开发的**方法论与元框架**——如何组织 spec、上下文、技能与工作流。不含运行时 agent 框架（见 `agent-frameworks`），不含纯技能合集（见 `agent-skills`）。
