# 二次标签收录与 Harness 调研更新

**两轮收录已在本地完成验收，按授权通过 PR 交付远端 main。** 合计新增 64 对双语页、14 个 fresh 页面；6 项待裁决、1 个自有项目跳过。没有安装上游项目，也没有修改你的 harness；实际合并状态以文末 PR 入口为准。

## 仍待你裁决的项目

六项沿用上轮 proposed，标签保留，本轮未偷偷降格为跳过，也未擅自收录。

| 候选 | 具体待决点 |
|---|---|
| breferrari/obsidian-mind | 复制技能的 MIT 版权与许可声明保留存在缺口；有独立运行时价值，等待补证。 |
| liseami/CCBaga | NOTICE 说复制树缺独立上游许可声明，再分发条款待确认；不等于已经证实无授权。 |
| JimLiu/baoyu-design | 提取、重打包产品内容的授权覆盖尚未证实；根许可证不能证明全部材料许可。 |
| Bennettxai/FounderOS | 与声明上游的来源及许可证保留存在差异；需核实复制时点许可或单独授权。 |
| dzhng/skills | 文件数与字节数得出不同复制占比，仍有工程技能；21 个工程技能不是 21 个原创技能。是否收录交你决定。 |
| 私有候选，身份不公开 | 未按公开开源分发处理；不发布其名称、实现或原始台账。 |

自有 `ZhenningLang/cpu-gpu-basic` 仍为 skipped。非 GitHub 标签和组织主页没有扩展处理。上述疑点不是侵权判决，也不是项目无价值的判断。

## 两轮怎样合在一起

