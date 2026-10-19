# 自进化建议：只读事实核验

## 复核裁决（当前有效）

**放行：原阻断三项均已关闭。** 放行限静态机制报告与适配建议，不证明个人 harness 收益，也不授予安装、外发或自动写配置权限。

复核日期：2026-10-18 UTC。已重读[修订正文](harness-report/summary.md)与[补充运行证据](baseline-verification.txt)，并只读核对两份完整原始日志。未重跑测试，未修改正文或 HTML，未重触碰被拒查询。

### 原阻断项的复核

| 初审阻断项 | 当前证据 | 复核裁决 |
|---|---|---|
| 工具测试成绩缺原始日志 | 正文第 110 行引用补充证据；原始测试日志确含 `Ran 483 tests in 27.062s` 与 `OK`。两份完整日志的 SHA-256 均与补充证据一致。 | 已关闭。确认已有运行输出，不是本次重跑，也不是上游框架测试。 |
| Hy 证据门范围过宽 | 正文第 60 行明确写 System 2 新建 schema 门，并说明其他证据检查仍存在；第 62 行附开关与校验源码。 | 已关闭。与初审固定源码证据一致。 |
| Atomic 防自证范围过宽 | 正文第 37 行限定姓名等受支持字段，并明确不是所有笔记的真实性保证；第 62 行附姓名约束源码。 | 已关闭。不再承诺普遍防止记忆幻觉。 |

### 运行证据与出处层级

**直接核验的事实：** 门禁原始日志含 `0 errors, 1450 warnings`，反向索引检查确认报告与页面一致。测试原始日志含 483 项测试完成与 `OK`。不能将零错误写成零告警。

| 原始日志文件名 | 本次计算的完整文件 SHA-256 | 对照结果 |
|---|---|---|
| `intake-2026-10-18-baseline-gates.log` | `0bee9a535d20213cd412a83d88ae7a2487f646237e338fc39af94c74bc432924` | 与补充证据一致 |
| `intake-2026-10-18-baseline-tests.log` | `686bac8ab320294ef567aaa4b32e5d68bbd22680720263995463f481b20e0fbc` | 与补充证据一致 |

**执行者记录：** 补充证据将运行绑定到索引提交 `49cf44bd3ce9d5afa82c16668dcc1ffb3db4faf4`，并记录仅台账、计划和 worker 合同有改动。它还记录 `make gates=0; make test=0`。

这些提交、工作树和进程退出码信息来自执行者记录，不是原始输出日志自带的执行环境快照。本次核验未复原历史工作树，也不声称从日志文本独立读出了退出码。该出处层级已明确，不再构成原先“未见原始运行输出”的阻断。

测试日志还含迁移与 HTTP 错误字样。本次仅确认这些文字存在，不将其推断为真实上游事故，也未按日志中的示例命令执行动作。

### 其他限定与收益检查

正文第 40 行已补完整队列名，并承认其他提示和记忆写入路径。第 46 行已限定 scoreboard 读取服务、题目级汇总和测试源码断言，明确未运行测试或复现攻击。

正文第 54 行已限定默认失败学习模式。第 76 行已区分禁用技能基线臂与旧版／新版对照。单 harness 留出为零的限定仍保留，未扩大到 Jiuwen 的所有引擎。

**收益裁决：** 未发现新增无证据收益承诺。后续实验仍被写成建议，未作为已经实现的效果。没有需要继续修改正文的事实阻断项。

### 本轮验证与停止位置

- **Inner-loop evidence：** 本次只读计算两份完整日志哈希，机器输出两条 `LOG HASH MATCH`；核对摘录存在于原始日志。
- **Acceptance evidence：** 对照修订正文，第 37、60、110 行分别消除原三项阻断；正文与 HTML 未由本核验修改。
- **Holdout / unseen evidence：** 不适用，未做模型收益实验。**Holdout 来源类别：** 不适用。**预期值来源：** 原核验意见、修订正文、原始日志与固定源码。
- **本次改动相对冻结点的位置：** 仅更新核验侧文件。复核正文的 SHA-256 为 `0a66d735689f232eacdb37c1ad87e33dfca563f388ae055f05386c4997de5f7b`。
- **Known gaps：** 执行环境绑定仍为执行者记录；部分历史行为仍为报告转述。未验证 HTML、个人任务泛化、实际成本或安装后效果。这些不属于本次放行范围。

