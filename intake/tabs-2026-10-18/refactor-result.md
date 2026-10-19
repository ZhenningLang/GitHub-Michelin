# 最小分类迁移结果

主会话已单独提交结构改动：`91b5347`。以下子任务验收记录保留当时的未提交状态；当前为本地已提交、尚未发布。

16 对页迁移已验收，尚未提交。
外部书签无法恢复；既有非阻断告警保留。

## 工作清单

- [x] 完整读取技能与已批准规划。
- [x] 核对规划差异，仅新增 OpenTunnel，合计 927 对。
- [x] 冻结全部页面、索引与图源快照。
- [x] 使用 git mv 迁移 16 对页。
- [x] 精确修复双语索引、README 分组与本地链接。
- [x] 同步健康列并重建反向报告。
- [x] 运行 make gates 与逐页保真验收。
- [x] 输出机器统计与外部书签风险。
- [x] 提交、浏览器、台账更新：按授权明确跳过。

宿主没有任务清单工具，本清单承载执行状态。

## Boundary facts

- 规划快照的 926 对页均未修改或删除；仅增加 OpenTunnel。
- `tools/schema.md` 允许父节点同时持有项目和孩子。
- 已批准四个自然子类，并保留父节点剩余页。
- 监督界面按人的查看、审批和引导职责分类，不限载体。
- 迁移不改变 slug、事实日期、健康评分、判断正文或生成文字块。
- 本地链接按旧位置解析，再映射目标并从新位置计算。
- `flows/`、`mechanisms/` 与 `assets/` 保持原名和原字节。

## 已知风险

11 对既有页改变路径。仓库内链接修复不能恢复外部书签。
不放置旧路径占位页，避免重复收录与分类契约冲突。

## 结果

完整映射和机器证据见 [refactor-result.json](refactor-result.json)。
冻结 HEAD 为 `eede19b4fbeb925c2f942e3676655b81674b3986`。
恢复后未重复迁移，没有丢弃已落盘修改。

| 验收项 | 迁移前 | 迁移后 |
| --- | ---: | ---: |
| 项目页对 | 927 | 927 |
| 分类节点 | 191 | 195 |
| 超过十二页的节点 | 6 | 0 |
| 最大直接页对数 | 15 | 12 |
| 监督界面直接页对 | 8 | 10 |

新建四个双语子类索引。
父节点保留直接页，不强建对称孩子。
Agor 与 dsh-TUI 转入已有监督界面类。

### 保真与链接统计

- 逐页检查全部 1,854 份项目文件。仅分类字段及相对链接改变；正文判断、章节顺序、事实日期和健康度保持。
- 1,856 个生成文字块原字节一致。2,240 份冻结文件与原 HEAD 的原始字节一致，排除了换行归一化掩盖差异。
- 4,591 份资源原名、原字节不变，包括 828 份流程源、84 份机制源与 3,679 张 SVG。
- 16 个移动 slug 在全库唯一。图卡 stem 不变，无需重生图。
- 首轮精确重定位 710 处 URL，涉及 164 份源文档。其中项目页 584 处、分类索引 62 处、README 64 处。
- 上述分类索引中的 60 处随原摘要和比较行迁入目标索引。710 不是净新增链接数。
- 全树 26,345 个本地 Markdown／图片链接均可解析。原项目页锚点和查询后缀不变。
- 双语 README 各保留 927 条唯一登记。各重分组 16 行，不改摘要、许可证或健康列。

迁移了 60 行原摘要与比较判断。
MLX 和 dsh-TUI 原索引缺少比较行。
其双语比较行复用原摘要，不新增选型判断。

已有图像子类、Maka、T3 Code、OpenChamber、OpenHands、LobsterAI、TimesFM 与 SwiftUI Pro 均保留原路径。

### 交付物验证

