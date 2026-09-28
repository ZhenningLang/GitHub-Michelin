---
name: claude-code-harness
slug: claude-code-harness
repo: https://github.com/Chachamaru127/claude-code-harness
category: engineering-workflows
tags: [claude-code, harness-config, sdlc-workflow, slash-commands, plan-work-review, plugin]
language: Shell
license: MIT
maturity: v5.15.0, active, ~3.1k stars (as of 2026-09)
last_verified: 2026-09-27
type: skill-pack
upstream:
  pushed_at: 2026-09-21T01:27:29Z
  default_branch: main
  default_branch_sha: 2b2b74805321089bd9b660a1064fa97556299703
  archived: false
health:
  schema: 1
  computed_at: 2026-09-27T17:50:03Z
  overall: B
  overall_score: 2.6
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 22
        active_weeks_13: 11
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: null
        canonical_package: null
        release_downloads: 475
        release_assets: 180
        release_tier: D
        signal_basis: releases
    longevity:
      grade: B
      raw:
        repo_age_days: 290
        last_commit_age_days: 22
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.923
        top3_share: 0.998
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
---

# claude-code-harness

你要一个功能，Claude Code 交回来的代码你没参与过规划、也没人评审。这套插件把交付逼成一条有闸门的循环：它起草给你批准的 `spec.md`/`Plans.md` 契约、在 TDD 门控下干活、重大评审问题直接拦住完成——并且从 v5 起，危险操作执行前先过一遍 Go 护栏引擎。

![claude-code-harness — 健康度雷达](../../../../assets/health/claude-code-harness.zh.svg)

## 何时使用

你是一个长期泡在 Claude Code（或 v5 的四个「正式支持」宿主之一：Codex CLI / Cursor / Grok）里的开发者，反复看到 agent 做同一件事：跳过写 spec、直接上手写代码、靠猜来「修」bug、让 review 和测试事后补（甚至根本不做），然后就宣布功能完成。你想让 agent 表现得像一支有纪律的交付团队——先写一份你批准的 spec、拆成计划、然后才在 TDD 下实现、通过独立 review、发布前打包好证据。你通过 Claude Code 插件市场安装（`/plugin marketplace add Chachamaru127/claude-code-harness`、`/plugin install claude-code-harness@claude-code-harness-marketplace`），跑一次 `/harness-setup`，就从 23 个 skill 里得到五个核心动词——`/harness-plan`（把意图变成 `spec.md` + `Plans.md`：范围、验收标准、依赖、未知项、停止条件）、`/harness-work`（在批准范围内执行，按任务量单干或组队，任务要求时强制 TDD）、`/harness-review`（与实现分离的评审，重大问题拦住完成）、`/harness-sync`（对照计划与实际实现的偏差）、`/harness-release`（只把已验证的证据打包成 CHANGELOG、tag 与 release）。

当你想让整条从规划到发布的脊柱由你批准或修正的显式契约产物把住关口——并且要 v5 新增的运行时防护：Go 引擎在执行前审查操作，一层「不可全局关闭」的 runtime floor（覆盖计费、网络外发、密钥读取、生产部署、任务工作区之外的删除），加一层可部分按项目配置的 R01–R16 护栏（直推 `main`、保护路径、强推、改写历史）——就选它，而不是自己攒一套 skill 栈。仓库还带 `bin/harness doctor --migration-report`，在不删任何东西的前提下盘点失效插件缓存、重复 skill 与失效软链；可选扩展包括 `/harness-loop`（有界循环执行）、Breezing 计划者/评审者/工人组队、跨 worktree 的会话名册。非 Claude 宿主的支持被刻意分成层级——Codex CLI/Cursor/Grok 走 setup 脚本算「正式支持」，OpenCode 是 internal-compatible 且明说不保证运行时对等，Copilot CLI 等只是候选。[推断]

## 怎么用起来

