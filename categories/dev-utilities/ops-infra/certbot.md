---
name: Certbot
slug: certbot
repo: https://github.com/certbot/certbot
category: ops-infra
tags: [tls, ssl, acme, lets-encrypt, certificates, https, automation, nginx, apache]
language: Python
license: Apache-2.0
maturity: "v5.8.0, active, ~33.3k stars (as of 2026-09)"
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-22T03:53:35Z
  default_branch: main
  default_branch_sha: 485649333422392901e7ef891630f0129985df8e
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T05:59:27Z
  overall: A
  overall_score: 3.8
  scored_axes: 5
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 18
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 60.0
        qualifying_issues: 13
        band: relaxed_solo
        window_offset_days: 4
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: certbot-dns-cloudflare
        dependent_repos_count: 41
        downloads_last_month: 476384
        graph_tier: D
        volume_tier: B
        cross_check_divergence: 1.02
        homebrew_installs_90d: 5132
        homebrew_tier: A
        release_downloads: 410837
        release_assets: 487
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 4338
        last_commit_age_days: 18
        cohort: tool
    governance:
      grade: B
      raw:
        active_maintainers_12mo: 22
        top1_share: 0.364
        top3_share: 0.83
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    risk_license: { reason: license_unparsed }
---

# Certbot

The EFF/Let's Encrypt ACME client that obtains and auto-renews free, browser-trusted TLS certificates, with plugins that wire the certs straight into nginx/Apache.

![certbot — health radar](../../../assets/health/certbot.svg)

## When to use

You're a sysadmin standing up HTTPS for a handful of public web servers — a couple of nginx vhosts, an Apache box, maybe a bare TCP service that just needs a cert on disk. You don't want to buy certificates, you don't want them expiring at 2 a.m. on a holiday, and you don't want to hand-edit `ssl_certificate` lines every 90 days. You install Certbot, run `certbot --nginx` (or `--apache`), answer a couple of prompts, and it talks ACME to Let's Encrypt, proves you control the domain via an HTTP-01 or DNS-01 challenge, writes the cert/key under `/etc/letsencrypt/live/`, and rewrites your server config to point at them. Common install methods (snap, distro packages) also pre-install a systemd timer or cron entry that runs `certbot renew` on a schedule — the docs tell you to check with `systemctl list-timers` and wire it up manually if it's missing — and `renew` only touches a certificate once less than a third of its lifetime remains, so a 90-day Let's Encrypt cert silently renews about a month before expiry. The cert that was a manual chore becomes a fire-and-forget piece of the host.

You reach for it specifically when you want the *reference* ACME client — the one EFF maintains, the one every tutorial assumes — with first-class web-server integration and a large set of DNS plugins (Route 53, Cloudflare, Google, etc.) for wildcard certs that need DNS-01. If your hosts already run Python and you value the official, batteries-included path over a minimal shell script, Certbot is the default.

## How it works

Certbot automates the whole ACME dance (the certificate-authority protocol standardized in RFC 8555) against Let's Encrypt by default: it generates the private key *locally on your box*, creates an order with the CA, then proves you control each domain by answering a challenge — HTTP-01 (drop a token file the CA can fetch on port 80), DNS-01 (publish a TXT record via a provider plugin), or TLS-ALPN-01 — and finally downloads the signed cert. The web-server plugins do one more thing a bare ACME client doesn't: the `--nginx`/`--apache` installer parses the server's own config, points it at the key and cert under `/etc/letsencrypt/live/`, reloads the server, and can wire up an http→https redirect. Every issuance is recorded as a per-certificate *renewal configuration* on disk, so a later `certbot renew` replays the same authenticator/options without prompts — that is what a timer can run unattended. What stays yours: keeping port 80 (or DNS API credentials) reachable, the reload/distribution *hooks* if anything unusual must happen after renewal, and staying inside Let's Encrypt's rate limits. Current releases default to ECDSA keys (RSA still selectable).

