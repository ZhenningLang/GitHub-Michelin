# 新增条目语义审查

两个补丁均放行。没有必须修复的实质缺陷。

裁决只绑定下列补丁，不代替主会话逐仓库门禁、提交与关标签。未审查 Kruk2/jasna。

| 仓库 | 裁决 | patchsha256 |
|---|---|---|
| harness/harness | allowed | `d4ba5907bf5b3d8d544dcbedccfbc76679e7be8378197b80405716203d3d6ad4` |
| parthh01/sphinx | allowed | `246945306d1cd340e35f1278edafa0d6d0be80b6e8268e633ff5bf23f7217e32` |

## 必须修复

无。限制性许可、可绕过的本地检查，以及上游安全风险，不构成拒收理由。两页已经说明这些边界，没有把收录写成部署安全背书。

## 可选改进

**Sphinx 研究缓存应保留原始字节。** 结果目录 `sources/` 中五份文件与固定 SHA 的 Git blob 不同：`src/evaluator.js`、`src/reviewer.js`、`src/mcp.js`、`src/working-context.js`、`test/evaluator.test.js`。例如考官源码第 107 行的控制字符正则，与远端原始文本不同。

79 项 `source-manifest.json` 的 SHA256 全部匹配本地文件，但这只证明缓存自洽，不证明缓存等同上游。本次另行从固定 SHA 获取这五份原文，并逐一核对 Git blob，全部匹配树记录。差异限于控制字符转义和相应测试字符串，不改变本页依赖的判据、隔离、外发或等待机制事实。因此不阻断这份内容补丁。后续若保留缓存作审计或源码用途，建议重新保存原始字节并更新 manifest；本审查未修改缓存。

## Harness 核查结论

固定源码：`f335f08374b83e9e4ddd54f4f47b4c6daad2fa54`。双语作者正文、flow 与 mechanism 源均完整阅读。

| 核查项 | 独立复核证据与结论 |
|---|---|
| 产品定位 | README、服务器与 runner 路径支撑 DevOps 平台定位；不是 Agent harness，也没有混入 harness2。 |
| Docker 权限 | README 挂载宿主 socket；`app/pipeline/runner/runner.go:42–51,85–90,121–126` 把发布插件特权表接入两个编译器。页面没有把容器或应用鉴权当恶意构建隔离。 |
| 默认外发 | `Dockerfile:83–88` 开启指标与 Gitspaces；`app/services/metric/values.go:40–64` 处理退出开关与持久标识；`collector_job.go:100–105,123–135,177–206` 取首位用户邮箱并发送每日载荷。页面分开说明 PostHog 与每日采集器，并提供显式关闭项。 |
| 文件级许可 | 根 LICENSE 为 Apache；`FavoriteStar.tsx:1–6` 是 PolyForm Shield，`.engops/pr_source_code_changes.sh:1–5` 是 PolyForm Free Trial。frontmatter、正文与雷达旁提示均披露混用，没有用根许可覆盖全树。 |
| 固定密码 | `app/gitspace/secret/password_resolver.go:26–36` 返回常量且忽略上下文；`secret/wire.go:20–29` 接入工厂。页中说的是具体解析器缺陷，不是宣称所有管理员使用默认密码。 |
| SQL 路径 | `registry/app/api/controller/metadata/list_webhooks.go:45–69` 先鉴权，`79–96` 传递排序方向；`registry/app/store/database/webhook.go:224–242` 在排序字段合法时格式化方向并执行查询。页面只称原始排序 SQL 路径，未复述未经验证的数据提取或会话伪造利用链。 |
| 网络边界 | `netpolicy/netpolicy.go:115–223` 检查实际连接地址；webhook 与 importer 的 transport 确实接入，webhook 不跟随重定向。`download_features.go:173–184,296–369` 的 tarball 下载与解包走另一条路径。页面正确限制共用策略的覆盖面，未把静态 grep 写成已验证 SSRF 利用。 |
| 版本与成熟度 | 区分 main 平台与 drone 分支发布；对历史 star、仓库年龄、浮动镜像一致性保留限制。 |

分类维持 `dev-utilities/ops-infra` 合理。检查现有分类树，未发现专属代码托管或 CI/CD 叶类；`workflow-orchestration` 面向批处理 DAG，不比此归类更准确。全库检索未发现已有 Gitea、Forgejo、Woodpecker、GitLab、Jenkins 或 Tekton 项目页。比较已覆盖两项更近的未收录替代；已打开 Argo Workflows 页，文中只把它用作集群工作负载策略轴的替代，没有冒充代码托管平台。

