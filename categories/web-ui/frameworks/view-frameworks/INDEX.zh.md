# view-frameworks

> 分类节点。组件与视图层框架——在浏览器里渲染组件、管理响应式的那层运行时。
> ← 返回[frameworks](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Angular** | 用于构建移动端和桌面端 Web 应用的综合性开发平台。基于 TypeScript，由 Google 构建和维护，专注于企业级应用。 | A（6/6） | [→](angular.zh.md) |
| **Lit** | 一个由 Google 出品的轻量级库，用于构建快速、可互操作的 Web Components。基于 Web Components 标准，无虚拟 DOM，运行时体积极小（lit-html 约 3 KB）。 | A（6/6） | [→](lit.zh.md) |
| **React** | 用于构建用户界面的声明式、组件化 JavaScript 库，由 Meta 维护。它是全球采用最广泛的 UI 库，从单页应用到通过 React Native 构建的原生移动应用都有它的身影。 | A（6/6） | [→](react.zh.md) |
| **Svelte** | 编译时前端框架，在构建阶段将组件转换为高效的 vanilla JavaScript，消除虚拟 DOM 开销，获得更小的包体积和更快的运行时性能。 | A（6/6） | [→](svelte.zh.md) |
| **TanStack Redact** | 当 Vite＋React 应用的包体积预算被约 69 KB、页面却用不到的 React 运行时吃掉时用它——一个插件把所有 React 导入换成约 23 KB 的同步重新实现——但应用依赖并发特性、构建工具不是 Vite、或需要许可证文件（目前没有）时不要用。 | D（6/6） | [→](tanstack-redact.zh.md) |
| **Vue.js** | 由 Evan You 创建的渐进式 JavaScript 用户界面框架，以温和的学习曲线、优秀的文档和可增量采纳的架构著称。 | A（6/6） | [→](vue.zh.md) |

## 什么该放这里

你用来写 UI 的组件模型与渲染运行时（React、Vue、Svelte、Angular、Lit），以及这类运行时的替换实现（TanStack Redact）。叠在其上的路由、SSR 与服务端代码归 `app-frameworks`；内容站与文档站归 `site-frameworks`；现成组件归 `web-ui/component-libraries`。
