# 本轮分类溢出规划

推荐移动 16 对页，旧页占 11 对。
新增四个子类，另将两项新页转入已有监督界面类。
本文件记录规划时快照。主会话已接受最小方案，实施另行取证。

主会话裁决：采用单一自然子类、父节点保留直接页。
仓库 schema 明确允许这种混合节点；不为对称结构多搬 34 对页。
保持父分类路径，不刷新事实日期。11 对既有页的旧外部书签不能自动恢复，最终报告须说明。

## 工作清单

- [x] 读取重分类技能与仓库树合同。
- [x] 递归实数，核对 intake 前基线。
- [x] 阅读六个溢出 INDEX、目标 INDEX 与相关页。
- [x] 检查父级路由、双语规则与相对资源路径。
- [x] 输出逐页映射和取舍。
- [x] 校验 JSON、内存模拟与只读边界。
- [ ] 实施迁移：本任务明确跳过，交主会话裁决。
- [ ] 重建 reports、提交与浏览器操作：本任务明确禁止。

宿主没有任务清单工具，本文件承载检查清单。

## 实数与基线

基线提交为 `49cf44bd`。
规划快照为 `57f7c72e96b2fe497cebe31c1d453d16e976a6c5`。
旧页以基线 git tree 是否存在判定，不看事实日期。

| 口径 | 数量 |
| --- | ---: |
| 本轮前的项目页对 | 866 |
| 当前已整合的新页对 | 60 |
| 当前全部项目页对 | 926 |
| 尚未整合的新页目标 | 1 |
| 分类节点 | 191 |
| 真正没有孩子的分类节点 | 164 |
| 无孩子节点中的页对 | 892 |
| 混合父节点中的页对 | 34 |

61 是本轮新增目标，不是当前已落盘数。
OpenTunnel 还未整合，之后需重算。
JSON 保存全部 171 个含直接页节点的计数。

`tools/lint.py:1187` 检查每个节点的直接页数。
父节点有孩子，也不能用来豁免溢出。
因此必须统计混合父节点中的页。

本次实跑 `python3 tools/lint.py`，退出码为零：

```text
191 category nodes, 926 EN + 926 ZH pages, 0 errors, 1550 warnings.
```

其中六条是分类溢出。
其余既有 warning 不在本次治理范围。

## 推荐取舍

| 分类 | 本轮前 | 当前 | 推荐后直接页 | 新孩子页数 |
| --- | ---: | ---: | ---: | ---: |
| video-production | 11 | 15 | 12 | 3 |
| engineering | 12 | 14 | 11 | 3 |
| personal-assistants | 12 | 15 | 11 | 4 |
| terminal-agents | 11 | 13 | 12 | 无 |
| orchestration-and-review | 12 | 13 | 12 | 无 |
| on-device-ml | 10 | 13 | 9 | 4 |
| supervision-surfaces | 8 | 8 | 10 | 无 |

前三类各只提取一个自然孩子。
父节点保留直接页，不改既有父路径。
这三项需要主会话明确接受。

`tools/schema.md:743–746` 允许父节点同时持页和孩子。
技能建议 2–5 个孩子，但也禁止硬凑。
若强制前三类全部下沉，需要移动 50 对页。

| 方案 | 总移动页对 | 旧路径移动页对 |
| --- | ---: | ---: |
| 单一自然孩子，父节点留页 | 16 | 11 |
| 前三类强制拆成两个孩子 | 50 | 37 |

第二方案多动 34 对页，旧页多动 26 对。
推荐第一方案，不把结构对称当作收益。
这不是全局数学最优证明，而是完整自然簇下的低扰动选择。

## 逐页映射与依据

下面均以英文路径表示。
每行必须同时移动同名中文镜像。
项目 slug 不变，不改事实、日期与正文判断。

### 监督界面：只动两项新页

目标目录为 `categories/agent-tooling/supervision-surfaces/`。
目标已有八项；接收后为十项，无需再拆。

