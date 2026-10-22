# 已有项目阅读总结

以下内容来自实际打开的索引页面，不代表重新核验上游。
sync-entry 的默认期限是 90 天。五项均未超期，未改页面和核验日期。

| 项目 | 解决的问题 | 何时选它 | 何时不用 | 页面核验日 |
|---|---|---|---|---|
| [AgentsView](../../categories/agent-tooling/session-history/agentsview.md) | 会话散在多个编码助手里，难找历史和汇总费用。 | 希望本地统一检索、分析自己的会话。 | 需要托管团队看板或生产 LLM 链路追踪。旧快照记载默认遥测，零外联需单独确认。 | 2026-09-28 |
| [Taste-Skill](../../categories/agent-skills/design/ui-taste/taste-skill.md) | 生成页面总是同一模板。 | 没有品牌系统，想控制布局变化、动效和密度。 | 已有设计系统或品味技能。提示词不是质量硬门。 | 2026-09-27 |
| [Agent Orchestrator](../../categories/agent-tooling/supervision-surfaces/agent-cockpits/agent-orchestrator.md) | 多代理抢工作树，人要转发 CI 和评审反馈。 | 需要桌面看板监管多个隔离分支。 | 单代理、无头流水线或共享主机。旧快照记载本机接口无鉴权、默认遥测。 | 2026-09-28 |
| [SolidCraft](../../categories/cad/solidcraft.md) | agent 建出的零件仍要修改尺寸和特征。 | 试做支架、外壳，保留可编辑的参数历史。 | 生产关键工程、成熟制造流程。内置 MCP 不能替代几何验证。 | 2026-10-18 |
| [wshobson/agents](../../categories/agent-skills/subagent-collections/wshobson-agents.md) | 跨领域任务要反复手写专家提示。 | 按领域取用现成专家，并接受逐项审核。 | 已有成熟技能栈，或要求固定、可复现行为。不要整包叠加。 | 2026-09-28 |

## 借鉴候选

以下是建议，不是已实施的变更。未修改 dotfiles。

- **AgentsView，high，已接入。** 跨助手日志归一化和检索入口，已用于 `agent-harness-improvement`，不再另造一份。
- **Taste-Skill，medium。** 把布局变化、动效强度、信息密度作为 `fe-ui-design` 的可选输入，不覆盖品牌约束。反重复已有 `fe-ui-critique`，不引入第二套规则。
- **Agent Orchestrator，medium。** 给 `dev-long-run` 的 worker 按分支归属回送 CI 与评审事件。可参考 `sidecar` 的事件裁决结构，但不能悄悄扩大它的单目标边界。
- **SolidCraft，medium。** 工具先检查参数和文件路径，再分发操作。映射 `guard-secure` 的信任边界核查；路径授权不是进程沙箱，须考虑硬链接。
- **wshobson/agents，medium。** 将外部插件来源、固定提交和审批链列入 `agent-health` 检查。它是候选机制，不是本次已证实的缺口。

## 本次发现但未修改

Agent Orchestrator 的 frontmatter 指向 `OrchestratorInc`，正文仍称当前归属 `Untrivial-ai`。页面内部存在不一致。本批按 fresh 门槛未强制刷新；后续 sync-entry 应核实并统一。
