---
name: Ponytail
slug: ponytail
repo: https://github.com/DietrichGebert/ponytail
category: engineering
tags: [yagni, over-engineering, behavior-ruleset, agent-skill, multi-harness, token-cost]
language: JavaScript
license: MIT
maturity: v5.1.0 (Ponytail 5 rewrite, 2026-10-08), active, ~160k stars (as of 2026-10)
last_verified: 2026-10-10
type: skill-pack
homepage: https://ponytail.dev
upstream:
  pushed_at: 2026-10-08T16:19:55Z
  default_branch: main
  default_branch_sha: 9cc65d03aa2da1db7121b912d03596409ee340b8
  archived: false
health:
  schema: 1
  computed_at: 2026-10-10T02:36:11Z
  overall: B
  overall_score: 3.0
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
        last_commit_age_days: 1
        active_weeks_13: 7
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: npmjs.org
        canonical_package: "@dietrichgebert/ponytail"
        dependent_repos_count: 0
        downloads_last_month: 80139
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 120
        last_commit_age_days: 1
        cohort: skill-pack
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 98
        top1_share: 0.497
        top3_share: 0.568
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

# Ponytail

你让编程 agent 加个日期选择器，它装一个库，或者手写 335 行日历；可仓库里本来就有 `Input` 组件，浏览器也自带 `type="date"`。Ponytail 把「你见过最懒的那位资深工程师」的条件反射装成一套常驻规则。动手前，agent 先列出这次改动必须波及的所有地方；再沿一架短阶梯取第一个可行的选项（不做、复用、标准库、已装依赖、一行）；每次回复结尾说清跳过了什么、没核实什么。校验、安全、错误处理永远不在可砍之列。

![Ponytail — 健康度雷达](../../../assets/health/ponytail.zh.svg)

## 何时使用

你用 Claude Code、Codex、Copilot CLI 或 Ponytail 适配的另外约 20 种宿主干活，反复撞上的毛病不是流程而是虚胖：该用标准库的地方它加依赖，`@lru_cache` 一行能解决的事它写一个缓存类，20 行的任务留下 400 行 diff。这时选 Ponytail：它是一层行为覆盖，让 agent 交出最小但**完整**的改动。两条 slash 命令装好，强度分档（`lite/full/ultra/off`）。5.0（2026-10-08）起还带两个命令：`/ponytail-review` 完整审查当前改动（bug、安全、负载、缺的测试、速度、该砍的），`/ponytail-audit` 对整个仓库做同样的检查并排出先修什么。

为什么要装一个包，而不是自己在 AGENTS.md 里写一句「YAGNI，写一行」？在作者 6 月的基准里，裸提示词发挥不稳，还是唯一丢掉安全护栏的那一路 [未验证：作者自建基准，未独立复现，见 benchmarks/results/2026-06-18-agentic.md]。这个包还靠一个 CI 检查让同一套规则在约 20 个宿主适配之间保持一致，手写规则会随编辑器各自漂移。

## 怎么用起来

你只装一次。有插件机制的宿主（Claude Code、Codex、Copilot CLI、OpenCode、Gemini、Grok、Devin、Hermes…）装插件；只吃指令文件的宿主（Cursor rules、Windsurf、Cline、Copilot Chat、Kiro…）拷一份 `AGENTS.md` 或对应的规则文件。之后由生命周期 hook 干活：宿主在会话启动、每次提交 prompt、派生子 agent 时运行的几个小 Node 脚本。它们注入规则，跟踪 `/ponytail lite|full|ultra|off` 切档；设了 `PONYTAIL_SUBAGENT_MATCHER` 正则时，还能圈定给哪些子 agent 注入。

5.0 新增：会话启动 hook 会附上一份**代码地图**，列出仓库源文件里的顶层函数、类和导出，每个目录一行，总长不超过 2000 字符。地图由 `git ls-files` 加每种语言一条正则生成，不调模型。目的是让「先复用」不用再花一次搜索。设 `PONYTAIL_MAP=0` 可关掉。

规则本体是散文，不是强制闸门。agent 先读代码，列出改动必须波及的每个调用方、测试、fixture 和配置；再取第一个完全可行的选项：不做、复用代码库已有的、标准库或平台特性、已装依赖、一眼能看懂的一行，都不行才写最小可用的代码。明文豁免：信任边界校验、防数据丢失的错误处理、安全、无障碍、用户点名要的东西。新增的非平凡逻辑要留一个小测试或 assert。已知局限的简写要写 `shortcut: <局限>, <何时升级>` 注释；5.1 用这个中性标记换掉了带品牌的 `ponytail:`。每次回复结尾交代跳过了什么、有什么风险。

`/ponytail-debt` 把这些注释收成一本账。它改变 agent 写什么，不拦截 agent 能提交什么。

![ponytail — 主干用户故事](../../../assets/flow/ponytail.zh.svg)

