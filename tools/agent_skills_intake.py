#!/usr/bin/env python3
"""Build an auditable intake report for agent-skills backlog URLs."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TODAY = dt.date.today().isoformat()

DEFAULT_URLS = [
    "https://github.com/slavingia/skills",
    "https://github.com/freestylefly/canghe-skills",
    "https://github.com/op7418/guizang-ppt-skill",
    "https://github.com/alchaincyf/huashu-skills",
    "https://github.com/virgiliojr94/book-to-skill",
    "https://github.com/OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL",
    "https://github.com/hello-simpleai/chatgpt-comparison-detection",
    "https://github.com/dongbeixiaohuo/writing-agent",
    "https://github.com/alchaincyf/nuwa-skill",
    "https://github.com/MrGeDiao/shuorenhua",
    "https://github.com/hylarucoder/ai-flavor-remover",
    "https://github.com/Leonxlnx/taste-skill",
    "https://github.com/hardikpandya/stop-slop",
    "https://github.com/op7418/Humanizer-zh",
    "https://github.com/blader/humanizer",
    "https://github.com/cbailes/awesome-deep-trading",
    "https://github.com/OpenBB-finance/OpenBB",
    "https://github.com/AI4Finance-Foundation/FinRL",
    "https://github.com/microsoft/qlib",
    "https://github.com/mementum/backtrader",
    "https://github.com/ranaroussi/yfinance",
    "https://github.com/kangarooking/cangjie-skill",
    "https://github.com/KKKKhazix/khazix-skills",
    "https://github.com/tt-a1i/archify",
    "https://github.com/mattpocock/skills",
    "https://github.com/browser-act/skills",
    "https://github.com/JuliusBrussee/caveman",
    "https://github.com/every-app/open-seo",
    "https://github.com/JCodesMore/ai-website-cloner-template",
    "https://github.com/alchaincyf/huashu-design",
    "https://github.com/JimLiu/baoyu-skills/tree/main/skills/baoyu-slide-deck",
    "https://github.com/hugohe3/ppt-master",
    "https://github.com/zarazhangrui/frontend-slides",
    "https://github.com/lewislulu/html-ppt-skill",
    "https://github.com/op7418/guizang-ppt-skill",
    "https://github.com/bradautomates/claude-video",
    "https://github.com/HKUDS/DeepTutor",
    "https://github.com/blockpanda/any2html",
    "https://github.com/xiaohuailabs/tacit-mining",
    "https://github.com/aeonfun/soul.md",
    "https://github.com/coreyhaines31/marketingskills",
    "https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering",
    "https://github.com/microsoft/agent-governance-toolkit",
]

CATEGORY_HINTS = {
    "slides-ppt": ["ppt", "slide", "deck", "presentation", "slides"],
    "writing": ["write", "writing", "humanizer", "ai-flavor", "shuorenhua", "huashu", "writer"],
    "design": ["design", "taste", "website-cloner", "archify", "seo"],
    "context-engineering": ["context-engineering", "tacit", "soul"],
    "engineering": ["skills", "cangjie", "canghe", "caveman"],
    "investment-finance": ["trading", "finance", "finrl", "qlib", "backtrader", "yfinance", "openbb"],
    "education-tutoring": ["tutor", "deeptutor"],
    "governance": ["governance"],
    "video-production": ["video"],
    "document-parsing": ["any2html"],
}

CATEGORY_OVERRIDES = {
    "hello-simpleai/chatgpt-comparison-detection": "llm-eval",
    "alchaincyf/nuwa-skill": "context-engineering",
    "hardikpandya/stop-slop": "de-ai-writing",
    "blader/humanizer": "de-ai-writing",
    "hylarucoder/ai-flavor-remover": "de-ai-writing",
    "mrgediao/shuorenhua": "de-ai-writing",
    "oubigfa/de-ai-prompt-enhancer-writer-booster-skill": "de-ai-writing",
    "alchaincyf/huashu-design": "design",
    "mattpocock/skills": "personal-collections",
    "slavingia/skills": "personal-collections",
    "freestylefly/canghe-skills": "personal-collections",
    "kangarooking/cangjie-skill": "context-engineering",
    "browser-act/skills": "engineering",
    "coreyhaines31/marketingskills": "writing",
    "microsoft/agent-governance-toolkit": "agent-governance",
}

TOP_CATEGORY_INFO = {
    "investment-finance": {
        "en": "Quant finance, market-data, trading research, and investment-analysis tooling.",
        "zh": "量化金融、市场数据、交易研究与投资分析工具。",
    },
    "education-tutoring": {
        "en": "AI tutoring, learning assistants, and education-focused agent systems.",
        "zh": "AI 辅导、学习助手与教育场景 agent 系统。",
    },
    "agent-governance": {
        "en": "Governance, policy enforcement, identity, sandboxing, and reliability controls for AI agents.",
        "zh": "AI agent 的治理、策略执行、身份、沙箱与可靠性控制。",
    },
}

AGENT_SKILL_LEAVES = {
    "de-ai-writing",
    "writing",
    "design",
    "slides-ppt",
    "visual-content",
    "context-engineering",
    "engineering",
    "personal-collections",
    "security",
    "vendor-collections",
    "subagent-collections",
}

LEAF_INFO = {
    "de-ai-writing": {
        "en": "Humanizing AI text, removing AI tells, and enforcing human-sounding prose.",
        "zh": "去 AI 味、消除机器腔、让文本更像真人写作。",
    },
}


def repo_key(url: str) -> tuple[str, str, str | None]:
    m = re.search(r"github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        raise ValueError(f"not a GitHub URL: {url}")
    repo = f"{m.group(1)}/{m.group(2).removesuffix('.git')}"
    path_m = re.search(r"github\.com/[^/]+/[^/]+/(?:tree|blob)/[^/]+/(.+)$", url)
    subpath = path_m.group(1) if path_m else None
    return repo.lower(), repo, subpath


def gh_repo(repo: str) -> dict:
    fields = "nameWithOwner,name,description,stargazerCount,forkCount,primaryLanguage,licenseInfo,isArchived,isFork,createdAt,pushedAt,defaultBranchRef,url,repositoryTopics"
    raw = subprocess.check_output(
        ["gh", "repo", "view", repo, "--json", fields],
        cwd=ROOT,
        text=True,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    data = json.loads(raw)
    topics = data.get("repositoryTopics", []) or []
    data["topics"] = [t.get("name", "") for t in topics if t.get("name")]
    lang = data.get("primaryLanguage") or {}
    data["language"] = lang.get("name") or ""
    lic = data.get("licenseInfo") or {}
    data["license"] = lic.get("spdxId") or "NOASSERTION"
    return data


def gh_branch_sha(repo: str, branch: str) -> str:
    raw = subprocess.check_output(
        ["gh", "api", f"repos/{repo}/branches/{branch}"],
        cwd=ROOT,
        text=True,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    return json.loads(raw)["commit"]["sha"]


def gh_default_branch(repo: str) -> str:
    raw = subprocess.check_output(
        ["gh", "api", f"repos/{repo}"],
        cwd=ROOT,
        text=True,
        stderr=subprocess.STDOUT,
        timeout=30,
    )
    return json.loads(raw).get("default_branch") or "main"


def esc(value: object) -> str:
    return str(value or "").replace("|", "\\|").replace("\n", " ").strip()


def rel_health(page_dir: Path, slug: str, zh: bool) -> str:
    card = f"{slug}.zh.svg" if zh else f"{slug}.svg"
    return os.path.relpath(ROOT / "assets" / "health" / card, start=page_dir)


def frontmatter(item: dict, sha: str) -> str:
    gh = item["github"]
    tags = [item["suggested_category"], slugify(item["repo"]), item["type"]]
    if item["type"] == "skill-pack":
        tags.insert(0, "agent-skill")
    tags = [] if not tags else list(dict.fromkeys(re.sub(r"[^a-z0-9_-]+", "-", t.lower()).strip("-") for t in tags if t))
    return f"""---
