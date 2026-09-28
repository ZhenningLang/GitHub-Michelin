---
name: Designer Skills
slug: designer-skills
repo: https://github.com/Owl-Listener/designer-skills
category: ui-taste
tags: [skills, ui-ux, design-systems, claude-code, gemini-cli, plugin]
language: Markdown
license: MIT
maturity: no tagged release, active (last pushed 2026-09; ~2.8k stars as of 2026-09)
last_verified: 2026-09-28
type: skill-pack
upstream:
  pushed_at: 2026-09-05T15:32:50Z
  default_branch: main
  default_branch_sha: 9a6930cf84a822eb458624bd11c61aac5bbdf224
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T03:20:42Z
  overall: B
  overall_score: 2.5
  scored_axes: 4
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 22
        active_weeks_13: 3
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
        repo_age_days: 205
        last_commit_age_days: 22
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.92
        top3_share: 0.96
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

# Designer Skills

你的 coding agent 产出的设计看着像样，一追问「为什么这么设计」就露馅：所谓「设计系统」只是一串颜色，批评只会说「看起来挺干净」。Designer Skills 是一个设计实践 skill pack——9 个 plugin 下共 111 个 skill、34 个 command，从用户研究一路覆盖到视觉批评——通过 plugin marketplace 装进 Claude Code 或 Gemini CLI，让 agent 运用训练有素的设计判断，而不是靠猜。

![designer-skills — 健康度雷达](../../../../assets/health/designer-skills.zh.svg)

## 何时使用

你是产品设计师（或在做设计工作的开发者），跑在 Claude Code 上，但 agent 产出的设计在语法上像样、在功底上很浅：UI 没有真正的布局栅格纪律，所谓「设计系统」只是一串颜色，可用性测试计划背后没有方法，批评只会说「看起来挺干净」而不点出层级和可供性的问题。你希望 agent 在*整条*生命周期上像受过训练的设计师那样推理——框定研究、论证信息架构、为字体和配色辩护、跑启发式评估、写交付规范——而不只是生成一个好看的页面。Designer Skills 把这套能力作为一个 marketplace bundle 提供：用 `/plugin marketplace add Owl-Listener/designer-skills` 安装，再启用你需要的 plugin（比如 `ui-design`、`design-systems`、`visual-critique`），agent 在做设计工作时按需加载相应的 skill。

当你要的是*广度*——一次安装就覆盖 研究 → 系统 → UI → 交互 → ops → 批评——而不想手工拼装多个单一用途的设计 skill 时，就用它。按这个 repo 的说法，*skill 是名词*（像「色彩系统」「格式塔原则」这样的领域知识单元），*command 是动词*（把多个 skill 串成完整工作的工作流），所以你既拿到可复用知识、也拿到现成流程。它还带了一套 `.gemini/extensions/` 布局，因此同一批包通过 clone-and-copy 方式也能在 Gemini CLI 里用。到 2026-09，这个家族已扩展为五个合集（共约 273 个 skill / 33 个 plugin，另外四个住在姊妹 repo 里），本 repo 还加了一个路由命令（`/designer-toolkit:start-here`）——不知道该从哪开始时，它会告诉你要跑哪条命令。

## 怎么用起来

每个 plugin 就是一个装着 markdown skill（agent 按需加载的领域知识）和斜杠 command（把多个 skill 串成一份交付物的固定工作流）的目录。你只需要做三件事：添加 marketplace、在 `/plugin` 的 Discover 页勾选想要的 plugin、以及——不知道从哪下手时——跑 `/designer-toolkit:start-here`，它会指出你所在的阶段，给你一条命令和紧随其后的两条。之后就是 agent 的活了：比如你跑 `/design-research:discover`，它会一口气走完 用户画像 → 共情地图 → 旅程图，边走边调用底层的 skill 指引，输出交付物。留在你这边的：挑要启用哪些 plugin、提供产品上下文、判断产出——这里没有任何硬闸门，它只是把设计师的判断写成文字供 agent 阅读。

![Designer Skills — 主干用户故事](../../../../assets/flow/designer-skills.zh.svg)

