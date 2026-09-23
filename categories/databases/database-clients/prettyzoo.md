---
name: PrettyZoo
slug: prettyzoo
repo: https://github.com/vran-dev/PrettyZoo
category: database-clients
tags: [zookeeper, gui, desktop, javafx, client, archived]
language: Java
license: Apache-2.0
maturity: v2.1.1 (2023-02), ARCHIVED — maintenance stopped, 3.2k stars (as of 2026-06)
last_verified: 2026-06-28
type: app
upstream:
  pushed_at: 2024-01-09T14:17:44Z
  default_branch: master
  default_branch_sha: 03d08cadac2b2080a1e61585cb6a5e9b8ed78dbb
  archived: true
health:
  schema: 1
  computed_at: 2026-09-22T17:42:29Z
  overall: D
  overall_score: 1.2
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
        last_commit_age_days: 987
        active_weeks_13: 0
        carve_out: null
    responsiveness:
      grade: E
      raw:
        median_ttfr_hours: null
        qualifying_issues: 0
        band: relaxed_solo
        window_offset_days: 8
    adoption:
      grade: C
      raw:
        registry: null
        canonical_package: null
        release_downloads: 147579
        release_assets: 123
        release_tier: C
        signal_basis: releases
        archived: true
    longevity:
      grade: E
      raw:
        repo_age_days: 2552
        last_commit_age_days: 987
        cohort: app
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    governance: { reason: unattributable }
---

# PrettyZoo

A cross-platform desktop GUI for Apache ZooKeeper (Win/Mac/Linux) — browse the znode tree, view/edit node data, manage ACLs and connections, without dropping into the `zkCli.sh` shell. **Archived: the author publicly announced in 2023 that maintenance has stopped.**

![prettyzoo — health radar](../../../assets/health/prettyzoo.svg)

## When to use

You're a backend or platform engineer operating systems that lean on ZooKeeper — Kafka, HBase, a Dubbo/legacy service registry, or a Curator-based coordination layer — and you need to *look at and poke* the znode tree without memorizing `zkCli.sh` commands. You want to expand the hierarchy visually, read a node's data, check the children under `/services`, fix a stale config value, and inspect ACLs. You launch PrettyZoo, save your cluster connections, and click through the tree in a JavaFX desktop app — far friendlier for debugging and one-off edits than typing `get`/`ls`/`set` at a CLI, especially when onboarding someone or eyeballing a misbehaving registry.

It's most useful as a **developer/operator convenience GUI** for inspection and light editing during development and incident triage — the "I just need to see what's in ZooKeeper right now" tool.

## When NOT to use

- **It's archived — no future fixes.** The author announced end of maintenance (2023) and the repo is archived; bugs, OS-compatibility breakage (new macOS/JDK), and security issues won't be patched upstream. For ongoing reliance, factor in fork-or-replace. [推断]
- **Production automation / scripting.** A GUI is for humans; for repeatable ops, config-as-code, or CI you want `zkCli.sh`, the ZooKeeper APIs, or Curator — not click-ops in a desktop app.
- **You don't run ZooKeeper at all.** Many stacks have moved coordination off ZooKeeper (Kafka KRaft removes the ZK dependency; etcd/Consul elsewhere). If you're not on ZooKeeper, this tool has no job.
- **Locked-down / headless environments.** A desktop JavaFX app needs a GUI session; for servers, bastions, or headless clusters you'll be back to the CLI anyway.
- **You need fine-grained auditing/RBAC over who changed what.** It's a single-user desktop client; it doesn't provide governance, audit trails, or multi-user access control over ZooKeeper changes.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| `zkCli.sh` (built-in) | 未收录 | Choose zkCli.sh when you need the always-available scriptable ZooKeeper client. | Ships with ZooKeeper, scriptable, always available — but raw CLI, no tree visualization, slower for browsing/onboarding. |
| ZooInspector | 未收录 | Choose ZooInspector when you need the classic Swing-based ZooKeeper GUI. | The classic Swing-based ZK GUI; older and clunkier UI, but historically the reference desktop inspector. |
| zkui / zk-web | 未收录 | Choose zkui or zk-web when you need a web-based multi-user ZooKeeper UI. | Web-based ZooKeeper UIs (deploy as a service, multi-user) rather than a desktop app; different deployment model. |
| Apache Curator | 未收录 | Choose Apache Curator when you need a Java client library for programmatic ZooKeeper access. | A Java client *library* for programmatic ZK access (recipes, leader election) — for building, not for ad-hoc GUI inspection. |
| Kafka KRaft / etcd | 未收录 | Choose Kafka KRaft or etcd when the strategic answer is removing ZooKeeper from the stack. | The strategic alternative: remove ZooKeeper from your stack entirely, making a ZK GUI moot. |

## Tech stack

- **Language:** Java, with a **JavaFX** desktop UI.
- **ZooKeeper client:** built on a ZooKeeper Java client (likely Apache Curator) for connection/znode operations.
- **Packaging:** native installers for Windows / macOS / Linux published as GitHub releases (last v2.1.1, 2023-02).
- **Form factor:** a standalone desktop application — no server component.

## Dependencies

- **A reachable ZooKeeper ensemble** to connect to (it's a client; it manages nothing itself).
- **A desktop OS + GUI session** (Win/Mac/Linux); a bundled or system JRE/JavaFX runtime depending on the installer you use.
- **No datastore, no service** — connection profiles are stored locally on your machine.
- **Compatibility caveat:** since it's archived at 2023-era builds, newer JDK/macOS versions may need a compatible JRE or may not run cleanly. [未验证]

## Ops difficulty

**Very low to run — but unmaintained.** As a desktop client there's nothing to deploy or operate: install the binary, add a connection, click around. The only "ops" concern is the **archival risk** — on a new OS or JDK the 2023 build may not launch, and there's no upstream to fix it. For occasional inspection that's tolerable; for a tool your team depends on daily, the lack of maintenance is the real cost, pushing you toward a maintained alternative or a fork.

## Health & viability

- **Responsiveness**: Grade E.
- **Maintenance (2026-06).** **Archived / abandoned.** The author posted an explicit "I have decided to stop maintaining the project" notice; repo is archived, last release v2.1.1 (2023-02), last push 2024-01, 0 open issues (closed out on archival). [推断]
- **Governance / bus factor.** A **single-author** project (vran-dev, `owner.type: User`) that has now ended — bus factor is effectively zero going forward; any future life depends on community forks. [推断]
- **Age & Lindy verdict.** Created 2019-09 (~6 years) **but no longer maintained** ⇒ Lindy **does not** apply — it had a solid run, but an abandoned repo's age is not a durability signal. [推断]
- **Adoption.** 3.2k stars, ~378 forks — it was a popular, well-liked ZK GUI in its active years (the README thanks its users on archival); the stars reflect past, not ongoing, momentum. [未验证]
- **Risk flags.** Abandonment is the dominant flag. Apache-2.0 license is clean and permissive, which at least makes forking/continuing it legally easy for anyone who wants to. [推断]

## Caveats (unverified)

- [未验证] Stars ~3.2k, forks ~378 as of 2026-06 — volatile, indicative only; 0 open issues reflects archival, not active triage.
- [未验证] JavaFX UI and Curator-based client are inferred from the project's nature and ecosystem norms, not re-confirmed from the current source for this entry.
- [未验证] Whether the 2023-era release runs cleanly on current macOS/JDK versions was not tested; treat OS/JDK compatibility as unverified.
- [推断] "Single author / bus factor zero" is inferred from `owner.type: User` plus the author's own maintenance-ended notice.
