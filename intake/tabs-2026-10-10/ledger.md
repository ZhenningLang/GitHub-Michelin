# Tab intake ledger — 2026-10-10 (UTC)

来源：用户本人 Chrome 的标签（按进程号定位，不碰自动化实例）。动作 add/sync/skip/propose；结果 pending/running/done/failed/skipped/proposed。
propose = 读过之后判断不适合收录，标签保留，等用户定。

| 规范名 | 动作 | 结果 | 页面路径 | 备注 | 标签里的写法 |
|:---|:---|:---|:---|:---|:---|
| cathrynlavery/diagram-design | add | done | categories/agent-skills/design/visual-artifacts/diagram-design.md |  | cathrynlavery/diagram-design |
| MDX-Tom/gpt-instruct | propose | proposed |  | 核心内容是去除 Codex 安全护栏的系统提示词（v5 明文：[MODE: UNRESTRICTED]，禁止拒绝措辞，点名覆盖 cracking/逆向/越狱），README 建议用日抛账号规避封号；可复用的非载荷部分很薄：codex-instruct.py 只是写 model_instructions_file 的部署器，评测脚本以 .zip 发布、明文源与评测输出留在作者本地。属灰区“活体有害载荷、其余可复用很少”。防御向红队需求已有 garak/promptfoo 收录。 | mdx-tom/gpt-instruct |
| vectorize-io/hindsight | sync | done | categories/agent-memory/app-memory/hindsight.md | fresh: last_verified 2026-09-28, delta 12d ≤ 90, no diff | vectorize-io/hindsight |
| ZhenningLang/cpu-gpu-basic | skip | skipped |  | owner 是 ZhenningLang，标签不动 | zhenninglang/cpu-gpu-basic |
