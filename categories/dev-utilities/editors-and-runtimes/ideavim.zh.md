---
name: IdeaVim
slug: ideavim
repo: https://github.com/JetBrains/ideavim
category: editors-and-runtimes
tags: [vim, jetbrains, intellij, ide-plugin, editor, keybindings, kotlin]
language: Kotlin
license: MIT
maturity: "2.47.1 (JetBrains Marketplace), very active, ~10.3k stars (as of 2026-09)"
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-27T09:00:40Z
  default_branch: master
  default_branch_sha: 6e47c141de86a69d9c675fea8a4d6aa4dcd5498f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T05:58:42Z
  overall: A
  overall_score: 3.75
  scored_axes: 4
  applicable_axes: 6
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
      grade: "?"
      raw: {}
    longevity:
      grade: A
      raw:
        repo_age_days: 5682
        last_commit_age_days: 2
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 11
        top1_share: 0.474
        top3_share: 0.965
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
    responsiveness: { reason: issues_disabled }
    adoption: { reason: ambiguous }
---

# IdeaVim

JetBrains 系 IDE（IntelliJ IDEA、PyCharm、GoLand、WebStorm、Rider 等）的 Vim 模拟插件——在 IDE 内提供 Vim 的 motion、模式、寄存器、宏，以及 `.ideavimrc`，由 JetBrains 自己维护。

![ideavim — 健康度雷达](../../../assets/health/ideavim.zh.svg)

## 何时使用

你是一个手指被 Vim 写进肌肉记忆的开发者——`hjkl`、`ciw`、`dd`、visual-block、`.` 重复、宏——但团队真正的活在 IntelliJ/PyCharm/GoLand 里，因为那里的重构、调试和语言智能你不肯放弃。在终端里跑真 Vim/Neovim 就丢了 IDE；用 IDE 自带键位就丢了肌肉记忆。你从插件市场装上 IdeaVim，在家目录放一个 `~/.ideavimrc`（你 `.vimrc` 的大部分语法能直接搬过来，甚至可以 `source ~/.vimrc`），编辑器面板就开始像 Vim 一样运转——模式、operator、寄存器、mark、宏——同时 `<Action>(id)` 映射让你把 IDE 动作绑到 Vim 键上（`map <leader>r <Action>(RenameElement)`），`:actionlist` 帮你找到动作 ID，IdeaVim 扩展集（`set surround`、`set multiple-cursors`、easymotion……）复刻你依赖的插件行为。你在同一个工具里同时拿到 Vim 编辑*和* IntelliJ 的语义重构/调试器。

当 IDE 不可妥协（大型 JVM/Kotlin/Go 代码库、重度重构、集成调试器）但你又拒绝像非 Vim 用户那样打字时，你会专门选它。这是 JetBrains 官方背书、最正统的做法。

## 怎么用起来

IdeaVim 是一个用 Kotlin 写的 Vim *引擎*，跑在 IDE 的编辑器组件内部——它并不内嵌一个真正的 Vim 进程。它在编辑器面板里拦截你的按键，运行自己的模式状态机（normal/insert/visual）：你敲下 `ciw`，它把这条 operator 解析出来，直接作用在 IDE 自己的文档模型上——不是缓冲区的副本——所以 IntelliJ 的重构、调试器和索引面对的始终是你正在编辑的同一份文本。归你管的是配置：一个 Vim 语法的 `~/.ideavimrc` 文件、用 `set` 开关点亮内置扩展（surround、multiple-cursors、commentary、easymotion），以及用 `<Action>(ActionId)` 映射从 Vim 键层够到 IDE 功能（README 明确不让你在映射里用 `:action`，`<Action>` 才是受支持的写法）。键位冲突在 IDE 自己的 Vim/Keymap 设置页里解决，`Tools | Vim` 一键关掉整个层、无需重启。

![IdeaVim — 主干用户故事](../../../assets/flow/ideavim.zh.svg)

