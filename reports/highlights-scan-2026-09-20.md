# 亮点扫描报告 — 2026-09-20

> **触发**：用户反馈「这样的项目好多啊，感觉都没啥亮点」。
> **基线**：`feat/highlights-scan` 分支，于 `03f1c28`（main）之上；本报告未 commit。
> **范围**：agent 相关的 9 个拥挤簇，共 **159 个英文词条页**（`agent-frameworks` 全部 39、`agent-skills` 全部 76、`agent-dev-methodology` 13、`agent-tooling` 10、`agent-memory` 10、`ai-code-review` 6、`team-chat` 5）。
> **方法**：只读词条页判定，不读上游仓库、不运行软件。判据与可靠性见 §2。

---

## 0. 结论先行

| 结论 | 数字 | 证据强度 |
|---|---|---|
| 全库有 **96 / 547** 个英文条目是机器生成的**占位页**（first-pass intake） | 17.5% | 机器可复现（§1） |
| 其中 **87 个**的 `Comparison` 表是**逐行相同的模板句** | 87 | 机器可复现（§1） |
| 结构性门禁 `quality_scan.py --fail-on-gated` **对这类占位页不报警**（绿） | exit 0 | 已实跑（§1.3） |
| 本次扫的 159 条里，有真实亮点的 **42 条（26%）** | 42 | 本报告判断（§4） |
| 功能叠加 **53 条**、策展打包 **44 条**、派生 **3 条**、占位页判不了 **17 条** | 117 | 本报告判断（附录 §7） |

**对「都没啥亮点」的裁决**：感觉**部分成立**，但归因要改。

- **成立**：`agent-skills`（76 条中 44 条是「某人的 skill 合集」式策展）+ `agent-dev-methodology`（13 条中 8 条是方法论文档）这两簇**确实没有机制差异**，同质是结论，不是错觉。
- **被放大**：`agent-frameworks` 最主流的 5 个框架页（CrewAI / AutoGen / LangGraph / Pydantic AI / OpenAI Agents SDK）**不是「没亮点」，而是根本没有内容**——它们是 96 个占位页之一。读到的是模板，不是这些项目。
- 所以「好多」= 真实拥挤 + **1/6 的语料是占位符**。「没亮点」里有一部分是**语料缺陷**，不是赛道结论；而这两件事在阅读体验上无法区分，因为占位页长得和真页面一模一样。

---

## 1. 最大发现：96 个占位页，且门禁漏过

### 1.1 规模（机器可复现）

```bash
rg -l "first-pass intake page|first-pass page generated" categories --glob '*.md' | rg -v '\.zh' | wc -l   # → 96
rg --files categories -g '*.md' | rg -v '\.zh\.md$' | rg -v 'INDEX' | wc -l                                   # → 547
```

96 个签名分三类：87 个「generated from GitHub metadata」、9 个「for a user-requested backlog item」、8 个「generated from the 2026-07-16 backlog」。

### 1.2 87 个共享逐行相同的模板句（机器可复现）

```bash
rg -l "Choose custom code only when the needed scope is tiny" categories --glob '*.md' | rg -v '\.zh' | wc -l          # → 87
rg -l "When you need the established in-index option for this category" categories --glob '*.md' | rg -v '\.zh' | wc -l  # → 87
rg -l "Use a more mature in-index page from the comparison table" categories --glob '*.md' | rg -v '\.zh' | wc -l        # → 87
```

样本：`categories/agent-frameworks/agent-runtimes/agent-sdks/crewai.md:98-101` 的四行 `Comparison` verdict 文本**完全相同**，只有链接目标不同；`crewai.md:83` 的 `When to use` 是「你正在为 `agent-runtimes` 类任务选型，需要一个真仓库」这类空转句。该页共 132 行，没有任何 CrewAI 特有的机制描述。

### 1.3 门禁缺口（已实跑）

`tools/quality_scan.py:19`：

```python
GENERIC_TEMPLATES = ["Use this page for its stated niche", "当前页用于它的主场景"]
```

`generic-comparison-template` 属于 `GATED_DETERMINISTIC_CATEGORIES`（`tools/quality_scan.py:31-37`）——按设计应让 CI 失败。但它只匹配这 2 条**历史遗留**短语；当前这批占位页用的是另一套模板（§1.2 三句），**不在模式表里**。

实跑：`python3 tools/quality_scan.py` → `No deterministic findings.`，exit 0。

**即：一个已存在、且被设计成 hard gate 的检查类别，覆盖不到当前 87/547 的同类缺陷。** 这不是「没写门禁」，是**门禁模式表没跟上生成模板**。[推断：修法是把 §1.2 三句并入 `GENERIC_TEMPLATES`；但那会让 87 页立即 CI 红，属仓库级决策，本报告不擅自实施]

