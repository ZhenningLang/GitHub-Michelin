# web-automation

> 分类节点。驱动或自动化 Web 界面——浏览器自动化，或页内自然语言 GUI agent。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **page-agent** | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 | B（6/6） | [→](page-agent.zh.md) |
| **Chrome DevTools MCP** | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 | A（6/6） | [→](chrome-devtools-mcp.zh.md) |
| **Cua** | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 | B（6/6） | [→](cua.zh.md) |
| **Agent Browser** | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 | B（6/6） | [→](agent-browser.zh.md) |
| **Selenium** | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 | B（6/6） | [→](selenium.zh.md) |
| **PhantomJS** | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 | D（5/6） | [→](phantomjs.zh.md) |
| **Selenium Wire** | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 | D（5/6） | [→](selenium-wire.zh.md) |
| **browser-use** | 🌐 Make websites accessible for AI agents. Automate tasks online with ease. | ?（0/6） | [→](browser-use.zh.md) |
| **Playwright** | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. | ?（0/6） | [→](playwright.zh.md) |
| **Puppeteer** | JavaScript API for Chrome and Firefox | ?（0/6） | [→](puppeteer.zh.md) |
| **nodriver** | 当你需要 Python-first 的异步直接 CDP 控制、且不想依赖 WebDriver 时用它；它仅支持 Chromium、采用 AGPL-3.0，反检测也只是尽力而为，不是稳定绕过契约。 | C（5/6） | [→](nodriver.zh.md) |
| **Playwright MCP** | 当支持 MCP 的 agent 需要厂商官方、基于无障碍树快照的确定性浏览器自动化时用它——适合有状态的探索式回路；微软自家 README 把高吞吐 coding agent 引向它的 CLI 兄弟。 | A（6/6） | [→](playwright-mcp.zh.md) |
| **Playwright CLI** | 当 coding agent（Claude Code、Copilot）需要便宜、token 高效的浏览器命令并装好 SKILLs 时用它——微软自己推荐给 coding agent 的路径；v0.1.x，刚重新定位。 | A（5/6） | [→](playwright-cli.zh.md) |
| **OpenCLI** | 当 agent 必须操作藏在你登录态后面的站点时用它——经扩展+daemon 桥接你已登录的 Chrome，并把站点工作流固化成可复用 CLI 命令；要预期适配器 churn 和真实的信任面。 | B（6/6） | [→](opencli.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [page-agent](page-agent.zh.md) | ✅ | B（6/6） | 想在页内用自然语言、通过直接读写 DOM 控制 Web 界面、且无需后端时用它。 |
| [Chrome DevTools MCP](chrome-devtools-mcp.zh.md) | ✅ | A（6/6） | 当 agent 需要驱动并用 DevTools 检查真实 Chrome（性能 trace、网络、控制台、堆内存）时使用。 |
| [Cua](cua.zh.md) | ✅ | B（6/6） | 当 agent 需要在隔离 VM 沙箱里用视觉操作整台桌面系统（而非仅网页）时使用。 |
| [Agent Browser](agent-browser.zh.md) | ✅ | B（6/6） | 当 agent 需要靠 shell 命令通过 CDP 驱动真实 Chrome、用稳定元素引用而非 CSS 选择器操作网页时使用。 |
| [Selenium](selenium.zh.md) | ✅ | B（6/6） | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 |
| [PhantomJS](phantomjs.zh.md) | ✅ | D（5/6） | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 |
| [Selenium Wire](selenium-wire.zh.md) | ✅ | D（5/6） | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 |
| [Playwright](playwright.zh.md) | ✅ | ?（0/6） | 带完整 runner 与 trace 能力的跨浏览器测试和自动化；当前索引条目仍需要补齐选型边界。 |
| [Puppeteer](puppeteer.zh.md) | ✅ | ?（0/6） | Chrome-first 的 JavaScript 自动化；当前索引条目仍需要补齐选型边界。 |
| [nodriver](nodriver.zh.md) | ✅ | C（5/6） | 不依赖 WebDriver 的 Python 异步直接 CDP 控制，代价是没有跨浏览器覆盖、许可不宽松，反检测也仅为尽力而为。 |
| [Playwright MCP](playwright-mcp.zh.md) | ✅ | A（6/6） | 微软官方 MCP 浏览器：AX 树快照、跨浏览器、客户端兼容最广；比微软自己引导 coding agent 使用的 CLI 兄弟更费 token。 |
| [Playwright CLI](playwright-cli.zh.md) | ✅ | A（5/6） | 微软面向 coding agent 的 token 高效 CLI+SKILLs 路径；v0.1.x 且刚重新定位，预期契约会 churn。 |
| [OpenCLI](opencli.zh.md) | ✅ | B（6/6） | 桥接你已登录的 Chrome，agent 完全不碰登录流程，另有可复用站点适配器；仅 Chromium、适配器 churn 是结构性的，扩展+daemon 继承你全部会话。 |
| undetected-chromedriver / SeleniumBase | 未收录 | — | nodriver 页面提到的 Selenium 兼容 stealth 工具与开箱即用 Python 浏览器测试框架。 |

## 什么该放这里

**驱动或自动化 Web/浏览器（乃至计算机）GUI** 的工具——headless 浏览器自动化、computer-use，或页内 GUI agent。不含服务端爬虫框架，不含企业级纯桌面 RPA。
