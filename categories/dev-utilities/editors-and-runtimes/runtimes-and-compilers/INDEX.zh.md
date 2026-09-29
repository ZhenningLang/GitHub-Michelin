# runtimes-and-compilers

> 分类节点。代码在哪里跑、最后打包成什么——JS/TS 运行时、编译成原生或 WASI 的预编译器、以及用 Web 前端做桌面应用的外壳。
> ← 返回 [editors-and-runtimes](../INDEX.zh.md) · 根：[分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Deno** | 当你想要一个具备安全默认设置、内置工具链和原生 TypeScript 支持的现代 JavaScript/TypeScript 运行时，无需 node_modules 时用它。 | A（6/6） | [→](deno.zh.md) |
| **Bun** | 当你想要一个极速一体化 JavaScript/TypeScript 工具集（运行时、打包器、测试运行器、包管理器）集成在单个二进制文件中时用它——但商用前请核实许可证。 | A（5/6） | [→](bun.zh.md) |
| **Tauri** | 当你想用 Rust 和操作系统原生 Webview 构建小巧、快速、安全的跨平台桌面与移动应用，替代 Electron 时用它。 | A（6/6） | [→](tauri.zh.md) |
| **scriptc** | 当类型写干净的 TypeScript CLI 或小型服务要以又小、启动又快的原生二进制或 WASI 模块交付时用它——但它只是两个月大的 Vercel Labs 实验，编不了静态的部分会被直接拒绝。 | C（6/6） | [→](scriptc.zh.md) |
| **NetWasm** | 当 C# 程序必须打包成一个极小的独立 WASI 组件交付——GC 链接在产物里、目标机器不装 .NET——时用它；但它是 7 周大的单人 pre-1.0 项目，工具链挂自定义非开源许可证。 | C（4/6） | [→](netwasm.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Deno](deno.zh.md) | ✅ | A（6/6） | 当你想要一个具备安全默认设置、内置工具链和原生 TypeScript 支持的现代 JavaScript/TypeScript 运行时，无需 node_modules 时用它。 |
| [Bun](bun.zh.md) | ✅ | A（5/6） | 当你想要一个极速一体化 JavaScript/TypeScript 工具集（运行时、打包器、测试运行器、包管理器）集成在单个二进制文件中时用它——但商用前请核实许可证。 |
| [Tauri](tauri.zh.md) | ✅ | A（6/6） | 当你想用 Rust 和操作系统原生 Webview 构建小巧、快速、安全的跨平台桌面与移动应用，替代 Electron 时用它。 |
| [scriptc](scriptc.zh.md) | ✅ | C（6/6） | 当类型写干净的 TypeScript CLI 或小型服务要以又小、启动又快的原生二进制或 WASI 模块交付时用它——但它只是两个月大的 Vercel Labs 实验，编不了静态的部分会被直接拒绝。 |
| [NetWasm](netwasm.zh.md) | ✅ | C（4/6） | 当 C# 程序必须打包成一个极小的独立 WASI 组件交付——GC 链接在产物里、目标机器不装 .NET——时用它；但它是 7 周大的单人 pre-1.0 项目，工具链挂自定义非开源许可证。 |

## 什么该放这里

通用运行时（Deno、Bun），把程序编成独立原生二进制或 WASI 模块的编译器（scriptc、NetWasm），以及把 Web 前端打包成桌面／移动应用的应用运行时（Tauri）。不含绑定某个框架的脚手架或调试工具（见 `tanstack-tooling`），也不含编辑器（见 `code-editors`）。
