---
name: memory-analyzer
slug: memory-analyzer
repo: https://github.com/facebookarchive/memory-analyzer
category: python-tooling
tags: [python, memory, debugging, profiling, gdb, introspection, archived]
language: Python
license: MIT
maturity: v0.1.2, ARCHIVED by Meta (read-only), last code push 2021-09 (2026-06)
last_verified: 2026-06-29
type: tool
upstream:
  pushed_at: 2021-09-15T20:30:34Z
  default_branch: main
  default_branch_sha: 9704810d994704761181eafcb816122751ef0fb7
  archived: true
health:
  schema: 1
  computed_at: 2026-09-22T16:56:25Z
  overall: D
  overall_score: 1.0
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: true
        last_commit_age_days: 1833
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: relaxed_solo
        window_offset_days: 9
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: memory-analyzer
        dependent_repos_count: 1
        downloads_last_month: 75
        graph_tier: D
        volume_tier: E
        cross_check_divergence: null
        tier_source: registry
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 2618
        last_commit_age_days: 1833
        cohort: tool
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
    governance: { reason: unattributable }
---

# memory-analyzer

A one-shot tool to inspect the memory of a **running** Python process — it attaches via GDB, pauses the target, and reports per-type object counts, total sizes, and forward/backward reference graphs. **Archived by Meta (read-only) — see Health & viability before relying on it.**

![memory-analyzer — health radar](../../assets/health/memory-analyzer.svg)

## When to use

You're an SRE or backend engineer chasing a memory leak in a long-running Python 3 daemon on Linux. You can't reproduce it locally, you don't want to redeploy with extra instrumentation, and you'd rather not restart the process and lose the in-flight state that's exhibiting the bloat. You find the PID, run `memory_analyzer run $PID`, and it launches GDB against the live interpreter, briefly pauses the process (and all its threads), and drops you into an ncurses UI showing how many objects of each type are alive, their total size, and — on demand — the forward and backward reference chains that are keeping the largest objects pinned. Run it again later against the same PID with `--snapshot` and it diffs the two captures so you can watch which object types are growing over time. For a single point-in-time "what is eating memory inside this live process" snapshot, it does exactly that.

The honest caveat is that this is the *legitimate* use case for a tool that is **no longer maintained**: it was archived by Meta and last saw code changes in 2021, it targets Python 3.6/3.7, and the reference-graph feature still tries to upload PNGs to **Phabricator** (a Meta-internal leftover). Even when it fits, treat it as a borrowed-from-the-attic tool and verify it runs on your interpreter first — or reach for a maintained alternative (see Comparison).

## When NOT to use

- **As a tool you depend on going forward — it is ARCHIVED.** Meta moved it to the `facebookarchive` org; the repo is **read-only**: no fixes, no PRs accepted, no releases. Last code push was **2021-09** (~5 years ago as of 2026-06). Adopting dead tooling for production diagnostics is a standing liability — prefer a maintained substitute.
- **On modern / future Python versions without testing.** It declares `python_requires>=3.6` and only classifies 3.6/3.7 (both now EOL). Nothing has been done to track CPython's evolving object model or GDB integration since 2021, so compatibility with current CPython is unverified and a real risk. [推断]
- **Anywhere you can't get GDB + ptrace.** It launches GDB to attach to the target, so it needs ptrace permitted on the host. On hardened systems you must `echo 0 > /proc/sys/kernel/yama/ptrace_scope` or run as root; in many containers (no `SYS_PTRACE` capability) and on macOS/Windows it won't work cleanly. Its README is explicit that it's Linux/ptrace-centric.
- **For continuous / production memory monitoring.** This is **one-shot snapshot** tooling — it pauses the whole process (and *all threads*) while it walks the heap, and grabbing references is explicitly "a costly operation." It is not a low-overhead continuous profiler; do not run it on a hot path or on a loop.
- **If the Phabricator upload path matters to you.** The reference-graph feature was wired to upload PNGs to Phabricator; outside Meta you rely on the `--no-upload` flag and local PNGs, and that integration is unmaintained. [推断]
- **When you just need allocation tracking inside your own code.** If you control the source, stdlib **tracemalloc** (or memray/Scalene) gives maintained, lower-friction allocation tracking without GDB attach — reach for those first.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [pyrasite](pyrasite.md) | ✅ | Choose pyrasite when you need live-code injection into a Python process rather than a packaged per-type memory snapshot. | Broader and more dangerous: it can run object dumps, thread stacks, or a reverse shell; it is low-cadence but **not archived**. |
| tracemalloc (stdlib) | 未收录 | Choose tracemalloc when you control the code and can instrument allocation tracking from inside the target process. | Built into CPython and maintained, but it cannot attach to an arbitrary already-running PID. |
| memray (Bloomberg) | 未收录 | Choose memray when an actively maintained profiler with flame graphs and live mode matters more than ncurses-style heap snapshots. | Modern Python memory workflow, but you use its launch/attach tooling rather than memory-analyzer's GDB-driven report. |
| Pympler | 未收录 | Choose Pympler when an embedded library for per-type object sizes/counts is enough. | It is one of memory-analyzer's dependencies, but it runs inside code you control rather than acting as an external attach tool. |
| objgraph | 未收录 | Choose objgraph when reference graphs from inside the process are the main diagnostic need. | Useful for chasing what keeps objects alive, but in-process rather than an external GDB attach. |
| guppy3 / heapy, Scalene | 未收录 | Choose guppy3/heapy for in-process heap analysis, or Scalene for maintained CPU/GPU/memory profiling. | Both answer "where is memory going" with maintained tooling, but neither matches memory-analyzer's arbitrary live-PID snapshot niche. |

