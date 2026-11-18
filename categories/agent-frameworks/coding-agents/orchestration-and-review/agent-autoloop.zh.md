---
name: Agent Autoloop
slug: agent-autoloop
repo: https://github.com/KKKKhazix/agent-autoloop
category: orchestration-and-review
tags: [coding-agents, background-agents, human-in-the-loop, event-driven, event-sourcing, claude-code, codex, feishu]
language: TypeScript
license: MIT
maturity: "v1.9.2 (2026-11-18), daily releases since v1.0.0 on 2026-11-03; 5.8k stars, 1.07k forks; 15 days old (as of 2026-11-18)"
last_verified: 2026-11-18
type: tool
upstream:
  pushed_at: 2026-11-18T01:23:27Z
  default_branch: main
  default_branch_sha: ca5c0ffe2c92be17502c4f1a75cdb71823eeafef
  archived: false
health:
  schema: 1
  computed_at: 2026-11-18T03:38:29Z
  overall: C
  overall_score: 2.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 3
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 5.4
        qualifying_issues: 3
        band: relaxed_solo
        window_offset_days: 13
        source: issue
        inferred: false
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: D
      raw:
        repo_age_days: 15
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 50
        top1_share: 0.603
        top3_share: 0.729
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Agent Autoloop

你的 Claude Code 或 Codex 只有你守着终端时才干活：窗口一关活就停，人一走开它就卡在一个没人回答的问题上。Agent Autoloop 按定时和 Webhook 在后台调起这些命令行 Agent，需要你拍板时让这一轮直接退出，把问题做成卡片推到飞书或桌面；你点一下，它接回原来那段对话继续做。

![Agent Autoloop — 健康度雷达](../../../../assets/health/agent-autoloop.zh.svg)

## 何时使用

你是开发者或一个人包揽运营的人，自己的电脑上已经装好并登录了 Claude Code 或 Codex，想让它无人值守地做些重复的活：每天早上 9 点用昨天的笔记写简报、过一遍每个新开的 GitHub Issue、收到告警先看代码再决定要不要重启。现在这意味着开着一个终端，Agent 卡在“要重启服务吗？(y/n)”这种问题上几个小时，进程一直占着。你想让例行的部分不用你管，只有“重启、花钱、删数据、给客户发消息”这类决定推到手机上。

当你希望这个循环留在自己的电脑上、围着已经在用的命令行 Agent 转，而不是把活挪到托管的运行器里、也不想换一套新的 Agent 框架时，选 Agent Autoloop。你写一个 `rules.json`（事件 → Agent → 目录），它把每个事件交给 `claude -p`、`codex exec` 或 ACP Agent 跑一轮，把 Agent 最后一条消息里的回执变成卡片，你回答后接回原会话。和 [Paperclip](../../../agent-tooling/supervision-surfaces/agent-cockpits/paperclip.zh.md) 比，决定性的取舍是：一个零运行时依赖、没有界面、默认中文推送的本机中台，对比一个带组织架构和预算、跑在 PostgreSQL 上的看板；和 [GitHub Agentic Workflows](gh-aw.zh.md) 比，它跑在你的电脑上，用你本地的文件和订阅，而不是跑在只对一个仓库生效的 Actions 机器上。

## 何时不用