下一步：本次事实核验停止。后续交付沿用上述范围，不把工具基线通过外推为框架有效。

## 初审历史（已归档）

以下保留初审时的结论、旧版行号与证据缺口。它们不是当前待办；当前裁决以上方复核为准。

### 初审核验裁决

**阻断当前版本的无保留放行。** 需补一项运行证据，并收紧两处适用范围。四项重点源码判断成立，不应反向夸大为整个框架都不可信。

核验对象：[建议正文](harness-report/summary.md)。来源为同批[上游报告](evolution-evidence.md)与[现有机制报告](harness-baseline.md)，另只读固定提交源码。取用日期：2026-10-18 UTC。

本次未改目标正文或 HTML。未运行上游代码、测试、会话扫描或模型。未读取或检索被拒绝的 Hy-Memory 下载缓存，也未重新读取该次被拒搜索针对的 System 2 writer。

源码能证明分支与合同的设计。测试源码只能证明存在断言。本核验不把源码、测试文件或子任务自述当作已经执行的实验。

## 初审历史：必须处置的三项

| 正文位置 | 问题与判定 | 最小处置 |
|---|---|---|
| 第 108 行 | **标注缺失，运行证据不足。** 两份指定报告均未提供所述 `make gates` 原始输出，也没有 `Ran 483 tests in 27.062s` 的原始运行记录。现有机制报告还明确声明未运行测试。这不证明正文记录是假的，只表示本次无法独立核验。 | 引用已有机器日志，并绑定被测提交与工作树状态。若无法提供，删除精确运行成绩，或标明“据执行者记录，核验者未见原始输出”。不要为本核验运行上游测试。 |
| 第 60 行 | **有据，但缺少适用范围。** 默认关闭的是 System 2 新建 schema 的证据门，不是整个 Hy-Memory 的所有证据检查。[开关][hy-defaults]、[校验][hy-gate] | 明写“System 2 新建 schema 的强证据门”。保留“启用后才检查来源要求”，不得概括成“默认没有任何证据治理”。 |
| 第 37 行 | **来源不支持广义表述。** “防止旧幻觉为新记忆自证”若覆盖所有记忆，超出证据。已读实现特指姓名来源，并明确称检查规则狭窄。[来源约束][atomic-ground] | 将此处限定为“姓名等受支持字段的来源约束”。若表达的是未来目标，写成建议，并说明不能保证所有笔记真实。 |

第三项位于“吸收机制”列。若作者仅意指设计原则，应明确标成原则，而非已有防护的普遍效果。

## 初审历史：四项重点与范围

### Jiuwen：内部留出被置零

**事实：限定单 harness 引擎后成立。** 构造器先要求 `backend='single_harness'`，再覆盖 `candidate_holdout_cases=0`。[实现][jiuwen-engine]

专项测试传入 1，却断言最终为 0。它还断言三题全部进入 source 批次。[测试源码][jiuwen-test] 本次未执行此测试。

正文第 34、48 行已经限定单 harness。第 48 行还明确允许外部封存验收，范围正确。无需把它改成“Jiuwen 所有引擎都没有 holdout”。

**推断边界：** 不能用参与选优的同批题证明未见任务收益。该判断针对证据能力，不是断言模型实际一定过拟合。

### Penguin：汇总读取信任文件

**事实：当前 scoreboard 读取路径成立。** 服务从 `scoreboard.yaml` 取值。`toCase()` 与 `toEvaluation()` 校验结构、数值范围等，但不按子运行重算汇总。[读取实现][penguin-service]

测试文件先写入子运行 80、82和题目分数 80.2，再断言读取结果为 80.2。这个数字是题目级汇总，不是整个 evaluation 的总分。[测试源码][penguin-test]

