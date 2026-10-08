---
name: pygame
slug: pygame
repo: https://github.com/pygame/pygame
category: game-dev
tags: [python, game-library, sdl, 2d-graphics, multimedia, gamedev]
language: C
license: LGPL-2.1
maturity: v2.6.1 (2024-09), last commit 2025-10-05, quiet since (as of 2026-10-08)
last_verified: 2026-10-08
type: library
upstream:
  pushed_at: 2025-11-01T03:05:13Z
  default_branch: main
  default_branch_sha: 85fda3f719d437cf27106afae8c890e6b88ba5f5
  archived: false
health:
  schema: 1
  computed_at: 2026-10-08T08:19:43Z
  overall: C
  overall_score: 2.0
  scored_axes: 4
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: D
      raw:
        archived: false
        last_commit_age_days: 367
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 460.0
        qualifying_issues: 3
        band: default
        window_offset_days: 6
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: pygame
        dependent_repos_count: 17300
        downloads_last_month: 2217050
        graph_tier: A
        volume_tier: A
        cross_check_divergence: null
        release_downloads: 2921212
        release_assets: 1777
        release_tier: B
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 3483
        last_commit_age_days: 367
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    governance: { reason: unattributable }
    risk_license: { reason: license_declared_unverifiable }
---

# pygame

A free, cross-platform Python library for writing 2D games and multimedia apps — a Pythonic wrapper over SDL that gives you a display surface, an event loop, image/sound/font loading, and sprite/collision helpers.

![pygame — health radar](../../assets/health/pygame.svg)

## When to use

You're teaching yourself (or a class) to program and you want the payoff of putting pixels on a screen, not just printing to a terminal. You `pip install pygame`, and in a couple dozen lines you have a window, a game loop polling `pygame.event.get()`, a player rectangle you move with the arrow keys, and a sound that plays on collision. There's no engine GUI, no project format, no asset pipeline to learn — it's just Python, and you can read every line of your game. For learning game loops, sprites, collision, and basic graphics/audio, pygame is the canonical low-friction starting point in Python.

You also reach for it when you want a *small* 2D game or interactive multimedia toy and you already think in Python: a game-jam entry, a visualization with keyboard/mouse interaction, a teaching demo, or a prototype. You get blitting to surfaces, image and font loading, mixer-based audio, sprite groups with collision detection, and a clock for frame-rate control — enough to ship a complete small 2D game without leaving the Python ecosystem or adopting a heavyweight engine.

## How it works

