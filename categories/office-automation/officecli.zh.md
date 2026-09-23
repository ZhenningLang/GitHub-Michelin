---
name: OfficeCLI
slug: officecli
repo: https://github.com/iOfficeAI/OfficeCLI
homepage: https://officecli.ai
category: office-automation
tags: [docx, xlsx, pptx, office, cli, ai-agent, openxml, single-binary, dotnet, mcp, document-generation]
language: C#
license: Apache-2.0
maturity: "v1.0.151, very active (last push 2026-09-16); 30.8k stars / 2.1k forks, created 2026-03-15 (API-verified), ~6-month-old repo, 151 releases"
last_verified: 2026-09-18
type: tool
upstream:
  pushed_at: 2026-09-16T18:40:37Z
  default_branch: main
  default_branch_sha: dced0d74ff85b1fef0b777efcdb637c2c4ef8a6e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:48:11Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 54.0
        qualifying_issues: 47
        band: relaxed_solo
        window_offset_days: 7
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: "@officecli/officecli"
        dependent_repos_count: 0
        downloads_last_month: 21585
        graph_tier: E
        volume_tier: D
        cross_check_divergence: null
        homebrew_installs_90d: 2327
        homebrew_tier: B
        release_downloads: 516361
        release_assets: 900
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: C
      raw:
        repo_age_days: 191
        last_commit_age_days: 1
        cohort: tool
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 20
        top1_share: 0.986
        top3_share: 0.994
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

# OfficeCLI

单二进制 .NET CLI，让 agent 通过 XPath 式路径和 JSON 输出读写、创建 `.docx`／`.xlsx`／`.pptx`，并用自研 HTML 渲染器闭合 render → look → fix 回路。

![OfficeCLI — 健康度雷达](../../assets/health/officecli.zh.svg)

## 何时使用

你在搭一条 agent 工作流，必须产出或修改**原生** Office 文件——一份 pitch deck、一份带格式的报告、一个含活公式的表格——而目标机器上既没有 Python 环境也没有 Microsoft Office。你选 OfficeCLI，因为它是本索引里唯一把三个格式装进一个约 34 MB 自包含二进制、零运行时依赖的选项，并且用同一套路径语法寻址（`/slide[1]/shape[2]`、`row[Salary>5000 and Region=EMEA]`），返回结构化 JSON。相对 [python-docx](python-docx.zh.md)／[python-pptx](python-pptx.zh.md)／[XlsxWriter](xlsxwriter.zh.md)，你用「一个 agent 不用写代码就能调的 CLI」换掉了「三套 Python API 加一个解释器」；相对 [Office-Word-MCP-Server](office-word-mcp-server.zh.md)，你拿到三个格式而不是只有 Word，且不需要装 MS Word。决定性特性是**渲染回看闭环**：`officecli view deck.pptx html|png` 让视觉模型能检查它刚造出来的东西，本分类里没有任何库提供这一环。适合一次性和迭代式的文档生成，且有人会肉眼过一遍结果。

## 何时不用

