---
name: Anthropic Cybersecurity Skills
slug: anthropic-cybersecurity-skills
repo: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
category: security
tags: [agent-skills, cybersecurity, threat-hunting, incident-response, mitre-attack, claude-code]
language: Python
license: Apache-2.0
maturity: v1.3.0, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-26T14:37:50Z
  default_branch: main
  default_branch_sha: 673da1f3b0b7be34ffc9624ef3858fe45f1c3bed
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:40:01Z
  overall: B
  overall_score: 3.0
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 23
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "N/A"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 209
        last_commit_age_days: 23
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 16
        top1_share: 0.78
        top3_share: 0.917
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# Anthropic Cybersecurity Skills

一个大型网络安全技能包（本次核查约 817 个技能），把结构化、已对齐框架的安全工作流加载进 coding agent——每个技能是一份 `SKILL.md`（何时使用 → 前置条件 → 分步工作流 → 验证），并交叉映射到 MITRE ATT&CK、NIST CSF、ATLAS、D3FEND、NIST AI RMF 与 MITRE F3。

![anthropic-cybersecurity-skills — 健康度雷达](../../../assets/health/anthropic-cybersecurity-skills.zh.svg)

## 何时使用

你是安全工程师、SOC 分析师或 DFIR 应急响应人员，驱动 Claude Code（或 GitHub Copilot、Codex CLI、Cursor、Gemini CLI……）做真实的防御工作——研判告警、狩猎横向移动、解析内存转储，或把发现回映射到 ATT&CK 写进事件报告。Agent 技术上能跑 Volatility、写 Sigma 规则、查 SIEM，但它不懂地道的操作流程、正确的参数，也不知道某个观测对应哪个框架技术——于是它即兴发挥、跳过验证，或贴错 TTP。你希望它照着资深分析师的步骤走，面前摆着经过审核的 runbook 和标准映射。

你为此引入这个技能包，等于把一套安全 playbook 一次性装上（`npx skills add mukul975/Anthropic-Cybersecurity-Skills` 或 `git clone`），agent 即获得覆盖 29 个领域的按需技能——云安全、威胁狩猎、威胁情报、网络安全、Web 应用安全、数字取证、恶意软件分析等等。每个技能附带 `SKILL.md` 加 `references/`（框架映射、工作流）、`scripts/`（辅助 Python）、`assets/`（检查清单、报告模板）；agent 只拉取任务需要的那几个，且工作流已映射到 ATT&CK / D3FEND / NIST，使报告说出评审者期望的术语。[推断]

## 何时不用

