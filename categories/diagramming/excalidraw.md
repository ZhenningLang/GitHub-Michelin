---
name: Excalidraw
slug: excalidraw
repo: https://github.com/excalidraw/excalidraw
category: diagramming
tags: [whiteboard, diagram, canvas, collaboration, hand-drawn, sketch, react, export]
language: TypeScript
license: MIT
maturity: active, ~126.5k stars (as of 2026-07)
last_verified: 2026-07-01
type: library
upstream:
  pushed_at: 2026-07-05T20:21:54Z
  default_branch: master
  default_branch_sha: 9357f98a9b6c4f8af3ada6ccce38e54330f2627c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:15:54Z
  overall: A
  overall_score: 3.67
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
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 34.4
        qualifying_issues: 26
        band: default
        window_offset_days: 5
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: npmjs.org
        canonical_package: "@excalidraw/excalidraw"
        dependent_repos_count: 523
        downloads_last_month: 1918275
        graph_tier: C
        volume_tier: B
        cross_check_divergence: 1.02
        release_downloads: 31973
        release_assets: 14
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 2456
        last_commit_age_days: 0
        cohort: library
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 13
        top1_share: 0.599
        top3_share: 0.889
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

# Excalidraw

A virtual whiteboard for sketching hand-drawn style diagrams — collaborative, end-to-end encrypted, and embeddable as a React component or used standalone on excalidraw.com.

![Excalidraw — health radar](../../assets/health/excalidraw.svg)

## When to use

You're a product manager or designer who needs to quickly whiteboard an architecture sketch, a user flow, or a wireframe in a meeting and share it with the team. You pick Excalidraw over Mermaid because you want the result to look informal and approachable — like a napkin sketch rather than a rendered text diagram — so stakeholders focus on the idea, not the syntax. You pick it over draw.io because you want a lightweight, hand-drawn aesthetic without the complexity of a full WYSIWYG canvas with rich shapes and integrations. You pick it over Figma because you need a quick whiteboard, not a high-fidelity design tool with component variants, constraints, and responsive preview. You open excalidraw.com, draw rectangles and arrows on an infinite canvas, drop in images, and share the link; the collaboration is end-to-end encrypted and the `.excalidraw` JSON format is open. You also reach for it when you're a React developer building a docs site or an app that needs an embedded whiteboard: the `@excalidraw/excalidraw` npm package gives you a drop-in component with dark mode, shape libraries, i18n, and PNG/SVG/clipboard export.

## When NOT to use

- If you need diagrams as version-controlled plain text, use Mermaid or PlantUML instead of Excalidraw, because Excalidraw stores drawings as JSON (or binary PNG/SVG), not as a text-to-diagram syntax that can be diffed in Git.
- If you need pixel-precise or auto-layout diagrams, use draw.io or bpmn-js instead of Excalidraw, because the hand-drawn aesthetic is the point; it does not enforce BPMN compliance, UML strictness, or automatic graph layout.
- If you need to generate diagrams programmatically from code, use Mermaid or PlantUML instead of Excalidraw, because there is no declarative text syntax to render, and producing diagrams from CI pipelines or LLM output requires scripting the JSON format or using a different tool.
- If you need a full design/prototyping tool, use Figma instead of Excalidraw, because Excalidraw is a whiteboard with no component variants, constraints, responsive preview, or design handoff.
- If you must work completely offline without any build step, use draw.io or a desktop diagram app instead of Excalidraw, because the web app requires a browser, and while the React component works offline after bundling, the zero-friction path is the hosted app. [推断]
- If you need real-time collaboration at enterprise scale, use Figma or draw.io Enterprise instead of Excalidraw, because the free tier runs on excalidraw.com and heavy team usage may need Excalidraw+ (paid) or self-hosted infrastructure not provided out of the box. [未验证]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
| --- | --- | --- | --- |
| [Mermaid](mermaid.md) | ✅ | Use Excalidraw for hand-drawn, collaborative whiteboarding; choose Mermaid when you need diagrams as plain text, diffable in Git, rendered in Markdown. | Plain-text, diffable diagrams rendered in Markdown and docs; trades visual style for version-control portability. |
| [flowchart.js](flowchart-js.md) | ✅ | Use Excalidraw for hand-drawn, collaborative whiteboarding; choose flowchart.js when you need a narrow, lightweight flowchart renderer in the browser. | Narrow JS flowchart renderer only; Mermaid covers more types and has broader host support. |
| [draw.io](drawio.md) | ✅ | Use Excalidraw for lightweight, hand-drawn sketch whiteboarding; choose draw.io when you need a full WYSIWYG canvas with rich shapes and integrations. | Full-featured WYSIWYG canvas editor with Google Drive / OneDrive / GitHub integrations; heavier and more formal than Excalidraw's sketch style. |
| tldraw | 未收录 | Use Excalidraw for the de-facto standard hand-drawn whiteboard; choose tldraw when you want a newer, more extensible whiteboard library with a stronger dev-focused API. | Newer whiteboard library with strong programmatic API; smaller ecosystem but more flexible for custom apps. |
| Figma | 未收录 | Use Excalidraw for quick, informal sketch whiteboarding; choose Figma when you need high-fidelity UI design, prototyping, and design-system management. | Industry-standard design tool for UI/UX; not a sketch whiteboard, requires a paid team plan for full features. |

