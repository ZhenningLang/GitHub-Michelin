# 自进化可信性：源码证据报告

**结论：借鉴实验设施，不授予自动改全局规则的权限。**

**本轮未运行任何上游测试、模型、安装器或示例。** 以下结论来自固定提交的静态源码。它们证明“代码如何决策”，不证明“接入后效果更好”。调研时间为 2026-10-18 UTC。

最重要的三点：

- **Penguin 和 Jiuwen 有真实优化链，但没有本轮所需的独立留出验收。** Penguin 反复用同一题集选优，还信任模型填写的平均分。Jiuwen 的单 harness 引擎主动将内部 holdout 设为零。
- **Headroom 最接近个人规则改进需求，但不是效果验证器。** 它从失败会话生成规则，默认预览；应用时直接写入指令文件。证据次数、收益估算和固定置信度，不等于规则已经有效。
- **记忆增长不等于 harness 进化。** Atomic 和 Hy-Memory 主要改变记忆。FounderOS 的一个“应用改进”函数只更新 Q 值，并按建议自身的 impact 发奖励，不能据此声称改进已执行。

这些判断分别由后文的实现与测试支撑。对个人 harness 的采纳建议属于 **[推断：依据是以下静态边界；未做个人任务集实验]**，不是实测收益结论。

## 范围与判据

核对了指定的 11 个仓库。深挖六个：Penguin、JiuwenSwarm、Headroom、Atomic Agent、Hy-Memory、FounderOS。

本报告把三个问题分开：

- **会不会变？** 有持久化写入即可成立。
- **会不会按分数选？** 要有可执行评价和晋升规则。
- **是否值得放进个人全局 harness？** 还要有未参与选优的验收任务、权限隔离、回滚与人工放行。

“独立评价器”不只是另开一个模型会话。“独立留出集”必须未用于诊断、改写和逐轮选优。回放同一题集可以查回归，但不是留出验收。

已只读对照本地维护约定和既有改进路线。这里不复制私人路径、配置内容或会话信息。报告不替换既有流程，也不产生配置变更。

## 候选身份核对

以下链接均钉到本轮读取的提交，不是浮动分支。

| 仓库 | 此提交实际做什么 | 自进化归类 |
|---|---|---|
| morluto/rea | 二进制、应用和运行行为的逆向工具。[README][rea] | 不是本题的自进化框架；不能因缩写贴标签。 |
| simplifaisoul/osiris | 全球 OSINT 实时地图与情报面板。[README][osiris] | 不属于本题。 |
| Prism-Shadow/penguin-harness | 固定模型，优化提示、skill、工具、hook。[README][penguin-readme] | 深挖：基准驱动优化，另有无基准的持续学习 hook。 |
| isair/jarvis | 本地桌面助手；图记忆分 user、directives、world。[源码][jarvis-graph] | 有记忆适配，不把它写成已验证的 harness 优化器。 |
| AtomicBot-ai/atomic-agent | 反思提取记忆、投票、蒸馏经验。[源码][atomic-reflect] | 深挖：记忆维护。 |
| Bennettxai/FounderOS | 业务控制台；有反馈提示、Q 表和事实晋升。[启动代码][founder-wire] | 深挖：运行时提示与记忆适配，不是统一自改代码系统。 |
| openJiuwen-ai/jiuwenswarm | 在线 skill 经验、基准驱动 harness 优化。[接线][jiuwen-rails] | 深挖：须区分在线经验和离线 RSI 两条路径。 |
| google/agentmesh | agent 私有网络、身份、服务发现与授权。[README][mesh] | 基础设施；不是自进化算法。 |
| Tencent-Hunyuan/Hy-Memory | 分层记忆、认知归纳、工作经验、代码改动链。[README][hy-readme] | 深挖：记忆进化；使用训练后模型不等于运行时训练。 |
| headroomlabs-ai/headroom | 压缩代理另带失败学习命令。[实现][headroom-cli] | 深挖：规则生成与写入。 |
| p1neappleXpress/OpenFlux | TCP/UDP 隧道、可插拔传输。[README][openflux] | 不属于本题。 |

对未深挖者的判断限于 README、完整文件树与所列源码。不声称穷尽这些项目所有分支或历史。

## Penguin Harness

### 实际闭环

**进化对象。** 默认工具包修改被测 agent 的 `AGENTS.md`、目标自有 skill，以及允许的运行时配置。模型与思考档由参考评价固定。它不是模型权重训练。[改动合同][penguin-loop]

**触发与输入。** 用户指定被测 agent、已发布且冻结的 Benchmark、目标分数、每题运行次数和轮数。优化器读取公开题面、分数、执行轨迹，以及历史候选；合同禁止读取 rubric、gold 和私有评价状态。[前置条件与隔离][penguin-contract]

**候选生成。** 每轮从当前最好版本起步。模型先提出可证伪假设，再做一个有界改动。候选版本递增，不沿用被拒版本。默认规则不是进化算法的纯代码状态机，而是 agent 执行的 skill 协议。[逐轮协议][penguin-loop]

**可执行评价。** 存在两类：普通题由独立评价子任务执行目标、读取私有 rubric 并评分；Harbor 题由任务 verifier 奖励替代 rubric 判断。示例另有确定性的 `score()`，检查报告格式与数值关键词。[评价合同][penguin-eval]、[示例计分代码][penguin-demo]

**晋升与回滚。** 默认协议要求完整有效的候选平均分严格高于参考分。改动前保存版本快照；失败时恢复原文件与新建文件清单。不存在逐候选强制人审步骤，满足协议即可接受。[接受与快照][penguin-loop]

