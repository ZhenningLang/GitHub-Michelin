# spec-driven-development

> 分类节点。面向 coding agent 的 spec / 计划 / 上下文优先方法论——你遵循的流程，而非你安装的 harness。
> ← 返回[agent-dev-methodology](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **12-Factor Agents** | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 | B（4/6） | [→](12-factor-agents.zh.md) |
| **Get Shit Done (GSD)** | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 | C（6/6） | [→](get-shit-done.zh.md) |
| **PURE** | 当 coding-agent intent lineage 必须落进 Git 跟踪的 spec、schema、registry、phase gate 和带测试 Shell 脚本时用它；它仍是单维护者的早期 v0.1 框架。 | C（5/6） | [→](pure-agentic.zh.md) |
| **Spec-Anchored Agentic Development** | 当永久 capability spec 和持续 spec-to-code conformance 比广泛 harness 支持更重要时用它；bundle 仅面向 Claude Code，而且项目只有十多天历史。 | B（3/6） | [→](spec-anchored-agentic-development.zh.md) |
| **Spec Kit** | 当你想要 GitHub 出品的面向 AI 编码智能体的 spec-driven 开发方法论时用它——但它极其年轻，且与 GitHub 生态深度绑定。 | B（5/6） | [→](spec-kit.zh.md) |
| **USDAD** | 当你要可编辑、文字优先的 planner／adversary／architect／executor 方法论原稿时用它；它是单提交文档工件，不是可安装 runtime 或强制执行的工作流。 | C（4/6） | [→](usdad.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [12-Factor Agents](12-factor-agents.zh.md) | ✅ | B（4/6） | 当你想用一套生产级 agent 设计原则来指导手写或薄框架 agent 时使用。 |
| [Get Shit Done (GSD)](get-shit-done.zh.md) | ✅ | C（6/6） | 当你靠 coding agent 写代码、想要一条规格驱动、每阶段全新上下文、对抗 context rot 的构建流水线时用它。 |
| [PURE](pure-agentic.zh.md) | ✅ | C（5/6） | 原生存入 Git 的 intent、schema、registry、handoff 与 phase-gate 机制；比纯文字方法更可执行，但仍很早期。 |
| [Spec-Anchored Agentic Development](spec-anchored-agentic-development.zh.md) | ✅ | B（3/6） | 永久 capability spec 加持续 spec-to-code conformance，但 bundle 仅面向 Claude Code，几乎没有采用历史。 |
| [Spec Kit](spec-kit.zh.md) | ✅ | B（5/6） | GitHub 出品的面向 AI 编码智能体的 spec-driven 开发方法论；极其年轻，与 GitHub 生态深度绑定。 |
| [USDAD](usdad.zh.md) | ✅ | C（4/6） | 可编辑的 planner／adversary／architect／executor 方法论文档，不是可安装 runtime，也不会机械执行流程。 |
| BMAD Method / Agent OS / SWE-bench / LTBL 实现组 / Beam | 未收录 | — | 各页提到的重角色方法、benchmark 基础设施与实现仓库。 |

## 什么该放这里

散文优先或 spec 优先的方法论与原则集——决定在 agent 改代码之前*先写下什么*、按什么顺序写。