pygame hands you building blocks, not a game. **It does the platform work**: through SDL (Simple DirectMedia Layer, a C library that talks to each operating system's windows, input, graphics and audio) it opens the window, collects keyboard and mouse events, loads images, sounds and fonts, and mixes audio in the background. **You write the loop that is the game**: every frame you pull events with `pygame.event.get()`, move your objects, blit — copy — your surfaces (in-memory images) onto the screen surface, call `pygame.display.flip()` to show the finished frame, and `clock.tick(60)` to hold the frame rate. Helpers such as `pygame.sprite` groups and rectangle collision tests save boilerplate, but scenes, physics and an editor are yours to build. It is a box of Lego bricks, not a pre-built model.

![pygame — backbone user story](../../assets/flow/pygame.svg)

<!-- flow-steps:begin (generated from flows/pygame.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the wheel, which bundles SDL on common platforms — `pip install pygame`
2. **You**: Open a window and load your images, sounds and fonts — `pygame.display.set_mode · pygame.image.load`
3. **You**: Write the game loop: read events, update positions, blit, flip, tick — `pygame.event.get() · pygame.display.flip() · clock.tick(60)`
4. **pygame**: Collects keyboard, mouse and window events from the OS into a queue via SDL
5. **pygame**: Copies your surfaces into the window and shows the finished frame on flip
6. **pygame**: Paces the loop to your frame rate while the mixer plays sound alongside

**Value**: A playable window with input and sound from plain Python — no engine or editor to learn

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You're building a 3D game or anything performance-critical.** pygame is a 2D, CPU-blitting library; it has no scene graph, no built-in 3D, and the Python game loop will bottleneck on anything demanding. For 3D or AAA-style work, that's Godot/Unity/Unreal territory.
- **You want an editor, scene system, or asset pipeline.** It's a *library*, not an engine — no visual editor, no scene format, no animation timeline. If you want "open a project and drag entities around," look at Godot.
- **You need a polished, full-featured 2D engine.** For more structure (built-in physics, tilemaps, GUI, deployment to consoles) consider pyglet, Arcade, or a real engine; pygame stays deliberately low-level.
- **You're targeting the web or mobile as a first-class platform.** pygame is desktop-first (Windows/macOS/Linux); web (via pygbag/WASM) and mobile are possible but are not the primary, well-paved path.
- **You're starting a new project and want an actively maintained line.** This repo has had no commit since 2025-10-05 and no release since 2.6.1 (2024-09). The community fork **pygame-ce** (`pip install pygame-ce`, still imported as `pygame`) was pushed 2026-10-06 and is on 2.5.8 on PyPI; prefer it unless a course or dependency pins the original package. Check which one your tutorials and dependencies assume — installing both into one environment fights over the same `pygame` import name.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| pygame-ce (community edition) | 未收录 | Choose pygame-ce when faster releases, newer SDL support, or tutorial compatibility point at the fork; choose pygame when the original package name and long-standing ecosystem are safer for your course or dependency chain. | A community fork of this same library with a faster release cadence and newer SDL support; API-compatible enough that the choice is mostly about maintenance velocity and which one your tutorials target. [未验证] |
| pyglet | 未收录 | Choose pyglet when OpenGL-first windowing, multimedia, or light 3D support matters; choose pygame when SDL-backed 2D teaching material and beginner ecosystem matter more. | Pure-Python, OpenGL-based windowing/multimedia library; no SDL dependency, supports 3D via OpenGL, but a smaller teaching community than pygame. |
| Arcade | 未收录 | Choose Arcade for a cleaner modern Python 2D API with tilemap and physics helpers; choose pygame when you want the lower-level classic API and larger tutorial base. | Modern Python 2D game library built on OpenGL with a cleaner OO API and built-in tilemap/physics helpers; younger and smaller ecosystem. |
| Godot | 未收录 | Choose Godot when you need an actual engine with editor, scenes, 2D/3D, and asset workflow; choose pygame for small Python-first 2D projects and teaching loops. | A full open-source game *engine* (editor, scenes, 2D+3D, GDScript/C#); vastly more capable but a whole different tool to learn — overkill for "draw a rect and move it." |
| Raylib (+ python bindings) | 未收录 | Choose Raylib when a simple C game library with multi-language bindings fits better; choose pygame when Python tutorial gravity and SDL-style 2D workflows are the deciding factors. | Simple C game library with bindings for many languages; very approachable, but a different ecosystem and less Python-tutorial gravity than pygame. |

## Tech stack

- **Core language:** C (the extension modules) wrapping **SDL** for windowing, input, and rendering, with a Python API on top. [推断]
- **Backends/libraries:** SDL plus its companion libs for image (SDL_image), audio mixing (SDL_mixer), and fonts (SDL_ttf/freetype); the repo bundles licenses for FLAC, Ogg/Vorbis, Opus, PNG, JPEG, freetype, portmidi, and more.
- **Distribution:** prebuilt wheels on PyPI for common platforms (so `pip install pygame` needs no compiler in the usual case), plus source builds.
- **API surface:** display/surface blitting, event queue, image/font/mixer modules, `sprite` groups + collision helpers, `time.Clock` for frame pacing.

## Dependencies

- **Runtime:** a CPython interpreter; on most platforms the PyPI wheel bundles the SDL stack so there's no separate system install.
- **System libs (source builds):** SDL2 and its companion dev libraries (image/mixer/ttf) when compiling from source rather than installing a wheel.
- **Build:** a C toolchain + the SDL dev headers to build from source; not needed when a matching wheel exists.

## Ops difficulty

**Low — it's a client-side library, nothing to operate.** For users, `pip install pygame` is the whole setup on supported platforms thanks to wheels; you run your game as a normal Python script. "Difficulty" only shows up at the edges: building from source against the right SDL versions, packaging a game for distribution (PyInstaller and friends), or targeting web/mobile, which are off the well-paved path. There is no server, datastore, or deployment surface.

## Health & viability

- **Responsiveness**: Grade C — median first-response time 460.0 hours across 3 qualifying issues/PRs.
- **Maintenance (2026-10): coasting.** Last releases 2.6.1 (2024-09) and 2.6.0 (2024-06); the last default-branch commits are one batch of merges on 2025-10-05 (Python 3.14 Windows build config, docs fixes), nothing since. The radar's maintenance axis fell from B to D on this re-score: a year without commits now outweighs the mature-library allowance. Not archived.
- **Governance / bus factor.** Organization-owned (`pygame`) with a multi-person contributor history (illume/René Dudfield, MyreMylar, Starbuck5, ankith26, and the original authors PeterShinners/llindstrom). The scorer can no longer attribute recent activity (no commits in its window), and much of the active development now happens in the **pygame-ce** fork (`pygame-community/pygame-ce`, pushed 2026-10-06). [推断]
- **Age & Lindy verdict.** This GitHub repo dates to 2017-03 (longevity axis now D, because age only counts while the repo stays active), but **pygame the project is ~25 years old** and still installed ~2.2M times a month — the *API and ecosystem* have a very strong Lindy prior; *this distribution's* release line no longer does. If you want the Lindy bet with live maintenance, pygame-ce inherits the same API.
- **Adoption.** Grade A — 2,217,050 monthly PyPI downloads and 17,300 dependent repos; ubiquitous in tutorials and courses.
- **Risk flags.** The split with **pygame-ce** is the main thing to weigh: same import name, diverging release lines. LGPL-2.1 per README (GitHub reports no SPDX id, so the radar's license axis is unscored).

## Caveats (unverified)

- [未验证] License: README states GNU **LGPL v2.1** (file `docs/LGPL.txt`) and explicitly reserves the right to relicense future versions; GitHub's API reported no SPDX id, so LGPL-2.1 is taken from the README/LICENSE file, not the API badge.
- [未验证] ~9.0k stars as of 2026-10 (4126 forks, 777 open issues as of 2026-06) — volatile, date-sensitive.
- [未验证] pygame-ce's activity (pushed 2026-10-06, PyPI 2.5.8) was checked on 2026-10-08; its degree of API compatibility, its newer-SDL support, and the claim that it keeps the `pygame` import name (so the two packages clash in one environment) come from community knowledge, not from its README or a code comparison.
- [未验证] True project age (~25 years, early-2000s origin) far exceeds the GitHub repo's 2017 `created_at`; the Lindy verdict relies on the older origin, which is not asserted from this repo's metadata alone.
- [推断] The SDL/SDL_image/SDL_mixer backend split and bundled dependency licenses are inferred from the repo's `docs/licenses` tree and standard pygame architecture, not a code audit.
- [未验证] Web (pygbag/WASM) and mobile support exist but are not the primary supported path; status changes over time.
