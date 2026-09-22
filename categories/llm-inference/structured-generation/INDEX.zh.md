# structured-generation

> 分类节点。约束解码器，让模型输出符合某个结构——JSON Schema、正则、上下文无关语法，或工具调用包装——而不是解析失败再重试。
> ← 返回 [llm-inference](../INDEX.zh.md) · 根路由：[分类路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **XGrammar** | 当你掌握模型的 logits、必须保证输出可解析——JSON Schema、正则、语法或工具调用——并且想要尽可能低的掩码延迟时用它；只调托管 API、或已在集成它的引擎上服务时不必用。 | B（6/6） | [→](xgrammar.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [XGrammar](xgrammar.zh.md) | ✅ | B（6/6） | vLLM/SGLang/TensorRT-LLM/MLC-LLM 内部默认的语法约束解码引擎：掩码近乎免费、语法前端最全，代价是一个 C++ 二进制依赖和 pre-1.0 的 API。 |

## 什么该放这里

主要职责是**约束模型能生成什么**的库与引擎——按 schema、正则、语法或工具调用结构做 token 掩码。不含服务引擎本身，即使它们内置了这类库（见 `serving-engines`）；也不含把语法模式当作附带功能的本地运行时（见 `local-runtimes`）。如果你的问题是编排多次生成而不是约束一次生成，那是框架层的事，不属于本节点。
