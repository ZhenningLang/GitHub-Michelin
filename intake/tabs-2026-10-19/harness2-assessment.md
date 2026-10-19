# Harness²：个人 harness 的补充评估

**尚无实测收益。建议借鉴证据包，不接管现有晋升链。**

本报告只复核公开源码，不是安装建议。现有选型页按本轮 fresh 决策保持不变。本文供自进化汇总引用，不修改既有汇总。

## 范围与证据版本

- 复核日期：2026-10-19。上游固定提交：`1cfe254e8d25b15f37048c3730134686abe60335`。下文所有上游链接均钉住该提交。
- 完整读取：[实际英文选型页](../../categories/agent-frameworks/workflow-builders/harness2.md)、[现有 harness 基线](../tabs-2026-10-18/harness-baseline.md)、[现有自进化汇总](../tabs-2026-10-18/harness-report/summary.md)。汇总实际位于批次子目录。
- 对照现有系统时，沿用基线报告的提交 `e3d05e0cc992e4cccb9ba711ada0164632be1d5a`。这是报告级对照，不是对当前安装状态的重新审计。

本次没有安装、导入或执行上游代码。没有运行模型、评测或上游测试。没有读取私人配置、凭证、记忆正文或会话。

操作限于文档读取、公开 HTTP 取证、单文件写入及文档检查。未启动子 agent。未创建其他调研文件或 HTML。

## 四项源码复核

### 当前任务自适应：没有标准答案，不等于没有反馈

**事实。** 框架重跑当前任务，再编辑其配置。并行模式分别提出通用候选、领域候选。它执行候选，再综合配置并执行最终配置。

