---
name: Claude Code Security Review
slug: claude-code-security-review
repo: https://github.com/anthropics/claude-code-security-review
category: ai-code-review
tags: [security, sast, github-action, claude, pr-review, slash-command]
language: Python
license: MIT
maturity: no tagged release, pinned via @main, active (2026-02)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-02-11T18:01:23Z
  default_branch: main
  default_branch_sha: 0c6a49f1fa56a1d472575da86a94dbc1edb78eda
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:41:34Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 223
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 414
        last_commit_age_days: 223
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.75
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
    adoption: { reason: ambiguous }
---

# Claude Code Security Review

Anthropic 出的 AI 安全审查器：一个 GitHub Action（外加 Claude Code 的 `/security-review` 斜杠命令），用 Claude 读 PR diff，并在出问题的具体行上贴出漏洞 finding。

![claude-code-security-review — 健康度雷达](../../assets/health/claude-code-security-review.zh.svg)

## 何时使用

你是一个中小型仓库的维护者，想要一道比正则/AST 模式匹配更进一步的 PR 安全闸门。传统 SAST 反复命中相同形状，却漏掉逻辑层面的 bug——比如一个 IDOR，它之所以成立是因为两个 handler 共享了 session；又比如一个注入，只有走某条特定代码路径才可达。你把这个 Action 加进 `.github/workflows/`，给它一个 Claude API key，之后每个 PR 它只分析改动过的文件、结合上下文推理 diff，并在它认为有漏洞的具体行留下带严重级别和修复建议的 review 评论。因为它“与语言无关”（本质是 Claude 在读代码，而非按语言写死规则集），同一套 workflow 就能覆盖你的 Python 服务、TypeScript 前端和 Terraform，无需分别配工具。

你也可能是一个日常用 Claude Code 的开发者，想在还没开 PR 之前就跑同样的检查。你对未提交的改动运行 `/security-review`，在本地拿到审查结果；还能把 `security-review.md` 拷进你仓库的 `.claude/commands/`，针对你的项目调 prompt。这个工具的整体卖点正是嘈杂扫描器的反面：一套有主张的误报过滤器，会丢掉 DoS/限流/开放重定向之类的 finding，让落地的评论都是值得动手处理的那些。

## 何时不用

- **你要审查不可信 / fork PR。** README 明确说它**未针对 prompt injection 做加固**，只应审查**可信 PR**；一个恶意 diff 可以尝试操纵审查器本身。对公开仓库，你必须把它挡在“维护者批准外部贡献者”之后——这是硬性运维约束，不是可选项。
- **你要免费或纯本地的扫描器。** 每次运行都调用 Claude API、按 token 计费（默认模型 `claude-opus-4-1-20250805`，单次默认 20 分钟超时）。PR 量大的仓库或开启 `run-every-commit: true` 会很贵——确定性的开源 SAST（Semgrep、CodeQL）没有按次 API 成本。
- **你需要确定性、可复现、合规级的结果。** LLM 审查器是非确定性的：同一份 diff 不同次运行可能浮现不同 finding。如果你需要稳定的规则 ID 集、抑制基线和审计可复现性，基于规则的 SAST 更合适。
- **你需要全代码库或定时深扫。** 它在设计上是 diff 感知的（只看 PR 改动文件），不是像一次完整 SAST 扫荡那样，在整个既有代码库里爬找潜在漏洞的爬虫。
- **你想要开箱即用的 SARIF / 第三方 security-tab 集成。** 输出是 PR 评论加一份结果 JSON 制品；[未验证] 没有文档化的原生 SARIF 导出，把 finding 接进 GitHub 的 code-scanning UI 不是一键的。
- **没有打 tag 的 release。** 用法 pin 的是 `@main`；没有 semver 发版线，所以你是用稳定性换“跟随一个未固定的移动分支”（或者自己 pin 某个 commit SHA）。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [open-code-review](open-code-review.zh.md) | ✅ | 当你要通用 LLM PR 审查、GitLab 集成或编码质量反馈时，选 open-code-review；当闸门必须是 Claude/GitHub Actions 原生且专注安全时，选本工具。 | 阿里出的基于 LLM 的代码审查器，面向 GitLab / 编码风格 + 质量；本工具则是安全专用，且是 Claude/GitHub-Actions 原生。 |
| [react-doctor](react-doctor.zh.md) | ✅ | 当你要确定性的 React 性能、正确性、可访问性和 agent 易错诊断时，选 react-doctor；当审查目标是跨 PR diff 的漏洞推理时，选本工具。 | React 专用的性能/正确性诊断，不是安全审查器；完全是另一类问题。 |
| Semgrep | 未收录 | 当可复现规则 ID、SARIF、本地免费运行和社区规则更重要时，选 Semgrep；当缺口是对可信 PR diff 做逻辑层安全推理时，选本工具。 | 确定性、基于规则的 SAST，带 SARIF 和庞大的社区规则集；快、免费、可复现——但被模式绑死，在逻辑/上下文型 bug 上更弱。 |
| GitHub CodeQL | 未收录 | 当你需要 GitHub 原生 code scanning 和深度数据流/污点分析时，选 CodeQL；当你想要 Claude 对改动行给出评论和修复文字时，选本工具。 | 深度数据流/污点分析，原生 code-scanning UI，对公开仓库免费；按语言、配置更重，无 LLM 修复文字。 |
| Claude Code GitHub Action（通用版） | 未收录 | 当你要通用 PR 协助或编码任务时，选通用 Claude Code Action；当你明确需要安全审计 prompt 和 finding 过滤时，选本工具。 | Anthropic 通用的 Claude Action，面向 PR/编码；并未专门做安全审计或 finding 过滤。 |
| Snyk Code | 未收录 | 当需求包含商业托管安全面板和依赖扫描时，选 Snyk Code；当你要的是由 Claude 评论驱动的单仓库开源 Action 时，选本工具。 | 商业 ML/SAST，带托管面板和依赖扫描；是托管 SaaS，而非单仓库开源 Action。 |