| 原路径 | 新路径 | 身份 | 迁移理由 |
| --- | --- | --- | --- |
| `categories/agent-frameworks/coding-agents/orchestration-and-review/agor.md` | `categories/agent-tooling/supervision-surfaces/agor.md` | 新页 | 共享分支板、会话与预览是主入口；人类团队协作决定选型。 |
| `categories/agent-frameworks/coding-agents/terminal-agents/dsh-tui.md` | `categories/agent-tooling/supervision-surfaces/dsh-tui.md` | 新页 | 它投影已有 DSH 状态并展示审批，不替代执行核心。 |

Agor 确有区域触发和执行策略，不能说它“没有编排”。
其页面与 Scion 的决定性区别仍是共享界面。
迁移只改主要导航，不删机制描述。

dsh-TUI 的后端切换会重启到另一会话。
它不是同时监管多个 agent 的终端复用器。
因此不转入 `agent-multiplexers`。

目标叶的范围已按人的查看与决定划分。
但父级 `agent-tooling/INDEX.md` 仍限定非终端入口。
实施时必须同步去掉这一限定，不能暗中塞页。

T3 Code、OpenChamber、OpenHands 均保留原路径。
它们有相邻分类问题，但移动它们超出本次最小范围。
Maka 拥有运行时与持久事件账本，也保持不动。

### 视频：只提取渲染引擎

旧目录为 `categories/video-production/`。
新目录为 `categories/video-production/render-engines/`。
下表文件名在两个目录间一一映射。

| 原页 → 新页 | 身份 | 迁移理由 |
| --- | --- | --- |
| `hyperframes.md` → `render-engines/hyperframes.md` | 旧页 | HTML 合成逐帧渲染；附带技能不改变引擎主价值。 |
| `remotion.md` → `render-engines/remotion.md` | 旧页 | React 参数化视频与云渲染，属于代码视频底层。 |
| `fframes.md` → `render-engines/fframes.md` | 旧页 | Rust/SVG 经 Skia 与 libav 输出视频，与前两项处于同层。 |

新孩子供已有脚本、素材与制作方法的人选择。
父节点保留导演技能、制作管线与成品创作应用。
全部成员见 JSON 的 `parent_retains`。

video-use、SeeCut 编辑现有片段，却提供完整 agent 方法。
它们不是裸渲染引擎，保持父目录。
传统编解码和 NLE 继续走媒体处理类。

不建议把本轮四项新页硬凑成一个子类。
提示包、短剧前期与本地艺术动画不在同一层。
仅按新增时间聚类，会把旧同类留错位置。

### 工程技能：提取科研工作流

旧目录为 `categories/agent-skills/engineering/`。
新目录为 `categories/agent-skills/engineering/scientific-workflows/`。

| 原页 → 新页 | 身份 | 迁移理由 |
| --- | --- | --- |
| `scientific-agent-skills.md` → `scientific-workflows/scientific-agent-skills.md` | 旧页 | 科学库、数据库与领域分析惯例。 |
| `auto-empirical-research-skills.md` → `scientific-workflows/auto-empirical-research-skills.md` | 旧页 | 社会科学识别、估计、稳健性与论文表格。 |
| `nature-skills.md` → `scientific-workflows/nature-skills.md` | 新页 | 论文阅读、公式图表溯源与证据驱动稿件。 |

科研包括实证社会科学，不能只装生命科学。
这三项都是宿主内技能，不是自动研究运行时。
因此不迁往研究自动化类。

父节点保留软件开发、测试、性能与交流习惯。
SwiftUI Pro 仍属于软件工程评审。
不因 Apple 标签迁入端侧 ML。

### 个人助手：提取消息常驻服务

旧目录为 `categories/agent-frameworks/agent-runtimes/personal-assistants/`。
新目录为其下的 `messaging-daemons/`。

