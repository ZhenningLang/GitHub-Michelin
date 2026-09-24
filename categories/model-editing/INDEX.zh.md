# model-editing

> 分类节点。通过编辑模型已保存的权重来改变它的行为——消融（abliteration）及相关模型手术——而不是训练它。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Heretic** | 当一个对齐后的开源模型拒答那些对你的工作是正当的提示词，而你想自动把拒答方向消融掉、并带一个可量化的质量取舍时用它——一张显卡、不用训练数据、工具侧是 AGPL。 | B（6/6） | [→](heretic.zh.md) |
| **Remove Refusals with Transformers** | 想要最短、可读的原生 `transformers` 拒答移除配方时用它——两个 Apache-2.0 脚本供阅读与改造，没有优化器、没有导出、也不维护。 | C（5/6） | [→](remove-refusals-with-transformers.zh.md) |
| **abliterator** | 想自己写脚本、针对 TransformerLens 的 hook 逐步检查消融过程时用它——激活缓存、方向打分、改权重——代价是仓库自 2024-06 起停更。 | D（4/6） | [→](abliterator.zh.md) |
| **ErisForge** | 想要一个可 `pip` 安装、能对选定解码层消融或“增强”某种行为、能给拒答打分并保存模型的库时用它——代价是单一维护者、仓库没有 `LICENSE` 文件。 | "?"（2/6） | [→](erisforge.zh.md) |
| **deccp** | 只在你要它的中文审查关注时用它：一个 Qwen2 去审查概念验证，附手工核对的数据集与文章，作者明确不再支持。 | C（4/6） | [→](deccp.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Heretic](heretic.zh.md) | ✅ | B（6/6） | 对稠密／MoE 变换器模型做自动消融：约 200 轮 Optuna 试验在拒答率与 KL 散度之间取平衡，再由你挑一个帕累托点并导出；AGPL-3.0、单一维护者、需要显卡。 |
| [Remove Refusals with Transformers](remove-refusals-with-transformers.zh.md) | ✅ | C（5/6） | 最精简的 Apache-2.0 原生 `transformers` 参考：两个可读脚本算出拒答方向并正交化权重；没有优化器、没有导出，自 2025-11 起闲置。 |
| [abliterator](abliterator.zh.md) | ✅ | D（4/6） | 基于 TransformerLens 的库，做脚本化激活缓存、逐 hook 拒答方向与权重修补；MIT 之下完全可控，但自 2024-06 停更且没有模型导出。 |
| [ErisForge](erisforge.zh.md) | ✅ | "?"（2/6） | 可 `pip` 安装的库，对选定解码层消融或增强行为方向，带拒答打分与 Hub 保存；单一维护者、没有 `LICENSE` 文件、依赖钉版偏旧。 |
| [deccp](deccp.zh.md) | ✅ | C（4/6） | 面向 Qwen2 的中文审查去对齐概念验证，附整理好的数据集、评测脚本与文章；作者声明不再支持，自 2025-04 起闲置。 |

## 什么该放这里

通过编辑模型已保存的权重来改变其行为或体积的工具——方向消融（abliteration）、权重合并、量化手术。不含训练或微调（见 `llm-training`），不含推理运行时与服务引擎（见 `llm-inference` / `on-device-ml`）。
