---
name: Baoyu Skills
slug: baoyu-skills
repo: https://github.com/JimLiu/baoyu-skills
category: content-production
tags: [agent-skills, translation, markdown, content-creation, claude-code, codex]
language: TypeScript
license: MIT
maturity: v2.5.2, active (2026-06)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-06-28T06:42:07Z
  default_branch: main
  default_branch_sha: c9a50cc908d0473f5d754efdbe08cbe387714f63
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T10:48:10Z
  overall: B
  overall_score: 2.75
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 1
        active_weeks_13: 13
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
        repo_age_days: 171
        last_commit_age_days: 1
        cohort: skill-pack
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 38
        top1_share: 0.894
        top3_share: 0.912
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
    adoption: { reason: no_package_structural }
---

# Baoyu Skills

宝玉出品的 20+ 个 coding agent 技能合集——翻译、markdown/HTML 排版、字幕与网页抓取，外加图片/图表/幻灯片生成——可装入 Claude Code、Codex 等支持 skill 的 harness。

![baoyu-skills — 健康度雷达](../../../../assets/health/baoyu-skills.zh.svg)

## 何时使用

你是一个常驻终端的双语内容创作者或开发者，而你围绕代码的真正工作是**发布**：把一篇英文随笔翻成可发表质量的中文、把原始字幕整理成干净文章、把杂乱 markdown 排版成适配公众号的样式，或在动笔写摘要前先抓下一段 YouTube 字幕。这些活儿你的 coding agent 单拎出来都能干——前提是你每次手搓 prompt；但你总在重复讲同一套流程，而且翻出来的稿子机器味重、读着不像人写的。你想把这些动作一次性沉淀成一组有主见、可按名调用的技能。

Baoyu Skills 正好覆盖了写作/翻译这一片：`baoyu-translate` 跑三档工作流（快翻 / 普通 / 精翻，精翻档走 分析 → 初稿 → 审校 → 润色 并支持自定义术语表）,`baoyu-format-markdown` 给纯文本补 frontmatter 和结构，`baoyu-markdown-to-html` 套上公众号主题，`baoyu-url-to-markdown` / `baoyu-youtube-transcript` 给流水线喂干净的源文本。安装一次（`npx skills add jimliu/baoyu-skills`，或插件市场）,agent 就会通过平台原生的 skill 加载机制按需载入每个技能，而不必你每次粘贴 prompt。

## 何时不用

