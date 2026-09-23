---
name: Cockpit
slug: cockpit
repo: https://github.com/cockpit-project/cockpit
category: ops-infra
tags: [server-admin, web-ui, linux, systemd, self-hosting, sysadmin]
language: JavaScript
license: LGPL-2.1-or-later
maturity: release 364, active (2026-06)
last_verified: 2026-06-26
type: app
upstream:
  pushed_at: 2026-06-29T10:04:42Z
  default_branch: main
  default_branch_sha: 262565fb117b9b05765580256f5665b36a4449e2
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:12:18Z
  overall: D
  overall_score: 2.67
  scored_axes: 6
  applicable_axes: 6
  capped: true
  cap_reason: "source-available/no-license: NONE"
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 52.6
        qualifying_issues: 43
        band: relaxed_solo
        window_offset_days: 6
        source: issue
        inferred: false
    adoption:
      grade: D
      raw:
        registry: proxy.golang.org
        canonical_package: github.com/cockpit-project/cockpit
        dependent_repos_count: 1
        downloads_last_month: null
        graph_tier: D
        volume_tier: "?"
        cross_check_divergence: null
        release_downloads: 19080
        release_assets: 121
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 4708
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 27
        top1_share: 0.426
        top3_share: 0.718
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: E
      raw:
        spdx_id: NONE
        permissiveness: source_available
        relicense_36mo: false
        content_license: null
---

# Cockpit

A web-based graphical admin interface for Linux servers — log in through a browser and manage services, storage, networking, containers, accounts and logs from a real `systemd` session, with no agent or persistent daemon to babysit.

![cockpit — health radar](../../../assets/health/cockpit.svg)

## When to use

You're a sysadmin (or a developer who just inherited an Ubuntu/Fedora/RHEL box) and you need to do real maintenance — restart a stuck service, see why the disk filled up, add a user, check the journal after a crash, attach a new block device — but you don't want to memorize a dozen CLI incantations or hand the keys to a heavyweight config-management stack. You install one package, open `https://server:9090`, and log in with the machine's own Linux credentials. Cockpit drops you into a live session: it shells out to `systemd`, `NetworkManager`, `udisks`, `podman` and the journal on your behalf, so what you see is the actual OS state, not a cached model. Change something in the UI and it changes on the box; change it on the command line and the UI reflects it — there's no separate database to drift out of sync.

It shines when you have a handful of servers and want a low-ceremony pane of glass, or when you're onboarding someone who's comfortable with Linux concepts but not yet fluent at the shell. From one Cockpit you can add other machines over SSH and switch between them, and because it's just a browser front-end over standard system APIs, you can uninstall it tomorrow and lose nothing — your servers were never reconfigured to depend on it.

## When NOT to use

- **Fleet-scale orchestration.** Cockpit is per-host administration with optional manual SSH hopping between boxes; it is not a fleet controller. For tens or hundreds of nodes you want Ansible, Salt, Puppet, or a Kubernetes control plane — declarative, version-controlled, repeatable. Clicking through Cockpit on each host does not scale and leaves no audit trail.
- **You need infrastructure-as-code / reproducibility.** UI-driven changes aren't captured in git. If your standard is "every change is a reviewed commit," a point-and-click admin panel works against you.
- **Non-Linux or non-systemd hosts.** Cockpit targets modern Linux with `systemd`; it is not for Windows Server, macOS, or legacy SysV-init boxes. [推断] BSDs are out of scope.
- **You want a hosted control panel for web hosting / multi-tenant billing.** That's the cPanel / Plesk / Webmin lane (vhosts, mail, DNS, reseller accounts). Cockpit is OS administration, not a hosting business panel.
- **Exposing it raw to the public internet.** It's a privileged root-capable surface bound to port 9090; running it unfirewalled with password auth is a liability. Treat it as an internal/VPN tool.
- **Headless automation.** There's no first-class declarative API for scripting bulk changes; the interface is the human UI. Reach for the underlying CLIs/APIs instead.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Webmin | 未收录 | Choose Webmin when you need an older, broader Perl-based control panel across many services and init systems. | Older, broader Perl-based control panel covering many services (mail, DNS, Apache, BIND) on multiple init systems; heavier and less "live session" — Cockpit is leaner, systemd-native, and reflects real-time OS state. |
| cPanel / Plesk | 未收录 | Choose cPanel / Plesk when you need commercial web-hosting control panels for vhosts, mail, billing, and reseller accounts. | Commercial web-hosting control panels (vhosts, mail, billing, reseller accounts); different problem — managed hosting, not bare OS administration. Proprietary and paid. |
| Ansible / Salt / Puppet | 未收录 | Choose Ansible, Salt, or Puppet when you need declarative fleet configuration with version control and idempotency. | Declarative, agentless (Ansible) or agent-based config management for fleets with version control and idempotency; the right tool at scale, but no live interactive UI for ad-hoc one-host triage. |
| Portainer | 未收录 | Choose Portainer when the job is specifically Docker/Kubernetes container management through a web UI. | Web UI focused specifically on Docker/Kubernetes container management; Cockpit's container view (Podman) is one tab among many, not the whole product. |
| Grafana + Prometheus | 未收录 | Choose Grafana + Prometheus when you need observability dashboards for metrics and alerts across a fleet. | Observability dashboards for metrics/alerting across a fleet; read-mostly monitoring, whereas Cockpit is hands-on administration of a single host. |
| [DevToys](../data-tools/devtoys.md) | ✅ | Choose DevToys when you need a developer's offline format/encode/convert toolbox on the desktop. | A developer's offline format/encode/convert toolbox on the desktop — unrelated problem; listed only because it shares this category, not a substitute. |

