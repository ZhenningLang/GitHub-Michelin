# native-cli-bridges

> 分类节点。在已有对话中通过已安装的原生 agent CLI 委派任务或进行跨模型评审。
> ← 返回[orchestration-and-review](../INDEX.zh.md) · root: [分类路由](../../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **AutoSwarm** | 从当前对话委派给已安装的原生 agent CLI，保留凭据和会话；工作区隔离与验收自行安排。 | B（6/6） | [→](autoswarm.zh.md) |
| **Claude Octopus** | 一个 Claude Code 插件：把单个任务扇出给至多约 8 个其他 AI 模型（Codex、Gemini、Perplexity、Ollama、OpenRouter 等），用它们之间的分歧作为盲点 / 共识闸门，全部由 `/octo:*` 斜杠命令驱动。 | C（6/6） | [→](claude-octopus.zh.md) |
| **Codex plugin for Claude Code** | 当你以 Claude Code 为主、手上已有 Codex 登录，想让 OpenAI 的 Codex 不离开会话就审你的改动、或接手卡住的任务时用它——但它只接一家厂商，rescue 默认可写，会泄漏中转进程，而且 2026-07 之后没有合并过任何东西。 | B（5/6） | [→](codex-plugin-cc.zh.md) |

## 横向对比

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [AutoSwarm](autoswarm.zh.md) | 已收录 | B（6/6） | 轻量原生调用与权限转接；不提供任务看板、工作树分配或自动验收。 |

## 什么该放这里

在已有 agent 对话中，通过已安装的原生 agent CLI 委派任务或跨模型评审的桥接层。任务流水线、容器工作区分配、操作控制台和 CLI 配置管理器留在[父分类](../INDEX.zh.md)。
