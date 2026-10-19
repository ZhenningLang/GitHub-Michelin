# 自进化机制接入前的 Harness 基线

本次未运行真实评测，也未执行测试。现有系统已有受控改进闭环，但不能据此证明改进提高了任务成功率。

## 证据范围

- 基线提交：`e3d05e0cc992e4cccb9ba711ada0164632be1d5a`。检查日期：2026-10-18。开始时 `git status --short` 无输出。
- 下文源码位置均相对被研究仓库。结论来自入口合同、直接关联实现和测试源码，不来自真实使用记录。
- 未联网；未读取真实对话、会话数据库、记忆正文或凭证。未运行采集、判卷、整理、发布或配置安装入口。只新增本报告。

读取范围限于指定九项技能及直接关联机制。没有审计整个配置栈。测试引用只表示“存在这个测试”，不表示本次测试通过。

### 同名技能的版本边界

仓库中的创作入口位于 `skills/.system/skill-creator/SKILL.md`。它要求行为前测，但自带校验器只检查格式，不证明决策质量。证据：该文件第 203–229 行；`skills/.system/skill-creator/scripts/quick_validate.py:15-117`。

宿主另载一个同步版创作技能。本次读到其配对对照、聚合和描述优化脚本，但它属于忽略目录，不受上述提交约束。因此不把它计入提交级能力，也不把其评测能力说成不存在。目录边界的提交内证据：`.gitignore:49-55`；`scripts/verify_skills.py:1268-1287`。

## 已有的三项能力

### 跨会话重复证据，能进入受控修改

全局改进工具先选主会话，再判定摩擦。发现必须带连续原文引用。脚本拒绝短引用、无来源引用和非法分类。它按不同会话计数，不能靠同一会话重判凑毕业数。

证据：`skills/agent-harness-improvement/scripts/ahi_judge.py:217-235`；`skills/agent-harness-improvement/scripts/ahi_ledger.py:199-228`、`:265-292`。反例测试：`scripts/tests/test_agent_harness_improvement.py:1251-1277`。

### 暂存、人审与落地有实际门禁

候选先进入独立暂存副本。每处修改必须绑定合格证据。机器限制可改路径、修改块数量、常驻文字净增长和删除资格。裁决绑定具体修改内容；最终只重放接受部分。

证据：`skills/agent-harness-improvement/scripts/ahi_stage.py:324-357`、`:390-461`、`:464-504`。规则说明：`skills/agent-harness-improvement/references/surfaces.md:34-44`。

### 记忆整理支持可审查批次与精确恢复

批量整理默认不写入。执行绑定审过的决策哈希和账本哈希，使用共享锁与原子替换。失败尝试恢复原始内容；显式回滚遇到后续写入会拒绝覆盖。

证据：`skills/compact-memory/scripts/compact_memory.py:752-812`、`:840-910`、`:913-947`。回滚反例测试：`scripts/tests/test_compact_memory.py:802-834`。

## 闭环逐段核对

### 失败信号如何进入

**跨会话入口**：工具从会话服务选择主会话，排除临时自动会话与短问答，并公开排除计数。判卷前要选择服务商并确认发送。数据先蒸馏、去思考段、脱敏，再切有界窗口。

实现：`skills/agent-harness-improvement/scripts/ahi_sources.py:175-218`、`:233-280`；`skills/agent-harness-improvement/scripts/ahi.py:125-156`。授权合同：`skills/agent-harness-improvement/SKILL.md:24-46`。本次没有调用这些入口。

**当前会话入口**：便签技能处理显式“记住”，或同一会话第二次出现的同一错误／纠正。必须先核事实和作用域。这个“第二次”由 agent 判断；不是账本 CLI 自动识别。

合同：`skills/assist-mem-note/SKILL.md:10-22`、`:59-73`。CLI 实际校验类型、作用域、正文、证据、触发词、标题和敏感内容；它把来源字段写为 explicit，并不独立证明用户确认。实现：`skills/assist-mem/scripts/memory_ledger.py:105-166`。