### 1.4 受影响最重的簇

| 簇 | 占位页数 | 簇规模 |
|---|---:|---:|
| `llm-eval` | 6 | 8 |
| `investment-finance` | 6 | 6 |
| `agent-memory` | 5 | 10 |
| `agent-frameworks/agent-runtimes/agent-sdks` | 5 | 7 |
| `workflow-orchestration` | 4 | 8 |
| `pdf-tools` | 4 | 8 |
| `observability` | 4 | — |
| `llm-training` | 4 | 12 |
| `deep-research` | 4 | 10 |

---

## 2. 判据与可靠性

### 2.1 什么是「亮点」

一个条目算有亮点，当且仅当满足下列之一（6 选 1）：

| 代号 | 含义 |
|---|---|
| **N1 新机制** | 引入新原语 / 新协议 / 新身份或信任边界 / 新执行或记忆机制（不是「多支持一个集成」） |
| **N2 极端** | 某维度做到明显极端（单二进制、零依赖、完全离线、不用 key、成本或延迟量级差异），且该极端改变可行性 |
| **N3 新产物** | 定义此前不存在的产物类型（格式、图结构、可复现包） |
| **F 功能叠加** | 原语与同簇兄弟相同，差异只在模型 / UI / 集成 / 打磨 / 覆盖广度 |
| **P 打包分发** | 他人 skill/prompt 的再分发、合集、策展、个人风格库 |
| **D 派生** | fork、重写、克隆已存在项目 |
| **?** | 页面无实质内容，判不了（= §1 的占位页） |

附加字段「改变选型」= 两个不同团队会不会因此做出不同选择。`?` 一律记 no。

### 2.2 可靠性（证据抽样）

从 9 个批次抽 **44 条证据引用**逐字复核：

