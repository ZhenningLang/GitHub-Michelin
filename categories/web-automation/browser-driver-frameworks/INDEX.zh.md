# browser-driver-frameworks

> 分类节点。你自己写脚本调用的浏览器驱动与自动化框架——WebDriver、CDP，以及已归档的前身。
> ← 返回[web-automation](../INDEX.zh.md) · root: [分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Selenium** | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 | A（6/6） | [→](selenium.zh.md) |
| **Selenium Wire** | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 | D（5/6） | [→](selenium-wire.zh.md) |
| **Puppeteer** | JavaScript API for Chrome and Firefox | A（6/6） | [→](puppeteer.zh.md) |
| **nodriver** | 当你需要 Python-first 的异步直接 CDP 控制、且不想依赖 WebDriver 时用它；它仅支持 Chromium、采用 AGPL-3.0，反检测也只是尽力而为，不是稳定绕过契约。 | C（5/6） | [→](nodriver.zh.md) |
| **PhantomJS** | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 | C（5/6） | [→](phantomjs.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Selenium](selenium.zh.md) | ✅ | A（6/6） | 当你需要跨浏览器、跨语言的 WebDriver 自动化时用它——现代单浏览器体验 Playwright/Cypress 更顺手。 |
| [Selenium Wire](selenium-wire.zh.md) | ✅ | D（5/6） | 当遗留的 Selenium 测试套件需要读取或改写浏览器后台 HTTP 流量时用它——但它已归档，新项目应改用 Selenium 4 原生 CDP/BiDi 或 Playwright。 |
| [Puppeteer](puppeteer.zh.md) | ✅ | A（6/6） | Chrome-first 的 JavaScript 自动化；当前索引条目仍需要补齐选型边界。 |
| [nodriver](nodriver.zh.md) | ✅ | C（5/6） | 不依赖 WebDriver 的 Python 异步直接 CDP 控制，代价是没有跨浏览器覆盖、许可不宽松，反检测也仅为尽力而为。 |
| [PhantomJS](phantomjs.zh.md) | ✅ | C（5/6） | 新项目别用——已归档、停更的可脚本化无头浏览器；改用 Puppeteer/Playwright 的无头 Chrome 或 Selenium。 |
| undetected-chromedriver / SeleniumBase | 未收录 | — | nodriver 页面提到的 Selenium 兼容 stealth 工具与开箱即用 Python 浏览器测试框架。 |

## 什么该放这里

开发者直接编码调用的库与框架，包括为迁移决策而保留的已归档项目。
