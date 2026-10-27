# Tab intake ledger — 2026-10-27 (UTC)

来源：用户本人 Chrome 的标签（按进程号定位，不碰自动化实例）。动作 add/sync/skip/propose；结果 pending/running/done/failed/skipped/proposed。
propose = 读过之后判断不适合收录，标签保留，等用户定。

| 规范名 | 动作 | 结果 | 页面路径 | 备注 | 标签里的写法 |
|:---|:---|:---|:---|:---|:---|
| alchaincyf/huashu-design | sync | done | categories/agent-skills/design/visual-artifacts/huashu-design.md | 固定4fc7bfdb完整源码重核并迁移v2；8份新旧来源blob经固定API树认证，第三方提示词权利仍存疑；no leftover Q&A | alchaincyf/huashu-design |
| anthropics/sandbox-runtime | add | done | categories/sandboxing/sandbox-runtime.md | 固定98a4016d；11份源码blob树认证，32处引用与2命令原样核验；默认允许读取及平台降级已披露，综合A非安全认证；no leftover Q&A | anthropics/sandbox-runtime |
| browseros-ai/BrowserOS | add | done | categories/web-automation/agent-browser-tools/browseros.md | 固定6967b953；44源码blob树认证、52引用与3命令核验；独立审稿修正Rust最低支持版本，许可分区及浏览器权限边界保留；no leftover Q&A | browseros-ai/browseros |
| designfuchen/word-atlas | add | done | categories/education-tutoring/word-atlas.md | 固定99c00767；23份blob固定树认证，22处引用和1命令原样核验；MIT代码与CC BY内容分开，备份缓存及导出破坏性边界保留；no leftover Q&A | designfuchen/word-atlas |
| google/elephant-goldfish-model | add | done | categories/agent-dev-methodology/spec-driven-development/elephant-goldfish-model.md | 固定b3a35956；18份blob固定树认证，52引用和4命令原样核验；独立内容审无问题，设计批准不等于实施授权；no leftover Q&A | google/elephant-goldfish-model |
| Infini-AI-Lab/hermit | add | done | categories/agent-frameworks/workflow-builders/hermit.md | 固定6957141d；49源码blob树认证、22引用与1命令核验；独立审稿修正可用轨迹条件，结构检查不保证涨分，MWM旧源权属仍存疑；no leftover Q&A | infini-ai-lab/hermit |
| kelvinkn17/skills | add | done | categories/agent-skills/visual-content/fun-isometric.md | 固定7c8a7526；13blob树认证、26处引用及3命令核验；独立内容审无问题，ZIP缺根MIT及单日历史已披露；no leftover Q&A | kelvinkn17/skills |
| microsoft/pylance-release | propose | proposed |  | README:5明确Pylance主体闭源，本仓为文档与反馈，另含协议及测试样例；CC-BY-4.0不等于扩展开源。官方指向microsoft/pyright；暂不扩收，标签保留。固定f03a84d9，no leftover Q&A | microsoft/pylance-release |
| nightly-labs/openbot | propose | proposed |  | 当前固定d71a4eb9明确为PolyForm Noncommercial源码可见版本，商业用途需另获许可；非缺失或伪造许可，旧Apache不覆盖新版本。准入留维护者裁决，标签保留；no leftover Q&A | nightly-labs/openbot |
| open-webui/open-webui | sync | done | categories/llm-chat-ui/open-webui.md | Fresh delta=19<=90；沿用2026-10-08原核验日期，未重读上游、未改双语页；no leftover Q&A | open-webui/open-webui |
| shcherbak-ai/contextgem | add | done | categories/document-parsing/contextgem.md | 固定90974fbb；19blob真实根树认证、48引用与3命令核验；独立审稿无问题，引用有效不等于答案正确，序列化非持久队列；no leftover Q&A | shcherbak-ai/contextgem |
| t3dotgg/tstack | add | done | categories/agent-skills/personal-collections/engineering-workflows/tstack.md | 固定92e38e2c；16blob真实根树认证、42引用与2命令核验；独立审稿补测试授权范围，机器人finished不是批准、full-stop不是只读；no leftover Q&A | t3dotgg/tstack |
| tractordev/webframe | add | done | categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/webframe.md | 固定03155e2b；29本体+7依赖blob两提交真实根树认证；独立审稿修复版本化go install与replace冲突，未执行构建，系统引擎及持久数据边界保留；no leftover Q&A | tractordev/webframe |
| unclebob/ub-mode | propose | proposed |  | 固定57a8bdd2完整树仅两文件，无明确复用许可；README承认规则来源但授权链未核清。技能有复用实质，非因纯提示或年轻拒收，标签保留；no leftover Q&A | unclebob/ub-mode |
| Vxtzq/CrowdGPT | add | done | categories/llm-training/crowdgpt.md | 固定02774d98；11blob真实根树认证、26引用与2字面量；独立审稿反例已修，同组仅尽力、本地进度非远端ETA，GPL评分桶保持现合同；no leftover Q&A | vxtzq/crowdgpt |
| wailsapp/wails | add | done | categories/dev-utilities/editors-and-runtimes/runtimes-and-compilers/wails.md | 固定3b1e7926；34blob真实根树认证、61引用与3字面量；独立审稿无问题，另核v3.0.0真实发布及31相同/3差异，Tauri旧判断和日期未重核；no leftover Q&A | wailsapp/wails |
| anonymous-own-1 | skip | skipped |  | 自有仓库，按范围跳过；标签保留 |  |
| blendi-remade/dioramas | add | done | categories/frontend-animation/dioramas.md | 固定868539fb；29blob真实根树认证、42引用与1字面量；独立审稿无问题，Three.js网站框架非skill，代码MIT/素材CC BY分开，unknown两轴保留；no leftover Q&A | blendi-remade/dioramas |
