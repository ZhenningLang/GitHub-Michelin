---
name: colorama
slug: colorama
repo: https://github.com/tartley/colorama
category: terminal-ui
tags: [terminal, ansi, colors, cross-platform, windows, python, cli]
language: Python
license: BSD-3-Clause
maturity: stable, active, ~3.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-05-13T18:21:46Z
  default_branch: master
  default_branch_sha: 841634ed2a0da5d5ac2d867db533da8131266cb2
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T17:06:59Z
  overall: B
  overall_score: 3.0
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 132
        active_weeks_13: 0
        carve_out: mature_library_lindy
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: colorama
        dependent_repos_count: 189970
        downloads_last_month: 250511955
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        tier_source: registry
    longevity:
      grade: B
      raw:
        repo_age_days: 4541
        last_commit_age_days: 132
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 1
        top1_share: 1.0
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-3-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# colorama

一个极小的纯 Python 库，让 ANSI 颜色/样式转义码在 Windows 上也能工作——调一次 `colorama.init()`，那些在 Linux/macOS 上给你输出着色的同一套 ANSI 序列，如今在老式 Windows 终端里也能正确渲染。

![colorama — 健康度雷达](../../assets/health/colorama.zh.svg)

## 何时使用

你在写一个 Python CLI——构建工具、测试 runner、部署脚本——想要红色的错误、绿色的成功、暗淡的次要文字。在 Linux 和 macOS 上你直接打印 ANSI 转义码（`\033[31m...`）。但你在老 Windows（cmd.exe、现代版之前的 conhost）上的用户看到的是 `←[31m` 这类乱码而非颜色，因为那些终端不解释 ANSI。你在启动处加上 `from colorama import init, Fore, Style; init()`,colorama 就在 Windows 上拦截 stdout/stderr，把 ANSI 码翻译成真正设置颜色的 Win32 控制台 API 调用——而在已经支持 ANSI 的平台上什么都不做（把 ANSI 原样透传）。结果是：一条代码路径、到处都是带色输出，不用 `if platform == 'windows'` 分支。它的 `Fore`、`Back`、`Style` 常量也给你可读的名字，而非裸的转义数字。

它是一大片 Python CLI 底下事实上的兼容垫片，也被许多更高层的颜色/UI 库打包进去——当你需要*跨平台带色终端文字*、又想要近乎零依赖时选它，而不是要一套完整 TUI。

## 何时不用

- **你只面向 Linux/macOS（或现代 Windows Terminal）。** 在已经认 ANSI 的平台上——包括开了 VT 处理的 Windows 10+ Terminal/conhost——colorama 基本是空操作；你不用它也能打印转义码（或用更轻的助手）。它的核心价值是*老式 Windows*。[推断]
- **你想要富终端 UI——表格、布局、进度条、markdown。** colorama 只翻译颜色/样式码。要带样式的表格、spinner、实时布局、语法高亮，请找 **Rich**（一个大得多的库），或要完整 TUI 找 **Textual**。
- **你想要高层的样式人体工学。** colorama 给你的是偏裸的 `Fore.RED + text + Style.RESET_ALL`；像 **Rich** 或 **click.style** 这类库 API 更好。colorama 是底层垫片，常常在*它们底下*。
- **非 Python 技术栈。** 它只面向 Python；别的生态有各自的（Node 的 chalk 等）。
- **你需要处处保证 24 位 truecolor。** colorama 聚焦标准 ANSI SGR 码和 Windows 控制台翻译；truecolor 支持取决于终端，colorama 不是保证它的那一层。[未验证]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Rich（Textualize）](rich.zh.md) | ✅ | 需要颜色、表格、Markdown、进度和 traceback 等完整带样式输出工具包时，选 Rich。 | 完整的带样式输出工具包（颜色、表格、markdown、进度、traceback）——能力强太多，但是个大库；只要跨平台颜色就是杀鸡用牛刀。 |
| termcolor / colored | 未收录 | 需要极小、API 友好的 ANSI 颜色助手，且不需要老式 Windows ANSI 翻译时，选 termcolor / colored。 | 极小的 ANSI 颜色助手，API 友好，但不在老式 Windows 上翻译 ANSI——常和 colorama *搭配*以补这点。 |
| click.style（Click） | 未收录 | 需要 Click CLI 框架内方便的样式能力时，选 click.style。 | Click CLI 框架内方便的样式；Click 自身历史上为 Windows 垫片依赖 colorama。 |
| blessed / blessings | 未收录 | 需要基于 terminfo 的终端能力、光标和样式控制时，选 blessed / blessings。 | 终端能力 + 光标/样式库（基于 terminfo）——终端控制更丰富、更重，对 Windows-ANSI 缺口不那么聚焦。 |
| 裸 ANSI 转义码 | 未收录 | 想要零依赖且只面向支持 ANSI 的终端时，选裸 ANSI 转义码。 | 零依赖，在每个支持 ANSI 的终端都能用，但在老式 Windows 控制台上崩——正是 colorama 补的缺口。 |

