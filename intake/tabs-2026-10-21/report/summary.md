# Chrome 项目收录与选型总结

五项资格问题待裁决；md2wechat 的健康卡有既有模板文字溢出。
本批不安装上游，也不修改个人 harness。暂缓项目保留标签，不当成已收录。
运行中又出现 `isjiamu/gzh-design-skill`，已分派独立调研；本页仍会补充该项结果。

## 先看结论

这批项目解决三类问题：让 agent 操作工具、把资料变成可用内容，以及替换现有基础组件。
不要把“技能指令”“真实工具权限”“完整应用”混为一谈。前者教模型怎么做，后两者才实际接触编辑器、桌面、数据库或账号。

对个人 harness，值得优先研究的是 **ZCode 的授权失效机制、LCU 的自审批防护，以及 FounderOS 的待人裁决队列**。
这些只是机制候选，不代表整包接入更好。AgentsView 已是现有工作流的数据源，不需要再造一套。

## 收录进度

| 状态 | 当前结果 |
|---|---|
| 新增 | 16 个项目已逐项提交，门禁通过，标签已全部关闭 |
| 已有页面 | 6 个 fresh，保留原页和核验日期，标签已关闭 |
| 暂缓 | 5 个，具体证据见下文与待裁决记录 |
| 自有项目 | 1 个，不收录、不关标签 |
| 运行中新增标签 | `isjiamu/gzh-design-skill`，重扫后共 29 条；其余均已终结 |
| 公开发布 | 仅发布脱敏分支，经 PR 与 CI 进入主干；远端状态以本批 PR 为准 |

批次开始于 **2026-10-21 UTC**，运行中跨到次日；新增页使用各自实际核验日，不倒填批次日期。已有六页按 90 天门槛判定 fresh，不声称重新读过其上游。
健康度是自动信号汇总，不是产品质量或生产适用性的认证。

## 新增项目：什么时候选，什么时候避开

