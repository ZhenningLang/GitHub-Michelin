# Tab intake ledger — 2026-10-26 (UTC)

来源：维护者明确要求再次执行`/intake-tabs`，只读取本人Chrome的GitHub仓库标签，按PID排除自动化实例。原全量汇总仍在既定本地忽略路径；本轮不另建替代总报告。

## Boundary facts

- 浏览器授权仅覆盖GitHub仓库标签的识别，以及完整收录、门禁通过并提交后的匹配标签关闭。非GitHub标签、本人仓库、组织入口和暂缓项保留；不读取登录凭据或浏览器存储，不安装执行上游。
- 原报告是汇总权威；先冻结实际当前版本和哈希，再增量整合。本轮不删除历史候选、不倒写旧核验日、不移除许可告警；原HTML拒绝继续有效，不重试渲染、配对或浏览器验收。
- 新页以固定公开源码为事实源；未知许可、同源和危险载荷按资格五问调查，灰区保留为proposed。未经公开性核验的元数据不得直接提交；非公开及自有身份在公开记录中匿名，不读非公开实现。
- 新增页和必要索引／生成资产在本轮功能分支；逐项目门禁和独立提交，类别溢出另做纯路由提交。主checkout不写入、不切分支、不提交或同步；新分支远端推送另取精确授权。

## Operational Contract

- 方向：公开固定来源→双语页→机器生成图卡和索引，只增量更新，不传播上游删除。已核本批结果→原本地汇总，按身份去重并保留旧正文；用户当前报告不被旧快照覆盖。
- 恢复：本台账是检查点，done不重做；每个提交和匹配标签关闭各记机器证据。原汇总在第一次修改前有冻结副本，逐项核哈希；失败不把未研究内容记为已完成。
- 效率：先测队列规模，研究最多三个隔离worker并行，主会话串行接索引、门禁、提交和标签操作；外部查询有界超时，不无限重试。
- 观测：每轮记录pending、running、done、failed、proposed和skipped数量；逐项报告完成点，项目间复扫，新增标签加入队列。只在现有本地忽略状态目录保留原始浏览器及元数据证据。
- 数据验收：核身份唯一、预期新增／更新数、旧项目保真、来源blob、双语与图卡、当前Markdown文件／锚点；独立来源复核及真实历史回归替代虚构留出分数。lint或测试绿不等于上游效果通过。
- 回退：页面与路由由独立提交定点revert；原报告按冻结版本恢复本轮写入，保留旧历史和其它工作区。标签仅关闭已提交项目，保留关闭前规范身份和计数用于核对；不得误关后靠猜测恢复用户状态。

## Queue

| 规范名 | 动作 | 结果 | 页面路径 | 备注 | 标签里的写法 |
|:---|:---|:---|:---|:---|:---|
| datawhalechina/diy-llm | add | pending |  |  | datawhalechina/diy-llm |
| ihhub/fheroes2 | add | pending |  |  | ihhub/fheroes2 |
| kdlbs/kandev | add | pending |  |  | kdlbs/kandev |
| kharmanskyi/open-steps | add | pending |  |  | kharmanskyi/open-steps |
| kunchenguid/no-mistakes | add | pending |  |  | kunchenguid/no-mistakes |
| llm-d/llm-d | sync | pending | categories/llm-inference/serving-engines/llm-d.md |  | llm-d/llm-d |
| XiaoLuoLYG/GOD | add | pending |  |  | xiaoluolyg/god |
| anonymous-own-1 | skip | skipped |  | 维护者自有仓库，按范围跳过；标签保留 |  |