**成本与权限。** 一轮评价规模为题数乘每题运行次数，再加优化器和评价器调用。失败修复不消耗有效轮数；协议没有固定重试次数上限，只要求每次有新修复。普通题的启动命令使用 `--approve allow-all`。这不等于操作系统 sandbox 被关闭，但不能把“独立子任务”当权限隔离证明。[修复规则][penguin-retry]、[启动参数][penguin-eval]

### 具体可信性问题

**同题选优，不是留出验收。** 默认协议要求每轮评估同一冻结 Case 集。基线一题一次，候选可多次；协议明确直接比较平均分，不补齐基线次数。[比较规则][penguin-contract]

**[推断：依据是同题反复选优及不等重复数；未做统计实验]** 多轮挑最高分会选择噪声，也会适配已见题。存在 GDPevo Train/Test 的产品入口，不代表默认工具包强制使用独立 Test 晋升。不能用 demo 涨分推导个人任务泛化。

**平均分由模型填写，服务端不复算。** 协议明确禁止增加平均分一致性检查。服务端 `toCase()` 和 `toEvaluation()` 信任存储汇总值。测试故意让子运行的 80、82 对应汇总 80.2，并断言显示 80.2，而非算术平均 81。[协议末尾][penguin-loop]、[解析实现][penguin-score]、[反例测试][penguin-score-test]

**[推断：依据是上述可写汇总与缺失一致性检查]** 分数计算错误或被污染的记分文件，可产生虚假的上升曲线。这不是已经复现的攻击；它是明确的数据可信边界。

**普通题的“保密”主要由指令声明。** skill 禁止优化器看 rubric，但本轮没有证据证明优化器在文件系统层读不到它。评价器会读私有 rubric。Harbor 容器提供不同边界，不能与普通题混为一谈。[访问合同][penguin-contract]、[评价准备][penguin-eval]

**另一条持续学习路径没有上述评分门。** `stop.mjs` 在任务超过 30 个完成回合时，摘取轨迹并返回后台子任务提示。提示要求直接编辑已有 skill，且提升版本号。该 hook 不运行 benchmark，不要求晋升评测，也不创建版本快照。[完整触发和写入提示][penguin-stop]

### 测试能说明什么

已读测试能检查记分文件解析，也明确固定了“不复算平均分”的行为。示例计分器是真代码，但格式样例和同任务重测不证明跨任务改进。[解析测试][penguin-score-test]、[示例任务与评分][penguin-demo]

**采纳建议：[推断：未接入个人任务集]** 借鉴版本快照、单假设改动和逐题执行轨迹。不要照搬模型填写汇总、同题最高分晋升，或后台直接改 skill。

## JiuwenSwarm

### 两条不同路径

**在线 skill 经验。** 主 agent 定期自查或响应 `/evolve`，由受限 reviewer 提出结构化经验。经验先存入 skill 经验库；后续调用即可加载，不必等合并进 `SKILL.md`。文档与 provider 接线吻合：leader 默认按 `auto_save=false` 接审批栈。[使用语义][jiuwen-doc]、[leader 接线][jiuwen-leader]

**离线 harness RSI。** 服务把数据集、harness 快照和模型配置交给 `SingleHarnessIterativeOptimizationOrchestrator`。该引擎不在 JiuwenSwarm 本体，而在固定的 agent-core 依赖。本轮继续读取了依赖提交，不把 wrapper 当算法实现。[依赖钉定][jiuwen-dep]、[生产调用][jiuwen-provider]

### 对象、候选和评价

**进化对象。** 单 harness 引擎允许 `prompt`、`skill`、`tool`、`rail`，提示改动限 `prompt_section`。因此不仅是文字，也可能包含工具或 rail 代码；这仍不是模型权重训练。[允许面][core-surfaces]

**触发与证据。** 在线路径以任务、调用轨迹、纠正和 reviewer 反馈为材料。受限 reviewer 的工具列表专门构造，MCP 为空，不挂 skill；它可以根据明确 user intent 提案，即使 `evidence_refs=[]`。这是设计允许的需求录入，不是失败证据已经成立。[reviewer 实现][core-reviewer]

**候选生成。** 离线路径对执行结果做分析，再生成有界候选。结构验证器检查 YAML、JSON、Python 语法、包加载和 action 约束；它明确“不执行评价、不计算 pass@k”。skill 脚本另有危险后缀、导入和调用黑名单。[验证实现][core-verify]

**可执行评价器存在。** `ScriptBasedJudger` 支持后端判分、参考答案比较及 SWE-bench 官方执行。它拒绝将“运行成功”直接当“答案正确”。另有显式 LLM-as-judge 路径，评分与格式校验为程序实现。[脚本判分][core-script]、[模型判分][core-judge]

**独立 holdout 不存在于这个单 harness 协议。** 构造器把 `candidate_holdout_cases` 强制覆盖成零。测试即使传入 1，也要求全部三题进入优化，最后断言 holdout 为零。[覆盖实现][core-no-holdout]、[专项测试][core-no-holdout-test]

**晋升与回滚是真机制。** 每个 epoch 对全部任务回放。过滤掉改动后，如生成了不同最终包，会再次评价最终包。最终包必须全局不退步，受保护任务不能退步，存在基础设施或机器证据不确定项也不能晋升；否则退回 epoch 起始版本。[完整晋升链][core-promote]

服务端另有发布包路径约束、软链越界检查与 manifest 加载校验。安装测试覆盖指针写失败、热加载失败补偿及回滚。[安装校验][jiuwen-activate]、[安装回滚测试][jiuwen-activate-test]

### 具体可信性问题

