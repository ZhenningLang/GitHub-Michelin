# healthcare-ai

> 分类节点。你自己运行的临床文本智能——在自有硬件上做医学实体抽取与 PHI/PII 去标识化，服务于不能离开网络的数据。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenMed** | 当临床笔记必须在患者数据绝不出网的前提下产出带类型实体与脱敏副本时用它——代价是每个模型都要在你自己的语料上验证，且发布节奏系于一人。 | B（5/6） | [→](openmed.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenMed](openmed.zh.md) | ✅ | B（5/6） | 本地优先的临床 NER + PHI 去标识化 SDK，2,266 行模型注册表横跨 CPU/CUDA/MLX/ONNX/移动端；模型须自验，单人发布节奏下要锁版本。 |

## 收录范围

主题必须是**临床／医学文本与健康数据**的软件：笔记实体抽取、PHI/PII 去标识化、FHIR/HL7 互操作、表型与编码管线，且要能在自有硬件上运行。不含无医学模型的通用 PII 框架（Presidio 一类），不含文档 OCR 或 PDF 解析（见 [ocr](../ocr/INDEX.zh.md) 与 [document-parsing](../document-parsing/INDEX.zh.md)），不含通用推理运行时（见 [on-device-ml](../on-device-ml/INDEX.zh.md)），也不含托管医疗 NLP API（它们不是仓库）。
