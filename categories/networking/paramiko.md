---
name: Paramiko
slug: paramiko
repo: https://github.com/paramiko/paramiko
category: networking
tags: [ssh, sshv2, sftp, python, networking, crypto, protocol]
language: Python
license: LGPL-2.1
maturity: stable, active, ~9.8k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-05-09T19:58:37Z
  default_branch: main
  default_branch_sha: d60d5c17d78f344b51ed651e796d2931133a9b22
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:43:34Z
  overall: B
  overall_score: 2.83
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 24
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 208.1
        qualifying_issues: 11
        band: default
        window_offset_days: 3
        source: pr
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: paramiko
        dependent_repos_count: 30613
        downloads_last_month: 124717264
        graph_tier: A
        volume_tier: A
        cross_check_divergence: null
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 6442
        last_commit_age_days: 24
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 2
        top1_share: 0.976
        top3_share: 1.0
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: C
      raw:
        spdx_id: LGPL-2.1
        permissiveness: weak_file_copyleft
        relicense_36mo: false
        content_license: null
---

# Paramiko

The leading pure-Python implementation of the SSHv2 protocol — client and server, with SFTP — letting Python code open SSH connections, run remote commands, and transfer files without shelling out to the `ssh` binary.

![paramiko — health radar](../../assets/health/paramiko.svg)

## When to use

You're writing a Python automation tool — a deploy script, a network-device collector, a CI step — that has to log into remote hosts over SSH, run commands, and pull back files. You don't want to `subprocess` the system `ssh` client (fragile quoting, host-key prompts, no structured error handling) and you don't want to depend on a CLI being installed in your container. You `pip install paramiko`, open a `SSHClient`, `connect()` with a key or password, and you have programmatic `exec_command()` returning real stdin/stdout/stderr file objects, plus an `open_sftp()` channel for uploads/downloads — all in-process, with Python exceptions you can catch and retry. When you need fine control — a custom `Transport`, port forwarding, agent forwarding, or even standing up an SSH *server* in Python — Paramiko exposes the protocol layer that higher-level tools sit on top of.

It's also the substrate you inherit indirectly: **Fabric** (remote task execution) and **Ansible**'s SSH connection plugins build on Paramiko, so understanding it pays off when you debug their connection behavior. Reach for Paramiko directly when you want a library, not a framework — the raw SSH/SFTP transport, owned by your code.

## When NOT to use

- **You just need to run a few remote tasks, not implement SSH.** For high-level "run this command on these hosts" workflows, **Fabric** (which wraps Paramiko) is far less boilerplate. Paramiko is the low-level transport; using it directly means managing connections, host keys, and threads yourself.
- **You need maximum throughput / native OpenSSH parity.** Being pure-Python, Paramiko is slower than the C OpenSSH client for bulk SFTP transfers and won't always match every OpenSSH config option, cipher, or `~/.ssh/config` nuance. Heavy file movement may be faster via `rsync`/`scp` over the real client.
- **You depend on a very new crypto algorithm or OpenSSH feature day-one.** Paramiko has historically lagged OpenSSH on some newer key types/algorithms; verify your required KEX/cipher/host-key algorithm is supported in the version you pin. [未验证]
- **LGPL-2.1 is a problem for your distribution model.** Paramiko is **LGPL-2.1**, not the MIT/BSD common to much of the Python ecosystem. For most apps (dynamic linking / pip import) this is fine, but if you statically bundle or have strict license policies, review it. [推断]
- **You want async-native I/O.** Paramiko is threading/blocking-oriented; for asyncio-native SSH, **AsyncSSH** is the purpose-built alternative.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| AsyncSSH | 未收录 | Pick AsyncSSH when your codebase is asyncio-native and you want SSH client/server APIs built around `await`. | asyncio-native SSHv2 client+server, broad modern algorithm support; better fit for async codebases, but a different (await-based) API and smaller ecosystem of dependents. |
| Fabric | 未收录 | Pick Fabric when you need high-level remote task orchestration built on Paramiko. | High-level remote-execution framework built *on* Paramiko; great for task orchestration, but it's a layer above, not a transport library. |
| `subprocess` + system `ssh` | 未收录 | Pick system `ssh` when zero Python dependencies and exact OpenSSH parity matter more than robust Python APIs. | Zero Python deps and full OpenSSH parity, but fragile (text parsing, quoting, host-key prompts) and requires the `ssh` binary present. |
| libssh2 / ssh2-python | 未收录 | Pick libssh2 bindings when transfer speed and a C-backed dependency matter more than Pythonic ergonomics. | C library bindings — faster transfers, but a compiled dependency and a thinner Pythonic API. |
| [`sshtunnel`](sshtunnel.md) | ✅ | Pick sshtunnel when all you need is a thin Paramiko wrapper for port-forwarding tunnels. | A thin Paramiko *wrapper* dedicated to port-forwarding tunnels only — narrower scope, built on the same engine. |

