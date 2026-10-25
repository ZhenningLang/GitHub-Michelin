# 2026-10-25 标签收录结果

**Stable Video Infinity 新增暂缓，未建页、保留标签。** 固定树191／319个blob与DiffSynth同源；常规许可文件与原样许可blob未保留，正文检索只覆盖已缓存的17个SVI文件。它有实质训练／推理代码，不能因论文拒收，也不据此裁定侵权。详见[待裁决依据](stable-video-infinity-proposal.md)。旧的[Open-Box专有产品与非公开候选](retained-decisions.md)继续暂缓；自有仓库跳过，身份不公开。

| 本批结果 | 数量 |
|---|---:|
| 新增正式项目 | 5 |
| 期限门控刷新／已有页免刷新 | 0／0 |
| 新增暂缓／既有暂缓复核 | 1／2 |
| 自有跳过／失败 | 1／0 |

| 新正式项目 | 决定性边界 | 本地选型页 |
|---|---|---|
| iris.c | 原生C图片推理；独立模型许可、GPU回退和提示历史要分开看 | [中文](../../categories/on-device-ml/local-image-generation/iris-c.zh.md) |
| ReAgent | 自备候选测试驱动重建；结构未知、命令信任和副本不等于等价证明或沙箱 | [中文](../../categories/dev-utilities/binary-analysis/reagent.zh.md) |
| Anima | 交互生物教学配图；引用指令与几何检查不证明科学事实 | [中文](../../categories/agent-skills/design/visual-artifacts/anima.zh.md) |
| Gemini API CLI | 已有助手的API工具，不是Gemini CLI底座；预览与真实成功分开 | [中文](../../categories/agent-tooling/harness-extensions/gemini-api-cli.zh.md) |
| HatchZip | 默认逐步销毁原包；恢复剩余条目不等于还原原包，RAR发布产物另有许可 | [中文](../../categories/dev-utilities/data-tools/hatchzip.zh.md) |

五项分别验证、提交后关闭匹配标签，期间复扫没有新公开队列。末次快照证明五组已完成仓库标签清空，三项暂缓与一项自有标签仍在。另观察到三个非目标URL较初始快照消失，原因未确定；只发出过上述五组已完成仓库的关闭请求，不把差异归因给用户或其它进程，也未擅自恢复。完整浏览器状态不变不能由这些快照证明，见[标签审计](tabs-audit.json)。

## Harness借鉴

本批没有新增 medium／high 接入建议。五个正式项目的局部实现只作 none／low 参考；SVI的张量误差回放也不是coding-agent RSI。仅对照2026-10-18固定基线，不重新断言今日缺口，不安装项目、不加载上游技能、不改个人配置、不宣称收益已实测。

## 横向比较选题池

| 当前分类项目数 | 最值得比较的问题 |
|---|---|
| 本地图像生成：4 | 原生C引擎、通用张量运行时和节点工作流，何时由模型覆盖、权重许可和内存决定？ |
| 可视化交付技能：7 | 科学取材、几何校验、浏览器审图和人审，哪些必须分别验收？ |
| Harness扩展：8 | 给已有助手增加命令面与替换助手底座，如何划分授权、格式和费用责任？ |
| 数据工具：11 | 预览、保留原始输入、可续跑与不可逆回收，怎样区分而不靠“安全”口号？ |

二进制分析另有三项，未达到四项选题阈值。本次将Ghidra、REA与ReAgent移入同级分类，保留原数据工具入口；1944页身份、日期、健康与正文保真，见[迁移证明](refactor-map.json)。

本批只覆盖已扫描公开项目，不扩收Diffusers、RetDec、Anatomy、Google Gen AI Python SDK、LLM、7-Zip、libarchive或PeaZip。no leftover Q&A。

原综合报告继续原址整合：旧127个身份加六个新候选，共133；129项有正式页，三项暂缓、一个历史自有跳过，仍按16类阅读。原127条介绍及四项版权警告保留。该总报告是本地阅读入口，不随 `git pull` 同步；本文件只是本批台账摘要，不是第二份全量报告。

验证与发布以[验证记录](verification.json)及本批PR的实时状态为准。上游安装、模型质量、性能、设备、崩溃恢复、完整清理与法律合规均未实测；索引门禁不替代这些验收。
