# dev-utilities

> 分类节点。独立开发者工具、数据处理工具、开发者运行时与可自托管基础设施。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **数据工具** | 离线转换、压缩、假数据、字体处理、进度条与搜索工具。 | [→](data-tools/INDEX.zh.md) |
| **二进制分析** | 检查无源码程序、收集逆向证据与重建候选源码。 | [→](binary-analysis/INDEX.zh.md) |
| **运维基础设施** | 服务器管理、指标采集、TLS 自动化、镜像瘦身、代理、远程桌面与密码基础设施。 | [→](ops-infra/INDEX.zh.md) |
| **编辑器与运行时** | 代码编辑器、IDE 扩展、应用运行时与 JS/TS 工具链。 | [→](editors-and-runtimes/INDEX.zh.md) |
| **包管理器 GUI** | 命令行包管理器的桌面前端——不用终端就能浏览、安装与升级（当前是 macOS 上的 Homebrew）。 | [→](package-manager-gui/INDEX.zh.md) |
| **包管理器** | 命令行包管理器本身——解析、下载并把软件包装进前缀的那个工具（当前是一个更快的 Homebrew 客户端）。 | [→](package-managers/INDEX.zh.md) |

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenRewrite** | 用类型信息执行 Java 迁移规则并审查差异；先核对新语言模块许可与制品下载权益。 | B（5/6） | [→](openrewrite.zh.md) |
| **Keploy** | 连同依赖响应录制 API 调用，供回归重放；须批准内核权限，并显式启用非 JSON 正文比较。 | A（6/6） | [→](keploy.zh.md) |
| **App Store Connect CLI** | 用独立 Go 命令管理苹果发布文案、TestFlight 与审核操作。 | B（6/6） | [→](app-store-connect-cli.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenRewrite](openrewrite.zh.md) | 已收录 | B（5/6） | 可复用的 JVM 转换规则，不是 Moderne 多仓库平台；核心 Apache 许可不覆盖所有语言模块。 |
| [Keploy](keploy.zh.md) | 已收录 | A（6/6） | 用捕获夹具代替手写桩；仍有 Linux 探测、私有解析器、服务条款和默认非 JSON 比较盲区。 |
| [App Store Connect CLI](app-store-connect-cli.zh.md) | ✅ | B（6/6） | 不需要 Ruby 的苹果发布 API 命令；仍要管理凭据和审批，本地构建需要 Xcode，默认开启遥测。 |

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [数据工具](data-tools/INDEX.zh.md) | 子分类 | 离线转换、压缩、假数据、字体处理、进度条与搜索工具。 |
| [二进制分析](binary-analysis/INDEX.zh.md) | 子分类 | 检查无源码程序、收集逆向证据与重建候选源码。 |
| [运维基础设施](ops-infra/INDEX.zh.md) | 子分类 | 服务器管理、指标采集、TLS 自动化、镜像瘦身、代理、远程桌面与密码基础设施。 |
| [编辑器与运行时](editors-and-runtimes/INDEX.zh.md) | 子分类 | 代码编辑器、IDE 扩展、应用运行时与 JS/TS 工具链。 |
| [包管理器 GUI](package-manager-gui/INDEX.zh.md) | 子分类 | 命令行包管理器的桌面前端——不用终端就能浏览、安装与升级（当前是 macOS 上的 Homebrew）。 |
| [包管理器](package-managers/INDEX.zh.md) | 子分类 | 命令行包管理器本身——解析、下载并把软件包装进前缀的那个工具（当前是一个更快的 Homebrew 客户端）。 |

## 什么该放这里

按工具类型继续下钻：数据处理、二进制分析、运维基础设施、编辑器 / 运行时，或包管理器前端。
