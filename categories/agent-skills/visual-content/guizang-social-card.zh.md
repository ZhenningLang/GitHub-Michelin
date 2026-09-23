---
name: Guizang Social Card Skill
slug: guizang-social-card
repo: https://github.com/op7418/guizang-social-card-skill
category: visual-content
tags: [skill, social-cards, xiaohongshu, wechat, editorial-design, swiss-design, claude-code, codex]
language: HTML
license: AGPL-3.0-only
maturity: no tagged release, active (last push 2026-05)
last_verified: 2026-06-26
type: skill-pack
upstream:
  pushed_at: 2026-05-27T16:58:08Z
  default_branch: main
  default_branch_sha: 032782ff67e0a20416bae8159f67000c1e4e7ae2
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:53:36Z
  overall: D
  overall_score: 1.33
  scored_axes: 3
  applicable_axes: 5
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: C
      raw:
        archived: false
        last_commit_age_days: 83
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
        repo_age_days: 118
        last_commit_age_days: 83
        cohort: skill-pack
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: E
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: true
        content_license: null
  unknowns:
    responsiveness: { reason: type_na }
    governance: { reason: unattributable }
  not_applicable:
    adoption: { reason: no_install_channel }
---

# Guizang Social Card Skill

一个 agent skill，把一个主题和几张图片变成小红书图文（1080×1440）以及公众号 21:9 + 1:1 封面对——单文件 HTML 经 Playwright 渲染成 PNG，由两套锁定的视觉系统（编辑杂志风与瑞士国际风）驱动。

![guizang-social-card — 健康度雷达](../../../assets/health/guizang-social-card.zh.svg)

## 何时使用

你是独立开发者、内容创作者或领域专家，日常活在 Claude Code 或 Codex 里，需要一批看起来“被认真排过版”而不是套 Canva 模板的社交图片。你手上有一篇写到一半的小红书笔记——一次旅行、一次产品拆解，或一份书单——外加一堆手机照片，而你不想手动摆文本框，也不想跟设计工具较劲。你把这个 skill 装上，说一句“做一套小红书图文”或“公众号 21:9 + 1:1 封面对”,agent 就走一套固定的 7 步流程：收集平台/风格/内容，在 Editorial（Monocle/Kinfolk 风，适合叙事/生活方式/旅行）和 Swiss（网格 + 单一锚定色，适合产品测评/数据/教程）之间选一个，从 28 个具名版式和 10 个主题预设里挑，抓取并本地缓存你的图片（写一份 `SOURCES.md` 署名文件），克隆一个种子 `.html`，再用 `node render.mjs` 渲染成 PNG。

它最适合你想要一套强烈、有主张的美学被预先内置、同时拿到一个你完全掌控的产物的场景。因为每套图就是一个自包含的 `.html` 文件，agent 能把它当文本来编辑、做 diff、无需构建链就重渲染——而一个可选的 Playwright 校验器（`validate-social-deck.mjs`）会在你交付前测量真实 DOM，检查溢出、字号上限违规、页脚碰撞和 Swiss 字重违规。你得到的是一套受约束、对 agent 可读的设计系统，带着平台需要的精确画布尺寸（`.poster.xhs` 1080×1440、`.poster.wide` 2100×900、`.poster.square` 1080×1080），而不是一张白纸。

## 何时不用

