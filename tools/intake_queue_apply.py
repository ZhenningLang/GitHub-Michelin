#!/usr/bin/env python3
"""Apply a verified project-intake queue into first-pass oss-atlas pages.

This is an operational helper for the 2026-07-06 intake wave. It deliberately
does not compute health grades; run tools/health_backfill.py after page creation.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TODAY = dt.date.today().isoformat()


CATEGORY_TAGS = {
    "agent-runtimes": ["llm-agent", "agent-runtime"],
    "workflow-builders": ["llm-workflow", "agent-builder"],
    "coding-agents": ["coding-agent", "developer-tool"],
    "agent-memory": ["agent-memory", "knowledge-graph"],
    "llm-eval": ["llm-eval", "testing"],
    "llm-training": ["llm-training", "fine-tuning"],
    "llm-inference": ["llm-inference", "serving"],
    "web-ui": ["frontend", "ui"],
    "web-automation": ["browser-automation", "testing"],
    "workflow-orchestration": ["workflow", "orchestration"],
    "document-parsing": ["document-parsing", "pdf"],
    "pdf-tools": ["pdf", "document"],
    "markdown-tools": ["markdown", "document"],
    "databases": ["database", "data"],
    "observability": ["observability", "monitoring"],
    "auth": ["auth", "authorization"],
    "rag-retrieval": ["rag", "retrieval"],
}


def run_json(cmd: list[str], timeout: int = 30) -> dict:
    out = subprocess.check_output(cmd, cwd=ROOT, text=True, stderr=subprocess.STDOUT, timeout=timeout)
    return json.loads(out)


def owner_repo(url: str) -> str:
    m = re.search(r"github\.com/([^/]+)/([^/#?]+)", url)
    if not m:
        raise ValueError(f"not a GitHub repo URL: {url}")
    return f"{m.group(1)}/{m.group(2).removesuffix('.git')}"


def branch_sha(repo_url: str, branch: str) -> str:
    data = run_json(["gh", "api", f"repos/{owner_repo(repo_url)}/branches/{branch}"], timeout=30)
    return data["commit"]["sha"]


def rel_health(page_dir: Path, slug: str, zh: bool) -> str:
    card = f"{slug}.zh.svg" if zh else f"{slug}.svg"
    return os.path.relpath(ROOT / "assets" / "health" / card, start=page_dir)


def esc(s: object) -> str:
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()


def slug_tag(slug: str) -> str:
    return slug.replace("-", "_") if slug and slug[0].isdigit() else slug


def tags_for(item: dict) -> list[str]:
    leaf = Path(item["category_path"]).name
    tags = list(CATEGORY_TAGS.get(leaf, [leaf]))
    tags.append(slug_tag(item["slug"]))
    tags.append(item["type"])
    out = []
    for tag in tags:
        tag = re.sub(r"[^a-z0-9_-]+", "-", tag.lower()).strip("-")
        if tag and tag not in out:
            out.append(tag)
    return out[:8]


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---", 3)
    fm = {}
    for line in text[3:end].splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        raw = raw.strip()
        if raw.startswith("[") and raw.endswith("]"):
            fm[key.strip()] = [x.strip() for x in raw[1:-1].split(",") if x.strip()]
        else:
            fm[key.strip()] = raw.strip('"\'')
    return fm


def existing_pages(cat_dir: Path, exclude_slug: str) -> list[tuple[str, str, str, str]]:
    pages = []
    for page in sorted(cat_dir.glob("*.md")):
        if page.name.startswith("INDEX") or page.name.endswith(".zh.md") or page.stem == exclude_slug:
            continue
        try:
            fm = parse_frontmatter(page)
        except Exception:
            continue
        name = fm.get("name", page.stem)
        health = "? (0/6)"
        if fm.get("health"):
            health = "? (0/6)"
        pages.append((name, page.name, page.with_name(page.stem + ".zh.md").name, health))
    return pages[:4]


def frontmatter(item: dict, sha: str) -> str:
    gh = item["github"]
    license_id = gh.get("license") or "NOASSERTION"
    state = "archived" if gh.get("archived") else "active"
    stars = gh.get("stars") or 0
    maturity = f"{state}, ~{stars:,} stars (as of 2026-07)"
    tags = ", ".join(tags_for(item))
    return f"""---
