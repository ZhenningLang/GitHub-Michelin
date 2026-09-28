---
name: Open Design
slug: open-design
repo: https://github.com/nexu-io/open-design
category: ai-design-generation
tags: [ai-design, local-first, desktop-app, electron, byok, design-systems, prototyping, slides, mcp]
language: TypeScript
license: Apache-2.0
maturity: v0.24.1, active, ~98.4k stars (as of 2026-09)
last_verified: 2026-09-28
type: app
upstream:
  pushed_at: 2026-09-28T10:22:08Z
  default_branch: main
  default_branch_sha: 64710082d02c041da47bf8c6d6c5316b36b28b22
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T10:21:32Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 0.1
        qualifying_issues: 10
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: null
        canonical_package: null
        homebrew_installs_90d: 1755
        homebrew_tier: B
        release_downloads: 947979
        release_assets: 246
        release_tier: C
        signal_basis: homebrew+releases
    longevity:
      grade: D
      raw:
        repo_age_days: 153
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 94
        top1_share: 0.193
        top3_share: 0.359
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Open Design

Ask your coding agent for a pitch deck or a clickable app mockup and you get a wall of unstyled HTML in the chat — or you pay for a closed hosted design tool that keeps your files on its servers. Open Design gives the agent you already run a desktop studio around it: brand design systems and templates go into its context, the result renders in a live preview, and you export real HTML/PDF/PPTX/MP4 files.

![open-design — health radar](../../assets/health/open-design.svg)

## When to use

You're a product engineer or founder who already lives in Claude Code, Codex, Cursor or a similar agent, and this week you need design output rather than code: a three-screen mobile onboarding mockup for a user test, a 12-slide investor update, a 30-second product promo. Asking the agent directly gets you `index.html` with Times New Roman and default blue links, because it has no brand to follow and no way to show you the result. The hosted answer (Claude Design, v0, Lovable) does look good, but it bills per seat, runs on the vendor's model, and your prompts, screenshots and brand assets live in someone else's cloud.

You reach for Open Design when you want that same brief → preview → critique → export loop but driven by *your* agent and *your* model key, with the output as plain files on your disk. It ships 151 `DESIGN.md` brand design systems (Linear, Stripe, Apple, Notion…), 100+ skills and a large template/plugin catalog, spawns whichever agent CLI you have installed, and previews what it writes in a sandboxed iframe. The deciding tradeoff against the narrower in-index siblings — a single deck skill, a prompt-to-HTML tool — is breadth: prototypes, decks, dashboards, images and HyperFrames video in one workspace, at the cost of installing and keeping up with a fast-moving desktop app.

## How it works

