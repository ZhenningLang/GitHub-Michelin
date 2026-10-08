# python-tooling

> 分类节点。Python 开发者工具——编译器、进程注入、notebook、异步 HTTP。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Cython** | 当你已 profile 出的 Python 热点循环需要逼近 C 的速度、或要封装 C／C++ 库时用它——但它会引入 C 编译器和按平台构建 wheel 的流水线负担。 | A（6/6） | [→](cython.zh.md) |
| **pyrasite** | 当一个卡死或漏内存的 Python 进程不能重启、你必须经 gdb 在它内部执行诊断代码时用它——但注入可能让目标崩溃，限制 ptrace 的主机会挡住它，维护也已近休眠。 | D（4/6） | [→](pyrasite.zh.md) |
| **memory-analyzer** | 当你万不得已、要经 GDB 给一个运行中的 Linux Python 进程拍一次按类型的对象快照和引用链时用它——但 Meta 已归档它（代码停在 2021，目标是已 EOL 的 3.6/3.7），先试 memray 或 tracemalloc。 | D（5/6） | [→](memory-analyzer.zh.md) |
| **gophernotes** | 当你想在 Jupyter 笔记本里用交互式 Go 单元做探索或教程时用它——但它自 2023 年起停滞，且跑的是解释器而非标准 Go。 | B（5/6） | [→](gophernotes.zh.md) |
| **GRequests** | 当你想以最小改动、用 `map()` 让一套现有同步 `requests` 代码并发扇出到几百个 URL 时用它——但一 import 它就会经 gevent 给标准库打猴子补丁，可能和 asyncio、多进程或 C 扩展冲突。 | C（4/6） | [→](grequests.zh.md) |
| **uv** | 当 Python 项目要同时摆弄 pip、pip-tools、virtualenv、pyenv、pipx，CI 每次安装要几分钟时用它——一个二进制就能装 Python、出跨平台锁文件——但它只管 PyPI 包，路线图归 Astral，而 OpenAI 已宣布收购 Astral。 | A（6/6） | [→](uv.zh.md) |
| **curl_cffi** | 当 Python 客户端被 TLS／JA3 指纹识别拦下、而你需要一个能伪装真实浏览器的 `requests` 风格 API 时用它——但它随包带原生 libcurl，并非纯 Python。 | A（6/6） | [→](curl-cffi.zh.md) |
| **Google Colab CLI** | 当你的 GPU 来自 Colab 套餐、代码却在本地仓库或 agent 写的脚本里时用它——一条命令租下 Colab 虚拟机、跑完文件再释放——但它依赖 Colab 网页会话接口，尚在 1.0 之前，只支持 Linux／macOS，硬件按档位限制。 | B（6/6） | [→](google-colab-cli.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Cython](cython.zh.md) | ✅ | A（6/6） | 当你已 profile 出的 Python 热点循环需要逼近 C 的速度、或要封装 C／C++ 库时用它——但它会引入 C 编译器和按平台构建 wheel 的流水线负担。 |
| [pyrasite](pyrasite.zh.md) | ✅ | D（4/6） | 换来在活解释器上下文里执行代码的能力，比调试器 attach 或采样器看得更深；代价是目标真有崩溃风险、需要 gdb 和 ptrace、GPL-3.0，以及一位基本沉默的维护者。 |
| [memory-analyzer](memory-analyzer.zh.md) | ✅ | D（5/6） | 换来对一个不能重启、不能补埋点的进程看到堆内情况；代价是暂停所有线程、主机要放开 ptrace 和 GDB，并在没测过的解释器上跑一份已归档代码。 |
| [gophernotes](gophernotes.zh.md) | ✅ | B（5/6） | 当你想在 Jupyter 笔记本里用交互式 Go 单元做探索或教程时用它——但它自 2023 年起停滞，且跑的是解释器而非标准 Go。 |
| [GRequests](grequests.zh.md) | ✅ | C（4/6） | 换来不把调用点改写成协程就有的 I/O 并发；代价是 gevent 猴子补丁、import 顺序很脆、单人维护且发版慢，还继承 requests 的局限（比如没有 HTTP/2）。 |
| [uv](uv.zh.md) | ✅ | A（6/6） | 一个快速工具加通用锁文件替掉四五个工具；代价是不管原生库、没有 Poetry 插件的替代品，路线图依赖单一公司。 |
| [curl_cffi](curl-cffi.zh.md) | ✅ | A（6/6） | 当 Python 客户端被 TLS／JA3 指纹识别拦下、而你需要一个能伪装真实浏览器的 `requests` 风格 API 时用它——但它随包带原生 libcurl，并非纯 Python。 |
| [Google Colab CLI](google-colab-cli.zh.md) | ✅ | B（6/6） | 把已有的 Colab 套餐变成终端／agent 能用的 GPU 执行器（不多供应商、不多账单）——代价是未公开的网页会话接口、按档位限制的硬件、空闲回收和 1.0 之前的客户端。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

面向 **Python** 生态的开发者工具——编译器、调试器/注入、内核、HTTP 辅助，以及把你的 Python 送到远程 notebook 内核上跑的 CLI。
