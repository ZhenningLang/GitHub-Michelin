# python-tooling

> Category node. Python developer tooling — compilers, process injection, notebooks, async HTTP.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Cython** | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. | A (6/6) | [→](cython.md) |
| **pyrasite** | Use it when a stuck or leaking Python process cannot be restarted and you must run diagnostic code inside it via gdb — but injection can crash the target, ptrace-restricted hosts block it, and maintenance is near-dormant. | D (4/6) | [→](pyrasite.md) |
| **memory-analyzer** | Use it when, as a last resort, you need a one-shot per-type object snapshot and reference chains from a live Linux Python process via GDB — but Meta archived it (last code 2021, targets EOL 3.6/3.7), so try memray or tracemalloc first. | D (5/6) | [→](memory-analyzer.md) |
| **gophernotes** | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. | B (5/6) | [→](gophernotes.md) |
| **GRequests** | Use it when an existing synchronous requests codebase must fan out to hundreds of URLs concurrently with the smallest diff, via map() — but importing it monkeypatches the stdlib through gevent, which can collide with asyncio, multiprocessing or C extensions. | C (4/6) | [→](grequests.md) |
| **uv** | Use it when a Python project juggles pip, pip-tools, virtualenv, pyenv and pipx, and CI spends minutes installing — one binary fetches Python and locks cross-platform — but it manages only PyPI packages, and its roadmap belongs to Astral, which OpenAI announced it would acquire. | A (6/6) | [→](uv.md) |
| **curl_cffi** | Use it when a Python client gets blocked by TLS/JA3 fingerprinting and you need a `requests`-like API that impersonates a real browser — but it ships a native libcurl, so it isn't pure-Python. | A (6/6) | [→](curl-cffi.md) |
| **Google Colab CLI** | Use it when your GPU is a Colab plan and your code is a local repo or an agent's script — one command rents the Colab VM, runs the file, and releases it — but it rides Colab's web-session endpoints, is pre-1.0, Linux/macOS-only, and its hardware is tier-gated. | B (6/6) | [→](google-colab-cli.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Cython](cython.md) | ✅ | A (6/6) | Use it when a profiled hot Python loop needs near-C speed or you must wrap a C/C++ library — but it forces a C compiler and per-platform wheel build pipeline. |
| [pyrasite](pyrasite.md) | ✅ | D (4/6) | Gets code execution in a live interpreter's context, beyond what a debugger attach or sampler shows; costs real crash risk to the target, gdb and ptrace requirements, GPL-3.0, and one quiet maintainer. |
| [memory-analyzer](memory-analyzer.md) | ✅ | D (5/6) | Gets a heap view of a process you cannot restart or re-instrument; costs pausing every thread, needing ptrace and GDB on the host, and running archived code on an untested interpreter. |
| [gophernotes](gophernotes.md) | ✅ | B (5/6) | Use it when you want interactive Go cells in a Jupyter notebook for exploration or tutorials — but it's stalled since 2023 and runs an interpreter, not standard Go. |
| [GRequests](grequests.md) | ✅ | C (4/6) | Gets I/O concurrency without rewriting call sites as coroutines; costs gevent monkeypatching, import-order fragility, a single maintainer with slow releases, and requests' own limits such as no HTTP/2. |
| [uv](uv.md) | ✅ | A (6/6) | One fast tool and a universal lockfile replacing four or five, paid for with no native-library management, no Poetry plugin equivalent, and dependence on a single company's roadmap. |
| [curl_cffi](curl-cffi.md) | ✅ | A (6/6) | Use it when a Python client gets blocked by TLS/JA3 fingerprinting and you need a `requests`-like API that impersonates a real browser — but it ships a native libcurl, so it isn't pure-Python. |
| [Google Colab CLI](google-colab-cli.md) | ✅ | B (6/6) | Your existing Colab plan as a terminal/agent GPU runner (no new vendor or bill) — paid for with undocumented web-session endpoints, tier-gated hardware, idle reclamation and a pre-1.0 client. |
| (alternatives named across the pages) | 未收录 | — | Substitutes referenced in each page's Comparison. |

## What belongs here

Developer tooling for the **Python** ecosystem — compilers, debuggers/injection, kernels, HTTP helpers, and CLIs that run your Python on a remote notebook kernel.