<!-- flow-steps:begin (generated from flows/designer-skills.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：先添加 marketplace（此时还没装任何东西） — `/plugin marketplace add Owl-Listener/designer-skills`
2. **你**：在 Discover 页勾选想要的 plugin，回车安装 — `/plugin` — 组件：`plugin marketplace`
3. **Designer Skills**：把所选 plugin 的 skill 作为按需加载的设计知识 — 组件：`plugin（如 ui-design）`
4. **你**：不知道从哪开始？说出你在做什么 — `/designer-toolkit:start-here`
5. **Designer Skills**：指出你所在的阶段，给你一条命令和随后的两条
6. **你**：带上你的上下文跑这条工作流命令 — `/design-research:discover`
7. **Designer Skills**：把底层的 skill 串成一份交付物（画像、共情地图、旅程图） — 组件：`command 串联 skill`

**价值**：agent 在整条生命周期上运用训练有素的设计判断，而不是产出看着像样、实则空洞的东西

</details>
<!-- flow-steps:end -->

## 何时不用

- **你已有一个信任的聚焦设计 skill。** 如果你已经接好了一个专门的批评或设计系统 skill，再在上面叠这个大而全的包，会引入相互重叠的指引和双重路由——比如对「好的层级」给出两套互相打架的定义。每个关注点只保留一个事实源。
- **你只需要其中一片。** 只想要视觉批评、或只想要一份设计系统 contract，却拉来 111 个 skill / 9 个 plugin 的大包，比任务本身重得多——单一用途的同类 skill 推理和维护起来更轻。只启用你用到的 plugin，或选更窄的包。
- **你不在受支持的 harness 上。** 激活依赖 Claude Code 的 plugin/skill 加载器或 Gemini CLI 的 extension 机制。在不受支持或自研的 agent 上没有加载器来触发这些 skill，光有 markdown 不会自动激活。[推断]
- **你需要强制执行，而非建议。** 行为存在于 agent 读取的 prompt/markdown skill 里，没有任何硬闸门。agent 可以忽略或只部分应用某个 skill，「做 X」是一条指令，不是保证。[推断]
- **你需要一个固定、稳定的接口面。** 没有打 tag 的 release；skill/command 集合在 `main` 上随时间变化，且维护者明确会关闭没有对应 issue 的 PR（新增 skill / 结构性改动）——上游按维护者的节奏演进。需要可复现就 pin 一个 commit。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [stitch-skills](../design-to-code/stitch-skills.zh.md) | ✅ | 只需要面向 Stitch 的聚焦包，而不是全生命周期设计套件时，选 stitch-skills。 | 比的是范围：面向 Stitch 的包 vs. 这套覆盖全生命周期的设计套件。需求窄时聚焦包更轻；要广度则 Designer Skills 胜。 |
| [ui-ux-pro-max](ui-ux-pro-max.zh.md) | ✅ | 另一个 UI/UX skill pack 的交互指引或安装路径更适配你的 harness 时，选 ui-ux-pro-max。 | 另一个 UI/UX skill pack；在「打磨界面」这一面重叠很多。按哪一个的 UI/交互指引更对你胃口、哪种安装路径更适配你的 harness 来选。 |
| [taste-skill](taste-skill.zh.md) | ✅ | 只需要聚焦视觉*品味*/判断的窄包时，选 taste-skill。 | 聚焦视觉*品味*/判断；比这套多学科套件窄。要带品味色彩的批评判断用它；同时还需要研究/系统/ops 时用 Designer Skills。 |
| [make-interfaces-feel-better](make-interfaces-feel-better.zh.md) | ✅ | 只需要交互打磨和「手感」细节，而不是完整生命周期时，选 make-interfaces-feel-better。 | 面向交互打磨 /「手感」；与 Designer Skills 的 `interaction-design` plugin 重叠。窄包在微交互上更锋利；Designer Skills 还覆盖生命周期其余部分。 |
| [Anthropic Skills](../../vendor-collections/anthropic-skills.zh.md) / 内置 skills | 部分已收录 | 只想用平台自带 skill 生态，避免第三方 bundle 与原生 skill 重复时，选 Anthropic Skills 或内置 skills。 | 平台自带的 skill 生态；Designer Skills 是叠在上面的第三方 bundle，可能与原生 skill 重复或冲突。 |
| 家族里的姊妹合集（AI 产品设计、UX 项目管理、设计领导力、包容性设计） | 未收录 | 需求落在同作者家族的相邻学科，而不是「设计实践」合集时，选那些姊妹 repo。 | 同作者家族里的姊妹 repo；本条目只覆盖「设计实践」这一合集。相邻学科去用其它几个。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-09）：** 在 `main` 上活跃——最后 push 于 2026-09-05，未归档——但**仍然完全没有打 tag 的 release**（一个 tag 都没有），所以没有稳定、带版本的接口面可 pin；skill/command 集合持续演进，维护者会关闭没有对应 issue 的 PR。现在仓库里有了 `CHANGELOG.md`，成了事实上的版本锚点。
- **治理 / bus factor：** 单人维护、`User` 所有的仓库（`Owl-Listener`，README 署名 MC Dean），约 2.8k stars，是个人五个设计合集家族的一部分。路线图由一个人定；无组织或基金会背书。
- **年龄与 Lindy 判断：** 年轻（创建于 2026-03，约 6 个半月）——**未经验证**，但势头是真的：两次核验之间（2026-06 到 2026-09）stars 大约翻倍（1.7k→2.8k），设计实践合集也从 97 涨到 111 个 skill。仍然没有可复现的锚点；需要稳定就 pin 一个 commit。
- **风险旗标：** 仅建议性的 prompt/markdown（无运行时强制）、以 Claude Code 优先且 Gemini CLI 支持是 README 声称的、skill 数量为自报且家族已扩到 33 个 plugin。skill 包无 relicense/CVE 之忧，但「无 release + 单作者 + 大而全」这一组合才是真正的脆弱点。

## 存疑（未验证）

- [未验证] 数量——111 个 skill / 34 个 command / 9 个 plugin（本合集，按 README 的 plugin 表格）以及全家族 273 个 skill / 76 个 command / 33 个 plugin——是 2026-09-28 从项目 README 读到的，未逐文件独立审计；README 自身还不一致（某处写的是「all 107 skills」）。线上 `main` 树可能不同。
- [未验证] plugin 列表（design-research、design-systems、ux-strategy、ui-design、interaction-design、prototyping-testing、design-ops、designer-toolkit、visual-critique）来自 README；请以当前目录为准核实，不要直接依赖此列表。
- [推断] 由于 skill 是 agent 加载的 prompt/markdown，强制力是建议性的——「做 X」是指令、非硬保证，且各 harness（Claude Code vs Gemini CLI）的激活保真度不一。
- [推断] README 描述了通过 `.gemini/extensions/` clone-and-copy 的 Gemini CLI 支持，但此处未确认其可用；将与 Claude Code 的跨 harness 平价视为未验证。
