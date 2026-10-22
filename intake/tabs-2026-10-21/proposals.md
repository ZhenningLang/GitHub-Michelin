# 待维护者裁决的项目

这些项目暂不建页，标签保留。`propose` 不是删除或永久拒收。
许可缺口不等于侵权判决，也不等于整个项目没有原创代码。
本次未安装、执行或吸收这些项目的代码。

## 一个非公开候选

GitHub API 确认不是公开开源项目，且未给出开源许可证。
主会话已用 GitHub API 复核可见性与许可。原始响应仅留本地工作记录，不进入公开提交。
不复制内部代码、文档、配置或实现信息到公开索引。
需维护者明确公开及许可后，才继续开源选型页流程。

## JimLiu/baoyu-design

项目有实际脚本和可复用组件。暂缓原因不是年轻或功能风险。
[README](https://github.com/JimLiu/baoyu-design/blob/6530033592bf7fa58bc1a5a2a2ad278da45213a9/README.md#credits--license)、[来源记录](https://github.com/JimLiu/baoyu-design/blob/6530033592bf7fa58bc1a5a2a2ad278da45213a9/skills/baoyu-design/references/upstream-sync/provenance.json)和[应用报告](https://github.com/JimLiu/baoyu-design/blob/6530033592bf7fa58bc1a5a2a2ad278da45213a9/skills/baoyu-design/references/upstream-sync/apply-report.json)记录了从 Claude Design 产品前端提取和复制的内容。
[根 MIT](https://github.com/JimLiu/baoyu-design/blob/6530033592bf7fa58bc1a5a2a2ad278da45213a9/LICENSE)只列 Jim Liu；所读文件未提供提取内容的再许可证明。
按本批次对“闭源产品提取内容”的规则暂缓，不自行做法律定性。

## liseami/CCBaga

原创身份归档与恢复实现具有实质内容，不因凭据操作或删除功能而拒收。
上游自己的 [NOTICE](https://github.com/liseami/CCBaga/blob/bdfb90ceadfc5fae6772ffff597bddecb0b73cc3/NOTICE.md#vendored-interface)明确写明：复制的 `vendor/cromma-ui` 没有独立上游许可声明，发布前应确认再分发条款。
树检查也未发现该子树的许可文件。根 MIT 不替代第三方授权。
主会话已读取 NOTICE 交叉确认。需维护者裁决后再决定是否带明确警告收录。

可供后续研究的机制是[先校验归档再切换状态](https://github.com/liseami/CCBaga/blob/bdfb90ceadfc5fae6772ffff597bddecb0b73cc3/src-tauri/src/identities/store.rs#L452-L630)：检查待恢复内容，保存当前状态，再用待恢复标记与回滚处理失败。
这只是静态源码的设计参考，不是本轮实测；本次不读取用户凭据，也不吸收身份轮换或网络部署脚本。

## breferrari/obsidian-mind

项目有实质记忆与 hook 实现，不能因以下缺口称它是整体复制品。
subagent 比较两个递归 Git 树，发现十个文件 blob 完全一致，其中八个为技能或参考文档。
[目标 LICENSE](https://github.com/breferrari/obsidian-mind/blob/fae7be467fc5e23bf9d51df7207d41f0c07e2754/LICENSE#L1-L13)只署 Brenno Ferrari；[上游 LICENSE](https://github.com/kepano/obsidian-skills/blob/3ccff5338ea700537839b21900aa5358a0402c98/LICENSE#L1-L13)署 Steph Ango，并要求保留声明。
subagent 对完整归档的 325 个文本文件扫描，未找到该上游版权声明。README 致谢不能替代许可条款要求的声明保留。
按 worth check 报上游声明保留缺口，交维护者裁决。

原创记忆实现中的[召回范围检查](https://github.com/breferrari/obsidian-mind/blob/fae7be467fc5e23bf9d51df7207d41f0c07e2754/.claude/scripts/lib/memory-recall.ts#L216-L245)把项目重合与共享平台作为显式可见性条件。
[会话注入](https://github.com/breferrari/obsidian-mind/blob/fae7be467fc5e23bf9d51df7207d41f0c07e2754/.claude/scripts/lib/session-start.ts#L130-L209)按字节预算分配内容，并记录摘要或指针等降级层级。
这些是待许可裁决后的机制研究候选，不是替换现有记忆账本的实施决定，也不证明模型召回效果。

## dzhng/skills

个人工程工作流有实质内容，本次不因小部分导入内容而否定其原创核心。
[复制 PR](https://github.com/dzhng/skills/pull/11)与目录检查确认小黑插画技能来自另一个技能包。
[原作者 MIT](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/686575741a61e2c0be5e4c6d3615ebf6217dd322/LICENSE#L1-L13)署 Ian，且早于该次复制；[目标根许可](https://github.com/dzhng/skills/blob/dc8f546c3adaa615ab86e8328449ae6efe23aca4/LICENSE#L1-L13)仅署 David Zhang。
subagent 检查复制子树全部六份 Markdown 及许可路径，未找到原作者版权和许可声明。
README 致谢不能替代完整许可声明，故按同一 worth check 待裁决，不作侵权法律判断。

可研究的原创机制是[选择审计账本](https://github.com/dzhng/skills/blob/dc8f546c3adaa615ab86e8328449ae6efe23aca4/skills/engineering/audit-choices/SKILL.md#L96-L136)：记录规格留白处的选择、影响和信心，结束时再与代码核对。
[证据检查脚本](https://github.com/dzhng/skills/blob/dc8f546c3adaa615ab86e8328449ae6efe23aca4/skills/visual/screenshot-critique/scripts/receipts.mjs#L9-L19)区分真实文件与静态命令转录；后者不能证明命令执行过。
这些只是待后续评估的机制候选。本批未复制技能，也不采纳“五分钟无人回复即继续决定”的人工审批策略。

## 验证边界

各项目只在未改内容的基线上跑门禁，结果均为 `0 errors, 1548 warnings`。
空范围扫描或基线门禁不是新页面验收；这些项目没有页面、卡片或索引投影。
原生 subagent 结果和取证材料留在对应独立工作区；公开记录只保留必要结论和公开来源。