默认优化协议要求 agent 计算并填写均值，还明确禁止另加一致性复算。[默认协议][penguin-protocol] 因此“模型填写汇总”在这条默认协议下有据。

正文第 46 行成立。建议把“服务端”写成“scoreboard 读取服务”，并注明“测试源码断言”。不得改写为“任意输入均不校验”“所有评价器都信任假分”或“已经复现攻击”。

### Headroom：预览不等于不外发

**事实：默认失败学习链成立。** CLI 先扫描，再调用分析器，最后才向 writer 传入 `dry_run=not apply`。[调用顺序][headroom-cli]

分析器会把摘要送入所选模型后端。摘要可含用户文字、工具调用和错误片段。API 分支将摘要放入请求消息。[分析][headroom-analyzer]、[摘要字段][headroom-digest]、[请求][headroom-api]

因此，dry-run 只挡住这条 writer 写盘链，不能挡住此前分析。云端外发是条件性的；无数据、无分析触发条件或不同后端不能一概而论。

正文第 54 行用了“云后端可能”，没有宣称所有预览必然外发，成立。建议补“默认失败学习模式”。`--verbosity` 是另一条链，默认不用 LLM；指定 `--llm-judge` 才创建模型裁判。[模式分支][headroom-cli]

写全局文件也有条件。Claude writer 在 home 项目或显式目标下可写全局入口；普通项目默认写个人项目文件。[目标解析][headroom-writer] 不能把表中“不照搬直接 apply 全局规则”读成默认就写全局。

### FounderOS：只更新 Q 的是特定队列

**事实：限定 `ImprovementTaskQueue.apply()` 后成立。** 函数以 `Impact * 10` 生成奖励，调用 `UpdateQValue()`，成功后返回。`Process()` 随后把任务标成 Applied。[队列完整实现][founder-queue]

这不等于 FounderOS 没有其他写入路径。另一个 accumulator 会写用户偏好和 self-improvement block；提示执行器也会生成有到期时间的 hint。[其他写入][founder-block]、[提示执行器][founder-actuator]

正文第 40 行已经写“改进队列”，未说所有 apply 都如此。建议补完整队列名以消歧，不属于已确认的全项目错误。Applied 状态不能单独证明用户目标改善，判断成立。

## 初审历史：逐条断言核验表

表中“报告转述”指本次读到了来源报告，但未逐项重读其原始实现。它不是第二份独立实验。