**审批并不覆盖所有参与者。** teammate provider 固定使用 `signal_trigger=True`、`auto_save=True`、`review_trigger=False`，与 leader 的人工审批路径不同。两者写入同一个物理 skill 库。[队员接线][jiuwen-member]、[单库根选择][jiuwen-library]

**[推断：依据是共享库及队员自动保存；未运行跨会话实验]** “leader 默认要审批”不能推出“全局 skill 经验不会被后台自动改变”。对多 agent 共用的个人 skill 库，这是应先隔离的权限边界。

**回归门不等于泛化门。** 全量回放和受保护题可以阻止已知退化。但全部题都参与优化，不能据此声称改进能迁移到未见任务。[无留出测试][core-no-holdout-test]

**在线经验分数也不是效果测量。** 被动优化器按信号类型预设初始分：执行失败、用户意图、脚本产物和对话复盘各有常数。这个初始分不是独立运行后的成功率。[常数与预算][core-skill-score]

**成本和权限。** RSI 包含目标执行、诊断、候选生成、验证修复、最终全量回放，过滤后还可能再跑一次。wrapper 声明支持恢复，但不支持中途暂停和终止。skill 被动候选的 LLM 策略设置 150 秒单次、300 秒总预算、最多两次尝试。[运行能力][jiuwen-provider]、[预算代码][core-skill-score]

### 测试能说明什么

引擎测试用替身 evaluator/analyzer 检查选题、晋升和回退；安装测试检查事务补偿。这些是有价值的控制流证据，**不是本轮运行结果，也不是实际模型收益证据**。[无留出测试][core-no-holdout-test]、[安装测试][jiuwen-activate-test]

**采纳建议：[推断：未做个人任务实验]** 六者中，这条离线链最值得研究“最终实际产物重测、已知成功不退步”。但先补外部封存任务；不要将在线队员自动保存挂到共享 skill 实体。

## Headroom

### 实际闭环

**进化对象。** `headroom learn` 生成项目指令或记忆文字。Claude 默认目标是 `CLAUDE.local.md`；Codex writer 会写 `AGENTS.md` 和对应 memory 文件；Gemini/Grok 有各自 writer。它不训练模型，也不自动实现工具代码。[写入器][headroom-writer]

**触发与证据。** 显式运行 CLI 后扫描选定项目；可指定全部项目。默认包含嵌套子任务，`--main-only` 才排除。分析器用工具失败、循环、用户文字、打断和既有规则构造摘要。[CLI 选项][headroom-cli]、[分析入口][headroom-analyze]、[摘要内容][headroom-digest]

**候选生成。** 一个 LLM 分析摘要，输出规则、`evidence_count`、`estimated_tokens_saved`。循环有程序测得的浪费估计并被优先加权；其他收益估计仍来自模型。解析器给 context 规则固定 0.9 置信度，memory 固定 0.7，并直接接受模型给的次数。[生成提示][headroom-objective]、[解析][headroom-parse]

**评价与晋升。** CLI 的主链是扫描、分析、输出建议、writer。没有在写入前运行新旧 harness 的任务对照。默认 dry-run，`--apply` 才写；没有逐条强制审批或基于 holdout 的效果晋升步骤。[实际调用链][headroom-flow]

**回滚。** writer 管理标记区、合并新旧小节，并防止内容关闭管理标记。所读主链没有创建上一版快照，也没有接受失败后的效果回滚控制器。需要外部版本管理，而非把重复写入幂等当回滚。[管理区与合并][headroom-merge]、[实际写盘][headroom-writer]

### 具体可信性问题

**dry-run 不是不外发。** 分析发生在 `writer.write(..., dry_run=not apply)` 之前。API 模型会收到摘要，其中包含用户文字、工具参数和失败输出片段。默认模型按环境中的 provider 可用性选择。该主链未要求逐 run 外发确认。[模型选择][headroom-backend]、[摘要字段][headroom-digest]、[API 请求][headroom-api]、[写入顺序][headroom-flow]

**能写全局入口。** Claude writer 对 home 项目特殊处理，写入 Claude 全局 `CLAUDE.md`；显式 `--target` 也接受绝对路径。它不是仅能写项目沙盒的工具。[目标解析][headroom-target]

**[推断：依据是按目标路径直接写入；未在本机执行]** 对软链分发的全局规则直接 `--apply`，可能绕过受管仓库的提案、审查与发布路径。默认项目输出较克制，但不能把默认文件名当硬写域。

**自己报告的收益不是验证。** 生成提示的目标是减少 token 浪费；解析器没有将 `evidence_count` 逐条绑定到真实会话，也未因次数少而拒绝规则。[生成目标][headroom-objective]、[解析实现][headroom-parse]

**[推断：依据是目标函数与缺失任务验收]** 更少重读、更短回答，不一定是更少错误。限制读取、跳过复核也可能在省 token 的同时降低可靠性。应以正确率、安全边界和重复摩擦率共同验收，不能用模型估算的省量替代。

**后端隔离不一致。** Claude CLI 路径清空工具、MCP 并禁 hook；Gemini 和 Codex 命令没有同等“零工具”参数。源码只对无法零工具的 agy 单独要求危险 opt-in。[后端构造][headroom-backend]

**[未验证：未启动各 CLI，也未检查其运行时权限]** 不能断言 Gemini/Codex 分支一定会执行恶意摘要，也不能称其隔离与 Claude 分支等价。

### 成本与测试

摘要默认预算为 80,000 token，溢出时减半重建。API 输出上限为 4,096 token；CLI 有墙钟与部分路径的空闲超时。未取得实际 token 账单，故不估算本机成本。[摘要预算][headroom-backend]、[API 调用][headroom-api]