| 交付物 | 存在 | 实质 | 接通 | 状态 |
| --- | --- | --- | --- | --- |
| 16 对迁移页 | 32 个目标文件，32 个旧路径消失 | 32 条暂存 git 重命名记录；全部项目正文保真 | 父子索引、README 与入链全部接通 | 已验证 |
| 四个双语子类 | 八份新 INDEX | 成员与批准的四簇完全一致 | 父节点导航、返回与根路由均有效 | 已验证 |
| 主登记与报告 | 双语 README 和反向报告存在 | 每种语言 927 条唯一项目登记 | 反向报告新鲜度检查通过 | 已验证 |
| 结果文件 | 本文件及同名 JSON | 含完整映射、统计、命令和风险 | 引用本次机器日志 | 已验证 |

### 命令与关键输出

恢复后完整重跑三条命令，退出码均为零：

```text
python3 tools/sync_index_health.py --apply
fixed 0 row(s) across 392 summary files.

python3 tools/reverse_index.py --write
repo -> page entries: 927
full mislabels (blocking, must be 0): 0

make gates
195 category nodes, 927 EN + 927 ZH pages, 0 errors, 1544 warnings.
reverse_index check: reports are current, no full mislabels (0 partly-indexed rows tracked in reports/project-intake-backlog.md)
Project pages scanned: 1854
English canonical pages scanned: 927
exit code: 0
```

`git diff --check` 退出码为零，无输出。
没有修改工具、测试、分类上限或门禁规则。
纯文档迁移未运行工具单测；全量保真检查与项目门禁承担验收。

### 验证证据分层

| 层级 | 结果 | 来源 | 证据 |
| --- | --- | --- | --- |
| Inner-loop evidence | 通过 | 本次复跑 | 三项 make gates 门禁与空白差异检查 |
| Integration evidence | 通过 | 本次复跑 | 健康列无漂移；反向报告与 927 条目一致 |
| Acceptance evidence | 通过 | 本次复跑 | 全部 927 对守恒，四簇及父节点成员精确匹配规划，六处溢出消除 |
| Holdout / unseen evidence | 边界回归替代 | 本次复跑 | 全库保真检查，加八组明确保留的历史边界 |
| Known gaps | 保留 | 本次复跑 | 外部书签；既有非阻断告警；无独立盲测集 |

Holdout 来源类别：真实捕获。
预期值来源：需求原文、已批准规划和仓库合同。
本次只改冻结点之后的文档生成／迁移侧，不改判定工具。

首轮范围断言把主会话新增的 `plan.md` 纳入报错。
已补正文件归属，未改动该文件。
这是验收归属修正，不是正文失败或内容修复；内容修复次数为零。

### 日志与恢复记录

日志目录：

```text
/private/var/folders/5m/p1nlq0ns455bc366q_z8zj4w0000gn/T/opencode/
```

- `refactor-before.json`：冻结页面、索引和资源哈希。
- `refactor-links.json`：32 文件映射与逐 URL 机械修改记录。
- `refactor-acceptance.log`、`refactor-acceptance.json`：全量保真、守恒、资源和边界回归。
- `refactor-health-resume.log`、`refactor-reverse-resume.log`：恢复后同步日志。
- `refactor-gates-resume.log`：恢复后的完整门禁输出。
- `refactor-gates.log`：中断前已完成的门禁输出，保留未覆盖。

门禁仍报告 1,544 条结构 warning。
质量扫描保留 75 条非阻断 finding，阻断分类均为零。
没有借迁移刷新正文或扩展治理范围。

机器刷新了三份报告；实际差异仅在两份 CSV。
原报告正文未漂移，也未动主会话的 intake 报告。
git 重命名已暂存；后续链接修改与新文件尚未提交。

## Boundary decisions

无新增越界裁决。沿用已批准的混合父节点、按职责划分监督界面，以及 Apple 优先而非平台排他边界。

下一步由主会话更新台账路径，再审查并提交本轮文档迁移。