Open Design does not ship its own agent. It is a local server (the "daemon", a background Node process that keeps projects in a SQLite file) plus a web/Electron front end. When you submit a brief, the daemon starts the coding-agent CLI you already have — `claude`, `codex`, `cursor-agent`, 26 CLIs in total — inside a project folder, and puts the chosen template or skill plus the active `DESIGN.md` (a Markdown file describing a brand's colours, type and components) into its instructions; think of it as handing a contractor your brand book before they start. The agent writes ordinary files; Open Design watches them and renders them in a locked-down preview frame. If no CLI is installed, a built-in proxy calls any OpenAI-compatible endpoint with your key instead. What you do: pick the artifact type and design system, write the brief, judge the result and export. The other way in is to skip the GUI entirely — `od mcp install claude` registers it as an MCP server (a plug-in tool interface) inside your agent, so you can say "use open-design to generate a landing page" from your normal session.

![open-design — backbone user story](../../assets/flow/open-design.svg)

<!-- flow-steps:begin (generated from flows/open-design.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the desktop app; have a coding-agent CLI on PATH or a BYOK model key — component: `desktop app`
2. **Open Design**: Detects the agent CLIs on PATH and loads skills, templates and 151 design systems — component: `local daemon`
3. **You**: On Home, pick an artifact type and a design system, then type a brief
4. **Open Design**: Runs your agent in the project folder with the template and DESIGN.md composed in — `DESIGN.md` — component: `runtime adapter`
5. **Open Design**: Renders the files it writes in a sandboxed live preview — component: `Studio preview iframe`
6. **You**: Critique in chat until it looks right, then export — `HTML · PDF · PPTX`

**Value**: On-brand prototypes, decks and videos as real files on your disk, made by the agent you already pay for

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You want zero install and zero upkeep.** It is a desktop app plus a local daemon that ships a minor release every few days. If logging into a website is the whole budget, the hosted Claude Design or v0 (neither is a repository) fit better; you give up local files and model choice for convenience.
- **You need an editable vector design file or real-time co-editing.** Output is code-rendered HTML/PPTX/MP4, not a layered vector document, and no multiplayer editing is documented. For pixel-level work, components with variants and team review, use [Penpot](../design-editors/penpot.md) (self-hosted) or Figma.
- **Your data policy forbids outbound telemetry.** Official builds turn product analytics on by default (opt-out on first run; the optional content channel can include prompts and tool output), and a scrubbed safety/reliability channel stays on regardless of the toggle. Forks and source builds without the telemetry credentials send neither — so in regulated or air-gapped settings build from source, or use a plain skill such as [guizang-ppt-skill](../agent-skills/slides-ppt/guizang-ppt.md) inside your existing agent, which adds no telemetry of its own.
- **You're on Linux and want a packaged app.** The latest releases ship only macOS (arm64/x64) and Windows x64 installers; Linux means running from source (Node ~24, pnpm 10.33) or the Docker image. If that's too much, [html-anything](html-anything.md) is a lighter prompt-to-HTML path.
- **You need a stable surface to build on.** It went from v0.11 to v0.24.1 between June and September 2026 (13 minor releases) and the plugin manifest, runtime adapters and design-system package shape are still moving. Pin a version, or depend on the underlying pieces — [HyperFrames](../video-production/hyperframes.md) for HTML→MP4, a single deck skill for slides — which have a smaller surface to break.
- **You have no model access.** There is no free bundled inference: you bring an agent CLI subscription, a BYOK key, or pay the vendor's own OpenDesign Cloud model service. Without one of those, nothing generates.
- **You need MP4 at volume.** HyperFrames renders through headless Chrome plus FFmpeg on your machine, and the cinematic video/audio templates call paid models (Seedance, Veo, Suno). For batch video pipelines, drive [HyperFrames](../video-production/hyperframes.md) directly on a render box instead of through a desktop GUI.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [html-anything](html-anything.md) | ✅ | When the output is a single standalone HTML page from a prompt, pick html-anything; pick Open Design when you also need decks, video, brand systems and export in one place. | Far less to install and learn; you lose the design-system catalog, live studio and PPTX/MP4 export. |
| [Impeccable](impeccable.md) | ✅ | When the job is polishing UI inside your existing agent session, pick Impeccable; pick Open Design when non-UI artifacts (decks, images, video) matter too. | Stays inside your agent with no extra app; covers only UI quality, not multi-artifact delivery. |
| [guizang-ppt-skill](../agent-skills/slides-ppt/guizang-ppt.md) | ✅ | When a magazine-style deck is the only artifact, install guizang-ppt-skill directly; Open Design bundles this same skill verbatim alongside everything else. | One skill, no daemon, no telemetry; no preview studio, other artifact types or design-system switching. |
| [HyperFrames](../video-production/hyperframes.md) | ✅ | When you only need agent-written HTML→MP4 video, especially in batch, use HyperFrames directly; Open Design is its GUI host plus prompt templates. | Scriptable and headless; you give up the studio preview and the Seedance/Veo template catalog. |
| [Penpot](../design-editors/penpot.md) | ✅ | When designers need a shared, editable vector file with components and comments, pick Penpot; pick Open Design when the agent should produce finished code-rendered artifacts. | Real multiplayer vector editing, self-hostable; no agent generation loop or HTML/MP4 output. |
| Claude Design (Anthropic) | not a repo | When managed hosting and Anthropic's polish matter more than local files and model choice, pick the hosted product; Open Design is its open, local-first counterpart. | Zero install and no upkeep; closed source, cloud-only, locked to Anthropic's models and billing. |

## Tech stack

- **Language:** TypeScript (pnpm monorepo: `apps/web`, `apps/daemon`, `apps/desktop`, plus shared `packages/`).
- **Front end:** Next.js 16.2 App Router + React 18.3.
- **Local daemon:** Node 24 · Express 5 · SSE streaming · `better-sqlite3` 12 for projects, conversations and runs; stdio MCP server; `od` CLI.
- **Desktop shell:** Electron 41 with a sandboxed renderer and a sidecar IPC channel; previews render in a sandboxed iframe.
- **Model access:** spawns 26 local agent CLIs via runtime adapters, or a BYOK proxy for Anthropic / OpenAI / Azure / Gemini / Ollama and any OpenAI-compatible endpoint, with an SSRF guard that blocks internal IPs unless allow-listed.
- **Content:** 151 `DESIGN.md` design-system packages, 100+ functional skills, 277 official plugins, 15 deck templates × 36 themes, HyperFrames templates.
- **Export:** HTML (inlined), PDF, PPTX, ZIP, Markdown, MP4 (HyperFrames).

## Dependencies

- **Model access (required):** a coding-agent CLI on `PATH`, a BYOK key for a supported/OpenAI-compatible endpoint, or a paid OpenDesign Cloud account.
- **Desktop:** the macOS (Apple Silicon / Intel) or Windows x64 installer bundles its runtime. On macOS, `/usr/bin/od` can shadow the `od` CLI — use the Settings → MCP server snippet instead.
- **From source (Linux, or dev):** Node `~24`, pnpm `>=10.33.2 <11`; data lives in a local SQLite file, no external database.
- **Server/Docker:** `deploy/docker-compose` with an `OD_API_TOKEN` for Basic/Bearer auth; public exposure needs a reverse proxy and `OPEN_DESIGN_ALLOWED_ORIGINS`.
- **Video:** HyperFrames rendering needs headless Chrome + FFmpeg on the host; cinematic video/audio templates need keys for the paid model providers they call.

## Ops difficulty

**Low on macOS/Windows desktop, medium elsewhere.** On the packaged app you install, point it at an agent or key, and generate; the recurring cost is keeping up with releases that land every few days and occasionally change plugin or runtime behaviour. Linux users and anyone self-hosting are on **medium**: exact Node/pnpm versions, the Docker compose file with an API token, reverse-proxy origin settings if exposed beyond loopback, and the Chrome/FFmpeg toolchain for video. Security-conscious teams also have to own telemetry settings — turn off the opt-out analytics on each install, or build from source to drop both telemetry channels.

## Health & viability

- **Maintenance (as of 2026-09-28):** very active — commits every week of the last quarter and 38 GitHub releases in five months, the latest v0.24.1 on 2026-09-24. Pace is itself the risk: minor versions arrive faster than most teams re-test.
- **Governance & bus factor:** owned by the `nexu-io` organization (created 2026-02, brands itself OpenDesign). About 94 people contributed in the past year and the top contributor holds ~19% of commits, so it is not a one-person repo; but MAINTAINERS.md reserves merge rights to an internal Core Team whose roster is not public, so the roadmap is vendor-controlled.
- **Backing & business model:** the same team sells OpenDesign Cloud, a paid model service built into the app (since v0.9), and the README opens with its promotions. That funds the project, but it is an open-core-style incentive to watch: whether future features land in the free BYOK path or only behind the Cloud sign-in is not yet knowable. [推断]
- **Age & Lindy verdict:** created 2026-04-28, five months old, with ~98k stars and ~11k forks — a launch-wave repo riding Claude Design's release, not a Lindy-safe bet. Treat stars as hype until it survives a year.
- **Risk flags / lock-in:** Apache-2.0, no relicense so far, and outputs are plain HTML/PDF/PPTX/MP4, so walking away costs little. The real flags are default-on product telemetry and minor-version churn in the plugin and adapter formats.

## Caveats (unverified)

- [未验证] Counts (151 design systems, 100+ skills, 277 plugins, 26 agent CLIs, 15 deck templates × 36 themes) are the README's own figures as of 2026-09-28 and change almost every release.
- [未验证] Star (~98.4k) and fork (~11.4k) counts are from the GitHub API on 2026-09-28 and are volatile; stars on a five-month-old repo are not evidence of durability.
- [未验证] The telemetry description comes from `PRIVACY.md` at the time of reading; what the shipped binaries actually send was not independently inspected.
- [推断] "No documented multiplayer editing" rests on the README and roadmap; a collaboration plugin (`od-tune-collab`) exists and its scope was not examined.
- [推断] Whether future capabilities stay available on the free BYOK path or move behind OpenDesign Cloud is a judgment about incentives, not an observed change.
- [未验证] The Linux gap reflects the v0.24.1 release assets and issue #4368; a Linux artifact may ship in any later release.
