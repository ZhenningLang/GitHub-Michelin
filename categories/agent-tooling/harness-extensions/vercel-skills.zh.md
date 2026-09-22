---
name: Vercel Skills
slug: vercel-skills
repo: https://github.com/vercel-labs/skills
category: harness-extensions
tags: [skills, package-manager, cli, claude-code, opencode, cursor, codex, npx, installer, agent-tooling]
language: TypeScript
license: MIT
maturity: v1.5.13, active (2026-06)
last_verified: 2026-06-26
type: tool
upstream:
  pushed_at: 2026-06-25T17:36:54Z
  default_branch: main
  default_branch_sha: 9a7d8acfbf29f9cced7fb5a504da1d65b484aed3
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:25:20Z
  overall: D
  overall_score: 2.5
  scored_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NONE"
  needs_human_review: true
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 3
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 35.2
        qualifying_issues: 5
        band: relaxed_solo
        window_offset_days: 0
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: skills
        dependent_repos_count: 3
        downloads_last_month: 2903169
        graph_tier: D
        volume_tier: B
        cross_check_divergence: 11.98
    longevity:
      grade: D
      raw:
        repo_age_days: 169
        last_commit_age_days: 3
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 97
        top1_share: 0.466
        top3_share: 0.597
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
---

# Vercel Skills

一个包管理器风格的 CLI（`npx skills`），把 agent「skills」——即 `SKILL.md` 指令包——从 GitHub/GitLab/本地源安装、查找、更新进 70+ 个编码 agent。它是*安装器*，不是 skill 内容本身。

![vercel-skills — 健康度雷达](../../../assets/health/vercel-skills.zh.svg)

## 何时使用

你是一名开发者，手头攒了一批 agent skills——有自己写的，有从 GitHub 上扒下来的 `SKILL.md` 包——你已经受够了那套手工流程：clone 仓库、把对的目录拷进 `.claude/skills`（或者 `.opencode`、`.cursor`，取决于你今天用哪个 agent），每台机器每个项目都重来一遍，一个月后还完全不知道哪些早就过期了。你想要的是 skills 版的 npm 体验：一条命令从 `owner/repo` 装一个包，一条命令列出已装的，一条命令把它们全部更新。

于是你用 `npx skills add owner/repo` 把一个 skill 放进对应的 agent 目录，用 `npx skills find <关键词>` 通过 skills.sh 注册表发现可用的包，再用 `npx skills list` / `npx skills update` 保持更新——因为它内置了 OpenCode、Claude Code、Codex、Cursor 以及几十个其它 agent 的目录布局约定，*同一条*命令无论你当下用哪个 agent，都能把 skill 落到正确位置。它是一个轻量、依赖极少的 TypeScript 二进制，通过 `npx` 调用，无需托管、无需常驻进程。

## 何时不用

- **你要的是 skills 本身，而不是管理它们的方式。** 这是安装器/管理器。真正可复用的指令是*内容*包——下方的 [skill-pack] 同类项（Planning with Files、Context Mode 等）正是它要安装的东西。装上这个工具，在你把它指向内容之前，不会给你的 agent 带来任何新能力。
- **你只用一个 agent，且很少换 skills。** 如果你完全活在 Claude Code 里、一年手工拷两个 skill，那它的价值（跨 agent 路径解析、批量更新）相比 `cp` + git submodule 就很边际；为了用不上的便利去引一个依赖，不划算。
- **你需要管理 MCP server、plugin 或工具二进制。** 它的范围只有 `SKILL.md` 指令包——不安装也不运行 MCP server、不管理 agent 二进制、不编排运行时状态。任务/状态类工具见对比表里的 [beads](../work-state/beads.zh.md) 一行。
- **你需要一个经过策展、做过安全审查的市场。** 源直接从任意 GitHub/GitLab/git URL 解析，装一个包意味着信任会进入你 agent 上下文的第三方 prompt 内容。没有审核闸门，供应链 / prompt 注入的警惕得你自己扛。
- **团队内可复现、可锁定版本的安装。** 文档里没有发现 lockfile / `skills.json` 清单，所以版本锁定和跨机器确定性重装目前不是一等公民（依赖前请对照当前版本核实）。
- **成熟度上限。** 2.0 之前、单一厂商（`vercel-labs`）、迭代很快（频繁小版本）；命令面和它对接的注册表可能随版本变动。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Planning with Files](../work-state/planning-with-files.zh.md) | ✅ | 需要 skill-pack 内容而非安装器时，选 Planning with Files。 | 一个 skill-pack（内容）——正是 Skills 要安装的*那类东西*，不是竞品。用 Skills 把这样的包送进你的 agent。 |
| [Context Mode](../work-state/context-mode.zh.md) | ✅ | 需要工作流内容而非 skill 分发机制时，选 Context Mode。 | 同样是 skill-pack / 工作流内容，不是安装器。正交关系：Skills 是投递机制，这是被投递的载荷。 |
| [beads](../work-state/beads.zh.md) | ✅ | 需要 agent 的持久任务/记忆状态，而不是 skill 分发时，选 beads。 | 不同层：给 agent 的持久任务/记忆*状态*，而非 skill 分发。你可能两个都装——它们不重叠。 |
| Claude Code 插件市场（`.claude-plugin/marketplace.json`） | 未收录 | 需要 Claude Code 原生插件分发时，选 Claude Code 插件市场。 | Claude Code 原生的插件/市场机制；更丰富（命令、hooks、MCP）但仅限 Claude Code。Skills 转而面向跨 70+ agent 的 `SKILL.md` 包。 |
| git submodule / 手工 `cp` | 未收录 | 零新依赖和完全透明最重要时，选 git submodule 或手工复制。 | 零新依赖、完全透明，但没有跨 agent 路径解析、没有发现注册表、没有批量 `update`——正是 Skills 取代的手工流程。 |
| 用 npm / pnpm 打包一个 skill 目录 | 未收录 | 想复用 JS 包生态的版本管理和 lockfile 时，选 npm/pnpm 打包。 | 复用 JS 包生态（有真正的版本管理 + lockfile），但 skills 不是 npm 形态，你得按 agent 手工摆放文件；Skills 是为 `SKILL.md` 布局专门做的。 |

