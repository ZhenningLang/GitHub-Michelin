---
name: sshtunnel
slug: sshtunnel
repo: https://github.com/pahaz/sshtunnel
category: networking
tags: [ssh, port-forwarding, tunnel, python, paramiko, networking]
language: Python
license: MIT
maturity: v0.4.0 (last release 2021), low activity, ~1.3k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2025-08-27T14:29:08Z
  default_branch: master
  default_branch_sha: dc0732884379a19a21bf7a49650d0708519ec54f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:43:44Z
  overall: B
  overall_score: 2.5
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
        last_commit_age_days: 391
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: sshtunnel
        dependent_repos_count: 1287
        downloads_last_month: 17633341
        graph_tier: B
        volume_tier: A
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: D
      raw:
        repo_age_days: 4486
        last_commit_age_days: 391
        cohort: library
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
    responsiveness: { reason: no_window_signal }
    governance: { reason: unattributable }
---

# sshtunnel

A small Python library (and CLI) that wraps Paramiko to give you SSH port-forwarding tunnels as a context manager — `with SSHTunnelForwarder(...) as t:` opens a local port that bridges, through an SSH bastion, to a service you can't reach directly.

![sshtunnel — health radar](../../assets/health/sshtunnel.svg)

## When to use

You're writing a Python script that needs to talk to a Postgres (or Redis, or an internal HTTP API) that lives inside a private network, reachable only by SSH through a bastion host. Doing this by hand means spawning `ssh -L 5432:db.internal:5432 bastion` in a subprocess and racing to know when the tunnel is up. Instead you wrap it: `with SSHTunnelForwarder(('bastion', 22), ssh_username=..., remote_bind_address=('db.internal', 5432)) as tunnel:` and then point your DB client at `127.0.0.1:tunnel.local_bind_port`. The tunnel opens on `__enter__`, tears down on `__exit__`, and you get the bound local port programmatically — no subprocess parsing, no leaked `ssh` processes, all inside your Python process and exception handling. It's the clean way to script "reach a private service via a jump host" without reimplementing port forwarding on Paramiko yourself.

It shines for throwaway automation and data scripts: a one-off migration that must hit a DB behind a bastion, a notebook pulling from an internal service, or a small daemon that needs a persistent forwarded port with start/stop control.

## When NOT to use

- **Production-grade, long-lived, high-throughput tunnels.** It's a convenience wrapper over Paramiko's (pure-Python, threaded) forwarding — fine for scripts, but for durable production tunneling, native `ssh -L`/`autossh`, or a real SSH-config-managed setup is more robust and faster.
- **You need OpenSSH config fidelity.** It won't honor your full `~/.ssh/config` (ProxyJump chains, match blocks, every option) the way the OpenSSH client does; complex multi-hop setups are easier with native `ssh`.
- **You already use Paramiko directly.** If your code is already managing a Paramiko `Transport`, adding `sshtunnel` is another layer for something Paramiko can do via `Transport.open_channel('direct-tcpip', ...)` — weigh the dependency.
- **You want active, current maintenance.** The last release is **0.4.0 (Jan 2021)**; the repo still gets occasional commits (last push 2025-08) but the cadence is slow — pin it and test against your Python/Paramiko versions. [未验证]
- **Reverse tunnels / SOCKS proxying as a primary need.** Its sweet spot is local→remote forwarding through a bastion; for general SOCKS or heavy reverse-forwarding, reach for purpose-built tooling.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Paramiko](paramiko.md) | ✅ | Choose Paramiko directly when you need full SSH/SFTP/transport control rather than sshtunnel's forwarding convenience wrapper. | Same engine underneath, but you implement forwarding and lifecycle ergonomics yourself. |
| native `ssh -L` / `autossh` | 未收录 | Choose native OpenSSH or autossh for durable tunnels that need config fidelity, speed, and optional auto-reconnect. | More robust for production, but managed as a process rather than an in-Python object. |
| `subprocess` + `ssh` | 未收录 | Choose `subprocess` plus `ssh` when zero Python dependencies are worth managing process readiness yourself. | Keeps OpenSSH behavior, but you own text parsing, child lifecycle, and failure handling. |
| AsyncSSH (forwarding API) | 未收录 | Choose AsyncSSH when the codebase is asyncio-native and SSH forwarding should live inside the event loop. | Different API and heavier than a thin Paramiko wrapper, but a better fit for async applications. |

## Tech stack

- **Language:** pure Python.
- **Core dependency:** **Paramiko** does the actual SSH transport and channel forwarding; sshtunnel adds the `SSHTunnelForwarder` object, threading, lifecycle, and a CLI.
- **API surface:** a context-manager / start-stop object exposing the bound local address/port, plus a `sshtunnel` command-line entry point.
- **Concurrency:** threaded, following Paramiko's blocking model — one (or more) forwarded channels managed by background threads.

## Dependencies

- **Runtime:** Python 3 and **Paramiko** (which in turn pulls in `cryptography`/OpenSSL). [推断]
- **External:** an SSH server / bastion you can authenticate to, and the target service reachable from that bastion — sshtunnel runs nothing of its own server-side.
- **Install:** `pip install sshtunnel`.

## Ops difficulty

**Low (as a library).** Nothing to deploy — `pip install` and use the context manager. The operational care is around reliability and auth: tunnels can drop on network blips (no built-in reconnection like `autossh`), so long-lived use needs your own keepalive/retry; credentials/keys must be handled safely; and because it sits on Paramiko, you inherit Paramiko's host-key policy and version-pinning concerns. For short scripts it's nearly zero-ops; for anything persistent, plan for reconnection and monitoring yourself.

## Health & viability

- **Responsiveness**: Cannot be scored — no_traffic.
- **Maintenance (2026-06).** Last tagged release **0.4.0 (Jan 2021)**; repo last pushed 2025-08 — **low activity / coasting** but not archived. Mature and small enough that "done" is plausible, but don't expect rapid fixes. [未验证]
- **Governance / bus factor.** Owned by an individual (**pahaz**, ~271 commits) with one substantial co-contributor (fernandezcuesta, ~142) — a **thin bus factor**; it's a single-author utility library. [推断]
- **Age & Lindy verdict.** Created **2014**, ~12 years old; the wrapper is thin and stable, so age + a small stable API is a *moderate* Lindy signal — but its health is really tied to **Paramiko's** continued maintenance underneath. [推断]
- **Adoption.** ~1.3k stars and broad use in data/automation scripts where a quick bastion tunnel is needed; widely referenced in tutorials for "connect to DB behind a jump host from Python." [未验证]
- **Risk flags.** MIT, no relicense history. Main risks: slow maintenance cadence and full dependence on Paramiko (its security advisories and version drift propagate here). [推断]

## Caveats (unverified)

- [未验证] ~1.3k stars / ~202 forks / ~81 open issues as of 2026-06 — date-sensitive, indicative only.
- [未验证] Last release 0.4.0 dated Jan 2021; whether newer fixes ship only as unreleased commits is not confirmed — check the repo before pinning.
- [推断] Exact transitive deps (Paramiko → cryptography, etc.) depend on the installed Paramiko version.
- [未验证] Behavior with complex multi-hop / ProxyJump setups and full `~/.ssh/config` parity is not verified — native `ssh` is the safer bet there.
- [推断] No built-in auto-reconnect; persistent-tunnel reliability depends on your own retry layer (inference from its scope as a thin wrapper).