name: {item['name']}
slug: {item['slug']}
repo: {gh.get('html_url') or item['repo']}
category: {Path(item['category_path']).name}
tags: [{tags}]
language: {gh.get('language') or 'Unknown'}
license: {license_id}
maturity: {maturity}
last_verified: {TODAY}
type: {item['type']}
upstream:
  pushed_at: {gh.get('pushed_at')}
  default_branch: {gh.get('default_branch')}
  default_branch_sha: {sha}
  archived: {str(bool(gh.get('archived'))).lower()}
---
"""


def comparison_en(item: dict, cat_dir: Path) -> str:
    rows = ["| Alternative | In index | Our verdict | Tradeoff |", "|---|---|---|---|"]
    for name, en, _zh, _health in existing_pages(cat_dir, item["slug"]):
        rows.append(f"| [{name}]({en}) | ✅ | When you need the established in-index option for this category, compare it against {item['name']} before switching. | {item['name']} is newly indexed from the intake backlog; use the existing page when its documented constraints match better, and choose {item['name']} only after verifying the repo-specific caveats below. |")
    if len(rows) == 2:
        rows.append(f"| Adjacent projects in this category | 未收录 | Use {item['name']} only after checking whether a narrower in-index page already covers the task. | This first-pass page records the project as a selectable repo, but the surrounding comparison set still needs semantic review. |")
    rows.append("| Hand-rolled integration | 未收录 | Choose custom code only when the needed scope is tiny and the maintenance burden is clearly lower than adopting this repo. | Custom code avoids a dependency but loses the upstream project, ecosystem, and documented tradeoffs captured here. |")
    return "\n".join(rows)


def comparison_zh(item: dict, cat_dir: Path) -> str:
    rows = ["| 替代品 | 是否收录 | 我们的评价 | 取舍 |", "|---|---|---|---|"]
    for name, _en, zh, _health in existing_pages(cat_dir, item["slug"]):
        rows.append(f"| [{name}]({zh}) | ✅ | 当你需要本分类里已经收录、约束更明确的方案时，先用它和 {item['name']} 对照。 | {item['name']} 是从 intake backlog 新增的首版页面；现有页面的“不用场景”如果更贴近任务，应优先按现有页面选择。 |")
    if len(rows) == 2:
        rows.append(f"| 本分类相邻项目 | 未收录 | 只有在确认没有更窄的已收录页面覆盖任务时，才选择 {item['name']}。 | 这个首版页面先把仓库纳入可选集合，但周边对比关系仍需要后续语义复核。 |")
    rows.append(f"| 自写集成 | 未收录 | 只有需求很小、维护成本明确低于引入 {item['name']} 时，才自写。 | 自写能少一个依赖，但会失去上游项目、生态和本页记录的选型取舍。 |")
    return "\n".join(rows)


def caveats_en(item: dict) -> str:
    reasons = item.get("reasons") or []
    bullets = ["- [未验证] This is a first-pass intake page generated from GitHub metadata and the 2026-07-06 backlog; before relying on it for a high-stakes selection, reread the upstream README, docs, license file, and release notes."]
    if "license_missing_or_noassertion" in reasons:
        bullets.append("- [未验证] GitHub API returned no SPDX license or NOASSERTION; inspect the repository license files before commercial or redistribution use.")
    if "github_repo_archived" in reasons:
        bullets.append("- [未验证] GitHub marks this repository archived; treat it as a pattern or legacy option unless a maintained successor is confirmed.")
    if "split_mixed_candidate_review_needed" in reasons:
        bullets.append("- [推断] The backlog item was mixed; this page records the verified repository URL only, not every adjacent project implied by the original label.")
    bullets.append("- [推断] The comparison table uses nearby in-index pages as a starting point; a later semantic review should replace generic neighboring rows with the closest true substitutes.")
    return "\n".join(bullets)


def caveats_zh(item: dict) -> str:
    reasons = item.get("reasons") or []
    bullets = ["- [未验证] 这是依据 GitHub 元数据和 2026-07-06 backlog 生成的首版 intake 页面；高风险选型前，请重新阅读上游 README、文档、许可证文件和 release notes。"]
    if "license_missing_or_noassertion" in reasons:
        bullets.append("- [未验证] GitHub API 没有返回 SPDX license，或返回 NOASSERTION；商用或再分发前必须检查仓库内许可证文件。")
    if "github_repo_archived" in reasons:
        bullets.append("- [未验证] GitHub 将该仓库标为 archived；除非确认有维护中的继任项目，否则只应当作模式参考或遗留选项。")
    if "split_mixed_candidate_review_needed" in reasons:
        bullets.append("- [推断] backlog 原项是混合候选；本页只记录已核验的具体仓库 URL，不代表原标签暗含的所有相邻项目。")
    bullets.append("- [推断] 横向对比表先使用同分类已收录页面作为起点；后续语义复核应把泛化邻居替换成最接近的真实替代品。")
    return "\n".join(bullets)


def page_en(item: dict, sha: str, cat_dir: Path) -> str:
    gh = item["github"]
    desc = esc(gh.get("description")) or f"{item['name']} is an open-source repository in the {Path(item['category_path']).name} category."
    archived = " It is archived on GitHub, so treat it as a legacy or pattern-source option rather than a default for new production work." if gh.get("archived") else ""
    card = rel_health(cat_dir, item["slug"], False)
    return frontmatter(item, sha) + f"""
