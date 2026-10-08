# code-editors

> Category node. Code editors and IDE extensions you write code in.
> ← back to [editors-and-runtimes](../INDEX.md) · root: [category route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **IdeaVim** | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. | A (4/6) | [→](ideavim.md) |
| **VS Code** | Use it when your team works across several languages and OSes and wants one editor whose language support and remote or container editing come from the extension ecosystem most tools target first — but the official build carries Microsoft telemetry and licensing. | A (5/6) | [→](vscode.md) |
| **Zed** | Use it when editor latency matters more than extension breadth and you want a native GPU-rendered editor with LSP, debugger, AI agents and live collaboration built in — but VS Code extensions don't run, it needs a working GPU driver, and collaboration requires Zed's service. | A (4/6) | [→](zed.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [IdeaVim](ideavim.md) | ✅ | A (4/6) | Use it when you live in a JetBrains IDE but want Vim motions, modes, and a `.ideavimrc` — but it's an emulation subset, power users will hit fidelity gaps. |
| [VS Code](vscode.md) | ✅ | A (5/6) | Cross-language breadth at zero cost, paid for with Electron's memory and startup overhead and dependence on Microsoft's marketplace terms for key extensions. |
| [Zed](zed.md) | ✅ | A (4/6) | Instant startup and built-in features, at the cost of a much smaller extension system, a GPU requirement, GPL-licensed source and only months of 1.x history. |

## What belongs here

Editors and IDEs themselves, and extensions that change how you edit inside one (keybinding emulation). Not the language runtimes your code runs on (see `runtimes-and-compilers`).