<!-- flow-steps:begin (generated from flows/ponytail.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：添加 ponytail 的插件市场 — `/plugin marketplace add DietrichGebert/ponytail`
2. **你**：再单独发一条 prompt 安装插件 — `/plugin install ponytail@ponytail`
3. **Ponytail**：会话启动时 hook 注入规则和仓库现有代码的简图，子 agent 同样注入 — 组件：`生命周期 hook + 代码地图`
4. **你**：照常提需求，不用改说法 — `Add a date picker to the frontend.`
5. **Ponytail**：先列出改动要波及的调用方、测试和配置，再停在第一级可行的阶梯 — 组件：`最小完整改动`
6. **Ponytail**：交回最小 diff，实质逻辑附测试，结尾交代跳过了什么 — `shortcut: <the limit>, <when to upgrade>`

**价值**：你不用再审任务根本没要的几百行代码：作者用 Opus 5.5 测得代码约少 53%，需要测试的逻辑 98% 带了测试

</details>
<!-- flow-steps:end -->

<!-- flow-steps:begin -->
<!-- flow-steps:end -->

## 何时不用

- **你要的是让 agent 走完整开发流程**（brainstorm → plan → TDD → verify），而不只是少写代码：用 [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) 或 [ECC](../../agent-dev-methodology/coding-agent-harnesses/ecc.zh.md)。Ponytail 不带流程、不带阶段、不带子 agent 流水线，只改「什么算写完」。
- **痛点是 agent 说话啰嗦，不是代码量大**：搭配或改用 [caveman](caveman.zh.md)、[i-have-adhd](i-have-adhd.zh.md)。Ponytail 管的是造什么；作者 6 月的基准里，纯压话术的一路（caveman）只砍了 −20% LOC，功能任务上 token 和成本反而涨了。
- **你会用 hook 插件打开不信任的仓库，或在很慢、很大的文件系统上工作**：设 `PONYTAIL_MAP=0`。5.0 的代码地图把仓库里的名字原样抄进隐藏的会话上下文：精心构造的导出列表或目录名，会被模型当成插件指令读进去；一个指向 `/dev/zero` 的已跟踪软链能让 hook 一直卡到超时（issue #1071）。在慢挂载盘上，地图可能在规则输出前就耗光 SessionStart 的 5 秒超时（#1079）。两者 2026-10-10 时都还 open。
- **你的项目 shell 把 Node 钉在 15 以下**（monorepo 里的旧 `.nvmrc`）：5.1 的 hook 启动命令调用了 `replaceAll`，每次都报错，规则就悄无声息地不再送到模型（#1072，2026-10-10 仍 open）。修好之前改用拷 `AGENTS.md` 的方式。
- **你需要确定性保证虚胖或不安全的代码出不去**：这是注入上下文的说服，遵从度取决于模型。`/ponytail-review` 是你手动调用、由模型执行的审查，不是合并闸门。要带证据的强制把关，在合并前面放一个行级 CI 审查器，如 [Open Code Review](../../ai-code-review/open-code-review.zh.md)。
- **你的宿主或模型不是 Claude Code + Opus**：v5 的数字只来自这一个组合。早先的 README 提醒过，爱权衡的推理模型会花更多 thinking token 逐级掂量阶梯（点名 GPT-5.5）[未验证：作者自述，未复现]。在意成本就先在自己的组合上量一遍，从 `lite` 开始。
- **任务本来就很小**（在现成模板上做 CRUD）：作者的分任务表里，各路在不可再减的代码上收敛（例如 `reuse-money` 三路都是 9 行）。覆盖层在这里收益很小，却每轮都占上下文。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [caveman](caveman.zh.md) | ✅ | 别二选一，配对用：caveman 压 agent 说的话，Ponytail 压 agent 写的代码。只能先修一边就先修代码：两者共享的 6 月基准显示，单压话术砍不动代码，功能任务的 token（+7%）和成本（+3%）还涨了。 | 两个常驻覆盖层叠加，每轮都占上下文。caveman 的可选代理层是 BSL-1.1 source-available，Ponytail 通体 MIT。 |
| [Superpowers](../../agent-dev-methodology/coding-agent-harnesses/superpowers.zh.md) | ✅ | agent 的毛病出在流程（跳过计划、没验证就说做完）选 Superpowers；流程本来就对、毛病只在虚胖选 Ponytail，它减代码，不接管你干活的方式。 | Superpowers 装的是一整套方法论（命令、子 agent、worktree），要整体接受；Ponytail 装的是一条带开关和记分板的行为规则。 |
| [ECC](../../agent-dev-methodology/coding-agent-harnesses/ecc.zh.md) | ✅ | 要一个自带 agents、hooks、memory、安全扫描的 Claude Code 全家桶平台，选 ECC；只想改掉现有工作流里过度工程这一个毛病、且强度可调，选 Ponytail。 | ECC 扩大安装面，集成由你负责；Ponytail 很小，但收益上限就是代码量和成本，没有可砍的地方就没有收益。 |
| 在 AGENTS.md 里手写一句「写一行就行 / YAGNI」 | 非仓库 | 抄一句话零成本，而 v5 的 `AGENTS.md` 本身只有约 30 行，你完全可以自己贴。插件值得装，是因为代码地图、切档、子 agent 注入和 review/audit 命令。6 月基准里裸提示词发挥不稳、是唯一丢护栏的一路；v5 那轮没有设裸提示词对照组。 | 免安装、免 hook、隐藏上下文里没有仓库文本；换来的是插件的便利，但要求 PATH 上有 ≥15 的 `node`，规则有版本管理而不用手维护。 |

## 健康度与可持续性

- **维护**（2026-10-10 经 GitHub API 核实）：最新 release v5.1.0，发布于 2026-10-08。2026-10-02 到 10-08 之间发了 8 个版本，其中 5.0 重写了规则、review 和 audit（PR #1061）。现在 open 的是 17 个 issue、27 个 PR，而 2026-09-28 时有 310 个 open issue：09-28 之后关了 129 个 issue，其中 58 个标为 not planned。这是一次批量清理，所以「17 个 open」更多说明清理过，不太能说明响应快。
- **治理 / bus factor**：个人账号（owner type 为 `User`）。按 contributors API，作者 145 次提交，第二名 12 次。`.github/CONTRIBUTING.md` 设了一道实在的门槛：改规则的 PR 必须附三路基准（无 skill / `main` / 分支），同任务同模型，才会合并；新 skill 只由维护者添加。CI（test.yml、publish.yml）里有脚本保证约 20 份规则拷贝对齐。
- **背书与寿命**：2026-06-12 创建，谈 Lindy 太早。资金来自 GitHub Sponsors 和一个可见赞助商（GreenPT）。README 仍挂着跳往 ponytail.dev 的「Something's coming」waitlist 横幅，现在还多了「Already built with Ponytail」展示位。open-core 或改许可证的风险在观察名单上，尚未发生。`LICENSE` 仍是 MIT。
- **采用与生态**（2026-10-10 取数）：约 15.97 万 star，watcher 只有 365，是出圈的形状。09-28 到 10-10 涨了约 1.2 万 star；同期有 10-05 的西班牙语、韩语、简体中文、日语 README，Kimi Code 适配，以及 10-08 的 Ponytail 5 发布 [推断：只是时间上重合，没核实因果]。可核实的使用量：npm `@dietrichgebert/ponytail` 截至 10-08 的 30 天下载约 9.4 万（一个月前约 5.7 万）。基准 harness 开源（`benchmarks/agentic/`），在 prompt 包里算高于平均；不过 v5 测试数字背后的测试分类和变异工具「还不在仓库里」。
- **风险旗**：最初「少 80–94% 代码」的招牌数字已被承认注水并重测（issue #126）。v5 的招牌数字（代码 −53%、成本 −26%）带置信区间和局限说明，但仍是作者测作者自己的工具。5.0 新增的 hook 会把仓库文本抄进隐藏上下文（#1071），还可能卡住启动（#1079）；5.1 的 hook 在 Node 15 以下崩溃（#1072）；三者 2026-10-10 都还 open。上次核实后已修：OpenCode 2 上静默失效（#863，10-02 关闭，现用 `opencode plugin add`），以及 v4.10.2 让 Codex、VS Code、Qwen 以无 hook 模式加载的回归（v4.11.0 修复）。

## 存疑（未验证）

- [未验证：未独立复现] v5 的全部基准数字都出自作者自建的 harness：LOC −53%、时间 −41%、成本 −26%、输出 token −45%；需要测试的逻辑 98% 带了测试（无 skill 68%）；隐藏检查 87/90 对 86/90。条件是单一宿主（Claude Code）、单一模型（Opus 5.5）、n=5，且禁用了 Bash，agent 从没运行过自己的代码。这些局限基准文档自己列了。
- [未验证：作者自建基准] 盲评裁判（Sonnet 5.5）认为 Ponytail 5 的回复好过 v4.13（110:67），但相对**无 skill** 略偏向后者（82:106，p=0.09）。「结尾交代跳过了什么」这个习惯胜过的是旧版 Ponytail，不是普通 agent。
- [未验证：作者自述] 推理模型（早先 README 点名 GPT-5.5）可能在阶梯上多花 thinking token。v5 的 README 已不再提这一点，也没找到第三方复现。
- [未验证：只读了 issue 里的复现步骤，没在本地跑] 代码地图注入与软链卡死（#1071）、慢文件系统超时（#1079）、Node 15 以下崩溃（#1072）都依据报告者的复现。
- [推断：依据 star/watcher 比和发版时间线] star 增长主要由发版和多语言 README 带动，不是持续使用带来的；npm 下载量是更稳的信号。
- [推断：仅依据 waitlist 横幅和 ponytail.dev 域名] 有商业产品在计划中；目前没有 open-core 限功能或改许可证的证据。
- [未验证：只按 README 徽章和 INSTALL.md 清点，没逐一装测] 「works with 20 agents」的支持面只是文档里写的，没有按宿主逐一核实。
