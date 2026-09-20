# llm-inference

> 分类节点。高性能 LLM/模型推理与服务引擎，以及 AI 系统语言。
> 按**引擎服务谁**拆成两个子分类：在服务端硬件上服务大量并发 API 请求，还是在用户自己的机器上服务单个用户。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 子分类

| 子分类 | 何时进入 | 路由 |
| --- | --- | --- |
| **Serving Engines** | 你要把模型放到服务端 GPU 后面以 API 形式暴露，需要批处理、前缀缓存或自动扩缩容时。 | [→](serving-engines/INDEX.zh.md) |
| **Local Runtimes** | 你要在笔记本、台式机或单机上给自己跑模型，只要它在本机可用时。 | [→](local-runtimes/INDEX.zh.md) |

## 对比矩阵

| 选项 | 类型 | 一句话取舍 |
| --- | --- | --- |
| [Serving Engines](serving-engines/INDEX.zh.md) | 子分类 | vLLM、SGLang、TensorRT-LLM、LMDeploy、TGI、Ray Serve、BentoML、Modular——用 GPU 级运维代价换吞吐与并发。 |
| [Local Runtimes](local-runtimes/INDEX.zh.md) | 子分类 | llama.cpp、Ollama、Magnitude、omlx、MTPLX——用单用户规模上限换零运维的本地推理。 |

## 什么该放这里

主要职责是 **LLM/模型推理与服务**的引擎与系统语言。不含端侧/边缘运行时（见 `on-device-ml`）、不含 LLM 微调（见 `llm-training`）。按规模选子分类：服务端并发（`serving-engines`）或单用户本地执行（`local-runtimes`）。
