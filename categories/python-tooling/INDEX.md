# python-tooling

> Category node. Python developer tooling — compilers, process injection, notebooks, async HTTP.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cython** | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. | A (6/6) | [→](cython.md) |
| **pyrasite** | Use it when you must inject diagnostic code into a stuck or leaking live Python process you can't restart — but injection can crash the target, treat it as incident-only. | C (4/6) | [→](pyrasite.md) |
| **memory-analyzer** | Use it when you need a one-shot per-type memory snapshot of a live Python 3 process via GDB — but Meta **archived** it (last code 2021, targets EOL 3.6/3.7), so prefer a maintained tool like memray/tracemalloc. | D (5/6) | [→](memory-analyzer.md) |
| **gophernotes** | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. | D (3/6) | [→](gophernotes.md) |
| **GRequests** | Use it when you want to make existing synchronous `requests` code concurrent with minimal diff via `map()` — but gevent monkeypatches the stdlib and can collide with your stack. | C (4/6) | [→](grequests.md) |
| **uv** | Use it when you want an extremely fast Python package manager and project tool that replaces pip, poetry, and pyenv with a single Rust binary and universal lockfile — but it's only ~3 years old and some edge cases in dependency resolution are still being ironed out. | A (6/6) | [→](uv.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cython](cython.md) | ✅ | A (6/6) | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. |
| [pyrasite](pyrasite.md) | ✅ | C (4/6) | Use it when you must inject diagnostic code into a stuck or leaking live Python process you can't restart — but injection can crash the target, treat it as incident-only. |
| [memory-analyzer](memory-analyzer.md) | ✅ | D (5/6) | Use it when you need a one-shot per-type memory snapshot of a live Python 3 process via GDB — but Meta **archived** it (last code 2021, targets EOL 3.6/3.7), so prefer a maintained tool like memray/tracemalloc. |
| [gophernotes](gophernotes.md) | ✅ | D (3/6) | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. |
| [GRequests](grequests.md) | ✅ | C (4/6) | Use it when you want to make existing synchronous `requests` code concurrent with minimal diff via `map()` — but gevent monkeypatches the stdlib and can collide with your stack. |
| [uv](uv.md) | ✅ | A (6/6) | Extremely fast Python package manager written in Rust; replaces pip, poetry, pyenv with a single tool and universal lockfile — but only ~3 years old with some edge cases still being resolved. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Developer tooling for the **Python** ecosystem — compilers, debuggers/injection, kernels, HTTP helpers.
