# 标签收录验证记录

五项资格问题待维护者裁决；md2wechat 两张健康卡仍有模板文字溢出。本文记录本地验收，远端 CI 与最终被审 SHA 以本批 PR 为准。

## 交付物

| 交付物 | 存在 | 实质内容 | 入口接通 | 状态 |
|---|---|---|---|---|
| 17 个新项目的双语页 | 例如 `categories/desktop-automation/lcu.md:1`；完整清单见 `verification/acceptance.json` | 例如 `lcu.md:82` 的具体场景、`:164` 的宿主自审批边界与固定源码 | `README.md:1166`、分类 `INDEX.md:11`、`reports/repo-page-index.csv:278`；其余逐项由机器核对 | 本地内容验收通过 |
| 34 份图定义、102 张 SVG | 每项目两份 JSON、六张 SVG，全部 XML 可解析 | 有源步骤与技术映射，生成器及结构门禁通过 | 双语页面引用与自动文字版接通 | 结构通过；两张健康卡视觉 partial |
| 6 个 fresh 项目 | 实际打开已有页面 | 未强制重核上游、未改原核验日期 | 单独核对提交；其中 AO 后续仅随分类搬迁 | 事实未刷新 |
| 标签闭环 | 29 条台账均终结 | 17 新增、6 fresh、5 proposed、1 自有 skipped、0 failed | 真实 Chrome 中 done 仍开为零，未匹配新仓库为零 | 本次捕获通过 |
| 分类整理 | 两处各 13 个项目拆成 3／10 | 事实、日期、正文与生成块保真 | 保留父入口、修复内部链接与报表 | 本地通过；旧外部叶页书签不重定向 |
| 总结及阅读版 | `report/summary.md` 为 SSOT，HTML 为派生物 | 分用途取舍、资格存疑、harness 候选及对比选题池 | 本地 companion 和 PR 阅读入口 | HTML 刷新与最终发布记录见 PR |

## 自动验证

- 完整新增内容树的 `make test`：`Ran 483 tests in 34.158s`，`OK`，无 skipped。
- 脱敏公开树再次执行 `make test`：`Ran 483 tests in 32.606s`，`OK`，无 skipped；`make gates` 同为 202 节点、948 对页面、0 errors。
- 最后项目合入后的 `make gates`：`202 category nodes, 948 EN + 948 ZH pages, 0 errors, 1572 warnings.`，退出码零。
- 每个新增项目的双语 scoped quality 均为 `No deterministic findings.`；不是把全仓存量报告项说成清零。
- 反向索引为 `reports are current, no full mislabels`；两处 overflow 均已消除。
- `git diff --check` 已执行，退出码零。
- 验收脚本对真实数据输出：`29 terminal rows`、`17 bilingual pairs`、`34 specs`、`102 parseable SVGs`、`0 done tabs open`、`0 unmatched repository tabs`。

台账和逐页／资产摘要见 `verification/acceptance.json`。原始取证缓存、私有候选身份、凭据与本机路径不随公开材料发布。
每个新增项目抽查一条固定技术源码路径，17／17 读取成功；其中复用本批先前 13 次 HTTP 读取，另补 4 次。只证明这些源路径可达，不冒称每条引文都独立复核，详见 `verification/source-path-sample.json`。
最终阅读版由隔离 worker 重渲染：`wrote intake/tabs-2026-10-21/report/summary.html headings=9 profile=research diagram=code`；`check_companion_set: 0 error(s), 0 warning(s)`；无本机路径、脚本或远端资产，`open` 退出码零。未做 HTML 浏览器截图目检。

## 审查与覆盖

首轮冻结公开树的 manifest 为 320 个文件。四组独立审查原始覆盖为 A 64／64、B 96／96、C 112／112、D 46／48。
主会话没有修改 D 组自报值，而是完整读取并解析两份 README：每份覆盖全部 947 个当时已收录项目，检查新行的许可与健康度、既有行除链接外不变，并调用仓库实际投影函数。
因此父流程账本为 320／320 reviewed，其中主流程补读 2。完整文件账本、原始自报与处置见 `verification/review-audit.json`。

唯一确认 finding 是 md2wechat 的双语健康卡长封顶说明溢出，P2、置信度 10。主会话另读实际 PNG，接受为已披露后续项；未删许可事实、改自动评分或手改 SVG。
最后新增的 gzh-design 与发布文件增量不冒充已在该冻结集合中审过；它们必须在最终实际 HEAD 上再做集成复核，结果留在 PR。

两次分类迁移，主会话分别核对 26 份迁移页／80 个生成块、54 份变更文档／64 个生成块与已验证 worker 输出一致。其他图源、资产、工具和门禁未变。

## 验证证据分层

| 层级 | 结果 | 来源 | 证据 |
|---|---|---|---|
| Inner-loop evidence | pass | 本次复跑 | 工具单测、每项目门禁、双语范围质量、差异检查 |
| Integration evidence | pass | 本次复跑 | 双语入口、自动健康投影、反向索引、图文与 17 项逐页接通 |
| Acceptance evidence | pass | 本次复跑 | 真实 Chrome 标签闭环与 `acceptance.json`；不是空范围扫描 |
| Holdout / unseen evidence | 不适用独立模型效果实验 | 本次复跑及复用 worker 固定源码证据 | 源码中的权限、恢复、许可与未合并修复作为反向边界样本 |
| Known gaps | 已披露 | 机器结果与实际图像 | 未运行上游；两图视觉 partial；五项资格待裁决；外部旧叶页书签失效 |

Holdout 来源类别：真实捕获，以及固定上游源码的边界抽样，不是自造 happy path。
预期值来源：用户需求、`tools/schema.md` 和既有门禁契约；补审没有引入新的严格 YAML 或许可格式要求。
本次改动相对冻结点的位置：仅新增／整理内容生成侧；工具、测试、阈值和判定侧保持本批开始时的版本。

## 被拦命令与存量观察

- 一次补充性的全仓旧路径 grep 被宿主以 `Permission denied: grep` 拒绝，未换写法重试。核心穷举迁移验证与门禁已独立通过；它不冒充已运行的证据。若要追加复跑，需单独授权。
- 一次长 heredoc 被提示 `shfmt AST verification failed`，并明确要求拆简单命令；按提示拆成临时脚本和单独执行，没有修改护栏。
- Ekko Studio 的旧许可列、TanStack Select 的无表头游离行、已有页面正文健康度口径等属于基线问题。本次保留旧行和旧事实，不借补审扩大修复范围。

## 不适用项与回退

不新增运行时、依赖、CI 配置、账户接入或数据迁移，所以代码可观测性与产品交互 UI 验证不适用。静态图卡的视觉缺口已单列，不能据此声称所有图都通过视觉验收。
未安装或执行上游，未调收费 API、读取业务凭据、创建文章草稿、跑安卓真机、Unity 或 GPU 推理；这些均不记为 pass。
内容事实或路由回归时，按项目／分类独立提交提出 revert PR，不强推或覆盖并发工作。主 checkout 不同步。