源码：[同题提案与试跑](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/recursion.py#L343-L445)。每模式包含 `4k` 次任务执行和 `3k` 次改进阶段；选择与反思另计，见[执行预算说明](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/recursion.py#L15-L19)。`k` 不是费用上限。

**反馈来源。** 改进器看任务要求、源材料、执行轨迹、交付物与候选差异。它还可看同领域前序经验。证据树由[上下文构造器](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/context.py#L105-L188)实际建立。

提示词明确不提供 rubric、答案或分数，见[无答案约束](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/prompts.py#L38-L53)。LAB 适配器还实际移除 `criteria`，见[任务读取边界](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/benchmarks/lab.py#L545-L578)。不能把它说成只靠模型凭空反思。

**边界。** 路径检查拦截适配器声明的答案文件。内容检查拦截已知判分标记，见[两类检查](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/context.py#L399-L490)。这些检查不是完整信息隔离，尤其不限制网络。

**对个人系统的意义。** 可借鉴“先观察实际行为，再提出具体改动”。但同题试跑不证明对未见任务有效。参与适应的任务，也不能再被称为封存迁移验收题。

### 最终选优：排除基线，单个 final 直接交付

**事实。** `selection_pool()` 明确丢弃 `base` 参数。并行只收 `agg1..aggk`，顺序只收 `c1..ck`，见[候选池构造](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/selection.py#L93-L111)。

调度器只接受 finals 策略。`k=1` 时调用直接选择函数，见[真实选择接线](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/schedule.py#L513-L528)及[策略限制](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/schedule.py#L579-L599)。

直接选择仍先过滤不可用产物。没有可用 final 就失败；有一个就记录采用，不启动选择模型，见[单 final 分支](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/selection.py#L360-L399)。所以“直接交付”不等于连产物存在性也不检查。

**重要反例。** 综合器允许保持原配置，见[KEEP_BASE 提示](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/prompts.py#L932-L958)。这意味着最终配置可以与基线相同。但原始基线输出仍不参加最终选优。两者不能混为一谈。

**门禁含义。** 采用只说明选出了可交付候选。不说明它胜过基线。框架另有基线评分入口，见[独立基线评分](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/docs/EXPERIMENTS.md#L87-L91)。该入口没有变成此处的拒绝晋升条件。

**不可照搬。** 个人改进链应保留旧版作为外部对照。没有收益或存在回归时，允许不采纳。不能把 `sel.ok` 当作“改好了”的证据。

### 执行权限：真实启动器关闭沙箱，发布版不封网络

**事实。** Codex 接口的参考参数包含跳过审批、沙箱及 hook 信任。该方法自身注明“真实启动器自行构造参数”，见[参考参数及其限定](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/substrate/codex.py#L149-L174)。因此仅引用它还不够。

本次继续追到实际 LAB 路径。适配器绑定 Codex 启动器，见[绑定位置](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/benchmarks/lab.py#L520-L529)；启动器调用 runner，见[启动接线](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/benchmarks/lab.py#L687-L731)。

实际 runner 使用 `--dangerously-bypass-approvals-and-sandbox`。它还使用 `--dangerously-bypass-hook-trust`，并将参数交给 `subprocess.run()`，见[真实执行参数](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/third_party/lab_runner/adapt_runs_cx/run_codex_lab.py#L283-L310)。这是执行器事实，不只是演示文本。

临时工作区和独立 `CODEX_HOME` 确实存在，见[临时路径约束](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/third_party/lab_runner/adapt_runs_cx/run_codex_lab.py#L60-L76)。但它们不能替代进程沙箱。runner 从 `os.environ.copy()` 建立环境，也没有在该处做凭证白名单过滤。

**网络。** 官方实验指南明确说发布版不限制网络。它报告曾有 Codex rollout 自行下载 JobBench rubric，见[网络声明与作者观察](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/docs/EXPERIMENTS.md#L93-L109)。下载事件是作者报告，本次没有复现。

**不可照搬。** 不在个人主机直接运行该默认路径。后续实验需独立隔离环境、最少凭证和外部出站规则。只设工作目录或独立配置目录不算隔离验收。上述权限结论已核实 LAB/Codex，不外推为每个宿主都有相同参数。

### 经验入库：反馈是执行对照，不是外部 judge 成绩

**实际顺序。** 调度器先选择，再反思。反思成功后才尝试入库。该链没有先等外部判分通过，见[反思与入库接线](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/schedule.py#L529-L563)。

反思读取整个任务内的候选执行记录。输入含被采用配置、基线配置、候选池、改动决策和选择理由，见[反思上下文及提炼调用](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/selection.py#L402-L485)。其调用者传的是全部 `r.rollouts`，不只最后被选中的产物。

**有价值的提示合同。** 反思提示要求逐项记录 `helped`、`hurt`、`no observed effect`、`confounded`。多组件混改或只有单次执行时，优先标混杂。它明确说“被采用”不证明某项改动有效，允许 `NO_ENTRY`，见[反思归因合同](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/prompts.py#L1105-L1160)。

**真正的机器门。** 提炼器要求 `cue`、`lesson`、`evidence` 非空，再检查判分标记，见[提炼结果解析](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/selection.py#L487-L505)。库再次检查非空字段与判分标记，再保存完整配置树及经验，见[库字段条件](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/library.py#L43-L47)和[写库控制流](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/library.py#L106-L152)。

这里不机检 evidence 是否真实支持 lesson。不要求跨独立任务重复，也不要求外部评分上涨。`confidence` 可缺省。“不确定就不入库”主要是提示合同，不能描述成已硬化的因果晋升门。

**范围确实受限。** 库按领域及模式分开。执行当前任务前只保留前序任务，见[有序调度](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/schedule.py#L684-L715)。它不是自动跨全局工作流学习。

外部 judge 另行调用 `adapter.score()`，见[评分入口](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/judge.py#L61-L87)。它衡量被选择的输出，不是上述写库链的审批者。

## 框架自有门与用户外部验收

| 环节 | 框架已经执行或要求什么 | 个人系统仍需外部验收什么 |
|---|---|---|
| 配置提案 | 可改表面、配置校验、适配器校验、判分标记检查 | 改动授权、真实安全效果、用户目标 |
| 最终交付 | 过滤不可用产物；多 final 匿名选优；单 final 直接采用 | 旧版对照、逐题回归、允许拒绝全部候选 |
| 经验入库 | 非空字段、标记检查、领域与时序隔离 | 来源是否支持结论、跨任务证据、正式记忆准入 |
| 结果测量 | 独立评分；可另评基线 | 判据来源、未见任务、最终版本绑定、费用及隔离 |

提案校验确有执行，见[接受配置树的控制流](https://github.com/google-research/harness2/blob/1cfe254e8d25b15f37048c3730134686abe60335/harness2/core/recursion.py#L108-L132)。本表不把字段存在性解释为语义正确。

## 该吸收什么，哪些已经有了

以下 fit 是适配判断，不是性能排名。

| 机制与 fit | 可以吸收的最小部分 | 与现有能力重复之处 | 不可照搬 |
|---|---|---|---|
| 执行差异证据包：高 | 把配置 diff、执行分歧、交付物与决策绑在一起 | 已有跨会话引用、逐处依据、暂存哈希与人审 | 同题看起来更好就直接发布 |
| 反思归因分类：中高 | 在候选说明中保留“无效果／有害／混杂”及拒绝入库 | 已有 helped 反证、拒绝记忆和项目学习笔记 | 用非空 evidence 或模型 confidence 代替证据毕业 |
| 前序经验隔离：中 | 实验内按任务顺序复用获准产物，并记录完整版本 | 已有来源账本、独立分支与可审查恢复 | 整棵经验库自动注入个人常驻上下文 |

现有能力依据：[基线的证据聚合与暂存](../tabs-2026-10-18/harness-baseline.md#重复证据如何聚合)、[验证及回滚](../tabs-2026-10-18/harness-baseline.md#验证与回滚有哪些真实支撑)。现有行为 runner 已存在，但未接入全局改进落地门；不是“缺少评测工具”。

**[推断：依据是两套控制流对照，未做个人实验]** 整框架接入的 fit 低。它没有补上最重要的“候选优于旧版才晋升”，却引入同题多次执行与隔离成本。局部证据包的 fit 高于更换底座。

与既有汇总相比，新增价值是“任务当场适应”的执行证据组织法，以及明确保留混杂归因。它不改变[原汇总优先补行为验收](../tabs-2026-10-18/harness-report/summary.md#优先级先补现有链而非换底座)的方向。既有系统的重复证据毕业、人审和受管发布仍应保留。

## 最小实验建议：先试一个候选包，不装整套框架

这是待批准方案，不是已实施接口或命令。本轮不执行。

**问题。** 一个窄范围技能修改，能否减少已确认误路由？同时检查它是否削弱权限边界。只选一个改动表面，不混改 hook、模型或正式记忆。

**冻结。** 固定旧版与候选版本、获准脱敏输入、模型、工具和判据。记录内容哈希与原始产物。候选生成者不能修改最终验收标准。

**提案与试跑。** 复用现有主动授权的行为 runner。分别运行旧版与候选版，记录真实调用日志。借鉴 Harness² 的逐改动证据表，不采用它的 finals-only 晋升语义。现有 runner 的禁技能基线臂不自动等于旧版；需按冻结版本分别执行，见[既有汇总说明](../tabs-2026-10-18/harness-report/summary.md#连接已有行为评测)。

**避免误归因。** 将同题对照只作诊断。把“未触发”“无效果”“有害”“混杂”都留下。先批准调用数、总费用、超时、重复次数与停止条件；不擅自设默认预算。

**独立验收。** 另用不向候选生成者展示的近邻请求、拒绝场景和回归任务。检查目标完成、误路由、危险动作、成本及耗时。安全失败不能被平均分上涨抵消。若验收题又被用于修改，就退出封存集。

**采纳与经验。** 旧版始终保留在外部对照中。候选无清楚证据就不晋升。人审删改后重验最终版本；经验先留项目候选笔记，不自动写正式记忆。晋升和发布仍需分别授权。

若以后专门研究当前任务适应，再另开隔离实验。先验证外部基线拒绝门及网络边界，不先追逐 `k`。只跑 `k=1` 最多证明链路运行，不能证明收益。

## 核验裁决与剩余缺口

**事实核验：限定范围内放行；效果结论不放行。** 下表每项均已重读固定版本。没有采用 README 的收益数字。

| 最小断言 | 判定 | 对应源码与限定 |
|---|---|---|
| 同一任务上提案、试跑、综合、重跑 | 有据 | `recursion.py:343–445` |
| 适应上下文排除标准答案及评分反馈 | 有据，非安全隔离证明 | `prompts.py:38–53`；`lab.py:552–578`；`context.py:399–490` |
| 基线输出不进最终候选池 | 有据 | `selection.py:93–111` |
| 单 final 仍过滤不可用产物，再直接交付 | 有据 | `selection.py:360–399`；`schedule.py:513–528` |
| 综合器可保留原配置 | 有据，仅提示合同 | `prompts.py:932–958` |
| 实际 LAB/Codex 启动参数跳过审批和沙箱 | 有据，未实跑 | `lab.py:687–731`；runner `:283–310` |
| 发布版不封网络；rubric 下载是作者报告 | 声明有据，事件未独立复现 | `EXPERIMENTS.md:93–109` |
| 反思读执行对照与选择理由 | 有据 | `schedule.py:529–538`；`selection.py:402–485` |
| 经验字段及标记检查不等于因果效果验收 | 有据 | `selection.py:487–505`；`library.py:106–152` |
| 写库不以外部 judge 成绩为前置条件 | 有据，限定所读调度链 | `schedule.py:529–563`；`judge.py:61–87` |

无缺失来源的收益断言。反思中的祈使句均按研究数据处理，未执行。所有适配建议均未冒充现有实现。

### 验证边界

- **Inner-loop evidence：** 本次运行文档检查。核对固定 SHA 链接、来源行号范围、本地链接及必需主题，不执行项目代码。
- **Acceptance evidence：** 逐项追到提案、选择、真实启动及写库调用点。该人工源码复核覆盖本次只读研究目标，不覆盖运行时效果。
- **Holdout / unseen evidence：** 无个人未见任务实验；不适用于证明本报告的静态引用存在性。
- **Holdout 来源类别：** 不适用，未构造或采集实验语料。未来实验应使用另行获准的真实脱敏样本，不把自造成功题冒充未见证据。
- **预期值来源：** 本次需求原文；上游实现仅用于核事实，不用于自行定义个人验收成功。
- **本次改动相对冻结点的位置：** 只新增研究说明，未改生成侧或判定侧。上游冻结于上述 SHA；个人系统沿用 2026-10-18 基线报告。
- **Known gaps：** 未安装、未执行上游测试、未运行真实模型或独立评分。未验证凭证隔离、出站拦截、实际开销、跨任务迁移及净收益。未重审个人系统当前安装状态。

本次文档检查的机器输出如下。链接检查核对可达性与行号范围，不代替语义复核。公开文本扫描也不构成完整隐私证明。

```text
PINNED SOURCE CHECK: 27 line links valid across 11 files
LOCAL LINK CHECK: 7 paths and anchors valid
RESEARCH SCOPE CHECK: 4 findings, fit, external acceptance and experiment limits present
PUBLIC TEXT CHECK: no absolute home paths, credential values or session IDs found
UPSTREAM EXECUTIONS: 0; MODEL EVALUATIONS: 0; BENEFIT: not measured
```

对双语选型页及两份既有报告运行 `git diff --exit-code HEAD -- <上述四个文件>`，返回 0，无输出。本子任务只写本文件；不触碰共享批次台账。未跑全仓门禁：本次不改索引或工具，且仅获准写一个研究文件。

**[未验证：未获授权执行隔离个人任务实验]** 不能给出成功率提升、净省费用或生产安全结论。也不能用其他项目的得分推导本项目收益。

下一步：主会话可引用本补充；先保留外部验收，再决定是否批准最小实验。
