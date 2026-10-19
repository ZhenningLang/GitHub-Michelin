# 2026-10-19 二次收录与合并

- [x] 用户授权续跑、切换脱敏发布工作区并交付远端 main。
- [x] 重放旧批次已验收内容，脱敏全部公开历史；保留原始本地分支。
- [x] 合入最新 origin/main，重扫 Chrome，保留上轮待裁决状态。
- [x] 并行研究新候选，串行门禁、单仓库提交、关闭 done 标签。
- [x] 更新双语索引、汇总与 HTML；完成内容审查与总验收。
- [ ] 精确 push 授权、PR、CI、合并，核实远端 main。

不改 dotfiles，不执行上游代码；私有候选不进入公开历史。
没有 todowrite 工具，以本文件记录可恢复计划。
回退：保留原始分支；远端通过受审查的 revert PR 撤销，不强推。

## 当前证据

- 重放 61 个项目内容提交与独立分类提交；公开树保留新增 Harness² 主干页面。
- 6,835 个旧内容／图源文件对象保真；差异仅是主干新增项的两份分类路由。
- 公开新增提交 diff 不含私有身份；工具、CI、AGENTS 契约未变。
- 重扫 10 行：2 新项目、1 fresh、6 沿用 proposed、1 自有 skipped。
- 中期全库门禁：928 EN + 928 ZH，0 errors；两个新项目仍由独立 worker 研究。
- 暂存和原始扫描只落批准临时目录；公开台账只存私有占位，不修改工具解析规则。
- 用户已授权精确命令 `! git push -u origin feat/intake-tabs-2026-10-18-public`，验收与 CI 通过后合并 main。
- 用户临时新增 Kruk2/jasna，重扫已登记第 11 行；独立 worker 重启后按断点恢复。
- 宿主重启恢复点：HEAD `eb11fd1c`；Harness OSS 补丁已应用且主会话门禁通过，仍待独立语义审查，不重复应用。
- Sphinx 补丁在 worker-2-results 完整保留，尚未应用；Jasna 由 worker-3 从断点续跑。
- 旧重放的隐私／集成审查通过；最终提交的 review 必须等新页及报告全部落盘后绑定新 HEAD。
- 三项新页均独立复核放行并提交：Harness `7fdb0e6`、Sphinx `78bc5a4`、Jasna `7490c7e`。
- 最终标签对账已落盘，不重复：85 个候选，64 新增、14 fresh、6 proposed、1 skipped；仍开 7 个，done 为 0。
- 全库 931 双语页对、0 errors、0 溢出；工具测试 483 tests，OK。
- 两个报告目录 companion 均为 0 errors、0 warnings；最终汇总已渲染并打开。
- 只剩最终提交审查与已授权的 push／PR／CI／merge，禁止再扩研究范围。