## Tech stack

- **Language:** Python 3 (CLI entry point `memory_analyzer`), driving **GDB** against the target process.
- **Mechanism:** launches GDB with the interpreter from `sys.executable` (overridable via `-e`), pauses the target PID (all threads), and uses **pympler** + **objgraph** *inside the target* to enumerate live objects, sizes, and forward/backward references.
- **UI:** an **ncurses** terminal UI for browsing per-type counts/sizes and snapshot-diff pages; reference graphs render as PNGs.
- **Output:** binary snapshot files under `memory_analyzer_out/`, re-viewable with `memory_analyzer view <file>`; multi-PID and snapshot-comparison modes.
- **Meta leftover:** reference-graph PNGs were wired to upload to **Phabricator** (suppress with `--no-upload`).

## Dependencies

- **Runtime on the host:** **GDB** and the ability to **ptrace** the target (kernel `yama/ptrace_scope` = 0, or run as root; container `SYS_PTRACE` capability).
- **Frontend packages:** `click`, `attrs`, `jinja2`, `prettytable`, plus `pympler` and `objgraph`.
- **Critically, in the TARGET's library path:** you must install **objgraph** and **pympler** where the analyzed process can import them — the analyzer runs them inside the target, so this is a real prerequisite, not just a frontend dep.
- **Install:** a small pip-installable package (`memory_analyzer`); the GDB/ptrace/host prerequisites are the real constraint, not the pip install.

## Ops difficulty

**Medium — and rising purely because it's unmaintained.** There's nothing to run as a service; you pip-install it and invoke it ad hoc. The friction is (1) **environment**: getting GDB attach permitted (ptrace_scope/root, container capabilities) and installing objgraph+pympler into the *target's* import path; (2) **blast radius**: it pauses the whole process and all threads while it walks the heap, and reference collection is costly — not something to run casually on a busy production process; and (3) **rot**: with no updates since 2021 and a 3.6/3.7 target, you may hit compatibility friction with current CPython/GDB and you're on your own to patch it (against a read-only repo). It's a precision, short-lived tool — but one you'd now be maintaining yourself.

## Health & viability

- **Responsiveness**: Grade E.
- **Archived — the central fact (2026-06).** The repo lives under **`facebookarchive`** and is **`archived: true`** (read-only): no merges, no releases, no fixes. Last code push **2021-09-15**. This is the decisive signal — it is **abandoned**, not merely quiet.
- **Age × still-active = a NEGATIVE Lindy verdict.** Created **2019-07** (~7 years old) but inactive since 2021. Lindy requires age **× still-active**; age alone is not safety. An old-*and-dead* tool fails the test — the years of dormancy are a risk flag, not a durability signal.
- **Governance / bus factor → effectively zero.** Owner is an **Organization** (Meta), but the contributors (`thatch`, `lisroach`, `cooperlees`, all ex/Meta) have moved on and the project is archived — there is no maintainer to escalate to. [推断]
- **Backing org track record.** Meta routinely sunsets and archives OSS into `facebookarchive`; being under that org is itself the deprecation notice. Don't read "Meta-backed" as ongoing support here — the backing has explicitly ended.
- **Adoption.** ~156 stars / ~14 forks (2026-06) — modest recognition, never a large ecosystem; mindshare for Python memory work has since moved to maintained tools (memray, tracemalloc, Scalene). Treat stars as historical. [未验证]
- **Risk flags.** Permissive **MIT** (no license trap), but **abandonment + EOL Python target + GDB/ptrace fragility + a Phabricator-coupled feature** are the real flags. Verdict: use only as a last resort for a one-off, and prefer a maintained alternative.

## Caveats (unverified)

- [未验证] ~156 stars, ~14 forks, 6 open issues as of 2026-06 — volatile and date-sensitive; reflects historical/modest recognition, not current activity (the repo is archived).
- [未验证] Only a single early GitHub release exists (`0.1.0`, "Initial Release", 2019-10); `0.1.1`/`0.1.2` are tags without releases, and `setup.py` carries `version="0.1.2"` with classifier "Development Status :: 1 - Planning" — i.e. it never reached a stable release line.
- [推断] Compatibility with current CPython (post-3.7) and modern GDB is unconfirmed; `python_requires>=3.6` and 3.6/3.7-only classifiers plus no updates since 2021 make incompatibility likely but untested here — verify before use.
- [未验证] Exact GDB/ptrace requirements (GDB version, `ptrace_scope`, container `SYS_PTRACE`) vary by host; the Linux/ptrace-centric constraint is from the README, not a per-environment audit.
- [推断] The Phabricator PNG-upload path and the "install objgraph+pympler in the target's library path" requirement are taken from the README/manifest, not a current-version run — confirm against the code if you proceed.
- [推断] Bus factor "effectively zero" is inferred from the archived status plus the contributor list having moved on, not a maintainer statement.