| 项目 | 真正解决的问题 | 决定性取舍与边界 |
|---|---|---|
| [LCU](../../../categories/desktop-automation/lcu.zh.md) | 现有编程 agent 卡在原生应用弹窗，无法完成导出等操作。 | 复用已装 ChatGPT 应用的电脑控制引擎，不必更换 agent；但依赖闭源运行时，Linux 没有逐应用授权，也不自带虚拟机。 |
| [ZCode](../../../categories/agent-frameworks/coding-agents/terminal-agents/vendor-agents/zcode.zh.md) | 希望桌面、网页和 CLI 使用同一套 agent 与任务工作流。 | 它提供自己的运行时，不只是包一层现有 CLI；默认没有操作系统沙箱，开放构建的原生 Computer Use 不可用。 |
| [FounderOS](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/founderos.zh.md) | 一个人经营业务，要在收件箱、收入和 agent 工作之间来回查。 | 它是可修改的业务监管界面，不是安装即运行的自治公司。真实 agent 看板依赖另设的 Paperclip；演示数据和已配置徽标不证明真实业务已接通。 |
| [Nezha](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/nezha.zh.md) | 多个 Claude Code／Codex 任务看起来都安静，需要找出待审批和待验收的那个。 | 本地桌面工作台集成终端、会话、文件与 Git；默认是本地目录，工作树须主动选。启动会改 Codex 全局 hook，部分启动参数绕过审批或信任，不能把工作台当沙箱。 |
| [leanrea](../../../categories/agent-skills/security/leanrea.zh.md) | 只想解释成品应用的一项功能，agent 却反复挑工具和读整包脚本。 | 短指令减少接线成本，但不提供分析引擎或证据账本。当前有危险清理、转义管道和缺失脚本，只适合授权范围内、有人监督的调查。 |
| [SAG](../../../categories/rag-retrieval/structured-retrieval/sag.zh.md) | 相似段落检索答不出跨文档的事件与实体关系。 | 提供个人资料库、关联检索和引用读取；默认快速策略不走完整扩展路径，默认名字登录与全库 MCP 也不是租户隔离。 |
| [EmDash](../../../categories/content-management/emdash.zh.md) | Astro 网站编辑改一个标题也要提 PR 和重建。 | 在 Astro 内加编辑后台与数据库，不是兼容 PHP 插件的 WordPress 替代安装包。插件沙箱按平台不同，原生插件不受其隔离。 |
| [OXR](../../../categories/document-parsing/oxr.zh.md) | 多栏 PDF 的文字、公式和表格解析混在一起，想独立替换区域检测器。 | 专门的 PDF／图片 GPU 服务，不是通用格式转换。源码可见许可含规模与托管竞争限制；占位 key 不等于鉴权，内存任务也不适合直接当持久批处理队列。 |
| [Biscotti](../../../categories/meeting-intelligence/biscotti.zh.md) | 想在 Mac 本地保存会议、分辨说话人并生成会后摘要。 | 不需要云推理账号，但限 Apple Silicon、macOS 15 及以上；不是会中行动 agent。PolyForm Perimeter 禁止竞争用途，MCP 开启后本机程序可读会议。 |
| [twitter-cli](../../../categories/social-media-management/twitter-cli.zh.md) | 想把自己的 X 书签和信息流接给终端脚本。 | 无需另建开发者应用，但把会话 cookie 交给非官方 HTTP 客户端。搜索修复尚未合并，鉴权失败还能回读其他浏览器，不宜作为稳定业务数据源。 |
| [md2wechat](../../../categories/social-media-management/md2wechat-skill.zh.md) | Markdown 成稿还要补封面、检查图片与元数据，再创建公众号草稿。 | 完整 Go CLI 加操作规程，不只是技能文本。主排版路径依赖付费服务并外发文章；公司营收相关工作与客户交付受许可限制，AI 模式只返回待执行提示词。其他平台仍由宿主浏览器完成。 |
| [KiviDB](../../../categories/databases/database-engines/kividb.zh.md) | Redis 风格业务还需要同库关键词与向量检索。 | 内置搜索与多核实现减少一份存储，但 AGPL、短公开历史及兼容／恢复边界需要验证。当前只有每秒刷盘，确认写入不等于同步落盘。 |
| [microG](../../../categories/android-system-services/microg-gmscore.zh.md) | 不带 Google 套件的安卓系统仍要运行已有应用。 | 替换设备上的服务实现，不替换 Google 后端。通常需要系统支持签名伪装；银行、完整性检查和推送兼容性要逐应用验收。 |
| [GameDev Agent Skills](../../../categories/agent-skills/engineering/awesome-gamedev-agent-skills.zh.md) | 通用 agent 混用引擎版本，缺跳跃、存档和发布的领域知识。 | 它是按引擎与版本选取的技能目录，不是编辑器连接。文字路由不能证明游戏能运行，仍需引擎编译和场景测试。 |
| [Unity-MCP](../../../categories/game-dev/unity-mcp.zh.md) | agent 写完 Unity 脚本，还要人手动挂组件、抄控制台错误。 | 真正连接编辑器并可执行 C#，不是仅给开发建议；权限面更大，也不是沙箱。根 Apache 许可不覆盖 Code-Exec 的 PolyForm Shield 例外。 |
| [紫微斗数](../../../categories/traditional-divination/ziwei-doushu.zh.md) | 需要研究传统排盘约定与文化娱乐界面，而不是重写整套排盘规则。 | 可复用引擎与演示，不含完整商业站后端和解读生成器。时间边界、流派默认与引文权利需核对；排盘一致不证明预测有效。 |

## 六个已有项目

| 项目 | 一句话判断 | 原核验日 |
|---|---|---|
| [AgentsView](../../../categories/agent-tooling/session-history/agentsview.zh.md) | 跨编码助手找历史、查用量；不是生产 LLM 追踪平台。旧快照记载默认遥测，零外联需要单独确认。 | 2026-09-28 |
| [Taste-Skill](../../../categories/agent-skills/design/ui-taste/taste-skill.zh.md) | 没有品牌系统时，用于减少生成 UI 的模板感；不要与现有品味规则整包叠加。 | 2026-09-27 |
| [Agent Orchestrator](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/agent-orchestrator.zh.md) | 监管多个隔离分支并回送 CI／评审反馈；单代理和无头流水线通常不值得增加桌面栈。 | 2026-09-28 |
| [SolidCraft](../../../categories/cad/solidcraft.zh.md) | 适合 agent 做可改尺寸的零件原型；不应独撑生产关键工程。 | 2026-10-18 |
| [wshobson/agents](../../../categories/agent-skills/subagent-collections/wshobson-agents.zh.md) | 按领域取现成专家，不要把大目录整包叠在已有技能栈上。 | 2026-09-28 |
| [Android Skills](../../../categories/agent-skills/vendor-collections/product-vendors/android-skills.zh.md) | 用平台官方流程补 Android 升级、构建和发布的特定知识，不替代通用开发流程或强制 CI 门禁。 | 2026-09-22 |

