# 公开重放：集成与隐私审查

两项新页仍待独立语义审查，最终 HEAD 也待验收。本次未发现旧补丁重放的集成或隐私阻断，可以继续发布准备；不代表批准合并。

## 范围与绑定

- 审查 HEAD：`eb11fd1c89eff768854fa4c6a44588878ad934e8`。
- 本地远端跟踪基线：`69ae87249c7ae9e57fd0635c59cf04a4c7d0e642`，即 Harness² 的 PR 199。
- 旧补丁终点：`83a1e96c7f01e6e96903fd9b414464215122d660`。
- 原始本地 tip：`b558b59773a0b94ceaa5d6886859571efa164a50`。
- 工作树元数据扫描时刻：`2026-10-19T05:54:09.137176+00:00`。

采用 `guard-review` simple 与 `guard-secure` 只读方法。不启动下级 agent，不做 two-pass。只写本报告和同名 JSON，不提交、不推送、不打标签。

范围是旧 61 项已验收补丁、16 对分类迁移及当时的 intake 元数据。`harness/harness` 与 `parthh01/sphinx` 的研究和语义裁决由独立 worker 承担。本次不重研 61 个上游，也不认证其运行效果。

原始私有台账仅取对应行作内存比较。报告不保存身份、URL、匹配词或私有实现。该原始分支必须只留本地，不能作为公开分支推送。

## 工作清单

宿主没有任务清单工具，以下记录执行范围。

- [x] 读取既有语义、事实及迁移验收材料。
- [x] 对账 diff manifest 与提交范围。
- [x] 重算源文件、生成块及迁移保真。
- [x] 核验主干新增页、路由及提交可达性。
- [x] 扫描新提交、变更对象及工作树元数据。
- [x] 写出本次结论与明确缺口。
- [ ] 两项新页语义审查：跳过，由独立 worker 负责。
- [ ] 最终 HEAD 全库门禁、review 与发布：留给主任务。

## Diff Overview 与覆盖口径

复用批准临时目录中的 `intake-public-diff-manifest.md`。本次另用 Git 对账，全部 `(path,status)` 身份一致。

```text
manifest_file_rows: 876
actual_files: 876
path_status_sets_match: true
status_counts: M=205, A=649, R=22
manifest overview: +56055 / -570
```

分类迁移总数是 16 对。相对主干只有 11 对既有页表现为重命名，其余 5 对属于本批新增页，因此这里是 22 个重命名文件。

| 文件组 | 差异文件数 | 本次覆盖方式 |
| --- | ---: | --- |
| 分类文档、图源与 SVG | 846 | 全树对象哈希、迁移前正文归一比较、生成块逐字节比较；不重做每页语义审查 |
| 根索引与双语 README | 4 | 路由存在性、登记行守恒及原始 tip 差异核验 |
| 反向报告 | 3 | 对原始 tip 核验；只有仓库索引多一条 Harness² 登记 |
| 已提交 intake 元数据 | 23 | 隐私模式扫描；指定事实与验收材料语义复用 |

manifest 将 876 项均标为 `deep_review`。本次按用户指定的集成范围覆盖，不将机器扫描或复用材料说成 876 文件逐行全量复审。另扫描当时工作树的 27 份元数据；其哈希见 JSON。新汇总等并行产物只纳入隐私扫描，不据此取得语义放行。

## Aspect Coverage

| 维度 | 处理 | 证据或跳过理由 |
| --- | --- | --- |
| code | 跳过运行逻辑审查 | 文档、静态图和报告变更；工具及执行配置无变化 |
| tests | 核验已有记录；不重跑 | 61 条逐项门禁记录均干净；不把旧工具成绩当本轮运行结果 |
| errors | 跳过 | 没有新增错误处理或外部调用代码 |
| types | 跳过运行时类型审查 | 没有 schema 或 API 合同变化；元数据映射另作对账 |
| hostile-input | 跳过 | 没有新增解析器或扫描循环代码 |
| blast-radius | 运行确定性核验 | 源对象、全部旧页正文、生成块和路由均有机器检查 |
| comments | 读取指定报告并复用语义证据 | 区分历史快照、静态机制与效果结论 |
| simplify | 跳过 | 只读审查，不混入文档清理 |