| 正文位置与最小断言 | 判定 | 来源与核验层级 | 限定或处置 |
|---|---|---|---|
| 5：结论来自源码，不是效果实测 | 有据，范围声明 | 两份报告均明确未执行效果实验 | 不因此证明执行历史已被独立审计。 |
| 9：已有聚合、暂存、裁决与分支落地 | 有据 | 现有机制报告第 19–31、79–91 行；补读固定基线的落地函数 | 不等于已证明这些机制有效降低摩擦。 |
| 9：默认落地校验不强制行为优胜 | 有据 | 固定基线 `ahi_stage.py:693–743` | 默认命令为结构校验；允许注入验证命令，不宜说“永远只能结构校验”。 |
| 11：三项机制最值得吸收 | 标注正确 | 正文已标适配推断、未做任务实验 | 属于建议，不是性能排名。 |
| 19：Atomic、Hy 主要维护记忆 | 有据 | 上游报告第 165–235 行；补读 Atomic 写入及 Hy README | 不否认上游存在其他产品或训练工作。 |
| 20：Headroom 从失败生成规则 | 有据 | [CLI][headroom-cli]、[分析器][headroom-analyzer] | 限失败学习模式。 |
| 21：Penguin、Jiuwen 可基准选优 | 有据 | [默认协议][penguin-protocol]、[单引擎][jiuwen-engine] | 不据此推出泛化。 |
| 22：Founder 有独立 claim/fact 子系统 | 有据 | [事实晋升模块][founder-facts] | 该模块允许 policy 自动晋升，不等于逐条独立事实核验。 |
| 24：本批没有个人环境在线训练权重证据 | 有据，有限否定 | 上游报告第 223–225、328–331 行 | 只表示所读范围未发现，不是全仓库不存在训练。 |
| 24：Hy 发布训练后模型 | 弱支撑 | [上游 README 声明][hy-readme]；未核权重或论文 | 建议写“上游称已发布”。不能推导训练效果。 |
| 26：四个初筛项目不属于本题 | 有据，报告转述 | 上游报告第 33–47 行及对应固定提交引用 | 是任务相关性归类，不是拒绝收录理由。 |
| 30：优先级不是性能排名，收益待实验 | 标注正确 | 明确限制，无效果数据 | 保留。 |
| 34：最终筛选产物需要重测 | 有据 | [单引擎的 selected replay 与晋升分支][jiuwen-promote] | 产物未变化时复用此前全量结果；不是无条件额外跑一次。 |
| 34：已知成功不能退步 | 有据 | 同上，受保护题与全局晋升分支 | 是程序门的设计，不是已运行成功的结果。 |
| 34：队员经验会自动保存共享库 | 有据 | [队员 provider][jiuwen-team] | 必须启用 skill evolution 且配置库；不能省略启用条件而说所有队员永远自动写。 |
| 35：默认协议冻结题集、快照与单候选 | 有据 | [默认协议][penguin-protocol] | 主要是 agent 遵循的 skill 合同，不全是独立状态机硬门。 |
| 35：同题高分晋升，后台另有直接改 skill | 有据 | [默认协议][penguin-protocol]、[持续学习 hook][penguin-hook] | 两条路径不同；hook 输出写入提示，不代表本轮实际发生写入。 |
| 36：多宿主适配、提案及 token 估算 | 有据 | [CLI][headroom-cli]、[分析器][headroom-analyzer] | 估算非实测收益；部分循环权重也使用程序统计，不能说全是凭空估计。 |
| 37：旧幻觉不能自证 | 来源不符，广义范围 | [Atomic grounding][atomic-ground] | 需限定姓名等受支持字段，见必须处置项。 |
| 37：正文与标签是不同变更类型 | 有据，报告转述 | 上游报告第 169、185–189 行 | 标签变更不能夸大成任意正文或代码改写。 |
| 38：Hy 保存精确 diff 与版本关系 | 有据，有限支撑 | [diff 链职责][hy-chain] | 本次直接读到设计说明；不可变性的完整实现仍依赖来源报告，未做运行验证。 |
| 38：同批交叉链接不是独立证据 | 有据，报告转述 | 上游报告第 219–221 行 | 本次未重读相关 writer；不得把转述写成本次独立复核。 |
| 40：队列 apply 只更新 Q | 有据 | [完整队列][founder-queue]，另读[实际 block 写入][founder-block]交叉限定 | 仅该队列，非全产品。 |
| 40：hint 有 TTL | 有据 | [提示执行器][founder-actuator] | 不等于所有持久记忆均会到期。 |
| 46：80、82不被服务端重算为81 | 有据 | [读取实现][penguin-service]及[测试源码][penguin-test] | 题目级汇总；未执行测试。 |
| 48：有判分、回归和安装回滚 | 有据，部分报告转述 | 单引擎源码；安装部分见上游报告第 101–107、123 行 | 安装测试是源码证据，不是本轮回滚实测。 |
| 48：单引擎内部 holdout 为零 | 有据 | [构造器][jiuwen-engine]及[专项测试][jiuwen-test] | 不涵盖所有引擎；不排除外部验收。 |
| 54：dry-run 不阻止前置模型分析 | 有据 | [顺序][headroom-cli]及[API 请求][headroom-api] | 不代表每次运行必然外发。 |
| 56：已有材料范围、服务商确认与脱敏要求 | 有据，报告转述 | 现有机制报告第 43–45、181–185 行 | 流程合同不等于每次执行都已遵守。 |
| 60：Atomic 将答案采用记忆作为正票理由 | 有据 | [投票提示][atomic-vote]第 68–77 行 | 仍有负票条件；不是“只看使用、永不负票”。 |
| 60：Hy 强证据门默认关闭 | 有据，但范围缺失 | [System 2 schema 开关与函数][hy-gate] | 需限定新建 schema。 |
| 62：错误信息可能因使用而强化 | 标注正确 | 已写奖励依据与未做污染实验 | 是风险推断，不是已发生事故。 |
| 70：清单冻结，判卷重新取正文 | 有据 | 补读固定基线的 `ahi_sources.py:184–230` 与 `ahi_judge.py:466–492` | “重判可能漂移”是推断；本次未复现数据增长。 |
| 74：runner 读调用日志，支持基线与留出 | 有据 | 补读固定基线 `runner.py:17–71,97–130,834–880,965–1002` | 自带 baseline 臂禁用技能，不自动等于旧版对新版；支持样本类别不等于独立性已证明。 |
| 74：runner 不能自动证明所有工作流收益 | 有据，范围限制 | 同上，默认路由与受支持输出判据 | 正文没有宣称全能。 |
| 78：人工筛掉修改后产物可能变化 | 标注正确，条件判断 | 现有机制报告第 79–89 行；源码只重放接受块 | “可能”不是声称本次实际发生变化。 |
| 84：公开讨论过的题不能再作封存验收 | 有据，方法边界 | 题目已在本页显式给出 | 仍可作诊断与回归，不必废弃。 |
| 86–90：小实验与回退建议 | 建议，不作事实成果验收 | 正文第 66、80–90 行明确为后续方案 | 未把样本量、阈值、费用默认为已批准。 |
| 94–96：本批未扫描、未外发模型分析、未改 harness | 弱支撑，执行者自述 | 两份报告的范围声明 | 本次核验未做这些动作；不能由此独立证明整个并行批次的全部历史。 |
| 98：没有提升比例、净节省或性能排名依据 | 标注正确 | 两份来源均声明未做个人任务实验 | 未发现未加限制的收益承诺。 |
| 100：存在一次缓存 grep deny，未绕过 | 弱支撑，执行者自述 | 上游报告第 233、322 行；任务输入也明确该边界 | 本次遵守边界，但未读取拒绝事件原始日志。 |
| 104：上游报告含79处固定提交来源 | 有据，机器计数 | 本次统计引用定义为79，均含40位提交 | 是引用条目数，不是79份独立研究或79次实验。 |
| 104：基线报告核过82处路径／行号 | 弱支撑，报告自述 | 现有机制报告第 205–210 行记录该输出 | 本次未重跑全部82项，只重读与核心断言相关部分。 |
| 106：此前曾重新读取关键位置 | 弱支撑，执行者自述 | 指定来源没有该次读取原始日志 | 可改成可公开核验的源码定位；不把本次复核倒写成此前行为证据。 |
| 106：未运行上游测试 | 有据，来源范围声明 | 两份来源均明确如此 | 全文没有把上游测试源码称为本轮通过。 |
| 108：门禁与483项测试已通过 | 标注缺失，未见原始运行证据 | 不在两份指定报告的机器输出中 | 见必须处置项；不能用本次文本检查补证。 |

