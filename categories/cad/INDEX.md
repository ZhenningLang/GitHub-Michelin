# cad

> Category node. Computer-aided design you run yourself — parametric 3D solid modeling, 2D drafting, and the geometry kernels and scripted-CAD toolchains behind them.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **text-to-cad** | Give an existing agent local Python-to-STEP modeling, saved-file checks and a viewer; not a trained CAD model. | B (6/6) | [→](text-to-cad.md) |
| **SolidCraft** | Editable parts through desktop sketches or built-in MCP; early Rust CAD, not proven suite equivalence. | C (5/6) | [→](solidcraft.md) |
| **FreeCAD** | Use it when you need an editable parametric history over a real solid model — sketch, constrain, pad/pocket, then re-dimension and let the part rebuild — on local files, with a Python API and no seat license. | A (5/6) | [→](freecad.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [text-to-cad](text-to-cad.md) | ✅ | B (6/6) | Agent skills plus a pinned Python CAD runtime and local viewer; source-first editing, default telemetry and explicit engineering review. |
| [SolidCraft](solidcraft.md) | ✅ | C (5/6) | Shared agent/UI commands and file scoping, at the cost of a young geometry stack. |
| [FreeCAD](freecad.md) | ✅ | A (5/6) | Open-source parametric 3D CAD: constraint-solved sketches, a feature history you can re-dimension, an OCCT solid kernel, local `.FCStd` files and a built-in Python API — at the cost of UX, assembly/CAM/FEM maturity and an upstream AI-contribution policy. |
| OpenSCAD · CadQuery · LibreCAD · Blender | 未收录 | — | The closest open-source substitutes (code-first CSG, Python-on-OCCT CAD, 2D drafting, mesh/artist pipeline) — named and weighed in FreeCAD's comparison table, not yet indexed. |
| Fusion 360 · Onshape · SolidWorks | 未收录 | — | Commercial/cloud CAD suites with polished assemblies, integrated simulation and vendor support — the workflows FreeCAD substitutes for and only partly matches. |

## What belongs here

Repositories whose primary job is **computer-aided design**: parametric or direct solid modeling, 2D drafting, and the CAD toolchains built on a geometry kernel. Not mesh-first artist DCC tools (see `game-dev`); not geographic data (see `geospatial`); not text-to-diagram tools (see `diagramming`).