## Tech stack

- **Language:** pure Python (no C extension of its own).
- **Crypto:** relies on the **`cryptography`** package (and via it, OpenSSL) for ciphers, key exchange, and key handling — the actual primitives are native code through that dependency.
- **Protocol surface:** SSHv2 transport, auth (password/publickey/keyboard-interactive/GSS-API), channels, `exec`/`shell`, SFTP subsystem, and an SSH *server* implementation.
- **Concurrency model:** threaded/blocking sockets; each `Transport` runs a background thread.

## Dependencies

- **Runtime:** Python 3 plus the **`cryptography`** library (which pulls in a compiled OpenSSL backend); optionally PyNaCl/bcrypt for certain key formats and `gssapi`/`pyasn1` for GSS-API/Kerberos auth. [推断]
- **External services:** none of its own — you point it at whatever SSH servers you already run.
- **Build/install:** `pip install paramiko`; the only non-pure-Python piece is the `cryptography` wheel's native backend.

## Ops difficulty

**Low (as a library).** There's nothing to deploy — it's `pip install paramiko` inside your application. Operationally the friction is in *usage*: host-key verification policy (don't blindly `AutoAddPolicy` in production), thread/connection lifecycle and cleanup, timeouts and keepalives on long-lived sessions, and pinning a version because the `cryptography` dependency and supported algorithms move over time. Long-running multi-host automation needs your own connection pooling and error handling, since Paramiko gives you the transport, not the orchestration.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 4.0 hours across 5 qualifying issues/PRs.
- **Maintenance (2026-06).** Repo last pushed 2026-05 — **active**, not archived. Releases are published primarily to **PyPI** (the GitHub Releases list is empty here), so cadence is best judged from PyPI/changelog rather than git tags. [未验证]
- **Governance / bus factor.** Under the **`paramiko` organization**, but historically driven overwhelmingly by one maintainer (**bitprophet** / Jeff Forcier, ~2,800 commits vs the next contributor in the hundreds) — a real **bus-factor** consideration despite the org wrapper. [推断]
- **Age & Lindy verdict.** Created **2009**, ~17 years old and **still active** ⇒ a **strong Lindy** signal: it is the de-facto Python SSH library, depended on by Fabric, Ansible, and a large slice of Python infra tooling. [推断]
- **Adoption.** ~9.8k stars, 2k+ forks, and enormous transitive use through downstream tools (Ansible, Fabric, pysftp wrappers) — adoption is not in question. The ~1.2k open issues reflect a huge surface and long history, not abandonment. [未验证]
- **Risk flags.** **LGPL-2.1** (unusual for the ecosystem — review for static-linking/strict-policy distribution) and the single-maintainer concentration are the two things to weigh; no relicense history found. As an SSH/crypto library it is also a security-sensitive dependency — track its advisories and keep `cryptography` current. [推断]

## Caveats (unverified)

- [未验证] ~9.8k stars / ~2,059 forks / ~1,180 open issues as of 2026-06 — counts are date-sensitive, indicative only.
- [未验证] Releases ship to PyPI; the empty GitHub Releases list does **not** mean inactivity — verify the current version and cadence on PyPI/the changelog.
- [推断] Exact transitive dependency set (PyNaCl/bcrypt/gssapi extras) depends on the version and chosen install extras; not pinned here.
- [未验证] Specific newer KEX/cipher/host-key-algorithm support relative to current OpenSSH is version-dependent — confirm against the version you pin.
- [推断] LGPL-2.1 obligations relative to your distribution model are a legal judgment, not asserted here as a blocker.
