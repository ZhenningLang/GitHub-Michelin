# harness-extensions

> 分类节点。往现有 coding-agent harness 上外挂能力——跨 agent 安装技能包，给只有图形界面的软件造一个 agent 能用的命令面，以及把额外的模型后端桥接进 harness。
> ← 返回 [agent-tooling](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Vercel Skills** | 当你想要一个 npm 风格的 CLI 来跨多个编码 agent 安装、查找、更新 SKILL.md 技能包时使用。 | D（6/6） | [→](vercel-skills.zh.md) |
| **CLI-Anything** | 当你想让编码 agent 驱动只有 GUI 的软件、走由应用自身引擎支撑的生成式 CLI harness 时用它——但它仍在 1.0 之前，且每个 harness 由社区维护。 | B（6/6） | [→](cli-anything.zh.md) |
| **codex-chatgpt-web** | 当 Codex 配额先耗尽、而付费的 ChatGPT 网页订阅闲着，想让 Codex 任务改记到 Web 套餐的独立额度上时用它——走的是一条上游随时能掐断的非官方浏览器桥。 | C（5/6） | [→](codex-chatgpt-web.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Vercel Skills](vercel-skills.zh.md) | ✅ | D（6/6） | 技能包的包管理器：跨约 70 个 agent 安装、查找、更新 `SKILL.md`——它负责分发能力，不负责定义能力。 |
| [CLI-Anything](cli-anything.zh.md) | ✅ | B（6/6） | 基于应用自身引擎生成的 CLI harness，让 agent 能驱动只有 GUI 的软件——覆盖广，但逐个 harness 由社区维护。 |
| [codex-chatgpt-web](codex-chatgpt-web.zh.md) | ✅ | C（5/6） | 把 ChatGPT 网页会话（Plus/Pro，含网页独占档位）桥进 Codex 模型选择器、记在 Web 套餐额度上——纯粹的配额套利，命脉握在 ChatGPT 的 DOM 和 ToS 手里。 |
| 各类技能包本身（agent-skills 条目） | 部分已收录 | — | 内容侧请看 [`agent-skills`](../../agent-skills/INDEX.zh.md)，那里是技能包本体而不是安装器。 |

## 什么该放这里

**扩展运行中 agent 能触达什么、能做什么**的手段：技能包的安装与发现，为只有图形界面的软件造命令面，以及把新提供方或新档位接到 harness 上的模型后端桥。不含 prompt/技能集合本体（见 `agent-skills`），也不含 agent 框架与运行时（见 `agent-frameworks`）。