## Sphinx 核查结论

固定源码：`7485020c1e8784c060d9a616adcb5ddeea6da2fb`。双语作者正文、flow 与 mechanism 源均完整阅读。

| 核查项 | 独立复核证据与结论 |
|---|---|
| 产品定位 | 是推送前考人的代码理解检查；不是同名文档系统、数据代理、代码安全扫描或身份认证。正文明确理解缺陷不等于修复缺陷。 |
| 全局安装与兼容 | `src/install.js:237–288` 默认写全局 hooksPath；`312–317` 提醒仓库覆盖；`390–418` 先运行原 hook 并保留非零退出。页面同时说明显式仓库接入与设置软链目标写入，没有承诺所有 hook 都已运行验证。 |
| 绕过与失败关闭 | `src/git-gate.js:55–69,94–119` 区分 yolo、免题、Skip，以及问卷不可用、取消、超时或凭据无效。后几种会停止 Git；固定原文 `bin/sphinx.js:7–10` 将未处理错误转为非零退出，不是普通错误一律 fail-open。`124–129` 的 GitHub 状态写入才是 best-effort，不能当强制门禁。页面未混淆这些路径。 |
| 快照与原操作 | `src/git.js:103–168,171–194,225–242` 绑定提交、目标、策略、忽略项和上下文；`git-gate.js:111–119` 唤醒后重验凭据。页面没有声称回调重新执行 Git 命令。 |
| 源码外发 | `src/review-workspace.js:197–274` 允许读取未改的相关普通文件，不只是 diff；不跟随软链或子模块。页面说明路径排除不等于内容秘密扫描，并说明云端接收代码、上下文与答案。 |
| 先固定判据 | 固定原文 `src/evaluator.js:24–80,445–473,508–568` 支撑预先固定预测与因果最低标准、独立请求复核和无效题不通关。页面没有把“独立请求”夸成不同模型或独立人类审核。 |
| 隔离边界 | `src/pi-runtime.js:26–34,84–108` 限制内嵌资源；`evaluator.js:219–232,374–408` 清理父会话并设置 CLI 隔离参数。页面明确这些不是同 OS 用户之间的授权边界。 |
| 误判证据 | `eval/fixtures/known-false-negatives.json:47–60,98–111` 保留充分答案被判 ambiguous 的 V18、V20 样例。页面将此用于拒绝能力认证或组织强制发布授权，没有把合成样例当作真实代码安全保证。 |

分类维持 `agent-tooling/supervision-surfaces` 合理。已检查相邻 harness-extensions、agent-governance 与 education-tutoring；它们分别侧重扩展能力、安全治理和通用教学，不是更窄的推送理解检查分类。已读 Plannotator、PR Lens、PR-Agent 页；比较区分人批注、理解导览与自动找问题。未发现遗漏更近的已收录理解考核工具。

## 图源、生成物与验证

图源是真正的两类输入：flow 描述用户与产品的交接；mechanism 描述源码机制和四项技术的映射。双语作者技术项给出问题、做法、边界与源码，生成文字不冒充额外研究证据。

只在内存解析补丁，并调用本索引的纯文本生成函数核对，没有应用补丁或渲染上游程序。机器输出：

```text
harness--harness en/zh: authored_techniques=4; generated_flow=exact; generated_mechanism=exact; mechanism_source_stamp=match; SVG_XML=valid
parthh01--sphinx en/zh: authored_techniques=4; generated_flow=exact; generated_mechanism=exact; mechanism_source_stamp=match; SVG_XML=valid
Harness fixed_tree_blob_checked=6249; mismatches=[]; tree_truncated=False
Sphinx cached_fixed_tree_blob_checked=70; mismatches=5; source_manifest_sha256_mismatches=[]
Sphinx mismatched_files_refetched_at_fixed_SHA=5; remote_blob_matches_tree=5/5
Sphinx bin/sphinx.js remote_blob_matches_tree=True
```

未运行安装器、上游测试、服务、模型或攻击载荷。未做运行态漏洞复现、hook 兼容实测或付费模型重评；这些不是本轮授权的验收项。全库门禁由主会话按原任务逐仓库执行。本审查只新增当前目录的 `new-entry-review.md` 与 `new-entry-review.json`，未修改作者补丁、categories、README 或 ledger。

下一步：主会话按绑定哈希继续逐仓库门禁与交付。
