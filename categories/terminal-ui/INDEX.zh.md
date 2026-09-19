# terminal-ui

> 分类节点。终端/CLI UI 库——着色、TUI、ASCII art、终端渲染。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **colorama** | 当 Python 命令行需要在旧版 Windows 控制台也能正确显示 ANSI 彩色输出时用它——但它只是颜色／样式适配层（不提供表格、TUI 或真彩保证），在现代终端上基本是空操作。 | B（5/6） | [→](colorama.zh.md) |
| **asciimatics** | 当你需要在 Linux／macOS／Windows 上跨平台构建全屏 Python TUI 并附带 ASCII 动画引擎时用它——但它的控件较简陋、API 偏旧式，且为单人维护。 | C（4/6） | [→](asciimatics.zh.md) |
| **Terminal Markdown Viewer (mdv)** | 当你想在 SSH 下的纯终端里一次性、只读地渲染带彩色与语法高亮的 Markdown 时用它——但它活跃度低（0.x，2024 年 5 月），glow／mdcat 已是更现代的默认选择。 | "?"（2/6） | [→](terminal-markdown-viewer.zh.md) |
| **ART** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | C（4/6） | [→](art.zh.md) |
| **asciify** | 当你只想要一份极简易读、可复制粘贴的图片转 ASCII 算法参考时用它——但它没有任何许可证（默认保留所有权利），自 2022 年起无人维护，切勿将其并入产品。 | E（4/6） | [→](asciify.zh.md) |
| **Warp** | 当你想要一个带命令块和集成编码 agent 的现代 AI 终端时用它——但这个 GitHub 仓库仅用于 issue，产品是专有闭源软件。 | B（6/6） | [→](warp.zh.md) |
| **Alacritty** | 当你想要一个快速、GPU 加速、跨平台的终端模拟器，具备合理的默认设置时用它——但它明确不支持标签页、分屏和连字，且需要 OpenGL 3.3+。 | A（6/6） | [→](alacritty.zh.md) |
| **Rich** | Rich is a Python library for rich text and beautiful formatting in the terminal. | B（6/6） | [→](rich.zh.md) |
| **Textual** | The lean application framework for Python.  Build sophisticated user interfaces with a simple Python API. Run your apps in the terminal and a web browser. | A（6/6） | [→](textual.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [colorama](colorama.zh.md) | ✅ | B（5/6） | 当 Python 命令行需要在旧版 Windows 控制台也能正确显示 ANSI 彩色输出时用它——但它只是颜色／样式适配层（不提供表格、TUI 或真彩保证），在现代终端上基本是空操作。 |
| [asciimatics](asciimatics.zh.md) | ✅ | C（4/6） | 当你需要在 Linux／macOS／Windows 上跨平台构建全屏 Python TUI 并附带 ASCII 动画引擎时用它——但它的控件较简陋、API 偏旧式，且为单人维护。 |
| [Terminal Markdown Viewer (mdv)](terminal-markdown-viewer.zh.md) | ✅ | "?"（2/6） | 当你想在 SSH 下的纯终端里一次性、只读地渲染带彩色与语法高亮的 Markdown 时用它——但它活跃度低（0.x，2024 年 5 月），glow／mdcat 已是更现代的默认选择。 |
| [ART](art.zh.md) | ✅ | C（4/6） | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 |
| [asciify](asciify.zh.md) | ✅ | E（4/6） | 当你只想要一份极简易读、可复制粘贴的图片转 ASCII 算法参考时用它——但它没有任何许可证（默认保留所有权利），自 2022 年起无人维护，切勿将其并入产品。 |
| [Alacritty](alacritty.zh.md) | ✅ | A（6/6） | 快速、GPU 加速的 OpenGL 终端模拟器，具备合理的默认设置；设计上不支持标签页、分屏和连字——复用请配合 tmux。 |
| [Warp](warp.zh.md) | ✅ | B（6/6） | 带命令块和编码 agent 的现代 AI 终端；GitHub 仓库仅用于 issue，产品为专有闭源软件。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

在**终端里渲染 UI** 的库——着色、TUI、ASCII art、样式化输出。
