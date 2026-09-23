---
name: Agent Skills (addyosmani)
slug: addyosmani-agent-skills
repo: https://github.com/addyosmani/agent-skills
category: engineering
tags: [skills, code-quality, web-performance, sdlc, claude-code, cursor, antigravity, plugin]
language: Shell
license: MIT
maturity: v0.6.2, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-28T18:11:20Z
  default_branch: main
  default_branch_sha: aba7c4e9695c363e65cb59effe926c7f1d1abe3d
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:38:43Z
  overall: A
  overall_score: 3.5
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
        last_commit_age_days: 2
        active_weeks_13: 13
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
        repo_age_days: 219
        last_commit_age_days: 2
        cohort: skill-pack
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 78
        top1_share: 0.331
        top3_share: 0.517
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
    responsiveness: { reason: type_na }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# Agent Skills (addyosmani)

一套约 24 个「生产级工程」技能包——把资深工程师用的工作流、质量闸门和评审清单装进你的 coding agent，再通过约 8 个贯穿研发生命周期的斜杠命令路由（`/spec`、`/plan`、`/build`、`/test`、`/review`、`/webperf`、`/code-simplify`、`/ship`）。

![addyosmani-agent-skills — 健康度雷达](../../../assets/health/addyosmani-agent-skills.zh.svg)

## 何时使用

你是一名工程师，在真实代码库上跑 AI coding agent(Claude Code、Cursor、Antigravity、Gemini CLI、Windsurf、Copilot、OpenCode、Kiro……)，而 agent 的*工程素养*正是短板：它一口气提交 500 行无测试的 diff，不打开 DevTools 就“优化”性能，给自己的代码做橡皮图章式 review，跳过人类 reviewer 会坚持的安全和迁移步骤。你要的不是一句泛泛的“做个好工程师”提示词，而是真正的资深工程师手册：测试金字塔与红-绿-重构、OWASP 式加固、Core Web Vitals 与打包体积剖析、契约优先的 API 设计、ADR、可观测性、安全的弃用/迁移，以及取自《Software Engineering at Google》的小改动纪律（约 100 行的变更、trunk-based、anti-rationalization 表）。

当你希望这套工程纪律按需触发——而不是只在你想起来时才提醒 agent——就用它。通过 agent 的 marketplace/插件机制装一次，技能就经由约 8 个映射到 SDLC 的斜杠命令暴露出来：Define(`interview-me`、`spec-driven-development`)、Build(`test-driven-development`、`frontend-ui-engineering`、`api-and-interface-design`)、Verify(`browser-testing-with-devtools`、`debugging-and-error-recovery`)、Review(`code-review-and-quality`、`security-and-hardening`、`performance-optimization`)、Ship(`git-workflow-and-versioning`、`ci-cd-and-automation`、`observability-and-instrumentation`)。它还附带预置 persona（code-reviewer、test-engineer、security-auditor、web-performance-auditor）和参考清单，让 agent 对照具体标准检查，而不是凭感觉。

## 何时不用

