# stealth-session-tools

> 分类节点。面向 agent 的隐身浏览器工具，选型卡点是会话被自动化检测或浏览器指纹拦截。
> ← 返回 [agent-browser-tools](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **invisible_playwright_mcp** | 当 MCP 助手总被验证码和机器人墙拦住时用它——它驱动一个 C++ 层打过补丁、指纹由种子推导的隐身 Firefox；只支持 Windows/Linux，单人维护，星数继承自改名前的投简历机器人仓库。 | B（5/6） | [→](invisible-playwright-mcp.zh.md) |
| **playwright-bot-bypass** | 当编码 agent 写的脚本在你自己的桌面机上被判成机器人时用它——一个 skill 加一个工厂函数，经 rebrowser-playwright 驱动你带窗口的真 Chrome；必须有显示器，对 IP、行为和验证码类拦截无效，核心依赖自 2025-05 起未发版。 | C（5/6） | [→](playwright-bot-bypass.zh.md) |
| **camofox-browser** | 当一个多用户、常驻的 agent 总被弹验证码时用它——在 Camoufox 反检测 Firefox 之上的常驻 REST/MCP/OpenClaw 服务，带按用户隔离的会话和按编号操作的快照；路由默认敞开、遥测默认开启，提交集中在一人，项目才八个月。 | B（6/6） | [→](camofox-browser.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [invisible_playwright_mcp](invisible-playwright-mcp.zh.md) | ✅ | B（5/6） | 当 MCP 助手总被验证码和机器人墙拦住时用它——它驱动一个 C++ 层打过补丁、指纹由种子推导的隐身 Firefox；只支持 Windows/Linux，单人维护，星数继承自改名前的投简历机器人仓库。 |
| [playwright-bot-bypass](playwright-bot-bypass.zh.md) | ✅ | C（5/6） | 一个 agent skill 加约 180 行的工厂函数，架在带窗口的真 Chrome 和 rebrowser-playwright 上：指纹破绽不是伪造掉而是不存在，macOS 也能用；只适合桌面机，数据为作者自测，单人维护，核心依赖停滞。 |
| [camofox-browser](camofox-browser.zh.md) | ✅ | B（6/6） | 一个共享的 Node 服务，把 Camoufox 反检测 Firefox 放到 REST、OpenClaw 和 MCP 工具后面，带按用户隔离的会话、cookie 导入和代理轮换；反检测能力全部继承自上游 Camoufox，不配置的话路由无鉴权、遥测开启，内存泄漏报告反复出现。 |

## 什么该放这里

以 agent 浏览器会话被识别或拦截为决定性选型轴的工具：隐身 MCP 接口、面向 agent 的浏览器配方，以及常驻反检测会话服务。本类不保证绕过挑战，也不授予自动化目标站点的权限。通用浏览器控制、DevTools 检查和已有登录态桥接留在 [agent-browser-tools](../INDEX.zh.md)；代码优先的浏览器引擎留在 [browser-driver-frameworks](../../browser-driver-frameworks/INDEX.zh.md)。
