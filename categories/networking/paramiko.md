---
name: Paramiko
slug: paramiko
repo: https://github.com/paramiko/paramiko
category: networking
tags: [ssh, sshv2, sftp, python, networking, crypto, protocol]
language: Python
license: LGPL-2.1
maturity: v5.0.0 (2026-05), active, ~9.9k stars (as of 2026-09)
last_verified: 2026-09-28
type: library
upstream:
  pushed_at: 2026-08-29T20:45:26Z
  default_branch: main
  default_branch_sha: 142f593e40ad767c5e3556cbace66dc84589620c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T07:18:47Z
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
        last_commit_age_days: 29
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 265.0
        qualifying_issues: 10
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
        downloads_last_month: 104197516
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 6447
        last_commit_age_days: 29
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

A deploy script has to hop onto two hundred hosts and run `df` — driving the system `ssh` binary through subprocess means quoting hacks, host-key prompts, and stderr text to parse. Paramiko implements SSHv2 directly in Python: `SSHClient.connect()` then `exec_command()` hands you real stdin/stdout/stderr file objects, `open_sftp()` transfers files, and failures come back as Python exceptions you can catch — all in-process, no `ssh` binary required.

![paramiko — health radar](../../assets/health/paramiko.svg)

## When to use

You're writing a Python automation tool — a deploy script, a network-device collector, a CI step — that has to log into remote hosts over SSH, run commands, and pull back files. You don't want to `subprocess` the system `ssh` client (fragile quoting, host-key prompts, no structured error handling) and you don't want to depend on a CLI being installed in your container. You `pip install paramiko`, open a `SSHClient`, `connect()` with a key or password, and you have programmatic `exec_command()` returning real stdin/stdout/stderr file objects, plus an `open_sftp()` channel for uploads/downloads — all in-process, with Python exceptions you can catch and retry. When you need fine control — a custom `Transport`, port forwarding, agent forwarding, or even standing up an SSH *server* in Python — Paramiko exposes the protocol layer that higher-level tools sit on top of.

It's also the substrate you inherit indirectly: the README describes Paramiko as "the foundation for the high-level SSH library Fabric", and Ansible's SSH connection plugins historically used it (current Ansible prefers libssh when available). Understanding Paramiko pays off when you debug their connection behavior. Reach for it directly when you want a library, not a framework — the raw SSH/SFTP transport, owned by your code.

## How it works

Paramiko implements the SSHv2 stack in Python. On `connect()` it performs key exchange — negotiating how traffic is encrypted and verifying the server's host key against your known-hosts data — then authenticates you with a password, key, or agent. Once authenticated, the single TCP connection is multiplexed into **channels** (virtual streams inside one connection): `exec_command()` opens a channel for a remote command and returns file-like objects for its stdin/stdout/stderr; `open_sftp()` opens one running the SFTP subsystem for file transfer. The actual crypto primitives are not Paramiko's own code — they come from the `cryptography` package (native-backed). Each `Transport` runs a background thread, which is where its threading (not asyncio) model comes from. What stays yours: the host-key policy (the default *rejects* unknown keys; `AutoAddPolicy` is an opt-in), connection lifecycle and cleanup, timeouts/keepalives, and any pooling or retry logic across fleets — orchestration like Fabric is a layer you add on top.

![paramiko — backbone user story](../../assets/flow/paramiko.svg)

