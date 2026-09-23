---
name: antfu/skills
slug: antfu-skills
repo: https://github.com/antfu/skills
category: engineering-workflows
tags: [skills, vue, nuxt, vite, unocss, vitest, claude-code, skills-cli]
language: TypeScript
license: MIT
maturity: no tagged releases, active (pushed 2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-23T00:14:36Z
  default_branch: main
  default_branch_sha: a74f281a27dadc02397bc1a174b0f2c97531b6ae
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:48:02Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 92
        active_weeks_13: 1
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
        repo_age_days: 237
        last_commit_age_days: 92
        cohort: skill-pack
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 11
        top1_share: 0.79
        top3_share: 0.871
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

# antfu/skills

Anthony Fu 个人精选的 agent skill 集合，面向 Vue/Vite/Nuxt 生态——包含他本人的 ESLint/pnpm/Vitest/UnoCSS 偏好，以及从官方文档自动生成和外部 vendored 的 Vue、Nuxt、Pinia、Vite、VitePress、Vitest、UnoCSS、Slidev、VueUse 等 skill，通过 `skills` CLI 安装。

![antfu-skills — 健康度雷达](../../../../assets/health/antfu-skills.zh.svg)

## 何时使用

你是一名常驻 Anthony Fu 技术栈的前端工程师——Vue 3、Nuxt、Vite、Vitest、UnoCSS、pnpm，外加他的 `@antfu/eslint-config`——而你的 coding agent 写出来的代码虽然“能跑”，却不符合该生态维护者们的真实写法：Vitest 测试惯用法不对、把 UnoCSS 当 Tailwind 用、ESLint/格式化和你的配置打架、Vue 写法忽视组合式 API 的最佳实践。你不想为这套栈里每个工具手写一份规则集，而是想直接继承“维护了其中很大一部分的那个人”的意见，并在任务匹配时自动应用。

你运行 `pnpx skills add antfu/skills --skill='*'`（加 `-g` 走全局安装），agent 便获得一组按需加载的 skill 菜单：两个手工维护的（`antfu` 管 app/library 项目偏好，`antfu-design` 管以 UnoCSS 为中心的设计），八个由官方文档生成的（Vue、Nuxt、Pinia、Vite、VitePress、Vitest、UnoCSS、pnpm），以及一组 vendored 的（Slidev、tsdown、Turborepo、VueUse functions、Vue best-practices、Vue Router、Vue 测试指南、web-design-guidelines）。由于它以 [skills.sh](https://skills.sh/) / agentskills.io 的 `SKILL.md` 格式分发，`skills` CLI 会把它装进你 harness 自己的 skills 目录（`.claude/skills/`、`.agents/skills/` 等），于是同一份 pack 可在 Claude Code、Cursor、OpenCode、Codex 等受支持 agent 间通用。当你的栈*就是* antfu 这套时，你会优先选它——与其重新发明，不如直接继承他的约定。这个仓库本身也是模板：改 `meta.ts` 再重新生成，就能搭出你自己的集合。

## 何时不用

- **你不在 Vue/antfu 这套栈上。** 价值高度集中在 Vue/Nuxt/Vite/UnoCSS/Vitest 以及 antfu 个人的 ESLint/pnpm 约定。在 React/Svelte/Astro 或非 antfu 工具链上，大多数 skill 用不上，其设计/lint 意见还可能与你的冲突。
- **你已经有一套该栈的精选 skill 栈。** 再叠一套有主见的 Vue/web-design pack，容易出现规则集冲突和评审时的双重路由——每个关注点只留一个事实源。
- **你想要厂商中立或社区共识的规则。** 这些明确是*某一个人*的偏好（ESLint 风格、设计取舍）；与你一致则有价值，不一致则是摩擦。
- **你的 harness 没有 skills 加载器。** 它靠 `skills` CLI 把文件写进各 agent 的 skills 目录来激活；在自研或不受支持的 agent 上没有东西去触发这些 `SKILL.md`，markdown 不会自动生效。
- **你需要的是强制，而不是建议。** 规则活在 agent *应当*遵循的 prompt/markdown 里；没有任何东西会拦合并或让 CI 失败。它是建议性指导，不是闸门。[推断]
- **你需要版本稳定性。** 截至本次核查没有打 tag 的 release——你跟的是移动的 `main`，而且生成/vendored 的 skill 会从上游文档重新生成，规则集与 skill 边界可能在每次拉取间变化。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Vercel Agent Skills](../../engineering/vercel-agent-skills.zh.md) | ✅ | React/Next.js/Vercel 平台规则比 Vue/Vite 约定更重要时，选 Vercel Agent Skills。 | Vercel 官方为 *React/Next.js/Vercel* 生态出的 pack，走同一套 `skills` CLI/格式。与 antfu 的恰成镜像：按你属于哪个框架世界（Vue 还是 React）来选；两者都是有主见的厂商/维护者规则集，并非中立。 |
| [Agent Skills (addyosmani)](../../engineering/addyosmani-agent-skills.zh.md) | ✅ | 需要框架无关的全 SDLC 工程规则时，选 Agent Skills。 | Addy Osmani 个人的全 SDLC 工程 pack（spec→build→review→ship、web 性能、安全）。生命周期覆盖更广且框架无关；antfu 的更窄、更绑栈（Vue 工具链约定），而非一条方法论脊柱。 |
| [web-quality-skills (addyosmani)](../../engineering/addyosmani-web-quality.zh.md) | ✅ | 只要厂商中立的 web 性能、可访问性和质量审计时，选 web-quality-skills。 | 专注 web 性能/可访问性/质量审计，厂商中立。与 antfu 的 `web-design-guidelines` vendored skill 有重叠，但更专一且能脱离 Vue 栈使用。 |
| [Dimillian/Skills](dimillian-skills.zh.md)、[gstack](gstack.zh.md)、[ljg-skills](../knowledge-content/ljg-skills.zh.md)、[khazix-skills](../knowledge-content/khazix-skills.zh.md)、[taches-cc-resources](taches-cc-resources.zh.md) | ✅ | 更认同某位维护者的个人栈和工作习惯时，选对应个人集合。 | 同一类型——个人维护者精选的 skill/harness 捆绑——但各自反映不同人的栈和约定；按你真正认同谁的工具链与意见来比。 |
| 各 agent 自带的 skills / 斜杠命令 | 未收录 | 想优先使用平台维护的原生能力，而非第三方捆绑时，选内置 skill。 | 平台自身的 skill 生态；antfu/skills 是叠在其上的第三方捆绑，可能与原生 skill 重复或冲突。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** 活跃——最后 push 于 2026-06，仅约 9 个 open issue。没有打 tag 的 release，因此你跟的是移动的 `main`，没有 semver 检查点。是活跃而非半荒废。
- **治理与 bus factor：** 这是一位高知名度维护者（antfu）的个人仓库，`User` 所有，无基金会或厂商背书。一人维护的合集却有约 5k star，是典型的 bus-factor 风险信号——方向与延续性完全系于一个人是否持续投入。
- **年龄与 Lindy 判断：** 创建于 2026-01，截至 2026-06 约半岁——年轻且当前处于热度期，尚未经 Lindy 验证。antfu 在 Vue/Vite 生态的长期履历令人安心，但*这个 pack 本身*没有存续历史；别把它的年龄当作安全信号。
- **风险标记：** 生成/vendored 的 skill 会从上游文档重新生成，规则集可能在每次拉取间变化；无法 pin release。仅为建议性（无强制闸门）。尽管仓库 license 为 MIT，vendored skill 仍保留各自上游 license。

## 存疑（未验证）

- [未验证] License 据 2026-06-26 的 GitHub 元数据为 MIT（README 另注明 vendored skill 保留各自上游 license）；主语言报告为 TypeScript——那反映的是生成/自动化工具与 `meta.ts`，并非可运行的应用，因为实质内容是 markdown 的 `SKILL.md` 文件。
- [未验证] 截至 2026-06-26 没有打 tag 的 release / `latestRelease` 为 null；"maturity" 由最后 push（2026-06-23）和活跃度推断，而非 semver。仓库未归档。
- [未验证] Star 数（2026-06-26 GitHub 约 5,409）不可靠且对日期敏感；仅作参考，不作质量信号。
- [未验证] skill 清单（手工维护的 `antfu`/`antfu-design`；生成的 Vue/Nuxt/Pinia/Vite/VitePress/Vitest/UnoCSS/pnpm；vendored 的 Slidev/tsdown/Turborepo/VueUse/Vue-best-practices/Vue-Router/Vue-testing/web-design-guidelines）以及 `sources/`、`vendor/`、`instructions/`、`scripts/`、`meta.ts` 结构均读自 2026-06-26 的 README/仓库列表；生成与 vendored 的部分会从上游重新生成，请以实时的 `skills/` 目录为准，勿信此快照。
- [未验证] 通过第三方 `skills` CLI 安装（`pnpx skills add antfu/skills --skill='*'`，`-g` 走全局）及其受支持 harness/目标目录行为（Claude Code `.claude/skills/`，Cursor/OpenCode/Codex `.agents/skills/` 等）是 vercel-labs `skills` 工具的属性，而非本仓库的属性；各 harness 的激活保真度此处未独立验证。
- [推断] 由于行为活在 agent 加载的 prompt/markdown skill 里，强制力是建议性的——agent 仍可偏离；这些约定是 prompt 级指令，不是硬保证。
- [推断] skill 编码的是某一位维护者的个人偏好；“最佳实践”的措辞是他的意见（对生成类 skill 而言，是生成当时官方文档的快照），并非独立验证过的标准。
