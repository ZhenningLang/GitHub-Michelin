# editors-and-runtimes

> 分类节点。代码编辑器、IDE 扩展、应用运行时与 JavaScript/TypeScript 工具链。
> ← 返回 [dev-utilities](../INDEX.zh.md) · 根：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **IdeaVim** | 当你离不开 JetBrains IDE、又想要 Vim 的动作、模式和 `.ideavimrc` 时用它——但它只是 Vim 子集的模拟，重度用户会撞上还原度的缺口。 | A（4/6） | [→](ideavim.zh.md) |
| **VS Code** | 当你需要一款快速、跨平台、具备智能补全、调试功能和最大扩展市场的代码编辑器时用它——但它是 Electron 应用，且分发版包含微软遥测。 | A（5/6） | [→](vscode.zh.md) |
| **Tauri** | 当你想用 Rust 和操作系统原生 Webview 构建小巧、快速、安全的跨平台桌面与移动应用，替代 Electron 时用它。 | A（6/6） | [→](tauri.zh.md) |
| **Deno** | 当你想要一个具备安全默认设置、内置工具链和原生 TypeScript 支持的现代 JavaScript/TypeScript 运行时，无需 node_modules 时用它。 | A（6/6） | [→](deno.zh.md) |
| **Bun** | 当你想要一个极速一体化 JavaScript/TypeScript 工具集（运行时、打包器、测试运行器、包管理器）集成在单个二进制文件中时用它——但商用前请核实许可证。 | A（5/6） | [→](bun.zh.md) |
| **Zed** | 当你想要一个高性能原生代码编辑器，支持实时多人协作时用它——但它的扩展生态远小于 VS Code，且仅约 4 年历史。 | A（4/6） | [→](zed.zh.md) |
| **scriptc** | 当类型写干净的 TypeScript CLI 或小型服务要以又小、启动又快的原生二进制或 WASI 模块交付时用它——但它只是两个月大的 Vercel Labs 实验，编不了静态的部分会被直接拒绝。 | C（6/6） | [→](scriptc.zh.md) |
| **TanStack CLI** | 当你要起一个 TanStack Start／Router 应用、希望认证、数据库、部署、监控以 add-on 方式组合进来时用它——技术栈不在 TanStack 上、或项目没有 `.cta.json` 可对照时不要用。 | B（6/6） | [→](tanstack-cli.zh.md) |
| **TanStack Devtools** | 当你的 Vite 应用挂着好几个 TanStack（或自家）库的调试面板、想合并成一个页内可停靠面板并附带点元素跳源码、生产构建自动剥离时用它——查 React 内部用 React DevTools；非 Vite/Rspack 构建、或开发服务器能被别人访问（命令注入 issue #464 未修）时不要用。 | B（6/6） | [→](tanstack-devtools.zh.md) |
| **TanStack Config** | 当 pnpm monorepo 里的 TypeScript 库要按 TanStack 自家包的方式做检查（以及遗留的 ESM／CJS 双格式构建）时用它——新项目的构建别用（TanStack 自己已转向 tsdown），发版流水线也别用（用 Changesets）。 | B（6/6） | [→](tanstack-config.zh.md) |
| **TanStack Container** | 当你要把真实的 Vite／TanStack Start 项目放进访客浏览器里跑——安装、进程、预览、存档恢复——而且要 MIT 开源、资源自托管，而不是闭源商业内核时用它——但 2026-09 时 npm 包还没发布，项目自己也声明不是安全边界。 | C（5/6） | [→](tanstack-container.zh.md) |
| **TanStack alt-cli** | 只把它当集成组合式脚手架的模式参考——2026 年 1 月只活了一周的 TanStack 实验，已归档，`@tanstack/cli` 包名如今发的是主线 CLI；要跑的东西一律用 TanStack CLI。 | D（5/6） | [→](tanstack-alt-cli.zh.md) |
| **NetWasm** | 当 C# 程序必须打包成一个极小的独立 WASI 组件交付——GC 链接在产物里、目标机器不装 .NET——时用它；但它是 7 周大的单人 pre-1.0 项目，工具链挂自定义非开源许可证。 | C（4/6） | [→](netwasm.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [IdeaVim](ideavim.zh.md) | ✅ | A（4/6） | 当你离不开 JetBrains IDE、又想要 Vim 的动作、模式和 `.ideavimrc` 时用它——但它只是 Vim 子集的模拟，重度用户会撞上还原度的缺口。 |
| [VS Code](vscode.zh.md) | ✅ | A（5/6） | 当你需要一款快速、跨平台、具备智能补全、调试功能和最大扩展市场的代码编辑器时用它——但它是 Electron 应用，且分发版包含微软遥测。 |
| [Tauri](tauri.zh.md) | ✅ | A（6/6） | 当你想用 Rust 和操作系统原生 Webview 构建小巧、快速、安全的跨平台桌面与移动应用，替代 Electron 时用它。 |
| [Deno](deno.zh.md) | ✅ | A（6/6） | 当你想要一个具备安全默认设置、内置工具链和原生 TypeScript 支持的现代 JavaScript/TypeScript 运行时，无需 node_modules 时用它。 |
| [Bun](bun.zh.md) | ✅ | A（5/6） | 当你想要一个极速一体化 JavaScript/TypeScript 工具集（运行时、打包器、测试运行器、包管理器）集成在单个二进制文件中时用它——但商用前请核实许可证。 |
| [Zed](zed.zh.md) | ✅ | A（4/6） | 当你想要一个高性能原生代码编辑器，支持实时多人协作时用它——但它的扩展生态远小于 VS Code，且仅约 4 年历史。 |
| [scriptc](scriptc.zh.md) | ✅ | C（6/6） | 当类型写干净的 TypeScript CLI 或小型服务要以又小、启动又快的原生二进制或 WASI 模块交付时用它——但它只是两个月大的 Vercel Labs 实验，编不了静态的部分会被直接拒绝。 |
| [TanStack CLI](tanstack-cli.zh.md) | ✅ | B（6/6） | 当你要起一个 TanStack Start／Router 应用、希望认证、数据库、部署、监控以 add-on 方式组合进来时用它——技术栈不在 TanStack 上、或项目没有 `.cta.json` 可对照时不要用。 |
| [TanStack Devtools](tanstack-devtools.zh.md) | ✅ | B（6/6） | 当你的 Vite 应用挂着好几个 TanStack（或自家）库的调试面板、想合并成一个页内可停靠面板并附带点元素跳源码、生产构建自动剥离时用它——查 React 内部用 React DevTools；非 Vite/Rspack 构建、或开发服务器能被别人访问（命令注入 issue #464 未修）时不要用。 |
| [TanStack Config](tanstack-config.zh.md) | ✅ | B（6/6） | 当 pnpm monorepo 里的 TypeScript 库要按 TanStack 自家包的方式做检查（以及遗留的 ESM／CJS 双格式构建）时用它——新项目的构建别用（TanStack 自己已转向 tsdown），发版流水线也别用（用 Changesets）。 |
| [TanStack Container](tanstack-container.zh.md) | ✅ | C（5/6） | 当你要把真实的 Vite／TanStack Start 项目放进访客浏览器里跑——安装、进程、预览、存档恢复——而且要 MIT 开源、资源自托管，而不是闭源商业内核时用它——但 2026-09 时 npm 包还没发布，项目自己也声明不是安全边界。 |
| [TanStack alt-cli](tanstack-alt-cli.zh.md) | ✅ | D（5/6） | 只把它当集成组合式脚手架的模式参考——2026 年 1 月只活了一周的 TanStack 实验，已归档，`@tanstack/cli` 包名如今发的是主线 CLI；要跑的东西一律用 TanStack CLI。 |
| [NetWasm](netwasm.zh.md) | ✅ | C（4/6） | 当 C# 程序必须打包成一个极小的独立 WASI 组件交付——GC 链接在产物里、目标机器不装 .NET——时用它；但它是 7 周大的单人 pre-1.0 项目，工具链挂自定义非开源许可证。 |

## 什么该放这里

代码编辑器、IDE 扩展、应用运行时与 JavaScript/TypeScript 工具链。