- **你要横滑幻灯片，而不是卡片。** 这个 skill 只做单张社交卡片和封面；README 把幻灯片需求路由给它的同门 [guizang-ppt](../slides-ppt/guizang-ppt.zh.md)。
- **你不在文件系统 + 浏览器 agent 里。** 它假设 agent 能读写文件、能跑 shell，且装了 Node + Playwright/Chromium(Claude Code、Codex、Cursor)。一个没有文件系统、没有 Node、没有 headless 浏览器的纯聊天机器人无法渲染出 PNG。
- **你要完全的颜色/品牌控制。** 主题只有预设——不允许自定义 hex（这是为保护美学一致性的刻意约束）。如果你必须命中精确品牌色，你会一直跟这套系统较劲。
- **照片精修、OOTD 穿搭图集、胶片颗粒或“真实素肌测试”类内容。** README 明确把这些放在范围之外；它只排布版式与文字，不编辑、不精修你的照片。
- **AGPL-3.0 对你是问题。** skill、模板、脚本都是 AGPL-3.0 许可；把其中部分塞进你对外发布的服务或产品会触发 copyleft（包括网络服务形态的衍生）——先读条款。
- **你需要一个长期稳定的契约。** 这是个年轻、迭代快、单维护者的 skill，目前还没有打 tag 的 release（最近一次 push 在 2026-05）；版式名、主题预设和问询流程可能在没有版本说明的情况下变动。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [guizang-ppt](../slides-ppt/guizang-ppt.zh.md) | ✅ | 需要完整多页横滑幻灯片而非单张卡片时，选 guizang-ppt。 | 同作者的同门 skill，定位是完整多页横滑幻灯片而非单张卡片/封面；视觉规则有重叠，产物形态不同。 |
| [html-anything](../../ai-design-generation/html-anything.zh.md) | ✅ | 需要通用的 agent 驱动 HTML 产物生成时，选 html-anything。 | 通用的 agent 驱动 HTML 产物生成；更宽泛、不带主张，因此缺少这个 skill 自带的锁定卡片版式、Swiss 校验器、平台画布尺寸和图片取材流程。 |
| [open-design](../../ai-design-generation/open-design.zh.md) | ✅ | 需要更宽的 UI/设计生成而非社交卡片专项时，选 open-design。 | 面向更宽的 UI/设计生成；不是带平台精确海报尺寸和渲染成 PNG 管线的社交卡片专家。 |
| [Impeccable](../../ai-design-generation/impeccable.zh.md) | ✅ | 需要设计质量 harness 层而非卡片生成时，选 Impeccable。 | 偏设计质量导向的生成；面不同——不是带 Playwright 校验器的单文件 HTML 卡片工作流。 |
| Canva / 稿定设计 | 未收录 | 需要托管模板 SaaS 而不是仓库时，选 Canva 或稿定设计。 | 托管模板 SaaS，不是仓库——对非 agent 用户更易上手、素材库更丰富，但封闭、无本地 agent 控制、无单文件 HTML 产物，视觉严谨度也低得多。 |
| Figma + 插件 | 未收录 | 需要完整的手工设计控制与协作时，选 Figma 加插件。 | 完整设计控制与协作，但纯手动；没有 agent 驱动的 7 步流程、没有自动取材，也不是你能 vendor 的仓库。 |

## 健康度与可持续性

- **响应速度**：无法计算——type_na。
- **维护（2026-06）：** [推断] 活跃但单薄——最近 push 在 2026-05-27，**完全没有打 tag 的 release**（pin 的是移动的 `main`），未关闭 issue 约 5。对一个一人 skill 包而言，这意味着版式名、预设和问询流程可能在没有任何版本说明的情况下变动。
- **治理与 bus factor：** [推断] **单人维护、`User` 个人仓库（`op7418`）、约 4k star**——一个 bus-factor 标记，不过比它的同门 `guizang-ppt`（约 19k）轻些，因为受众更小。没有组织或共同维护者兜底；它是同一作者 `guizang-ppt` 的同门，可持续性画像一致。缓解点：每套卡片都是你完全拥有的自包含 `.html`，因此废弃只会停掉后续更新。
- **年龄与 Lindy：** [未验证] 仓库约创建于 2026-05，截至 2026-06 约一个月——**全新；Lindy 先验为零。** 无发版线、迭代快——把契约（28 个版式、10 个预设、画布尺寸）当作不稳定的，请对照当前仓库核实。
- **风险标记：** [未验证] vendoring 时触发 **AGPL-3.0-only** copyleft（含网络服务形态的衍生）；渲染/校验脚本需要 Node + Playwright/Chromium；图片取材回退链依赖第三方 provider（Unsplash/Pexels/Flickr/Wallhaven），可能需要 key/网络。对静态 HTML 生成器而言无相关 CVE。

## 存疑（未验证）

- [未验证] 许可证依 GitHub `licenseInfo` API 与 `LICENSE` 文件读为 AGPL-3.0-only(2026-06-26)；依赖 copyleft 范围前请对照仓库核实确切 SPDX/版本。
- [未验证] 不存在打 tag 的 GitHub release（API 在 2026-06-26 显示 `latestRelease` 为 null）；最近一次 push 2026-05-27;star 约 4.0k——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 渲染脚本（`render.mjs`）与校验器（`validate-social-deck.mjs`）是 Node + Playwright 脚本；其确切依赖版本与规则覆盖来自 README 描述，未实际运行核实。Playwright 安装时会拉取 Chromium。
- [推断] “28 个版式”(Editorial M01–M16、Swiss S01–S12)、“10 个主题预设”以及 11 个小红书品类路由是项目自己在 README 里的表述；确切数量/命名可能随版本变动。
- [推断] 图片取材回退链（用户提供 → AI 生成 → Unsplash → Pexels → Flickr CC → Wallhaven）与 MapLibre/OSM 旅行地图来自 README；各 provider/API 在具体环境是否可用未经验证，可能需要 key 或网络。
- [推断] 引用的具体字体（Editorial:Playfair Display + Noto Serif;Swiss:Inter + Helvetica）与画布尺寸均来自 README；依赖精确渲染前请对照当前模板核实。