## 技术栈

- **语言：** Python（按 GitHub 约 89.6%；另有少量 TypeScript/JavaScript 用于工具链）。[未验证] 百分比是语言条快照，会漂移。
- **运行时模型：** Claude(Claude Code)——默认 `claude-opus-4-1-20250805`，可通过 `claude-model` 输入配置。
- **交付方式：** 一个组合式 GitHub Action（`anthropics/claude-code-security-review@main`）外加一个 `/security-review` Claude Code 斜杠命令。
- **核心模块：** `github_action_audit.py`（主审计）、`prompts.py`（审计 prompt 模板）、`findings_filter.py`（误报过滤）、`claude_api_client.py`（API 客户端）、`json_parser.py`（健壮 JSON 解析）、`evals/`（评测工具）。
- **测试：** `pytest claudecode -v`。

## 依赖

- **必需：** 一个 Anthropic Claude API key（须同时对 Claude API 与 Claude Code 启用），以 `claude-api-key` / GitHub secret 提供。
- **平台：** 开启 Actions 的 GitHub 仓库（主路径）；也可经 evals 框架在本地运行。
- **权限：** workflow 需要 `pull-requests: write`（发评论）与 `contents: read`。
- **Python 依赖：** `claudecode/requirements.txt` 很轻——`PyGithub>=1.59.0`、`requests>=2.28.0`、`anthropic>=0.39.0`（解析用 stdlib）。没有重型 ML 栈，因为推理在远端。
- **Claude CLI:** `claude` 命令行工具需单独安装（Action 会处理）；分析是通过它驱动的，而不仅是裸 API。

## 运维难度

**低。** 走顺路径就是一个约 15 行的 workflow 文件加一个 secret——无服务器、无数据存储、无需自托管模型（推理是远端 Claude API）。日常维护主要两件事：成本控制（token 花费随 PR 量和 `run-every-commit` 增长，注意 20 分钟的 `claudecode-timeout`）和 prompt-injection 约束（你必须配置 fork/外部贡献者的批准闸门）。调误报过滤器或自定义扫描指令是可选的文件式配置。主要残余风险是运维而非基础设施：pin `@main` 意味着上游改动可能在没有版本号变化的情况下改变行为。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）：** [推断] **在滑行，而非废弃。** 最近 push 在 2026-02——截至 2026-06 约四个月没动——且从未打过 tag release（用法 pin 的是 `@main`）。对一道安全闸门来说，这意味着：没有可锚定的版本线，行为可能在没有任何信号的情况下变化（甚至默默不再跟随当前 Claude 模型默认值）。没死，但比同类同侪走得更慢。
- **治理与背书：** [推断] 归属 `anthropics`（Anthropic 官方组织），这家厂商对它所驱动的 Claude-Code 生态有直接利益。相比单人维护，这降低了 bus-factor 风险，但它是厂商的橱窗/配套工具，而非基金会治理的项目——Anthropic 可以随时重新划定范围或悄悄降低优先级。
- **年龄与 Lindy：** [推断] 创建于 2025-08，截至 2026-06 约 10 个月——**偏年轻、Lindy 先验弱。** 在不足一岁的基础上叠加四个月的停滞，意味着它既无寿命也无强劲的近期势头；把它当成有用但未经证明的工具，而非长期押注。
- **风险标记：** [推断] 这是硬约束，不是可以推后的标记：README 声明它**未针对 prompt injection 做加固**，只能审查可信 PR——这是 LLM 审查器的结构性限制，不是一个会被补丁修掉的 bug。外加按次的 Claude API 成本与非确定性（见「何时不用」）。MIT 许可证，未发现 relicense 历史。

## 存疑（未验证）

- [未验证] `gh` 报告 `latestRelease: null`,star 约 5.37k（截至 2026-02，最近 push 2026-02-11）;GitHub star 不可靠且对时间敏感——仅供参考。
- [未验证] 无文档化的原生 SARIF / GitHub code-scanning 导出；把 finding 接进 security tab 可能需要自定义胶水代码。
- [未验证] 仓库语言占比（约 89.6% Python / 7.2% TS / 3.2% JS）是 GitHub 快照，随时间变化。
- [推断] 默认模型 `claude-opus-4-1-20250805` 是写作时 README 的默认值，上游可能上调；依赖某具体模型/成本画像前请核实当前默认。
- [推断] 单次成本与延迟取决于 diff 大小、所选模型和 `run-every-commit`；此处未发布一方成本数字。
- [未验证] `claudecode/requirements.txt`（2026-06-26 核实）仅 pin 了 `PyGithub>=1.59.0`、`requests>=2.28.0`、`anthropic>=0.39.0`，并注明 `claude` CLI 需单独安装——上游后续可能新增依赖。