name: {display_name(item)}
slug: {item['slug']}
repo: {item['github'].get('url') or 'https://github.com/' + item['repo']}
category: {Path(item['category_path']).name}
tags: [{', '.join(tags[:8])}]
language: {gh.get('language') or 'Unknown'}
license: {gh.get('license') or 'NOASSERTION'}
maturity: active, ~{gh.get('stars', 0):,} stars (as of 2026-07)
last_verified: {TODAY}
type: {item['type']}
upstream:
  pushed_at: {gh.get('pushed_at')}
  default_branch: {item.get('default_branch') or 'main'}
  default_branch_sha: {sha}
  archived: {str(bool(gh.get('archived'))).lower()}
---
"""


def display_name(item: dict) -> str:
    return item["repo"].split("/", 1)[1]


def card_line(item: dict, zh: bool) -> str:
    label = "健康度雷达" if zh else "health radar"
    page_dir = ROOT / item["category_path"]
    return f"![{item['slug']} — {label}]({rel_health(page_dir, item['slug'], zh)})"


def comparison_en(item: dict) -> str:
    cat = item["suggested_category"]
    rows = ["| Alternative | In index | Our verdict | Tradeoff |", "|---|---|---|---|"]
    if cat == "de-ai-writing":
        rows += [
            "| [Humanizer-zh](humanizer-zh.md) | ✅ | Choose Humanizer-zh for Chinese-first AI-writing cleanup with an already indexed rubric; choose this page when its upstream language, examples, or workflow fit better. | Humanizer-zh is the current in-index baseline; this new entry broadens the comparison set but needs deeper semantic review. |",
            "| Hand-written voice guide | 未收录 | Choose a project-specific voice guide when one author or brand voice matters more than a reusable public skill. | A private guide fits one voice better; a public skill is easier to install and compare. |",
        ]
    elif cat == "slides-ppt":
        rows += [
            "| [Guizang PPT Skill](guizang-ppt.md) | ✅ | Choose Guizang PPT when a constrained single-file HTML deck with strong art direction is acceptable; choose this page when editable PowerPoint or a different deck workflow is the key constraint. | Guizang is opinionated and already reviewed; this entry expands the deck-skill surface but needs deeper review. |",
            "| [HTML Anything](../../ai-design-generation/html-anything.md) | ✅ | Choose HTML Anything for broad Markdown-to-HTML artifacts; choose a slide-specific skill when the whole job is a presentation deck. | Broader artifact coverage vs narrower deck-specific constraints. |",
        ]
    elif cat in AGENT_SKILL_LEAVES:
        rows += [
            "| Existing skills in this leaf | ✅ | Prefer a more deeply reviewed in-index page when it already names your exact task and constraints. | This page is first-pass intake; existing pages may have sharper when-not guidance. |",
            "| Custom SKILL.md | 未收录 | Write a custom skill when the task is narrow, private, or tightly bound to one repository's conventions. | Custom skills fit local context better but lose upstream maintenance and community examples. |",
        ]
    else:
        rows += [
            "| Existing projects in this category | ✅ | Prefer a mature in-index page when it covers the same job with clearer dependencies and when-not guidance. | This page adds a backlog candidate; existing pages may be safer until deeper review is complete. |",
            "| Custom implementation | 未收录 | Build custom only when the needed scope is tiny and ongoing maintenance is cheaper than adopting a repo. | Avoids dependency risk but loses upstream fixes, docs, and ecosystem signals. |",
        ]
    return "\n".join(rows)


def comparison_zh(item: dict) -> str:
    cat = item["suggested_category"]
    rows = ["| 替代品 | 是否收录 | 我们的评价 | 取舍 |", "|---|---|---|---|"]
    if cat == "de-ai-writing":
        rows += [
            "| [Humanizer-zh](humanizer-zh.zh.md) | ✅ | 需要中文优先、已收录的去 AI 味基线时选 Humanizer-zh；当本页上游的语言、示例或流程更贴近任务时再选本页项目。 | Humanizer-zh 是当前索引基线；本页扩展对比集合，但仍需要更深语义复核。 |",
            "| 自写 voice guide | 未收录 | 当单个作者或品牌 voice 比可复用公共 skill 更重要时，自写项目内 voice guide。 | 私有 guide 更贴合一个 voice；公共 skill 更容易安装和横向比较。 |",
        ]
    elif cat == "slides-ppt":
        rows += [
            "| [Guizang PPT Skill](guizang-ppt.zh.md) | ✅ | 能接受强审美约束的单文件 HTML deck 时选 Guizang PPT；当可编辑 PowerPoint 或另一种 deck 流程是硬约束时再选本页项目。 | Guizang 更有主张且已审过；本页扩展 deck skill 选择面，但仍需更深复核。 |",
            "| [HTML Anything](../../ai-design-generation/html-anything.zh.md) | ✅ | 需要宽口径 Markdown 到 HTML 产物时选 HTML Anything；整个任务都是演示文稿时选专门的 slide skill。 | 更宽的产物覆盖 vs 更窄的 deck 专用约束。 |",
        ]
    elif cat in AGENT_SKILL_LEAVES:
        rows += [
            "| 本叶子已收录技能 | ✅ | 如果已有更深审过的页面已经点名你的任务和约束，优先选它。 | 本页是首版 intake；已有页面的“何时不用”可能更锋利。 |",
            "| 自写 SKILL.md | 未收录 | 当任务很窄、私有或强绑定某个仓库约定时，自写 skill。 | 自写更贴本地上下文，但失去上游维护和社区示例。 |",
        ]
    else:
        rows += [
            "| 本分类已收录项目 | ✅ | 如果成熟页面覆盖同一任务且依赖与不用场景更清楚，优先选现有页面。 | 本页补入 backlog 候选；深审完成前，现有页面可能更安全。 |",
            "| 自写实现 | 未收录 | 只有范围很小、长期维护成本低于引入仓库时才自写。 | 少一个依赖，但失去上游修复、文档和生态信号。 |",
        ]
    return "\n".join(rows)


def page_en(item: dict, sha: str) -> str:
    gh = item["github"]
    name = display_name(item)
    desc = esc(gh.get("description")) or f"An open-source repository for the {item['suggested_category']} area."
    is_skill = item["type"] == "skill-pack"
    extra_sections = "" if is_skill else f"""

