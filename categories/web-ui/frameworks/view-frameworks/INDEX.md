# view-frameworks

> Category node. Component / view-layer frameworks — the runtime that renders components and manages reactivity in the browser.
> ← back to [frameworks](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Angular** | Use it when a large TypeScript team needs routing, forms, HTTP, dependency injection, and a CLI from one versioned framework so every squad wires things the same way — but it is overkill for small apps and fights teams that avoid TypeScript. | A (6/6) | [→](angular.md) |
| **Lit** | Use it when one design system must serve React, Vue, Angular, and plain-HTML apps, so components ship once as standard custom elements — but it is a component library, not an app framework, and core releases have slowed since May 2026. | A (6/6) | [→](lit.md) |
| **React** | Use it when a many-screen app needs components that re-render from shared data and you value the largest ecosystem, deepest hiring pool, and a React Native path — but it is only the view layer, so routing, data loading, and SSR come from a framework. | A (6/6) | [→](react.md) |
| **Svelte** | Use it when users on mid-range phones and spotty networks make framework runtime weight matter and your team prefers plain HTML and CSS — but its third-party ecosystem and hiring pool are far smaller than React's or Vue's. | A (6/6) | [→](svelte.md) |
| **TanStack Redact** | Use it when a Vite + React app's bundle budget is eaten by ~69 KB of React runtime the pages never lean on — one plugin swaps every React import for a ~23 KB synchronous re-implementation — not when the app needs concurrent features, a non-Vite build, or a license file (there is none yet). | D (6/6) | [→](tanstack-redact.md) |
| **Vue.js** | Use it when a backend-leaning team wants reactive HTML-like templates, starting with one widget on an existing server-rendered page and growing into a full app — but Western hiring pools favor React, and the roadmap leans heavily on Evan You. | A (6/6) | [→](vue.md) |

## What belongs here

The component model and rendering runtime you build UI on (React, Vue, Svelte, Angular, Lit) plus drop-in replacements for such a runtime (TanStack Redact). Routing, SSR and server code layered on top belong in `app-frameworks`; content and docs sites in `site-frameworks`; ready-made components in `web-ui/component-libraries`.