# {item['name']}

{desc}{archived}

![{item['name']} — health radar]({card})

## When to use

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## When NOT to use

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## Comparison

{comparison_en(item, cat_dir)}

## Tech stack

- **Primary language:** {gh.get('language') or 'Unknown'} per GitHub metadata.
- **Repository:** `{gh.get('full_name')}`.
- **Project shape:** categorized as `{item['type']}` for atlas routing; verify upstream architecture before treating this as a stable API contract.
- **Upstream state:** default branch `{gh.get('default_branch')}`, last pushed `{gh.get('pushed_at')}`, archived `{str(bool(gh.get('archived'))).lower()}`.

## Dependencies

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## Ops difficulty

<!-- oss-atlas:unresearched -->
**UNRESEARCHED.** Nobody has read the upstream sources for this section. This is a hole, not a
verdict — do not act on it. Fill it from the sources (`sync-entry`) before this page can merge.

## Health & viability

- **Maintenance snapshot:** GitHub reports `archived={str(bool(gh.get('archived'))).lower()}` and `pushed_at={gh.get('pushed_at')}` as of {TODAY}.
- **Adoption snapshot:** ~{gh.get('stars') or 0:,} GitHub stars as of 2026-07; stars are only a noisy adoption signal.
- **License snapshot:** `{gh.get('license') or 'NOASSERTION'}` from GitHub API; inspect repository license files when the license matters.
- **Lindy and governance:** not fully reviewed in this intake pass. Treat org ownership, project age, release cadence, and bus factor as open review items before long-term adoption.
- **Risk flags:** {('archived repository; ' if gh.get('archived') else '')}{('license needs manual verification; ' if 'license_missing_or_noassertion' in item.get('reasons', []) else '')}first-pass page generated from backlog metadata.

## Caveats (unverified)

{caveats_en(item)}
""".lstrip()


def page_zh(item: dict, sha: str, cat_dir: Path) -> str:
    gh = item["github"]
    desc = esc(gh.get("description")) or f"{item['name']} 是 `{Path(item['category_path']).name}` 分类下的开源仓库。"
    archived = " GitHub 将它标为 archived，因此新生产项目不应把它当默认方案，而应先当作遗留或模式参考。" if gh.get("archived") else ""
    card = rel_health(cat_dir, item["slug"], True)
    return frontmatter(item, sha) + f"""
# {item['name']}