## 技术栈

- **语言：** TypeScript（约 95%），少量 JS；构建为 `.mjs` CLI(`bin/cli.mjs`)。
- **运行时：** Node.js，通过 `npx skills` 调用（也以 `add-skill` 暴露）。
- **分发：** 以 `skills` 发布到 npm；用 `npx` 运行（无需全局安装）。
- **发现：** `npx skills find` 背后是 `skills.sh` 注册表。
- **可解析的源：** GitHub 简写（`owner/repo`）、完整 GitHub/GitLab/通用 git URL，以及本地路径。
- **消费的 skill 格式：** 含 `SKILL.md`（YAML frontmatter,`name`、`description`）的目录；也识别 Claude 插件清单（`.claude-plugin/marketplace.json` / `plugin.json`）。

## 依赖

- **运行时：** Node.js `>=18`（据 `engines`）；无独立服务、守护进程或数据存储。
- **生产依赖：** 仅声明一个运行时依赖——`yaml`（解析 frontmatter）。其余实现为自有代码；`ThirdPartyNoticeText.txt` 覆盖捆绑的第三方声明。
- **网络：** 需访问 GitHub/GitLab/git 远端拉取包，以及 `skills.sh` 注册表做发现；离线使用仅限已拉取 / 本地路径源。
- **落地目标：** 写入各 agent 的 skill 目录（`.claude/skills`、OpenCode/Cursor/Codex 等价目录），无需管理任何全局运行时。

## 运维难度

**低。** 它是一个无状态的 `npx` CLI：无需部署、无 server、无数据库、无后台进程。「运维」它就是按需跑命令；唯一的活动部件是 Node `>=18` 和到源远端 / 注册表的网络访问。真正要操心的是治理而非基础设施——因为它把第三方 prompt 内容直接装进 agent 上下文，要把*装哪些*包（以及从哪装）当成需要审查的对象，并自己做版本锁定/追踪，因为没找到 lockfile 机制。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 35.2 小时，基于 5 个 qualifying issues/PRs。
- **维护（2026-06）：** [推断] 在积极维护——最近 push 在 2026-06，最新发布 v1.5.13（2026-06-23），未归档，小版本发布节奏很快。未关闭 issue 约 805（截至 2026-06）对一个小型 CLI 偏高，更应读作活跃使用带来的流转，而非疏于维护，但要预期有积压。
- **治理与背书：** [推断] `vercel-labs` 是 Vercel 的实验/labs 组织，并非 Vercel 的核心产品线。「labs」仓库带有真实的弃坑/废弃风险——Vercel 发很多实验项目，并非都会毕业或获得长期支持。单一厂商主导路线图，无基金会中立性。
- **年龄与 Lindy：** [推断] 创建于 2026-01，截至 2026-06 约半岁——**年轻、按 Lindy 尚未证明**。安装/更新的人体工学现在确实有用，但一个半岁、2.0 之前的 labs 工具没有寿命记录；它的命令面以及所依赖的 `skills.sh` 注册表仍可能变动。
- **风险标记：** [未验证] 没有用于固定可复现安装的 lockfile/清单（见存疑）；按 `package.json` 为 MIT 但未检测到 SPDX `LICENSE` 文件；它会把任意第三方 prompt 内容装进 agent 上下文（供应链 / prompt 注入面由操作者承担）。它是*安装器*，因此自身的可持续性与你实际运行的 skill 内容在一定程度上是解耦的。

## 存疑（未验证）

- [未验证] Star 数约 23.6k(gh `stargazerCount`,2026-06-26);GitHub star 不可靠且对日期敏感——仅供参考。
- [未验证] 据 README 与 `package.json` 的 `license` 字段，许可证为 **MIT**，但 GitHub 许可证 API 返回 404，仓库根目录也未见 SPDX `LICENSE` 文件（只有 `ThirdPartyNoticeText.txt`）;SPDX id 由声明字段推得，而非检测到的许可证文件。
- [未验证]「70+ 支持的 agent」/ 具体清单（OpenCode、Claude Code、Codex、Cursor……）是 README 自己的说法；确切列表及每个 agent 的路径映射会随版本变动——依赖某个 agent 前请核实。
- [未验证] 没有 lockfile / `skills.json` 清单这一点，是从文档未提及推得的；锁定机制可能已存在或在后续版本落地。
- [推断] 仅声明一个生产依赖（`yaml`）取自 `package.json`;`src/` 与 `scripts/` 下的传递/捆绑代码未审计，所以「依赖少」只描述声明层面。
- [推断] v1.5.13 最新发布于 2026-06-23，最后 push 于 2026-06-25，未归档（gh 元数据，2026-06-26）；迭代节奏与「活跃」状态是时间点观察，非维护保证。
