# imozuru：评分阻塞已获授权解决

固定源码提交为 `ecb82c71b611872a0f49e783eda3bec987c80d91`。用户明确选择“允许标准评分”后，主会话执行项目标准健康评分入口，生成真实健康块与双语卡片，复跑结构和专项门禁并提交 `c191623`，再关闭标签。原阻塞不再存在。

评分时页面位于父目录，现已在独立分类提交中迁入 [source-workflows](../../categories/deep-research/source-workflows/imozuru.zh.md)。下列旧路径只记录当时命令，不是今天的页面定位。

被拦命令如下，`<workdir>`为专属研究工作区，不是上游参数：

```text
OSS_ATLAS_GH=<workdir>/.agent-state/bin/gh OSS_ATLAS_HEALTH_CACHE=<workdir>/.agent-state/health-cache GH_CONFIG_DIR=<workdir>/.agent-state/empty-gh python3 tools/health.py --page categories/deep-research/imozuru.md --write --evidence
```

护栏原文：`guard cannot tell what this gh command runs (the command changes gh's config location); run the underlying gh command directly.`

worker当时停止了该步骤。主会话收到明确授权后，使用 `python3 tools/health.py --page categories/deep-research/imozuru.md --write`，没有修改认证配置、护栏或手填健康分数。该问题属于本地命令配置，不代表上游资格不合格。

授权补齐后，主会话门禁为 `0 errors`，双页专项扫描为 `No deterministic findings.`。引用匹配不等于语义核验、搜索词外发、DNS重绑定及旧报告残留边界均保留。新增后出现的分类溢出单独整理，不混进项目研究提交。

本次不将上游安装、研究效果或安全视作已验证；未运行上游。默认 `gh api` 查询公开仓库属于本批正常工具使用，不应把使用既有CLI认证误写成已经发生凭据泄漏；本任务没有读取或展示令牌。`no leftover Q&A`。
