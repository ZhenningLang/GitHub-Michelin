# coding-agent-harnesses

> 分类节点。可安装的命令 / skill / agent 套件，把现成的 SDLC 层装到现有 coding agent 上。
> ← 返回[agent-dev-methodology](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **ub-mode** | 阅读测试先行与独立质量工具配对的短工程清单；没有可执行门禁，也未声明许可。 | D（4/5） | [→](ub-mode.zh.md) |
| **Claude Code Templates** | 当你想在一个大目录里逛逛、单点自选地安装现成的 Claude Code agent、命令、hook、MCP 和 skill，而不是自己从头写时，用它。 | B（6/6） | [→](claude-code-templates.zh.md) |
| **Claude Code Game Studios** | 在 Claude Code 里把游戏点子做成检查过的可玩浏览器原型，再逐步长大；单人维护、要克隆进仓库的模板，只支持 Claude Code。 | C（5/6） | [→](claude-code-game-studios.zh.md) |
| **Compound Engineering** | 当你想要一套即插即用的 brainstorm→plan→work→review→compound 循环、并把经验跨会话沉淀复用时，就用它。 | B（4/5） | [→](compound-engineering.zh.md) |
| **ECC** | 当你想要一套有人维护、开箱即全的 Claude Code 底座（skill、agent、hook、memory 加安全扫描）时用它。 | B（6/6） | [→](ecc.zh.md) |
| **LifeOS** | 当你想让 coding agent 跨会话携带*你自己*——沉淀好的个人档案、记忆和现状→理想状态仪表盘——而不是再多一套编码工作流时，用它。 | B（6/6） | [→](lifeos.zh.md) |
| **SuperClaude Framework** | 当你常驻 Claude Code、想一次装好现成的命令、agent 和行为模式框架时用它。 | B（6/6） | [→](superclaude.zh.md) |
| **Superpowers** | 当你想给编程 agent 装一套即插即用的「头脑风暴→计划→TDD→验证」SDLC 方法论时用它。 | B（4/5） | [→](superpowers.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [ub-mode](ub-mode.zh.md) | 已收录 | D（4/5） | 一份提示词而非插件运行时；须审查推送、清理指令和未核清的复用权限。 |
| [Claude Code Templates](claude-code-templates.zh.md) | ✅ | B（6/6） | 当你想在一个大目录里逛逛、单点自选地安装现成的 Claude Code agent、命令、hook、MCP 和 skill，而不是自己从头写时，用它。 |
| [Claude Code Game Studios](claude-code-game-studios.zh.md) | ✅ | C（5/6） | 换来游戏专用的点子→简报→构建→无头自检流程，外加钩子和总监门禁；代价是绑定 Claude Code、每个仓库手工升级、巴士因子为 1。 |
| [Compound Engineering](compound-engineering.zh.md) | ✅ | B（4/5） | 当你想要一套即插即用的 brainstorm→plan→work→review→compound 循环、并把经验跨会话沉淀复用时，就用它。 |
| [ECC](ecc.zh.md) | ✅ | B（6/6） | 当你想要一套有人维护、开箱即全的 Claude Code 底座（skill、agent、hook、memory 加安全扫描）时用它。 |
| [LifeOS](lifeos.zh.md) | ✅ | B（6/6） | 当你想在 Claude Code 里装一个常驻的个人生活层（TELOS 档案、记忆、Pulse 仪表盘）时用它；要跨 harness 的工程底座选 ECC。 |
| [SuperClaude Framework](superclaude.zh.md) | ✅ | B（6/6） | 当你常驻 Claude Code、想一次装好现成的命令、agent 和行为模式框架时用它。 |
| [Superpowers](superpowers.zh.md) | ✅ | B（4/5） | 当你想给编程 agent 装一套即插即用的「头脑风暴→计划→TDD→验证」SDLC 方法论时用它。 |

## 什么该放这里

装进宿主 coding agent（Claude Code、Codex、Cursor…）的发行物——slash 命令、skills、子 agent、hooks、记忆。不含底层 runtime（见 `agent-frameworks`）。
