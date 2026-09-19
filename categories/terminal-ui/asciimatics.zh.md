---
name: asciimatics
slug: asciimatics
repo: https://github.com/peterbrittain/asciimatics
category: terminal-ui
tags: [terminal-ui, tui, curses, ascii-art, animation, cross-platform, python, widgets]
language: Python
license: Apache-2.0
maturity: v1.15.x, active (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2025-06-03T21:42:03Z
  default_branch: master
  default_branch_sha: 0a400e6c6c52cb7f4ba15ffaaa55b535d0d1b2b1
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T08:19:27Z
  overall: C
  overall_score: 2.0
  scored_axes: 4
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: D
      raw:
        archived: false
        last_commit_age_days: 398
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: asciimatics
        dependent_repos_count: 176
        downloads_last_month: 82881
        graph_tier: C
        volume_tier: C
        cross_check_divergence: null
    longevity:
      grade: D
      raw:
        repo_age_days: 4097
        last_commit_age_days: 398
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# asciimatics

一个跨平台的 Python 全屏文本 UI 库——一套类 curses 的 API，外加一层 widget/表单工具集和一个 ASCII 动画/特效引擎，在 Linux、macOS 和 Windows 上表现一致。

![asciimatics — 健康度雷达](../../assets/health/asciimatics.zh.svg)

## 何时使用

你是 Python 开发者，需要一个真正的全屏终端界面——交互式表单、仪表盘、向导——而且希望它在同事的 Windows 笔记本、你的 Mac 和 Linux CI 机器上行为一模一样。标准库的 `curses` 只能在 Unix 上用，且出了名地难伺候，你也不想为此写两套代码路径。于是你引入 asciimatics：它给你一个 `Screen` 抽象，统一处理彩色/带样式文本（含 256 色和 CJK unicode）、光标定位、非阻塞键鼠输入，以及控制台 resize 检测，三个平台一致。在此之上它还带一层 `Frame`/widget——文本框、列表、按钮、布局——让你不用手搓事件循环就能拼出一个表单驱动的 TUI。

当你想要那层*好玩*的能力时，你也会选它：滚动横幅、精灵、粒子特效、生命游戏、场景间转场。asciimatics 最初就是个动画工具集（名字本身就是双关），所以如果你在做启动画面、复古 demo、ASCII 艺术开场或教学可视化，它的 `Effect`/`Scene`/`Renderer` 模型就是为此而生。无论你要的是严肃的数据录入屏，还是滚动片尾，用的都是同一个库。

## 何时不用

- **你只面向 Linux/macOS 且想要最大控制力。** 如果跨平台不是硬需求，原生 `curses` 或更底层的绑定没有额外依赖、控制更细——asciimatics 的抽象是一层你未必需要的便利层。
- **你想要现代、响应式、样式丰富的 TUI 框架。** Textual（CSS 式样式、异步、鼠标优先 widget）或 `urwid` 面向更丰富的应用 UI；asciimatics 的 widget 集能用但偏简朴，API 风格也偏老。做大型应用前请先对比。
- **你只想要漂亮的静态输出、表格、进度条或标记。** `rich` 更适合带样式的非全屏输出——asciimatics 会接管整个屏幕，给日志上色或画进度条属于杀鸡用牛刀。
- **你只需要 ASCII 艺术字横幅或图片转 ASCII。** 用更聚焦的库（[art](art.zh.md) 做 figlet 风格文字，图片转 ASCII 用专门转换器）；asciimatics 是 UI/动画引擎，不是字体/艺术生成器。
- **你在意单一维护者风险。** 开发主要由一位作者推动；对一个长期生产依赖来说，请权衡 bus-factor（见健康度）。[推断]

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Textual](textual.zh.md) | ✅ | 需要现代异步、CSS 样式、鼠标优先的 TUI 框架时，选 Textual。 | 现代异步、CSS 样式、鼠标优先的 TUI 框架（Textualize）；widget/样式模型丰富得多、背书活跃，但更重，编程模型也与 asciimatics 类 curses 的 API 不同。 |
| urwid | 未收录 | 需要老牌 Python 控制台 UI 库和灵活 widget/布局系统时，选 urwid。 | 老牌 Python 控制台 UI 库，widget/布局系统灵活；偏 Unix（Windows 支持弱），且无动画引擎。 |
| [rich](rich.zh.md) | ✅ | 需要表格、标记、进度、语法高亮等带样式终端*输出*时，选 rich。 | 带样式的终端*输出*（表格、标记、进度、语法）——不是全屏 UI/事件循环；与之互补，不能替代交互屏。 |
| blessed / curses（标准库） | 未收录 | 需要更底层的终端控制，而不是 widget/动画框架时，选 blessed 或 curses。 | 更底层的终端控制；`curses` 仅 Unix，`blessed` 是更友好的封装——两者都不带 widget 或动画框架。 |
| prompt_toolkit | 未收录 | 需要强交互提示、REPL 或输入密集型全屏应用时，选 prompt_toolkit。 | 擅长交互式提示/REPL 和部分全屏应用，行编辑很强，但侧重点不同（输入），也没有 ASCII 特效引擎。 |