这套 harness 是一个由 23 个 skill 组成的 Claude Code 插件，围绕五个动词；它的核心动作是把临时起意的 prompt 变成*有闸门的产物*。你给出意图和完成标准（`/harness-plan Fix duplicate orders. The completion criterion is that the same order is stored once.`），plan 阶段先检查现有代码，写出 `spec.md` + `Plans.md`，在你批准或修正这份契约之前什么都不执行。随后 `/harness-work` 派发工人（单干，或任务多时用 Breezing 的计划者/评审者/工人组队），所有动作留在批准范围内——agent 没见到的数据记成 `unknown` 而不是编造，每个任务跑必需检查与 TDD。危险操作真正执行前，由 Go 引擎分两层裁决：runtime floor（五类，允许/拒绝，没有全局关闭开关）与 R01–R16 护栏（拒绝/确认/警告，部分可按项目配置），每条裁决都写进决策日志；注意覆盖面依宿主而定。仍然归你管的：定义「完成」的含义、批准每份契约、在迭代上限内修正评审发现、以及最后按下 `/harness-release`——README 自己就强调，别的工具有 setup 脚本只意味着「有入口」，不意味着同一套保证。

![claude-code-harness — 主干用户故事](../../../../assets/flow/claude-code-harness.zh.svg)