- **你已经在用一套方法论技能包。** 它与更宽泛的 SDLC 包（brainstorm → plan → TDD → verify）高度重叠。叠在已有的方法论层之上，会在同样的生命周期阶段产生互相冲突的“强制”指令和双重路由——只保留一个事实源。
- **你想要的是可运行的 runtime/CLI/库。** 这里没有任何东西可以 `import` 或独立运行——它是 markdown 技能 + 斜杠命令 + 各平台配置。脱离支持它的 agent harness，它什么都不做。
- **你的 agent 没有技能/插件加载器。** 它依赖各平台的原生技能加载机制（marketplace、`agy plugin install`、`gemini skills install`、rules 文件）激活。在自研或不受支持的 agent 上没有加载器去触发技能，markdown 也不会自动生效。
- **你需要硬性闸门强制执行。** 质量闸门住在 prompt/markdown 里，只能*建议* agent，并不会拦截合并。agent 仍可能跳步或为自己找理由——需要 CI 级强制时，请接入真实工具链（linter、测试闸门、CI）。[推断]
- **一次性脚本 / 非代码任务。** 对于一行脚本或改个配置，完整的 spec→build→review→ship 流程是额外负担。
- **单维护者、上游迭代快。** 仍处 1.0 之前（v0.6.x），发布频繁；技能名称、路由和斜杠命令映射可能在版本间变动。需要稳定就锁定某个 tag。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [web-quality-skills (addyosmani)](addyosmani-web-quality.zh.md) | ✅ | 只需要 web 性能、无障碍和质量审计时，选这个更聚焦的姊妹包。 | 更聚焦的姊妹包，专攻 web 性能/无障碍/质量审计。本包已把该主题（`/webperf`、web-performance-auditor）纳入完整 SDLC；只需 web 质量审计时用那个聚焦的。 |
| [scientific-agent-skills](scientific-agent-skills.zh.md) | ✅ | 任务是科研或科学计算工程，而非通用软件工程时，选 Scientific Agent Skills。 | 面向科研/科学计算工程工作流的技能包；领域不同。按你的工作是通用软件工程还是科学计算来选。 |
| [Waza](waza.zh.md) | ✅ | 想要更小的工程习惯集合、少一些完整 SDLC 结构时，选 Waza。 | 本 leaf 内另一个面向工程的技能集合；对比各自实际定义了哪些生命周期阶段、工作流多强制。 |
| [vercel-labs/agent-skills](vercel-agent-skills.zh.md) | ✅ | 真正需要厂商策划的 React/Vercel 规则时，选 Vercel Agent Skills。 | 厂商精选的技能集；对比覆盖广度（本包是完整 SDLC vs. 厂商范围）、harness 覆盖与维护节奏。 |
| [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) | ✅ | 重心是 brainstorm→plan→TDD→verify 的方法论纪律时，选 Superpowers。 | 方法论优先的包，围绕 brainstorm→plan→TDD→verify 纪律；本包则以具体工程实践域（质量/安全/性能/API/发布）和生命周期斜杠命令为中心，而非 TDD/subagent 主脊。目标重叠，重心不同。 |
| 各 agent 内置技能 / 斜杠命令 | 未收录 | 想用平台原生、平台负责维护的命令生态时，选内置技能。 | 平台自带的技能生态；本包是叠加其上的第三方 bundle，可能与原生技能重复或冲突。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 活跃——最后 push 于 2026-06，最新 release v0.6.2，1.0 前发版频繁，未归档。有版本号，但仍是 v0.x，路由与斜杠命令映射可能随升级变动。
- **治理与 bus factor：** 单维护者 `User` 仓库（Addy Osmani）背着约 67k stars——个人声誉很强，但确有 bus-factor 集中风险，路线图没有组织或 foundation 背书。[推断]
- **年龄与 Lindy：** 创建于 2026-02，截至 2026-06 仅几个月——年轻且被 star 炒热；Lindy 维度未经检验。主要信号是作者声望，而非这个仓库的过往记录。
- **风险标记：** 「质量闸门」仅建议性（prompt/markdown，不会拦截 merge 或 CI）＋1.0 前频繁变动 ⇒ 想要稳定路由就锁定一个 tag。[推断]

## 存疑（未验证）

- [未验证] 最新 release 报告为 v0.6.2（发布于 2026-06-11），仓库最后 push 于 2026-06-25;license 为 MIT、主语言为 Shell，据 GitHub 元数据（截至 2026-06-26）——依赖某个具体版本行为前请重新核实。
- [未验证] star 数（GitHub 2026-06-26 约 66.9k）不可靠且对日期敏感；仅作参考，不作质量信号。
- [未验证] 技能清单（“约 24 个技能”）及生命周期分组（Define/Plan/Build/Verify/Review/Ship/Meta）、约 8 个斜杠命令，均于 2026-06-26 从 README 读取；实际 `skills/` 目录与命令集随版本变动——请查看当前仓库而非依赖本清单。
- [未验证] 受支持 harness 列表（Claude Code、Antigravity、Gemini CLI、Cursor、Windsurf、GitHub Copilot、OpenCode、Kiro）及各平台安装命令均来自 README；各 harness 的激活保真度不一，此处未独立确认。
- [推断] 由于行为住在 agent 加载的 prompt/markdown 技能里，所谓“质量闸门”是建议性的——agent 可偏离；它们是 prompt 级指令，不是硬保证。
- [推断] 出处声明（实践取自《Software Engineering at Google》、OWASP、Core Web Vitals）是 README 对技能内容的措辞框定，此处未核实为对这些来源的真实引用。