- **你已经维护着一套自己信任的安全技能 / runbook 栈。** 这个包广而强势；在你自己的 runbook 之上再叠 ~817 个技能会带来指令冲突和双重路由。每个领域只保留一个事实源。
- **你的 harness 没有技能加载器。** 它通过 agentskills.io / 开放 Agent Skills 标准激活（Claude Code、Copilot、Codex、Cursor、Gemini CLI、MCP 兼容 agent）。在没有加载器的自研 agent 上，`SKILL.md` 只是惰性 markdown，不会自动激活。
- **你需要安全工具预装就位。** 技能只讲*怎么用* Volatility、nmap、YARA 等——不会带来这些二进制、SIEM、实验数据或云凭据。这些仍由你自己准备和运维，任何攻击性动作的授权范围也由你负责。
- **你要的是强制护栏，而非建议。** 技能文档是建议性的 prompt 上下文，不是沙箱或策略引擎；agent 仍可能跑出破坏性或越界的命令。攻击性 / 红队类技能带有真实的法律与操作风险，无论技能怎么写都需要显式授权。
- **你需要稳定、经过审计的安全基线。** 这是快速迭代的单作者仓库（近几个版本从 734 → 817 个技能）；内容和框架版本随版本漂移，且广度意味着各技能深度与审核程度不一。请锁定版本并逐一审查你依赖的具体技能。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| 个人 / 团队技能栈中 `/guard-secure`、`/guard-threat-model` 风格的安全技能 | 未收录 | 可强制执行和可信精选比覆盖面更重要时，选 harness 原生安全闸门。 | 你已信任、且能在 hook 中强制执行的手工精选、harness 原生安全闸门；覆盖面窄得多。本包用可强制性和精选度，换 800+ 现成领域工作流。 |
| MITRE ATT&CK Navigator / 框架官方文档（自己读原始映射） | 未收录 | 权威、当前的技术数据比 agent 工作流更重要时，选框架官方文档。 | 权威、始终最新的技术数据，但没有 agent 可执行的工作流——你得手动把 ATT&CK 接到操作流程。本包把工作流预绑定到（某一快照版的）这些框架。 |
| 安全类 MCP server（如包装 SIEM/扫描器的工具型 MCP） | 未收录 | 缺的是带结构化 I/O 的实时工具访问时，选安全类 MCP server。 | 给 agent 提供带结构化 I/O 的实时*工具访问*；本包提供*流程知识*而非连通性。两者互补而非替代——一个懂步骤，一个能对系统执行。 |
| 逐任务自写 prompt（自己写 `SKILL.md`） | 未收录 | 最大控制力和零冗余表面比成套包更重要时，选自写 prompt。 | 控制力最强、零冗余表面，但你得为每个领域自建并维护精选、对齐框架的 runbook，而不是装一个已审核的成套包。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— 非常活跃且迭代快：最新发布 v1.3.0（2026-06），最后推送 2026-06，未归档（截至 2026-06）。技能数近几个版本从 734 增到约 817，内容和框架版本随版本漂移——锁版本，并逐一审查你依赖的具体技能。
- **治理与 bus factor** —— 单作者社区仓库（`User` 所有，`mukul975`），约 22k stars。一个维护者把控 800+ 个深度不一的安全技能；对安全相关内容来说，这是很重的单作者 bus factor。名字里的「Anthropic」**不是**背书——这是社区项目，不是官方发布。
- **年龄与 Lindy** —— 创建于 2026-02，截至 2026-06 约 0 年：年轻且被热捧（短期内 star 数高），Lindy 上未经验证。对*安全* runbook 而言，「新」会叠加审查负担——这些工作流都没有长期 track record。
- **风险旗标** —— Apache-2.0（复用清晰），但技能是建议性的 prompt 上下文，**不是**沙箱、已验证的检测规则或策略引擎；攻击性/红队类技能带有真实法律与操作风险，无论技能怎么写都需显式授权。框架版本和技能数声明均来自 README。

## 存疑（未验证）

- [未验证] 截至 2026-06-26 的元数据（GitHub）：最新发布 v1.3.0（2026-06-22 发布），仓库最后 push 于 2026-06-22，许可证 Apache-2.0，主语言 Python（少量 PowerShell），未归档——依赖某具体版本行为或技能清单前请重新核验。
- [未验证] Star 数（GitHub 2026-06-26 约 21.5k）不可靠且随时间变化；仅作参考，不能当作质量或信任信号。
- [未验证] 技能数（约 817）及各领域细分（如云安全 66、威胁狩猎 58、威胁情报 52）来自项目 README/描述，随版本漂移；据称 v1.0.0 发布时为 734 个技能。请查看当前 `skills/` 目录而非依赖此清单。
- [未验证] 声称的框架版本（MITRE ATT&CK v19.1、NIST CSF 2.0、ATLAS v5.4、D3FEND v1.3、NIST AI RMF 1.0、MITRE F3 v1.1）以及“20+/26+ 平台”兼容声明均来自 README；实际映射准确度和各 harness 激活保真度此处未独立确认。
- [未验证] 仓库提供辅助 Python 脚本和模板，但据称没有独立 CLI 或 MCP server；`agentskills.io` 标准与 `npx skills add` 安装器是外部依赖，其可用性 / 行为此处未验证。
- [未验证] 仓库名带 "Anthropic" 字样，但这是 `mukul975` 的社区项目，并非 Anthropic 官方发布——不要把名字当作背书。
- [推断] 由于技能是加载进 agent 的 markdown 文档，其指导是建议性的——agent 仍可能执行错误、破坏性或越界的安全操作；它们不是强制控制、已验证的检测规则，也不能替代授权和人工复核。
