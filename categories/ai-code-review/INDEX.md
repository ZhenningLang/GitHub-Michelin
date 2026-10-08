# ai-code-review

> Category node. LLM-assisted code review that produces line-level findings on a diff or repo.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Open Code Review** | Use it when you want precise, line-level LLM review comments on Git diffs in CI without PR noise. | B (5/6) | [→](open-code-review.md) |
| **Claude Code Security Review** | Use it when you want Claude to read each trusted PR's diff for logic-level vulnerabilities and comment on the exact lines, in any language — but it is not hardened against prompt injection, so never run it on untrusted fork PRs. | B (4/6) | [→](claude-code-security-review.md) |
| **React Doctor** | Use it when a coding agent writes React and you want deterministic, repeatable checks for React-specific anti-patterns. | B (5/6) | [→](react-doctor.md) |
| **PR-Agent** | Use it when a team on GitHub, GitLab, Bitbucket, Azure DevOps or Gitea wants every PR auto-described and pre-reviewed by a model it pays for directly — but it sees only the compressed diff, and its license changed three times in 14 months. | A (5/6) | [→](pr-agent.md) |
| **Metis** | Use it when a security team wants an LLM's deep first pass over a large C/C++ codebase, or to triage another scanner's SARIF, on a model their policy allows — but it is a CLI with no PR bot, and results vary run to run. | B (5/6) | [→](metis.md) |
| **OpenReview** | Use it when your code is on GitHub, you already use Vercel, and you want an @-mentioned Claude reviewer that runs your linter and tests in a sandbox and pushes fixes — but it is a dormant Vercel demo with no LICENSE file. | D (5/6) | [→](openreview.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Open Code Review](open-code-review.md) | ✅ | B (5/6) | Use it when you want precise, line-level LLM review comments on Git diffs in CI without PR noise. |
| [Claude Code Security Review](claude-code-security-review.md) | ✅ | B (4/6) | Buys context-aware findings that pattern-based SAST misses; costs per-run Claude API tokens, non-deterministic results, and an untagged action you can only pin to @main. |
| [React Doctor](react-doctor.md) | ✅ | B (5/6) | Use it when a coding agent writes React and you want deterministic, repeatable checks for React-specific anti-patterns. |
| CodeRabbit / Greptile | 未收录 | — | Other LLM code-review tools named across the pages. |

## What belongs here

Tools whose primary job is **LLM-assisted code / security review** producing line-level findings. Not general agent frameworks, not non-LLM linters.