- **需要可重现的文档流水线** → 用 [python-docx](python-docx.zh.md)／[python-pptx](python-pptx.zh.md)／[XlsxWriter](xlsxwriter.zh.md) 并锁版本。OfficeCLI 平均每 1.58 天发一个 release（100 个 release 跨 2026-04-13 至 2026-09-16，API 已验证），**且自动更新默认开启**（`UpdateChecker.cs:853` — `AutoUpdate { get; set; } = true`），所以除非你在 `~/.officecli/config.json` 里关掉，同一个脚本两次运行可能产出不同结果。
- **任何需要可审计回归证据的场景** → 公开仓库里**没有测试工程**：`officecli.slnx` 引用了 `tests/OfficeCli.Tests/OfficeCli.Tests.csproj`，但它不在 1,208 个 tracked 文件里，且全仓零 xunit／NUnit／MSTest 引用（2026-09-18 验证）。`build.yml` 只在 `v*` tag 和 `workflow_dispatch` 时跑；PR 上只有一个 SKILL.md diff 检查。面对 278,904 行手写 OOXML，请优先选有公开测试套件的库。
- **气密或离线环境** → PNG 导出会 shell out 到外部浏览器（`Core/HtmlScreenshot.cs`：playwright CLI → Chrome／Edge／Chromium → Firefox；源码注释原文：*"No embedded browser engine"*），mermaid 转图需要 `mmdc` 或 headless 浏览器并从 `cdn.jsdelivr.net` 拉 `mermaid.min.js`，每日更新检查会连 `d.officecli.ai`。README 那句 "No dependencies. Works everywhere." 对渲染闭环的 PNG 那一半不成立。改用 [python-pptx](python-pptx.zh.md) 配自己的光栅化器，或用 [Pandoc](../markdown-tools/pandoc.zh.md) 做单向转换。
- **有严格 skill／prompt 治理的 harness** → `officecli install` 会往约 14 个探测到的 agent 目录写 skill 文件（`~/.claude/skills`、`~/.cursor/skills`、`~/.config/opencode/skills`、`~/.agents/skills`、`~/.openclaw/skills` 等），而 `SkillInstaller.RefreshInstalled()` 会在**每次版本变化时自动重推**。根 `SKILL.md` 是 25,974 字节的模型上下文。如果你的 agent 配置是版本控制且要过评审的，这一步绕过了评审。直接用那些库更合适。
- **长期基础设施押注** → 6,128 个 commit 里 98.2% 来自单一作者（`goworm` 6,017；第二名 55，API 2026-09-18 验证），仓库约 6 个月大。它的价值在覆盖广度（tracked changes、pivot cache、slicer、morph 转场、3D 模型、RTL／i18n）——恰恰是别人接不动的那部分。要依赖多年的东西，请用那些 13 年历史的库。
- **把文档读进 RAG** → 用 [MarkItDown](../document-parsing/markitdown.zh.md) 或 [Docling](../document-parsing/docling.zh.md)；OfficeCLI 的读取路径返回的是为编辑服务的 OOXML 形状 JSON，不是为摄取服务的干净 Markdown。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
| --- | --- | --- | --- |
| [python-docx](python-docx.zh.md) | ✅ | 如果你已经在跑 Python、且需要一个能审计能锁版本用多年的 Word 依赖，选 python-docx；如果 agent 必须在一台没有解释器的机器上同时处理三个格式，或者需要**看见**渲染结果，选 OfficeCLI。 | OfficeCLI 用「6 个月、单人作者的二进制加默认开启的自动更新」换来广度和渲染闭环；python-docx 用「Word 单格式、无渲染能力」换来 13 年的 MIT 许可稳定性。 |
| [python-pptx](python-pptx.zh.md) | ✅ | 在 Python 服务里做程序化幻灯片生成、且版本由你掌控，选 python-pptx；如果幻灯片是 agent 驱动且要反复迭代，选 OfficeCLI，因为 python-pptx 没有预览路径，且自 2024-08-07 起未再发版。 | OfficeCLI 提供 `watch` 实时预览加 HTML／PNG 反馈，以及 python-pptx 从未实现的动画与转场；python-pptx 提供一个稳定、可测、依赖轻、能冻结的库。 |
| [XlsxWriter](xlsxwriter.zh.md) | ✅ | 用 Python 做大批量表格**生成**选 XlsxWriter——它更快、只有 30 个 open issue、零依赖；需要**修改已有**工作簿、或消费方是 agent 而非脚本时选 OfficeCLI。 | XlsxWriter 是只写的，无法读取或编辑不是它自己创建的文件；OfficeCLI 能读能改能建，但它的公式引擎没有公开回归套件。 |
| [Office-Word-MCP-Server](office-word-mcp-server.zh.md) | ✅ | 任何新工作都选 OfficeCLI：那个 MCP server 已**归档**（2025-12-31），且它的 PDF 路径需要真实安装 MS Word；只有在维护一个已经依赖其 tool schema 的既有集成时才选它。 | MCP server 只提供 Word 单格式的标准化 tool 接口，且有 Windows／macOS 硬地板；OfficeCLI 提供三格式的 headless 能力，代价是集成形状是 CLI 而非 MCP。 |
| [MarkItDown](../document-parsing/markitdown.zh.md) | ✅ | 任务是「文档 → Markdown 供 LLM 摄取」选 MarkItDown；任务是「Markdown 形状的意图 → 原生 Office 文件」或就地编辑选 OfficeCLI。两者是同一条管道的相反方向，可以组合使用。 | MarkItDown 是只读的，且按设计会损失格式保真度；OfficeCLI 保留 OOXML 结构，但不是摄取工具。 |

## 技术栈

