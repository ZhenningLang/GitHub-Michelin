---
name: Mermaid
slug: mermaid
repo: https://github.com/mermaid-js/mermaid
category: diagramming
tags: [diagram, flowchart, text-to-diagram, markdown, sequence-diagram, gantt, visualization, javascript]
language: TypeScript
license: MIT
maturity: active, ~89k stars (2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-29T10:42:57Z
  default_branch: develop
  default_branch_sha: 338c98df454b7587f4e4a8a73c5dcbbd59ba3175
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:16:04Z
  overall: A
  overall_score: 3.83
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
        last_commit_age_days: 1
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: B
      raw:
        median_ttfr_hours: 62.8
        qualifying_issues: 16
        band: default
        window_offset_days: 7
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: npmjs.org
        canonical_package: "@mermaid-js/parser"
        dependent_repos_count: 1
        downloads_last_month: 54202447
        graph_tier: D
        volume_tier: A
        cross_check_divergence: 1.03
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4343
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 79
        top1_share: 0.18
        top3_share: 0.395
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Mermaid

A JavaScript/TypeScript library that renders diagrams from a Markdown-like text syntax — flowcharts, sequence, gantt, class, ER, state, git-graph, pie, mindmap and more — so diagrams live as plain text in version control instead of as binary image files.

![mermaid — health radar](../../assets/health/mermaid.svg)

## When to use

You're an engineer who keeps writing architecture docs and runbooks in Markdown, and the diagrams keep rotting: someone drew the flow in draw.io a year ago, exported a PNG, and now the PNG is wrong but nobody has the source file. You want the picture to live *in* the doc, diff in a pull request, and re-render automatically. You write a fenced ` ```mermaid ` block with a few lines of `graph TD; A-->B`, push it, and GitHub, GitLab, your docs site (Docusaurus, MkDocs, Obsidian), and your IDE preview all render it inline — no binary asset, no external editor, no broken export. When the flow changes you edit text and the diagram follows; reviewers see the diff of the *diagram*, not a swapped-out image.

You also reach for it when you're an agent or a tool generating diagrams programmatically: the input is text you can template and emit, so producing a sequence diagram or an ER schema from code or from an LLM is just string assembly, then `mermaid.render()` in a browser/headless context (or `mmdc` from `@mermaid-js/mermaid-cli`) to get SVG/PNG. It's the de-facto text-to-diagram format precisely because so many host platforms already understand the fenced block — you target Mermaid and inherit GitHub/GitLab/Notion-style rendering for free.

## When NOT to use

- **You need pixel-precise or hand-tuned layouts.** Mermaid auto-lays-out via its layout engine; you do not place nodes by hand. When the exact position, spacing, or routing matters, a manual canvas (draw.io/diagrams.net, Excalidraw) or a layout language you can steer (Graphviz/DOT, D2) gives control Mermaid intentionally withholds.
- **Large or dense graphs.** Auto-layout quality and rendering performance degrade as node/edge count grows; big flowcharts come out tangled or unreadable. For serious graph layout at scale, Graphviz (with its mature layout algorithms) or the ELK-based engines are stronger. [未验证]
- **It runs JavaScript in the renderer.** Mermaid executes in the browser/JS runtime and historically has had XSS surface; rendering *untrusted* diagram text means you must set `securityLevel` (`strict`/`sandbox`) appropriately and accept that some interactive features get disabled. Don't render attacker-controlled Mermaid with `securityLevel: 'loose'`.
- **You want a WYSIWYG drawing tool.** There is no drag-and-drop canvas — you edit text. Non-technical stakeholders who expect to push boxes around will not be happy; give them draw.io or Excalidraw.
- **Diagram types it does poorly or doesn't cover.** Highly custom/freeform diagrams, precise UML beyond the supported subset, or very specific notations may be better served by PlantUML (broader/stricter UML) or a general drawing tool. Verify your specific diagram type renders acceptably before standardizing on it. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Graphviz / DOT | 未收录 | Pick Graphviz when mature graph layout algorithms for large or dense graphs matter more than Markdown-native rendering. | Mature, scriptable graph **layout** engine with strong algorithms for large/dense graphs; produces excellent auto-layout but DOT is lower-level and not natively rendered inline by docs platforms the way Mermaid is. |
| [PlantUML](plantuml.md) | ✅ | Pick PlantUML when you need broader, stricter UML coverage and can accept Java/server rendering. | Broader and stricter UML coverage (and more diagram types); typically needs a Java runtime/server to render, vs Mermaid's pure-JS in-browser rendering and ubiquitous host support. |
| [D2](d2.md) | ✅ | Pick D2 when its newer language and layout-engine choices matter more than Mermaid's host-platform ubiquity. | Newer text-to-diagram language (Go) with multiple layout engines (incl. ELK/dagre) and a focus on cleaner layouts; smaller install base and far less built-in host-platform rendering than Mermaid. |
| draw.io (diagrams.net) | 未收录 | Pick draw.io when you need a full WYSIWYG canvas editor rather than version-control-friendly diagram source. | Full WYSIWYG canvas editor — pixel control and rich shapes — but diagrams are stored as XML/binary, not diffable plain text, and not auto-rendered from a fenced code block. |
| [Excalidraw](excalidraw.md) | ✅ | Pick Excalidraw when hand-drawn whiteboarding and collaboration matter more than text-to-diagram syntax. | Hand-drawn-style WYSIWYG whiteboard; great for sketches and collaboration, not a text-to-diagram syntax and not version-control-diffable as source. |
| [flowchart.js](flowchart-js.md) | ✅ | Pick flowchart.js only when you need a narrow flowchart-only JS library. | Narrow JS library for flowcharts only; Mermaid covers far more diagram types and has vastly larger ecosystem/host support. |

## Tech stack

- **Language:** TypeScript (with substantial JavaScript), distributed as an npm package and via CDN (jsDelivr); also packaged as `@mermaid-js/mermaid-cli` (`mmdc`) for headless rendering.
- **Rendering:** browser/DOM — produces SVG. Uses **D3.js** for SVG manipulation and **dagre / dagre-d3** for graph layout; some diagram types/configs can use an ELK-based layout.
- **Syntax:** a Markdown-inspired DSL per diagram type (`graph`/`flowchart`, `sequenceDiagram`, `classDiagram`, `erDiagram`, `stateDiagram`, `gantt`, `gitGraph`, `pie`, `mindmap`, `journey`, C4, …).
- **Config/security:** runtime config object including `securityLevel` (`strict` / `loose` / `antiscript` / `sandbox`) controlling script execution and sandboxed-iframe rendering. [未验证]

## Dependencies

- **Runtime:** a JavaScript environment with a DOM. In production that's the user's browser (or a host platform — GitHub/GitLab/Notion/Docusaurus/MkDocs/Obsidian — that bundles it). For server-side/CLI rendering it needs a headless browser (the CLI uses Puppeteer/Chromium under the hood).
- **Library deps:** pulls in D3 and dagre (and their transitive deps) as an npm dependency; nothing to operate as a service.
- **Install paths:** `npm i mermaid`, CDN `<script>` from jsDelivr, or `npm i -g @mermaid-js/mermaid-cli` for `mmdc`.
- **No backend/datastore:** it is a client-side rendering library, not a service.

## Ops difficulty

**Low** for the common case: there is nothing to deploy or operate — you drop a fenced block into a platform that already renders Mermaid, or add the npm/CDN script to a page. "Ops" only appears when you render *yourself*: server-side/headless rendering via `mermaid-cli` drags in a Chromium/Puppeteer dependency, which is the usual source of CI breakage, sandbox/permission issues, and image size bloat. The other real concern is **security**, not uptime: if you ever render untrusted diagram text, getting `securityLevel` right (and keeping the library patched against XSS advisories) is the maintenance burden. As a pinned library dependency it's low-touch; auto-layout output occasionally shifts across versions, so visual regressions on upgrade are the thing to watch.

## Health & viability

- **Responsiveness**: Grade B — median first-response time 62.8 hours across 16 qualifying issues/PRs.
- **Maintenance (2026-06).** Last pushed 2026-06 with recent releases (e.g. `@mermaid-js/tiny@11.16.0`, 2026-06-25) — **actively** maintained, not archived. [推断]
- **Governance / bus factor.** Owned by the `mermaid-js` GitHub org (a multi-maintainer community project, not a lone-maintainer repo), which lowers bus-factor risk versus a single-author library. No single corporate owner. [推断]
- **Age & Lindy verdict.** ~12 years old (created 2014-11) and still active ⇒ a **strong Lindy** signal; it's the de-facto text-to-diagram standard, embedded by GitHub/GitLab/Notion/Docusaurus/Obsidian. [推断]
- **Adoption & ecosystem.** Very large adoption — ~89k stars and, more meaningfully, first-class rendering baked into major platforms — makes it the safe default for diagram-as-code. [未验证]
- **Risk flags.** No relicense (MIT) and no commercial open-core split found; the standing concern is **security**, not viability — it runs JS in the renderer and has historically had XSS surface, so `securityLevel` must be set when rendering untrusted input. The ~1.6k open issues are typical for a project of this reach, not a health flag. [推断]

## Caveats (unverified)

- [未验证] ~88.9k GitHub stars and "TypeScript primary language" as of 2026-06 per the repo page; star counts are date-sensitive and approximate.
- [未验证] Latest published release observed as `@mermaid-js/tiny@11.16.0` (2026-06-25) on the repo's releases; the main `mermaid` package version and exact current number shift release-to-release — check npm/releases before pinning.
- [未验证] Layout/rendering internals (D3 + dagre/dagre-d3, optional ELK engine) are stated from the README and general knowledge; the exact engines used per diagram type and the default change across versions — confirm against current docs.
- [未验证] `securityLevel` values and their precise effects (script execution, sandboxed iframe, disabled interactivity) are summarized from the docs; verify the current option set and defaults for your version before rendering untrusted input.
- [未验证] CLI/headless rendering depending on Puppeteer/Chromium is inferred from `@mermaid-js/mermaid-cli`'s typical implementation; confirm the current renderer and its system requirements.
- [推断] Performance/quality degradation on large or dense graphs is a general property of auto-layout, not a measured benchmark of this library; test your largest real diagram before committing.
- [推断] "Does some diagram types poorly" is an inference about auto-layout fit, not a per-type defect claim — evaluate your specific diagram type.
