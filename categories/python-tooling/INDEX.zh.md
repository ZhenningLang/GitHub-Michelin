# python-tooling

> 分类节点。Python 开发者工具——编译器、进程注入、notebook、异步 HTTP。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Cython** | 当你已 profile 出的 Python 热点循环需要逼近 C 的速度、或要封装 C／C++ 库时用它——但它会引入 C 编译器和按平台构建 wheel 的流水线负担。 | A（6/6） | [→](cython.zh.md) |
| **pyrasite** | 当你必须向一个无法重启、卡死或泄漏的运行中 Python 进程注入诊断代码时用它——但注入可能让目标崩溃，只当救火工具用。 | D（4/6） | [→](pyrasite.zh.md) |
| **memory-analyzer** | 当你需要经 GDB 对一个活的 Python 3 进程做一次性按类型内存快照时用它——但 Meta 已**归档**它（代码停在 2021，目标是 EOL 的 3.6／3.7），优先选 memray／tracemalloc 这类有维护的工具。 | D（5/6） | [→](memory-analyzer.zh.md) |
| **gophernotes** | 当你想在 Jupyter 笔记本里用交互式 Go 单元做探索或教程时用它——但它自 2023 年起停滞，且跑的是解释器而非标准 Go。 | B（5/6） | [→](gophernotes.zh.md) |
| **GRequests** | 当你想用 `map()` 以最小改动让现有同步 `requests` 代码并发时用它——但 gevent 会猴补丁标准库，可能与你的技术栈冲突。 | C（4/6） | [→](grequests.zh.md) |
| **uv** | 当你想要一个极速 Python 包管理器和项目工具，用单一 Rust 二进制和通用锁文件替代 pip、poetry 和 pyenv 时用它——但它仅约 3 年历史，依赖解析的某些边缘情况仍在完善。 | A（6/6） | [→](uv.zh.md) |
| **curl_cffi** | 当 Python 客户端被 TLS／JA3 指纹识别拦下、而你需要一个能伪装真实浏览器的 `requests` 风格 API 时用它——但它随包带原生 libcurl，并非纯 Python。 | A（6/6） | [→](curl-cffi.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Cython](cython.zh.md) | ✅ | A（6/6） | 当你已 profile 出的 Python 热点循环需要逼近 C 的速度、或要封装 C／C++ 库时用它——但它会引入 C 编译器和按平台构建 wheel 的流水线负担。 |
| [pyrasite](pyrasite.zh.md) | ✅ | D（4/6） | 当你必须向一个无法重启、卡死或泄漏的运行中 Python 进程注入诊断代码时用它——但注入可能让目标崩溃，只当救火工具用。 |
| [memory-analyzer](memory-analyzer.zh.md) | ✅ | D（5/6） | 当你需要经 GDB 对一个活的 Python 3 进程做一次性按类型内存快照时用它——但 Meta 已**归档**它（代码停在 2021，目标是 EOL 的 3.6／3.7），优先选 memray／tracemalloc 这类有维护的工具。 |
| [gophernotes](gophernotes.zh.md) | ✅ | B（5/6） | 当你想在 Jupyter 笔记本里用交互式 Go 单元做探索或教程时用它——但它自 2023 年起停滞，且跑的是解释器而非标准 Go。 |
| [GRequests](grequests.zh.md) | ✅ | C（4/6） | 当你想用 `map()` 以最小改动让现有同步 `requests` 代码并发时用它——但 gevent 会猴补丁标准库，可能与你的技术栈冲突。 |
| [uv](uv.zh.md) | ✅ | A（6/6） | 用 Rust 编写的极速 Python 包管理器；以单一工具加通用锁文件替代 pip、poetry、pyenv——但仅约 3 年历史，部分边缘情况仍在解决。 |
| [curl_cffi](curl-cffi.zh.md) | ✅ | A（6/6） | 当 Python 客户端被 TLS／JA3 指纹识别拦下、而你需要一个能伪装真实浏览器的 `requests` 风格 API 时用它——但它随包带原生 libcurl，并非纯 Python。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向 **Python** 生态的开发者工具——编译器、调试器/注入、内核、HTTP 辅助。