## 技术栈

- **语言：** 纯 Python，无编译扩展。
- **机制：** 包住 `sys.stdout`/`sys.stderr`，在 Windows 上解析 ANSI SGR 序列并经 **Win32 控制台 API**（SetConsoleTextAttribute 等）重放；在别的平台上是透传。
- **API：** `init()`/`deinit()`/`just_fix_windows_console()`，加上 `Fore`、`Back`、`Style` 常量命名空间和 `AnsiToWin32` 内部实现。

## 依赖

- **运行时：** 只要 Python——**无第三方运行时依赖**（它用 ctypes/标准库调 Windows 控制台 API）。这种零依赖足迹正是它被如此广泛打包的一大原因。[推断]
- **外部服务：** 没有。
- **安装：** `pip install colorama`。

## 运维难度

**微不足道。** 一句 `pip install` 加一次 `init()` 调用（或 `just_fix_windows_console()`）；没有要部署、配置或运维的东西。唯一实际要在意的是早点调 `init()`、记得 `Style.RESET_ALL` 以免颜色串色，并知道它在已支持 ANSI 的终端上基本是空操作——所以别指望它加上它本就不打算提供的能力（truecolor、TUI）。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 仓库最后 push 于 2026-05——**活跃**，未归档；一个稳定成熟、不需频繁改动但保持更新的库。（这里没列 GitHub tag 发布；它经 **PyPI** 发布。）[未验证]
- **治理 / bus factor。** owner 类型 **User**（tartley / Jonathan Hartley），有多位稳定贡献者（wiggin15、hugovk、njsmith、jdufresne）——bus factor 好于单人脚本，但仍是个人所有而非基金会背书。[推断]
- **年龄与 Lindy 判断。** **2014** 年创建，约 12 岁且**仍在维护**⇒ **强 Lindy** 信号；它是个安定、无处不在的依赖，它要解决的问题（老式 Windows 的 ANSI）本身也很稳定。[推断]
- **采用度。** 约 3.8k star，但真正的信号是**传递式无处不在**——它是海量 Python CLI 和颜色/UI 库的依赖（历史上 pip、Click、pytest 相关工具等都打包或依赖它）。[未验证]
- **风险标记。** **BSD-3-Clause**，宽松，未发现 relicense 历史。随着老式 Windows 退场（Windows Terminal 原生支持 ANSI），这个库的*相关性*在缓慢收窄，但它仍是求广泛兼容的安全默认。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 3.8k star / 约 279 fork / 约 137 open issue——对时间敏感，仅供参考。
- [未验证] 经 PyPI 发布；空的 GitHub Releases 列表不代表不活跃——在 PyPI/changelog 上核实当前版本。
- [推断] 「零第三方运行时依赖」是依其设计/足迹推断；若涉及关键决策请对照版本元数据确认。
- [推断] 在现代支持 ANSI 的终端上 colorama 基本是透传；「那里是空操作」是对行为的推断，并非对每个终端/版本的保证。
- [未验证] 跨终端的 truecolor（24 位）行为在 colorama 的保证范围之外，这里未经核实。