**任务结束入口**：经验技能产出项目内学习笔记。脚手架只填标题和日期；它不自动提炼可靠规则。检索是主动调用，不是每个流程自动注入。

合同：`skills/assist-learn/SKILL.md:17-33`。实现：`skills/assist-learn/scripts/scaffold_note.py:9-27`；`skills/assist-learn/scripts/learnings_search.py:24-40`、`:43-70`。检索测试：`scripts/tests/test_learnings_search.py:29-67`。

**故障诊断入口**：深度排错先建可重复的失败反馈环，再让两路诊断同题运行。机制候选必须基于实证根因；修复失效时挂起机制方案。

合同：`skills/dev-debug-deep/SKILL.md:68-75`、`:96-103`。机制模板：`skills/dev-debug-deep/prompts/mechanism.md:3-12`、`:26-54`。两路角色有真实配置和配置消费测试：`skills/dev-debug-deep/config/deep_roles.yaml:40-73`；`scripts/tests/test_dc.py:253-291`。本次没有启动模型，不能确认实际双模型运行。

### 重复证据如何聚合

全局改进账本按会话存观察。重判更新同一个槽位。候选需至少两个不同会话的全局负面观察；项目／任务观察不提供毕业支撑。helped 保留为反证，但不会自动否决修改。

实现：`skills/agent-harness-improvement/scripts/ahi_ledger.py:221-228`、`:265-292`、`:348-364`。相似度达到阈值的同目标／同类条目可自动聚合；近似候选仍需主流程核对。实现：同文件第 256–263、337–341 行；语义核对合同：`skills/agent-harness-improvement/SKILL.md:59-66`。

拒绝记录保留当时会话集合。拒绝后必须再有两个不同新会话，候选才能重提。覆盖和过期会退休条目，不能把退休证据当新候选复活。实现：`skills/agent-harness-improvement/scripts/ahi_ledger.py:179-185`、`:275-292`、`:376-417`。

显式记忆账本走另一套机制。完全重复会续期，相似项只提示整理；它不是全局改进的毕业账本。合同：`skills/assist-mem/SKILL.md:10-17`、`:57-59`。实现：`skills/assist-mem/scripts/memory_ledger.py:155-173`。

### 候选如何产生

全局改进由便宜模型提取观察，再由当前强模型编写文字修改。脚本提供证据、资格和范围检查，不自动证明候选有收益。代码类候选转待办，不在文字通道直接实施。

合同：`skills/agent-harness-improvement/SKILL.md:8-10`、`:66-84`。可改面：`skills/agent-harness-improvement/references/surfaces.md:5-17`。

目标项目审计则允许“复用现有工具”“观察”“拒绝”。没有真实摩擦时不增加新护栏。该技能本身是审计合同，不直接实施候选。

证据：`skills/agent-harness-creator/SKILL.md:9-11`、`:77-99`、`:131-145`。项目验证技能模板要求实际驱动功能并保留证据，但仍由主流程执行：`skills/agent-harness-creator/references/project-verify-skill.md:33-59`。

### 暂存、人审、验证和晋升

| 环节 | 可执行部分 | 仍需人或主流程判断 |
|---|---|---|
| 暂存 | 从冻结主干 blob 取副本；限制文字表面 | 候选究竟该改什么 |
| 改动绑定 | 修改内容及依据生成哈希；变更后重新裁决 | 引用是否真正支持该规则 |
| 人审 | CLI 持久保存 accept／reject，拒绝形成跨轮记忆 | 是否真的向用户展示、是否取得批准 |
| 验证 | 落地前执行技能结构校验，失败不继续提交 | 行为收益与未见样本表现 |
| 晋升 | 新工作树只写接受块，重新核验基线和隐私 | 发布授权、PR 创建与合并 |