Agent Orchestrator 的仓库字段与正文归属名称不一致，Android Skills 的部分正文健康度口径也与 frontmatter 不一致，已记为后续刷新项；本批没有绕过 fresh 门槛顺手改事实。
其中 Agent Orchestrator 后因分类拆分搬迁路径，只改路由、相对链接及 category，未刷新事实和核验日期。

## 暂缓项目：不是永久拒收

| 项目 | 已查到的具体问题 | 本轮处理 |
|---|---|---|
| 一个非公开候选 | 未给出开源许可证，不适合直接发布到公开开源索引。 | 不披露名称、内部材料或实现细节，保留标签待裁决。 |
| JimLiu/baoyu-design | 自身来源记录承认提取 Claude Design 产品前端内容，提取内容的再许可未核清。 | 不把根 MIT 当作全部内容授权，也不作侵权判决。 |
| liseami/CCBaga | 上游 NOTICE 明示复制的 UI 子树缺独立许可声明，发布前须确认再分发条款。 | 不否定其原创身份归档实现，但不替第三方授权背书。 |
| breferrari/obsidian-mind | 十个文件与已署名上游 blob 一致，完整文本扫描未找到上游 MIT 版权声明。 | 按声明保留缺口待裁决，不称整个项目是复制品。 |
| dzhng/skills | 复制的小黑插画技能未保留原作者 MIT 版权及许可声明。 | 不否定工程技能核心；不直接安装或复制，先交维护者裁决。 |

公开证据与固定源码链接见[待裁决记录](../proposals.md)。原始私有记录仅留本地，公开分支不得包含该历史。

## 可借鉴的 harness 机制

以下均为建议，不是本次已实施功能，也不是已证实的现有缺陷。只列 medium／high，不为凑数量新增依赖。

| 优先级与适配度 | 项目与机制 | 对应落点 | 本地阅读入口 |
|---|---|---|---|
| 优先，medium | ZCode：把工作区身份与 Hook 声明摘要绑定；声明变化使旧授权失效，执行前再复核。 | hooks 的工作区信任准入；记忆整理只读权限与写入边界。不能把修改限制误当保密沙箱。 | [ZCode](../../../categories/agent-frameworks/coding-agents/terminal-agents/vendor-agents/zcode.md) |
| 优先，medium | LCU：在 macOS 拒绝控制承载 agent 的审批应用；给子 agent 独立轮次，避免子任务清理父任务。 | `computer-use` 授权边界与已有适配器的生命周期诊断。目前没有正式 OpenCode／kilo 适配器，不带入自动授权。 | [LCU](../../../categories/desktop-automation/lcu.md) |
| 后续，medium | FounderOS：分开展示已完成产物和待批准请求，优先显示逾期或有人等待的事项。 | `dev-long-run` 状态台、`sidecar` 通知呈现。文件命名只是展示线索，不是授权门。 | [FounderOS](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/founderos.md) |
| 后续，medium | GameDev Agent Skills：先查项目标记和锁文件，再选单引擎与专项技能，逐层读参考材料。 | `workflow-helper`、`think-context-map`。不把整个游戏目录常驻加载。 | [技能页](../../../categories/agent-skills/engineering/awesome-gamedev-agent-skills.md) |
| 已有，high | AgentsView：统一多个助手的会话日志，提供检索和分析入口。 | `agent-harness-improvement` 已将其作为取数源，不重复建设。 | [AgentsView](../../../categories/agent-tooling/session-history/agentsview.md) |
| 后续，medium | Taste-Skill：把布局变化、动效与密度变成明确输入。 | `fe-ui-design` 的可选设计约束，不覆盖品牌系统；反重复沿用 `fe-ui-critique`。 | [Taste-Skill](../../../categories/agent-skills/design/ui-taste/taste-skill.md) |
| 后续，medium | Agent Orchestrator：按分支归属回送 CI 与评审事件。 | `dev-long-run` 的事件归属；参考 `sidecar` 的裁决结构，但不扩大其单目标边界。 | [Agent Orchestrator](../../../categories/agent-tooling/supervision-surfaces/agent-cockpits/agent-orchestrator.md) |
| 后续，medium | SolidCraft：分发工具前检查参数和文件范围。 | `guard-secure` 的信任边界核查；路径范围不是进程沙箱，硬链接仍要考虑。 | [SolidCraft](../../../categories/cad/solidcraft.md) |
| 后续，medium | wshobson/agents：把外部插件来源、固定提交和审批链一起审。 | `agent-health` 的跨信任边界检查，不引入第二套技能总目录。 | [wshobson/agents](../../../categories/agent-skills/subagent-collections/wshobson-agents.md) |

