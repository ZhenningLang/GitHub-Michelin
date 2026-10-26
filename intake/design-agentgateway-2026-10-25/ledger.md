# 三项定向收录台账 — 2026-10-25（UTC）

仅处理维护者指定三项（含追加OpenUI）；done须有完整双语页、验证与提交。local-complete表示内容和本地验证完成，准备进入已授权的原子内容提交；不是远端已发布。资格问题按真实证据propose，不沿用其它仓库的许可例外。

| 规范名 | 动作 | 结果 | 页面路径 | 备注 |
|:---|:---|:---|:---|:---|
| elayadesign/ai-design-skills | add | done | categories/agent-skills/design/visual-artifacts/ai-design-skills.md | 双语页、标准图卡与真实许可已审；主会话门禁／专项通过，独立来源预审零finding；独立提交2b3eda2；未加载上游；no leftover Q&A |
| agentgateway/agentgateway | add | local-complete | categories/api-gateway/agentgateway.md | 双语页、图卡与标准健康B（6/6）已接入；独立来源复核核心描述无确定错误；CEL通知完整保留未核清，补查遭拒且未绕过；默认允许、guardrail早于资源授权、stdio非沙箱均明示；未编译部署；no leftover Q&A |
| thesysdev/openui | add | local-complete | categories/ai-design-generation/openui.md | 追加项；固定SHA核界面语言、注册组件、流式解析／查询与工具权限；独立四文件来源复核零finding；MIT与图标／字体许可分开，安装遥测、云采集、Autofix及自托管缺口均明示；未运行上游；no leftover Q&A |

UTC 2026-10-26本地验收：`make gates`结构项为`0 errors, 1626 warnings`，反向报告已同步；六页专项为`No deterministic findings.`；工具回归为`Ran 483 tests ... OK`。全库报告型质量信号与旧页警告不作语义通过；发布仍未进行。原汇总现为137候选／135有页，原134条正文逐字不变，302个本地链接和195个内部锚点无缺失；完整机器证据见[最终验收记录](verification.json)。

维护者于2026-10-26授权“提交与发布”。网关、OpenUI与必要分类／路由作为联动内容提交，避免中间提交缺页；最终提交另做完整差异审查，再走功能分支PR和真实CI。原HTML阻塞与CEL通知缺口仍保留；不把本地汇总算作远端产物。后续PR和合并状态以远端记录为准，本台账不预填成功。
