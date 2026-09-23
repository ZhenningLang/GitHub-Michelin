# function-calling

> 分类节点。主要职责是把自然语言请求变成受 schema 约束的工具/函数调用的一类模型与服务栈。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Functionary** | 只把当它开源 JSON Schema 函数调用的历史参考——它已废弃；生产环境请服务当前模型或走端侧。 | B（4/6） | [→](functionary.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Functionary](functionary.zh.md) | ✅ | B（4/6） | 早期开源函数调用模型的代表作（JSON Schema 工具、vLLM/SGLang 服务）——现已废弃，仅作模式来源。 |
| FunctionGemma（Google）/ 云端工具 API | 未收录 | — | 页面里点到的其他函数调用模型与 API——一个是模型卡，其余是托管服务，均非本索引收录的仓库。 |

## 什么该放这里

以**工具/函数调用**本身为主题的条目——从自然语言填充函数参数的模型、服务栈与 schema/grammar 契约。不含通用聊天模型或端侧运行时（见 `on-device-ml` / `llm-inference`），不含 agent 框架（见 `agent-frameworks`）。