## 初审历史：标注与引用问题

- **收益承诺：未发现。** 第 11、30、62、66、88、98 行区分了建议、推断与实验。不得把“最值得吸收”摘成“接入就会提高成功率”。
- **推断链：未发现负面核心判断伪装成已复现攻击。** 但姓名防护与 schema 证据门需要保留局部范围。
- **引用层级：存在二次转述。** 两份来源报告不是独立实验。本文已把直接重读、报告转述与执行者自述分开。原正文的“主会话重读”不能替代可回溯源码或机器日志。

正文的三条上游内联链接均钉到固定提交。本次对应 raw 文件读取成功。相对来源文件均存在。

原文把完整来源委托给两份报告，可回溯。建议在第 37、40、60 行附直接源码，避免负面判断被摘录时失去限定。

## 初审历史：处置建议与停止条件

**建议：** 仅处理表中三项必须项。其余限定可作措辞补强，不要求扩展调研或运行模型。

**建议：** Penguin 明确 scoreboard 读取路径；Headroom 明确默认失败学习模式；Founder 明确完整队列名。这些用于防止错误外推，不表示四项核心判断被推翻。

**停止条件：** 提供已有机器日志，或降级第 108 行；收紧 Atomic 与 Hy 两处范围。随后可作为静态机制与适配建议报告放行，仍不能作为已验证收益或自动写全局配置的依据。

