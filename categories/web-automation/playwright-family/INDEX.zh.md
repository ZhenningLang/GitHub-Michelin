# playwright-family

> 分类节点。微软的 Playwright 栈——测试/自动化框架本体，外加面向 agent 的 CLI+SKILLs 与 MCP 两个接口。
> ← 返回[web-automation](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Playwright** | Playwright is a framework for Web Testing and Automation. It allows testing Chromium, Firefox and WebKit with a single API. | A（5/6） | [→](playwright.zh.md) |
| **Playwright CLI** | 当 coding agent（Claude Code、Copilot）需要便宜、token 高效的浏览器命令并装好 SKILLs 时用它——微软自己推荐给 coding agent 的路径；v0.1.x，刚重新定位。 | A（5/6） | [→](playwright-cli.zh.md) |
| **Playwright MCP** | 当支持 MCP 的 agent 需要厂商官方、基于无障碍树快照的确定性浏览器自动化时用它——适合有状态的探索式回路；微软自家 README 把高吞吐 coding agent 引向它的 CLI 兄弟。 | A（6/6） | [→](playwright-mcp.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Playwright](playwright.zh.md) | ✅ | A（5/6） | 带完整 runner 与 trace 能力的跨浏览器测试和自动化；当前索引条目仍需要补齐选型边界。 |
| [Playwright CLI](playwright-cli.zh.md) | ✅ | A（5/6） | 微软面向 coding agent 的 token 高效 CLI+SKILLs 路径；v0.1.x 且刚重新定位，预期契约会 churn。 |
| [Playwright MCP](playwright-mcp.zh.md) | ✅ | A（6/6） | 微软官方 MCP 浏览器：AX 树快照、跨浏览器、客户端兼容最广；比微软自己引导 coding agent 使用的 CLI 兄弟更费 token。 |

## 什么该放这里

你写测试代码所针对的框架，以及微软在同一引擎上维护的两个面向 agent 的前端。