C#／.NET 10，以 self-contained + trimmed + single-file 发布 8 个 RID（osx／linux／win × x64／arm64，外加 linux-musl），每个二进制约 34 MB（release 资产，API 2026-09-18 验证）。NuGet 依赖只有两个：`DocumentFormat.OpenXml 3.4.1`（MIT）和 `System.CommandLine 3.0.0-preview.2`（MIT，**preview**）。360 个文件共 278,904 行 C#；HTML 渲染器、公式求值器（宣称 350+ 函数）、字体度量读取器、KaTeX 资源打包、图表 SVG 渲染器、mermaid 转原生形状全部自研。常驻文档会话走命名管道；`watch` 默认在 26315 端口提供 HTTP；内置 MCP server 模式（`McpServer.cs`，32 KB）。SDK 单独发布到 npm（`@officecli/sdk`）和 PyPI（`officecli-sdk`）。

## 依赖

读写、创建 `.docx`／`.xlsx`／`.pptx` 以及 HTML 预览：无依赖。**PNG 导出需要外部浏览器**：PATH 上有 playwright CLI，或 Chrome／Edge／Chromium，或 Firefox。**mermaid 转图需要 `mmdc`（mermaid-cli）或 headless 浏览器**，并会从 `cdn.jsdelivr.net` 下载 `mermaid.min.js`／`layout-elk`（有缓存，在每日后台任务里刷新）。默认网络外联：`d.officecli.ai`（项目自控的 Cloudflare 前置 nginx，跑在一台 VPS 上），以 `github.com` 为 fallback，每 24 小时一次，用于自动更新检查。无数据库、无 GPU、无需安装 Office。环境变量开关包括 `OFFICECLI_SKIP_UPDATE`、`OFFICECLI_NO_AUTO_INSTALL`、`OFFICECLI_NO_AUTO_RESIDENT`、`OFFICECLI_MMDC`、`OFFICECLI_WATCH_ALLOWED_HOSTS`。

## 运维难度

安装和运行**低**：下载二进制，或 `brew install officecli`／`npm install -g @officecli/officecli`，然后 `officecli install`。没有需要看护的服务——常驻会话是按文档粒度的命名管道进程，空闲会自动退出。但要**可预测地**运维是**中到高**，三个原因：（1）自动更新默认开启并会自我替换二进制；完整性校验做到 SHA256SUMS + magic bytes + smoke run，但**没有针对固定密钥的签名**（源码注释自己承认了这点），所以信任根是项目自己的 VPS；（2）同一个更新流程会改写你 agent 目录里的 skill 文件，那是一次你没过评审的模型上下文变更；（3）在没有公开测试套件、release 节奏约 1.58 天的前提下，锁版本并自己验证输出是获得可重现性的唯一办法。CI 场景请关掉自动更新、锁定版本，并在需要 PNG 时预装 headless 浏览器。

## 健康度与可持续性