首轮新增 61 对双语页，13 个已有页保持 fresh。二次扫描先发现两个新项目，之后用户又加入 Jasna。另有 1 个 fresh 页面：Harness² 已由独立 PR [#199](https://github.com/ZhenningLang/GitHub-Michelin/pull/199) 进入主干，不能重复计作本会话新增。

| 结果 | 首轮 | 本轮 | 两轮去重合计 |
|---|---:|---:|---:|
| 新增页对 | 61 | 3 | 64 |
| fresh，不改页 | 13 | 1 | 14 |
| sync 实质改写 | 0 | 0 | 0 |
| 待裁决 | 6 | 沿用 6 | 6 |
| 自有项目跳过 | 1 | 沿用 1 | 1 |
| 失败／非终态 | 0 | 0 | 0 |

合计 85 个不同仓库候选，78 个 done。实际 Chrome 对账仍开 7 个仓库：6 proposed、1 skipped；done 仍开为 0，未匹配新仓库为 0。Sphinx 的关闭命令未匹配标签，按当前浏览器状态确认它已不在打开集合，没有伪称本次关闭了它。

旧批次的原始分支保留本地，不推送。公开分支从安全主干出发，重放 61 个项目提交与独立分类提交；每个项目仍保留提交边界。6,835 个旧内容／资产文件对象已比较，仅两份分类 INDEX 因主干新增 Harness² 而有预期差异。

公开台账是原始台账的脱敏投影。新增提交 diff 已检查，不含该私有候选的身份。原始扫描与精确匹配材料只放在批准临时目录，没有通过更名工具参数来关闭不该关闭的标签。

对应证据：[公开重放映射](../public-replay.json)、[保真审计](../replay-audit.json)、[首轮逐项目验证](../../tabs-2026-10-18/per-repo-verification.json)。原证据的本地提交标识保留；新增 `public_content_commit` 指向可发布历史，避免伪称两者提交号相同。

## 自进化研究的新结论

**[推断：依据是固定源码与既有 harness 基线，未运行个人任务实验]** 主方向不变：先补独立行为验收，再考虑自动生成更多规则。新增 Harness² 证据强化了这个判断，而不是证明应该整套安装。

### Harness²：更有价值的是证据组织，不是自动晋升

它针对当前任务提案、试跑、综合再执行，改进器看轨迹与交付物，而不是完全没有反馈。其候选池排除原始基线输出；单个可用 final 直接采用，不能据此说“已胜过旧版”。综合器可以保留原配置，但不等于基线输出重新进入最终选择。

实际 LAB/Codex 执行路径跳过审批与沙箱；发布版也不封网络。这是已追到真实启动器的源码结论，不外推到所有宿主，也不把作者报告的 rubric 下载事件写成我们复现过的攻击。

经验反思要求区分“有帮助／有害／无效果／混杂”，允许不入库。机器检查的却主要是非空字段与判分标记，不证明 evidence 支持 lesson，也不要求外部 judge 先判改善。

| 适配优先级 | 可吸收机制 | 映射现有入口 | 不照搬的部分 |
|---|---|---|---|
| 高 | 配置差异、执行分歧、交付物与决策组成同一证据包 | `agent-harness-improvement` 的暂存与验证产物 | finals-only 选择和单 final 直收，不当成生产晋升门 |
| 中 | 保留“无效果／有害／混杂”的逐改动归因 | `assist-learn`、记忆候选说明 | 模型置信度或非空 evidence 不替代独立验收 |

页面：[Harness²](../../../categories/agent-frameworks/workflow-builders/harness-evolution/harness2.zh.md)。完整补充与固定源码行链：[harness2-assessment.md](../harness2-assessment.md)。已有页面按 fresh 不改日期；补充研究单独列出，未伪称重写选型页。

### 原有优先项继续保留

首轮 14 项中高适配清单继续可读：[机制与接入位置](../../tabs-2026-10-18/harness-report/batch.md#值得吸收的机制)。最优先的两项仍是 Penguin 的冻结实验与版本快照、Jiuwen 的最终实际产物重测。两者也都需要外部未见任务验收。

Headroom 的预览仍可能先调用模型；Atomic 的被引用奖励不等于事实正确；Hy 的强证据门限定新建 schema 路径。这些边界没有因评分、记忆增长或“自进化”命名而消失。首轮报告与独立复核保留全部限定，不重复扩写成新的实施清单。

## 新项目、验证与发布

### [Harness OSS](../../../categories/dev-utilities/ops-infra/harness-open-source.zh.md)：不是自进化框架

`harness/harness` 是从 Drone／Gitness 演变而来的 DevOps 平台，整合 Git、容器构建和制品库。对个人 harness 的适配为低：不建议引入整个平台，只把连接前地址校验和遥测出口分账当审查参考。

固定源码中仍有 Gitspace 密码解析器返回固定值、注册表排序方向进入 SQL 构造及部分下载路径未受统一网络策略保护的情况；本轮没有执行利用验证，不能据此量化可利用性。根 Apache 检测也不覆盖部分文件的 PolyForm 声明。故页面将它限定为可信隔离环境的评估候选，不建议原样公开部署。

### [Sphinx](../../../categories/agent-tooling/supervision-surfaces/sphinx.zh.md)：可选理解检查，不是安全审批

`parthh01/sphinx` 暂停原始 Git 操作，让独立于编码对话的模型考察人是否理解代码。判题前固定行为结果和因果最低标准；完成凭据绑定代码、目标与政策，操作继续前重新校验。这些机制可用于 `readable-diff-explainer` 的理解测验，适配为中。

**[推断：依据是固定实现的判据与凭据流程，未运行个人实验]** 值得借鉴预先固定判据，而不是直接安装全局 hook。它默认改全局 Git hook 配置，云路线会发送代码和答案；已有充分答案误判案例，且可绕过。它不替代代码审查、验证或发布授权，本轮没有修改现有 hook。

### [Jasna](../../../categories/media-processing/jasna.zh.md)：媒体修复，不是 Harness 机制

这是对移动马赛克区域做检测、跟踪、裁剪和时序修复的 GPU 应用。公开免费 BasicVSR++ 路径可独立复用，但官方包启动会初始化私有保护组件；不能把公开 AGPL 源码与整个官方发行包混为一谈。

源码中的流媒体模式监听全部接口且处理器没有认证检查；后处理命令和关机是可选动作，默认关闭，不能写成启动即执行。模型修复结果也不能作为原始像素的取证证明。页面保留这些边界，但未运行模型、视频、激活或安全利用验证。

对个人 harness 的适配为无：核心是媒体与 GPU 管线，通用队列或错误处理不足以构成新机制。本次照常收录，不因与自进化研究无关而丢弃。

本轮不安装第三方项目，也不运行其模型、技能、安装器或示例。不读取你的私人会话或凭证。

## 横向对比选题池

以下分类在本轮合并树中均有至少四个直接项目页。数量按文件实数，不凭总览印象；它们不是本轮追加实施任务。

| 分类 | 最值得比较的问题 |
|---|---|
| [应用记忆](../../../categories/agent-memory/app-memory/INDEX.zh.md) | 事实、经验与代码变更如何分账，什么才算学习成功？ |
| [编码宿主记忆](../../../categories/agent-memory/coding-agent-memory/INDEX.zh.md) | 自动捕获怎样约束误记和跨项目污染？ |
| [知识库](../../../categories/knowledge-base/INDEX.zh.md) | 检索片段和来源随版本变化后怎样保持可追溯？ |
| [Agent 服务](../../../categories/agent-frameworks/agent-runtimes/agent-services/INDEX.zh.md) | 协作、组织权限和进程隔离，谁真正提供哪一层？ |
| [终端编码助手](../../../categories/agent-frameworks/coding-agents/terminal-agents/INDEX.zh.md) | 工具成功与任务完成怎样分开验证？ |
| [视频制作](../../../categories/video-production/INDEX.zh.md) | 导演提示包与可执行管线分别省哪一步？ |
| [Apple 本地推理](../../../categories/on-device-ml/apple-local-inference/INDEX.zh.md) | MLX、Metal 与 Core ML 的覆盖和硬件成本怎样取舍？ |
| [有限答案决策](../../../categories/decision-models/INDEX.zh.md) | 概率、校准和拒答怎样接入而不变成模型授权？ |
| [工作流框架](../../../categories/agent-frameworks/workflow-builders/INDEX.zh.md) | 当前任务适应、离线选优与普通工作流构建有什么本质差别？ |

## 验证与交付边界

发布走功能分支与 PR，不直推 main、不强推。远端合并前保留逐项目提交及分类提交；若出现索引错误或内容回归，通过受审查的 revert PR 撤销对应改动，不覆盖其他人的提交。

发布入口：[此脱敏分支对应的 PR](https://github.com/ZhenningLang/GitHub-Michelin/pulls?q=is%3Apr+head%3Afeat%2Fintake-tabs-2026-10-18-public)。实际合并状态以该 PR 与远端 main 为准，不把本地检查当成远端已通过。

所有新页都要经过独立语义审查、主会话全库门禁和范围质量扫描，之后才提交并关闭对应标签。完整 HTML 阅读版由 Markdown 派生；上游来源不自动获得指令权。

本轮三项均已完成上述验收并独立提交。全库结构结果：`195 category nodes, 931 EN + 931 ZH pages, 0 errors, 1548 warnings.`；三项双语范围扫描均为 `No deterministic findings.`。工具测试复跑：`Ran 483 tests in 75.127s`，`OK`。告警并非零，本轮没有为消除既有告警放宽门禁。

最终树中没有分类溢出。新增三项的中文流程、机制与健康度 SVG 均渲染成 PNG 并由主会话目检；不是只证明文件存在。旧 16 对迁移的正文、生成块和资源保真已有独立复核。

证据：[计数及浏览器验收](../counts-checkpoint.json)、[三项新页及提交](../new-entry-evidence.json)、[两项新页审查](../new-entry-review.md)、[Jasna 审查](../jasna-review.md)、[公开重放安全审查](../publication-audit.md)、[全部候选吸收判断](../absorption-assessment.json)。

**Inner-loop evidence：** 结构／质量门禁及 483 项工具测试。**Acceptance evidence：** 真实标签对账、公开提交页接通、独立固定源码复核、生成图文与迁移保真。**Holdout / unseen evidence：** 不适用模型效果验收，本轮未实施个人改进实验。**Holdout 来源类别：** 真实捕获标签与固定上游源码。**预期值来源：** 用户需求和仓库 schema。**本次改动相对冻结点的位置：** 内容侧新增与路径迁移；不改工具、CI、schema 或个人 harness。

没有个人封存任务实验，因此不承诺 harness 成功率或费用改善。个人基线仍沿用首轮固定提交，不冒称重新审计今天的安装状态。