<!-- flow-steps:begin (generated from flows/ideavim.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：在 IDE 的插件管理里安装 IdeaVim — `Settings | Plugins`
2. **IdeaVim**：Vim 引擎接管编辑器面板的按键处理 — 组件：`Vim 引擎`
3. **你**：把 Vim 风格设置写进 ideavimrc 文件 — `~/.ideavimrc`
4. **你**：用 Action 映射把 IDE 动作绑到 Vim 键上 — `map <leader>r <Action>(RenameElement)`
5. **IdeaVim**：模式与宏作用在 IDE 自己的文档上，重构与调试器照常

**价值**：一个编辑器里同时拥有 Vim 肌肉记忆和 JetBrains 语义工具，随时一键切回

</details>
<!-- flow-steps:end -->

## 何时不用

- **你不在 JetBrains IDE 里。** 它只在 IntelliJ 平台 IDE 内工作。VS Code 用 VSCodeVim/Neovim 扩展；终端用真 Vim/Neovim。宿主选错＝工具选错。
- **你要 100% 的 Vim/Neovim 保真或你完整的插件生态。** 它是对一个大子集的*模拟*，不是 Vim 本身——一些冷门命令、边界行为，以及整个原生 Vimscript/Lua 插件宇宙都不在（IdeaVim 有自己更小的扩展集）。重度用户会撞到缺口。[未验证]
- **你想在 IDE 里用 Neovim 的 Lua 配置 / LSP / treesitter。** IdeaVim 读 `.ideavimrc`，不是你的 Neovim Lua 配置；语言智能由 IDE 提供，而非 Neovim 那套栈。
- **极简 / 轻键位编辑。** 如果你本来就不用 Vim 思维，给 IDE 叠一层模态编辑是摩擦而非提速——要么刻意学，要么跳过。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| VSCodeVim | 未收录 | 编辑器是 VS Code 且只需要 Vim 模拟时，选 VSCodeVim。 | VS Code 的 Vim 模拟；同样的点子换个宿主——按你实际用哪个 IDE 来选，而非按插件。 |
| vscode-neovim | 未收录 | 需要在 VS Code 内嵌入一个*真* Neovim 实例时，选 vscode-neovim。 | 在 VS Code 内嵌入一个*真* Neovim 实例，保真更高＋可用你的 Neovim 配置；更重且仅限 VS Code，JetBrains 侧没有这种深度的对应物。 |
| 真 Vim / Neovim | 未收录 | 需要完整插件生态与 Lua/LSP，而不是 IDE 集成时，选真 Vim 或 Neovim。 | 货真价实，拥有完整插件生态与 Lua/LSP；但你会失去 JetBrains 的集成重构/调试器/索引。 |
| JetBrains 自带键位 | 未收录 | 需要没有模拟层、完全受支持的设置时，选 JetBrains 自带键位。 | 没有模拟层、完全受支持；但没有 Vim 模式/motion——对 Vim 用户而言失去意义。 |

## 技术栈

- **语言：** Kotlin（JetBrains 自家语言；插件跑在 IntelliJ 平台 / JVM 上）。
- **宿主：** IntelliJ 平台插件 API——它挂接任何基于 IntelliJ 的 IDE 的编辑器组件。
- **配置：** 一个用 Vim 风格命令/映射写的 `~/.ideavimrc`，加上 `<Action>(ActionId)` 映射来调用 IDE 动作（按当前 README 的指引；`:action` 用于一次性调用而非映射），以及一组 IdeaVim 扩展插件。
- **分发：** JetBrains Marketplace（并在 IntelliJ 平台 IDE 中内置/可安装）。

## 依赖

- **运行时：** 一个兼容版本的 JetBrains IntelliJ 平台 IDE（IntelliJ IDEA、PyCharm、GoLand、WebStorm、Rider、CLion 等）——这个 IDE *就是*它要插入的平台。
- **无外部服务 / 数据存储**——它是 IDE 内插件；配置是本地文件。
- **可选：** 一并安装的 IdeaVim 扩展插件（surround、sneak 等）。

## 运维难度

**极低。** 从插件市场安装，可选写一个 `.ideavimrc`，打开开关即可。没有任何东西要部署或运维——它完全活在你本就在跑的 IDE 里。唯一的「难度」是配置口味（移植 `.vimrc` 习惯、映射 IDE 动作），以及偶尔的 IDE 版本兼容性升级——而这由 JetBrains 自己紧盯，因为是他们出品。

## 健康度与可持续性

- **响应速度**：无法计算——GitHub issues 已关闭，追踪器是 JetBrains YouTrack（`VIM` 项目），健康度评分器读不到它。这是测量盲区，不是无人维护的信号。
- **维护（2026-09）。** 非常活跃——最后 push 2026-09-27，提交频繁，由一个 JetBrains 小团队（AlexPl292 等）领衔、提交上千。Marketplace 当前构建 2.47.1（plugins.jetbrains.com API，2026-09-28）。通过 Marketplace 分发而非 GitHub Releases，所以 GitHub 上「无 release」是正常现象，并非停滞信号。未归档。[推断：Marketplace 版本与仓库提交节奏的对应关系未逐一核对]
- **治理 / 背书。** 由 **JetBrains**（一个组织，也就是 IDE 厂商本身）拥有并维护——第一方、资金充足的治理，且有直接动机让它在历次 IDE 发布间保持可用。在 IDE 插件里属于最强的背书画像之一。[推断]
- **年龄与 Lindy。** 2011 年创建，约 15 岁且**仍在活跃发布**⇒ **强 Lindy** 信号——它跨越 IntelliJ 平台多个大版本一路跟随，至今仍是 JetBrains 的默认 Vim 层。[推断]
- **采用度。** 约 10.3k GitHub star（API，2026-09-28），且 JetBrains Marketplace API 对插件 164 报出 **2210 万下载量**（2026-09-28）——对一个 IDE 插件来说，包索引数字比 star 更诚实；它是大多数 JetBrains-Vim 用户配置的标配。健康度评分器仍把 adoption 记为 `?`，因为它无法把 Marketplace 制品对应到包注册表。[推断：下载数计的是安装面而非活跃用户]
- **风险标记。** 很少——宽松 MIT、第一方厂商背书。结构性天花板是内在的：它是绑定 IntelliJ 平台的*模拟*，所以保真缺口与平台版本耦合才是真实（且有界）的风险，而非项目废弃。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-09-28 约 10.3k GitHub star（API 核对）；star 数对时间敏感，仅供参考。
- [未验证] Marketplace 对插件 164 报出 2210 万下载（API，2026-09-28）；这是累计安装量而非活跃用户数，且具体的发布/版本节奏与 IDE 兼容范围在 Marketplace 上，这里未逐一列出。
- [未验证] 支持的 Vim 特性集与缺口（以及 IdeaVim 扩展目录）随版本变动；请对照当前文档核实你依赖的具体命令/插件。
- [推断]「第一方、资金充足」是从 JetBrains 所有权推断；具体投入 IdeaVim 的人力/资金未明示。
- [推断] 与任一 IDE 版本的兼容由插件声明的平台范围决定且随时间变化，这里不断言具体矩阵。
