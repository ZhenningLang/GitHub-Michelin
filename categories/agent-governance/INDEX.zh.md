# agent-governance

> 分类节点。AI agent 的治理、策略执行、身份、沙箱与可靠性控制。
> ← 返回[分类路由](../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **agent-governance-toolkit** | Microsoft 面向 AI agent 的 public-preview 治理工具包：策略门控 tool call、身份 / 信任、审计 / 合规、MCP security gateway、SRE 控制和多语言 SDK。 | B（6/6） | [→](agent-governance-toolkit.zh.md) |
| **SkillSpector** | NVIDIA 的 AI agent skill 安全扫描器：安装前通过 CLI/MCP 检查 prompt injection、外传、危险脚本、MCP poisoning、依赖，并输出 SARIF/JSON 证据。 | B（5/6） | [→](skillspector.zh.md) |
| **Snyk Agent Scan** | Snyk 的整机扫描器：清点 14 种编程 agent 里已装的 MCP 服务和 skill；发现在本地做，但每个结论都来自 Snyk 托管的闭源分析接口（要账号、有配额、数据外传）。 | A（6/6） | [→](agent-scan.zh.md) |
| **claude-skill-audit** | 离线正则扫描整个 Claude Code `.claude/` 目录（skill、agent、hook、权限、MCP 配置、密钥）的零依赖 TypeScript 小工具；单一作者、0 star、检测浅，只能当快速 lint 用。 | C（5/6） | [→](claude-skill-audit.zh.md) |
| **skills-scanner** | 零依赖的 Python CLI：盘点 Claude Code、Claude Desktop、Cursor、Windsurf 下的 skill、命令和 MCP 配置，离线跑规则，并与 SQLite 基线比对漂移。2026-05 起休眠且未上 PyPI：当模式来源看，不要当依赖用。 | C（5/6） | [→](skills-scanner.zh.md) |
| **agent-guard** | 安装前把关的 skill：把 skill、MCP 包、npm/PyPI/Go/cargo 包、release 二进制和安装脚本分派给 SkillSpector、Cisco mcp-scanner、GuardDog、OpenSSF package-analysis 或 VirusTotal，再合并成一个 fail-closed 的退出码；自己没有检测能力，单一作者，3 个 star。 | C（5/6） | [→](agent-guard.zh.md) |
| **Claude Skills Security Guide** | 一份 Claude skill 十二种攻击向量的书面目录，附手册和六个去掉杀伤力的示例攻击，外加三个演示水平、可直接拷入的防御 skill（正则扫描器、哈希清单、文本净化器）；2026-03 起无人维护，拿来读，别拿来卡流程。 | C（4/5） | [→](claude-skills-security-guide.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [agent-governance-toolkit](agent-governance-toolkit.zh.md) | ✅ | B（6/6） | Microsoft 背书的宽 agent governance stack；生产 policy / audit 强，只做小型 middleware gate 时偏重。 |
| [SkillSpector](skillspector.zh.md) | ✅ | B（5/6） | 面向 skill artifact 的窄安装前 scanner；真正问题是 tool-call policy 和 audit 时，应配合运行时治理。 |
| [Snyk Agent Scan](agent-scan.zh.md) | ✅ | A（6/6） | 一条命令清点并给所有已装组件打风险分，连运行中的 MCP 工具描述也读；检测器闭源托管、输出不稳定，而且会执行被扫描的服务。 |
| [claude-skill-audit](claude-skill-audit.zh.md) | ✅ | C（5/6） | 能从头读完、可离线运行的整套配置模式扫描；未经验证且已停更，看不到脚本、非英文注入和常见密钥格式。 |
| [skills-scanner](skills-scanner.zh.md) | ✅ | C（5/6） | 零依赖的整机盘点加漂移基线；规则只有浅层正则与语法树，单一作者，2026-05 后无更新，只能从 git 安装。 |
| [agent-guard](agent-guard.zh.md) | ✅ | C（5/6） | 一道“先扫后装”的闸门覆盖多种目标类型和本机所有 agent；代价是很深的工具链（uv、Docker、特权容器），以及一层没人用过、单人维护、包在上游扫描器外面的脚本。 |
| [Claude Skills Security Guide](claude-skills-security-guide.zh.md) | ✅ | C（4/5） | 威胁词汇、培训材料和测真扫描器用的攻击样本；它自己的扫描器把自家防御 skill 判成 CRITICAL，而且不调用就什么都不运行。 |


## 什么该放这里

AI agent 的治理、策略执行、身份、沙箱、可靠性控制与安装前安全闸门。
