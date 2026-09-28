# scheduling

> Category node. Function-execution timing utilities for client apps — debouncing, throttling, rate limiting, queuing and batching, plus framework hooks that expose the pending state.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Pacer** | Your app hand-rolls `setTimeout`/`clearTimeout` around search inputs, autosave and scroll handlers, and you want typed, stateful, cancelable debouncing/throttling/rate-limiting/queuing/batching with sync and async variants — not a server-side quota. | A (6/6) | [→](tanstack-pacer.md) |

## Comparison matrix

| Project | Patterns | Frameworks | Reactive state | License |
| --- | --- | --- | --- | --- |
| TanStack Pacer | debounce, throttle, rate-limit, queue, batch — each in sync and async form | vanilla, React, Preact, Solid, Angular (Vue/Svelte unported) | yes, via TanStack Store; `pacer-lite` drops it for bundle size | MIT |

## What belongs here

Libraries that decide *when* a function runs inside a client application: call-rate control (debounce/throttle/rate-limit) and call arrangement (queue/batch), including the framework hooks around them. Broker-backed or distributed job systems belong in [task-queue](../../task-queue/INDEX.md); DAG orchestrators in [workflow-orchestration](../../workflow-orchestration/INDEX.md); rate limits enforced against your API on the server belong to the backend stack, not here.
