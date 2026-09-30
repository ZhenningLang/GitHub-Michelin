# Tab intake ledger — 2026-09-30 (UTC)

来源：Chrome 标签（只读用户本人的 Chrome，按进程号定位，不碰自动化实例）。动作 add/sync/skip；结果 pending/done/failed/skipped。本批 worker 用 claude-opus-5-5。

批次约定：对比表里点名但未收录的替代项**不连带新增**（add-project 的 close-the-loop 在本批降级），保持 `未收录` 并在 tradeoff 格写原因。

| 规范名 | 动作 | 结果 | 页面路径 | 备注 | 标签里的写法 |
|:---|:---|:---|:---|:---|:---|
| tursodatabase/turso | add | done | categories/databases/database-engines/turso.md |  | tursodatabase/turso |
| OpenBMB/VoxCPM | add | done | categories/speech/voxcpm.md |  | openbmb/voxcpm |
| superlinked/sie | add | done | categories/llm-inference/serving-engines/sie.md |  | superlinked/sie |
| miqdadbadjuber/anti-slop | add | done | categories/agent-skills/design/ui-taste/anti-slop.md |  | miqdadbadjuber/anti-slop |
| GoogleChrome/modern-web-guidance-src | add | done | categories/agent-skills/vendor-collections/modern-web-guidance.md |  | googlechrome/modern-web-guidance-src |
| openclaw/openclaw-enterprise | add | done | categories/agent-frameworks/kubernetes-agents/openclaw-enterprise.md |  | openclaw/openclaw-enterprise |
| HunxByts/GhostTrack | add | done | categories/osint/ghosttrack.md | 可用于追踪个人位置、无许可证；按用户「安全工具也收」收录，页面须写明法律与隐私风险 | hunxbyts/ghosttrack |
| alphaXiv/OpenResearch | sync | done | categories/agent-frameworks/coding-agents/orchestration-and-review/openresearch.md | 新鲜页，sync-entry 按阈值未重核，无改动 | alphaxiv/openresearch |
| ZhenningLang/cpu-gpu-basic | skip | skipped |  | owner 是 ZhenningLang（按规则跳过，标签不动） | zhenninglang/cpu-gpu-basic |
| yetone/magpie | add | done | categories/api-gateway/magpie-model-router.md | 处理中新开的标签；slug 避开已收录的 Blinue/Magpie | yetone/magpie |
| pingdotgg/t3code | sync | done | categories/agent-frameworks/coding-agents/terminal-agents/t3code.md | 新鲜页，sync-entry 按阈值未重核，无改动 | pingdotgg/t3code |
| cursor/plugins | add | done | categories/agent-skills/vendor-collections/cursor-plugins.md |  | cursor/plugins |
| emilkowalski/skills | sync | done | categories/agent-skills/design/ui-taste/emilkowalski-skills.md | 新鲜页（last_verified 2026-07-16，76 天 < 90），sync-entry 按阈值未重核，无改动 | emilkowalski/skills |
| Gaurav-Gosain/tuios | add | done | categories/agent-frameworks/coding-agents/orchestration-and-review/tuios.md |  | gaurav-gosain/tuios |
| humanlayer/skills | sync | done | categories/agent-skills/vendor-collections/humanlayer-skills.md | 新鲜页（last_verified 2026-09-22，8 天 < 90），sync-entry 按阈值未重核，无改动 | humanlayer/skills |
| kubernetes-sigs/agent-sandbox | add | done | categories/sandboxing/agent-sandbox.md |  | kubernetes-sigs/agent-sandbox |
| llm-d/llm-d | add | done | categories/llm-inference/serving-engines/llm-d.md |  | llm-d/llm-d |
| SemiAnalysisAI/InferenceX | add | running |  |  | semianalysisai/inferencex |
| SimoneAvogadro/android-reverse-engineering-skill | add | failed |  | worker 调研完成（拟归 agent-skills/security），写页时回复被安全分类器拦截，未改写绕过、未产出页面；标签保留，待用户决定 | simoneavogadro/android-reverse-engineering-skill |
| vllm-project/semantic-router | add | done | categories/api-gateway/vllm-semantic-router.md |  | vllm-project/semantic-router |