负载假设不适用：本范围不改运行行为。规则映射已读取，JSON 使用现有专用规则，其他文档使用现有默认规则。

## 集成证据

### 源文件与主干保留

本次用 `git ls-tree -r -z` 比较 Git blob 身份，而非只采信已有 `replay-audit.json`。

```text
source_files: 6835
identical_files: 6833
differing_old_files: 2
added_content_files: 10
added_identical_to_main: 10
MAIN ANCESTOR: true
SOURCE TIP IN PUBLIC ANCESTRY: false
MAPPING ROWS: 61
MAPPING REACHABLE: 61
```

两处旧文件差异仅为 `workflow-builders/INDEX.md` 与中文镜像。逐项核对 diff，均只新增主干 Harness² 的摘要行和比较行。其 10 份页面、图源与 SVG 与主干字节一致。

旧 tip 的根索引未变。双语 README 各保留原有 927 条登记，只新增一条 Harness²。三份反向报告中，仅 `repo-page-index.csv` 增加对应一行；另外两份字节不变。

### 迁移正文与生成块

本次从迁移前提交 `eede19b4` 读取全部旧项目文件。仅归一分类字段和本地链接解析目标，再比较其余完整文本。旧目标先按 16 对迁移映射转换，查询和锚点后缀参与比较。

```text
moved_pairs: 16
mapped_old_paths_absent: 32
destination_paths_present: 32
pre_migration_project_files: 1854
project_normalized_body_mismatches: []
generated_blocks_compared: 1856
generated_block_mismatches: []
pre_migration_asset_files: 4591
asset_mismatches: []
```

生成块直接比较原始字节，未归一换行。图源与图片未重生。既有事实、章节判断和生成文字保真结论仍成立。

另扫描当前提交的分类文档、根索引和 README 中的本地内容链接。检查跳过代码围栏，覆盖内联链接与引用定义；只验证目标文件存在，不重新判定锚点存在。

```text
route_documents_checked: 2250
local_content_link_occurrences_checked: 26369
unresolved_content_paths: []
README.md: 927 -> 928; removed_or_changed_rows=0
README.zh.md: 927 -> 928; removed_or_changed_rows=0
```

### 证据映射与执行边界

逐条核对工作树 `per-repo-verification.json` 的公开提交映射。61 个公开内容提交都在当前 HEAD 祖先链内；122 份对应内容页与原始内容提交字节相同，最终双语路径均存在。

```text
PER-REPO: 61 rows; 122 content files; mismatches=[]
gate_records_zero_errors: 61
scoped_quality_records_clean: 61
PROTECTED PATH CHANGES ACROSS ALL COMMITS: []
git diff --check origin/main..HEAD: exit 0
```

保护路径检查覆盖整个新增提交范围，不只检查净 diff。`tools/`、`.github/`、`AGENTS.md`、技能配置、Makefile 和预提交配置均未改变。

工作树新增的 `public_content_commit` 保留公开可达身份，旧 `content_commit` 保留历史证据身份。台账也已重映射。它们尚未提交，最终发布必须包含主任务确认后的版本；本报告不替主任务提交。

## 隐私与安全检查

项目没有 `docs/threat-model.md`，本次降级为通用 STRIDE 检查。静态内容公开边界是重点；不因缺少运行时认证或限流提出无关 finding。

本次检查所有 65 个新增提交的 diff、提交说明及路径，也读取其 1,201 个唯一变更 blob。私有身份按规范名、原别名及有辨识度的仓库名组件作不区分大小写比较。匹配词只留内存，不写报告。

凭证模式覆盖常见 GitHub、AWS、Slack、模型服务密钥、私钥头及 URL 内嵌密码。该检查不证明任意格式秘密都不存在。

```text
new_commits_scanned: 65
unique_changed_blobs_scanned: 1201
private_identity_hits: 0
high_confidence_credential_pattern_hits: []
working_metadata_files_scanned: 27
working_metadata_private_hits: 0
working_metadata_credential_hits: 0
```

- 信息泄露：未命中指定私有身份或上述凭证模式。公开台账只保留占位行。
- 篡改与抵赖：对象哈希、提交祖先和原始到公开映射均核对通过。
- 伪装、拒绝服务与提权：本 diff 未引入对应运行入口，不扩展为上游安全认证。