## Tech stack

- **Language:** TypeScript, compiled to JavaScript; distributed as an npm package (`@excalidraw/excalidraw`) and a CDN-ready bundle.
- **Frontend:** React component built on the HTML5 Canvas API (and an interactive SVG layer for export); uses `rough.js` for the hand-drawn, sketch-like rendering style.
- **Collaboration:** End-to-end encrypted real-time collaboration via WebSockets on the hosted instance; self-hosted or embedded usage omits this.
- **Export:** PNG, SVG, clipboard copy, and `.excalidraw` JSON open format; dark mode and shape libraries are built-in.
- **Styling:** Customizable theme colors and element styles; the "sketchy" look is a core design choice, not an after-effect.

## Dependencies

- **Runtime:** A modern web browser with Canvas support. For embedded use, a React 18+ application.
- **Library deps:** Install via `npm i @excalidraw/excalidraw` or load from CDN; the package bundles its own rendering logic and does not require a separate backend to draw.
- **Collaboration backend:** The hosted app uses a server for WebSocket relay and end-to-end encryption; self-hosted collaboration requires setting up your own signaling server.
- **No database:** The whiteboard state is client-side JSON; persistence is via export, local storage, or your own backend.

## Ops difficulty

**Low** for the common case: use the free hosted app at excalidraw.com, export your drawings, and move on. **Medium** when embedding the React component: you pin the npm package, handle version upgrades (the component API can shift), and bundle it into your build pipeline. **Medium–High** if you want self-hosted real-time collaboration: you must operate a WebSocket relay server, manage encryption keys, and handle NAT/firewall traversal. As a client-side library, the main maintenance burden is staying current with React/TypeScript compatibility and occasional breaking API changes in the npm package. [推断]

## Health & viability
- **Maintenance**: Grade A — 13/13 active weeks in trailing 13; last commit 3 days ago.
- **Responsiveness**: Grade A — median first-response time 23.5 hours across 22 qualifying issues/PRs.
- **Adoption**: Grade B — 1,390,033 monthly downloads via npmjs.org (package: @excalidraw/excalidraw).
- **Longevity**: Grade A — 2374 days old.
- **Governance**: Grade B — top-3 contributor share 83.5% (?).
- **Risk / License**: Grade A — MIT license.
## Caveats (unverified)

- [未验证] ~126.5k GitHub stars as of 2026-07-01; star counts are approximate and time-sensitive.
- [未验证] The exact npm package API version and React compatibility requirements shift release-to-release; verify the current `@excalidraw/excalidraw` docs before embedding.
- [未验证] End-to-end encryption details for the hosted collaboration are summarized from the project README; confirm the current encryption model and key handling for sensitive use cases.
- [未验证] Self-hosted collaboration server requirements are inferred from the repo architecture; the official docs should be consulted for production deployment guidance.
- [未验证] Styling customization and theme color details are summarized from the project description; confirm the current theming API for your version.
- [推断] The "sketchy" rendering style is core to the product and cannot be disabled for a clean vector look; if you need crisp line art, evaluate other tools.
- [推断] Large canvas performance with thousands of elements may degrade in browser memory; test with your expected diagram complexity before committing.
