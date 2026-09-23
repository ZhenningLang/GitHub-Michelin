#!/usr/bin/env python3
"""Sync health frontmatter data to the body 'Health & viability' section.

Reads the health block from YAML frontmatter and rewrites the corresponding
prose section in the body so they never drift.  Preserves the Caveats section."""
import argparse, re, yaml
from pathlib import Path


def parse_frontmatter(text):
    """Return (frontmatter_dict, body_text) or (None, text) if no frontmatter."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    try:
        fm = yaml.safe_load(text[3:end])
    except Exception:
        return None, text
    return fm or {}, text[end + 4:]


def axis_bullet_en(name, axis):
    """Generate an English health bullet from axis data."""
    grade = axis.get("grade", "?")
    raw = axis.get("raw", {}) or {}
    inferred = raw.get("inferred", False)
    source = raw.get("source", "")
    
    labels = {
        "maintenance": "Maintenance",
        "responsiveness": "Responsiveness",
        "adoption": "Adoption",
        "longevity": "Longevity",
        "governance": "Governance",
        "risk_license": "Risk / License",
    }
    label = labels.get(name, name)
    
    if grade == "N/A":
        reason = axis.get("reason", "not applicable")
        return f"- **{label}**: Not applicable to this project type — {reason}."

    if grade == "?":
        reason = axis.get("reason", "unknown")
        return f"- **{label}**: Cannot be scored — {reason}."
    
    if name == "maintenance":
        active = raw.get("active_weeks_13", "?")
        last = raw.get("last_commit_age_days", "?")
        return f"- **{label}**: Grade {grade} — {active}/13 active weeks in trailing 13; last commit {last} days ago."
    
    if name == "responsiveness":
        median = raw.get("median_ttfr_hours")
        qualifying = raw.get("qualifying_issues")
        if median is not None and qualifying is not None:
            return f"- **{label}**: Grade {grade} — median first-response time {median} hours across {qualifying} qualifying issues/PRs."
        elif inferred or source == "inferred":
            return f"- **{label}**: Grade {grade} — inferred from maintenance activity (no direct issue/PR response data)."
        else:
            return f"- **{label}**: Grade {grade}."
    
    if name == "adoption":
        registry = raw.get("registry", "?")
        pkg = raw.get("canonical_package", "?")
        downloads = raw.get("downloads_last_month")
        stars = raw.get("stars")
        if downloads is not None:
            return f"- **{label}**: Grade {grade} — {downloads:,} monthly downloads via {registry} (package: {pkg})."
        elif stars is not None:
            return f"- **{label}**: Grade {grade} — {stars:,} GitHub stars."
        else:
            return f"- **{label}**: Grade {grade}."
    
    if name == "longevity":
        age = raw.get("repo_age_days", "?")
        return f"- **{label}**: Grade {grade} — {age} days old."
    
    if name == "governance":
        owner = raw.get("owner_type", "?")
        top3 = raw.get("top3_share")
        if top3 is not None:
            return f"- **{label}**: Grade {grade} — top-3 contributor share {top3:.1%} ({owner})."
        else:
            return f"- **{label}**: Grade {grade} ({owner})."
    
    if name == "risk_license":
        spdx = raw.get("spdx_id", "?")
        return f"- **{label}**: Grade {grade} — {spdx} license."
    
    return f"- **{label}**: Grade {grade}."


def axis_bullet_zh(name, axis):
    """Generate a Chinese health bullet from axis data."""
    grade = axis.get("grade", "?")
    raw = axis.get("raw", {}) or {}
    inferred = raw.get("inferred", False)
    source = raw.get("source", "")
    
    labels = {
        "maintenance": "维护活跃度",
        "responsiveness": "响应速度",
        "adoption": "采用广度",
        "longevity": "长青度",
        "governance": "治理集中度",
        "risk_license": "许可风险",
    }
    label = labels.get(name, name)
    
    if grade == "N/A":
        reason = axis.get("reason", "not applicable")
        return f"- **{label}**：该项目类型不适用——{reason}。"

    if grade == "?":
        reason = axis.get("reason", "unknown")
        return f"- **{label}**：无法计算——{reason}。"
    
    if name == "maintenance":
        active = raw.get("active_weeks_13", "?")
        last = raw.get("last_commit_age_days", "?")
        return f"- **{label}**：Grade {grade}——最近 13 周中 {active} 周有提交；最后提交距今 {last} 天。"
    
    if name == "responsiveness":
        median = raw.get("median_ttfr_hours")
        qualifying = raw.get("qualifying_issues")
        if median is not None and qualifying is not None:
            return f"- **{label}**：Grade {grade}——中位首次响应时间 {median} 小时，基于 {qualifying} 个 qualifying issues/PRs。"
        elif inferred or source == "inferred":
            return f"- **{label}**：Grade {grade}——基于维护活跃度推断（无直接 issue/PR 响应数据）。"
        else:
            return f"- **{label}**：Grade {grade}。"
    
    if name == "adoption":
        registry = raw.get("registry", "?")
        pkg = raw.get("canonical_package", "?")
        downloads = raw.get("downloads_last_month")
        stars = raw.get("stars")
        if downloads is not None:
            return f"- **{label}**：Grade {grade}——{registry} 上月下载量 {downloads:,}（包名：{pkg}）。"
        elif stars is not None:
            return f"- **{label}**：Grade {grade}——GitHub {stars:,} 星。"
        else:
            return f"- **{label}**：Grade {grade}。"
    
    if name == "longevity":
        age = raw.get("repo_age_days", "?")
        return f"- **{label}**：Grade {grade}——仓库已创建 {age} 天。"
    
    if name == "governance":
        owner = raw.get("owner_type", "?")
        top3 = raw.get("top3_share")
        if top3 is not None:
            return f"- **{label}**：Grade {grade}——前三贡献者占比 {top3:.1%}（{owner}）。"
        else:
            return f"- **{label}**：Grade {grade}（{owner}）。"
    
    if name == "risk_license":
        spdx = raw.get("spdx_id", "?")
        return f"- **{label}**：Grade {grade}——{spdx} 许可证。"
    
    return f"- **{label}**：Grade {grade}。"


def sync_page(path):
    """Sync health data for a single page.  Returns True if changed."""
    text = path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    if not fm or "health" not in fm:
        return False

    health = fm["health"]
    axes = health.get("axes", {})
    is_zh = path.name.endswith(".zh.md")
    
    # Build the new health section bullets
    bullets = []
    for axis_name in ["maintenance", "responsiveness", "adoption", "longevity", "governance", "risk_license"]:
        axis_data = axes.get(axis_name, {})
        if is_zh:
            bullets.append(axis_bullet_zh(axis_name, axis_data))
        else:
            bullets.append(axis_bullet_en(axis_name, axis_data))
    
    health_section = "\n".join(bullets) + "\n"
    
    # Replace only the Health & viability section, preserving Caveats
    if is_zh:
        header = "## 健康度与可持续性\n"
        next_header = "## 存疑（未验证）"
    else:
        header = "## Health & viability\n"
        next_header = "## Caveats (unverified)"
    
    # Replace the health section's body only, stopping at the NEXT H2 of any kind.
    #
    # This used to scan forward to a hardcoded `next_header` ("## Caveats (unverified)")
    # with a negative lookahead, which had two destructive failure modes:
    #   1. Any H2 sitting between the two headers was swallowed and overwritten. This
    #      really happened: a `--all` run deleted `## Tech stack` / `## Dependencies` /
    #      `## Ops difficulty` from pyav and lit (4 files), recovered from git.
    #   2. On a page with no Caveats section the lookahead never matches, so `.*` under
    #      DOTALL runs to end of file and the whole tail of the page is replaced.
    # Terminating on `\n## ` makes the rewrite structurally local: it can only touch the
    # lines between this H2 and the following one.
    pattern = re.escape(header) + r"(.*?)(?=\n## |\Z)"
    match = re.search(pattern, body, re.DOTALL)
    if not match:
        return False

    new_body = body[:match.start()] + header + health_section + body[match.end():]

    # Defence in depth: a section rewrite must not change which sections exist. The fix
    # above is an argument about a regex; this is a check on the actual output, so a later
    # edit to that regex cannot silently resume eating sections.
    before_h2 = re.findall(r"(?m)^## .*$", body)
    after_h2 = re.findall(r"(?m)^## .*$", new_body)
    if before_h2 != after_h2:
        lost = [h for h in before_h2 if h not in after_h2]
        raise SystemExit(
            f"{path}: refusing to write — section rewrite changed the H2 set\n"
            f"  lost:   {lost or '(none)'}\n"
            f"  before: {before_h2}\n"
            f"  after:  {after_h2}"
        )

    # Reconstruct full text with original frontmatter
    new_text = text[:len(text) - len(body)] + new_body
    
    if new_text == text:
        return False
    
    path.write_text(new_text, encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser(description="Sync health frontmatter to body prose")
    ap.add_argument("--all", action="store_true",
                    help="sync all pages in categories/ (requires --overwrite-prose)")
    ap.add_argument("--page", help="sync a single page path")
    ap.add_argument("--overwrite-prose", action="store_true",
                    help="acknowledge that --all replaces hand-written analysis with the "
                         "generated one-line-per-axis template")
    args = ap.parse_args()

    if args.page:
        changed = sync_page(Path(args.page))
        print(f"{'synced' if changed else 'no change'}: {args.page}")
        return 0

    if args.all:
        # `--all` is destructive on any page whose health prose was written by hand: the
        # generated text is one terse line per axis, so a corpus-wide run replaces
        # multi-paragraph analysis with ~350 chars of restated frontmatter. That happened
        # once (1218 pages rewritten, 548 of them losing hand-written analysis, recovered
        # from git). The script's real job is newly-added pages, which have no prose yet.
        if not args.overwrite_prose:
            print("refusing --all without --overwrite-prose.\n"
                  "  --all regenerates the health section of EVERY page from frontmatter,\n"
                  "  replacing any hand-written analysis with one terse line per axis.\n"
                  "  For a newly-added page use --page; if you really mean the whole\n"
                  "  corpus, re-run with --overwrite-prose.")
            return 2
        pages = list(Path("categories").rglob("*.md"))
        changed = 0
        for p in pages:
            if p.name.endswith("INDEX.md"):
                continue
            if sync_page(p):
                changed += 1
                print(f"synced: {p}")
        print(f"\n{changed}/{len(pages)} pages synced")
        return 0

    ap.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
