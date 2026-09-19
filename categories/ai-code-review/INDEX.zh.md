# ai-code-review

> 分类节点。LLM 辅助的代码评审：对 diff 或仓库产出行级问题。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Open Code Review** | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 | B（6/6） | [→](open-code-review.zh.md) |
| **Claude Code Security Review** | 当你想用 Claude 在可信 PR 上做上下文感知的安全审查、且接受按 token 计费与非确定性结果时使用。 | C（5/6） | [→](claude-code-security-review.zh.md) |
| **React Doctor** | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 | B（5/6） | [→](react-doctor.zh.md) |
| **PR-Agent** | 🚀 PR Agent: The Original Open-Source PR Reviewer.  This project It is not the Qodo free tier. | A（6/6） | [→](pr-agent.zh.md) |
| **Metis** | Metis is an open-source, AI-driven tool for deep security code review | B（5/6） | [→](metis.zh.md) |
| **OpenReview** | An open-source, self-hosted AI code review bot powered by Vercel. | D（4/6） | [→](openreview.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Open Code Review](open-code-review.zh.md) | ✅ | B（6/6） | 想在 CI 里对 Git diff 拿到精确行级 LLM review 评论、又不被噪声淹没时用它。 |
| [Claude Code Security Review](claude-code-security-review.zh.md) | ✅ | C（5/6） | 当你想用 Claude 在可信 PR 上做上下文感知的安全审查、且接受按 token 计费与非确定性结果时使用。 |
| [React Doctor](react-doctor.zh.md) | ✅ | B（5/6） | 当 coding agent 在写 React、你想要对 React 特有反模式做确定性、可重复的检查时用它。 |
| CodeRabbit / PR-Agent (Qodo) / Greptile | 未收录 | — | 各页对比里点到的其他 LLM 代码评审工具。 |

## 什么该放这里

主要职责是**LLM 辅助代码/安全评审**、产出行级问题的工具。不含通用 agent 框架，不含无 LLM 的传统 linter。
