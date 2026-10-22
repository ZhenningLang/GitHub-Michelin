# independent-runtimes

> 独立／社区编码运行时与已有 agent 的监督层。按运行时或监督机制选型；不表示没有商业支持，也不保证支持任意模型。
> ← 返回[terminal-agents](../INDEX.zh.md) · root: [分类路由](../../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Apache Maka (Incubating)** | agent 崩溃后，最后一次工具操作不该随窗口消失。Maka 把模型、工具和权限事件写入本地账本，供桌面和终端共同读取。 | B（6/6） | [→](maka.zh.md) |
| **aider** | 当你想在终端里让 AI 改你点名的文件、模型随你选、每次改动都自动成为可 `/undo` 的 git 提交时用它——但它实质上是一人维护，2025-08 之后没有再发版。 | B（6/6） | [→](aider.zh.md) |
| **Freebuff** | 想要一个不订阅、不填 API key 的终端编码 agent 时用它——托管模型由文字广告和每日额度买单，代价是提示词会被拿去做广告分析，也没有 shell 命令确认关卡。 | B（6/6） | [→](freebuff.zh.md) |
| **Letta Code** | 当你想要一个长期存在的终端编码 agent，把你的仓库和你的纠正跨会话记在它自己改写、用 git 记版本的记忆里时用它——但默认后端是 Letta Cloud，一天不止发一个版本，行为也会随记忆变化而漂移。 | B（6/6） | [→](letta-code.zh.md) |
| **OmO** | 你把一个大任务交给终端 agent，结果一晚上都在把它拽回正轨。OmO 把这些拖拽的活接了过去：一句 `mass ulw`，任务就变成一张并行 worker 的依赖图，每一块跑在合适的模型上、验证通过才算完成。 | B（5/6） | [→](oh-my-openagent.zh.md) |
| **Open Interpreter** | 当你想让 Kimi、GLM、DeepSeek、Qwen 这类便宜模型在 Codex 式终端 agent 里，套上各自家族习惯的 harness 干活时用它——但它是才几个月大的 Codex fork，过去出名的 Python REPL 已经不在这个仓库里。 | A（6/6） | [→](open-interpreter.zh.md) |
| **OpenCode** | 当你想要一个 MIT 许可的终端编码 agent，工作方式不变，底下在 75+ 家 provider、本地模型或 ChatGPT / Copilot 登录之间随意换时用它——但默认权限放行改文件和 shell 命令、不先问你，也用不了 Claude Pro/Max 订阅。 | A（5/6） | [→](opencode.zh.md) |
| **Pi** | 想要一个极简终端 agent、行为由你仓库里的文件决定——技能、prompt 模板、它自己也能写的 TypeScript 扩展——并且愿意自己承担沙箱时用它。 | B（5/6） | [→](pi.zh.md) |
| **Prime Agent** | 当长任务把对话窗口塞烂、你要模型对着持久 Python 内核写程序、派子 agent、断开终端还能接着跑时用它。 | B（6/6） | [→](prime-agent.zh.md) |
| **T3 Code** | 当一个本地 GUI 要驱动已经认证的 Codex、Claude、Cursor、OpenCode CLI 时用它。 | A（6/6） | [→](t3code.zh.md) |

## 对比矩阵

| 项目 | 是否收录 | 健康度 | 关键取舍 |
|---|---|---|---|
| [Apache Maka (Incubating)](maka.zh.md) | ✅ | B（6/6） | 优先要共享 Runtime Host 与执行事件记录；账本不证明补丁正确。 |
| [aider](aider.zh.md) | ✅ | B（6/6） | 优先要点名文件的结对编程与可撤销提交，而非更长的自主循环。 |
| [Freebuff](freebuff.zh.md) | ✅ | B（6/6） | 优先要免管密钥和账单的托管模型目录；须审查广告与代码外发代价。 |
| [Letta Code](letta-code.zh.md) | ✅ | B（6/6） | 优先要 agent 自改的跨会话记忆，而非提供方广度或极简核心。 |
| [OmO](oh-my-openagent.zh.md) | ✅ | B（5/6） | 优先要预装编排、记忆与模型混用；接受其源码可用许可。 |
| [Open Interpreter](open-interpreter.zh.md) | ✅ | A（6/6） | 优先要 Codex 机制之上的分模型 harness，而非换一套 agent 循环。 |
| [OpenCode](opencode.zh.md) | ✅ | A（5/6） | 优先要切换提供方与自主 plan/build 模式，而非每次编辑一次提交的结对编程。 |
| [Pi](pi.zh.md) | ✅ | B（5/6） | 优先要极简核心、文件式资源与 TypeScript 扩展；执行隔离自己负责。 |
| [Prime Agent](prime-agent.zh.md) | ✅ | B（6/6） | 优先要程序化折叠上下文与可断开的长任务；接受多进程运行时及无默认沙箱。 |
| [T3 Code](t3code.zh.md) | ✅ | A（6/6） | 优先要一个 GUI 监督已有编码 agent，而非替换它们的运行时。 |

## 什么该放这里

独立／社区编码运行时与已有 agent 的监督层。按运行时或监督机制选型；不表示没有商业支持，也不保证支持任意模型。