## Tech stack

- **Primary language:** {gh.get('language') or 'Unknown'} per GitHub metadata.
- **Repository shape:** `{item['repo']}`; this first-pass page has not exhaustively read every dependency manifest.
- **Default branch snapshot:** last pushed `{gh.get('pushed_at')}`; archived `{str(bool(gh.get('archived'))).lower()}`.

## Dependencies

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## Ops difficulty

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## When to use

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## When NOT to use

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## Comparison

{comparison_en(item)}
{extra_sections}

## Health & viability

- **Maintenance snapshot ({TODAY}):** GitHub reports `archived={str(bool(gh.get('archived'))).lower()}` and `pushed_at={gh.get('pushed_at')}`.
- **Adoption snapshot:** ~{gh.get('stars') or 0:,} GitHub stars as of 2026-07; this is a noisy signal and low-star projects are still included when the repository is real and relevant.
- **License snapshot:** `{gh.get('license') or 'NOASSERTION'}` from GitHub metadata; manual license-file review remains required when license matters.
- **Lindy / governance:** not fully reviewed in this intake pass. Check age, owner type, contributor concentration, releases, and issue response before long-term adoption.
- **Risk flags:** first-pass page generated from the 2026-07-16 backlog; semantic comparison and dependency review are intentionally conservative.