- **维护：节奏极强，已验证** —— v1.0.151 发布于 2026-09-16；自 2026-04-13 起 151 个 release（约每 1.58 天一个，API 验证）；最后 push 2026-09-16，距验证日两天；6,128 个 commit。
- **治理：实质单人** —— `goworm` 提交了 6,128 个 commit 中的 6,017 个（98.2%）；第二名 55 个，第三名 14 个（API 2026-09-18 验证）。`NOTICE` 写明 "Created and maintained by goworm"。无基金会、无 CLA、无 RFC 流程。
- **背书与寿命** —— 所属 org `iOfficeAI` 是 AionUi 团队（aionui.com）；桌面 agent 协作应用 AionUi 有 32.9k star，并把 OfficeCLI 用作文档引擎。[推断] 因此路线图优先服务 AionUi 的产品需求。未发现 open-core 功能门：对 README 和源码 grep 付费／云／license key 层级只返回误报（2026-09-18）。
- **年龄／Lindy：雷达给 `C`，先验要求打折** —— 创建于 2026-03-15，验证时 187 天大，最后 commit 距今 2 天。机器把长青度评为 `C`，因为仓库年轻但确实活跃；Lindy 先验依然要打折，因为「预期剩余寿命」是由年龄 × 仍活跃预测的，而 6 个月的历史什么也预测不了。对照 python-docx（2013）、python-pptx（2012）、XlsxWriter（2013，长青度 `A`）。
- **采用度：决定性的负面项，而且是实测的** —— 健康度雷达记录到**上月 npm 下载 21,585 次、依赖仓库 0 个**（2026-09-18）。在同一分类里，[python-docx](python-docx.zh.md) 实测 94,383,978 次下载和 3,530 个依赖仓库，[XlsxWriter](xlsxwriter.zh.md) 是 87,471,871 次和 3,828 个——下载量差距约 **4,000 倍**，而对方做的还是更窄的活。与此同时仓库有 30,797 star／2,099 fork（star 比 fork 为 14.7，属正常区间，所以不像是明显刷出来的），48 个 open／175 个 closed issue 加 179 个 PR，即有真实用户交互。[推断] star 和 issue 流量度量的是关注度；依赖仓库和下载量度量的是被嵌入程度。OfficeCLI 有前者、几乎没有后者，而同一 org 在 13 个月内产出两个 30k star 仓库、其余四个只有 30 至 125 star——这读起来更像强分发能力，而不是与之成比例的生产使用量。
- **怎么对照本页结论读那个 `B (6/6)` 雷达** —— 卡片聚合的是实测信号，且明确**不是**选型结论。OfficeCLI 在维护项拿 `A`（最近 13 周全部活跃）、响应度拿 `A`、许可风险拿 `A`，这三项把总评抬到 `B`；采用度是 `B`，而治理是 `D`、长青度是 `C`。那个 `D` 恰恰是「何时不用」里承重的风险，而且雷达没有任何一个轴能度量「没有公开测试套件」或「默认自动更新并改写你的 agent 配置」——所以这里的 `B` 不该被读成「可以放心依赖」。
- **风险标记** —— 无公开测试、PR 无构建／测试 CI（见「何时不用」）；默认开启的自动更新来自项目自控 VPS 且无固定密钥签名；自动改写 agent skill 目录；依赖一个 `preview` 版 NuGet 包（`System.CommandLine 3.0.0-preview.2`）；`officecli.slnx` 引用了仓库里不存在的测试工程，所以按检出状态构建整个 solution 会失败。正面项：存在 `SsrfGuard.cs` 和 `HyperlinkUriValidator.cs`，release 附带 `SHA256SUMS`，npm／PyPI 发布走 OIDC trusted publishing 而非长期 token，`SECURITY.md` 指向 GitHub 私密漏洞上报。

## 存疑（未验证）

- [未验证] 所有渲染保真度主张（"high fidelity"、"reproduces documents with high fidelity"）——本次评审未执行该二进制；仓库里不存在保真度基准，也没有公开测试套件可供对照。验证需要一个装了浏览器的复现环境。
- [未验证] 「350+ 内置函数并自动求值」的公式引擎主张——`Core/Formula/FormulaEvaluator.Functions.cs` 确实存在且体量很大，但函数数量与对 Excel 语义的正确性既未枚举也未执行验证。
- [未验证] 生成的文件能否在真实 Microsoft Office／LibreOffice 中干净打开，覆盖完整特性面（tracked changes、pivot cache 写时复制、slicer、morph 转场、3D `.glb` 模型）。没有公开的 round-trip 固定样本。
- [未验证] 实际的 PNG／HTML 视觉质量与分页行为——取决于现场有哪个外部浏览器及其版本；本次未实测。
- [未验证] npm 下载数（16,081／月，健康度雷达 2026-09-18）只反映 npm 渠道；`curl | bash`、Homebrew 和直接下载 release 资产的安装未被计入，所以总采用量高出一个未知倍数。`dependent_repos_count: 0` 这一测量基于 GitHub 依赖图，同样低估了私有和非 GitHub 的消费方——但相对 python-docx 约 5,000 倍的差距，太大而不可能只由渠道构成解释。[推断]
- [推断] 公开测试工程缺失意味着测试是私有存在的——多处源码注释引用了测试行为（"so tests can override `$HOME` between cases"），暗示存在一套只是没提交上来的内部套件。无法从公开仓库确认。
- [推断] 路线图从属于 AionUi 是由 org 归属和 README 把 AionUi 定位为 GUI 前端推断出来的；没有公开路线图或治理文档这么写。
- [未验证] `d.officecli.ai` 是否在所有情况下都提供与 GitHub Releases 逐字节相同的资产；代码把 GitHub 当 fallback，但镜像的同步延迟未测量。
- [未验证] `watch` HTTP 服务的绑定地址与鉴权姿态——源码里确认了默认端口（26315）和 `OFFICECLI_WATCH_ALLOWED_HOSTS` 开关，但监听器的网卡绑定未追踪。