| 原页 → 新页 | 身份 | 迁移理由 |
| --- | --- | --- |
| `openclaw.md` → `messaging-daemons/openclaw.md` | 旧页 | 主机 Gateway 常驻，跨消息渠道共享会话。 |
| `hermes-agent.md` → `messaging-daemons/hermes-agent.md` | 旧页 | VPS 长驻、消息入口、计划任务与累积记忆。 |
| `picoclaw.md` → `messaging-daemons/picoclaw.md` | 旧页 | 小板常驻，消息适配器与计划任务是使用入口。 |
| `octop.md` → `messaging-daemons/octop.md` | 旧页 | 自托管多用户消息控制面，一个进程连 IM、CLI 与 cron。 |

四页形成完整自然簇。
不能只为少移一页而把 Octop 留在父节点。
dashboard 或伴随客户端不改变主要使用形态。

父节点保留交互助手，但不硬贴“桌面工作区”标签。
Jarvis 是语音伴侣，OpenMinis 是手机原位工具。
Atomic Agent 是本地模型工作站操作者。

LobsterAI 虽包装 OpenClaw，主价值是桌面会话与产物层。
OpenHuman 主打摄取式记忆，Raven 主打任务图。
这些边界项目都保持原路径。

### 端侧 ML：Apple 优先，不是 Apple 专属

旧目录为 `categories/on-device-ml/`。
新目录为其下的 `apple-local-inference/`。

| 原页 → 新页 | 身份 | 迁移理由 |
| --- | --- | --- |
| `mlx-mlx-lm.md` → `apple-local-inference/mlx-mlx-lm.md` | 旧页 | 主要场景是 M 系列 Mac 上用 MLX/Python 试模型与微调。 |
| `uzu.md` → `apple-local-inference/uzu.md` | 旧页 | 当前 SDK 的硬边界是新 Apple OS 与 Metal 4。 |
| `fluiduse.md` → `apple-local-inference/fluiduse.md` | 新页 | Swift/Core ML 决策模型与真实 Mac 控件集成。 |
| `turbo-fieldfare.md` → `apple-local-inference/turbo-fieldfare.md` | 新页 | Swift/Metal 在小内存 Mac 上流式加载指定 Gemma 专家。 |

MLX 页面明确列有 CUDA/CPU extras。
所以子类按主要使用路径分，不声称平台排他。
本轮 TurboFieldfare 同属此簇，必须一并纳入。

TimesFM 有 MLX 标签，但主价值是时间序列预测。
BitNet 和 LiteRT-LM 能跑 Mac，也不是 Apple 集成路线。
它们均保持父节点。

已有 `local-image-generation/` 完全保留。
父路由先按图像生成任务进入旧孩子。
其余再按 Apple 本地计算栈进入新孩子。

## 父子 INDEX 规则

每个新目录都创建双语 INDEX。
父节点增加子类入口，保留剩余直接页。
父路径与祖父路由不改名。

- 英文路由只链英文页与英文 INDEX。
- 中文路由只链中文页与中文 INDEX。
- 新孩子上行返回 `../INDEX.md` 及对应中文文件。

移走项目的主登记和项目级对比行迁入孩子。
父节点改放子类对比入口，不能重复主登记。
确有跨层比较时，只修路径，不重写判断。

工程父 INDEX 去掉“叶子”描述。
其上层分类行也改为可继续下降的入口。
视频父说明需覆盖制作方法、管线与应用。

监督界面父路由应去掉“非终端”条件。
目标叶说明补足终端、浏览器与桌面载体。
职责仍是人的查看、审批与引导，不扩成所有 agent。

根 INDEX 保留所有现有顶层路由。
新孩子不越级直接挂根。
视频根行如修文案，只同步父节点边界。

## 实施时的机械修补

本节只约束主会话未来操作，本任务未执行。

- 双语页只改 `category` 与必要相对链接目标。
- 日期、健康度、上游元数据与正文判断全部不动。
- 生成文字块保持原字节，不重新研究或重新渲染。

十六个 slug 都唯一，图卡 stem 不变。
资源文件、流程 JSON 与机制 JSON 无需搬迁。
只按新位置修正图片链接。

