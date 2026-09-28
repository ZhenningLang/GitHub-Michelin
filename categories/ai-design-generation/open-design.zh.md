---
name: Open Design
slug: open-design
repo: https://github.com/nexu-io/open-design
category: ai-design-generation
tags: [ai-design, local-first, desktop-app, electron, byok, design-systems, prototyping, slides, mcp]
language: TypeScript
license: Apache-2.0
maturity: v0.24.x, active, ~98k stars (as of 2026-09)
last_verified: 2026-09-28
type: app
upstream:
  pushed_at: 2026-09-28T04:50:02Z
  default_branch: main
  default_branch_sha: 1b47e60bd46641469fcd8b69c496c4e3a548bc28
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T04:59:10Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 4
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.1
        qualifying_issues: 15
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 1757
        homebrew_tier: B
        release_downloads: 946958
        release_assets: 246
        release_tier: C
        signal_basis: homebrew+releases
    longevity:
      grade: D
      raw:
        repo_age_days: 153
        last_commit_age_days: 4
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 94
        top1_share: 0.194
        top3_share: 0.359
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Open Design

一个 local-first、BYOK 的 Electron 桌面应用，把编码 agent 变成设计工作室——生成沙箱化 HTML 原型、杂志风幻灯片、品牌级图像，以及 HTML→MP4 动态图形，全部由可复用的 Skills 和 `DESIGN.md` 设计系统驱动。

![open-design — 健康度雷达](../../assets/health/open-design.zh.svg)

## 何时使用

你是产品工程师或设计师，已经常驻在某个编码 agent 里（Claude Code、Codex、Cursor、Copilot 等），希望它能*产出设计交付物*，而不只是写代码——一个可点击的移动端原型、一份路演 deck、一张品牌社交卡片——而又不想把你的 prompt 和素材都送进别人的云。你在意的是：一切跑在自己机器上、用自己的模型 key、产物是你能留存的纯 HTML/PDF/PPTX/MP4。Open Design 给你一个桌面版“Studio”：agent 读取 `DESIGN.md` 设计系统，在沙箱 iframe 里渲染原型，导出 deck、图像、dashboard 和 HyperFrames（HTML→MP4）——并自带 100+ 功能 Skill 与 151 套品牌设计系统包（Linear、Stripe、Apple、Notion 等）作为起点。

当你想要一个能接入*你已有的任何 agent* 的统一设计面时，它同样合适。它不把你锁死在单一助手上，而是通过 MCP server 和 BYOK 代理（任意 OpenAI 兼容端点）对外暴露，同一套原型/deck 工作流可被 26 个不同的编码 agent CLI 调用（daemon 注册表共 27 条运行时定义）。你在类浏览器的渲染器里做原型、对 live artifact 就地迭代，然后导出文件就走——开源路径无需账号、不按席位计费，不过自 v0.9 起应用内也提供可选的付费登录式模型服务，适合不想自己管 key 的人（v0.9 上线时名为 **OpenDesign AMR**，现称 **OpenDesign Cloud**）。

## 怎么用起来

OpenDesign 是一个本地 daemon，上面罩着设计工作台面——Electron 桌面、浏览器 UI，或无头的 `od` CLI——并且刻意*不自带 agent*。你选定产物类型（原型、deck、图像、HyperFrames 视频）和简报后，daemon 会拉起你机器上已装好的编码 agent CLI（26 个不同的可执行文件），或经 BYOK 代理流式调用你配置的任意 OpenAI 兼容端点；模型永远是你的。agent 随后在磁盘上组装三样开放、可版本化的东西——**skill/plugin**（工作流）、**设计模板**（渲染蓝图）、**`DESIGN.md`** 设计系统（品牌契约，仓库内自带 151 套）——产出真实 HTML/CSS 项目文件，而非专有文档。daemon 把这些文件渲染进仅回环（127.0.0.1）的 sandboxed iframe 供你在 Studio 里检查迭代，HyperFrames 经 headless Chrome + FFmpeg 把动态图形确定性渲染成 MP4，成品可导出 HTML/PDF/PPTX/MP4/ZIP/Markdown。留在你手上的：模型 key（或可选的付费云服务登录）、agent 运行时、每一个输出文件——另注意：产品分析与 session replay 需同意才开启，但 README 声明脱敏后的安全/可靠性遥测始终在运行。

