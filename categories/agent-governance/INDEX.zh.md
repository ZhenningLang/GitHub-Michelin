# agent-governance

> 分类节点。AI agent 的治理、策略执行、身份、沙箱与可靠性控制。
> ← 返回[分类路由](../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **agent-governance-toolkit** | Microsoft 面向 AI agent 的 public-preview 治理工具包：策略门控 tool call、身份 / 信任、审计 / 合规、MCP security gateway、SRE 控制和多语言 SDK。 | B（6/6） | [→](agent-governance-toolkit.zh.md) |
| **SkillSpector** | NVIDIA 的 AI agent skill 安全扫描器：安装前通过 CLI/MCP 检查 prompt injection、外传、危险脚本、MCP poisoning、依赖，并输出 SARIF/JSON 证据。 | B（5/6） | [→](skillspector.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [agent-governance-toolkit](agent-governance-toolkit.zh.md) | ✅ | B（6/6） | Microsoft 背书的宽 agent governance stack；生产 policy / audit 强，只做小型 middleware gate 时偏重。 |
| [SkillSpector](skillspector.zh.md) | ✅ | B（5/6） | 面向 skill artifact 的窄安装前 scanner；真正问题是 tool-call policy 和 audit 时，应配合运行时治理。 |


## 什么该放这里

AI agent 的治理、策略执行、身份、沙箱、可靠性控制与安装前安全闸门。