## Caveats (unverified)

- [未验证] This page is generated from public GitHub metadata plus the user-provided intake list; upstream README, docs, examples, releases, and dependency manifests still need deeper review.
- [未验证] License, install commands, supported harnesses, and runtime requirements may differ from GitHub metadata; verify them in the repository before use.
- [推断] The comparison table starts from nearby atlas categories rather than a complete substitute survey; refine it after reading the full upstream project and adjacent alternatives.
""".lstrip()


def page_zh(item: dict, sha: str) -> str:
    gh = item["github"]
    name = display_name(item)
    desc = esc(gh.get("description")) or f"一个面向 `{item['suggested_category']}` 方向的开源仓库。"
    is_skill = item["type"] == "skill-pack"
    extra_sections = "" if is_skill else f"""

## 技术栈

- **主要语言：** GitHub 元数据返回为 {gh.get('language') or 'Unknown'}。
- **仓库形态：** `{item['repo']}`；本首版页面尚未穷尽读取所有依赖清单。
- **默认分支快照：** 最后 push `{gh.get('pushed_at')}`，archived 为 `{str(bool(gh.get('archived'))).lower()}`。

## 依赖

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 运维难度

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 何时使用

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 何时不用

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 横向对比

{comparison_zh(item)}
{extra_sections}