![open-design — 主干用户故事](../../assets/flow/open-design.zh.svg)

<!-- flow-steps:begin (generated from flows/open-design.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：装桌面应用（macOS/Windows），或直接把 agent 接上 — `od mcp install claude`
2. **你**：选产物类型、插件与一套 DESIGN.md 设计系统，写简报
3. **Open Design**：启动你 PATH 上已有的编码 agent CLI，或走你的 BYOK 端点 — 组件：`本地 daemon`
4. **Open Design**：把 Skill、模板与品牌契约组装成真实项目文件，沙箱里预览 — 组件：`被拉起的 agent`
5. **你**：在 Studio 里迭代，导出成品

**价值**：原型、deck、视频都以真实文件留在本机——不用托管工作室，不锁模型

</details>
<!-- flow-steps:end -->

## 何时不用

- **你想要托管、零配置的 SaaS。** 这是一个你需要安装并运行的桌面应用（Electron + 本地 Node daemon）。如果你更想登录一个网站、由厂商打理一切，那么专有的 Claude Design / 类似托管工具更契合——本项目是用这份便利换本地掌控。
- **你需要真正的矢量设计 / 自由画布编辑。** 它生成的是*代码渲染*的产物（HTML/PPTX/MP4），不是可编辑的矢量文档。它定位为“生成侧的 Figma 替代”，但并非协作矢量编辑器——要逐像素手调、实时多人协作或精确矢量工作，Figma/Penpot 仍是该用的工具。
- **早期成熟度 / 频繁变动。** 它仍是 pre-1.0（v0.24.1，从 v0.21 到 v0.24 只用了截至 2026-09-24 的四周），一个五个月大的仓库挂着约 500 个未关闭 issue；Skills、插件格式和 agent 适配面都还在动。[推断] 锁定风险低（开放格式、Apache-2.0），但 minor 版本之间出现破坏性变更是有可能的。
- **你在 Linux 桌面上用。** 官方 release **没有预打包的 Linux 产物**（只有 macOS Apple Silicon/Intel + Windows x64；Linux 由 issue #4368 跟踪）——必须用 Node ~24 + pnpm 从源码跑，那是真正的搭建步骤，不是下载。
- **没有 GPU/视频预算却要大量 MP4。** HyperFrames（HTML→MP4）和视频生成依赖本地渲染加上你的 BYOK 模型花费；大批量视频既不免费也不即时。
- **你无法或不愿管理模型 key。** 开源路径就是 BYOK——没有内置免费推理。v0.9 起可选的付费登录服务（上线时叫 OpenDesign AMR，现称 OpenDesign Cloud）能免去管 key，但那是商业托管服务；API key 和付费云订阅都不能接受的话，你就生成不了。
- **你要求“local-first”工具零外发。** 产品分析与 session replay 需同意才开，但 README 声明脱敏后的安全/可靠性遥测始终运行——local-first 是默认姿态，不是绝对保证。
- **团队级的生产设计系统治理。** 它是单用户的本地 studio；没有内置多人协作、评审流程或中心化资产治理。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [html-anything](html-anything.zh.md) | ✅ | 只需要把 prompt 变成独立 HTML 产物时，选 html-anything。 | 同类目下专注把 prompt 变成独立 HTML 产物的同胞；Open Design 是围绕这一想法更重的完整桌面 studio（deck/视频/设计系统/导出）。 |
| [Impeccable](impeccable.zh.md) | ✅ | 任务只要求高精度 UI 生成时，选 Impeccable。 | 同胞，主打高精度 UI 生成；Open Design 覆盖更广（幻灯片、图像、视频、MP4）且以本地应用而非更窄的生成器形态交付。 |
| [guizang-ppt-skill](../agent-skills/slides-ppt/guizang-ppt.zh.md) | ✅ | 只需要 deck 生成这个单一 Skill 时，选 guizang-ppt-skill。 | 单一用途的 deck 生成 Skill；Open Design 把 deck 生成作为众多产物类型之一，并自带运行时/导出。 |
| [guizang-social-card-skill](../agent-skills/visual-content/guizang-social-card.zh.md) | ✅ | 产物明确是社交卡片时，选 guizang-social-card-skill。 | 专注社交卡片的 Skill；Open Design 在一个打包应用里覆盖卡片/图像等多种产物类型。 |
| Claude Design（Anthropic，托管） | 未收录 | 托管云和产品打磨度比 local-first/BYOK 控制更重要时，选专有托管产品。 | 本项目克隆的专有托管产品；托管云 + 打磨度 vs Open Design 的 local-first、BYOK、开放格式立场。 |
| v0（Vercel） | 未收录 | 目标是托管 prompt-to-web-UI 生成，而不是本地多产物 studio 时，选 v0。 | 托管的 prompt-to-UI 生成器；云 SaaS、范围更窄（偏 web UI），vs Open Design 的本地多产物 studio。 |
| Figma / Penpot | 未收录 | 需要多人协作的矢量编辑，而不是代码渲染产物时，选 Figma 或 Penpot。 | 真正的矢量设计编辑器，带多人协作；Open Design 生成代码渲染产物，而非可编辑矢量文档。 |

## 技术栈

- **语言：** TypeScript（仓库主语言）。
- **前端/Studio：** Next.js 16 App Router + React 18（按 README 架构表）。
- **本地 daemon：** Node 24 · Express · SSE 流式 · `better-sqlite3` 存储项目/会话。
- **桌面外壳：** Electron + 沙箱 renderer；有文件系统的路径把规范项目文件渲染进沙箱 iframe，纯 BYOK/API 路径把一个完整 `<artifact>` 块解析进沙箱 `srcdoc` iframe；daemon 绑定 127.0.0.1（局域网暴露需显式 `OD_BIND_HOST` + `OD_ALLOWED_ORIGINS`）。
- **集成：** stdio MCP server 加按 agent 的安装器（`od mcp install <agent>`）；多供应商 BYOK 代理（`/api/proxy/{anthropic,openai,azure,google,ollama,senseaudio}/stream`）支持任意 OpenAI 兼容端点，在 daemon 边缘做 SSRF 防护；26 个不同本地 CLI 可执行文件、27 条运行时定义，DeepSeek Harness（`dsh`）是一等公民的原生运行时。
- **内容：** 100+ 功能 Skill（`skills/`）+ 独立的渲染模板目录（`design-templates/`）、151 套 `DESIGN.md` 设计系统包、277 个官方插件（另有 183 个可改写示例）、15 套 deck 模板 × 36 主题、93 个图像提示模板、11 个 HyperFrames 模板 + 39 条 Seedance 提示。
- **视频：** HyperFrames 是 HeyGen 的 Apache-2.0 agent 原生框架——agent 写 HTML+CSS+GSAP，经 headless Chrome + FFmpeg 确定性渲染成 MP4；可选路由 Seedance/Veo/Sora/Kling 模型变体与 Suno/Lyria 音频。
- **导出：** HTML、PDF（浏览器打印）、PPTX、MP4、ZIP、Markdown。

## 依赖

- **运行时：** 从源码运行需 Node ~24 与 pnpm 10.33.x；打包桌面版**只有 macOS（Apple Silicon + Intel）和 Windows（x64）**——暂无预打包 Linux 产物（issue #4368 跟踪）。
- **模型：** 一个 OpenAI 兼容（或 Anthropic/Azure/Google/Ollama）端点的 BYOK key——开源路径的生成都必需；可选的付费 OpenDesign Cloud 订阅是零配置的替代。
- **数据存储：** 本地 SQLite（`better-sqlite3`）；核心使用不需要外部数据库/服务。
- **视频路径：** MP4 导出要求本机有 headless Chrome + FFmpeg（HyperFrames 渲染管线，README 所述）。
- **可选：** Docker（`deploy/` compose，web UI 在 127.0.0.1:7456、`OD_API_TOKEN` basic auth 之后）、Sealos 模板，或 web 版走 Vercel。

## 运维难度

**桌面使用低，源码/web 部署中。** 最快路径是预打包桌面应用：下载、填 BYOK key（或登录 OpenDesign Cloud）、生成——几乎零运维，全程本地。从源码运行或自托管 web 构建则是**中**：你要管理 Node ~24 / pnpm 版本、本地 daemon（`pnpm tools-dev` 生命周期）和 Docker/Vercel 部署，再加上跨 OS 的 Electron 摩擦——且 macOS/WSL2 上裸 `od` 命令与系统自带的八进制转储程序同名，README 让桌面用户改从 Settings → MCP 复制绝对路径片段。因为它 local-first 且单用户，没有服务器集群要维护，但你确实要自己负责模型 key 管理、跟上快速 minor 发版（v0.21 → v0.24 只用了四周），以及本机的 Chrome/FFmpeg 视频工具链。

## 健康度与可持续性

- **响应速度**：Grade A——中位首次响应时间 0.1 小时，基于 15 个 qualifying issues/PRs（评分器，2026-09-28）。
- **维护（截至 2026-09）：** 未归档；最后提交距评分 4 天，近 13 周全部 13 周活跃，v0.21.0 → v0.24.1 发布于 2026-08-25 → 2026-09-24。极其活跃；五个月大的仓库挂着约 526 个未关闭 issue，既说明用得多，也说明这是个快速变动、尚未稳定的产物面。[推断：把 issue 量读作使用强度]
- **治理与 bus factor：** 由 `Organization`（nexu-io）持有，12 个月内有 94 位活跃贡献者、头号贡献者只占约 19% 提交——年轻仓库里这已算真正的团队而非孤胆维护者。但组织小而未经验证；付费的 OpenDesign Cloud 服务暗示商业背书，资金与路线图归属仍未核实。[推断：由云服务推断商业资助]
- **年龄与 Lindy 判断：** 建于 2026-04-28，评分时仓库 153 天——**非常年轻**，star 在发布热潮后仍持续上涨（本页 2026-06 复核时约 71k → 2026-09-28 约 98k）。热潮退去后仍在增长是好信号，但不等于耐久；仍不是 Lindy 安全的押注，按「有前景但未被证明」权衡。
- **采用/生态：** 90 天 Homebrew 安装 1,757 次、GitHub release 下载 946,916 次（评分器，2026-09-28）；对 26 个不同 agent CLI 的适配面加 MCP，让它能从 agent 团队已有的工作位置接入。
- **风险标记/锁定：** 好处仍是锁定确实低——Apache-2.0、local-first、BYOK、开放导出格式（HTML/PDF/PPTX/MP4），即便项目停摆你也留得住产物。要盯的：插件/Skill 格式定型前的 minor 破坏性变更；OSS 核心旁边多了一个付费云服务面；分析与 session replay 需同意，但脱敏安全遥测始终开启（README）。

## 存疑（未验证）

- [未验证] v0.24.1 发布于 2026-09-24（GitHub releases，截至 2026-09-28）；发版约每周一次，任何版本 pin 都会快速过时。
- [未验证] star 约 98.4k（截至 2026-09-28）——GitHub star 不可靠且对时间敏感，仅供参考。
- [未验证] 内容数字（151 套设计系统、277 官方插件 + 183 示例、100+ Skills、26 CLI / 27 运行时定义、93 图像提示、11+39 视频模板）是当前 README 自己的表述，随版本变动；约 526 个未关闭 issue 来自 2026-09-28 的 GitHub search API，含机器人/PR 噪声。
- [未验证] 框架/运行时版本（Next.js 16、React 18、Node ~24、pnpm 10.33.x）取自 README 架构表，未对照 lockfile 独立确认。
- [未验证] README 路线图写着“AI-emitted tweaks panel UX——尚未实现”，产品导览却演示了 live-dashboard 的 tweaks 面板；就地参数编辑的现状在来源内部自相矛盾。
- [未验证] OpenDesign Cloud 的定价、条款与可用性是商业托管服务细节，本轮未核查。
- [推断] AMR → Cloud 的品牌连续性：v0.9 的 release notes 引入登录式的 OpenDesign AMR 模型服务，v0.13 起的 notes 与当前 README 称之为 OpenDesign Cloud（登录/钱包界面一致），但 CHANGELOG 未明说改名。
- [推断] “Figma 替代” / “Claude Design 替代”是项目的定位说法，而非功能对等的保证。
