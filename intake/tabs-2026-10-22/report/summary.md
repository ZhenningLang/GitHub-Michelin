# 标签收录完整报告：本轮复核与累计成果

五项资格问题仍待裁决；本轮没有新增选型页。
当前六个仓库标签全部来自上一轮保留项，不是六个新发现项目。重复执行不等于自动豁免来源或许可检查。

## 本轮结论与统计

| 结果 | 本轮 2026-10-22 | 上轮已合并成果 |
|---|---|---|
| 新增项目页 | 0 | 17 对中英文页 |
| 刷新已有页 | 0 | 6 项 fresh，未刷新事实 |
| 暂缓 proposed | 5 | 相同的 5 项，不重复计数 |
| 自有项目跳过 | 1 | 相同的 1 项，不重复计数 |
| failed | 0 | 0 |
| 关闭仓库标签 | 0；本轮没有 done 仓库 | 已完成的 23 项全部关闭 |

本轮新核四个公开候选的默认分支，以及两条非公开记录的可见性元数据。三项公开候选提交未变；dzhng 新增一项提交，但没有修复许可声明缺口。
非公开候选和自有私有仓库均匿名。没有读取它们的内部内容，也没有改写既有 Git 历史；匿名承诺针对本轮新产物，不声称清除过去已经发布的标识。