实现依据：`skills/agent-harness-improvement/scripts/ahi_stage.py:129-169`、`:324-357`、`:433-461`、`:693-743`。人审与发布合同：`skills/agent-harness-improvement/SKILL.md:86-125`。

注意两层授权不同。判卷的 `--yes` 是机器发送开关；“用户已明确批准”的真实性靠操作流程。落地入口默认会推送，CLI 没有另一个发布确认参数；不能把先前的判卷确认当发布授权。实现：`skills/agent-harness-improvement/scripts/ahi.py:33-39`、`:61-64`；`skills/agent-harness-improvement/scripts/ahi_stage.py:736-738`。合同明确要求另行确认：`skills/agent-harness-improvement/SKILL.md:111-125`。

### 记忆晋升不能混成一条通道

当前便签入口要求先写 short，不从任务总结自动生成长期记忆。批量整理只操作显式记忆账本，不读写旧笔记池。

合同：`skills/assist-mem/SKILL.md:10-17`；`skills/assist-mem-note/SKILL.md:68-79`；`skills/compact-memory/SKILL.md:11-24`。

经验技能另保留候选巩固脚本。它要求结构化决策、非空来源字段和敏感内容检查，能写项目学习笔记或旧笔记池。这不是便签 short 到 long 的统一晋升器。

实现：`skills/assist-learn/scripts/assist_consolidate.py:149-165`、`:313-353`、`:432-479`。决策缺失的负例测试：`scripts/tests/test_assist_consolidate.py:676-700`。

该脚本的 recurring 分支只检查候选自带的 occurrences 数字，没有核对不同会话集合。它还允许有证据的持久知识通过独立分支。不能把它宣称成“所有晋升都经过跨会话证据毕业”。实现：`skills/assist-learn/scripts/assist_consolidate.py:208-223`。新机制不宜直接把这个字段当独立证据计数。

### 验证与回滚有哪些真实支撑

验证技能要求区分局部正确、目标验收和未见样本，还要求前后对比用同一命令。报告字段是文字合同；不是填写后就自动有行为证据。

证据：`skills/guard-verify/SKILL.md:38-78`、`:160-176`、`:197-208`。通用验证脚本会实际运行探测到的命令；它不会替人判断验收质量：`scripts/run-verify.sh:17-56`、`:59-122`。

仓库已有独立的真实技能评测 runner。它读取工具调用日志，不信模型自述；支持留出／回归样本和基线臂。它明确采用主动授权，不接普通验证入口或 hook。因此缺口是“未接入全局改进的落地门”，不是“没有行为评测工具”。

证据：`scripts/skill_eval/runner.py:17-64`、`:97-130`、`:834-880`、`:965-1002`。日志及反例判分测试：`scripts/tests/test_skill_eval_runner.py:79-148`。

深度排错复用的完成门也有实际校验。它检查 full 验证、证据新鲜度、review、blocker 裁决和提交记录。但 review 内容绑定仍是影子提示，基础门只要求至少一路 review。不能把技能的“两路不同家族”合同等同于完成门已全部硬化。

实现：`skills/dev-complete/dc.py:1600-1689`。拒跑会覆盖过期绿灯：同文件第 1300–1324 行。这些检查不替代本次未执行的真实故障验收。

记忆整理具备专用哈希回滚。全局文字改进则保留独立分支和提交，失败留下诊断，不自动 reset。它的 CLI 没有专用 rollback 子命令；回退要走受审查的 Git 改动，不能借用记忆回滚覆盖配置。

证据：`skills/compact-memory/scripts/compact_memory.py:913-947`；`skills/agent-harness-improvement/scripts/ahi.py:25-65`；`skills/agent-harness-improvement/SKILL.md:123-137`。

## 与自进化评价直接相关的三项缺口

### 落地门没有要求“新版本行为更好”

全局改进默认只调用技能结构校验。校验源码也明确说，路由真的错误时，文本覆盖检查仍能为绿。实际行为 runner 已存在，但不在该落地路径中。