已读 integration 测试包括无建议不写、幂等、误报过滤，以及依赖真实本机会话和 API key 的条件测试。它们会在缺条件时跳过；没有因此得到“学习后任务更成功”的证据。本轮未运行，尤其没有让它扫描私有会话。[测试边界][headroom-tests]

**采纳建议：[推断：未做个人任务实验]** 可借鉴失败循环探测与多宿主适配。只把输出当提案，不启用自动写全局目标；现有受治理改进路线不应被它替换。

## Atomic Agent

### 实际闭环

**进化对象。** 反思可写 profile、自由笔记和已有笔记标签；蒸馏再产生 lesson 与 procedure。`NeighborEvolver` 明确只改 tags，不接受内容改写。这里的 procedure 是记忆条目，不是自动安装的可执行 skill。[反思写入][atomic-reflect]、[标签变更器][atomic-evolve]、[蒸馏结果][atomic-distill]

**触发与输入。** 反思在回复后异步执行，输入用户消息、助手回复、可选滑动窗口，以及本轮展示过的记忆 ID。平凡窗口可跳过；同会话新反思可中止旧反思。另有冷路径按冷却、聚类、租约蒸馏旧笔记。[输入合同][atomic-input]、[执行入口][atomic-reflect]、[冷路径][atomic-cold]

**候选生成。** 模型输出语法受限的 SET、NOTE、EVOLVE。确定性 grounding 过滤无来源姓名、助手人格和某些一次性指令。合法结果随后直接写入，并非等待独立任务评测。[调用、过滤与写入][atomic-write]

**评价。** 运行时投票器让反思 LLM 对本轮展示的条目投票；输入是用户消息、助手回复和短预览。另有离线 E3 审计框架，让注入的 judge 按 rubric 评价提取结果。后者没有接入每次记忆晋升门。[投票实现][atomic-vote]、[离线审计][atomic-audit]

**晋升与回滚。** 记忆与标签通过语法、来源及限额检查后写库；投票影响后续维护。蒸馏保留 parent ID 并归档原笔记，老化、负票和溢出会降级条目。所读链未提供新旧记忆在独立任务集胜出后才生效的门，也不是整套 harness 的版本回滚。[冷路径及降级实现][atomic-consolidate]

### 具体可信性问题

**“被答案使用”被当作赞成理由。** 投票提示要求：答案直接使用、转述或符合条目建议时就 upvote。它没有得到独立正确答案或工具成功证据作为必需字段。[提示词与输入类型][atomic-vote-prompt]

**[推断：依据是该奖励定义；未运行污染实验]** 一条错误笔记若被助手照抄，也可能得到正票。重复使用会形成自我确认；展示 ID 白名单只能限制“给谁投票”，不能证明“投得对”。

**空召回集退成无白名单。** `applyEvolves()` 仅在 ID 数组非空时构造 allowlist；缺失或空数组变成 `undefined`。`NeighborEvolver` 只在 allowlist 存在时检查目标 ID。[调用点][atomic-allowlist]、[写入门][atomic-evolve]

**[推断：依据是这两个条件分支；未执行复现]** 当反思输出已存在记忆的 ID 时，空召回集不表示“零条可改”，而表示不做此项白名单检查。影响范围是有数量上限的标签变更，不应夸大为任意内容或代码改写。

**来源防护是真实但有界。** 姓名 grounding 特别防止旧幻觉姓名为自己作证；这值得借鉴。它不自动构成所有自由笔记的语义真实性校验。[来源纪律][atomic-write]

### 成本与测试

标签 EVOLVE 共用反思调用，不另发 LLM 请求；投票另有一次子调用；蒸馏每簇一次。各 runner 有超时和数量上限。使用本地模型仍有算力成本；云路径会发送反思输入，本轮未测费用。[标签成本][atomic-evolve]、[投票上限][atomic-vote]、[蒸馏预算][atomic-distill]

测试验证 25 次 evolve 不改原文、写入限额和非空白名单过滤。E3 统计 useful/wrong/NONE；可注入独立 judge，但接口不强制它与生成模型不同。没有未见任务泛化结论。[标签测试][atomic-evolve-test]、[E3 实现][atomic-audit]

**采纳建议：[推断：未做个人任务实验]** 借鉴来源不能自证、正文追加式保留和明确变更类型。不要用“被答案采纳”作提升全局规则的奖励。

## Hy-Memory

### 实际闭环

**进化对象。** Chat 路径把事实归纳成高层 schema；Working/Coding 路径提取事实和可复用经验；Coding 另附真实 diff 版本链。diff 链代码明确只记录改动，不选择“最好版本”，也不负责修改仓库。[认知引擎][hy-system2]、[写入协调器][hy-writer]、[版本链职责][hy-chain]

**触发与证据。** System 2 由调用方显式调用 `evolve()`，读取当前用户的记忆池，做聚类与已有图查询；无事实或无聚类时可以跳过。Working/Coding 使用带工具轨迹的消息。[显式触发][hy-evolve]、[聚类流程][hy-system2]、[跳过条件][hy-skip]、[工作路径][hy-writer]

**候选生成。** System 2 的 LLM 提出图节点与证据关系；工作路径用 LLM 提取，再分别协调经验 ADD/UPDATE/DELETE/SKIP 与事实 INSERT/SUPERSEDE。不是生成多版 harness 后赛马。[工作写入][hy-writer]

**评价器。** `coding/judge.py` 实际是 chat/working/coding 场景分类器，不是“这条经验是否让任务成功”的裁判。System 2 有证据门与去重规则；未在所读写入链看到新旧记忆的任务执行比较。[judge 职责][hy-judge]、[证据门][hy-evidence]

**晋升与回滚。** 图写入器创建的节点直接为 ACTIVE、INFERRED，confidence 可来自操作参数。schema revise 保留旧版本并使旧版退出 active；这属于记忆版本治理，不是 harness 效果回滚。[图写入与修订][hy-tools]

