# spec-driven-development

> 分类节点。面向 coding agent 的 spec / 计划 / 上下文优先方法论——你遵循的流程，而非你安装的 harness。
> ← 返回[agent-dev-methodology](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **12-Factor Agents** | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 | C（3/6） | [→](12-factor-agents.zh.md) |
| **Get Shit Done (GSD)** | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 | C（6/6） | [→](get-shit-done.zh.md) |
| **PURE** | 当 coding-agent intent lineage 必须落进 Git 跟踪的 spec、schema、registry、phase gate 和带测试 Shell 脚本时用它；它仍是单维护者的早期 v0.1 框架。 | C（5/6） | [→](pure-agentic.zh.md) |
| **Spec-Anchored Agentic Development** | 当永久 capability spec 和持续 spec-to-code conformance 比广泛 harness 支持更重要时用它；bundle 仅面向 Claude Code，而且项目只有十多天历史。 | B（3/6） | [→](spec-anchored-agentic-development.zh.md) |
| **Spec Kit** | 当你想要 GitHub 出品的面向 AI 编码智能体的 spec-driven 开发方法论时用它——但它极其年轻，且与 GitHub 生态深度绑定。 | B（5/6） | [→](spec-kit.zh.md) |
| **USDAD** | 当你要可编辑、文字优先的 planner／adversary／architect／executor 方法论原稿时用它；它是单提交文档工件，不是可安装 runtime 或强制执行的工作流。 | C（4/6） | [→](usdad.zh.md) |
| **BMAD Method** | 当你要的是角色驱动的端到端 agent 方法（analyst、PM、架构、UX、开发、复核），而不是薄薄的 spec 管线时用它——并把飞快的涨星曲线当成未经验证。 | B（4/6） | [→](bmad-method.zh.md) |
| **Agent OS** | 当你要把项目 standards 装进去并选择性注入、在实现前先塑形计划时用它——发布线自 v3.0.0（2026-01）后一直很安静。 | B（4/6） | [→](agent-os.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [12-Factor Agents](12-factor-agents.zh.md) | ✅ | C（3/6） | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 |
| [Get Shit Done (GSD)](get-shit-done.zh.md) | ✅ | C（6/6） | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 |
| [PURE](pure-agentic.zh.md) | ✅ | C（5/6） | 原生存入 Git 的 intent、schema、registry、handoff 与 phase-gate 机制；比纯文字方法更可执行，但仍很早期。 |
| [Spec-Anchored Agentic Development](spec-anchored-agentic-development.zh.md) | ✅ | B（3/6） | 永久 capability spec 加持续 spec-to-code conformance，但 bundle 仅面向 Claude Code，几乎没有采用历史。 |
| [Spec Kit](spec-kit.zh.md) | ✅ | B（5/6） | GitHub 出品的面向 AI 编码智能体的 spec-driven 开发方法论；极其年轻，与 GitHub 生态深度绑定。 |
| [USDAD](usdad.zh.md) | ✅ | C（4/6） | 可编辑的 planner／adversary／architect／executor 方法论文档，不是可安装 runtime，也不会机械执行流程。 |
| [BMAD Method](bmad-method.zh.md) | ✅ | B（4/6） | 重角色的端到端方法（analyst／PM／架构／UX／开发／复核），以 skills 与 agent persona 交付；项目很年轻，涨星曲线快到可疑。 |
| [Agent OS](agent-os.zh.md) | ✅ | B（4/6） | 薄薄的 standards + spec 层，安装项目约定并按需选择性注入；发布线自 v3.0.0（2026-01）后一直很安静。 |
| [SWE-bench](../../llm-eval/swe-bench.zh.md) | ✅ | B（6/6） | benchmark 基础设施，收录在 `llm-eval` 而不是本类目——它给补丁打分，不是开发方法。 |
| LTBL 实现组 / Beam | 未收录 | — | `study-and-experiments/` 里点到的 LTBL 实现仓库。`Beam` 刻意不收录：名字搜索命中的是 apache/beam，而各页指的是另一个项目——要先把仓库人工认准。 |

## 什么该放这里

散文优先或 spec 优先的方法论与原则集——决定在 agent 改代码之前*先写下什么*、按什么顺序写。
