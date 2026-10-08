# browser-driver-frameworks

> 分类节点。你自己写脚本调用的浏览器驱动与自动化框架——WebDriver、CDP，以及已归档的前身。
> ← 返回[web-automation](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Selenium** | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 | A（6/6） | [→](selenium.zh.md) |
| **Selenium Wire** | 当一套遗留的 Python Selenium 代码已经靠它读取或改写浏览器后台的请求和响应时用它——但它已归档、不再维护，新项目应改用 Selenium 4 的 CDP/BiDi 网络能力或 Playwright。 | D（5/6） | [→](selenium-wire.zh.md) |
| **Puppeteer** | 当 Node.js 任务本来就绑定 Chrome（服务端渲染 PDF、定时截图、预渲染单页应用、脚本化登录下载），并且你想用 Chrome 团队维护的参考 CDP 客户端时用它——但它不支持 Safari/WebKit，也没有测试运行器，这两样要用 Playwright。 | A（6/6） | [→](puppeteer.zh.md) |
| **nodriver** | 当你需要 Python-first 的异步直接 CDP 控制、且不想依赖 WebDriver 时用它；它仅支持 Chromium、采用 AGPL-3.0，反检测也只是尽力而为，不是稳定绕过契约。 | C（5/6） | [→](nodriver.zh.md) |
| **PhantomJS** | 只在遗留 CI 任务、截图服务或爬虫已经钉死它、你得撑到迁移完成时用它——但它已归档、2018 年起停止开发，新工作请用 Puppeteer 或 Playwright 驱动的无头 Chrome。 | C（5/6） | [→](phantomjs.zh.md) |
| **Moli** | 当结构优先的 agent 机群要用约 100 MB 的单进程浏览、真实布局与截图只是按需打开的例外，协议面要 CDP+WebDriver 时用它。 | B（6/6） | [→](moli.zh.md) |
| **Lightpanda** | 当批量 JS+DOM 提取永远不看像素时用它：无渲染引擎的 Zig 浏览器，自报比 Chrome 省 16 倍内存，带 CDP/BiDi/MCP。 | B（6/6） | [→](lightpanda.zh.md) |
| **Obscura** | 当对抗性抓取要一个自带 stealth、常开渲染、单文件的 Rust 浏览器时用它。 | B（6/6） | [→](obscura.zh.md) |
| **undetected-chromedriver** | 只在要让现成的 Python Selenium 代码绕开 chromedriver 自带的检测标记、又没法重写时用它——PyPI 最后一版停在 2024-02，新项目该用 nodriver 或 SeleniumBase UC Mode。 | C（4/6） | [→](undetected-chromedriver.zh.md) |
| **Camoufox** | 当 Playwright 爬虫因为浏览器本身被识别而被拦时用它：在引擎层伪装指纹的 Firefox 分支——只有 Firefox、约 1.3 GB、自己声明不适合稳定生产。 | B（6/6） | [→](camoufox.zh.md) |
| **rebrowser-playwright** | 只在一个钉在 1.52 的现有 Node.js Playwright 任务因 Chrome 上的 `Runtime.Enable` CDP 信号被识别时用它——预先打好补丁的直接替换包，自 2025-05 起冻结。 | D（3/6） | [→](rebrowser-playwright.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Selenium](selenium.zh.md) | ✅ | A（6/6） | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 |
| [Selenium Wire](selenium-wire.zh.md) | ✅ | D（5/6） | 换来只改一行 import 就能抓请求、mock 响应、导出 HAR；代价是一个自带 CA 证书的 MITM 代理、TLS 开销、遇证书固定会崩，依赖还封顶在 Python 3.10。 |
| [Puppeteer](puppeteer.zh.md) | ✅ | A（6/6） | 依赖最小、Chrome 优先、保留原始 CDP 通道且有 Google 背书，代价是不支持 WebKit、没有内置测试运行器，大版本更迭快、常有破坏性变更。 |
| [nodriver](nodriver.zh.md) | ✅ | C（5/6） | 不依赖 WebDriver 的 Python 异步直接 CDP 控制，代价是没有跨浏览器覆盖、许可不宽松，反检测也仅为尽力而为。 |
| [PhantomJS](phantomjs.zh.md) | ✅ | C（5/6） | 换来今天不改一行就让老流水线继续跑；代价是冻结的 WebKit 渲染不了现代网页、引擎 CVE 永不修补，所以要隔离它，绝不喂不可信内容。 |
| [Moli](moli.zh.md) | ✅ | B（6/6） | 结构优先的 agent 机群要 ~100 MB 单进程浏览、渲染按需打开、一个端点说 CDP+WebDriver 时用它；兼容性长尾让给真实 Chrome。 |
| [Lightpanda](lightpanda.zh.md) | ✅ | B（6/6） | 批量 JS+DOM 提取且永不渲染时最划算；要截图/几何就得换引擎，AGPL 也要先过法务。 |
| [Obscura](obscura.zh.md) | ✅ | B（6/6） | 对抗性赛道要 stealth+常开渲染的单文件浏览器时用它；协议面以 CDP 为主，治理面还很薄。 |
| [undetected-chromedriver](undetected-chromedriver.zh.md) | ✅ | C（4/6） | 保住每一个 Selenium 调用，同时把 chromedriver 的标记抹掉；代价是 GPL-3.0、默认不开沙箱、2024-02 之后没有发版。 |
| SeleniumBase | 未收录 | — | 开箱即用的 Python 浏览器测试框架，其 UC Mode 建在 undetected-chromedriver 之上；nodriver 与 undetected-chromedriver 页面都提到它。 |
| [Camoufox](camoufox.zh.md) | ✅ | B（6/6） | 在重新编译、隐藏自动化并轮换设备身份的 Firefox 上保留 Playwright API；代价是 GB 级下载、扮不了 Chrome、2025 年有过维护空窗，以及条款与法律风险自担。 |
| [rebrowser-playwright](rebrowser-playwright.zh.md) | ✅ | D（3/6） | 保留 Playwright API 并去掉一条可被检测的 CDP 命令；停在 Playwright 1.52.0，2025-05 之后没有维护者活动，新项目应选仍在更新的 patchright。 |

## 什么该放这里

开发者直接编码调用的库与框架，包括为迁移决策而保留的已归档项目。
