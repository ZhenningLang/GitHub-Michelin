# behavior-overlays

> 分类节点。改变 agent 的回复风格、写代码习惯或读入上下文，不接管通用工程流程，也不补领域知识。
> ← 上层 [engineering](../INDEX.zh.md) · 根 [路由](../../../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类合集

| 合集 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **caveman** | 简短表达技能加可选本地代理：压缩 coding agent 说出来的话，wrap 之后也压缩它读进去的东西，代码、命令和报错原样保留。 | D（6/6） | [→](caveman.zh.md) |
| **i-have-adhd** | 一份 10 条规则的回复风格技能：让 coding agent 每轮先说动作、把步骤编号、复述进度，并删掉铺垫与收尾；一套规则覆盖约 15 种 harness。 | A（4/5） | [→](i-have-adhd.zh.md) |
| **Ponytail** | 常驻的「最懒资深工程师」规则集：coding agent 先列出改动要波及的地方，再取阶梯上第一个可行的选项（不做 → 复用 → 标准库 → 已装依赖 → 一行），交回最小但完整的 diff，回复结尾交代跳过了什么；带生命周期 hook、会话启动时的代码地图、review/audit 命令，覆盖约 20 种 harness。 | B（5/6） | [→](ponytail.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [caveman](caveman.zh.md) | ✅ | D（6/6） | token 花销覆盖层：MIT 技能缩短回复；可选 BSL 代理压缩 agent 反复读的日志 / JSON / diff。 |
| [i-have-adhd](i-have-adhd.zh.md) | ✅ | A（4/5） | 给工作记忆短的读者用的表达覆盖层；改变 agent 的说话方式而非它知道什么——痛点是 token 花销时选 caveman。 |
| [Ponytail](ponytail.zh.md) | ✅ | B（5/6） | 压代码那一侧：先复用的阶梯逼出最小完整改动，带强度档位和由模型执行的 review/audit；要压的是话术不是代码，选 caveman / i-have-adhd。 |

## 什么该放这里

叠加在现有 coding-agent 配置上的行为与上下文覆盖层：回复形状、简短表达、先复用的写代码规则，以及可选的读入内容压缩。通用工程流程与软件领域指引留在 [engineering](../INDEX.zh.md)；科研方法走 [scientific-workflows](../scientific-workflows/INDEX.zh.md)。