### 具体可信性问题

**强证据门默认未开。** `_S2_SCHEMA_EVIDENCE_GATE_ENABLED` 的环境缺省是 false。`validate_new_schema_evidence()` 在关闭时直接返回；开启后才要求 user-owned 事实及至少两个独立 raw/session 来源。提示词写了“两份独立证据”，不能当作默认硬门已启用。[默认值][hy-defaults]、[校验函数][hy-evidence]

**[推断：依据是默认开关与校验分支；未执行生成实验]** 默认部署不能仅凭文档宣称有跨事件证据硬保证。模型仍可能遵守提示，但那是模型行为，不是程序强制。

**同批全互链不是逐条证明。** `CodingWriter._crosslink()` 把同批所有经验与同批事实两两连接；它保留历史链接，但不逐条判断哪一条事实支持哪一条经验。[交叉链接实现][hy-crosslink]

**[推断：依据是全互链实现]** 这些链接适合追溯“同次写入”，不宜直接当“每条经验都获得了全部事实支持”。若把链接数用于晋升，会把批次关联错当独立证据数量。

**训练后模型不等于运行时学习权重。** README 宣称发布了 RL 训练的 30B-A3B 模型。本轮只核对 SDK、公开文件树和实现，没有读取技术报告或权重，也没有在检索到的训练路径中取得可复现训练链。[上游声明][hy-readme]

**[未验证：未审论文、训练数据及权重]** 不评价该模型训练收益，也不声称查到训练/测试泄漏。当前 SDK 的“进化”证据是记忆写入与修订，不是本机梯度更新。

### 成本与测试

System 2 涉及全池扫描、embedding、聚类、LLM 和图存储；工作路径还含分类、提取与协调调用。调用次数依事实簇和分批变化，不能用一次 `evolve()` 当一次 LLM 请求。[认知流程][hy-system2]、[工作流水线][hy-writer]、[显式触发][hy-evolve]

本轮读到的 coding E2E 测试使用 `MockLLMProvider`、mock embedding，验证跨链、路由和写入。这能检查数据接线，不能验证经验正确性或模型效果。[测试源码][hy-tests]

有一项针对下载缓存中 System 2 writer 的 grep 被权限系统拒绝，未换工具或命令绕过。已取得的相关代码仍足以支持以上限定结论；该搜索未完成，不补造结果。

**采纳建议：[推断：未做个人任务实验]** 可借鉴精确 diff 记忆、来源计数和不可变修订。不要把它直接当自动修全局 harness 的框架。

## FounderOS

### 实际闭环

**进化对象。** 一条路径把指标偏差转为有 TTL 的提示修正；另一条把用户偏好、session 模式及高分建议存为 memory block。后台启动接线确实创建 observer、Q 引擎、提示 provider 与控制循环，不只是孤立类名。[启动接线][founder-wire]、[提示执行器][founder-actuator]、[block 写入][founder-block]

**触发和证据。** 字符串规则识别重述、挫败、偏好及“thanks/ok”等确认。确认给 response_format 的 Q 状态正奖励，挫败给 prompt/context 类型负奖励。它不是用任务 verifier 归因某次候选改动。[检测器][founder-pattern]、[奖励归因][founder-block]

**候选生成。** 引擎枚举七种固定建议类型，描述来自静态模板；confidence 是 Q 值乘十并截断，impact 是 confidence 再乘类型权重。冷启动还注入随机小数。没有在这个函数里生成和比较可执行代码候选。[建议代码][founder-q]

**评价与晋升。** 高于 5 的建议会写成 self_improvement block；`AutoApply` 使用 confidence≥9、impact≥0.25。两者均是派生分门槛，不是未见任务集得分。[block 门槛][founder-block]、[建议门槛][founder-q]

**回滚与成本。** PromptActuator 默认十分钟 TTL，并能清理过期 hint；持久偏好 block 不设到期。Q 表在该引擎内存中维护，Redis 读取的是奖励权重。启发式规则本身不调用模型，外围分类和业务执行仍有开销。本轮未量测。[提示生命周期][founder-actuator]、[偏好与 Q 路径][founder-block]、[Q 存储实现][founder-q]

### 具体可信性问题

**一个“apply”没有应用业务改动。** `ImprovementTaskQueue.apply()` 的全部动作是 `reward = suggestion.Impact * 10`，再 `UpdateQValue()`，然后返回成功。它没有改提示、代码或配置。`Process()` 随后将任务标成 Applied。[队列实现][founder-queue]

**[推断：依据是该函数体；未运行接口]** 该模块把建议自身估计的 impact 作为奖励，不能证明用户目标更好。也不能用 Applied 状态证明改进已实际落地。主启动路径的 memory-block 适配是真实的，但不能替这个空缺作证。

**奖励容易错归因。** “ok”等确认奖励固定类别，而不是绑定到某个候选版本及其执行结果。`stateKey` 包含具体上下文、agent 类型和改进类型；一般礼貌确认未必命中原问题上下文。[检测规则][founder-pattern]、[奖励调用][founder-block]、[Q key][founder-q]

**[推断：依据是文本启发式和状态键]** 既可能把礼貌当成功，也可能根本奖励不到导致满意的候选。Q 值增长不应当成可靠的改进置信度。

**另一个事实晋升子系统更值得借鉴。** bundled Optimal Engine 将 claim 与 fact 分开，事务内写来源、派生账本和 supersession。策略拒绝同 evaluator 自审，除非显式放行；也允许 policy 自动晋升。[事实晋升][founder-fact]、[审查策略][founder-policy]

