# terminal-agents

> 分类节点。终端优先的 coding agent 与 CLI 结对编程工具。
> ← 返回[coding-agents](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **aider** | 当你想在终端里让 AI 改你点名的文件、模型随你选、每次改动都自动成为可 `/undo` 的 git 提交时用它——但它实质上是一人维护，2025-08 之后没有再发版。 | B（6/6） | [→](aider.zh.md) |
| **Codex** | 当你已经在付 ChatGPT 的钱，想让这份订阅在终端里跑一个带沙箱的“改代码、跑测试、再修”循环时用它——但自定义模型提供方必须实现 Responses API，OpenAI 不收外部 PR，0.x 接口几乎天天在变。 | A（5/6） | [→](codex.zh.md) |
| **Freebuff** | 想要一个不订阅、不填 API key 的终端编码 agent 时用它——托管模型由文字广告和每日额度买单，代价是提示词会被拿去做广告分析，也没有 shell 命令确认关卡。 | B（6/6） | [→](freebuff.zh.md) |
| **Gemini CLI** | 当你想要一个用普通 Google 账号登录、在每日额度内免费用、上下文窗口装得下大仓库的终端 agent 时用它——但它只连 Gemini，没有离线或本地模型这条路。 | A（6/6） | [→](gemini-cli.zh.md) |
| **Letta Code** | 当你想要一个长期存在的终端编码 agent，把你的仓库和你的纠正跨会话记在它自己改写、用 git 记版本的记忆里时用它——但默认后端是 Letta Cloud，一天不止发一个版本，行为也会随记忆变化而漂移。 | B（6/6） | [→](letta-code.zh.md) |
| **OmO** | 你把一个大任务交给终端 agent，结果一晚上都在把它拽回正轨。OmO 把这些拖拽的活接了过去：一句 `mass ulw`，任务就变成一张并行 worker 的依赖图，每一块跑在合适的模型上、验证通过才算完成。 | B（5/6） | [→](oh-my-openagent.zh.md) |
| **Open Interpreter** | 当你想让 Kimi、GLM、DeepSeek、Qwen 这类便宜模型在 Codex 式终端 agent 里，套上各自家族习惯的 harness 干活时用它——但它是才几个月大的 Codex fork，过去出名的 Python REPL 已经不在这个仓库里。 | A（6/6） | [→](open-interpreter.zh.md) |
| **OpenCode** | 当你想要一个 MIT 许可的终端编码 agent，工作方式不变，底下在 75+ 家 provider、本地模型或 ChatGPT / Copilot 登录之间随意换时用它——但默认权限放行改文件和 shell 命令、不先问你，也用不了 Claude Pro/Max 订阅。 | A（5/6） | [→](opencode.zh.md) |
| **Pi** | 想要一个极简终端 agent、行为由你仓库里的文件决定——技能、prompt 模板、它自己也能写的 TypeScript 扩展——并且愿意自己承担沙箱时用它。 | B（5/6） | [→](pi.zh.md) |
| **Prime Agent** | 当长任务把对话窗口塞烂、你要模型对着持久 Python 内核写程序、派子 agent、断开终端还能接着跑时用它。 | B（6/6） | [→](prime-agent.zh.md) |
| **T3 Code** | 当一个本地 GUI 要驱动已经认证的 Codex、Claude、Cursor、OpenCode CLI 时用它。 | A（6/6） | [→](t3code.zh.md) |

## 什么该放这里

终端优先的 coding agent 与 CLI 结对编程工具。
