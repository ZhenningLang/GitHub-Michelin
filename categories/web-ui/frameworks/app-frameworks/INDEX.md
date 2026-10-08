# app-frameworks

> Category node. Full-stack application meta-frameworks and routers — routing, data loading, SSR and server code on top of a view framework.
> ← back to [frameworks](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Next.js** | Use it when a React product needs server-rendered pages search engines can read plus backend routes in the same codebase, like a marketplace or SaaS with public pages — but static content sites suit Astro better, and Vercel alone steers the roadmap. | B (5/6) | [→](nextjs.md) |
| **Nuxt** | Use it when a Vue team needs server-rendered pages search engines can read and an API in the same project's server folder, deployable to Node, serverless, or edge — but it is Vue-only, and since NuxtLabs joined Vercel its roadmap owner also owns Next.js. | A (6/6) | [→](nuxt.md) |
| **SvelteKit** | Use it when a small team wants Svelte with folder-based routing, server-side data loading, progressively enhanced forms, and adapters for Node, serverless, or static hosts — but 3.0 (2026-10) is a large breaking release, and React's ecosystem does not plug in. | A (6/6) | [→](sveltekit.md) |
| **TanStack Router** | Use it when the URL is the app's state container and a mistyped link, param or search value must fail the compiler instead of the user — not when routing is a few static pages, or when RSC-first architecture is the requirement (pick Next.js; TanStack Start on top of it is still Release Candidate). | A (6/6) | [→](tanstack-router.md) |
| **TanStack Bling** | Archived 2023 Vite/Astro plugin that compiles `server$(fn)` into a server endpoint plus a client fetch stub — read it as a pattern source or to migrate an old dependency; for new apps use TanStack Start's `createServerFn`, SolidStart or Next.js Server Actions. | D (5/6) | [→](tanstack-bling.md) |

## What belongs here

Meta-frameworks and application routers that turn a view framework into an application: file or typed routing, loaders, SSR/SSG and server endpoints (Next.js, Nuxt, SvelteKit, TanStack Router). The view framework itself belongs in `view-frameworks`; frameworks whose deliverable is a content or docs site belong in `site-frameworks`.
