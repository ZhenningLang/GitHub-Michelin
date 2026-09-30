# security

> [agent-skills](../INDEX.zh.md) 的叶子。安全评审、威胁建模、网络安全 playbook。
> ← 上层 [agent-skills](../INDEX.zh.md) · 根 [路由](../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本叶子的合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Anthropic Cybersecurity Skills** | 一个大型网络安全技能包（约 817 个技能），由对齐 MITRE ATT&CK、NIST CSF、ATLAS、D3FEND、NIST AI RMF、MITRE F3 的 SKILL.md runbook 组成，按需加载进 coding agent。 | B（4/5） | [→](anthropic-cybersecurity-skills.zh.md) |
| **reverse-skill** | 当你的 AI 编码客户端需要一个通往 45 个逆向/渗透/CTF playbook 的路由器、带授权闸门与证据链报告时用它——双用途内容会触发杀软，且要求信任第三方写的 agent 可执行指令。 | A（4/5） | [→](reverse-skill.zh.md) |
| **android-reverse-engineering** | 当你只有安卓二进制、要把它调用的 HTTP API 面写成文档时用它——Claude Code 插件，jadx/Fernflower 反编译、恢复被 R8 藏起的 Kotlin 类名、扫 Retrofit/OkHttp/Ktor/Apollo 出端点与鉴权。 | B（4/5） | [→](android-reverse-engineering.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Anthropic Cybersecurity Skills](anthropic-cybersecurity-skills.zh.md) | ✅ | B（4/5） | 一个大型网络安全技能包（约 817 个技能），由对齐 MITRE ATT&CK、NIST CSF、ATLAS、D3FEND、NIST AI RMF、MITRE F3 的 SKILL.md runbook 组成，按需加载进 coding agent。 |
| [reverse-skill](reverse-skill.zh.md) | ✅ | A（4/5） | 通往 45 个安全 playbook 的任务路由器，带 case-guard 授权门和 175 例路由基准；自带 WAF/EDR 绕过 payload 语料被 Defender 判为恶意软件（#125），agent 自举的自动执行行为有争议（#134）。 |
| [android-reverse-engineering](android-reverse-engineering.zh.md) | ✅ | B（4/5） | 单任务安卓流水线：指纹分诊→jadx/Fernflower 反编译→R8 名字恢复→端点扫描，没有源码也能产出两层 API 文档；无授权闸门，安装脚本用 sudo 且改 shell rc 文件（#17 披露未处理），macOS bash-3.2 路径是坏的（#30/#31）。 |

## 什么该放这里

面向**安全工作**的技能合集——评审、威胁建模、网络安全 playbook。
