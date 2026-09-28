# app-frameworks

> Category node. Full-stack application meta-frameworks and routers — routing, data loading, SSR and server code on top of a view framework.
> ← back to [frameworks](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Next.js** | The default full-stack React framework, created and maintained by Vercel. Ships with App Router, React Server Components, automatic static optimization, ISR, and a built-in API layer — with tight Vercel integration as the "happy path." | A (6/6) | [→](nextjs.md) |
| **Nuxt** | the full-stack Vue framework | A (6/6) | [→](nuxt.md) |
| **SvelteKit** | web development, streamlined | A (6/6) | [→](sveltekit.md) |
| **TanStack Router** | Use it when the URL is the app's state container and a mistyped link, param or search value must fail the compiler instead of the user — not when routing is a few static pages, or when RSC-first architecture is the requirement (pick Next.js; TanStack Start on top of it is still Release Candidate). | A (6/6) | [→](tanstack-router.md) |
| **TanStack Bling** | Archived 2023 Vite/Astro plugin that compiles `server$(fn)` into a server endpoint plus a client fetch stub — read it as a pattern source or to migrate an old dependency; for new apps use TanStack Start's `createServerFn`, SolidStart or Next.js Server Actions. | D (5/6) | [→](tanstack-bling.md) |

## What belongs here

Meta-frameworks and application routers that turn a view framework into an application: file or typed routing, loaders, SSR/SSG and server endpoints (Next.js, Nuxt, SvelteKit, TanStack Router). The view framework itself belongs in `view-frameworks`; frameworks whose deliverable is a content or docs site belong in `site-frameworks`.
