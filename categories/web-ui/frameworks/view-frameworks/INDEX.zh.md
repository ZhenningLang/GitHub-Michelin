# view-frameworks

> 分类节点。组件与视图层框架——在浏览器里渲染组件、管理响应式的那层运行时。
> ← 返回[frameworks](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Angular** | 当大型 TypeScript 团队需要路由、表单、HTTP、依赖注入和 CLI 都来自同一个统一版本的框架，让各小组接法一致时用它——但对小应用是大材小用，回避 TypeScript 的团队也会一直别扭。 | A（6/6） | [→](angular.zh.md) |
| **Lit** | 当一套设计系统要同时服务 React、Vue、Angular 和纯 HTML 应用，希望组件按标准自定义元素只发布一次时用它——但它是组件库不是应用框架，而且核心包自 2026 年 5 月以来发版放缓。 | A（6/6） | [→](lit.zh.md) |
| **React** | 当多页面应用需要按共享数据自动重渲染的组件，并且看重最大的生态、最深的招聘池和 React Native 这条移动端路线时用它——但它只是视图层，路由、取数和服务端渲染要靠框架补齐。 | A（6/6） | [→](react.zh.md) |
| **Svelte** | 当用户多在中端手机和不稳定网络上、框架运行时的体积成了问题，而团队更习惯写 HTML 和 CSS 时用它——但第三方生态和招聘池都远小于 React 和 Vue。 | A（6/6） | [→](svelte.zh.md) |
| **TanStack Redact** | 当 Vite＋React 应用的包体积预算被约 69 KB、页面却用不到的 React 运行时吃掉时用它——一个插件把所有 React 导入换成约 23 KB 的同步重新实现——但应用依赖并发特性、构建工具不是 Vite、或需要许可证文件（目前没有）时不要用。 | D（6/6） | [→](tanstack-redact.zh.md) |
| **Vue.js** | 当偏后端的团队想用绑定响应式数据的类 HTML 模板，先在现有服务端页面里放一个组件、再逐步长成完整应用时用它——但在欧美招聘市场 React 更占优，路线图也很大程度压在尤雨溪一人身上。 | A（6/6） | [→](vue.zh.md) |

## 什么该放这里

你用来写 UI 的组件模型与渲染运行时（React、Vue、Svelte、Angular、Lit），以及这类运行时的替换实现（TanStack Redact）。叠在其上的路由、SSR 与服务端代码归 `app-frameworks`；内容站与文档站归 `site-frameworks`；现成组件归 `web-ui/component-libraries`。
