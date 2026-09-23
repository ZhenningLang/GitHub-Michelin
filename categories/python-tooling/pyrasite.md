---
name: pyrasite
slug: pyrasite
repo: https://github.com/lmacken/pyrasite
category: python-tooling
tags: [python, debugging, code-injection, introspection, gdb, diagnostics]
language: Python
license: GPL-3.0
maturity: v2.0 (old), low-cadence maintenance (2026-06)
last_verified: 2026-06-28
type: tool
upstream:
  pushed_at: 2025-04-07T02:52:38Z
  default_branch: develop
  default_branch_sha: 61229f0bc2b8356224247e427d7b85f5c8971266
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:56:35Z
  overall: D
  overall_score: 1.0
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
        last_commit_age_days: 534
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: pypi.org
        canonical_package: pyrasite
        dependent_repos_count: 14
        downloads_last_month: 10512
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 5491
        last_commit_age_days: 534
        cohort: tool
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: D
      raw:
        spdx_id: GPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_traffic }
    governance: { reason: unattributable }
---

# pyrasite

A tool to inject arbitrary Python code into a **running** Python process — attach to a live PID via gdb, run diagnostic snippets, dump objects, or open a reverse shell, without restarting the target.

![pyrasite — health radar](../../assets/health/pyrasite.svg)

## When to use

You have a long-running Python process in trouble — a daemon that's leaking memory, a worker that's wedged, a service you can't restart because it holds state you'd lose — and your logs don't tell you what's happening *right now* inside it. You don't want to add print statements and redeploy. With pyrasite you point it at the live PID and inject a snippet that runs *inside that process*: dump the count of live objects by type to find the leak, print the stacks of all threads to see where it's stuck, or drop into an interactive shell that's attached to the running interpreter. You inspect and even nudge a production process in place, then detach and let it keep running.

You reach for it specifically when the alternative — kill and restart with more instrumentation — is unacceptable, and when a normal debugger attach isn't enough because you want to *execute code* in the target's context (walk its object graph, call into its modules, snapshot state). For incident-time introspection of a stuck or leaking Python service, it's a sharp, narrow tool.

## When NOT to use

- **In production without understanding the blast radius.** Injecting code into a live process via gdb can crash it, corrupt state, or trip security controls. This is an incident/diagnostic tool, not routine instrumentation — treat every injection as potentially fatal to the target.
- **On non-Linux / no-gdb environments.** It relies on **gdb** to attach to the process (Linux-centric); on platforms or hardened hosts where ptrace/gdb attach is restricted (`ptrace_scope`, containers, hardened prod), it simply won't work. [未验证]
- **For everyday debugging.** For normal development, `pdb`/`breakpoint()`, `py-spy`, or a profiler are safer and purpose-built. pyrasite is for the case where you can't stop the process.
- **When you need a maintained, fast-moving tool.** The project is largely **dormant** — last real release (2.0) is many years old; it still gets occasional fixes but is not actively developed. Verify it works against your current Python/gdb before relying on it. [未验证]
- **For sampling profiling / flame graphs.** If you want low-overhead "where is my Python spending time," **py-spy** reads the target without injecting code and is the modern, safer choice.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| py-spy | 未收录 | Choose py-spy when observe-only sampling is enough and avoiding code injection is the priority. | Great for "where's the time/why is it stuck," but it cannot run arbitrary code in the target. |
| pyrasite vs gdb + python-gdb | 未收录 | Choose raw gdb plus CPython helpers when you want manual attach/inspect control and can wire the injection yourself. | Pyrasite packages the inject-and-run-snippet workflow; raw gdb is lower-level and more manual. |
| manhole / remote pdb | 未收录 | Choose manhole or remote pdb when you can embed the debug shell ahead of time instead of attaching after the fact. | Cleaner and safer, but no help for an already-wedged process that lacks pre-instrumentation. |
| Austin | 未收录 | Choose Austin when the job is low-overhead frame-stack profiling rather than live code execution. | Observe-only and actively maintained, but a profiling alternative rather than a code injector. |
| reload/restart with logging | 未收录 | Choose restart-plus-logging when preserving live state is less important than staying on the safe operational path. | Safe, but it loses the in-the-moment symptom that pyrasite exists to inspect. |

## Tech stack

- **Language:** Python, driving **gdb** to attach to the target process and execute injected payloads inside the running CPython interpreter. [推断]
- **Mechanism:** uses ptrace/gdb to pause the process, call into it, and run the injected code; ships a payload-running harness and a few canned tools (object dumps, thread stacks, reverse shell).
- **Interfaces:** a CLI (`pyrasite`) plus, historically, a GUI (`pyrasite-gui`) for interactive inspection.
- **Targets:** CPython processes on Linux where gdb attach is permitted.

## Dependencies

- **Runtime:** **gdb** with Python support, plus a CPython interpreter; ptrace must be permitted on the host (kernel `yama/ptrace_scope`, container capabilities).
- **Optional:** GTK/GObject stack for the historical `pyrasite-gui`.
- **Install:** a pip-installable package; the gdb/ptrace prerequisites are the real constraint, not the Python install.

## Ops difficulty

**Medium — not because of deployment, but because of operational risk.** There's nothing to run as a service; you install it and invoke it ad hoc. The difficulty is (1) **environment**: getting gdb attach permitted on the target host (hardened prod and containers often block ptrace), and (2) **risk**: an injection can destabilize or crash the very process you're trying to save, so it demands care and ideally a rehearsal on a non-critical copy. Its age also means you may hit compatibility friction with current Python/gdb versions. It's a precision tool used briefly, not standing infrastructure.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** Repo last pushed 2025-04 with sporadic merge activity (a few PRs in 2025 and 2023), but the last real release tag (**2.0**) is many years old — best read as **low-cadence / near-dormant maintenance**, coasting rather than abandoned. Not archived. [推断]
- **Governance / bus factor.** **User**-owned, single-author project (`lmacken`/Luke Macken) with a handful of occasional contributors — a clear single-maintainer bus-factor risk for a tool of this sensitivity. [推断]
- **Age & Lindy verdict.** Created 2011-09 (~14 years) ⇒ long-lived, but Lindy requires age **× still-active**; here activity is minimal, so the verdict is "venerable but coasting" — it has persisted, but don't read its age as a sign of ongoing investment. [推断]
- **Adoption.** ~2.9k stars reflect long-standing recognition as *the* Python live-injection tool, but mindshare has shifted toward observe-only tools (py-spy) that don't inject; treat stars as historical, not current momentum. [未验证]
- **Risk flags.** **GPL-3.0** copyleft (relevant if you'd vendor/redistribute it); near-dormant maintenance + single maintainer + an inherently dangerous mechanism are the real flags — verify it still works on your stack before depending on it. [推断]

## Caveats (unverified)

- [未验证] ~2.9k stars, 220 forks, 46 open issues as of 2026-06 — volatile, date-sensitive; here likely reflecting historical popularity more than current activity.
- [未验证] The newest release tag is 2.0 (old); recent repo activity is occasional PR merges (2025-04, 2023-10) rather than new releases — "near-dormant" is inferred from that cadence, not a maintainer statement.
- [未验证] gdb/ptrace dependency and Linux-centric attach are inferred from the project's described mechanism; exact requirements (gdb version, `ptrace_scope`, container caps) vary by host and aren't asserted here.
- [推断] The CLI + historical GUI surface and the canned tools (object dumps, thread stacks, reverse shell) are from the project's documented features, not a current-version audit — verify against the latest code.
- [未验证] Compatibility with current CPython and gdb versions is unconfirmed given the project's age; test before relying on it in an incident.