没有发现需要误报裁决的 Critical 或 Important 安全项。没有执行外部安全扫描、联网核验、上游代码、浏览器、会话读取或凭据读取。没有新增依赖，故不触发依赖 CVE 扫描。

## 语义证据复用

本次完整读取以下材料，采用其顶部当前裁决，不把归档初审阻断当现存漏洞：

- `evolution-evidence.md`：固定源码机制、未运行上游及收益限制。
- `facts-review.md:3-48`：原三项阻断已关闭，仅放行静态机制与适配建议。
- `batch-facts-review.md:3-15`：唯一事实阻断已关闭，仅放行批次汇总。
- `refactor-result.md:55-103` 及同名 JSON：迁移正文、生成块、登记与链接保真。
- `per-repo-verification.json`：61 项旧门禁与内容提交记录。
- `final-verification.txt`：昨日工具成绩及发布边界快照。

这些材料不是新的上游研究或独立效果实验。部分历史关闭标签、权限事件与执行顺序仍依赖当时记录，本次不重新认证。

昨日报告中的“待发布”“尚未提交”和护栏阻断是带日期的过程快照，不是内容安全漏洞。审查期间主任务已在工作树添加历史说明和新汇总入口。时态更新不改变原有机制结论，也不能替代最终发布证据。

## 验证结果

| 交付物 | 存在 | 实质 | 接通 | 状态 |
| --- | --- | --- | --- | --- |
| 本报告与同名 JSON | 两份文件存在 | 含实际机器计数、范围、证据哈希和待验收项 | 绑定同一 HEAD，引用的七份语义证据均存在 | 本次审查交付已验证；最终发布仍待验收 |

本次运行本地只读 Python 校验。它解析 JSON，核对文件组及状态计数、快照哈希、证据路径和未批准合并的裁决。

```text
AUDIT STRUCTURE: PASS; JSON parsed; 876 manifest identities accounted; 27 metadata hashes consistent
AUDIT SCOPE: PASS; no final merge approval; both new-entry semantic reviews explicitly pending
CURRENT HEAD: eb11fd1c89eff768854fa4c6a44588878ad934e8
CONCURRENT METADATA DRIFT AFTER SNAPSHOT: []
```

| 证据层 | 来源 | 结果 |
| --- | --- | --- |
| Inner-loop evidence | 本次复跑 | 审查文件 JSON、计数、哈希和路径校验通过 |
| Integration evidence | 本次复跑 | 源树、迁移正文、生成块、README 和主干接通检查通过 |
| Acceptance evidence | 本次复跑 | 旧重放范围及指定私有身份边界通过；不替两项新页放行 |
| 旧页语义与历史工具成绩 | 复用他人证据 | 来源为上节七份记录；未冒充本次复跑 |
| Holdout / unseen evidence | 本次复跑 | 不做模型效果验收；以全部旧语料保真和主干新增页边界回归替代抽样 |
| Known gaps | 本次复跑 | 两项新页、最终 HEAD、后续并行改动与外部书签，见下节 |

Holdout 来源类别：真实捕获。预期值来源：需求原文、已批准迁移映射与仓库外部契约。本次改动相对冻结点的位置：仅新增判定侧报告，不改生成侧；冻结对象为上述 HEAD 和带时间的元数据快照。

测试、构建及 UI 验证不适用于本次两份审查文档。没有调用会写缓存或执行项目逻辑的通用验证入口；采用本地只读确定性检查，未扩展授权。

## 实际问题与裁决

**Issues：未发现本范围内可复现的集成或隐私阻断。** 没有命中破坏性执行、虚构路径、注入、新依赖未锁定、测试删除或 CI 放宽等 Hard Stop。未发现未经要求的运行范围扩张。

已知限制不是新增漏洞：11 对既有页的外部书签无法在仓库内修复；昨日非阻断告警继续保留。本次没有重新执行全库门禁、工具单测或 HTML 视觉验收。

**Ready to merge? No。** 原因是两项新页及最终 HEAD 尚未取得完整验收，不是本次发现了阻断漏洞。**可以继续发布准备。** 本结论仅绑定上述 HEAD 和 JSON 中记录的工作树快照；并行写入和后续提交不自动继承审查。

下一步由主任务完成两项新页独立语义审查，纳入元数据修订，再对最终 HEAD 跑门禁、隐私扫描与最终 review。
