# desktop-automation

> 分类节点。程序化桌面 GUI 自动化（鼠标/键盘/屏幕）。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Cua** | 当 agent 需要操作整台电脑（原生桌面应用、系统弹窗，而非仅网页）、且这次运行需要隔离时使用。 | B（5/6） | [→](cua.zh.md) |
| **PyAutoGUI** | 当你要用 Python 脚本在 Windows、macOS 或 Linux 上点击、输入一个只有图形界面的桌面程序时用它——但基于坐标和像素的自动化会因 DPI、分辨率或主题变化静默失效，必须有真实显示器，且上游自 2023 年起已无新提交。 | C（4/6） | [→](pyautogui.zh.md) |
| **Windows-MCP** | 当 Claude、Codex、Gemini 里的 agent 需要按控件名（UI Automation 树）在原生 Windows 程序里点击、输入，并且直接作用在你的真实会话上时使用——没有沙箱，PowerShell、注册表工具和遥测都默认开启。 | B（6/6） | [→](windows-mcp.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Cua](cua.zh.md) | ✅ | B（5/6） | 当 agent 需要操作整台电脑（原生桌面应用、系统弹窗，而非仅网页）、且这次运行需要隔离时使用。 |
| [PyAutoGUI](pyautogui.zh.md) | ✅ | C（4/6） | 换来十几行就能跑、跨平台的鼠标键盘机器人，不用学 RPA 平台；代价是脆弱、不能无头运行，也读不到无障碍树。 |
| [Windows-MCP](windows-mcp.zh.md) | ✅ | B（6/6） | 换来一行 `uvx` 就能接入、任何 MCP agent 都能用的无障碍树元素标签；代价是只支持 Windows、没有隔离，且项目年轻、基本靠一个维护者。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

**驱动桌面 GUI**（鼠标/键盘/屏幕）的工具。不含网页自动化（见 `web-automation`）。
