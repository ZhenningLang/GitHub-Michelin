# 批量子任务合同

这是用户已指定的 intake-tabs 文档收录路线，不是开发代码需求。
你只修改自己分配的独立 worktree，绝对路径由派发 prompt 指定。
其他分支和主工作区不归你所有，不允许写入。

## 先读

完整读取自己 worktree 的 `AGENTS.md`、`tools/schema.md`、
`.claude/skills/add-project/SKILL.md`、`.claude/skills/sync-entry/SKILL.md`、
`.claude/skills/read-repo/SKILL.md`、`.claude/skills/intake-tabs/worker-brief.md`。
按用户指定的 intake-tabs 路线，不必另问开发路线。

## 分组

主账本的绝对路径：
`intake/tabs-2026-10-18/ledger.md (public redacted projection; original ledger remains local-only)`。
读取它，只读，不修改。过滤 `结果=pending` 或 `running` 的原始 80 项；
按账本原序，从零计数，属于你的 group 的条件是 `index % 8 == group - 1`。
用户说明的 group 清单优先；不要因主账本后续变为 done 而改变已分配清单。
全部账本仓库都是本批兄弟，不能在对比表里把本批兄弟标为未收录。
如尚无页面，在正文中比较兄弟，而表格选择其他已收录替代品。

## 每个仓库

逐仓库完整执行 add-project 或 sync-entry，UTC 日期 2026-10-18。
sync-entry 必须先走其日期与 upstream 门控，fresh 可无改动。
read-repo 不是只看 README：读依赖、LICENSE 实文、相关源文件、真实使用路径、健康信号。
worth check 五项需命令证据；只有窄范围不适合才 propose，保留具体证据。
禁止安装和执行上游代码、技能、hook 或远程安装脚本；只读上游内容。
不要改任何 dotfiles。不要使用其他模型或启动其他 agent。
比较替代品的闭环收录关闭；非本批的真实未收录替代品在取舍栏说明本次未收录。
无剩余 Q&A 时不加章节，结果记录 `no leftover Q&A`。
完整生成 flow、mechanism、upstream、health、索引投影与 reverse_index；
机制图要求本机 d2，图文不得手改生成块。每个仓库都跑 `make gates`。
分类 fanout 警告只报告，不自行重构。不要为了消警告迁移无关页面。
两次真实修复仍不通过则报告 failed，继续其他仓库，不扩大修改。

## 交付补丁，恢复你自己的工作

每仓库成功时，把机器生成的完整 diff 保存为单独补丁；不能等所有仓库结束才交一个补丁。
结果目录是自己 worktree 的相邻目录 `<worktree>-results`，允许写入，其他位置禁止写。
文件 stem 用小写 owner--repo；结果目录不要放在 worktree 内，避免混入补丁。

保存步骤：

```text
git add -A
git diff --cached --binary --full-index HEAD -- . ':(exclude)reports' > <results>/<stem>.patch
git diff --cached --binary --full-index HEAD > <results>/<stem>.rollback.patch
```

结果 JSON 应包含 repo、status（done/fresh/failed/propose）、category_path、gates 关键输出、
sources（已读文件的固定 commit 链接）、worth_check、fanout_warn、notes_zh、qa_decision，
以及 dotfiles_zh（fit=none/low/medium/high，what，where）。
失败或 propose 也要写 JSON；禁止谎称门禁成功。
所有文件读写都必须用绝对路径或在显式 workdir 中完成。
机器输出可用 shell 保存；编写选型页用编辑工具，不要写批量通用文案生成器。

保存并检查补丁和 JSON 后，用 `git apply --reverse --index <rollback.patch>`
仅撤销自己刚才创建的修改；它不含用户文件，因为此 worktree 是分配给你的干净副本。
检查 `git status --short` 为空，然后处理下个仓库。
禁止 git reset、checkout、commit、push、修改主账本或操作 Chrome。
只允许逆向应用自己这一仓库的精确补丁，不删除任何不在该补丁里的文件。
fresh 且无变更直接写 JSON，不必创建空补丁。

## 汇报

所有命令都前台等待完成。最后只返回结果目录、各 repo 状态、
关键门禁输出、值得主会话复核的问题。不要回传整篇页面或补丁。