![Certbot — backbone user story](../../../assets/flow/certbot.svg)

<!-- flow-steps:begin (generated from flows/certbot.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install Certbot on the web server — `sudo snap install --classic certbot`
2. **You**: Run it against your web server — `sudo certbot --nginx`
3. **Certbot**: Generates the key locally, orders via ACME, proves domain control over HTTP-01 — component: `nginx plugin`
4. **Certbot**: Saves the cert/key and rewrites the server config to serve HTTPS — `/etc/letsencrypt/live/`
5. **Certbot**: A timer runs certbot renew, which replays each cert's saved config near expiry — `certbot renew` — component: `renew timer (systemd/cron)`

**Value**: Free, browser-trusted HTTPS that renews itself — no expiry incident, no hand-edited cert paths

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You want minimal footprint.** Certbot is a heavyweight Python client with its own venv/dependency tree. If you just need a cert on a constrained box, a tiny single-file client — [acme.sh](#comparison) (pure shell) or [lego](#comparison) (single Go binary) — is far lighter and has no Python runtime to drag along.
- **Your reverse proxy already does ACME.** Caddy issues and renews certs automatically out of the box, and Traefik has built-in ACME; if you're fronting everything with one of those, a separate Certbot is redundant. [推断]
- **You need an internal/private CA.** Certbot speaks ACME to public CAs (Let's Encrypt by default). For internal PKI / private CA issuance you want step-ca/smallstep or your CA's own tooling — Let's Encrypt won't issue for private or non-public-DNS names.
- **You'll hit Let's Encrypt rate limits.** Mass issuance (many subdomains, frequent re-issue, CI churn) runs into per-domain/per-account weekly limits; plan certs (and the staging environment for testing) accordingly — this is a Let's Encrypt constraint, not a Certbot bug. [未验证]
- **You dislike the plugin coupling.** The `--nginx`/`--apache` installers parse and rewrite your server config; on unusual or templated configs they can misedit or fail, and many operators prefer `certonly` (just fetch the cert) plus their own config management instead.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| acme.sh | 未收录 | Pick acme.sh when you want a pure-shell ACME client with a tiny footprint and many DNS APIs. | Pure-shell ACME client, zero language runtime, tiny footprint, huge DNS-API list; less "official," no config-rewriting nginx/apache installer — you wire the cert in yourself. |
| lego | 未收录 | Pick lego when you need a static Go binary or embeddable Go ACME library with broad DNS support. | Single static Go binary, ACME client + Go library, broad DNS provider support; great for embedding/automation, but no web-server config installer. |
| Caddy (automatic HTTPS) | 未收录 | Pick Caddy when adopting a web server that handles ACME automatically is acceptable. | A web server that *is* the ACME client — issues/renews transparently with no separate tool; replaces Certbot only if you also adopt Caddy as your server. |
| dehydrated | 未收录 | Pick dehydrated when you want a minimal hook-driven Bash ACME client and accept more DIY wiring. | Minimal Bash ACME client (formerly letsencrypt.sh); hook-driven, lightweight, but more DIY and a smaller ecosystem than Certbot. |

## Tech stack

- **Language:** Python — distributed as a CLI plus a set of plugin packages.
- **Protocol:** ACME (RFC 8555) against Let's Encrypt by default; supports HTTP-01, DNS-01, and TLS-ALPN-01 challenges. Default key type is ECDSA; RSA remains selectable (README, 2026-09).
- **Plugins:** authenticator/installer plugins for nginx (0.8.48+) and Apache (2.4+) per the README's support list, a `webroot`/`standalone` authenticator, and a family of `certbot-dns-*` plugins (Route 53, Cloudflare, Google, DigitalOcean, …) for DNS-01.
- **On-disk layout:** certs/keys/account state under `/etc/letsencrypt`; renewal config per-cert so `certbot renew` is stateless to invoke.

## Dependencies

- **Runtime:** a Python interpreter and Certbot's dependency tree (cryptography, requests, the ACME library, etc.) — heavier than the single-binary alternatives. The exact minimum Python version tracks the project's current support policy and shifts over time. [未验证]
- **A web server (for the installer plugins):** nginx or Apache if you use `--nginx`/`--apache`; otherwise none — `certonly` just writes cert files.
- **Network + a public CA:** outbound access to the ACME directory (Let's Encrypt) and a domain whose control you can prove via HTTP-01 (port 80 reachable) or DNS-01 (DNS API credentials).
- **Install paths:** the official `certbot.eff.org` interactive guide generates per-OS instructions — distro packages (most distros), the official `snap`, `pip`, and Docker images.

## Ops difficulty

**Low** for the common case. Install, run `certbot --nginx`, and (on most install methods) the renewal timer is set up for you — verify once with `systemctl list-timers`; day-to-day maintenance is essentially nothing — `renew` is automatic and idempotent. Difficulty rises when you leave the happy path: DNS-01/wildcard certs need provider API credentials and the right `certbot-dns-*` plugin (on the snap install path that also needs `sudo snap set certbot trust-plugin-with-root=ok` before `sudo snap install certbot-dns-cloudflare`, per the official instructions); HTTP-01 needs port 80 reachable through firewalls/load balancers; the nginx/apache installer can mis-parse non-standard configs (many shops use `certonly` + their own templating to avoid that); and renewal *hooks* (reload the server, distribute certs to other nodes) are yours to write and test. Across a fleet you'll want config management to deploy Certbot and its renewal hooks consistently rather than hand-tuning each host.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 60.0 hours across 13 qualifying issues/PRs (scorer, 2026-09-28).
- **Maintenance (2026-09).** Last pushed 2026-09; v5.8.0 shipped 2026-09-01 after v5.7.0 (2026-07-21) — a steady ~monthly-to-bimonthly minor cadence, **active**, not coasting. Not archived. [推断]
- **Governance / bus factor.** Owned by an **Organization** and developed in the open by EFF, now under ISRG (Let's Encrypt's nonprofit) stewardship — **nonprofit, team/foundation-backed governance, low bus-factor**. This is the reference client for the CA that issues most of the web's free certs, so it has institutional reasons to stay maintained. [推断]
- **Backing & Lindy.** Created 2014-11 (~12 years) and **still actively shipping** ⇒ a **strong Lindy** signal: a long-lived, battle-proven client, not a hyped newcomer. The nonprofit backing (EFF/ISRG) further lowers abandonment risk versus a single-vendor commercial tool. [推断]
- **License.** Apache-2.0 (read from the LICENSE file; GitHub reports `NOASSERTION` only because the bundled nginx parser carries MIT) — a permissive, foundation-friendly license with **no relicense risk** of the SSPL/AGPL kind. [推断]
- **Adoption.** Near-universal: Certbot is the default ACME client in countless tutorials and distro packages, with broad real-world deployment across the Let's Encrypt ecosystem. [未验证]

## Caveats (unverified)

- [未验证] ~33.3k GitHub stars and v5.8.0 (released 2026-09-01) as of 2026-09-28 — star counts and version numbers are date-sensitive; treat as indicative.
- [推断] GitHub's license API returns `NOASSERTION`; the actual project license is Apache-2.0 per the LICENSE file (the `NOASSERTION` is because the bundled nginx parser is MIT). Verified by reading the file, but flagged because the API badge disagrees.
- [未验证] Let's Encrypt rate limits (per-domain/per-account, weekly issuance) are a CA-side policy that changes over time — check current limits before bulk issuance; not a Certbot-imposed limit.
- [未验证] Minimum supported Python version tracks Certbot's current support policy and moves over time; not asserting a specific number.
- [推断] "Caddy/Traefik make it redundant" and "the nginx/apache installer can mis-edit configs" are operational inferences from how those tools work, not measured claims about a specific config.
