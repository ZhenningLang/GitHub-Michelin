# keyboard-shortcuts

> Category node. Keyboard shortcut libraries for web apps — bind key combinations and sequences to actions, handle the Cmd/Ctrl platform split and text inputs, record user rebindings and display shortcuts.
> ← back to [web-ui](../INDEX.md) · root: [category route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **TanStack Hotkeys** | Hand-written `keydown` checks keep breaking — Cmd+S opens the browser save dialog on Mac, single-key shortcuts fire while users type, recorded rebindings never match again — and you want typed `Mod+S` bindings, sequences, a recorder and display formatting with adapters for React, Vue, Angular, Solid, Svelte, Preact and Lit. | B (6/6) | [→](tanstack-hotkeys.md) |

## Comparison matrix

| Project | Frameworks | Scope model | Pick it over the rest when | License |
| --- | --- | --- | --- | --- |
| TanStack Hotkeys | React, Preact, Vue, Angular, Solid, Svelte, Lit, vanilla | element `target` + per-registration `enabled`, singleton manager with conflict warnings | you need typed bindings, physical-key support, recording and display helpers, or non-React adapters — and can absorb alpha 0.x churn and ESM-only packages | MIT |

## What belongs here

Libraries that listen for keyboard input in a web page and dispatch shortcuts: key-combination parsing, sequences, platform modifier mapping, scoping, shortcut recording and display. Command-palette UIs belong in `component-libraries`; OS-level global hotkey daemons are not front-end libraries.
