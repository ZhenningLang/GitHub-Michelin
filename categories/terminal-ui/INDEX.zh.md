# terminal-ui

> 分类节点。终端/CLI UI 库——着色、TUI、ASCII art、终端渲染——以及围着这些工具保活 pane 与 session 的终端复用器（tmux、Zellij）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **colorama** | 当 Python 命令行要让 ANSI 颜色在老式 Windows 控制台上也正确显示、又想几乎零依赖时用它——但它只翻译颜色和样式码，在 Linux、macOS 或 Windows 10+ 上它能做的你自己也能做。 | B（5/6） | [→](colorama.zh.md) |
| **asciimatics** | 当你需要在 Linux／macOS／Windows 上跨平台构建全屏 Python TUI 并附带 ASCII 动画引擎时用它——但它的控件较简陋、API 偏旧式，且为单人维护。 | B（5/6） | [→](asciimatics.zh.md) |
| **Terminal Markdown Viewer (mdv)** | 当你想在 SSH 下的纯终端里一次性渲染一份简单 Markdown（带颜色、表格和代码高亮）时用它——但它自 2023-10 起无人维护，遇到内嵌 HTML 直接失败，glow 或 mdcat 更稳。 | D（3/6） | [→](terminal-markdown-viewer.zh.md) |
| **ART** | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 | B（5/6） | [→](art.zh.md) |
| **asciify** | 当你想花一分钟读懂经典的图片转 ASCII 做法（缩小、转灰度、亮度映射字符梯度），拿来学习或自己重写时用它——但仓库没有许可证、默认保留所有权利，且自 2018-10 起已废弃。 | E（4/6） | [→](asciify.zh.md) |
| **Warp** | 当你想让终端把每条命令的输出切成可选中的块，由内置编码 agent 直接读取并在同一会话里接着干活，而且要在 macOS、Linux、Windows 上用同一个应用时用它——但只有 AGPL 客户端开源，agent、同步和认证都跑在 Warp 的闭源服务器上。 | B（5/6） | [→](warp.zh.md) |
| **Alacritty** | 当你想要一个用显卡渲染、在 macOS、Linux、BSD、Windows 上行为一致的快速终端，并且布局已交给 tmux 或窗口管理器时用它——但它设计上就没有标签页、分屏和连字。 | A（6/6） | [→](alacritty.zh.md) |
| **Rich** | 当 Python 命令行的输出不只要颜色、还要排版（对齐的表格、进度条、代码高亮、好读的报错栈），且想用一个像 `print` 的 API 搞定时用它——但它没有事件循环、做不了交互界面，而且维护如今压在一个人身上。 | B（6/6） | [→](rich.zh.md) |
| **Textual** | 当 Python 命令行工具参数多到失控，大家要在 SSH 上浏览、筛选、操作数据，又不想做网页应用时用它——但 Textualize 公司 2025 年收尾后基本只剩作者一人维护，大版本也换得勤。 | B（6/6） | [→](textual.zh.md) |
| **tmux** | 当 SSH 上的长任务必须比终端活得久、你要的是最小且无处不在的复用器时用它——但它对 pane 里跑什么一无所知，agent 监管得自己搭胶水。 | A（6/6） | [→](tmux.zh.md) |
| **Zellij** | 当你想要自带可发现性的终端复用（模式提示条、鼠标、布局、WASM 插件）外加 token 鉴权 web client 时用它——但它是 pre-1.0、issue 积压大，且 web 接入要做真 TLS 运维。 | A（6/6） | [→](zellij.zh.md) |
| **Pebrel** | 当你在 Windows 上同时跑好几个 AI 编程命令行，想让每个面板自己报告在跑／在等／跑完，并用通知跳回那个面板，同时 SSH/SFTP 也在同一个应用里时用它——但它只有十二周、单人维护，Linux/macOS 仍是 Preview。 | C（5/6） | [→](pebrel.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [colorama](colorama.zh.md) | ✅ | B（5/6） | 换来一个 12 年、无处不在的垫片，一条代码路径到处有颜色；代价是没有表格、排版或 TUI，自 2022 年的 0.4.6 起不再发版，且随老式 Windows 退场而越来越不需要。 |
| [asciimatics](asciimatics.zh.md) | ✅ | B（5/6） | 当你需要在 Linux／macOS／Windows 上跨平台构建全屏 Python TUI 并附带 ASCII 动画引擎时用它——但它的控件较简陋、API 偏旧式，且为单人维护。 |
| [Terminal Markdown Viewer (mdv)](terminal-markdown-viewer.zh.md) | ✅ | D（3/6） | 换来一个 pip 即装、能读 stdin、带主题的 Markdown 转 ANSI；代价是要 Python 运行时、只支持 POSIX、没有分页和搜索，而且作者自称的概念验证不会再有人修。 |
| [ART](art.zh.md) | ✅ | B（5/6） | 当 Python 命令行需要纯 Python 的 figlet 风格 ASCII 文字横幅、且不依赖系统二进制时用它——但它只做文字转艺术字（不做图片转 ASCII），也不与 figlet 字体完全一致。 |
| [asciify](asciify.zh.md) | ✅ | E（4/6） | 换来一个短小易读、整套算法一眼看完的脚本；代价是没有复制它的合法授权、没有彩色或视频输出、也没人维护——要用就自己重写，或改用 ascii-magic。 |
| [Alacritty](alacritty.zh.md) | ✅ | A（6/6） | 十年专注、稳定的渲染速度和极简配置，代价是标签页、分屏、连字和 AI 功能都得交给别的工具。 |
| [Warp](warp.zh.md) | ✅ | B（5/6） | 三大平台通用、原生集成 agent 的终端工作流，代价是依赖一家风投支持厂商的云服务，开源代码库也只有几个月的公开历史。 |
| [tmux](tmux.zh.md) | ✅ | A（6/6） | SSH 长任务要活得比终端久时的最小通用复用器；对 pane 内容无感知，agent 监管自己搭。 |
| [zellij](zellij.zh.md) | ✅ | A（6/6） | 自带提示条、鼠标、布局、WASM 插件与鉴权 web client 的“人本位”复用器；pre-1.0，issue 积压大。 |
| [pebrel](pebrel.zh.md) | ✅ | C（5/6） | 以 Windows 为先的 GPU 终端，给 Claude Code／Codex 装钩子让面板报告 agent 状态，自带 SSH/SFTP；非常年轻、单人维护、GPL-3.0。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

在**终端里渲染 UI** 的库——着色、TUI、ASCII art、样式化输出——以及终端**多路复用器**（管 session/pane 存活的东西，如 tmux、Zellij；感知 agent 的那类，如 [herdr](../agent-frameworks/coding-agents/orchestration-and-review/herdr.zh.md)，归在 `agent-frameworks/coding-agents/orchestration-and-review`）。