暂缓项目也有值得研究的思想，但没有发布选型页：dzhng 的选择审计账本、Obsidian Mind 的作用域与注入预算，以及 CCBaga 的归档验收和回滚标记，先留在[待裁决记录](../proposals.md)，不直接复用实现。
其余项目评为 low／none：不是差，而是与个人 coding-agent harness 的目标距离较远，或现有机制已经覆盖。

## 横向对比选题池

以下分类连同子分类，当前均已有至少四个项目。问题是后续写作选题，不是本批追加开发任务。

- **桌面自动化：** 复用已装闭源引擎、调用独立桌面驱动，还是先买一层可丢弃虚拟机隔离？
- **数据库引擎：** 内置关键词／向量搜索省掉第二份数据，是否值得承担兼容、许可和恢复语义的迁移成本？
- **agent 监管界面：** 你缺的是待人处理队列、远程会话入口，还是自动回送 PR／CI 反馈的控制平面？
- **工程技能：** 如何把通用开发流程、领域知识和实际执行工具分开，避免“装得多”反而增加指令冲突？
- **结构化检索：** 长文档章节树、跨文档事件关联和持久知识图谱，分别在哪类问题上值得额外建索引？
- **终端编码助手：** 自带运行时、模型厂商第一方助手和现有 CLI 的监督层，究竟在哪一层替换最省迁移成本？
- **UI 品味技能：** 没有品牌规范时怎样形成设计方向，有了设计系统以后又该删掉哪些“品味推断”？
- **游戏开发：** 选轻量引擎做完整小项目，还是连接 Unity 编辑器让 agent 直接改场景，验收责任如何划分？
- **社媒管理：** 官方 API、浏览器桥和会话 cookie 客户端，在权限范围、账号风险和可恢复发布上如何取舍？
- **文档解析：** 选混合格式／CPU 管线，还是拆开版面检测与识别的 GPU 服务，商用许可和长任务恢复要付出什么？

## 验证与剩余缺口

- 本次复跑：每个新增项目合入后分别运行 `make gates` 和双页 scoped quality，均为退出码零；范围扫描均无 deterministic findings。
- 基线工具测试：`Ran 483 tests in 11.976s`，`OK`，无 skipped。最终整合后仍需重跑。
- 人工内容复核：逐页读适用场景、何时不用、比较、源码技术和存疑账本，特别检查未合并 PR 不被写成已发布能力。
- 复用 worker 证据：固定源码、许可原文、图卡渲染和目检。它们不是主会话的运行实测。
- 未运行：上游安装、模型调用、桌面控制、登录态 X 操作、安卓真机、Unity 场景、数据库崩溃恢复或占卜数据生成。不能把静态收录当成产品认证。
- 已知视觉缺口：md2wechat 的健康卡因通用模板把长许可封顶理由与覆盖率放在同一行，双语卡有文字溢出。分数、六轴和正文许可说明仍在；未手改自动评分或生成图，未扩到工具代码修复。该两图的视觉验收为 partial，不冒充全部配图无缺陷。

Inner-loop evidence：结构门禁、范围质量扫描与工具测试。
Acceptance evidence：真实 Chrome 标签逐项提交后关闭；页面、生成图、双语入口与反向索引接通；最终对账待补。
Holdout / unseen evidence：不适用模型效果实验，以源码限制、未合并修复和真实标签作为边界抽样。
Holdout 来源类别：真实捕获及源码抽样。
预期值来源：用户需求与 `tools/schema.md` 外部契约。
本次改动相对冻结点的位置：只改内容生成侧，未改工具、判定器、门禁阈值或个人 harness。

Boundary decisions：两处分类各拆成 3／10 项，保留原父入口。内部路由已修复，52 个旧叶页路径不提供外部书签重定向；工具、门禁阈值和个人 harness 未改。

下一步：维护者裁决五项资格问题；健康卡模板排版单列后续修复，不自动扩大本批开发范围。