## 技术栈

- **语言：** 纯 Python（支持当前 CPython 版本；具体最低版本请对照仓库的 `setup`/`pyproject` 核实）。[未验证]
- **核心抽象：** 一个 `Screen` 类封装各平台终端后端——Unix-like 上用 `curses`、Windows 上用原生 console API——对外呈现统一的跨平台界面。
- **widget 层：** `Frame`、`Layout` 及各 widget（文本、列表、按钮等），其上叠加场景/特效模型。
- **动画引擎：** `Scene` / `Effect` / `Renderer` 原语，用于精灵、粒子、转场和 ASCII 艺术渲染。

## 依赖

- **运行时：** Python 加一小撮 pip 依赖（如某个 Windows console 绑定、`wcwidth` 之类）；`pip install asciimatics` 即可。确切依赖清单见打包元数据。[未验证]
- **平台：** 一个终端/控制台；Windows 上用原生 console API，而非要求 Unix 的 `curses`。
- **无外部服务或数据存储**——它是进程内 UI 库。

## 运维难度

**低。** 它是库不是服务——没有要部署或运维的东西。负担纯在开发期：它会接管整个终端，所以你要围绕它的事件循环和场景模型来设计，并在你实际面向的终端上测试渲染（各模拟器的彩色支持、resize 行为、CJK/unicode 宽度处理都不同）。无数据存储、无网络、无运行时基础设施。

## 健康度与可持续性

- **响应速度**：无法计算——no_traffic。
- **维护（2026-06）。** 最后 push 于 2025-06；提交仍在持续但节奏不快。版本有打 tag（1.15.x 线）。读作**有维护但推进缓慢**，并非废弃——未归档。[推断]
- **治理 / bus factor。** 单一维护者项目（Peter Brittain），托管在个人账号下，外加一条偶发贡献者的长尾；路线图很大程度取决于一个人。这是长期依赖的主要治理风险。[推断]
- **年龄与 Lindy 判断。** 约 11 年（2015-04 创建）且仍在收到提交⇒ **强 Lindy** 信号：一个成熟稳定、早已定型的库，而非被炒作的新秀。[推断]
- **采用度。** 约 4.3k star，作为 Python 跨平台 TUI/动画的首选库被广泛使用；文档完善、示例齐全。[未验证]
- **风险标记。** Apache-2.0（宽松，未发现 relicense 历史）；现实风险在维护速度/bus-factor，而非许可。[推断]

## 存疑（未验证）

- [未验证] 截至 2026-06 约 4.3k GitHub star、1.15.x 发布线；star 数和版本号会漂移——仅供参考。
- [未验证] 确切的 Python 最低版本和精确的运行时依赖清单由仓库打包元数据决定且随版本变化，这里不断言具体数值。
- [推断] “有维护但推进缓慢”是从 2025-06 的最后 push 和不快的提交节奏推断，而非实测的发布频率数字。
- [推断] 单一维护者/bus-factor 的判断是从贡献者分布和个人账号归属推断，而非来自某份治理文档。
- [推断] Textual/urwid“更丰富”是对其特性集的概括，而非对 asciimatics 逐项功能审计。