**但不是全部都要人审。** scheduler 默认 `auto_threshold`；按置信度筛选后调用自动晋升。claim score 又允许调用方覆盖置信度。因此“有审查生命周期”不等于“每个 fact 都获独立事实核验”。[scheduler][founder-scheduler]、[分数来源][founder-policy]

### 测试能说明什么

Q 测试可检查常量奖励下数值变化和 AutoApply 门槛；claim 测试可检查拒绝、过期和冲突约束。这些不能证明反事实任务收益，也不能补上 queue apply 缺失的执行动作。[Q 测试][founder-q-test]、[claim 测试][founder-fact-test]

**采纳建议：[推断：未做个人任务实验]** 借鉴 claim/fact 分离、来源账本和修正 TTL。不把 Q 分数直接接成全局规则自动晋升，不引入整套业务平台仅为个人 harness 改进。

## 横向裁决

| 项目与路径 | 真正改动 | 可执行评价 | 未用于选优的留出门 | 人审与回滚 |
|---|---|---|---|---|
| Penguin 默认 RSI | 指令、skill、配置 | 有；模型 rubric 或 Harbor verifier | 默认协议无；反复同题 | 自动按分接受；有快照协议 |
| Penguin 持续学习 | skill 文本 | hook 无评价步骤 | 无 | 后台写入提示；所读 hook 无快照门 |
| Jiuwen 在线经验 | skill 经验及重建 | 受限提案审查，不是任务收益评价 | 无 | leader 默认审批；teammate 固定自动保存 |
| Jiuwen 单 harness RSI | prompt、skill、tool、rail | 有程序判分和模型判分 | 明确强制内部 holdout=0 | 全量回归、最终包重测、服务安装回滚 |
| Headroom learn | 指令及记忆文字 | 没有接入规则前后任务评价 | 无 | 默认预览；apply 直接写文件 |
| Atomic | profile、笔记、标签、lesson、procedure | 离线审计有；在线主要模型投票 | 不作为在线晋升条件 | 有来源/限额/归档；非 harness 版本回滚 |
| Hy-Memory | 事实、经验、schema、diff 链 | 场景分类与证据规则；非任务收益裁判 | 不在所读写入链中 | schema 修订保留旧版；非效果门 |
| FounderOS | hint、memory block、Q 表 | 文本信号、派生分；非候选任务比较 | 不在所读改进链中 | hint 有 TTL；事实另有治理子系统 |

**不应统一称为“自己评自己”。** Penguin 把评价委托给另一子任务，Jiuwen 有真正的程序评价器，Atomic 离线框架可注入不同 judge。问题分别是权限隔离、题集独立性、奖励定义和结果来源；只换一个模型不能同时解决。

**没有发现足够证据可宣布“已发生训练测试泄漏”。** 可以确认的是选优与验收题集未分开，或私有 rubric 的隔离只在协议里声明。前者是设计事实，后者是尚未验证的执行边界；它们不等同于已经泄漏。

## 对个人 harness 的最小建议

以下是建议，不是本轮实施计划或已验证收益。

**[推断：基于以上六条静态链]** 不迁入整套“自进化”框架。保留现有受治理改进路线，补一个小型、外置的实验层即可。不要让上游 writer、后台 hook 或队员直接触碰共享全局配置。

只借三个机制：

- **候选隔离。** 从冻结版本复制，限定到单个提示或 skill；保留哈希、diff、写域和还原点。参考 Penguin 快照与 Jiuwen 最终包重测，而非运行中覆盖共享实体。
- **机器算分。** 执行器输出原始结果，程序汇总。训练/诊断任务与封存验收任务分开；候选生成者看不到封存答案。把安全与已知成功回归设成不能用总分补偿的门。
- **人审晋升。** 模型只提案。验收覆盖正确率、重复摩擦、危险动作与成本；人工确认后才经受管发布入口生效。没有实测收益，先不改全局默认。

**[未验证：尚未建立个人封存任务集并做候选实验]** 本轮不能回答能提升多少、哪一个项目能净省成本、或更换框架是否优于现有路线。需要的是一次隔离的小实验，不是先安装再观察。

## 已执行的只读操作与未运行项

### 命令记录

全部 shell 为前台 `python3 - <<'PY' ... PY`。代码只用标准库获取公开 HTTPS 文本、保存缓存、解析 JSON 和检索文本；没有 import 或执行上游模块。为避免泄露私人目录，以下将批准的临时缓存根统一写成 `$CACHE`；这是记录中的路径归一化，不是声称实际 shell 里定义过该变量。

| 顺序 | 已执行操作及关键语句 | 机器结果 |
|---|---|---|
| 首轮 | 对 11 个 `repos` 并发 `urllib.request.urlopen('https://api.github.com/repos/'+repo)`；读取默认分支 commit，再读取 `git/trees/<sha>?recursive=1` 和固定 SHA 的 root README；写 `meta.json`、`commit.txt`、`tree.json`、`manifest.json` 到缓存 | 11 个 commit；11 棵树均 `truncated=false` |
| 初筛 | `re.search(r'evol|learn|improv|reflect|optim|memory|train|holdout|evaluat|自进|自我|进化', line, re.I)`；另按相关路径筛文件树 | 列出 README 命中行与源码路径；未下载 node_modules 或数据集 |
| 首批源码 | 按报告六个核心项目的目录筛选 raw 固定 SHA 文本，`ThreadPoolExecutor(max_workers=16)` | `requested: 218, saved: 218, errors: []` |
| 补充工具包 | 修正路径匹配，读取五个 RSI toolkit 的 skill 文本 | `Saved 15 RSI skill files` |
| 补充接线 | 读取评价 skill、依赖声明、allowlist、测试等固定文件 | `Additional requested: 16` |
| 依赖定位 | 查询 `openJiuwen/agent-core` 的固定提交树 | HTTP 404；未把它当可用来源 |
| 依赖定位 | 查询 `openJiuwen-ai/agent-core` 同一固定提交树 | `commit found 7808` |
| 依赖源码 | 从依赖固定 SHA 下载 harness RSI、judge、reviewer 与专项测试 | `Pinned dependency sources saved: 29` |
| 补充追踪 | 读取 Founder 启动与 agent 提示接线、记忆评分策略等 | `Additional static sources saved: 24` |
| 真实调用方 | 读取 Founder `internal/subconscious/*.go` | `FounderOS subconscious files: 14` |
| 时间与清单 | `datetime.datetime.now(datetime.timezone.utc).isoformat()`；枚举已保存元信息及缓存文件 | `2026-10-18T06:22:37.890068+00:00`；当时缓存 `357` 文件，含元信息 |

