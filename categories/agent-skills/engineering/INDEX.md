# engineering

> Leaf of [agent-skills](../INDEX.md). Code quality, web performance, testing, and scientific/eng workflows.
> ← up to [agent-skills](../INDEX.md) · root [route](../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **Agent Skills (addyosmani)** | A curated pack of ~24 production-engineering skills (quality, security, web-perf, API, ship) installed into your coding agent and routed through ~8 SDLC slash commands. | A (4/5) | [→](addyosmani-agent-skills.md) |
| **web-quality-skills** | A six-skill agent pack encoding Lighthouse / Core Web Vitals / WCAG / SEO best practices as on-demand instruction sets so a coding agent can audit and fix web-quality issues; advisory, not a measurement tool. | B (4/5) | [→](addyosmani-web-quality.md) |
| **Scientific Agent Skills** | A large skill pack (~147 skills) that turns a coding agent into a research assistant for biology, chemistry, medicine, and drug discovery — each skill wraps a scientific Python library or database with a documented SKILL.md loaded on demand. | A (4/5) | [→](scientific-agent-skills.md) |
| **Auto-Empirical Research Skills** | Use it when a coding agent must run an empirical social-science paper (DiD/IV/RDD/SCM, robustness, journal tables) and you need a catalog that routes to one skill instead of a general coding prompt. | C (3/5) | [→](auto-empirical-research-skills.md) |
| **Vercel Agent Skills** | Vercel's official agent-skill pack — install-on-demand React/Next.js/Vercel deploy, web-design, and docs audit guides in the agentskills.io/skills.sh format. | B (4/6) | [→](vercel-agent-skills.md) |
| **cc-skills-golang** | Use it when your coding agent writes Go that compiles but isn't idiomatic — error wrapping, nil traps, naming — and you want on-demand Go instruction files rather than a process/TDD pack. | C (5/6) | [→](cc-skills-golang.md) |
| **Waza** | A compact collection of eight "engineering habit" skills (plan, design, review, debug, write, research, read, audit) a coding agent loads on demand across Claude Code, Codex, and Cursor. | C (5/6) | [→](waza.md) |
| **mattpocock/skills** | Matt Pocock's engineering skill pack for Claude Code and skills.sh: grilling, domain docs, TDD, bug diagnosis, architecture, review, tickets, and implementation flow. | B (4/5) | [→](mattpocock-skills.md) |
| **BrowserAct Skills** | Agent-facing browser automation skill pack for BrowserAct: indexed browser control, stealth/private sessions, remote human handoff, and Skill Forge scraping workflows. | B (4/5) | [→](browser-act-skills.md) |
| **caveman** | Brevity skill plus optional local proxy: shrinks what a coding agent says and, if wrapped, what it reads, while leaving code, commands, and errors intact. | D (6/6) | [→](caveman.md) |
| **i-have-adhd** | A 10-rule response-style skill that makes a coding agent lead with the action, number steps, restate progress every turn, and drop the preamble and closer — one ruleset across roughly 15 harnesses. | A (4/5) | [→](i-have-adhd.md) |
| **Ponytail** | An always-on "lazy senior dev" ruleset: the coding agent maps what the change must reach, then takes the first rung that works (skip → reuse → stdlib → installed dep → one line) and returns the smallest complete diff, ending each reply with what it skipped. Lifecycle hooks, a session-start codebase map, review/audit commands, ~20 harness adapters. | B (5/6) | [→](ponytail.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Agent Skills (addyosmani)](addyosmani-agent-skills.md) | ✅ | A (4/5) | A curated pack of ~24 production-engineering skills (quality, security, web-perf, API, ship) installed into your coding agent and routed through ~8 SDLC slash commands. |
| [web-quality-skills](addyosmani-web-quality.md) | ✅ | B (4/5) | A six-skill agent pack encoding Lighthouse / Core Web Vitals / WCAG / SEO best practices as on-demand instruction sets so a coding agent can audit and fix web-quality issues; advisory, not a measurement tool. |
| [Scientific Agent Skills](scientific-agent-skills.md) | ✅ | A (4/5) | A large skill pack (~147 skills) that turns a coding agent into a research assistant for biology, chemistry, medicine, and drug discovery — each skill wraps a scientific Python library or database with a documented SKILL.md loaded on demand. |
| [Auto-Empirical Research Skills](auto-empirical-research-skills.md) | ✅ | C (3/5) | Catalog-plus-router for empirical social science (DiD/IV/RDD, journal tables); not life-science libraries, and licenses are mixed. |
| [Vercel Agent Skills](vercel-agent-skills.md) | ✅ | B (4/6) | Vercel's official agent-skill pack — install-on-demand React/Next.js/Vercel deploy, web-design, and docs audit guides in the agentskills.io/skills.sh format. |
| [cc-skills-golang](cc-skills-golang.md) | ✅ | C (5/6) | On-demand Go idiom skills for a coding agent; not a process/TDD pack, and installing all of it biases toward the author's libraries. |
| [Waza](waza.md) | ✅ | C (5/6) | A compact collection of eight "engineering habit" skills (plan, design, review, debug, write, research, read, audit) a coding agent loads on demand across Claude Code, Codex, and Cursor. |
| [mattpocock/skills](mattpocock-skills.md) | ✅ | B (4/5) | Engineering process pack for requirements grilling, domain docs, TDD, bug diagnosis, architecture, review, tickets, and implementation flow. |
| [BrowserAct Skills](browser-act-skills.md) | ✅ | B (4/5) | Agent browser automation layer with indexed actions, stealth/private sessions, remote handoff, and Skill Forge; use Playwright for deterministic tests. |
| [caveman](caveman.md) | ✅ | D (6/6) | Token-spend overlay: MIT skill shortens replies; optional BSL proxy shrinks logs/JSON/diffs the agent rereads. |
| [i-have-adhd](i-have-adhd.md) | ✅ | A (4/5) | Overlay for a reader with a short working memory; shapes how the agent talks, not what it knows — pick caveman when token spend is the problem. |
| [Ponytail](ponytail.md) | ✅ | B (5/6) | The code-side shrinker: forces the smallest complete change via a reuse-first ladder, with intensity levels and a model-run review/audit; pick caveman/i-have-adhd when the fat thing to cut is prose, not code. |


## What belongs here

Skill/prompt collections that make a coding agent better at **engineering tasks** — code review, performance, testing, scientific workflows.
