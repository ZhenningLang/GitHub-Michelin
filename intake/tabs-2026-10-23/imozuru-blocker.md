# imozuru：研究已做，收录被健康评分步骤阻断

固定源码提交为 `ecb82c71b611872a0f49e783eda3bec987c80d91`。已完成研究、双语草稿和流程／机制资产，但尚缺健康块及卡片。主会话没有把失败草稿集成到正式索引，也没有关闭标签。

被拦命令如下，`<workdir>`为专属研究工作区，不是上游参数：

```text
OSS_ATLAS_GH=<workdir>/.agent-state/bin/gh OSS_ATLAS_HEALTH_CACHE=<workdir>/.agent-state/health-cache GH_CONFIG_DIR=<workdir>/.agent-state/empty-gh python3 tools/health.py --page categories/deep-research/imozuru.md --write --evidence
```

护栏原文：`guard cannot tell what this gh command runs (the command changes gh's config location); run the underlying gh command directly.`

worker停止了该步骤；主会话没有改写环境或另包命令重试。评分是本仓库强制门禁，不能手工补造健康分数来放行。需要明确授权按项目标准路径重做健康评分后，才可补卡、复跑门禁、提交并关标签。此为本地执行阻塞，不代表项目不合收录资格。

当前草稿门禁：`4 errors`，全部来自健康块或卡片缺失；专项内容扫描没有确定性发现。这个专项结果不能抵消结构门禁失败。研究发现的引用逐字匹配、搜索外发、DNS重绑定及旧报告残留边界，仍需在后续正式收录时保留。

本次不将上游安装、研究效果或安全视作已验证；未运行上游。默认 `gh api` 查询公开仓库属于本批正常工具使用，不应把使用既有CLI认证误写成已经发生凭据泄漏；本任务没有读取或展示令牌。`no leftover Q&A`。