另使用只读 Read/Grep 工具核对本文全部引用行，包括实现、调用方和测试断言。一次 System 2 writer 的 grep 返回 `Permission denied: grep`，未重试或绕过。曾有两个缓存路径不存在的 Read；随后没有引用不存在的文件。

本地只读约定文件不列入公共引用清单。未读取任何 secrets、用户对话库、模型缓存或登录状态。未操作标签，未触碰选型页和收录 worker 文件。

### 未运行项

- 没有运行 npm、pip、uv、brew、Docker、项目测试、示例、benchmark、模型调用或上游 installer。
- 没有运行 Headroom 的扫描/分析命令。其 integration 测试可能读取本机会话，故连“试一下”也未执行。
- 没有验证 OS sandbox、rubric 读权限、真实 provider 路由、成本账单、模型泛化或训练数据泄漏。
- 没有为六个框架建立统一任务集。本文没有跨项目性能排名。

## 事实核验裁决

**有保留放行：限源码机制报告，不放行为安装或自动写全局配置的依据。**

| 核心断言 | 判定 | 实现及交叉证据 | 不能外推 |
|---|---|---|---|
| Penguin 不复算平均分 | 有据 | 解析器与故意不一致的测试 | 不等于所有上游分数都错 |
| Jiuwen 单 harness 内部 holdout 被置零 | 有据 | 构造器与专项测试 | 不等于用户不能另设外部验收 |
| Headroom apply 直接写指令文件 | 有据 | CLI 调用顺序与 writer | 不等于默认就写全局文件 |
| Atomic 标签进化与白名单分支 | 有据 | 调用点、变更器、非空白名单测试 | 空集合风险未做动态复现 |
| Hy 的 schema 强证据门默认关闭 | 有据 | 开关及函数早返回 | 不等于模型每次都会违反提示 |
| Founder queue apply 只更新 Q | 有据 | 完整函数体及 Process 状态转移 | 不等于其他反馈路径不存在 |
| 六者能提高个人 harness 效果 | 未验证，正文已限定 | 无个人封存任务实验 | 不作收益承诺 |

所有公开源码链接钉到 40 位 commit，附行号。上游 README 的效果与训练声明只作为其声明，不当成本轮独立验证。

交付前执行了独立文本校验：逐个核对引用的 commit、缓存文件与行号，检查未定义/未使用引用、六个核心章节和私人路径。也执行 `git diff --check -- intake/tabs-2026-10-18/evolution-evidence.md`，输出为空。它们只验证报告完整性，不执行上游代码；最终机器输出以交付会话记录为准。

## 固定提交来源

取用日期均为 2026-10-18 UTC。下列是实际读取的文件版本；同一引用可覆盖其所属段落中的连续实现事实。

