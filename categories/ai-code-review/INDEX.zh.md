# ai-code-review

> 分类节点。LLM 辅助的代码评审：对 diff 或仓库产出行级问题。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Open Code Review** | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 | B（5/6） | [→](open-code-review.zh.md) |
| **Claude Code Security Review** | 当你想让 Claude 在每个可信 PR 上读 diff、找逻辑层面的漏洞并在具体行上评论、且不分语言时用它——但它没做 prompt injection 加固，绝不能用在不可信的 fork PR 上。 | B（4/6） | [→](claude-code-security-review.zh.md) |
| **React Doctor** | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 | B（5/6） | [→](react-doctor.zh.md) |
| **PR-Agent** | 当团队在 GitHub、GitLab、Bitbucket、Azure DevOps 或 Gitea 上，想让每个 PR 一打开就自动写好说明并预审一遍、模型费用直接付给厂商时用它——但它只看压缩后的改动，许可证 14 个月里还换了三次。 | A（5/6） | [→](pr-agent.zh.md) |
| **Metis** | 当安全团队想让大模型对一个大型 C/C++ 代码库做一遍深入初筛，或者给其他扫描器的 SARIF 降误报，并且只用安全策略允许的模型时用它——但它只是 CLI、没有 PR 机器人，每次运行的结果都会有出入。 | B（5/6） | [→](metis.zh.md) |
| **OpenReview** | 当你的代码在 GitHub、本来就用 Vercel，想要一个 @ 一下就在沙箱里跑 lint 和测试、还能推回修复的 Claude 审查者时用它——但它是一个停更的 Vercel 演示，仓库里没有 LICENSE 文件。 | D（5/6） | [→](openreview.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Open Code Review](open-code-review.zh.md) | ✅ | B（5/6） | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 |
| [Claude Code Security Review](claude-code-security-review.zh.md) | ✅ | B（4/6） | 换来基于模式的 SAST 会漏掉的上下文感知 finding；代价是每次运行按 token 计费、结果不确定，且 action 没有版本，只能钉 `@main`。 |
| [React Doctor](react-doctor.zh.md) | ✅ | B（5/6） | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 |
| CodeRabbit / Greptile | 未收录 | — | 各页对比里点到的其他 LLM 代码评审工具。 |

## 什么该放这里

主要职责是**LLM 辅助代码/安全评审**、产出行级问题的工具。不含通用 agent 框架，不含无 LLM 的传统 linter。
