# product-vendors

> Leaf of [vendor-collections](../INDEX.md). First-party bundles in which a platform or product vendor teaches a coding agent to use its own product correctly — AWS, Android, Chrome, Remotion, Cloudflare, Bright Data; only useful if you are on that vendor.
> ← up to [vendor-collections](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **Agent Plugins for AWS** | AWS Labs' official collection of nine agent plugins (serverless, Amplify, SageMaker, migration, databases, deploy/cost-estimate, etc.) that teach Claude Code / Cursor / Codex to architect, deploy, and operate on AWS via marketplace-installed, trigger-phrase skills wired to AWS MCP servers. | B (5/6) | [→](aws-agent-plugins.md) |
| **Remotion Agent Skills** | Remotion's official 12-skill bundle that teaches a coding agent (Claude Code, Codex, Cursor, Kimi Code) to write correct Remotion React video code — installable with `npx skills add remotion-dev/skills`, version-locked to the framework. | C (4/5) | [→](remotion-skills.md) |
| **Android Skills** | Google's official 24-skill pack for the Android jobs models still fail (edge-to-edge, R8, Navigation 3, Play policy) — installed with the Android CLI, not `npx skills add`. | B (5/6) | [→](android-skills.md) |
| **Modern Web Guidance** | Google Chrome's search-then-retrieve skill: before writing HTML/CSS/client JS the agent pulls one eval-graded modern-platform guide (native APIs, Baseline support, sized fallbacks) from a local-search npm CLI. | B (5/6) | [→](modern-web-guidance.md) |
| **Agent Toolkit for AWS** | Use it when your coding agent works in a real AWS account and you want AWS's current playbooks plus agent calls that IAM and CloudTrail can tell apart from yours: ~114 skills and a hosted MCP endpoint; AWS-only, the hosted half sees your traffic. | A (4/5) | [→](agent-toolkit-for-aws.md) |
| **Cloudflare Skills** | Use it when your coding agent builds on Cloudflare and keeps writing from stale memory: 16 official skills that pick the right Cloudflare product and make the agent read current docs first, plus a hosted MCP entry; Cloudflare-only, no tags, mostly pointers that need network access. | A (4/5) | [→](cloudflare-skills.md) |
| **Bright Data Skills** | Use it when your agent keeps hitting 403s and challenge pages and you have chosen to pay Bright Data to get past them: 21 vendor skills that route each fetch to the right paid product and check for block pages; every call is metered, one skill tells the agent to drop its built-in web tools, no tags, and the README Quick Start points at deleted scripts. | C (4/5) | [→](brightdata-skills.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Agent Plugins for AWS](aws-agent-plugins.md) | ✅ | B (5/6) | AWS Labs' official collection of nine agent plugins (serverless, Amplify, SageMaker, migration, databases, deploy/cost-estimate, etc.) that teach Claude Code / Cursor / Codex to architect, deploy, and operate on AWS via marketplace-installed, trigger-phrase skills wired to AWS MCP servers. |
| [Remotion Agent Skills](remotion-skills.md) | ✅ | C (4/5) | Vendor-canonical, version-locked guidance for agents authoring React video; useless if you are not on a skill-loading harness or not using Remotion, and its content license is undeclared. |
| [Android Skills](android-skills.md) | ✅ | B (5/6) | Google's official Android playbooks for the jobs models still fail; Android-only, CLI-installed, contributions closed. |
| [Modern Web Guidance](modern-web-guidance.md) | ✅ | B (5/6) | Browser-vendor build guidance retrieved per task; preview `0.0.x`, npm on every call, telemetry on by default, never checks your output. |
| [Agent Toolkit for AWS](agent-toolkit-for-aws.md) | ✅ | A (4/5) | AWS's successor to its Labs plugins: skills plus agent-tagged calls via a hosted endpoint; AWS-only, no tags, outside PRs closed, startup plugin carries partner-offer links. |
| [Cloudflare Skills](cloudflare-skills.md) | ✅ | A (4/5) | Cloudflare's own product router plus doc-pointer skills and one hosted MCP entry; Cloudflare-only, installs track `main` with a hand-bumped version, no hooks or evals, routing skill is written to recommend Cloudflare products. |
| [Bright Data Skills](brightdata-skills.md) | ✅ | C (4/5) | Operating manual for Bright Data's paid unblocking network, not a scraper: no key, no function, every call metered with no spend cap in the pack; installs track `main`, a pending PR stack would delete 17 of 21 skills, and it says almost nothing about site terms or data law. |

## What belongs here

First-party bundles in which a platform or product vendor teaches a coding agent to use its own product correctly — AWS, Android, Chrome, Remotion, Cloudflare, Bright Data; only useful if you are on that vendor.
