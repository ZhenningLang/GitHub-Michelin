# app-frameworks

> 分类节点。全栈应用元框架与路由——在视图框架之上补齐路由、数据加载、SSR 与服务端代码。
> ← 返回[frameworks](../INDEX.zh.md) · root: [分类路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Next.js** | 全栈 React 框架的默认选择，由 Vercel 创建并维护。内置 App Router、React Server Components、自动静态优化、ISR 和内置 API 层——与 Vercel 深度集成是「happy path」。 | A（6/6） | [→](nextjs.zh.md) |
| **Nuxt** | the full-stack Vue framework | A（6/6） | [→](nuxt.zh.md) |
| **SvelteKit** | web development, streamlined | A（6/6） | [→](sveltekit.zh.md) |
| **TanStack Router** | 当 URL 就是应用的状态容器、写错的链接／参数／查询值必须在编译期报错而不是吓到用户时用它——但路由只是寥寥几页静态页面时不要用，需要 RSC 优先架构时选 Next.js；其上的 TanStack Start 仍是 Release Candidate。 | A（6/6） | [→](tanstack-router.zh.md) |
| **TanStack Bling** | 2023 年已归档的 Vite／Astro 插件，把 `server$(fn)` 编译成服务端接口＋浏览器端发请求的替身——只当设计参考或迁移旧依赖时读；新应用用 TanStack Start 的 `createServerFn`、SolidStart 或 Next.js Server Actions。 | D（5/6） | [→](tanstack-bling.zh.md) |

## 什么该放这里

把视图框架变成一个应用的元框架与应用路由：文件式或类型化路由、loader、SSR/SSG 与服务端端点（Next.js、Nuxt、SvelteKit、TanStack Router）。视图框架本身归 `view-frameworks`；产出物是内容站或文档站的框架归 `site-frameworks`。
