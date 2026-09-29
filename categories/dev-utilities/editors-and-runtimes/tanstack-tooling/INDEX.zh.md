# tanstack-tooling

> 分类节点。围绕 TanStack 技术栈的开发期工具——脚手架 CLI、调试面板、共享的检查／构建预设、浏览器内项目运行时。
> ← 返回 [editors-and-runtimes](../INDEX.zh.md) · 根：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **TanStack CLI** | 当你要起一个 TanStack Start／Router 应用、希望认证、数据库、部署、监控以 add-on 方式组合进来时用它——技术栈不在 TanStack 上、或项目没有 `.cta.json` 可对照时不要用。 | B（6/6） | [→](tanstack-cli.zh.md) |
| **TanStack Devtools** | 当你的 Vite 应用挂着好几个 TanStack（或自家）库的调试面板、想合并成一个页内可停靠面板并附带点元素跳源码、生产构建自动剥离时用它——查 React 内部用 React DevTools；非 Vite/Rspack 构建、或开发服务器能被别人访问（命令注入 issue #464 未修）时不要用。 | B（6/6） | [→](tanstack-devtools.zh.md) |
| **TanStack Config** | 当 pnpm monorepo 里的 TypeScript 库要按 TanStack 自家包的方式做检查（以及遗留的 ESM／CJS 双格式构建）时用它——新项目的构建别用（TanStack 自己已转向 tsdown），发版流水线也别用（用 Changesets）。 | B（6/6） | [→](tanstack-config.zh.md) |
| **TanStack Container** | 当你要把真实的 Vite／TanStack Start 项目放进访客浏览器里跑——安装、进程、预览、存档恢复——而且要 MIT 开源、资源自托管，而不是闭源商业内核时用它——但 2026-09 时 npm 包还没发布，项目自己也声明不是安全边界。 | C（5/6） | [→](tanstack-container.zh.md) |
| **TanStack alt-cli** | 只把它当集成组合式脚手架的模式参考——2026 年 1 月只活了一周的 TanStack 实验，已归档，`@tanstack/cli` 包名如今发的是主线 CLI；要跑的东西一律用 TanStack CLI。 | D（5/6） | [→](tanstack-alt-cli.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [TanStack CLI](tanstack-cli.zh.md) | ✅ | B（6/6） | 当你要起一个 TanStack Start／Router 应用、希望认证、数据库、部署、监控以 add-on 方式组合进来时用它——技术栈不在 TanStack 上、或项目没有 `.cta.json` 可对照时不要用。 |
| [TanStack Devtools](tanstack-devtools.zh.md) | ✅ | B（6/6） | 当你的 Vite 应用挂着好几个 TanStack（或自家）库的调试面板、想合并成一个页内可停靠面板并附带点元素跳源码、生产构建自动剥离时用它——查 React 内部用 React DevTools；非 Vite/Rspack 构建、或开发服务器能被别人访问（命令注入 issue #464 未修）时不要用。 |
| [TanStack Config](tanstack-config.zh.md) | ✅ | B（6/6） | 当 pnpm monorepo 里的 TypeScript 库要按 TanStack 自家包的方式做检查（以及遗留的 ESM／CJS 双格式构建）时用它——新项目的构建别用（TanStack 自己已转向 tsdown），发版流水线也别用（用 Changesets）。 |
| [TanStack Container](tanstack-container.zh.md) | ✅ | C（5/6） | 当你要把真实的 Vite／TanStack Start 项目放进访客浏览器里跑——安装、进程、预览、存档恢复——而且要 MIT 开源、资源自托管，而不是闭源商业内核时用它——但 2026-09 时 npm 包还没发布，项目自己也声明不是安全边界。 |
| [TanStack alt-cli](tanstack-alt-cli.zh.md) | ✅ | D（5/6） | 只把它当集成组合式脚手架的模式参考——2026 年 1 月只活了一周的 TanStack 实验，已归档，`@tanstack/cli` 包名如今发的是主线 CLI；要跑的东西一律用 TanStack CLI。 |

## 什么该放这里

TanStack 组织发布、价值基本以“你在用（或在开发）TanStack 栈”为前提的工具。TanStack 的*库*本身（Query、Router、Table、Form）在 `web-ui` 下。技术栈不是 TanStack 时，改从 `runtimes-and-compilers` 或对应的 `web-ui` 分类找。