<!-- flow-steps:begin (generated from flows/claude-code-harness.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：在 Claude Code 里添加插件市场 — `/plugin marketplace add Chachamaru127/claude-code-harness`
2. **你**：安装插件并跑一次 setup — `/harness-setup`
3. **claude-code-harness**：五个核心动词与 Go 护栏引擎接入你的会话 — 组件：`harness 插件`
4. **你**：交出一个意图和完成标准 — `/harness-plan Improve the README onboarding flow`
5. **claude-code-harness**：起草 spec.md + Plans.md：范围、验收标准、未知项、停止条件 — 组件：`/harness-plan`
6. **你**：批准或修正契约，然后整盘执行 — `/harness-work all`
7. **claude-code-harness**：工人按计划干活；每个操作执行前由 Go 引擎裁决放行或拒绝 — 组件：`runtime floor + 护栏`
8. **你**：独立评审结果，然后发布 — `/harness-review · /harness-release`
9. **claude-code-harness**：重大问题拦住完成；发布只打包已验证的证据 — 组件：`/harness-release 预检`

**价值**：每个功能都落成批准的契约、TDD 门控、独立评审与执行前护栏，而不是「我测过了，放心」

</details>
<!-- flow-steps:end -->

## 何时不用

- **你已经在跑一套精选的工作流/方法论栈。** 这套 harness 是强主张的（spec 先于代码、work 受 TDD 门控、review 拦住完成）。把它叠在已有的 plan→ship 方法论上——gstack、Superpowers，或你自己的命令——会引发路由冲突和双重治理；只能选一个事实源。
- **你不想要一个运行时护栏引擎。** v5 起操作执行前要过 Go 引擎，runtime floor *没有全局关闭开关*（只有有限的白名单）。这是强制而不是仪式——但它的覆盖面依宿主而异，且拦截行为本身是项目自己的声称。[未验证]
- **你的主力在非「支持」层的宿主上。** 支持层：Claude Code v2.1+、Codex CLI、Cursor、Grok；OpenCode 是 internal-compatible，明说不保证运行时对等；Codex app、Hermes、GitHub Copilot CLI 是候选；Antigravity 无安装路线。「有入口」≠「同一套保证」——README 自己就这么写。
- **一次性脚本、spike、非代码任务。** 当你只想快速改一处或调个配置时，plan→work→review→release 这套仪式是负担；它假定一个有值得门控产物的真实软件变更循环。
- **快速演进的单维护者上游。** 处于 v5.x，发版频繁、行为烤进 prompt 与 skill 路由——v4→v5 大版本间就加了安全层与 `/harness-sync`；一次版本跳变可能改变这些动词所强制的内容。请 pin 版本并在升级后重新核对。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [gstack](gstack.zh.md) | ✅ | 想要 Garry Tan 的 persona 命令体系，而不是显式 spec/plan 契约与护栏引擎时，选 gstack。 | Garry Tan 的个人 Claude Code 配置，驱动一个类似的 plan → build → review → ship 循环，但靠 ~23 个角色扮演 persona 命令（CEO/设计师/QA/安全官）。claude-code-harness 是五个命名动词，带显式 `spec.md`/`Plans.md` 契约、Go 护栏引擎和 `doctor` 工具；gstack 更依赖 persona 而非契约产物。 |
| [shaping-skills](shaping-skills.zh.md) | ✅ | 只需要 Shape Up 式“定义要造什么”的前端塑形环节时，选 shaping-skills。 | Ryan Singer 的 Shape Up「shaping」包只覆盖*定义要造什么*这个前端环节。本 harness 覆盖完整的 定义→实现→review→发布 脊柱，因此二者互补而非互替。 |
| [Superpowers](../../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) | ✅ | 需要更精简、跨更多 harness 的方法论、而非逐操作护栏时，选 Superpowers。 | 跨 harness 的 skills 库，具备相同的 brainstorm/plan→TDD→verify 脊柱，打包给多种 agent。claude-code-harness 在“闸门”上更重——spec/plan 契约文件、执行前审查操作的 Go runtime floor 加 R01–R16 护栏、发布预检——代价是更重、更 Claude 中心的安装；Superpowers 是更轻的方法论、更广的覆盖、没有强制引擎。 |
| harness-mem（可选配套） | 未收录 | 需要跨会话记忆插件、而不是工作流替代品时，才看 harness-mem。 | 同一维护者的可选记忆插件，被本项目引用但明确声明不依赖；属于另一关切（agent 记忆），不是工作流替代品。 |
| Claude Code 原生 skills / 内置 slash 命令 | 非仓库 | 优先使用平台维护的原生命令生态、不要第三方治理时，选 Claude Code 内置能力。 | 平台自带的 skill 生态，并非独立仓库；本项目是叠在其上的第三方 bundle，可能与原生命令重复或冲突。 |

## 健康度与可持续性

- **维护（2026-09）：** 活跃——v5.15.0 发布于 2026-09-06（默认分支最后提交同日，约 15 个 open issue），建立在本页 2026-06 记录到的 v4.16.3 稳定发版线之上。与本叶子里多数个人 pack 不同，它确实打 tag 发版，因此你*可以* pin 版本——而 v4→v5 的跳变也说明设计仍在移动。
- **治理与 bus factor：** 单一维护者的 `User` 仓库（Chachamaru127），无基金会或厂商。约 3.1k star 体量不大；路线图、宿主支持层与延续性完全系于一人。
- **年龄与 Lindy 判断：** 创建于 2025-12，约九个半月——仍未经验证存续。高速发版透着冲劲，也意味着不稳定：安全层与动词集合在大版本之间发生过变化，prompt/路由行为可能随版本跳变。尚不是 Lindy 意义上的安全押注。
- **风险标记：** v5 的强制叙事（无全局关闭的 runtime floor、护栏裁决、评审拦住完成、发布预检）是项目 README 的自称，宿主覆盖明确不均（有 hardening-parity 文档）；非 Claude 宿主的分层声称在此未经证实。模型路由写死了具体模型 ID，可能很快过时。升级后请 pin 并重核。

## 存疑（未验证）

- [未验证] 强制行为（runtime floor 允许/拒绝、R01–R16 裁决、评审拦住完成、发布预检）读自 2026-09-27 的 v5 README；本页未在真实 Claude Code 安装里执行验证，且 README 自己的 hardening-parity 文档说明宿主覆盖不均。
- [未验证] 最新发布 v5.15.0（2026-09-06），默认分支最后提交 2026-09-06（仓库 `pushed_at` 2026-09-21 来自其他分支），创建于 2025-12-12；MIT、主语言 Shell 均据 2026-09-27 的 GitHub 元数据——依赖某具体版本行为前请重新核验。
- [未验证] star 数（2026-09-27 GitHub 显示约 3.1k）不可靠且对日期敏感；仅作参考，不作质量信号。
- [未验证] 角色→模型路由表（如 deep 决策用 Fable 5.1/`high`、专职评审用 Sonnet 5/`xhigh`、Codex 路线用 GPT-6 astra）引自 README；这些 ID 在具体安装中能否解析、覆盖优先级如何，未测试。
- [未验证] 各宿主安装层级（supported：Claude Code / Codex CLI / Cursor / Grok；internal-compatible：OpenCode；候选：Codex app / Hermes / Copilot CLI）与 H1–H8 验收声称均出自项目自身；非 Claude 宿主的实际激活保真度此处未验证。
- [推断] 动词集合与 skill 路由逐版本变化（v4→v5 就新增了 `/harness-sync` 与安全层）；请核对当前 skill 清单而非依赖本页。
- [推断] 尽管有护栏引擎，prompt 级步骤（spec 先行、TDD 闸门）对 agent 的*推理*仍是软约束——硬拒绝覆盖的是要执行的操作，不是敷衍的执行，评审产出仍需人来读。