- **34 条逐字命中**；
- **9 条只差行内格式**（页面原文带 `` ` `` 或 `**`，引用时被抹掉），语义准确；
- **1 条伪造**：`agent-memory/memori` 的引用「SQL-native open-source memory engine for agents」在页面里**不存在**。已按页面原文修正（§4.1）。

**方法限制**（必须记住）：判定只基于**词条页**，没读上游仓库、没跑软件。因此——

- 页面写得差 → 误判为 F（把好项目判平庸）；
- 页面写得夸大 → 误判为 N（把包装判成机制）。

两类误差方向相反，**无法在本报告内消除**。[推断] 鉴于 §1 存在 96 个占位页，本报告的主要误差类型是**前者**（系统性低估），而非后者。

---

## 3. 每簇结论

| 簇 | 结论 | 值得看的 |
|---|---|---|
| `agent-frameworks/workflow-builders` (9) | 5 个（langchain / langflow / dify / flowise / llamaindex）是同一件事的不同包装；机制差异只存在于 4 个 | dspy、skillopt、autogpt、kagent |
| `agent-frameworks/agent-runtimes` (14) | **7 个是占位页**，含 5 个最主流框架 | smolagents、parlant、eve、openhuman、openfang |
| `agent-frameworks/coding-agents` (16) | 终端/IDE 代理基本同质（配置切换、模式叠加）；差异集中在编排层 | gemini-cli、rtk、swarm-forge、background-agents、claude-octopus |
| `agent-skills/design` + `engineering` (18) | 10/18 是个人策展；差异在于是否带**确定性脚本** | ai-website-cloner-template、ui-ux-pro-max、archify、addyosmani-web-quality、browser-act-skills |
| `agent-skills` 其余 (58) | **44 条策展/合集**，全库最同质的区块 | tacit-mining、webnovel-writer、guizang-ppt、book-to-skill、distilly、guizang-social-card、reverse-skill |
| `agent-skills/personal-collections` (15) | 12/15 纯策展；3 个带可执行检查 | claude-code-harness、shaping-skills、pua、patent-disclosure-skill、dbskill |
| `agent-dev-methodology` (13) | **全部是方法论文档或合集，无一 N2**；唯一契约级产物是 pure-agentic | pure-agentic |
| `agent-tooling` (10) | 4 个真工具，6 个工作流包装 | cli-anything、entire-cli、context-mode、beads |
| `agent-memory` (10) | **5 个占位页**；存活的差异是「记忆原语之争」 | byterover、memori |
| `ai-code-review` (6) | 5/6 是「LLM 再评论一次」；只有 1 个确定性检查器 | react-doctor |
| `team-chat` (5) | 唯一一个**每个存活条目都有不可互换原语**的簇 | zulip、mattermost、buzz |

**一句话**：同质最严重的是 `agent-skills`（策展）与 `agent-dev-methodology`（文档）；真正拥挤、也确实值得区分的是 `agent-sdk` / `workflow-builders` / `coding-agents`——而这恰是占位页最集中的区域。

---

## 4. 亮点清单（42 条）

### 4.1 N1 新机制（31 条）

| slug | 簇 | 实际新增了什么 | 证据（file:line + 原文） |
|---|---|---|---|
| skillopt | workflow-builders | 用验证分数门控技能文档的每次编辑 | `workflow-builders/skillopt.md:82` "each edit is kept only if it raises a held-out validation score" |
| dspy | workflow-builders | 用类型签名声明程序、按指标编译提示 | `workflow-builders/dspy.md:82` "define a `Signature` like `question -> answer`, wrap it in a `Module`" |
| autogpt | workflow-builders | 无人值守持续执行 | `workflow-builders/autogpt.md:74` "run continuously without human intervention" |
| kagent | kubernetes-agents | 代理本身成为 Kubernetes 对象 | `kubernetes-agents/kagent.md:79` "kagent makes the agent itself a Kubernetes object" |
| smolagents | agent-sdks | 代码即动作（而非 JSON tool schema） | `agent-runtimes/agent-sdks/smolagents.md:82` "its distinctive bet is that the agent *writes Python* as its action (`CodeAgent`) rather than filling JSON tool schemas" |
| parlant | agent-services | 行为规则成为逐轮执行原语 | `agent-runtimes/agent-services/parlant.md:84` "you express behavior as **guidelines** — condition/action rules" |
| eve | agent-services | 会话即带检查点的持久工作流 | `agent-runtimes/agent-services/eve.md:91` "Each session becomes one durable workflow that checkpoints at step boundaries" |
| openhuman | personal-assistants | `local_only` 在 Rust 核心是构造期拒绝 | `agent-runtimes/personal-assistants/openhuman.md:81` "`local_only` is a construction-time refusal in the Rust core" |
| swarm-forge | coding-agents | commit 既作隔离边界又作角色交接 | `coding-agents/orchestration-and-review/swarm-forge.md:87` "commit-as-handoff inside a configurable role pipeline" |
| background-agents | coding-agents | 请求方离线后沙箱继续执行 | `coding-agents/orchestration-and-review/background-agents.md:79` "isolated cloud sandboxes after the requester leaves the page" |
| claude-octopus | coding-agents | 跨模型分歧升级为合并门禁 | `coding-agents/orchestration-and-review/claude-octopus.md:71` "uses their disagreement as a blindspot/consensus gate" |
| ai-website-cloner-template | design | 网站逆向重建的执行流水线 | `agent-skills/design/ai-website-cloner-template.md:73` "asset extraction, component specs, parallel builders, assembly, and visual QA" |
| ui-ux-pro-max | design | 本地 CSV 检索驱动设计决策（非纯提示词） | `agent-skills/design/ui-ux-pro-max.md:76` "a bundled Python `search.py` over CSV databases" |
| addyosmani-web-quality | engineering | 确定性静态 HTML 检查脚本 | `agent-skills/engineering/addyosmani-web-quality.md:76` "a read-only `analyze.sh` helper that greps HTML" |
| browser-act-skills | engineering | 索引化元素操作 + 远程人工接管 | `agent-skills/engineering/browser-act-skills.md:73` "`state` returns indexed elements, actions target those indexes" |
| tacit-mining | context-engineering | 访谈提炼隐性规则并分片持久化 | `agent-skills/context-engineering/tacit-mining.md:75` "stores confirmed or fuzzy rules under `memory/tacit/`" |
| webnovel-writer | writing/fiction | 章节提交驱动的可查询连续性状态 | `agent-skills/writing/fiction/webnovel-writer.md:79` "auditable project-side story system and queryable continuity state" |
| guizang-ppt | slides-ppt | 确定性校验器拒绝违规页面结构 | `agent-skills/slides-ppt/guizang-ppt.md:76` "validator script that rejects centered titles, improvised page structures" |
| guizang-social-card | visual-content | Playwright 实测 DOM 溢出 | `agent-skills/visual-content/guizang-social-card.md:72` "an optional Playwright validator (`validate-social-deck.mjs`) measures the real DOM for overflow" |
| reverse-skill | security | 授权硬门禁 + 证据链 | `agent-skills/security/reverse-skill.md:76` "`case-guard` hard-blocks any action on a target until authorization and network profile are recorded (exit 2)" |
| claude-code-harness | personal-collections | Go 原生插件漂移诊断器 | `.../engineering-workflows/claude-code-harness.md:76` "inventories duplicate skills, plugin caches, and stale symlinks" |
| shaping-skills | personal-collections | 可执行的涟漪/副作用检查钩子 | `.../engineering-workflows/shaping-skills.md:76` "A `hooks/shaping-ripple.sh` script does a ripple/side-effect check." |
| pua | personal-collections | 生命周期钩子注入持久上下文 | `.../engineering-workflows/pua.md:76` "wires `SessionStart` / `PostToolUse` / `UserPromptSubmit` hooks to inject context" |
| patent-disclosure-skill | personal-collections | 权利要求结构与支持性门禁 | `.../knowledge-content/patent-disclosure-skill.md:110` "`audit_claims.py`, `check_support.py` check claim structure and support" |
| dbskill | personal-collections | 诊断会话可保存恢复 | `.../knowledge-content/dbskill.md:71` "so a diagnosis session can persist and resume" |
| cli-anything | agent-tooling | 从应用后端生成 agent-callable CLI | `agent-tooling/cli-anything.md:78` "makes existing software agent-callable by emitting CLI harnesses" |
| context-mode | agent-tooling | 工具输出在上下文窗口外处理 | `agent-tooling/context-mode.md:78` "keeps raw tool output out of an agent's context window" |
| memori | agent-memory | 客户端拦截 + 实体/进程维度的结构化状态（**引用已修正**，原引用为伪造） | `agent-memory/memori.md:80` "you register your existing client (`Memori().llm.register(client)`), tag a call with an `entity_id` and `process_id`"；`memori.md:96` "Memori leans on automatic client interception + structured entity/process state and an opinionated cloud" |
| react-doctor | ai-code-review | 确定性 React 静态检查器 | `ai-code-review/react-doctor.md:74` "A deterministic static analyzer for React" |
| zulip | team-chat | topic 成为一等会话原语 | `team-chat/zulip.md:79` "every conversation to live under an explicit topic" |
| buzz | team-chat | agent 是持有密钥的签名主体 | `team-chat/buzz.md:70` "its own keypair, its own channel membership, its own signed trail" |

### 4.2 N2 极端（5 条）

| slug | 簇 | 极端维度 | 证据 |
|---|---|---|---|
| openfang | agent-services | ~32 MB 单 Rust 二进制、低空闲内存 | `agent-runtimes/agent-services/openfang.md:79` "one ~32 MB Rust binary with low idle memory" |
| gemini-cli | terminal-agents | 个人 Google 账号免 key 高额度 | `coding-agents/terminal-agents/gemini-cli.md:80` "free tier (60 req/min, 1,000 req/day with a personal Google account)" |
| rtk | coding-agents | 零运行时依赖、亚 10ms 开销 | `coding-agents/orchestration-and-review/rtk.md:77` "single static binary with zero runtime dependencies and sub-10ms overhead" |
| book-to-skill | agent-skills | 完全离线产出可安装技能 | `agent-skills/book-to-skill.md:83` "keeps everything local and offline" |
| mattermost | team-chat | 单 Go 二进制聊天核心 | `team-chat/mattermost.md:84` "server is a single Go binary over PostgreSQL" |

### 4.3 N3 新产物（6 条）

| slug | 簇 | 新产物 | 证据 |
|---|---|---|---|
| archify | design | 带类型化 JSON IR 的图稿 | `agent-skills/design/archify.md:73` "typed JSON IR, and renderer-backed validation" |
| distilly | agent-skills | 工作层 + 人格层的 Person Profile | `agent-skills/distilly.md:68` "**Person Profile** packaged as an installable agent skill (a *Work* layer plus a *Persona* layer)" |
| pure-agentic | spec-driven | intent / knowledge block / A2A handoff 的 JSON Schema 契约 | `spec-driven-development/pure-agentic.md:107` "JSON Schema for intents, knowledge blocks, and A2A handoffs" |
| entire-cli | agent-tooling | 与会话关联的独立 git checkpoint 分支 | `agent-tooling/entire-cli.md:71` "indexes them as checkpoints alongside your commits on a separate" |
| beads | agent-tooling | 可版本化、可分支合并的任务依赖图 | `agent-tooling/beads.md:76` "dependency-aware, version-controlled task/issue graph" |
| byterover | agent-memory | 可分支/提交/合并的上下文树 | `agent-memory/byterover.md:77` "structured context trees with git-like versioning" |

---

## 5. 同质区块（不必逐个读）

- **策展/合集 44 条（P）**：`vendor-collections` 全部 6 个、`subagent-collections` 全部 3 个、`prompt-engineering` 3 个、`personal-collections` 12 个、`engineering`/`design` 的个人包 10 个、`writing/content-production` 2 个，其余 8 个。统一依据：页面自述是某人的 skill 集合或官方合集。
- **功能叠加 53 条（F）**：差异只在模型、UI、集成面、打磨度。典型：`langchain`/`langflow`/`dify`/`flowise`（同一张图的不同画布）、`codex`/`opencode`/`t3code`/`kilocode`（同一循环的不同外壳）、`ai-code-review` 里 5 个 LLM 评论器、`de-ai-writing` 全部 5 个去 AI 味提示包。
- **派生 3 条（D）**：`open-interpreter`（Codex CLI 分支）、`translate-book`（对既有流程的重构）、`humanizer-zh`（humanizer 中文本地化）。
- **占位页 17 条（?）**：crewai、autogen、pydantic-ai、langgraph、openai-agents-sdk、langmem、zep、letta、pr-agent、aider、cline、swe-agent、openhands、llamaindex、flowise、hermes-agent（部分）、de-ai-prompt-enhancer（部分）。

完整 159 行判定表见 §7。

---

## 6. 建议（按代价排序）

1. **补门禁模式表**（最便宜、收益最大）：把 §1.2 三句并入 `tools/quality_scan.py:19` 的 `GENERIC_TEMPLATES`。副作用是 87 页立刻 CI 红——这正好把「哪些页需要重写」变成一张确定清单。**需要你裁决是否接受一次 red 状态。**
2. **清点并重建 96 个占位页**：优先 `agent-sdks`（5/7 全是占位）、`agent-memory`（5/10）、`llm-eval`（6/8）。这是把「没亮点」从语料缺陷里剥出来的唯一办法。
3. **给 schema 加 `Novelty` 字段**（§2.1 那套 N1/N2/N3 判据）：强制每页用一句话回答「新增了什么原语」，写不出来的就是同质项。代价 547 页回填，收益是选型时不必通读全文。
4. **本轮不做**：`agent-skills` 策展簇的去重/合并——同质在那里的**结论而非缺陷**（策展本来就卖 curation），除非要按 refactor-index 拆子类。

---

## 7. 附录：159 条完整判定

| slug | 簇 | verdict | 新增了什么 | 最近邻 | 改变选型 |
|---|---|---|---|---|---|
| dify | workflow-builders | F | 视觉编排 + RBAC + 企业部署 | langflow | yes |
| llamaindex | workflow-builders | ? | 页面无实质内容 | langchain | no |
| langflow | workflow-builders | F | 可定制画布 | flowise | yes |
| langchain | workflow-builders | F | 组件与适配器覆盖广度 | llamaindex | yes |
| skillopt | workflow-builders | **N1** | 验证门控的技能文档迭代 | dspy | yes |
| dspy | workflow-builders | **N1** | 签名声明 + 提示编译 | skillopt | yes |
| flowise | workflow-builders | ? | 页面无实质内容 | langflow | no |
| autogpt | workflow-builders | **N1** | 无人值守持续执行 | dify | yes |
| kagent | kubernetes-agents | **N1** | 代理即 K8s 对象（CRD） | 未收录 | yes |
| crewai | agent-sdks | ? | 占位页 | agentscope | no |
| autogen | agent-sdks | ? | 占位页 | crewai | no |
| pydantic-ai | agent-sdks | ? | 占位页 | openai-agents-sdk | no |
| langgraph | agent-sdks | ? | 占位页 | agentscope | no |
| smolagents | agent-sdks | **N1** | 代码即动作 | pydantic-ai | yes |
| agentscope | agent-sdks | F | 服务 + 权限 + 沙箱 + 追踪打包 | eve | no |
| openai-agents-sdk | agent-sdks | ? | 占位页 | autogen | no |
| symphony | agent-services | F | Linear 工单 × Codex 运行 | claude-octopus | no |
| openfang | agent-services | **N2** | ~32MB 单二进制自治运行时 | openclaw | yes |
| parlant | agent-services | **N1** | guideline 规则成为逐轮原语 | 未收录 | yes |
| eve | agent-services | **N1** | 会话即可检查点工作流 | agentscope | yes |
| hermes-agent | personal-assistants | ? | 自动生成技能（[未验证]） | openclaw | no |
| openclaw | personal-assistants | F | 多渠道覆盖广度 | hermes-agent | no |
| openhuman | personal-assistants | **N1** | 构造期强制本地信任边界 | openclaw | yes |
| t3code | terminal-agents | F | 统一多代理的图形会话界面 | cc-switch | no |
| opencode | terminal-agents | F | 同终端切多模型 | open-interpreter | no |
| open-interpreter | terminal-agents | D | Codex CLI 分支 + 可换 harness | codex | no |
| gemini-cli | terminal-agents | **N2** | 免 key 高额度免费层 | codex | yes |
| aider | terminal-agents | ? | 占位页 | opencode | no |
| codex | terminal-agents | F | OpenAI 官方 + 打磨 | gemini-cli | no |
| kilocode | ide-agents | F | 模式编排 + 模型市场 | cline | no |
| cline | ide-agents | ? | 占位页 | kilocode | no |
| swarm-forge | coding-agents | **N1** | commit-as-handoff | oh-my-claudecode | yes |
| rtk | coding-agents | **N2** | 零依赖 + 亚 10ms 压缩 | 未收录 | yes |
| background-agents | coding-agents | **N1** | 请求方离线后继续执行 | openhands | yes |
| oh-my-claudecode | coding-agents | F | Claude 内分阶段流水线 | swarm-forge | no |
| cc-switch | coding-agents | F | 代理配置统一界面 | t3code | no |
| swe-agent | coding-agents | ? | 占位页 | openhands | no |
| openhands | coding-agents | ? | 占位页 | background-agents | no |
| claude-octopus | coding-agents | **N1** | 跨模型分歧作门禁 | oh-my-claudecode | yes |
| emilkowalski-skills | design | P | 个人动效经验合集 | make-interfaces-feel-better | no |
| taste-skill | design | P | 可调视觉风格提示合集 | hallmark | no |
| ai-website-cloner-template | design | **N1** | 网站逆向重建流水线 | stitch-skills | yes |
| stitch-skills | design | F | 包装 Stitch 能力 | ai-website-cloner-template | no |
| make-interfaces-feel-better | design | P | 文章式微调规则库 | emilkowalski-skills | no |
| huashu-design | design | F | 多视觉产物导出 | archify | no |
| designer-skills | design | P | 全周期设计技能合集 | ui-ux-pro-max | no |
| ui-ux-pro-max | design | **N1** | 本地 CSV 检索生成设计系统 | designer-skills | yes |
| archify | design | **N3** | 类型化 JSON IR 图稿 | huashu-design | yes |
| hallmark | design | P | 单一反俗套风格协议 | taste-skill | no |
| scientific-agent-skills | engineering | P | 科学库技能策展 | 未收录 | no |
| vercel-agent-skills | engineering | P | Vercel 官方规则合集 | addyosmani-web-quality | no |
| caveman | engineering | F | 极简话风叠加 | 未收录 | no |
| addyosmani-web-quality | engineering | **N1** | 确定性 HTML 检查脚本 | vercel-agent-skills | yes |
| browser-act-skills | engineering | **N1** | 索引元素 + 人工接管 | 未收录 | yes |
| waza | engineering | P | 八项工程习惯合集 | mattpocock-skills | no |
| mattpocock-skills | engineering | P | 个人工程流程合集 | waza | no |
| addyosmani-agent-skills | engineering | P | 生产工程技能合集 | mattpocock-skills | no |
| tacit-mining | context-engineering | **N1** | 隐性规则提炼 + 分片记忆 | soul-md | yes |
| soul-md | context-engineering | F | 身份/风格/记忆分层人设包 | nuwa-skill | yes |
| nuwa-skill | context-engineering | F | 人物研究与视角蒸馏 | distilly | yes |
| context-engineering-skills | context-engineering | P | 策展 15 项技能 | 未收录 | no |
| cangjie-skill | context-engineering | F | 长材料转技能包流程 | book-to-skill | yes |
| notebooklm-skill | context-engineering | F | 接入 NotebookLM 检索 | context-engineering-skills | yes |
| open-seo | writing/marketing-seo | F | SEO + MCP 接口 | marketingskills | yes |
| marketingskills | writing/marketing-seo | P | 营销全流程合集 | open-seo | no |
| chinese-novelist-skill | writing/fiction | F | 无运行时的中文小说流程 | webnovel-writer | yes |
| webnovel-writer | writing/fiction | **N1** | 可审计连续性状态 | chinese-novelist-skill | yes |
| claude-translater | writing/translation | F | 简单脚本 + PPTX 翻译 | translate-book | yes |
| translate-book | writing/translation | D | 重构旧流程 + 并行续跑 | claude-translater | yes |
| huashu-skills | writing/content-production | P | 中文创作工具箱 | baoyu-skills | no |
| baoyu-skills | writing/content-production | P | 翻译/排版/发布合集 | huashu-skills | no |
| writing-agent | writing/content-production | F | 证据门控的长文产线 | huashu-skills | yes |
| frontend-slides | slides-ppt | F | 单文件 HTML 输出 | html-ppt-skill | yes |
| html-ppt-skill | slides-ppt | F | 模板与主题覆盖 | frontend-slides | yes |
| ppt-master | slides-ppt | F | 原生可编辑 PPTX | frontend-slides | yes |
| guizang-ppt | slides-ppt | **N1** | 校验器拒绝违规结构 | frontend-slides | yes |
| book-to-skill | agent-skills | **N2** | 完全离线生成技能 | cangjie-skill | yes |
| distilly | agent-skills | **N3** | Person Profile 产物 | nuwa-skill | yes |
| humanizer | de-ai-writing | F | 宽版去 AI 流程 | stop-slop | no |
| stop-slop | de-ai-writing | F | 短版强硬规则 | humanizer | no |
| ai-flavor-remover | de-ai-writing | F | 单段提示 | humanizer-zh | no |
| shuorenhua | de-ai-writing | F | 中文场景规则 + 保护区 | humanizer-zh | no |
| humanizer-zh | de-ai-writing | D | humanizer 中文本地化 | humanizer | no |
| de-ai-prompt-enhancer-writer-booster-skill | de-ai-writing | ? | 附审计脚本，机制未写清 | shuorenhua | no |
| guizang-social-card | visual-content | **N1** | DOM 实测卡片校验器 | html-anything | yes |
| ian-illustrations | visual-content | F | 固定画风与分镜 | 未收录 | — |
| reverse-skill | security | **N1** | 授权门禁 + 证据链 | anthropic-cybersecurity-skills | yes |
| anthropic-cybersecurity-skills | security | P | 框架映射运行手册 | reverse-skill | no |
| minimax-skills | vendor-collections | P | 厂商官方合集 | anthropic-skills | no |
| knowledge-work-plugins | vendor-collections | P | Anthropic 官方合集 | anthropic-skills | no |
| claude-plugins-official | vendor-collections | P | 官方插件目录 | anthropic-skills | no |
| remotion-skills | vendor-collections | P | 版本同步技能 | anthropic-skills | no |
| aws-agent-plugins | vendor-collections | P | AWS 官方合集 | claude-plugins-official | no |
| anthropic-skills | vendor-collections | P | Anthropic 官方合集 | claude-plugins-official | no |
| prompt-engineering-guide | prompt-engineering | P | 提示工程知识库 | prompts-chat | no |
| prompts-chat | prompt-engineering | P | 社区投票语料库 | prompt-master | no |
| prompt-master | prompt-engineering | F | 按工具方言生成提示 | prompts-chat | no |
| wshobson-agents | subagent-collections | P | 多 harness 子代理合集 | agency-agents | no |
| agency-agents | subagent-collections | P | ~232 角色代理合集 | wshobson-agents | no |
| awesome-claude-code-subagents | subagent-collections | P | 100+ 子代理合集 | wshobson-agents | no |
| antfu-skills | personal-collections | P | Vue 作者偏好合集 | dimillian-skills | no |
| taches-cc-resources | personal-collections | P | Claude 扩展生成器合集 | gstack | no |
| claude-code-harness | personal-collections | **N1** | Go 插件漂移诊断器 | gstack | yes |
| karpathy-skills | personal-collections | P | 编码原则包装 | qiushi-skill | no |
| qiushi-skill | personal-collections | P | 方法论提示合集 | karpathy-skills | no |
| gstack | personal-collections | P | 创始人角色化命令集 | claude-code-harness | no |
| dimillian-skills | personal-collections | P | Apple 开发合集 | antfu-skills | no |
| shaping-skills | personal-collections | **N1** | 可执行涟漪检查钩子 | superpowers | yes |
| pua | personal-collections | **N1** | 生命周期钩子注入 | qiushi-skill | yes |
| canghe-skills | personal-collections | P | 内容发布工具合集 | khazix-skills | no |
| ljg-skills | personal-collections | P | 中文知识工作合集 | khazix-skills | no |
| patent-disclosure-skill | personal-collections | **N1** | 权利要求门禁脚本 | 未收录 | yes |
| khazix-skills | personal-collections | P | 中文工具杂合集 | canghe-skills | no |
| slavingia-skills | personal-collections | P | 创业书方法包装 | dbskill | no |
| dbskill | personal-collections | **N1** | 诊断会话可持久化 | slavingia-skills | yes |
| quad | study-and-experiments | P | 四角色方法论文档 | usdad | no |
| learn-claude-code | study-and-experiments | P | 17 课重建课程 | 12-factor-agents | no |
| ltbl-experiment | study-and-experiments | P | 未完成的实验索引 | 未收录 | no |
| ecc | coding-agent-harnesses | F | 大而全技能套件 | superclaude | no |
| compound-engineering | coding-agent-harnesses | P | 六阶段复盘插件 | superpowers | no |
| superclaude | coding-agent-harnesses | P | 命令/角色/模式合集 | superpowers | no |
| superpowers | coding-agent-harnesses | P | 开发流程技能包 | compound-engineering | no |
| 12-factor-agents | spec-driven | P | 设计原则清单 | usdad | no |
| get-shit-done | spec-driven | F | 原子计划独立上下文 | spec-kit | no |
| usdad | spec-driven | P | 四角色文档方法论 | pure-agentic | no |
| spec-kit | spec-driven | F | CLI 化规格流程 | get-shit-done | no |
| spec-anchored-agentic-development | spec-driven | F | 能力规格作长期契约 | spec-kit | no |
| pure-agentic | spec-driven | **N3** | JSON Schema 契约 | usdad | yes |
| vercel-skills | agent-tooling | F | 跨代理技能安装 CLI | 未收录 | no |
| cli-anything | agent-tooling | **N1** | 生成 agent-callable CLI | 未收录 | yes |
| agentsview | agent-tooling | F | 多代理会话与成本汇总 | entire-cli | no |
| entire-cli | agent-tooling | **N3** | 会话 checkpoint 分支 | agentsview | yes |
| agent-orchestrator | agent-tooling | F | worktree 并行控制台 | ccpm | no |
| context-mode | agent-tooling | **N1** | 工具输出离上下文处理 | planning-with-files | yes |
| ccpm | agent-tooling | F | PRD → Issues 工作流 | agent-orchestrator | no |
| ralph-claude-code | agent-tooling | F | Ralph 循环 + 护栏 | agent-orchestrator | no |
| planning-with-files | agent-tooling | F | Markdown 状态 + 钩子 | context-mode | no |
| beads | agent-tooling | **N3** | 版本化任务依赖图 | ccpm | yes |
| langmem | agent-memory | ? | 占位页 | mem0 | no |
| zep | agent-memory | ? | 占位页 | graphiti | no |
| cognee | agent-memory | F | 自托管知识图谱记忆 | graphiti | no |
| byterover | agent-memory | **N3** | 可分支合并的上下文树 | claude-mem | yes |
| graphiti | agent-memory | F | 实时知识图谱记忆 | cognee | no |
| mem0 | agent-memory | F | 抽取事实 + 向量召回 | langmem | no |
| claude-mem | agent-memory | F | 生命周期钩子采集回注 | claude-subconscious | no |
| letta | agent-memory | ? | 占位页 | mem0 | no |
| claude-subconscious | agent-memory | F | Letta 后台记忆钩子 | claude-mem | no |
| memori | agent-memory | **N1** | 客户端拦截 + 实体/进程结构化状态（引用已修正） | mem0 | yes |
| react-doctor | ai-code-review | **N1** | 确定性 React 检查器 | open-code-review | yes |
| pr-agent | ai-code-review | ? | 占位页 | open-code-review | no |
| openreview | ai-code-review | F | 自托管审查机器人 | pr-agent | no |
| metis | ai-code-review | F | 安全向 LLM 审查 | claude-code-security-review | no |
| open-code-review | ai-code-review | F | 确定性定位 + LLM 判断 | pr-agent | no |
| claude-code-security-review | ai-code-review | F | Claude 安全审查提示 | metis | no |
| mattermost | team-chat | **N2** | 单 Go 二进制核心 | zulip | yes |
| zulip | team-chat | **N1** | topic 一等原语 | mattermost | yes |
| rocket-chat | team-chat | F | 全渠道 + 联邦 | mattermost | no |
| buzz | team-chat | **N1** | agent 为签名主体 | mattermost | yes |
| hivechat | team-chat | F | 多模型配额前端 | 未收录 | no |

**计数**：N1 31 · N2 5 · N3 6 · F 53 · P 44 · D 3 · ? 17 ＝ 159。

---

## 8. Caveats（未验证）

- `[推断]` 全部 159 条判定基于词条页文本，**未读上游仓库、未运行软件**；页面质量直接决定判定质量（§2.2）。
- `[未验证]` 96 / 87 / 547 等计数由 §1 列出的命令在 `03f1c28` 上产出，未 commit，随语料变动而失效。
- `[未验证]` 「改变选型」是判定者判断，不是可测量量；同簇内存在相互矛盾时（如 `dify`↔`langflow` 都记 yes）说明该字段在 F 类上不稳定。
- `[推断]` §1.3 的「门禁模式表未跟进」是据 `tools/quality_scan.py:19` 与实跑输出推断的因果，未读生成这些页面的脚本以确认模板来源。
- `[未验证]` `hermes-agent`、`de-ai-prompt-enhancer-writer-booster-skill` 两页并非完整占位页，但关键机制描述不充分，暂记 `?`。
- 本次唯一被证伪的引用（`memori`，§4.1）已修正；其余 9 条失败项经复核为行内格式差异。
