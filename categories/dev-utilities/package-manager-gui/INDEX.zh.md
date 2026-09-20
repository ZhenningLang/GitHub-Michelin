# package-manager-gui

> 分类节点。命令行包管理器的桌面前端——不用终端就能浏览、安装、升级和卸载。当前条目全部是 macOS／Homebrew 图形前端。
> ← 返回 [dev-utilities](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **BrewUI** | 当你在 macOS 26 上想要 Homebrew 官方 GUI，并且要把底层每条 `brew` 命令显示在可复制的控制台里时用它。 | C（4/6） | [→](brewui.zh.md) |
| **Applite** | 当非技术用户需要在从未有过终端的机器上安装 Mac 应用时用它——它自带 Homebrew，且只管理 cask。 | B（5/6） | [→](applite.zh.md) |
| **CaskHub** | 当你在 macOS 15.6+ 上想要最丰富的应用商店式 cask 浏览体验时用它，但要接受内置的遥测。 | B（5/6） | [→](caskhub.zh.md) |
| **Cork** | 当你想要最完整的 Homebrew 操作面——services、tap、标签、菜单栏更新——并愿意为预编译版付 25€ 时用它。 | B（4/6） | [→](cork.zh.md) |
| **Cakebrew** | 只把它当作第一代 Homebrew GUI 的参考；它自 2021 年起实际已无人维护，也没有可安装的 cask。 | E（3/6） | [→](cakebrew.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [BrewUI](brewui.zh.md) | ✅ | C（4/6） | 官方、透明、带完整控制台——代价是 macOS 26 门槛，且不管理 tap 与 prefix。 |
| [Applite](applite.zh.md) | ✅ | B（5/6） | 不需要终端也不需要 Homebrew，Brewfile 还能往返——但只支持 cask，且应用自己拥有一份 Homebrew。 |
| [CaskHub](caskhub.zh.md) | ✅ | B（5/6） | 目录浏览最丰富、近期安装触达最强——但只支持 cask，且内置 Sentry 与 TelemetryDeck。 |
| [Cork](cork.zh.md) | ✅ | B（4/6） | 拥有 brew 本身缺失的 services、标签与菜单栏更新——但预编译版 25€，且许可禁止复用。 |
| [Cakebrew](cakebrew.zh.md) | ✅ | E（3/6） | Objective-C 时代的 formula 与 tap 管理——但主分支自 2021 年起没动过。 |

## 什么该放这里

包装命令行包管理器的桌面图形界面：目录浏览、安装／升级／卸载，以及底层包管理器提供的管理面。包管理器本身、以及不驱动真实包管理器的应用商店客户端不属于这里。
