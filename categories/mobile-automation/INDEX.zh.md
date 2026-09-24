# mobile-automation

> 分类节点。程序化驱动 iOS／Android 模拟器与真机——注入输入、驱动界面、跑端到端流程。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **baguette** | 当你想无头、可脚本地控制 Apple Silicon 上的 iOS 模拟器——60fps 投屏、宿主机手势注入、多设备 farm——但它需要 Xcode 26，且骑在 SimulatorKit 私有符号上时使用。 | B（6/6） | [→](baguette.zh.md) |
| **idb** | 当你要从远端客户端用细粒度原语自动化 iOS 模拟器**和**真机时用它——但 iOS 26 打坏了它一部分能力，且每个目标要挂一个 companion 进程。 | B（6/6） | [→](idb.zh.md) |
| **AXe** | 当你想要一个 `axe tap／type／describe-ui` 命令直接操作模拟器时用它——但它是单人维护，2026-07 后就没动静了。 | B（6/6） | [→](axe.zh.md) |
| **Appium** | 当你需要一个跨平台、跨语言的 WebDriver 测试框架同时覆盖 iOS 和 Android 时用它——代价是要自己跑一个服务端并逐平台装驱动。 | A（6/6） | [→](appium.zh.md) |
| **WebDriverAgent** | 当你要自己搭 iOS 自动化底层时用它——它就是 Appium 驱动的那个 WebDriver 服务端，多数团队不会单独跑它。 | A（4/6） | [→](webdriveragent.zh.md) |
| **Maestro** | 当你想用 YAML 流程、几分钟就能上手做 Android／iOS／Web 的端到端测试时用它——但不支持 iOS 真机。 | A（6/6） | [→](maestro.zh.md) |
| **Detox** | 当你在测 React Native 应用、想要灰盒同步来压住 flaky 时用它——但它锁 React Native 版本、只支持 JS，且不支持 iOS 真机。 | B（6/6） | [→](detox.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [baguette](baguette.zh.md) | ✅ | B（6/6） | 无头模拟器控制带投屏和 farm，但仅限 Apple Silicon＋Xcode 26，且依赖私有符号。 |
| [idb](idb.zh.md) | ✅ | B（6/6） | 面向模拟器**和**真机的细粒度远端原语，但更重（每个目标一个 companion），且 iOS 26 回归问题仍开着。 |
| [AXe](axe.zh.md) | ✅ | B（6/6） | 最省事的模拟器输入 CLI，但单人维护、2026-07 后停滞。 |
| [Appium](appium.zh.md) | ✅ | A（6/6） | 覆盖面最广的跨平台框架，代价是跑服务端并逐个装驱动。 |
| [WebDriverAgent](webdriveragent.zh.md) | ✅ | A（4/6） | Appium XCUITest 驱动底下的 iOS 引擎——是依赖，不是独立的测试工具。 |
| [Maestro](maestro.zh.md) | ✅ | A（6/6） | 扁平 YAML 流程、上手最快，但不支持 iOS 真机。 |
| [Detox](detox.zh.md) | ✅ | B（6/6） | 对 React Native 的 flaky 控制最好，但锁 RN 版本且只支持 JS。 |
| （各页对比里点到的非仓库工具） | 非仓库 | — | `xcrun simctl` 与 `XCUITest` 随 Xcode 分发；详见各页横向对比。 |

## 什么该放这里

**驱动移动设备及其模拟器／仿真器**的工具——iOS（以及工具自身覆盖的 Android）的输入注入、UI 自动化与端到端测试框架。不含桌面 GUI 自动化（见 `desktop-automation`）和网页自动化（见 `web-automation`）。
