# agent-browser-tools

> 分类节点。面向 agent 的浏览器 / computer-use 接口——MCP server、CLI+SKILLs、页内 agent，以及已登录会话桥接。
> ← 返回[web-automation](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Agent Browser** | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 | B（6/6） | [→](agent-browser.zh.md) |
| **browser-use** | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | B（6/6） | [→](browser-use.zh.md) |
| **BrowserSkill** | 当 agent 必须在不动你现有窗口的前提下操作你已登录的 Chromium 时用它——借你的页签要先经你确认，遇到登录或验证码把控制权交还给你。 | B（6/6） | [→](browserskill.zh.md) |
| **Chrome DevTools MCP** | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 | A（6/6） | [→](chrome-devtools-mcp.zh.md) |
| **Cua** | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 | B（6/6） | [→](cua.zh.md) |
| **OpenCLI** | 当 agent 必须操作藏在你登录态后面的站点时用它——经扩展+daemon 桥接你已登录的 Chrome，并把站点工作流固化成可复用 CLI 命令；要预期适配器 churn 和真实的信任面。 | B（6/6） | [→](opencli.zh.md) |
| **page-agent** | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 | B（6/6） | [→](page-agent.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Agent Browser](agent-browser.zh.md) | ✅ | B（6/6） | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 |
| [browser-use](browser-use.zh.md) | ✅ | B（6/6） | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. |
| [BrowserSkill](browserskill.zh.md) | ✅ | B（6/6） | 让任何能调 shell 的 agent 桥接你已登录的 Chromium，不干扰你自己的窗口，遇到只能人做的步骤交还给你；信任面与 OpenCLI 同级，但没有它的确定性站点适配器。 |
| [Chrome DevTools MCP](chrome-devtools-mcp.zh.md) | ✅ | A（6/6） | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 |
| [Cua](cua.zh.md) | ✅ | B（6/6） | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 |
| [OpenCLI](opencli.zh.md) | ✅ | B（6/6） | 桥接你已登录的 Chrome，agent 完全不碰登录流程，另有可复用站点适配器；仅 Chromium、适配器 churn 是结构性的，扩展+daemon 继承你全部会话。 |
| [page-agent](page-agent.zh.md) | ✅ | B（6/6） | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 |

## 什么该放这里

为 agent 回路而非固定测试代码而建的接口：协议 server 与 CLI、视觉/自然语言 agent，以及桥进真实登录态浏览器的方案。
