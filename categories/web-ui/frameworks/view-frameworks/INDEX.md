# view-frameworks

> Category node. Component / view-layer frameworks — the runtime that renders components and manages reactivity in the browser.
> ← back to [frameworks](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Angular** | A comprehensive web development platform for building mobile and desktop web applications using TypeScript. Built and maintained by Google with a strong focus on enterprise-scale apps. | A (6/6) | [→](angular.md) |
| **Lit** | A lightweight library from Google for building fast, interoperable web components. Built on Web Components standards with no virtual DOM and a tiny runtime (~3 KB for lit-html). | A (6/6) | [→](lit.md) |
| **React** | A declarative, component-based JavaScript library for building user interfaces. Maintained by Meta, it is the most widely adopted UI library in the world, powering everything from single-page apps to native mobile apps via React Native. | A (6/6) | [→](react.md) |
| **Svelte** | A compile-time frontend framework that transforms components into efficient vanilla JavaScript at build time, eliminating virtual DOM overhead for smaller bundles and faster runtime performance. | A (6/6) | [→](svelte.md) |
| **TanStack Redact** | Use it when a Vite + React app's bundle budget is eaten by ~69 KB of React runtime the pages never lean on — one plugin swaps every React import for a ~23 KB synchronous re-implementation — not when the app needs concurrent features, a non-Vite build, or a license file (there is none yet). | D (6/6) | [→](tanstack-redact.md) |
| **Vue.js** | A progressive JavaScript framework for building user interfaces, created by Evan You. Known for its gentle learning curve, excellent documentation, and incrementally adoptable architecture. | A (6/6) | [→](vue.md) |

## What belongs here

The component model and rendering runtime you build UI on (React, Vue, Svelte, Angular, Lit) plus drop-in replacements for such a runtime (TanStack Redact). Routing, SSR and server code layered on top belong in `app-frameworks`; content and docs sites in `site-frameworks`; ready-made components in `web-ui/component-libraries`.