## 健康度与可持续性

- **维护快照（{TODAY}）：** GitHub 返回 `archived={str(bool(gh.get('archived'))).lower()}`，`pushed_at={gh.get('pushed_at')}`。
- **采用快照：** 2026-07 约 {gh.get('stars') or 0:,} 个 GitHub stars；这是有噪声的信号，低 star 项目只要是真实且相关，也会被纳入。
- **许可证快照：** GitHub 元数据返回 `{gh.get('license') or 'NOASSERTION'}`；许可证关键时仍需人工核验许可证文件。
- **Lindy / 治理：** 本次 intake 未完整复核。长期采用前，请继续检查项目年龄、owner 类型、贡献者集中度、release 和 issue 响应。
- **风险信号：** 本页来自 2026-07-16 backlog 的首版生成；语义对比和依赖复核刻意保守。

## 存疑（未验证）

- [未验证] 本页依据公开 GitHub 元数据和用户提供的 intake 清单生成；上游 README、文档、示例、release 和依赖清单仍需深度复核。
- [未验证] 许可证、安装命令、支持的 harness 和运行时要求可能与 GitHub 元数据不同；使用前请在仓库中核验。
- [推断] 横向对比表先从邻近 atlas 分类出发，并不是完整替代品综述；读完上游项目和相邻方案后应继续细化。
""".lstrip()


def health_text(item: dict) -> str:
    return "? (0/6)"


def health_text_zh(item: dict) -> str:
    return "?（0/6）"


def ensure_category_indexes(cat_dir: Path, cat: str) -> None:
    en = cat_dir / "INDEX.md"
    zh = cat_dir / "INDEX.zh.md"
    if en.exists() and zh.exists():
        return
    cat_dir.mkdir(parents=True, exist_ok=True)
    info = TOP_CATEGORY_INFO.get(cat) or LEAF_INFO.get(cat) or {
        "en": f"Projects and tools for {cat}.",
        "zh": f"{cat} 方向的项目和工具。",
    }
    if not en.exists():
        back = "../../INDEX.md" if cat_dir.parent.name == "categories" else "../../../INDEX.md"
        parent = "category route" if cat_dir.parent.name == "categories" else "agent-skills"
        en.write_text(f"""# {cat}

> Category node. {info['en']}
> ← back to [{parent}]({back}) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |

## What belongs here

{info['en']}
""", encoding="utf-8")
    if not zh.exists():
        back = "../../INDEX.zh.md" if cat_dir.parent.name == "categories" else "../../../INDEX.zh.md"
        parent = "分类路由" if cat_dir.parent.name == "categories" else "agent-skills"
        zh.write_text(f"""# {cat}