## Tech stack

- **Frontend:** JavaScript / TypeScript single-page UI (React, PatternFly design system), served by Cockpit's own web server.
- **Web server / session:** `cockpit-ws` (C) terminates HTTPS and authenticates; `cockpit-bridge` runs inside the user's Linux session and speaks D-Bus / runs commands on their behalf.
- **System integration:** talks to `systemd`, `NetworkManager`, `udisks2`/`storaged`, `podman`, `firewalld`, the `journal`, PAM/`sssd` for auth — mostly over D-Bus.
- **Backend glue:** C for the privileged bridge/ws core; Python for several APIs and tests; per-page UI modules are largely JS/TS.
- **Packaging:** native distro packages (`cockpit`, plus optional `cockpit-podman`, `cockpit-machines`, `cockpit-storaged`, etc.); also a Flatpak "Cockpit Client" for connecting out to remote hosts.

## Dependencies

- **OS:** a modern Linux distribution with `systemd` (Fedora, RHEL/CentOS Stream, Debian, Ubuntu, Arch, openSUSE and others ship it). [推断] No Windows/macOS support.
- **Runtime:** `systemd`, D-Bus, a PAM stack for login; `NetworkManager` for the networking page, `udisks2` for storage, `podman` for containers, `libvirt` (via `cockpit-machines`) for VMs — each optional add-on page pulls its own backend.
- **Client:** any modern web browser; no client install required (the Flatpak client is optional, for SSH-based remote connection).
- **Network:** listens on TCP 9090 (HTTPS) by default; SSH for managing additional remote machines.
- **Install:** `apt/dnf/pacman install cockpit` then `systemctl enable --now cockpit.socket` — it's socket-activated, so it consumes no resources until someone connects.

## Ops difficulty

**Low.** Installation is one package plus enabling a socket; it's socket-activated so there's no always-on daemon to tune, and it self-updates with the distro. There is essentially no state to back up — Cockpit stores almost nothing of its own and reads live OS state on demand, so removing it is clean. The main operational care is **security exposure**, not maintenance burden: it's a root-capable web surface on 9090, so you must keep it behind a firewall/VPN, front it with a real TLS certificate (it generates a self-signed one by default), and consider stronger auth than passwords. Difficulty rises only when you add many optional pages whose backends (`libvirt`, `podman`, `udisks`) each have their own quirks.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 30.0 hours across 45 qualifying issues/PRs.
- **Maintenance (2026-06):** **active and steady** — rolling integer releases (latest `364`, 2026-06-23) shipped on a frequent cadence; last pushed 2026-06. This is a continuously-released project, not a coasting one. [推断]
- **Governance & bus factor:** `Organization`-owned under `cockpit-project`, effectively **Red Hat-backed** — a vendor with a long Linux-tooling track record and a multi-person team, so low bus-factor risk (org governance, not a solo maintainer). [推断]
- **Age & Lindy (~12yr, created 2013-11):** **old and still active** — a strong Lindy verdict. A decade-plus of continuous releases plus distro-default shipping (Fedora/RHEL/Debian/Ubuntu) is about as safe a longevity bet as this category offers.
- **Adoption/ecosystem:** ships in the default repos of major distros and integrates with standard system APIs (`systemd`/D-Bus/`podman`/`libvirt`); broad real-world deployment. ~14k stars understates reach since it's distributed via packages, not GitHub. [推断]
- **Risk flags:** none structural; the live concern is operational security exposure (root-capable surface on port 9090), not project viability.

## Caveats (unverified)

- [未验证] Latest release is `364`, published 2026-06-23 (per GitHub release metadata); Cockpit uses a rolling integer-version scheme rather than semver, so "364" is a build number, not a stability tier.
- [未验证] Stargazer count ~14.4k as of 2026-06 — GitHub stars are unreliable and date-sensitive; treat as indicative only.
- [未验证] The repo is multi-licensed (LGPL-2.1-or-later for the core, plus GPL-3.0-or-later, BSD-3-Clause, CC-BY-SA-3.0, MIT for various parts, per the README and the `LICENSES/` directory); the frontmatter cites the predominant core license only — check `LICENSES/` for a specific file's terms.
- [未验证] Exact language percentages (JS ~33%, Python ~33%, C ~18%, TS ~9%) are GitHub's linguist estimate and shift over time.
- [推断] Optional add-on pages (machines/podman/storaged) are shipped as separate packages with their own backend dependencies; the precise package split varies by distribution.
- [推断] Cockpit targets systemd-based Linux only; BSD/macOS/Windows and SysV-init systems are out of scope — verify against the project's "running" docs for a given distro.