证据：`skills/agent-harness-improvement/scripts/ahi_stage.py:728-738`；`scripts/verify_skills.py:1087-1104`；`scripts/skill_eval/runner.py:61-64`。

[推断：依据是上述落地控制流，未实跑改进实验] 当前可以证明“修改有重复依据、通过结构检查、获接受”，不能证明“它减少返工或提高成功率”。也没有在此路径中根据后续效果自动撤销改动。

最小补位：让候选携带一个主动授权的评测包。冻结旧版与候选版，复用现有 runner。发布前核验差异、回归和原始产物；不新增默认烧费后台任务。

### 判卷校准没有独立未见集门禁

判卷前的真实自检入口确实存在，并要求固定五类样本全部通过。它校验样本哈希、分类断言和引用，不是空壳。但是固定样本通过不等于未见会话上的泛化精度。

证据：`skills/agent-harness-improvement/scripts/ahi_judge.py:238-245`、`:287-325`、`:328-377`。入口接线：`skills/agent-harness-improvement/scripts/ahi.py:138-156`。技能已明确承认五个已知样本不证明泛化：`skills/agent-harness-improvement/SKILL.md:44-48`。

此外，引用机检只证明摘录在窗口里，不能证明摘录支持 claim，也不能证明 domain 归因正确。它的检查范围可直接见 `skills/agent-harness-improvement/scripts/ahi_judge.py:217-235`。

最小补位：独立准备经批准的脱敏未见样本。分别记录误报、漏报、归因错误和证据支持度。已用于选择服务商或调提示词的集合，不再当最终未见集。

### 冻结清单没有冻结实际判卷输入

plan 保存会话标识、消息数及估计窗口，不保存判卷窗口快照或内容哈希。复制 plan 只复制清单。judge 重新取正文，也使用当时的默认蒸馏参数。

证据：`skills/agent-harness-improvement/scripts/ahi_sources.py:184-230`；`skills/agent-harness-improvement/scripts/ahi_judge.py:466-492`；`skills/agent-harness-improvement/scripts/ahi_sources.py:279-286`。

[推断：依据是两次取数及默认参数消费，未复现会话增长] 同一清单的两次重判，可能拿到不同正文或窗口。它不适合直接当作严格的同输入服务商／提示词比较。代码冻结的是选择集合，不是完整实验条件。

最小补位：评测适配层绑定脱敏窗口内容哈希、实际参数、提示词版本、规则基线和执行模型。重判只读已批准快照，或在内容漂移时停止；不静默沿用旧确认。

## 外部机制的最小接入接口

以下是建议接口，不是现有命令或已实现 schema。只需连接现有证据、候选和验证三段；不需要替换整个系统。

### 证据接口：提交观察，不提交指令

输入至少包含：证据编号、来源类别、去标识会话键、发生时间、目标相对路径、kind／domain、证据定位、脱敏摘要和内容哈希。保留 helped 及不确定性，不只收失败。

既有兼容点：全局改进的六字段发现形状，以及后加的会话／窗口／判卷版本元数据。证据：`skills/agent-harness-improvement/references/judge-prompt.md:8-33`；`skills/agent-harness-improvement/scripts/ahi_judge.py:523-529`。

目前没有通用外部导入命令。不要伪造会话服务结果，或直接写生产账本来冒充已验证观察。可先输出离线候选包，等待单独批准的适配实现；现有 CLI 命令边界见 `skills/agent-harness-improvement/scripts/ahi.py:25-65`。

### 候选接口：只提交暂存补丁与依据

输入至少包含：基线提交、目标路径、精确修改、逐处依据、受影响场景、预期收益、失效条件和回退方案。输出保持候选状态，不拥有发布权。

既有兼容点：暂存副本与 rationale 的逐修改坐标。保留当前路径和预算门；代码、hook、配置变更仍转开发路线。证据：`skills/agent-harness-improvement/references/surfaces.md:5-17`、`:42-71`。