> 分类节点。{info['zh']}
> ← 返回[{parent}]({back}) · English：[INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |

## 什么该放这里

{info['zh']}
""", encoding="utf-8")


def insert_before(text: str, marker: str, row: str) -> str:
    if row in text:
        return text
    idx = text.find(marker)
    if idx == -1:
        return text.rstrip() + "\n" + row + "\n"
    return text[:idx].rstrip() + "\n" + row + "\n\n" + text[idx:]


def update_category_index(item: dict) -> None:
    cat_dir = ROOT / item["category_path"]
    name = display_name(item)
    desc = esc(item["github"].get("description")) or f"Use it when you need {name} in this category."
    en_row = f"| **{name}** | {desc} | {health_text(item)} | [→]({item['slug']}.md) |"
    zh_row = f"| **{name}** | {desc} | {health_text_zh(item)} | [→]({item['slug']}.zh.md) |"
    en_cmp = f"| [{name}]({item['slug']}.md) | ✅ | {health_text(item)} | {desc} |"
    zh_cmp = f"| [{name}]({item['slug']}.zh.md) | ✅ | {health_text_zh(item)} | {desc} |"
    en = cat_dir / "INDEX.md"
    zh = cat_dir / "INDEX.zh.md"
    s = en.read_text(encoding="utf-8")
    s = insert_before(s, "\n## Comparison", en_row)
    s = insert_before(s, "\n## What belongs here", en_cmp)
    en.write_text(s, encoding="utf-8")
    s = zh.read_text(encoding="utf-8")
    s = insert_before(s, "\n## 对比", zh_row)
    s = insert_before(s, "\n## 什么该放这里", zh_cmp)
    zh.write_text(s, encoding="utf-8")


def update_root_indexes_for_top(cat: str) -> None:
    if cat in AGENT_SKILL_LEAVES or cat not in TOP_CATEGORY_INFO:
        return
    info = TOP_CATEGORY_INFO[cat]
    row = f"| **{cat}** | {info['en']} | [→](categories/{cat}/INDEX.md) |"
    zh_row = f"| **{cat}** | {info['zh']} | [→](categories/{cat}/INDEX.zh.md) |"
    for path, line in ((ROOT / "INDEX.md", row), (ROOT / "INDEX.zh.md", zh_row)):
        s = path.read_text(encoding="utf-8")
        if f"categories/{cat}/INDEX" in s:
            continue
        marker = "\n## How to add a category" if path.name == "INDEX.md" else "\n## 如何新增分类"
        s = insert_before(s, marker, line)
        path.write_text(s, encoding="utf-8")


def update_agent_skills_parent(cat: str) -> None:
    if cat not in LEAF_INFO:
        return
    info = LEAF_INFO[cat]
    row = f"| **{cat}** | {info['en']} | [→]({cat}/INDEX.md) |"
    zh_row = f"| **{cat}** | {info['zh']} | [→]({cat}/INDEX.zh.md) |"
    for path, line in ((ROOT / "categories/agent-skills/INDEX.md", row), (ROOT / "categories/agent-skills/INDEX.zh.md", zh_row)):
        s = path.read_text(encoding="utf-8")
        if f"{cat}/INDEX" in s:
            continue
        marker = "\n## Projects in this category" if path.name == "INDEX.md" else "\n## 本分类项目"
        s = insert_before(s, marker, line)
        path.write_text(s, encoding="utf-8")


def update_readme(item: dict) -> None:
    top = Path(item["category_path"]).relative_to("categories").parts[0]
    name = display_name(item)
    gh = item["github"]
    desc = esc(gh.get("description")) or f"Use it when you need {name} in the {top} area."
    en_page = f"{item['category_path']}/{item['slug']}.md"
    zh_page = f"{item['category_path']}/{item['slug']}.zh.md"
    en_row = f"| **{name}** | {desc} | {gh.get('license') or 'NOASSERTION'} | {health_text(item)} | [EN]({en_page}) · [中]({zh_page}) |"
    zh_row = f"| **{name}** | {desc} | {gh.get('license') or 'NOASSERTION'} | {health_text_zh(item)} | [中]({zh_page}) · [EN]({en_page}) |"
    for path, row in ((ROOT / "README.md", en_row), (ROOT / "README.zh.md", zh_row)):
        s = path.read_text(encoding="utf-8")
        if en_page in s or zh_page in s:
            continue
        heading = f"### {top}"
        idx = s.find(heading)
        if idx == -1:
            s = s.rstrip() + f"\n\n{heading}\n\n| Project | Use when | License | Health | Page |\n| --- | --- | --- | --- | --- |\n{row}\n"
        else:
            nxt = s.find("\n### ", idx + len(heading))
            if nxt == -1:
                nxt = len(s)
            s = s[:nxt].rstrip() + "\n" + row + "\n" + s[nxt:]
        path.write_text(s, encoding="utf-8")


def read_urls(path: str | None = None, use_stdin: bool = False) -> list[str]:
    if path and use_stdin:
        raise ValueError("choose either --input-file or --stdin, not both")
    if use_stdin:
        raw = sys.stdin.read()
    elif path:
        raw = Path(path).read_text(encoding="utf-8")
    else:
        return list(DEFAULT_URLS)
    urls: list[str] = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.search(r"https://github\.com/\S+", line)
        if m:
            urls.append(m.group(0).rstrip(").,;"))
    if not urls:
        raise ValueError("no GitHub URLs found in input")
    return urls


def report_paths(prefix: str) -> tuple[Path, Path]:
    reports = ROOT / "reports"
    reports.mkdir(exist_ok=True)
    return reports / f"{prefix}.json", reports / f"{prefix}.md"


def load_payload(payload_path: str | None = None, prefix: str = "agent-skills-intake-2026-07-16") -> dict:
    path = Path(payload_path) if payload_path else report_paths(prefix)[0]
    return json.loads(path.read_text(encoding="utf-8"))


def apply_pages(limit: int | None = None, payload_path: str | None = None, prefix: str = "agent-skills-intake-2026-07-16") -> int:
    payload = load_payload(payload_path, prefix)
    items = [i for i in payload["items"] if i.get("status") == "candidate"]
    normalize_candidates(items)
    if limit:
        items = items[:limit]
    failed = []
    for idx, item in enumerate(items, 1):
        cat = item["suggested_category"]
        cat_dir = ROOT / item["category_path"]
        ensure_category_indexes(cat_dir, Path(item["category_path"]).name)
        update_root_indexes_for_top(cat)
        update_agent_skills_parent(cat)
        en = cat_dir / f"{item['slug']}.md"
        zh = cat_dir / f"{item['slug']}.zh.md"
        print(f"phase=apply current={idx}/{len(items)} page={en.relative_to(ROOT)}", flush=True)
        if en.exists() or zh.exists():
            print(f"phase=skip reason=exists slug={item['slug']}", flush=True)
            continue
        try:
            branch = gh_default_branch(item["repo"])
            item["default_branch"] = branch
            sha = gh_branch_sha(item["repo"], branch)
            en.parent.mkdir(parents=True, exist_ok=True)
            en.write_text(page_en(item, sha), encoding="utf-8")
            zh.write_text(page_zh(item, sha), encoding="utf-8")
            subprocess.check_call(["python3", "tools/health.py", "--page", str(en.relative_to(ROOT)), "--write"], cwd=ROOT)
            subprocess.check_call(["python3", "tools/health_card.py", str(en.relative_to(ROOT)), str(zh.relative_to(ROOT))], cwd=ROOT)
            update_category_index(item)
            update_readme(item)
        except Exception as exc:  # noqa: BLE001 - keep batch progressing.
            failed.append({"repo": item["repo"], "error": str(exc)[:300]})
            print(f"phase=failed repo={item['repo']} error={str(exc)[:160]}", flush=True)
    if failed:
        out = ROOT / "reports/agent-skills-apply-failures-2026-07-16.json"
        out.write_text(json.dumps(failed, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"summary planned={len(items)} failed={len(failed)}")
    return 1 if failed else 0


def existing_repo_map() -> dict[str, str]:
    out: dict[str, str] = {}
    for page in (ROOT / "categories").rglob("*.md"):
        if page.name.startswith("INDEX") or page.name.endswith(".zh.md"):
            continue
        text = page.read_text(encoding="utf-8")
        m = re.search(r"(?m)^repo:\s*(\S+)", text)
        if not m:
            continue
        try:
            key, _, _ = repo_key(m.group(1))
        except ValueError:
            continue
        out[key] = str(page.relative_to(ROOT))
    return out


def infer_category(repo: str, data: dict, subpath: str | None) -> str:
    override = CATEGORY_OVERRIDES.get(repo.lower())
    if override:
        return override
    haystack = " ".join([
        repo,
        subpath or "",
        data.get("description") or "",
        " ".join(data.get("topics") or []),
    ]).lower()
    for cat, words in CATEGORY_HINTS.items():
        if any(w in haystack for w in words):
            return cat
    return "personal-collections" if repo.lower().endswith("/skills") else "uncertain"


def slugify(repo: str) -> str:
    owner, name = repo.split("/", 1)
    base = name.lower()
    # Avoid generic collisions for many owner/name `skills` repos.
    if base in {"skills", "agents"}:
        base = f"{owner.lower()}-{base}"
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return base or re.sub(r"[^a-z0-9]+", "-", repo.lower()).strip("-")


def category_path(cat: str) -> str:
    if cat in AGENT_SKILL_LEAVES:
        return f"categories/agent-skills/{cat}"
    return f"categories/{cat}"


def project_type(cat: str, repo: str, desc: str) -> str:
    if cat in AGENT_SKILL_LEAVES:
        return "skill-pack"
    if cat in {"investment-finance", "llm-eval", "document-parsing"}:
        name = repo.lower()
        if any(x in name for x in ["yfinance", "backtrader"]):
            return "library"
        if "awesome" in name:
            return "tool"
        return "framework"
    if cat in {"education-tutoring", "agent-governance", "video-production"}:
        return "app"
    return "tool"


def normalize_candidates(rows: list[dict]) -> None:
    for item in rows:
        if item.get("status") != "candidate":
            continue
        cat = CATEGORY_OVERRIDES.get(item["repo"].lower()) or item.get("suggested_category") or "uncertain"
        if cat == "uncertain":
            cat = "personal-collections"
        item["suggested_category"] = cat
        item["category_path"] = category_path(cat)
        item["slug"] = slugify(item["repo"])
        item["type"] = project_type(cat, item["repo"], item.get("github", {}).get("description", ""))


def build_report(urls: list[str], prefix: str) -> int:
    seen: set[str] = set()
    existing = existing_repo_map()
    rows = []
    duplicates = []
    for raw_url in urls:
        key, repo, subpath = repo_key(raw_url)
        if key in seen:
            duplicates.append(raw_url)
            continue
        seen.add(key)
        item = {"input_url": raw_url, "repo": repo, "subpath": subpath}
        if key in existing:
            item.update({"status": "already_indexed", "existing_page": existing[key]})
            rows.append(item)
            continue
        try:
            meta = gh_repo(repo)
        except Exception as exc:  # noqa: BLE001 - report, don't crash the whole wave.
            item.update({"status": "metadata_failed", "error": str(exc)[:300]})
            rows.append(item)
            continue
        item.update({
            "status": "candidate",
            "suggested_category": infer_category(repo, meta, subpath),
            "github": {
                "url": meta.get("url"),
                "description": meta.get("description") or "",
                "stars": meta.get("stargazerCount") or 0,
                "forks": meta.get("forkCount") or 0,
                "language": meta.get("language") or "",
                "license": meta.get("license") or "NOASSERTION",
                "archived": bool(meta.get("isArchived")),
                "fork": bool(meta.get("isFork")),
                "created_at": meta.get("createdAt"),
                "pushed_at": meta.get("pushedAt"),
                "topics": meta.get("topics") or [],
            },
        })
        rows.append(item)

    json_path, md_path = report_paths(prefix)
    payload = {"generated_at": TODAY, "input_count": len(urls), "duplicate_inputs": duplicates, "items": rows}
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# Agent Skills Intake — 2026-07-16",
        "",
        f"Generated: {TODAY}",
        f"Input URLs: {len(urls)}",
        f"Unique repos: {len(seen)}",
        f"Duplicate input URLs: {len(duplicates)}",
        "",
        "## Dry-run Evidence",
        "",
        "This report is a non-mutating intake gate. It fetches public GitHub metadata, deduplicates against existing oss-atlas pages, and assigns a first-pass category for human/agent review before any page creation.",
        "",
        "| # | Status | Repo | Suggested category | Stars | License | Description / note |",
        "|---|---|---|---|---:|---|---|",
    ]
    for i, item in enumerate(rows, 1):
        gh = item.get("github", {})
        note = item.get("existing_page") or item.get("error") or gh.get("description", "")
        note = str(note).replace("|", "\\|")[:140]
        lines.append(
            f"| {i} | {item['status']} | `{item['repo']}` | {item.get('suggested_category', '—')} | {gh.get('stars', 0)} | {gh.get('license', '—')} | {note} |"
        )
    if duplicates:
        lines += ["", "## Duplicate Inputs", ""] + [f"- {u}" for u in duplicates]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {json_path}")
    print(f"wrote {md_path}")
    print(f"summary input={len(urls)} unique={len(seen)} duplicates={len(duplicates)} items={len(rows)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--input-file", help="file containing GitHub URLs, one per line or embedded in text")
    parser.add_argument("--stdin", action="store_true", help="read GitHub URLs from stdin")
    parser.add_argument("--report-prefix", default="agent-skills-intake-2026-07-16", help="output prefix under reports/ without extension")
    parser.add_argument("--payload", help="JSON payload to use with --apply; defaults to reports/<report-prefix>.json")
    args = parser.parse_args()
    if args.apply:
        return apply_pages(args.limit, args.payload, args.report_prefix)
    urls = read_urls(args.input_file, args.stdin)
    return build_report(urls, args.report_prefix)


if __name__ == "__main__":
    sys.exit(main())
