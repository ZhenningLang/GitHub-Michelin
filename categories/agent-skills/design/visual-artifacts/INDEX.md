# visual-artifacts

> Leaf of [design](../INDEX.md). Skills whose **deliverable is itself a visual artifact** — editable technical diagrams, HTML-native prototypes, decks, animations, infographics. They generate files to inspect, rather than steering UI code or copying a named design.
> ← up to [design](../INDEX.md) · root [route](../../../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Collections in this leaf

| Collection | Use when | Health | Page |
| --- | --- | --- | --- |
| **archify** | Agent skill for self-contained architecture, workflow, sequence, data-flow, and lifecycle diagrams with theme toggle and export controls. | B (4/6) | [→](archify.md) |
| **drawio-skill** | An agent skill that turns prose, code, IaC and API schemas into editable `.drawio` files, then re-syncs them from the source without discarding a hand-tuned layout. | B (4/5) | [→](drawio-skill.md) |
| **diagram-design** | Agent skill for publishable diagrams in your own brand: onboards your site's palette and fonts, then draws 44 editorial diagram and chart types as one self-contained HTML+SVG file — at the cost of any editable source. | B (4/5) | [→](diagram-design.md) |
| **huashu-design** | HTML-native design skill for prototypes, slide decks, editable PPTX, animation/MP4/GIF, infographics, and visual artifact generation. | B (5/6) | [→](huashu-design.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [archify](archify.md) | ✅ | B (4/6) | Best for technical diagrams; choose human diagram editors when WYSIWYG editing is required. |
| [drawio-skill](drawio-skill.md) | ✅ | B (4/5) | Best when the deliverable is an editable `.drawio` that must track a real source; choose Mermaid when the diagram should stay plain text, or archify when no draw.io install is acceptable. |
| [diagram-design](diagram-design.md) | ✅ | B (4/5) | Best when the diagram will be published and must match your brand; choose Mermaid when it lives in git and changes often, drawio-skill when someone must keep editing it. |
| [huashu-design](huashu-design.md) | ✅ | B (5/6) | Best for agent-generated HTML artifacts; choose Stitch for implementation handoff or Taste-Skill for lightweight UI taste guidance. |


## What belongs here

Agent skills that **produce a visual deliverable** — a diagram file, an HTML prototype, a deck, an infographic, a rendered animation. Not publishing surfaces (social cards and article illustrations live in [visual-content](../../visual-content/INDEX.md); dedicated deck tooling in [slides-ppt](../../slides-ppt/INDEX.md)), and not taste guidance applied to shipped UI code (see [ui-taste](../ui-taste/INDEX.md)).
