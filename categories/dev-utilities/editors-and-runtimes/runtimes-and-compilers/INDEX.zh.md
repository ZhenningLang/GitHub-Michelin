# runtimes-and-compilers

> 分类节点。代码在哪里跑、最后打包成什么——JS/TS 运行时、编译成原生或 WASI 的预编译器、以及用 Web 前端做桌面应用的外壳。
> ← 返回 [editors-and-runtimes](../INDEX.zh.md) · 根：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Deno** | 当你新起一个 TypeScript 后端、命令行工具或脚本，默认拒绝文件、网络和环境变量访问以及内置 fmt、lint、test 比原样运行现有 Node 代码更重要时用它——但大型 Node 应用迁移和依赖原生插件的项目不合适。 | A（6/6） | [→](deno.zh.md) |
| **Bun** | 当一个 Node.js 上的 TypeScript 项目想用一个快速二进制同时负责运行 .ts、装包、打包和测试时用它——但 Node API 尚未完全兼容，v1.4 刚把代码库从 Zig 重写为 Rust，也没有权限沙箱。 | A（5/6） | [→](bun.zh.md) |
| **Tauri** | 当一个 Web 前端的桌面应用要做到安装包小、内存低，而不是像 Electron 那样捎带整份 Chromium 时用它——但各系统 webview 渲染不一致，Linux 需要 webkit2gtk 4.1，原生逻辑必须用 Rust 写。 | A（6/6） | [→](tauri.zh.md) |
| **scriptc** | 当类型写干净的 TypeScript CLI 或小型服务要以又小、启动又快的原生二进制或 WASI 模块交付时用它——但它只是两个月大的 Vercel Labs 实验，编不了静态的部分会被直接拒绝。 | C（6/6） | [→](scriptc.zh.md) |
| **NetWasm** | 当 C# 程序必须打包成一个极小的独立 WASI 组件交付——GC 链接在产物里、目标机器不装 .NET——时用它；但它是 7 周大的单人 pre-1.0 项目，工具链挂自定义非开源许可证。 | C（4/6） | [→](netwasm.zh.md) |
| **Effect** | 当一个要长期维护的 TypeScript 服务老是以类型里没写的方式出错，而你想让错误、依赖和取消都由 `tsc` 检查、跑在一个零依赖的运行时上时用它——但这套模型会传染，4.0 才发布一周，HTTP／SQL／RPC／工作流模块还标着 unstable。 | A（6/6） | [→](effect.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Deno](deno.zh.md) | ✅ | A（6/6） | 一个二进制里拿到沙箱化运行时和整套工具链，代价是要学新约定（权限参数、deno.json、JSR），对 Node 的 node_modules 目录结构也只是部分兼容。 |
| [Bun](bun.zh.md) | ✅ | A（5/6） | 同一份 package.json 下少几个工具、少等一会儿，代价是运行时兼容缺口，以及路线图归一家公司（Oven，现已并入 Anthropic）。 |
| [Tauri](tauri.zh.md) | ✅ | A（6/6） | 换来小安装包和基于 capability 的权限模型，代价是各平台渲染有差异，团队还得接上 Rust 工具链。 |
| [scriptc](scriptc.zh.md) | ✅ | C（6/6） | 当类型写干净的 TypeScript CLI 或小型服务要以又小、启动又快的原生二进制或 WASI 模块交付时用它——但它只是两个月大的 Vercel Labs 实验，编不了静态的部分会被直接拒绝。 |
| [NetWasm](netwasm.zh.md) | ✅ | C（4/6） | 当 C# 程序必须打包成一个极小的独立 WASI 组件交付——GC 链接在产物里、目标机器不装 .NET——时用它；但它是 7 周大的单人 pre-1.0 项目，工具链挂自定义非开源许可证。 |
| [Effect](effect.zh.md) | ✅ | A（6/6） | 当一个要长期维护的 TypeScript 服务老是以类型里没写的方式出错，而你想让错误、依赖和取消都由 `tsc` 检查、跑在一个零依赖的运行时上时用它——但这套模型会传染，4.0 才发布一周，HTTP／SQL／RPC／工作流模块还标着 unstable。 |

## 什么该放这里

通用运行时（Deno、Bun），把程序编成独立原生二进制或 WASI 模块的编译器（scriptc、NetWasm），以及把 Web 前端打包成桌面／移动应用的应用运行时（Tauri）。也包括在语言内部替换平台自带异步与错误模型、供整个应用使用的运行时库（Effect）。不含绑定某个框架的脚手架或调试工具（见 `tanstack-tooling`），也不含编辑器（见 `code-editors`）。