[rea]: https://github.com/morluto/rea/blob/b83b9caf4a5f0241a5fd370792f1aed1bffbb2cf/README.md#L6-L10
[osiris]: https://github.com/simplifaisoul/osiris/blob/07a24fc9b7504e021965bcaa57f7d04d51d0a7ed/README.md#L3-L14
[mesh]: https://github.com/google/agentmesh/blob/c34e3ca698425c6a1120c93d8d84f27d288775fc/README.md#L7-L24
[openflux]: https://github.com/p1neappleXpress/OpenFlux/blob/edcf77a1848a72370cfba9f346d3b897b61e7e7d/README.md#L1-L7
[jarvis-graph]: https://github.com/isair/jarvis/blob/380cf069714e819e11c6479d3fc20a19191d0dee/src/jarvis/memory/graph.py#L98-L121
[penguin-readme]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/README.md#L50-L74
[penguin-contract]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/plugins/default-rsi-toolkit/skills/agent-optimization/SKILL.md#L9-L47
[penguin-loop]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/plugins/default-rsi-toolkit/skills/agent-optimization/SKILL.md#L49-L134
[penguin-retry]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/plugins/default-rsi-toolkit/skills/agent-optimization/SKILL.md#L92-L98
[penguin-eval]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/plugins/agent-evaluation/skills/agent-evaluation/SKILL.md#L55-L105
[penguin-score]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/packages/server/src/services/benchmark-service.ts#L225-L319
[penguin-score-test]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/packages/server/test/benchmarks.test.ts#L302-L334
[penguin-demo]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/examples/self-improving-agent/self-evolve.ts#L39-L169
[penguin-stop]: https://github.com/Prism-Shadow/penguin-harness/blob/7e08d23f67e8f3945d37fbc793d398d55454b9bd/plugins/continual-learning/hooks/stop.mjs#L177-L219
[jiuwen-doc]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/docs/en/SkillSelfEvolution.md#L9-L55
[jiuwen-rails]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/jiuwenswarm/agents/swarm/providers/evolution_rails.py#L488-L504
[jiuwen-leader]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/jiuwenswarm/agents/swarm/providers/evolution_rails.py#L584-L642
[jiuwen-member]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/jiuwenswarm/agents/swarm/providers/evolution_rails.py#L779-L847
[jiuwen-library]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/jiuwenswarm/agents/swarm/providers/evolution_rails.py#L99-L113
[jiuwen-dep]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/pyproject.toml#L16-L21
[jiuwen-provider]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/jiuwenswarm/agents/harness/common/rsi/harness_provider.py#L157-L249
[jiuwen-activate]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/jiuwenswarm/agents/harness/common/rsi/harness_activation.py#L79-L154
[jiuwen-activate-test]: https://github.com/openJiuwen-ai/jiuwenswarm/blob/660d28b26c70390ac1ac8f48dc1513dd149983ed/tests/unit_tests/rsi/test_harness_activation.py#L260-L366
[core-surfaces]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/single_harness/iterative.py#L84-L85
[core-no-holdout]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/single_harness/iterative.py#L150-L174
[core-no-holdout-test]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/tests/unit_tests/rsi/test_single_harness_iterative.py#L1434-L1513
[core-promote]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/single_harness/iterative.py#L833-L1015
[core-reviewer]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/harness/rails/evolution/review/subagent.py#L23-L171
[core-skill-score]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/agent_evolving/optimizer/skill_call/experience_optimizer.py#L46-L58
[core-verify]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/member_optimizer/verification.py#L1-L104
[core-script]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/evaluator/judger/script_based.py#L31-L134
[core-judge]: https://github.com/openJiuwen-ai/agent-core/blob/4e6e53d4f3a97e4f39651be337ba309835de15e0/openjiuwen/rsi/harness_rsi/evaluator/judger/llm_as_judge.py#L50-L114
[headroom-cli]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/cli/learn.py#L70-L171
[headroom-flow]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/cli/learn.py#L289-L359
[headroom-backend]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L43-L217
[headroom-analyze]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L230-L287
[headroom-digest]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L355-L512
[headroom-objective]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L519-L590
[headroom-parse]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L1109-L1152
[headroom-api]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/analyzer.py#L1063-L1101
[headroom-merge]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/writer.py#L302-L370
[headroom-writer]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/writer.py#L487-L665
[headroom-target]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/headroom/learn/writer.py#L530-L542
[headroom-tests]: https://github.com/headroomlabs-ai/headroom/blob/fbf7bc3278c11975299b9bd0a2ecf200dfd25a05/tests/test_learn/test_integration.py#L1-L179
[atomic-input]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/reflection/reflection-runner.ts#L29-L97
[atomic-reflect]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/reflection/reflection-runner.ts#L334-L479
[atomic-write]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/reflection/reflection-runner.ts#L334-L479
[atomic-allowlist]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/reflection/reflection-runner.ts#L762-L784
[atomic-evolve]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/evolution/neighbor-evolver.ts#L10-L175
[atomic-vote]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/voting/vote-runner.ts#L224-L301
[atomic-vote-prompt]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/voting/vote-prompt.ts#L24-L101
[atomic-distill]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/consolidator/distill-runner.ts#L24-L103
[atomic-consolidate]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/consolidator/consolidator-job.ts#L479-L610
[atomic-cold]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/consolidator/consolidator-job.ts#L14-L52
[atomic-evolve-test]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/src/memory/evolution/neighbor-evolver.test.ts#L121-L184
[atomic-audit]: https://github.com/AtomicBot-ai/atomic-agent/blob/7899d173e0a07665f45cf014de065eb38f405127/eval-memory/experiments/e3-reflection-audit/runner.ts#L81-L169
[hy-readme]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/README.md#L24-L56
[hy-defaults]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_agent.py#L72-L94
[hy-system2]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_agent.py#L1-L17
[hy-skip]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_agent.py#L967-L979
[hy-evidence]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_agent.py#L746-L837
[hy-evolve]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_writer.py#L1152-L1239
[hy-writer]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/coding/writer.py#L1-L63
[hy-crosslink]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/coding/writer.py#L196-L279
[hy-judge]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/coding/judge.py#L1-L16
[hy-tools]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/pipelines/system2_tools.py#L599-L872
[hy-chain]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/hy_memory/coding/chain_store.py#L1-L53
[hy-tests]: https://github.com/Tencent-Hunyuan/Hy-Memory/blob/0c59413ad81158a3bd4748beb7bdda354659b3af/tests/coding/test_writer_e2e.py#L141-L181
[founder-wire]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/cmd/server/bootstrap.go#L891-L973
[founder-actuator]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/feedback/prompt_actuator.go#L54-L143
[founder-pattern]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/subconscious/pattern_extractor.go#L29-L137
[founder-block]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/subconscious/block_accumulator.go#L119-L204
[founder-q]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/feedback/self_improvement.go#L126-L337
[founder-queue]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/feedback/task_queue.go#L94-L200
[founder-fact]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/optimal-engine/lib/optimal_engine/memory_core/fact_promoter.ex#L1-L29
[founder-policy]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/optimal-engine/lib/optimal_engine/memory_core/scoring_policy.ex#L74-L244
[founder-scheduler]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/optimal-engine/lib/optimal_engine/memory_core/promotion_scheduler.ex#L1-L39
[founder-q-test]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/desktop/backend-go/internal/feedback/self_improvement_test.go#L151-L220
[founder-fact-test]: https://github.com/Bennettxai/FounderOS/blob/5460099e2c5181e3841ad6a0ceea85dd73387782/optimal-engine/test/memory_core/claim_review_test.exs#L51-L80
