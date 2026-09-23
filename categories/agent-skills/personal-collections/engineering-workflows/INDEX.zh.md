# engineering-workflows

> [personal-collections](../INDEX.zh.md) 的叶子。聚焦 coding-agent 工作流、工程流程、harness 设置、评审和架构的个人 skill pack。
> ← 上层 [personal-collections](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **antfu/skills** | Anthony Fu 个人精选、面向 Vue/Vite/Nuxt 栈的 agent skill 集合（其 ESLint/pnpm/Vitest/UnoCSS 偏好 + 生成与 vendored 的框架 skill），通过 skills CLI 安装。 | B（4/5） | [→](antfu-skills.zh.md) |
| **claude-code-harness** | 一套个人化 Claude Code harness：以插件形式装入受治理的 plan → work → review → release 循环，并附带 Go 原生 doctor CLI 诊断插件缓存与 skill 漂移。 | B（5/6） | [→](claude-code-harness.zh.md) |
| **Dimillian Skills** | 某开发者个人精选的 16 个自包含 Codex skill，重心压在 Apple 平台，外加通用评审／重构 swarm。 | C（4/5） | [→](dimillian-skills.zh.md) |
| **gstack** | Garry Tan 的私人 Claude Code harness：54 个 skill——约一半是角色人设（CEO、工程经理、设计师、QA、安全官、发布工程师），另一半是工具命令——外加一个 agent 真正驱动的浏览器，串成一条「规划 → 构建 → 评审 → 发布 → 复盘」冲刺流程。 | B（4/5） | [→](gstack.zh.md) |
| **andrej-karpathy-skills** | 一个行为准则包，把 Karpathy 关于 LLM 编码的四条原则注入 Claude Code / Cursor。 | C（4/5） | [→](karpathy-skills.zh.md) |
| **PUA** | 一个高能动性人设 skill 包，用职场 PUA/PIP 话术逼 coding agent 穷尽调试路径。 | D（5/6） | [→](pua.zh.md) |
| **Qiushi-Skill** | 一套方法论 skill 包，用“实事求是”加唯物辩证法思维工具武装 coding agent。 | B（4/5） | [→](qiushi-skill.zh.md) |
| **shaping-skills** | Ryan Singer 的个人 Claude Code skill 包，把 Shape Up shaping 带进 coding agent，让 AI 写代码前先框定要做什么。 | E（4/5） | [→](shaping-skills.zh.md) |
| **TÂCHES CC Resources** | TÂCHES 的个人化 Claude Code 扩展合集，含 slash 命令、元生成器 skill、审计 subagent 和 hooks，可作为 marketplace 插件安装。 | B（4/5） | [→](taches-cc-resources.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [antfu/skills](antfu-skills.zh.md) | ✅ | B（4/5） | 当你的技术栈匹配 Anthony Fu 的 Vue/Vite/Nuxt 约定时最合适。 |
| [claude-code-harness](claude-code-harness.zh.md) | ✅ | B（5/6） | 需要带 doctor 工具的受治理 Claude Code harness 时最合适。 |
| [Dimillian Skills](dimillian-skills.zh.md) | ✅ | C（4/5） | 适合 Apple 平台 Codex 工作流和个人评审／重构 swarm。 |
| [gstack](gstack.zh.md) | ✅ | B（4/5） | 想要某位操作者的整套冲刺闭环（角色技能加真浏览器驱动）而不是自己拼零件时最合适。 |
| [andrej-karpathy-skills](karpathy-skills.zh.md) | ✅ | C（4/5） | 适合作为紧凑行为准则包，而不是完整 harness。 |
| [PUA](pua.zh.md) | ✅ | D（5/6） | 适合刻意使用高压人设 prompt，而不是中性流程政策。 |
| [Qiushi-Skill](qiushi-skill.zh.md) | ✅ | B（4/5） | 当你想要“实事求是”和调查式推理风格时最合适。 |
| [shaping-skills](shaping-skills.zh.md) | ✅ | E（4/5） | 适合 Shape Up 式 shaping；许可证和维护信号让健康度更弱。 |
| [TÂCHES CC Resources](taches-cc-resources.zh.md) | ✅ | B（4/5） | 适合想要个人化 Claude Code 元工具合集，而不是单个窄 skill。 |

## 什么该放这里

主要价值是改善 coding agent 工程工作流、评审循环、架构判断、harness 行为或编码人设的个人合集。