上轮结果已通过 [PR #201](https://github.com/ZhenningLang/GitHub-Michelin/pull/201) 合并。本轮报告不把历史页表述成今天重新研究、安装或运行过的项目。

## 当前仍开着的项目与裁决点

| 项目 | 本轮查到的变化 | 为什么仍不建页 | 维护者可决定什么 |
|---|---|---|---|
| breferrari/obsidian-mind | 默认分支提交未变；补读双方 MIT 及两段记忆实现。 | 沿用旧树／全文取证：复制的上游内容未保留原作者 MIT 声明。不是对整个项目原创性的否定。 | 等补齐声明，或在核对权利依据后明确授权带警告收录。 |
| dzhng/skills | 新增一个提交，修改四份测试规范；小黑复制子树的 blob 映射未变。 | 重新读当前许可、README 和子树六份 Markdown，原作者版权与许可声明仍未补齐。 | 保留工程核心的价值判断，但不能用根 MIT 替第三方素材背书。 |
| JimLiu/baoyu-design | 默认分支提交未变；复用固定版本的来源记录。 | 项目记录了 Claude Design 产品前端提取内容，既有所读资料未提供该部分再许可证明。 | 先补可核验授权依据，或明确决定如何限定可介绍、可复用的部分。 |
| liseami/CCBaga | 默认分支提交未变；本轮重读 NOTICE。 | NOTICE 仍明示复制 UI 子树缺独立许可声明，要求确认再分发条款。 | 等上游补证，或另审证据后决定是否带明确告警收录。 |
| 一个非公开候选 | 仅查可见性与检测许可元数据。 | 公开索引读者不能访问它；本轮没有公开可核验的开源资格依据。 | 先决定是否公开并补齐许可，不从私有材料生成公开选型页。 |
| 一个自有私有仓库 | 元数据确认私有。 | 自有项目按本 skill 范围跳过，与技术优劣无关。 | 不需要为本轮收录操作；标签保留。 |

以上是收录资格的待裁决状态，不是侵权判决。GitHub 检测到 MIT，也不证明第三方部分的许可已经闭合；检测许可为空，也不能单独证明内部没有 LICENSE。

## 公开候选的证据与用途

### Obsidian Mind：工作知识库，不是无条件共享记忆

它把工作记录、跨会话教训和关联笔记留在 Markdown／Obsidian 体系，结合 hooks 和工具检索。适合研究人能读、能追溯的知识库；代价是模板、宿主兼容和整理流程都要维护。

本轮确认目标仍为 [`fae7be46`](https://github.com/breferrari/obsidian-mind/commit/fae7be467fc5e23bf9d51df7207d41f0c07e2754)。[目标 MIT](https://github.com/breferrari/obsidian-mind/blob/fae7be467fc5e23bf9d51df7207d41f0c07e2754/LICENSE#L1-L13)只署 Brenno Ferrari；[上游 MIT](https://github.com/kepano/obsidian-skills/blob/3ccff5338ea700537839b21900aa5358a0402c98/LICENSE#L1-L13)署 Steph Ango，并要求保留声明。
十个同 blob 文件和 325 个文本文件的缺声明扫描，明确复用[上轮取证](../../tabs-2026-10-21/proposals.md#breferrariobsidian-mind)，不是本轮重新全量扫描。

可研究[显式召回范围](https://github.com/breferrari/obsidian-mind/blob/fae7be467fc5e23bf9d51df7207d41f0c07e2754/.claude/scripts/lib/memory-recall.ts#L216-L245)和[按字节分级注入](https://github.com/breferrari/obsidian-mind/blob/fae7be467fc5e23bf9d51df7207d41f0c07e2754/.claude/scripts/lib/session-start.ts#L130-L209)。后者不是无条件硬上限：非正数预算会返回完整内容，不可降级部分也没有在本轮证明总能满足预算。

### dzhng/skills：选择审计有价值，许可缺口没有随测试更新消失

原创工程核心围绕探索、规格、分片实施、测试与选择审计。最有价值的角度是把规格留白处的决定从大 diff 中单独提出；账本依旧依赖模型与项目验证，不是授权硬门。

默认分支从 `dc8f546c` 前进到 [`8e74252a`](https://github.com/dzhng/skills/commit/8e74252ad975acff3de6305299cf82c4b14cc026)。[四文件差异](https://github.com/dzhng/skills/compare/dc8f546c3adaa615ab86e8328449ae6efe23aca4...8e74252ad975acff3de6305299cf82c4b14cc026)涉及回归测试优先放在端到端／系统层、单测服务具体反馈效率的策略，没有许可修复。
这不意味着应删除现有单测或改掉本地 TDD；这里只记录上游的新主张，本轮未验证收益，也未改变个人规则。

[当前根许可](https://github.com/dzhng/skills/blob/8e74252ad975acff3de6305299cf82c4b14cc026/LICENSE#L1-L13)仍只署 David Zhang；[原作者许可](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/686575741a61e2c0be5e4c6d3615ebf6217dd322/LICENSE#L1-L13)署 Ian。新旧完整树对比确认复制子树未变；本轮重新检查其六份 Markdown 与许可路径，不能用 README 致谢代替完整声明。
机制入口是[选择审计账本](https://github.com/dzhng/skills/blob/8e74252ad975acff3de6305299cf82c4b14cc026/skills/engineering/audit-choices/SKILL.md#L96-L136)和[证据 receipts 的能力边界](https://github.com/dzhng/skills/blob/8e74252ad975acff3de6305299cf82c4b14cc026/skills/visual/screenshot-critique/scripts/receipts.mjs#L9-L19)：数字旁有命令转录，不等于命令真实执行过。

### baoyu-design：可复用接线不等于提取内容全部获许可

既有研究发现本地设计脚本、组件、设计系统绑定和导出编排，不是空仓库。它能作为本地设计工作流的候选，但许可来源必须先讲清楚。

当前仍为 [`65300335`](https://github.com/JimLiu/baoyu-design/commit/6530033592bf7fa58bc1a5a2a2ad278da45213a9)。[Credits](https://github.com/JimLiu/baoyu-design/blob/6530033592bf7fa58bc1a5a2a2ad278da45213a9/README.md#credits--license)、[提取来源](https://github.com/JimLiu/baoyu-design/blob/6530033592bf7fa58bc1a5a2a2ad278da45213a9/skills/baoyu-design/references/upstream-sync/provenance.json)和[复制记录](https://github.com/JimLiu/baoyu-design/blob/6530033592bf7fa58bc1a5a2a2ad278da45213a9/skills/baoyu-design/references/upstream-sync/apply-report.json)沿用上轮固定证据；本轮没有重新抓取整个仓库或完成新一轮法律授权审计。
提交未变只证明该提交树的文件未变，不证明站外协议、其他分支或所有授权事实均未变化。

### CCBaga：归档恢复思想可研究，不能替整包授予 MIT

它有实质身份归档、恢复和浏览器环境实现。研究价值不因凭据功能或删除能力而被否定；同样，恢复步骤存在也不证明崩溃恢复一定成功。

当前仍为 [`bdfb90ce`](https://github.com/liseami/CCBaga/commit/bdfb90ceadfc5fae6772ffff597bddecb0b73cc3)。本轮重新读取 [NOTICE](https://github.com/liseami/CCBaga/blob/bdfb90ceadfc5fae6772ffff597bddecb0b73cc3/NOTICE.md#vendored-interface)：复制组件缺独立声明、需确认再分发条款的文字仍在。根 MIT 不替代其他版权人的许可。
[先校验归档、保存当前状态、设置待恢复标记并处理回滚](https://github.com/liseami/CCBaga/blob/bdfb90ceadfc5fae6772ffff597bddecb0b73cc3/src-tauri/src/identities/store.rs#L452-L630)的实现判断沿用旧静态源码证据；本轮没跑恢复，也没读取个人凭据。

## 已完成项目的完整用途索引

下面是上轮已合并的 17 个新增项目，不是本轮新增。用途与限制复用已读的[上轮完整报告](../../tabs-2026-10-21/report/summary.md)，仍按其原核验日期理解，不冒称今天重核了全部上游。

| 项目 | 何时想到它 | 决定性边界 |
|---|---|---|
| [LCU](../../../categories/desktop-automation/lcu.zh.md) | 现有编程助手要操作原生桌面应用。 | 依赖本机闭源引擎，不自带虚拟机；Linux 没有逐应用授权。 |
| [ZCode](../../../categories/agent-frameworks/coding-agents/terminal-agents/vendor-agents/zcode.zh.md) | 想统一桌面、Web 和 CLI 的自带 agent 运行时。 | 默认无系统沙箱，开放构建缺原生 Computer Use。 |
| [FounderOS](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/founderos.zh.md) | 单人业务要同时看收入、收件箱与 agent 工作。 | 是监管界面，不是安装即运行的自治公司；真实执行另接服务。 |
| [Nezha](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/nezha.zh.md) | 监管 Claude Code／Codex 的任务、终端和 Git。 | 默认本地目录，工作树须主动选；会改全局 hook，存在绕过参数。 |
| [leanrea](../../../categories/agent-skills/security/leanrea.zh.md) | 授权范围内解释成品应用的一项功能。 | 短指令不是分析引擎；危险命令与缺失脚本不适合无人值守。 |
| [SAG](../../../categories/rag-retrieval/structured-retrieval/sag.zh.md) | 相似段落检索不足以连接跨文档事件。 | 默认快速策略不走完整扩展；单用户边界不是租户隔离。 |
| [EmDash](../../../categories/content-management/emdash.zh.md) | Astro 网站需要数据库驱动的编辑后台。 | 不继承 PHP 插件；原生插件与沙箱插件权限不同。 |
| [OXR](../../../categories/document-parsing/model-backed-pdf/oxr.zh.md) | 科研 PDF／图片需要拆开版面检测与识别。 | GPU 与商业许可门槛；内存任务不是持久队列，占位 key 不是鉴权。 |
| [Biscotti](../../../categories/meeting-intelligence/biscotti.zh.md) | Mac 本地会议录制、会后转写与摘要。 | Apple Silicon、macOS 15 以上；非竞争许可，MCP 开放本机读取。 |
| [twitter-cli](../../../categories/social-media-management/twitter-cli.zh.md) | 把个人 X 书签与信息流交给脚本。 | 非官方会话客户端，兼容性与账号风险不能由延迟／指纹选项消除。 |
| [md2wechat](../../../categories/social-media-management/md2wechat-skill.zh.md) | 检查 Markdown、预览排版、明确创建公众号草稿。 | 主排版依赖付费服务且受商用限制；AI 模式只交接提示词。 |
| [gzh-design-skill](../../../categories/agent-skills/ai-writing/content-production/gzh-design-skill.zh.md) | 对已有文章套主题组件后手动复制。 | 不是自动发布或确定性排版；零退出不等于正文与手机效果验收通过。 |
| [KiviDB](../../../categories/databases/database-engines/kividb.zh.md) | Redis 风格存储需要同库文本／向量搜索。 | AGPL、短历史、兼容与恢复语义需验证；确认写入不等于同步落盘。 |
| [microG](../../../categories/android-system-services/microg-gmscore.zh.md) | 自定义安卓系统仍需兼容现有 Google 服务调用。 | 替客户端不等于替 Google 后端；签名与逐应用兼容需系统支持。 |
| [GameDev Agent Skills](../../../categories/agent-skills/engineering/awesome-gamedev-agent-skills.zh.md) | 补游戏引擎版本、玩法与素材领域配方。 | 技能文本不是编辑器连接；最终还要编译和场景测试。 |
| [Unity-MCP](../../../categories/game-dev/unity-mcp.zh.md) | 让助手真实读取、修改 Unity 场景和运行编辑器工具。 | 编辑器执行权限不是沙箱；混合许可不能只看根 Apache。 |
| [紫微斗数](../../../categories/traditional-divination/ziwei-doushu.zh.md) | 研究传统排盘规则与文化娱乐界面。 | 不含完整商业后端；时间边界与引文权利需核对，不验证预测有效。 |

上轮还核对了六个 fresh 项目：

| 项目 | 使用判断 | 原核验日 |
|---|---|---|
| [AgentsView](../../../categories/agent-tooling/session-history/agentsview.zh.md) | 跨助手会话检索与用量分析，不是生产 LLM 追踪平台。 | 2026-09-28 |
| [Taste-Skill](../../../categories/agent-skills/design/ui-taste/taste-skill.zh.md) | 缺设计系统时补品味输入，不叠加第二套相互冲突的规范。 | 2026-09-27 |
| [Agent Orchestrator](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/agent-orchestrator.zh.md) | 多分支监管与反馈回送；单助手通常不需要整套控制平面。 | 2026-09-28 |
| [SolidCraft](../../../categories/cad/solidcraft.zh.md) | 可编辑参数的零件原型，不独撑生产关键工程。 | 2026-10-18 |
| [wshobson/agents](../../../categories/agent-skills/subagent-collections/wshobson-agents.zh.md) | 按域取专家，不把大目录整包叠到已有技能栈上。 | 2026-09-28 |
| [Android Skills](../../../categories/agent-skills/vendor-collections/product-vendors/android-skills.zh.md) | 用平台官方流程补特定 Android 任务，不替代开发生命周期和 CI。 | 2026-09-22 |

两轮去重后仍是同一组 29 个候选：23 项已有页面、5 项待裁决、1 项自有跳过，不是 35 个新项目。

## 对个人 harness 的借鉴裁决

只记机制候选，不启动实验，不安装整包，不改 dotfiles。下列 medium 表示值得比较的思想，不表示现有系统存在已证实缺陷或收益已经实测。

| 优先级／适配 | 思想与边界 | 对应落点 | 本地阅读入口 |
|---|---|---|---|
| 优先，medium | dzhng：把规格留白的选择、影响、信心和裁决写成单独账本；静态转录不冒充执行证据。 | 边界决策账本、`guard-review`、`guard-verify`。保留现有审批，不抄五分钟无人回复即决定的策略。 | 本报告“dzhng/skills”节；未建选型页。 |
| 后续，medium | Obsidian Mind：显式记忆可见性与分级降级清单；不能把预算策略当绝对硬上限。 | `assist-mem`、`compact-memory`、上下文 capsule。先比现有作用域和丢弃计数，不替换账本。 | 本报告“Obsidian Mind”节；未建选型页。 |
| 后续，medium | CCBaga：归档先验收，当前状态先检查点，再提交恢复标记和回滚。 | `dev-operational-task`、`guard-gitops`。仅思想候选，不接入身份轮换、指纹或凭据处理。 | 本报告“CCBaga”节；未建选型页。 |
| 已有，high | AgentsView 的跨助手日志归一化和检索已在现有取数链中。 | `agent-harness-improvement`。这是已接入的数据源，不重复建设或吸收耦合其库表的内部记忆模块。 | [本地页](../../../categories/agent-tooling/session-history/agentsview.md) |
| 延续，medium | ZCode 的声明摘要绑定授权、LCU 的宿主自审批防护、FounderOS 的待人裁决队列。 | hooks 信任准入、`computer-use`、`dev-long-run`／`sidecar`。全部仅设计参考，不搬自动授权与全局配置接管。 | [ZCode](../../../categories/agent-frameworks/coding-agents/terminal-agents/vendor-agents/zcode.md)、[LCU](../../../categories/desktop-automation/lcu.md)、[FounderOS](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/founderos.md) |

baoyu-design 本轮没有足够新增证据支持 medium／high 接入建议；非公开候选和自有项目不做内部机制挖掘。其余已收录项目的逐项中高适配判断与本地页路径，见[上轮机制表](../../tabs-2026-10-21/report/summary.md#可借鉴的-harness-机制)。
没有本地选型页的 proposed 不会被伪装成已收录；本报告的固定源码与证据节是临时研究入口，不替代正式页面。

## 对比选题池

本轮没有新增覆盖，因此没有“因本轮入库而新达四项”的分类。以下延续已有四项以上的比较池，且不把未收录的 proposed 计入项目数：

- **记忆与上下文：** 作用域隔离、分级注入和可见降级分别解决什么，哪些已经被现有轻量账本覆盖？
- **工程技能：** 选择审计与端到端回归如何补 TDD，什么时候只是增加另一套指令？
- **设计与内容生产：** 设计系统、主题组件与发布 CLI 各负责到哪一步，许可和完成证据怎么分开？
- **agent 监管：** 会话入口、待人裁决队列和 PR／CI 自动回送，究竟缺哪一层才值得加控制平面？

更完整的桌面、数据库、检索、游戏、社媒和文档解析问题见[上轮选题池](../../tabs-2026-10-21/report/summary.md#横向对比选题池)。这些是选题，不是本轮追加开发承诺。

## 验证范围与不确定性

本轮新核：本人 Chrome 标签、公开性、默认分支 SHA、dzhng 的四文件增量与相关许可子树，以及部分固定许可／NOTICE。其余固定提交的已读事实明确复用上轮材料。
提交相同只约束该 git 树；不证明站外授权、其他分支、分发包、作者承诺或未来状态未变。缺少公开补证不等于已证实没有私下授权。

本轮没有安装／执行上游、读取业务凭据、接入模型或调用付费接口。没有新页面，因此不会以空范围扫描冒充内容页验收，也不重打健康度雷达或改核验日期。
上轮已披露的健康卡排版问题、中文对比行漏译和旧事实口径差异不是本轮修复目标；不声称它们已修复。

自动验证与最终标签对账记录在本轮 `verification.json`；门禁、工具测试和报告审查结果在发布记录中给出。

本轮已复跑的关键输出：

```text
make gates: 202 category nodes, 948 EN + 948 ZH pages, 0 errors, 1572 warnings.
reverse_index check: reports are current, no full mislabels.
make test: Ran 483 tests in 26.435s; OK; no skipped.
browser acceptance: 6 terminal rows; 5 proposed; 1 skipped; 0 failed.
browser acceptance: all 6 intended tabs retained; 0 unmatched repositories.
```

这些是索引和本轮操作的验证，不是对未建页项目的运行或安全认证。项目页、分类、工具及反向索引的 git diff 均为空，没有借报告修改事实或修上轮遗留问题。
Inner-loop evidence：本轮门禁、工具单测、报告与链接检查。
Acceptance evidence：真实标签与匿名公开台账一致；四项资格复核有当前提交依据；proposed／自有标签全部保留。
Holdout / unseen evidence：不适用模型效果评测，以真实提交差异与许可边界交叉核对；没有独立运行留出集。
Holdout 来源类别：真实捕获；历史事实另标为复用证据。
预期值来源：用户需求、仓库收录契约与固定版本来源，而非模型自行扩张的许可门槛。
本次改动相对冻结点的位置：只新增本轮台账、证据摘要和报告；不改项目页、分类、工具、门禁或个人 harness。

下一步：维护者裁决五项资格问题。有可核验补证后再完整建页，不用反复执行来替代裁决。