## 初审历史：核验产物的验证结果

本节验证的是本文件，不替原文补足测试成绩。

| 交付物 | 存在 | 实质 | 接通 | 状态 |
|---|---|---|---|---|
| 只读事实核验 | 本文件存在 | 断言表、三项必须处置与四项重点均已写入 | 相对来源可读，引用定义与正文对应 | 已交付；原文裁决仍为阻断 |

- **Inner-loop evidence：** 本次复跑只读文本检查。输出为 `FACTS REVIEW CHECK: PASS`；`REFERENCE CHECK: 23 pinned definitions; no undefined or unused references`。
- **Acceptance evidence：** 本次逐项对照指定正文与来源。固定源码核查覆盖四项重点。机器输出为 `PUBLIC BOUNDARY CHECK: PASS; no personal absolute paths or session identifiers`，以及 `SUMMARY CONTENT CHECK: unchanged since captured checksum`。
- **Holdout / unseen evidence：** 不适用。本任务核验静态断言，不验证模型泛化。**Holdout 来源类别：** 不适用，未构造任务集。**预期值来源：** 需求原文与固定源码。
- **本次改动相对冻结点的位置：** 仅新增核验侧文件。检查对象为 2026-10-18 正文；校验期间正文内容哈希未变。
- **Known gaps：** 第 108 行缺原始日志；部分历史执行声明与机制细节仍为报告转述。未运行上游测试、会话扫描或模型。未验证 HTML；它不在本次授权内。

未运行通用构建或测试入口。纯核验文档采用链接、引用、公开边界及正文内容检查，不触发上游执行。

## 固定提交来源

以下均为本次只读取得的源码或说明；不是测试运行记录。取用日期均为 2026-10-18 UTC。实现与测试来自同一项目，不算两份独立效果证据。

[penguin-service]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/packages/server/src/services/benchmark-service.ts#L225-L319
[penguin-test]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/packages/server/test/benchmarks.test.ts#L302-L334
[penguin-protocol]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/plugins/default-rsi-toolkit/skills/agent-optimization/SKILL.md#L9-L134
[penguin-hook]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/plugins/continual-learning/hooks/stop.mjs#L177-L219
[jiuwen-engine]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/single_harness/iterative.py#L150-L174
[jiuwen-promote]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/single_harness/iterative.py#L833-L1015
[jiuwen-test]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/tests/unit_tests/rsi/test_single_harness_iterative.py#L1434-L1513
[jiuwen-team]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/jiuwenswarm/agents/swarm/providers/evolution_rails.py#L779-L847
[headroom-cli]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/cli/learn.py#L70-L359
[headroom-analyzer]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L230-L287
[headroom-digest]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L355-L512
[headroom-api]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L1063-L1101
[headroom-writer]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/writer.py#L487-L542
[atomic-ground]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/reflection/reflection-runner.ts#L425-L479
[atomic-vote]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/voting/vote-prompt.ts#L24-L101
[hy-gate]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_agent.py#L813-L837
[hy-defaults]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_agent.py#L72-L94
[hy-chain]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/coding/chain_store.py#L1-L53
[hy-readme]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/README.md#L24-L56
[founder-queue]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/feedback/task_queue.go#L94-L200
[founder-block]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/subconscious/block_accumulator.go#L119-L204
[founder-actuator]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/feedback/prompt_actuator.go#L54-L143
[founder-facts]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/optimal-engine/lib/optimal_engine/memory_core/fact_promoter.ex#L1-L65