<!-- flow-steps:begin (generated from flows/paramiko.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the library into your automation tool — `pip install paramiko`
2. **You**: Create a client and load the host keys you already trust — `client = SSHClient() · client.load_system_host_keys()`
3. **You**: Connect to the remote host — `client.connect('ssh.example.com')`
4. **Paramiko**: Exchanges keys, verifies the server's host key, authenticates, multiplexes channels — component: `Transport`
5. **You**: Run the remote command — `stdin, stdout, stderr = client.exec_command('ls -l')`
6. **Paramiko**: Gives back real file objects per stream; failures are Python exceptions you can catch — component: `Channel`

**Value**: Scripted SSH in-process — commands and SFTP without an ssh binary, quoting hacks, or host-key prompts

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You just need to run a few remote tasks, not implement SSH.** Paramiko's own README recommends **Fabric** for "common client use-cases such as running remote shell commands or transferring files" and says direct use of Paramiko is "only intended for users who need advanced/low-level primitives or want to run an in-Python sshd". Paramiko is the low-level transport; using it directly means managing connections, host keys, and threads yourself.
- **You need maximum throughput / native OpenSSH parity.** Being pure-Python, Paramiko is slower than the C OpenSSH client for bulk SFTP transfers and won't always match every OpenSSH config option, cipher, or `~/.ssh/config` nuance. Heavy file movement may be faster via `rsync`/`scp` over the real client.
- **You must keep talking to legacy SSH servers.** The 4.x/5.x majors removed old crypto aggressively: 4.0.0 (2025-08) dropped DSA keys; 5.0.0 (2026-05) dropped SHA-1 RSA signatures (the `"ssh-rsa"` algorithm identifier), SHA-1 key exchange (`diffie-hellman-group1*-sha1`), and GSSAPI — with the changelog explicitly warning this is backwards incompatible and telling you to stay on Paramiko 3.x for hosts you don't control. Old network gear and embedded SSH stacks that only implement those algorithms are unreachable from 5.x.
- **You need a very new crypto algorithm or OpenSSH feature day-one.** Paramiko has historically lagged OpenSSH on newer algorithms — e.g. hybrid post-quantum ML-KEM key exchange merged to `main` on 2026-08-09 but was still unreleased as of 2026-09 (latest release 5.0.0). Verify your required KEX/cipher/host-key algorithm is supported in the version you pin.
- **LGPL-2.1 is a problem for your distribution model.** Paramiko is **LGPL-2.1**, not the MIT/BSD common to much of the Python ecosystem. For most apps (dynamic linking / pip import) this is fine, but if you statically bundle or have strict license policies, review it. [推断]
- **You want async-native I/O.** Paramiko is threading/blocking-oriented; for asyncio-native SSH, **AsyncSSH** is the purpose-built alternative.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| AsyncSSH | 未收录 | Pick AsyncSSH when your codebase is asyncio-native and you want SSH client/server APIs built around `await`. | asyncio-native SSHv2 client+server, broad modern algorithm support; better fit for async codebases, but a different (await-based) API and smaller ecosystem of dependents. |
| Fabric | 未收录 | Pick Fabric when the job is "run this command on these hosts" — Paramiko's own README recommends it for common client use-cases and reserves direct Paramiko use for low-level primitives or an in-Python sshd. | High-level remote-execution framework built *on* Paramiko; great for task orchestration, but it's a layer above, not a transport library. |
| `subprocess` + system `ssh` | 未收录 | Pick system `ssh` when zero Python dependencies and exact OpenSSH parity matter more than robust Python APIs. | Zero Python deps and full OpenSSH parity, but fragile (text parsing, quoting, host-key prompts) and requires the `ssh` binary present. |
| libssh2 / ssh2-python | 未收录 | Pick libssh2 bindings when transfer speed and a C-backed dependency matter more than Pythonic ergonomics. | C library bindings — faster transfers, but a compiled dependency and a thinner Pythonic API. |
| [`sshtunnel`](sshtunnel.md) | ✅ | Pick sshtunnel when all you need is a thin Paramiko wrapper for port-forwarding tunnels. | A thin Paramiko *wrapper* dedicated to port-forwarding tunnels only — narrower scope, built on the same engine. |

## Tech stack

- **Language:** pure Python (no C extension of its own).
- **Crypto:** relies on the **`cryptography`** package (and via it, OpenSSL) for ciphers, key exchange, and key handling — the actual primitives are native code through that dependency.
- **Protocol surface:** SSHv2 transport, auth (password/publickey/keyboard-interactive; GSS-API support was removed in 5.0.0, 2026-05), channels, `exec`/`shell`, SFTP subsystem, and an SSH *server* implementation. Post-quantum ML-KEM hybrid key exchange is merged on `main` (2026-08) but unreleased as of 2026-09.
- **Concurrency model:** threaded/blocking sockets; each `Transport` runs a background thread.

## Dependencies

- **Runtime:** Python **>=3.9** (PyPI metadata for 5.0.0); core install dependencies are **`bcrypt>=3.2`, `cryptography>=3.3`, `invoke>=2.0`, `pynacl>=1.5`** — `invoke` became a core dependency in 4.0.0 (2025-08), and the `[all]`/`[invoke]` extras were removed at the same time. The actual crypto primitives run through `cryptography`'s native (OpenSSL-backed) wheels.
- **External services:** none of its own — you point it at whatever SSH servers you already run.
- **Build/install:** `pip install paramiko`; the only non-pure-Python piece is the native backend behind `cryptography`.

## Ops difficulty

**Low (as a library).** There's nothing to deploy — it's `pip install paramiko` inside your application. Operationally the friction is in *usage*: host-key verification policy (don't blindly `AutoAddPolicy` in production), thread/connection lifecycle and cleanup, timeouts and keepalives on long-lived sessions, and pinning a version because the `cryptography` dependency and supported algorithms move over time. Long-running multi-host automation needs your own connection pooling and error handling, since Paramiko gives you the transport, not the orchestration.

## Health & viability

- **Responsiveness**: Grade C — median first-response time 265.0 hours across 10 qualifying issues/PRs.
- **Maintenance (2026-09).** Repo last pushed 2026-08-29 (GitHub API), **active**, not archived. Releases ship to **PyPI** — the GitHub Releases list is empty (re-confirmed via API), though git tags do exist for recent versions; cadence: 3.5.1 (2025-02) → 4.0.0 (2025-08) → **5.0.0 (2026-05-09)**. The majors are security-forward by design (DSA, SHA-1 signatures/KEX, and GSSAPI removed with changelog warnings), at the cost of upgrade churn.
- **Governance / bus factor.** Under the **`paramiko` organization**, but historically driven overwhelmingly by one maintainer (**bitprophet** / Jeff Forcier) — a real **bus-factor** consideration despite the org wrapper. [推断]
- **Age & Lindy verdict.** Created **2009**, ~17 years old and **still active** ⇒ a **strong Lindy** signal: it is the de-facto Python SSH library, depended on by Fabric and a large slice of Python infra tooling. [推断]
- **Adoption.** ~9.9k stars (9,863, GitHub API 2026-09), ~2,080 forks, and enormous transitive use through downstream tools (Fabric and its ecosystem) — adoption is not in question. The ~1.2k open issues/PRs (API count, 2026-09) reflect a huge surface and long history, not abandonment.
- **Risk flags.** **LGPL-2.1** (unusual for the ecosystem — review for static-linking/strict-policy distribution), the single-maintainer concentration, and the **two majors in ~10 months (4.0, 5.0) that removed legacy crypto** — if you talk to old devices you may be pinned to 3.x indefinitely. As an SSH/crypto library it is also a security-sensitive dependency — track its advisories and keep `cryptography` current. [推断]

## Caveats (unverified)

- [未验证] ~9,863 stars / ~2,080 forks / ~1,199 open issues+PRs as of 2026-09 (GitHub API) — counts are date-sensitive, indicative only; the open-issue figure includes pull requests.
- [推断] The Ansible-vs-libssh nuance (current Ansible may prefer libssh over Paramiko for its `ssh` connection plugin) is from ecosystem familiarity, not re-verified against Ansible docs this pass.
- [推断] Exact behavior differences between staying on 3.x and moving to 4.x/5.x beyond what the changelog lists were not tested hands-on.
- [推断] LGPL-2.1 obligations relative to your distribution model are a legal judgment, not asserted here as a blocker.
- [推断] ML-KEM post-quantum key exchange is confirmed merged on `main` (commits dated 2026-08-09/2026-08-29) but "unreleased" follows from 5.0.0 being PyPI's latest as of 2026-09-28; the next release could change this.