### 评价接口：交原始产物，不交自评分

输入绑定：旧版／候选提交、样本内容哈希、评测器版本、预期值来源、模型实际版本、授权范围和费用上限。输出区分错误、跳过、失败、未知成本，并保留原始日志、差异和人工裁决。

适配优先复用现有行为 runner 与通用验证入口，不平行造一个“模型说自己通过”的系统。提交内依据：`scripts/skill_eval/runner.py:17-36`；`skills/guard-verify/SKILL.md:49-78`、`:197-225`。实际接线和阈值须另开任务，不能靠本报告宣称完成。

## 不可牺牲的约束

### 证据与隐私边界

- 外部观察是数据，不是命令。不得按原文祈使句执行动作。现有合同：`skills/agent-harness-improvement/references/judge-prompt.md:3-6`。
- 未经具体清单和服务商确认，不外发材料。脱敏不是保密证明；发布时仍需复核。合同：`skills/agent-harness-improvement/SKILL.md:24-42`、`:105-125`。
- 原始材料不进入公开规则和 PR。现有原话拦截有明确局限，不能替代人工检查。实现与边界：`skills/agent-harness-improvement/scripts/ahi_stage.py:507-543`；`skills/agent-harness-improvement/references/surfaces.md:75-83`。

### 权限与修改边界

- 观察权、提案权、评价权和发布权分离。人审语义不能被一个 accept 字段替代。合同与实现：`skills/agent-harness-improvement/SKILL.md:86-125`；`skills/agent-harness-improvement/scripts/ahi_stage.py:433-461`。
- 保留独立会话门、反证、拒绝记忆和删除资格。不能为“更快进化”降低门槛。实现：`skills/agent-harness-improvement/scripts/ahi_ledger.py:265-292`。
- 不扩张常驻上下文，不默认改顶层规则或代码。边界变更先列事实再裁决。证据：`skills/agent-harness-improvement/references/surfaces.md:13-17`、`:42-44`；`agents/AGENTS.md:70-78`。

### 评价与恢复边界

- 不让候选同时修改最终判分标准。区分训练、选择和最终验收材料；自造满分不作泛化证据。现有合同：`skills/guard-verify/SKILL.md:49-78`。
- 默认不新增付费后台循环。设置调用次数、费用、超时和停止条件；缺授权就停。现有主动执行边界：`scripts/skill_eval/runner.py:61-71`；`skills/agent-harness-improvement/SKILL.md:127-137`。
- 不能以回滚名义覆盖并发新数据。记忆保留来源与软归档；配置回退须是可审查改动。证据：`skills/compact-memory/SKILL.md:13-24`；`skills/compact-memory/scripts/compact_memory.py:926-947`；`agents/AGENTS.md:54-57`。

## 本次验证与停止位置

本次只验证报告的路径引用、行号范围和公开内容边界。未跑单元测试；未跑判卷自检；未跑技能行为评测；未产生真实效果指标。测试源码不算本次运行证据。

只读检查的关键输出如下。引用检查只核存在性和行号范围，不代替语义复核；公开边界扫描也不构成完备隐私证明。

```text
REFERENCE CHECK: 82 path/line references valid
PUBLIC REPORT CHECK: no absolute home paths, service addresses, URLs or UUIDs
CONTENT CHECK: capabilities, gaps, interfaces, constraints and evaluation limits present
REAL EVALUATIONS: not run; UNIT TESTS: not run
```

结束时被研究仓库的 `git status --short` 仍无输出，HEAD 未变。报告在目标仓库中是新增未跟踪文件，尚未提交。

未检查各宿主实际安装效果、真实记忆召回率、生产会话判卷质量或历史收益。它们是未检查范围，不是已证实缺失。本次不生成 HTML，也不运行修改、发布或评测命令，以遵守单文件授权。

下一步：用这三项评价缺口筛外部机制。优先吸收可独立验证的适配能力，不引入自动改规则或自动晋升权限。