{desc}{archived}

![{item['name']} — 健康度雷达]({card})

## 何时使用

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 何时不用

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 横向对比

{comparison_zh(item, cat_dir)}

## 技术栈

- **主要语言：** GitHub 元数据返回为 {gh.get('language') or 'Unknown'}。
- **仓库：** `{gh.get('full_name')}`。
- **项目形态：** atlas 路由暂归为 `{item['type']}`；把它当稳定 API 契约前，请复核上游架构。
- **上游状态：** 默认分支 `{gh.get('default_branch')}`，最后 push `{gh.get('pushed_at')}`，archived 为 `{str(bool(gh.get('archived'))).lower()}`。

## 依赖

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 运维难度

<!-- oss-atlas:unresearched -->
**未研究。** 还没有人为这一节读过上游资料。这里是一个空洞，不是结论——不要据此判断。请先读源头把它补上（`sync-entry`），这个页面才能合并。

## 健康度与可持续性

- **维护快照：** 截至 {TODAY}，GitHub 返回 `archived={str(bool(gh.get('archived'))).lower()}`，`pushed_at={gh.get('pushed_at')}`。
- **采用快照：** 2026-07 约 {gh.get('stars') or 0:,} 个 GitHub stars；stars 只是有噪声的采用信号。
- **许可证快照：** GitHub API 返回 `{gh.get('license') or 'NOASSERTION'}`；许可证关键时必须检查仓库内许可证文件。
- **Lindy 与治理：** 本次 intake 未完整复核。长期采用前，请继续检查组织归属、项目年龄、发布节奏和 bus factor。
- **风险信号：** {('仓库已归档；' if gh.get('archived') else '')}{('许可证需要人工核验；' if 'license_missing_or_noassertion' in item.get('reasons', []) else '')}本页是从 backlog 元数据生成的首版页面。

## 存疑（未验证）