出链必须先按旧位置解析，再按映射计算新位置。
不能对每个 URL 都机械加一个 `../`。
同迁移簇内部互链常常无需增加深度。

入链扫描须覆盖全库分类页、根路由与双语 README。
双语 README 各保留每个项目的一条主登记。
已有健康列从页面机器同步，不凭手工评分。

链接修补范围会大于十六对移动页。
快照中 OpenClaw 入链涉及 58 个 Markdown 文件。
Hermes 涉及 42 个，Remotion 涉及 38 个。

这些计数含 INDEX 与 README，也含迁移页间互链。
它们不是旧路径移动数，不能混报。
外部书签也无法通过本地链接修补恢复。

未来实施使用 `git mv`，保持历史。
之后重建反向索引，并单独提交重分类。
本规划不运行任何写 reports 的命令。

主会话未来需执行：

```bash
python3 tools/sync_index_health.py --apply
python3 tools/reverse_index.py --write
python3 tools/lint.py
python3 tools/reverse_index.py --check
python3 tools/quality_scan.py --fail-on-gated
```

## Boundary facts

- 父节点可持页，合同依据是 `tools/schema.md:743–746`。
- 告警按直接页数计算，依据是 `tools/lint.py:1187`。
- 监督界面旧父说明偏向非终端，接收 dsh-TUI 必须显式修正。

## Boundary decisions：待主会话裁决

- 接受前三类各只提取一个孩子，避免额外改旧路径。
- 接受监督界面按职责分，不按终端载体分。
- 接受 Apple 子类按主路径分，不写成平台排他。

## 验证结果

规划校验已通过，不能把建议写成已经实施。
当前 lint 是修改前基线，不是迁移后验收。

验收清单覆盖 JSON、真实文件映射与内存模拟。
冻结点是本文件所列快照，修改在建议生成侧。
没有修改门禁代码或分类上限。

- Inner-loop evidence：本次复跑 JSON、全树计数、双语源页与基线身份检查，全部通过。
- Acceptance evidence：本次内存应用全部映射，页数守恒，四簇完整，所有节点不超过上限。
- Holdout / unseen evidence：以真实边界页作替代回归，明确保留项全部通过；不声称有独立盲测。

机器输出的关键行如下：

```text
PASS JSON and complete census: 926 pairs / 171 page-bearing nodes
PASS moves: 16 pairs / 32 files / 11 baseline pairs / 5 intake pairs
PASS simulated tree: 926 pairs conserved / 0 overflows / max direct pages 12
PASS 4 complete child clusters and their parent-retained sets
PASS link-rebasing feasibility: 814 relevant local links / 156 inbound-link files
PASS canonical content snapshot unchanged: 0d01d3d415c24b33779cb5ab8c7077862aa1f1afdb2663d73635b4cecc68950d
```

链接检查只是无写入的重定位可行性验证。
814 是相关链接出现次数，不是实际修改数。
156 是指向迁移页的文件并集。

| 交付物 | 存在 | 实质 | 接通 | 状态 |
| --- | --- | --- | --- | --- |
| JSON 规划 | 文件可解析 | 16 条映射、171 项计数与逐页依据 | 对真实树模拟，核对父子成员与容量 | 已验证 |
| Markdown 规划 | 文件非空 | 边界、取舍、索引和机械修补规则 | 与同名 JSON 使用相同映射与统计 | 已验证 |

git 状态只新增这两份规划文件。
台账修改在本子任务开始前已经存在。
分类页、README 与 reports 没有改动。

Holdout 来源类别：真实捕获。
预期值来源：需求原文与仓库合同。
本次改动相对冻结点的位置：建议生成侧，快照为上述 HEAD。

Known gaps：主会话尚未裁决，OpenTunnel 尚未整合。
未实际搬页，不能声称重构后的 lint 已通过。
只读边界以输出文件白名单与页面快照复核。

下一步由主会话确认边界，再按 JSON 映射实施。
