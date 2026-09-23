---
name: SdPaint
slug: sdpaint
repo: https://github.com/houseofsecrets/SdPaint
category: ai-design-generation
tags: [stable-diffusion, controlnet, painting, sketch-to-image, automatic1111, pygame, python]
language: Python
license: MIT
maturity: v1.2a, stalled (last push 2024-04)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2024-04-25T10:42:31Z
  default_branch: main
  default_branch_sha: 30aace450eb4a0b70ea68d322be93a9b2ad87647
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T15:57:35Z
  overall: D
  overall_score: 1.33
  scored_axes: 3
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 880
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: E
      raw:
        repo_age_days: 1254
        last_commit_age_days: 880
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: no_package_structural }
    governance: { reason: unattributable }
---

# SdPaint

A real-time sketch-to-image painting app: you draw on a pygame canvas and each stroke is sent to a running Stable Diffusion (AUTOMATIC1111 + ControlNet) backend, so a rough scribble becomes a generated image live as you draw.

![sdpaint — health radar](../../assets/health/sdpaint.svg)

## When to use

You're an artist or hobbyist who already runs **AUTOMATIC1111's Stable Diffusion WebUI with the ControlNet extension** locally, and you want a faster, more tactile loop than typing prompts and clicking Generate. You launch SdPaint, it opens a pygame window, and as you sketch (scribble or lineart), it streams each stroke to the WebUI's API with a ControlNet model so the generated picture updates in near-real-time — optionally accelerated with an LCM LoRA for fewer steps. You set a prompt and preset, doodle the composition, and watch SD fill it in, iterating by drawing rather than re-prompting.

You reach for it specifically when you want **interactive scribble-driven generation on your own machine**, you've already paid the cost of a working A1111 + ControlNet setup, and you'd rather paint than prompt. It's a thin, local front-end over that backend, not a hosted creative suite.

## When NOT to use

- **You don't already run AUTOMATIC1111 + ControlNet.** SdPaint is a *client* — it has no model and no inference of its own. The hard part (a working A1111 install, ControlNet extension, the right ControlNet v1.1 models, a capable GPU) is a prerequisite, not something it provides.
- **You want a polished, supported product.** It's a small enthusiast app, last touched 2024-04 (see Health); expect rough edges and no responsive upstream. [未验证]
- **You're not on a supported platform / have weak hardware.** Windows and macOS have install docs; **Linux is listed "To Do."** Real-time generation needs a GPU strong enough to keep up stroke-by-stroke; on weak hardware the "real-time" loop falls apart. [未验证]
- **You want managed cloud generation or a modern node UI.** For hosted or graph-based workflows, ComfyUI/Krita-AI/cloud SD services fit better than a local pygame client tied to A1111's API.
- **You need long-term reliability.** It's pinned to A1111's API and ControlNet behavior of its era; as those evolve, an unmaintained client can drift out of compatibility. [推断]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Krita + AI Diffusion plugin | 未收录 | Choose Krita with AI Diffusion when you need a full painting app with an SD plugin. | Full painting app with an SD plugin and live generation inside a real art tool; far richer canvas, heavier setup, more actively developed. |
| [ComfyUI](../on-device-ml/comfyui.md) | ✅ | Choose ComfyUI when you need a flexible node-graph Stable Diffusion front-end. | Node-graph SD front-end with huge flexibility and an active ecosystem; powerful but not a draw-and-watch scribble loop. |
| AUTOMATIC1111 WebUI (img2img / sketch tab) | 未收录 | Choose AUTOMATIC1111 when you need the backend SdPaint sits on. | The backend SdPaint sits on; can do sketch→image in-browser, but the click-Generate loop is less immediate than live stroke streaming. |
| ControlNet scribble in any SD UI | 未收录 | Choose ControlNet scribble when you need the underlying technique without SdPaint's front-end. | The underlying technique SdPaint wraps; available everywhere, but without SdPaint's real-time painting front-end. |

## Tech stack

- **Language:** Python.
- **UI:** pygame canvas for drawing and live preview (plus an alternative web interface launcher).
- **Generation backend (external):** AUTOMATIC1111 Stable Diffusion WebUI in API mode, with the **ControlNet** extension (scribble / lineart models), optional **LCM LoRA** for fast low-step rendering.
- **Models:** ControlNet v1.1 models (fetched from Hugging Face) loaded into the A1111 backend, not bundled.

## Dependencies

- **The A1111 backend** — a running Stable Diffusion WebUI with API enabled, the ControlNet extension, and the ControlNet v1.1 models. This is the heavy dependency; SdPaint talks to its HTTP API.
- **GPU** — a CUDA/Metal-capable GPU strong enough for near-real-time SD inference; CPU-only is impractical for the live loop.
- **Python + pygame** and the client's own requirements; optional LCM LoRA model files.
- **Platform:** documented for Windows and macOS; Linux "To Do."

## Ops difficulty

**Medium-to-high — almost entirely in the backend.** SdPaint itself is just a Python client (`pip install` deps, run the script). The operational weight is standing up and tuning AUTOMATIC1111 + ControlNet: GPU drivers, the WebUI install, enabling its API, downloading the correct ControlNet/LCM models, and getting inference fast enough to feel "real-time." If you already operate A1111, adding SdPaint is trivial; if you don't, that backend is the whole job. Because the client is unmaintained, you may also hit API-compatibility friction against newer A1111/ControlNet versions.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** **Stalled.** Last release v1.2a (2024-04), last push 2024-04 — roughly two years quiet. Not archived, but no recent activity; treat as coasting/likely-abandoned. [推断]
- **Governance / bus factor.** Owner is a **User** account (houseofsecrets); a top contributor (Danamir) authored most commits — effectively a one-to-two-person hobby project, weak bus factor. [推断]
- **Age & Lindy.** Created 2023-04; ~3 years old **but inactive for ~2 of them** ⇒ Lindy does **not** apply — it's a young project that stopped, not a durable one. The fast-moving SD ecosystem makes a stale client especially prone to drift. [推断]
- **Adoption.** ~1.6k stars reflect a burst of interest during the 2023 ControlNet wave; current usage is unverified and the ecosystem has moved toward ComfyUI/Krita-AI. [未验证]
- **Risk flags.** Hard external dependency on a specific-era A1111 + ControlNet API; unmaintained client risks compatibility breakage; permissive MIT, no relicense concerns. [推断]

## Caveats (unverified)

- [未验证] ~1.6k GitHub stars as of 2026-06; star counts are date-sensitive and reflect 2023-era interest, not necessarily current use.
- [推断] "Stalled / likely abandoned" is inferred from last release and last push both 2024-04 — GitHub does not mark it archived.
- [未验证] The dependency stack (A1111 API mode, ControlNet extension/models, LCM LoRA, pygame UI) and platform support (Windows/macOS, Linux "To Do") come from the README and are not re-tested against current A1111/ControlNet versions here.
- [推断] GPU requirement and "real-time needs a capable GPU" are inferred from the live-generation design, not a benchmarked spec.
- [推断] Compatibility with newer AUTOMATIC1111/ControlNet releases is an inference from the project being unmaintained; not verified against a current install.