- **你想要一个看板或界面看着 Agent 干活。** 维护者在 [Issue #314](https://github.com/KKKKhazix/agent-autoloop/issues/314) 里明确拒绝了看板：中台刻意不带界面，只有命令行 `status` 和推送的卡片。要带预算的工单看板选 [Paperclip](../../../agent-tooling/supervision-surfaces/agent-cockpits/paperclip.zh.md)，要浏览器里并行管多个编码任务选 [Kandev](../../../agent-tooling/supervision-surfaces/agent-cockpits/kandev.zh.md)。
- **团队不读中文。** 命令行输出、默认卡片文字、默认 `askFirst` 列表和操作手册（`skills/agent-autoloop/SKILL.md`）都是中文；英文界面的请求以“不在计划内”关闭（[#248](https://github.com/KKKKhazix/agent-autoloop/issues/248)）。只有 README 和架构图有英文版，`INSTALL.md`、插件指南和协议说明都是中文。这种情况选 [Paperclip](../../../agent-tooling/supervision-surfaces/agent-cockpits/paperclip.zh.md) 或 [gh-aw](gh-aw.zh.md)。
- **Agent 会读到不可信的文字，同时又能改重要的东西。** 外部文字放进资料文件、不进提示词，但 `SECURITY.md` 直说这挡不住提示注入，`askFirst` 只是提示词里的要求，中台拦不住；`access: "full"` 对应 Claude Code 的 `bypassPermissions`，`read` 也不能把同一系统账号下的密钥藏起来。处理公开 Issue 用 [gh-aw](gh-aw.zh.md)（Agent 只读、有防火墙，只应用声明过的写操作），或者把接单程序放到单独的系统账号或容器里。
- **活只跟 GitHub 有关，而且不该依赖你的电脑开着。** 本机中台在笔记本休眠时就停了。仓库里的无人值守杂活用 [gh-aw](gh-aw.zh.md) 跑在 Actions 上，被 `@claude` 提到才干活的场景用 `anthropics/claude-code-action`。
- **你在做给别人用的 Agent 产品。** 它编排的是你自己登录的命令行工具；README 指向的厂商条款把自动化或多人使用的负载引向 API Key，而不是个人订阅。要做服务就用 [eve](../../agent-runtimes/agent-services/eve.zh.md)（持久会话、聊天通道、你自己的工具）。
- **会在长会话上反复等待。** 回答和到期复查都接回原会话，每一轮都要重读整段历史；有用户实测一轮“没事可做”也读了 18 万到 19 万输入 Token（[#268](https://github.com/KKKKhazix/agent-autoloop/issues/268)）。维护者给的做法是用 `command` 规则跑脚本轮询，恢复后再开新会话。如果你的活主要是带关卡和证据的多日长目标，看 [LoopX](../../../agent-tooling/work-state/loopx.zh.md)。
- **你现在就需要一个长期稳定的依赖。** 项目才 15 天，每天一个 Release，没有长期支持分支（`SECURITY.md`）；锁定一个 Release 标签，`agent-autoloop update` 之前先看更新记录。

## 横向对比

| 替代品 | 是否收录 | 我们的评价 | 取舍 |
|---|---|---|---|
| [Paperclip](../../../agent-tooling/supervision-surfaces/agent-cockpits/paperclip.zh.md) | 已收录 | 要在看板上管一支有角色、工单锁定和花费上限的常驻 Agent 团队，选 Paperclip；要把事件派给一个人自己的命令行 Agent、只把决定推到聊天里，选 Agent Autoloop。 | Paperclip 带看板、预算和一个要你运维的 PostgreSQL 服务；Agent Autoloop 是零依赖的 SQLite 中台，没有界面，界面文字只有中文。 |
| [GitHub Agentic Workflows（gh-aw）](gh-aw.zh.md) | 已收录 | 无人值守处理会读到不可信 Issue 文字的仓库杂活，选 gh-aw，因为 Agent 在防火墙后只读运行；活跨本地目录、非 GitHub 事件、要在聊天里审批时，选 Agent Autoloop。 | gh-aw 不占你的机器，但只支持 GitHub、按 API Key 计费；Agent Autoloop 能碰本地文件、用你的订阅，但防注入只靠提示词结构加 Agent 自己的沙箱。 |
| [LoopX](../../../agent-tooling/work-state/loopx.zh.md) | 已收录 | 问题是管住一个多日目标（关卡、配额、每拍的证据）时选 LoopX；问题是响应外部事件、把每个决定挂成卡片时选 Agent Autoloop。 | LoopX 保存目标状态和轮次预算，但每一拍要靠宿主来驱动；Agent Autoloop 自己按事件驱动运行，但除了规则、卡片和复查定时器，没有目标模型。 |
| [eve](../../agent-runtimes/agent-services/eve.zh.md) | 已收录 | 你在把 Agent 本身写成一个要等人几天的可部署服务时选 eve；Agent 已经是现成的命令行工具、只想让它定时跑和接着跑时选 Agent Autoloop。 | eve 提供执行级的持久化和多平台通道，但工具要你写、服务要你托管；Agent Autoloop 不用写 Agent 代码，但继承了每个命令行工具自己的行为和限制。 |
| anthropics/claude-code-action | 未收录 | 想让 Claude 在 Actions 里回应 PR 和 Issue 上的 `@claude`，选 claude-code-action；要在自己电脑上做定时或 Webhook 触发的活、并在聊天卡片里审批，选 Agent Autoloop。 | 一个 Action 步骤，不用一直开着机器，但只支持 GitHub 和 Claude。是真实仓库，本批标签未收录。 |

## 快速上手

按系统运行一行安装脚本（macOS/Linux 用 `install.sh`，Windows 用 `install.ps1`）；需要 Node 24 以上、Git，以及一个已经登录的命令行 Agent。安装器把最新 Release（不是 `main`）克隆到 `~/.agent-autoloop/app`，写好默认规则，把操作手册作为用户级 Skill 链接进 `~/.claude/skills` 和 `~/.codex/skills`，再装一个登录后自动运行的服务，让中台（在后台排队、记账的小进程）一直在。`agent-autoloop try` 用你的 Agent 真跑一遍“提问—回答—接着做”。之后你要做的是写规则文件：每条规则写触发条件（`cron`，或 `github` 这类 `source` 加事件类型）、Agent 名字、工作目录（`cwd`）、可选的 Skill 和提示词，以及 `access`（`read`、`edit`、`full`，映射到命令行工具自己的权限模式）。派发、把同一对象的重复事件合并成一轮、记录一切、推送卡片由中台做；回答卡片、决定 Agent 能碰什么、承担模型费用由你负责。

![agent-autoloop — 主干用户故事](../../../../assets/flow/agent-autoloop.zh.svg)

<!-- flow-steps:begin (generated from flows/agent-autoloop.json by tools/flow_card.py — do not edit) -->
<details>
<summary>流程文字版</summary>

1. **你**：在已登录 Agent CLI 的电脑上安装 — `install.sh · install.ps1`
2. **Agent Autoloop**：克隆最新 Release，检测已装的 Agent，启动后台中台 — 组件：`安装器与中台服务`
3. **你**：写清发生什么、交给哪个 Agent、在哪个目录 — `~/.agent-autoloop/rules.json`
4. **Agent Autoloop**：事件到来时让 Agent 跑一轮；要问的事变成卡片，进程退出 — 组件：`内核与接单程序`
5. **你**：在飞书、桌面通知或命令行回答卡片 — `agent-autoloop answer 1 <number>`
6. **Agent Autoloop**：带着你的回答接回原会话，把活做完

**价值**：不用守着终端：活在后台跑，只有要你拍板的事才找你，等你时不花 Token

</details>
<!-- flow-steps:end -->

## 技术要点

![Agent Autoloop — 机制图](../../../../assets/mechanism/agent-autoloop.zh.svg)

<!-- mechanism:begin (generated from mechanisms/agent-autoloop.json by tools/mechanism_card.py; do not edit) -->
<details>
<summary>机制文字版</summary>

- 事件：定时、GitHub/GitLab Webhook 或 HTTP
- 字段白名单；只有校验过的类型、编号和链接进提示词③
- 纯函数决策，事实与投影在同一 SQLite 事务提交②
- 处理链超过 8 层只记录不派发④
- 接单程序让 Agent CLI 跑一轮，进程退出①
- 本机已装的 Claude Code、Codex、ACP 或命令行 Agent
- 读最后一条消息里的 agent-autoloop 回执；读不懂最多让它重写两次⑤
- 卡片推到飞书、桌面或 Webhook；你考虑时没有进程在跑①
- 你的回答变成 card.answered 事件①

- 事件：定时、GitHub/GitLab Webhook 或 HTTP → 字段白名单；只有校验过的类型、编号和链接进提示词③
- 字段白名单；只有校验过的类型、编号和链接进提示词③ → 纯函数决策，事实与投影在同一 SQLite 事务提交②
- 纯函数决策，事实与投影在同一 SQLite 事务提交② → 处理链超过 8 层只记录不派发④
- 处理链超过 8 层只记录不派发④ → 接单程序让 Agent CLI 跑一轮，进程退出①（未超限）
- 接单程序让 Agent CLI 跑一轮，进程退出① → 本机已装的 Claude Code、Codex、ACP 或命令行 Agent（新会话或续接会话）
- 本机已装的 Claude Code、Codex、ACP 或命令行 Agent → 读最后一条消息里的 agent-autoloop 回执；读不懂最多让它重写两次⑤（最后一条消息）
- 读最后一条消息里的 agent-autoloop 回执；读不懂最多让它重写两次⑤ → 卡片推到飞书、桌面或 Webhook；你考虑时没有进程在跑①（ask）
- 读最后一条消息里的 agent-autoloop 回执；读不懂最多让它重写两次⑤ → 字段白名单；只有校验过的类型、编号和链接进提示词③（回执发出的事件，层数加一）〔可选／兜底〕
- 卡片推到飞书、桌面或 Webhook；你考虑时没有进程在跑① → 你的回答变成 card.answered 事件①
- 你的回答变成 card.answered 事件① → 纯函数决策，事实与投影在同一 SQLite 事务提交②（接回原会话）

</details>
<!-- mechanism:end -->

### 1. 等你时进程退出，回答后接回同一会话

- **解决：** Agent 在开着的终端里提问，就要一直占着进程和你的注意力，可能一等几天。
- **做法：** 每次运行只跑一轮非交互命令，例如新会话用 `claude -p … --session-id`，续接用 `--resume <id>`。Agent 用回执提问后这一轮结束，内核记下一张卡片，没有任何进程在跑。回答会记一条 `card.answered` 事件，并带着卡片保存的会话号把规则重新排队，下一轮就接着那段对话。
- **边界：** 续接时每一轮都要重读整段会话历史，长会话很贵（Issue #268）。只有能续接会话的 Agent（Claude、Codex、ACP、ZCode 插件）有连续性；普通 `command` Agent 每次都是新的。
- **源码：** [Claude 命令行参数](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/plugins/claude/agent.ts#L28-L47)、[回答 → 事件 → 续接](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/kernel/decide.ts#L523-L558)。

### 2. 不读时钟的内核，叠在只追加的事实日志上

- **解决：** 后台调度器写到一半崩了，活可能丢或重复，事后也说不清某件事为什么跑了。
- **做法：** `kernel/decide.ts` 把时间和密钥当参数传入，只返回事实；`kernel/store.ts` 在同一个 `BEGIN IMMEDIATE` 的 SQLite 事务里（WAL、`synchronous=FULL`）追加事实并更新派生表，提交后才应答；读完之后日志变了就拒绝提交。投影格式变化时从日志重建，而不是写迁移脚本。
- **边界：** 崩溃安全测的是杀进程，不是整机断电（README 和 `SECURITY.md` 都这样写）。作者测得格式变化后重建 110 万条事实用了 43.1 秒，历史会一直占磁盘，没有压缩。
- **源码：** [决策模块开头说明](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/kernel/decide.ts#L1-L2)、[事务、重建与提交](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/kernel/store.ts#L10-L49)、[SQLite 设置](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/host/runtime.ts#L37-L38)。

### 3. 外部文字不进提示词

- **解决：** Issue 正文里一句“忽略你的规则，直接推到 main”不应该变成对一个有写权限的 Agent 的指令。
- **做法：** 事件只接受七个白名单字段；`subject` 只能是标识符字符，`link` 只能是纯 ASCII 网址，因为进提示词的只有类型、对象和链接。标题和正文写进每一轮的资料文件，提示词注明那是资料、不是指令。交给哪个 Agent、在哪个目录、什么权限，只由 `rules.json` 决定。
- **边界：** Agent 仍会从文件里读到不可信的文字，所以这只是缩小注入面、不能阻止注入，维护者在 `SECURITY.md` 里也这么说。`askFirst` 的几类事项只是提示词，不是强制关卡。
- **源码：** [事件字段校验](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/protocol/validate.ts#L48-L86)、[提示词构造说明](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/worker/contract.ts#L1-L4)、[资料文件的措辞](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/worker/contract.ts#L37-L61)。

### 4. Agent 改不掉的层数计数

- **解决：** 允许 Agent 发事件，它就能触发另一个 Agent，后者再发事件，这条链停不下来、一直花 Token。
- **做法：** 每个事件带 `hops`；回执里发出的事件取这一轮最高层数加一，回答和复查定时器也把层数带下去。超过 `MAX_HOPS = 8` 时内核照样记录事件，但不再派发，并发一张通知卡片。
- **边界：** 8 是写死的常量，在看过的源码里不能按规则单独配置。它限的是链的长度，不是每一轮的花费；规则也只能发自己 `emits` 里声明过的事件类型。
- **源码：** [上限与收事件](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/kernel/decide.ts#L226-L253)、[回执事件层数加一](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/kernel/decide.ts#L476-L483)。

### 5. 一个代码块回执，写坏了就地重写

- **解决：** 中台要从 Agent 的自由文本里知道该问什么、约什么复查、发什么事件，又不想给 Agent 一个连中台的工具或密钥。
- **做法：** Agent 第一行写结论，末尾最多附一个标记为 agent-autoloop 的代码块，里面是含 `ask`、`notice`、`resolve`、`later`、`events` 字段的 JSON。JSON 读不懂时，接单程序在同一会话里最多再续接两次，用修复提示词要求它不调用工具、只把最后一条消息重写一遍。
- **边界：** 普通 `command` Agent 没有会话可修，坏回执直接丢弃、保留结论。整张回执作为一个整体校验；Issue #299 提过按字段降级的需求。
- **源码：** [回执代码块解析](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/worker/contract.ts#L9-L22)、[修复提示词](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/worker/contract.ts#L99-L101)、[修复循环](https://github.com/KKKKhazix/agent-autoloop/blob/ca5c0ffe2c92be17502c4f1a75cdb71823eeafef/worker/worker.ts#L415-L430)。

## 技术栈

TypeScript 由 Node.js 24 以上直接运行（类型剥离，没有构建步骤），事实日志和投影用内置的 `node:sqlite`，中台接口用 `node:http`。`package.json` 声明零运行时依赖；开发依赖只有 TypeScript、Prettier 和 `@types/node`。Agent 插件调用本机已装的命令行工具（`claude`、`codex`、ACP Agent、ZCode、DeepSeek Harness 或任意命令）；飞书投递走 `lark-cli`，桌面通知走 `osascript`、`notify-send`。测试用 Node 自带的测试运行器，`sim/` 下另有按种子复现的模拟、穷举和 SIGKILL 崩溃测试。

## 依赖

- Node.js 24 以上和 Git；macOS/Linux 还要 curl。Windows 用 PowerShell 5.1、任务计划程序和 Windows Script Host。
- 至少一个你装好并登录的命令行 Agent；模型用量记在你自己的账号上。
- 按功能可选：GitHub Issue 轮询和 PR 交付流水线要已登录的 `gh`，飞书卡片要 `lark-cli` 和一个飞书应用，用链接回答的 Webhook 通道要一个可访问的 `hub.publicUrl`（前面放你自己的 HTTPS 反向代理），GitHub、GitLab Webhook 也要投递到这个地址。

## 运维难度

**低到中。** 单机安装是一条脚本加一个用户级登录服务，数据在 `~/.agent-autoloop`（权限 0700，里面有主密钥和密钥配置，备份要按密钥保管）。一旦为 Webhook 或链接回答把中台暴露出去（HTTPS 代理要你自己配）、加飞书或 GitHub 凭据、在其他电脑上跑接单程序，就到了中等。日常维护是跟着每天的 Release 执行 `agent-autoloop update`、格式变化时偶尔的全量重建，以及盯住长会话续接的 Token 花费；`status`、`doctor`、`runs` 和 `why <轮次>` 在命令行里就能排查。

## 健康度与可持续性

- **维护（2026-11-18）：** 非常活跃，15 天内 239 次提交、25 个 Release（2026-11-03 的 v1.0.0 到 2026-11-18 的 v1.9.2），CI 覆盖 Ubuntu、macOS 和 Windows，另有夜间模拟。修复先进 `main`，下一个 Release 才到用户手上；没有长期支持分支。
- **治理与巴士因子：** 仓库属于个人账号，路线由所有者决定；`main` 上 239 次提交里有 156 次记在所有者名下，范围取舍也在 Issue 里由所有者拍板（界面和多语言都拒了）。其他账号的 PR 合并了 83 个，说明有真实的外部贡献，但不是共同维护。
- **年龄与 Lindy：** 只有 15 天，Lindy 先验几乎给不了支撑；星标涨得比任何履历都快。[推断：依据是创建 15 天内 5.8k 星、1.07k fork，以及所有者 5.2k 关注者] 把热度当作关注度，不当作生产使用的证明。
- **采用信号：** 两周内 25 个 Issue；已关闭的 23 个里有 22 个在 24 小时内关闭，要么修了代码，要么写明了决定。场景模板和插件都是官方自带的，README 列清了哪些 Agent 和通道真跑过（Claude Code、Codex、ACP、ZCode、飞书），哪些只对着模拟服务测过（Webhook 模板、GitLab）。
- **雷达实测：** C，六个轴都有分。采用度是 E，是因为包标了 `private`、靠 `git clone` 安装，没有包仓库下载量或依赖方数量可量，不代表没人用；寿命 D 反映的是 15 天的年龄。
- **风险信号：** MIT，版权人是作者本人，没有 CLA。主要风险在运行层面（提示注入落到有写权限的 Agent 上、个人订阅用于自动化的条款问题、只有中文界面），不在许可证。

## 存疑（未验证）

- [未验证：本批不允许安装或运行上游代码] 安装、`try` 一轮、跨 Agent 的会话续接和 Windows 服务都是读源码和文档得出的，没有复现。
- [未验证：作者自报，没有同硬件复测] 基准数字（冷启动 88.78 毫秒、每秒 2,394 次持久写入、110 万条事实重建 43.1 秒）来自 README，测试机是 Apple M5 Pro。
- [推断：依据是星标与 fork 增速相对项目年龄，以及所有者的关注者数] 采用热度更多反映作者的受众，而不是实测的生产使用。
- [未验证：没有完整审阅厂商条款] 某个厂商是否允许用个人订阅做后台自动化，取决于它当前的条款；README 只给了指向。
- [未验证：本批进行期间上游有更新] 源码按 `ca5c0ffe2c92be17502c4f1a75cdb71823eeafef` 审阅；上游快照记录的是脚本运行时 GitHub 上的状态。