- **你只想要翻译/去机器味，不想要整包。** 这是一个宽口径的 20+ 技能包（图片、信息图、幻灯片、发到 X/公众号/微博、Electron 抽取）。只为 `baoyu-translate` 装它会引入一大片表面积和一套你未必想要的 TypeScript 辅助包安装。单一用途的翻译/去 AI 痕技能更轻。
- **你已有一套自管的技能/voice 体系。** 若你已有自己的翻译或去机器味技能，把宝玉这套有主见的工作流叠上去会造成双路由、术语表/voice 指令冲突——只保留一个事实源。
- **你不在受支持的 harness 上。** 它通过各平台的 skill 加载器激活（README 称支持 Claude Code、Codex 等支持 skill 的 agent）；在没有加载器的自定义 agent 上，这些 markdown 技能不会自动触发。[推断]
- **你不信任非官方/逆向后端。** 部分技能（`baoyu-danger-gemini-web`、`baoyu-danger-x-to-markdown`）明确包了非官方 API 并带着项目自己的免责声明；写作类技能没有，但它们同仓发布。
- **你需要硬性强制。** 技能行为由 prompt/markdown 驱动，属建议性——agent 可以偏离；“精翻档”是一份有文档的工作流，不是保证。[推断]
- **单维护者、快速迭代的上游。** 频繁发版（v2.x）意味着一次版本跳变可能改掉某技能的 prompt、档位或路由；请锁版本，升级后重新核对。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Humanizer-zh](../de-ai-writing/humanizer-zh.zh.md) | ✅ | 只需要聚焦中文去机器味和 voice 调整时，选 Humanizer-zh。 | 一个聚焦的中文 AI 文本去机器味技能——窄而单一（去 AI / voice），而 Baoyu Skills 是宽口径的内容/发布套件，其翻译技能只是 20+ 之一。只想去机器味就选聚焦的那个；想要整条 翻译→排版→发布 流水线就选 Baoyu。 |
| 手写项目技能 | 未收录 | 完全控制和零第三方表面积最重要时，选手写项目技能。 | 自己写 `SKILL.md` 做翻译/排版能拿到完全控制权、零第三方表面积，但三档工作流、术语表处理、HTML 主题都得你自建自维护。 |
| 单条去 AI / 翻译 prompt | 未收录 | 任务不需要持久化、版本化或按名加载时，选一次性 prompt。 | 一次性 prompt 是单任务下最轻的选择，但它不会像已安装技能那样跨会话持久化、版本化、按名加载。 |
| harness 自带技能生态 | 未收录 | 想优先用原生 harness 等价技能、避免第三方重叠时，选自带技能生态。 | harness 自家市场里的技能；Baoyu 是叠在其上的第三方合集，可能与原生等价物重叠或冲突。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护** —— [未验证] 最近一次 push 在 2026-06，未归档，open issue 约 1 个；v2.5.2（2026-06）加上 v2.x 的快速发版节奏，使其**活跃、甚至快速迭代**——并且发布了真正带版本号的 release，而非只跟 `main`。
- **治理与 bus factor** —— [推断] **`User` 所有、单人维护（「宝玉」/JimLiu）、约 22k star（2026-06）——这是一个 bus-factor 风险标记。** 个人项目，无团队或组织背书；节奏与延续性都压在一个作者身上。
- **年龄与 Lindy** —— [推断] 创建于 2026-01，截至 2026-06 仅约 5 个月：**全新，无 Lindy 履历**。热门但尚未经时间检验。
- **风险标记** —— [推断] 快速发版意味着一次版本跳变可能改掉某技能的 prompt、档位或路由——请锁版本，升级后重新核对。[未验证] 部分 `baoyu-danger-*` 技能包裹非官方/逆向后端（可能失效或违反第三方条款）；写作类技能不涉及，但同仓、同发布节奏。MIT 许可。

## 存疑（未验证）

- [未验证] 最新发布据称为 v2.5.2（2026-06-18 发布），仓库最后 push 于 2026-06-20;license 为 MIT、主语言 TypeScript，均据 2026-06-26 的 GitHub 元数据——依赖某具体版本行为前请重新核验。
- [未验证] star 数（2026-06-26 GitHub 显示约 22.5k）不可靠且与日期相关；仅作参考，不当质量信号。
- [未验证] 技能清单（`skills/` 下 21 个目录，含 `baoyu-translate`、`baoyu-format-markdown`、`baoyu-markdown-to-html`、`baoyu-url-to-markdown`、`baoyu-youtube-transcript` 及图片/图表/幻灯片/发布类技能）来自仓库文件列表与 README；具体集合与各技能档位会随版本变动——请查当前 `skills/` 目录。
- [未验证] 受支持 harness（Claude Code、Codex 等支持 skill 的 agent）与安装路径（`npx skills add`、插件市场、拷入 `.agents/skills/`）来自 README；实际激活保真度因 harness 而异，此处未独立确认。
- [推断] 由于技能逻辑存于 agent 加载的 markdown（TypeScript workspace 包作为辅助），强制力属建议性——有文档的档位/工作流是 prompt 级指令，非硬性保证。
- [推断] 翻译/去机器味的质量取决于 agent 所跑的底层模型；技能编排工作流，本身不附带翻译引擎。
- [未验证] `baoyu-danger-*` 类技能据 README 包裹非官方/逆向后端，可能失效或违反第三方条款；写作类技能不涉及，但同仓、同发布节奏。