{caveats_zh(item)}
""".lstrip()


def table_row_en(item: dict, rel_page: str) -> str:
    gh = item["github"]
    use = esc(gh.get("description")) or f"Use it when you need {item['name']} for the {Path(item['category_path']).name} category."
    return f"| **{item['name']}** | {use} | ? (0/6) | [→]({rel_page}) |"


def table_row_zh(item: dict, rel_page: str) -> str:
    gh = item["github"]
    desc = esc(gh.get("description")) or f"当你需要在 `{Path(item['category_path']).name}` 分类中评估 {item['name']} 时用它。"
    return f"| **{item['name']}** | {desc} | ?（0/6） | [→]({rel_page}) |"


def insert_before_section_end(path: Path, row: str, marker: str) -> None:
    text = path.read_text(encoding="utf-8")
    if row in text:
        return
    idx = text.find(marker)
    if idx == -1:
        text = text.rstrip() + "\n" + row + "\n"
    else:
        text = text[:idx].rstrip() + "\n" + row + "\n\n" + text[idx:]
    path.write_text(text, encoding="utf-8")


def add_index_rows(item: dict, cat_dir: Path) -> None:
    en = cat_dir / "INDEX.md"
    zh = cat_dir / "INDEX.zh.md"
    insert_before_section_end(en, table_row_en(item, f"{item['slug']}.md"), "\n## Comparison")
    insert_before_section_end(zh, table_row_zh(item, f"{item['slug']}.zh.md"), "\n## 对比")
    # Some category indexes use "## What belongs here" directly after project rows.
    if f"{item['slug']}.md" not in en.read_text(encoding="utf-8"):
        insert_before_section_end(en, table_row_en(item, f"{item['slug']}.md"), "\n## What belongs here")
    if f"{item['slug']}.zh.md" not in zh.read_text(encoding="utf-8"):
        insert_before_section_end(zh, table_row_zh(item, f"{item['slug']}.zh.md"), "\n## 什么该放这里")


def top_category(item: dict) -> str:
    rel = Path(item["category_path"]).relative_to("categories")
    return rel.parts[0]


def add_readme_row(item: dict) -> None:
    top = top_category(item)
    page_rel = f"{item['category_path']}/{item['slug']}.md"
    zh_rel = f"{item['category_path']}/{item['slug']}.zh.md"
    gh = item["github"]
    use = esc(gh.get("description")) or f"Use it when you need {item['name']} in the {top} area."
    row = f"| **{item['name']}** | {use} | {gh.get('license') or 'NOASSERTION'} | ? (0/6) | [EN]({page_rel}) · [中]({zh_rel}) |"
    zh_use = esc(gh.get("description")) or f"当你需要在 {top} 方向评估 {item['name']} 时用它。"
    zh_row = f"| **{item['name']}** | {zh_use} | {gh.get('license') or 'NOASSERTION'} | ?（0/6） | [EN]({page_rel}) · [中]({zh_rel}) |"
    for readme, line in ((ROOT / "README.md", row), (ROOT / "README.zh.md", zh_row)):
        text = readme.read_text(encoding="utf-8")
        if page_rel in text or zh_rel in text:
            continue
        heading = f"### {top}"
        start = text.find(heading)
        if start == -1:
            readme.write_text(text.rstrip() + f"\n\n{heading}\n\n| Project | Use when | License | Health | Page |\n| --- | --- | --- | --- | --- |\n{line}\n", encoding="utf-8")
            continue
        next_heading = text.find("\n### ", start + len(heading))
        if next_heading == -1:
            next_heading = len(text)
        updated = text[:next_heading].rstrip() + "\n" + line + "\n" + text[next_heading:]
        readme.write_text(updated, encoding="utf-8")


def apply(queue_path: Path, limit: int | None, include_risky: bool) -> int:
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    items = [i for i in queue if i.get("status") == "verified"]
    if not include_risky:
        items = [i for i in items if not i.get("reasons")]
    if limit:
        items = items[:limit]
    done = skipped = failed = 0
    for idx, item in enumerate(items, 1):
        cat_dir = ROOT / item["category_path"]
        en = cat_dir / f"{item['slug']}.md"
        zh = cat_dir / f"{item['slug']}.zh.md"
        print(f"phase=apply current={idx}/{len(items)} page={en.relative_to(ROOT)}", flush=True)
        if en.exists() or zh.exists():
            skipped += 1
            continue
        try:
            sha = branch_sha(item["repo"], item["github"].get("default_branch") or "main")
            en.write_text(page_en(item, sha, cat_dir), encoding="utf-8")
            zh.write_text(page_zh(item, sha, cat_dir), encoding="utf-8")
            add_index_rows(item, cat_dir)
            add_readme_row(item)
            item["status"] = "page_created"
            done += 1
        except Exception as exc:
            item["status"] = "apply_failed"
            item.setdefault("reasons", []).append(f"apply_failed:{str(exc)[:160]}")
            failed += 1
        queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"summary created={done} skipped={skipped} failed={failed}")
    return 1 if failed else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", type=Path, default=ROOT / "reports/project-intake-queue-2026-07-06.json")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--include-risky", action="store_true", help="include verified items with risk reasons such as archived or NOASSERTION")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    queue = json.loads(args.queue.read_text(encoding="utf-8"))
    verified = [i for i in queue if i.get("status") == "verified"]
    risky = [i for i in verified if i.get("reasons")]
    planned = verified if args.include_risky else [i for i in verified if not i.get("reasons")]
    if args.limit:
        planned = planned[: args.limit]
    print(f"phase=dry-run total={len(queue)} verified={len(verified)} risky={len(risky)} planned={len(planned)} blocked={sum(1 for i in queue if i.get('status') == 'blocked')}")
    for item in planned[:10]:
        print(f"  - {item['id']}: {item['name']} -> {item['category_path']}/{item['slug']}.md")
    if len(planned) > 10:
        print(f"  ... {len(planned) - 10} more")
    if not args.apply:
        print("apply_ready=false reason=dry-run-only add --apply")
        return 0
    return apply(args.queue, args.limit, args.include_risky)


if __name__ == "__main__":
    raise SystemExit(main())
