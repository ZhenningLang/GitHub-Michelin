# engineering-workflows

> [personal-collections](../INDEX.zh.md) 的叶子。聚焦 coding-agent 工作流、工程流程、harness 设置、评审和架构的个人 skill pack。
> ← 上层 [personal-collections](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **agent-scripts** | 一位维护者用来在 Codex 与 Claude Code 之间共享一份 `AGENTS.MD` 和约 70 个 skill 的权威仓库，靠软链同步脚本分发；更像参考布局而非可移植的 skill 包（不少 skill 默认作者自己的机器）。 | B（4/5） | [→](agent-scripts.zh.md) |
| **antfu/skills** | Anthony Fu 个人精选、面向 Vue/Vite/Nuxt 栈的 agent skill 集合（其 ESLint/pnpm/Vitest/UnoCSS 偏好 + 生成与 vendored 的框架 skill），通过 skills CLI 安装。 | B（4/5） | [→](antfu-skills.zh.md) |
| **claude-code-harness** | 一套个人化 Claude Code harness：以插件形式装入受治理的 plan → work → review → release 循环，并附带 Go 原生 doctor CLI 诊断插件缓存与 skill 漂移。 | B（5/6） | [→](claude-code-harness.zh.md) |
| **Dimillian Skills** | 当你用 OpenAI Codex 做 iOS／macOS 开发、想要现成的 SwiftUI、Swift 并发、模拟器调试和 App Store 发布类 skill 时用它——但它是单作者、只面向 Codex 的快照，2026-03 之后没再更新，而它跟的 Apple beta 变得很快。 | C（4/5） | [→](dimillian-skills.zh.md) |
| **gstack** | Garry Tan 的私人 Claude Code harness：54 个 skill——约一半是角色人设（CEO、工程经理、设计师、QA、安全官、发布工程师），另一半是工具命令——外加一个 agent 真正驱动的浏览器，串成一条「规划 → 构建 → 评审 → 发布 → 复盘」冲刺流程。 | B（4/5） | [→](gstack.zh.md) |
| **andrej-karpathy-skills** | 当你的 Claude Code 或 Cursor agent 爱过度设计、顺手改无关文件、没验证就说完成，而你想用一份约 65 行的 `CLAUDE.md` 基础层压住这些毛病时用它——但它只是建议性文字，且是第三方提炼，并非 Karpathy 本人所写。 | C（3/5） | [→](karpathy-skills.zh.md) |
| **PUA** | 一个高能动性人设 skill 包，用职场 PUA/PIP 话术逼 coding agent 穷尽调试路径。 | C（4/6） | [→](pua.zh.md) |
| **Qiushi-Skill** | 一套方法论 skill 包，用“实事求是”加唯物辩证法思维工具武装 coding agent。 | B（4/6） | [→](qiushi-skill.zh.md) |
| **shaping-skills** | Ryan Singer 的个人 Claude Code skill 包，把 Shape Up shaping 带进 coding agent，让 AI 写代码前先框定要做什么。 | E（4/5） | [→](shaping-skills.zh.md) |
| **TÂCHES CC Resources** | 当你常驻 Claude Code、总在手搓新的 slash 命令、subagent、hook 或 MCP server，想要一套元生成 skill 加审计 subagent 来规整这件事时用它——但它是单维护者、只认 Claude Code 的快照，2026-04 之后没再更新。 | C（4/5） | [→](taches-cc-resources.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [agent-scripts](agent-scripts.zh.md) | ✅ | B（4/5） | 当你要把自己的规则和 skill 分发到多个仓库与 agent 时最合适；借它的布局，别照搬它的私人 skill。 |
| [antfu/skills](antfu-skills.zh.md) | ✅ | B（4/5） | 当你的技术栈匹配 Anthony Fu 的 Vue/Vite/Nuxt 约定时最合适。 |
| [claude-code-harness](claude-code-harness.zh.md) | ✅ | B（5/6） | 需要带 doctor 工具的受治理 Claude Code harness 时最合适。 |
| [Dimillian Skills](dimillian-skills.zh.md) | ✅ | C（4/5） | 换来通用 skill 包少有的 Swift／SwiftUI 深度；代价是只能装进 Codex，且 skill 在作者两次更新之间就可能过时。 |
| [gstack](gstack.zh.md) | ✅ | B（4/5） | 想要某位操作者的整套冲刺闭环（角色技能加真浏览器驱动）而不是自己拼零件时最合适。 |
| [andrej-karpathy-skills](karpathy-skills.zh.md) | ✅ | C（3/5） | 换来一份零配置、即插即用的小规则文件；代价是毫无强制力，并与你已有的全局 agent 规则高度重叠。 |
| [PUA](pua.zh.md) | ✅ | C（4/6） | 适合刻意使用高压人设 prompt，而不是中性流程政策。 |
| [Qiushi-Skill](qiushi-skill.zh.md) | ✅ | B（4/6） | 当你想要“实事求是”和调查式推理风格时最合适。 |
| [shaping-skills](shaping-skills.zh.md) | ✅ | E（4/5） | 适合 Shape Up 式 shaping；许可证和维护信号让健康度更弱。 |
| [TÂCHES CC Resources](taches-cc-resources.zh.md) | ✅ | C（4/5） | 换来一次插件安装就能规整产出 Claude Code 扩展的“工厂”；代价是接受一个人的编写风格，审计器只是建议，也没有可 pin 的版本。 |

## 什么该放这里

主要价值是改善 coding agent 工程工作流、评审循环、架构判断、harness 行为或编码人设的个人合集。
