---
name: nginx-upload-module
slug: nginx-upload-module
repo: https://github.com/fdintino/nginx-upload-module
category: nginx-modules
tags: [nginx, file-upload, multipart, c-module, web-server]
language: C
license: BSD-3-Clause
maturity: v2.3.0 tag line, low activity (last push 2024-07), ~1.0k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2024-07-17T20:13:04Z
  default_branch: master
  default_branch_sha: 96e64603dc5a588a2d1ae59a62b0019d6b41070c
  archived: false
health:
  schema: 1
  computed_at: 2026-09-22T16:44:22Z
  overall: "?"
  overall_score: null
  scored_axes: 2
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: E
      raw:
        archived: false
        last_commit_age_days: 1189
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
        repo_age_days: 6483
        last_commit_age_days: 1189
        cohort: library
    governance:
      grade: "?"
      raw: {}
    risk_license:
      grade: "?"
      raw: {}
  unknowns:
    responsiveness: { reason: no_traffic }
    adoption: { reason: ambiguous }
    governance: { reason: unattributable }
    risk_license: { reason: license_unparsed }
---

# nginx-upload-module

An NGINX C module that handles `multipart/form-data` (RFC 1867) file uploads at the server edge — NGINX streams the upload to disk itself and passes only the file metadata (paths, names, sizes) to your backend, so your application never has to buffer the raw upload.

![nginx-upload-module — health radar](../../assets/health/nginx-upload-module.svg)

## When to use

You're running an app behind NGINX that accepts large file uploads, and you don't want your application server tying up a worker/thread for minutes while a client dribbles a multi-gigabyte file over a slow connection. You want NGINX — which is already great at slow-client I/O — to receive and buffer the upload to disk, and then hand your backend a tiny request with just the saved file's path, original name, content type, and size. You compile this module into NGINX, point an `upload_pass` at your app endpoint, configure `upload_store` directories, and now uploads land on disk via NGINX while your backend gets a clean, small form POST describing the file instead of the bytes themselves.

It also fits when you need **resumable uploads** (the module supports a resumable upload protocol via `Content-Range`) or per-file hashing/CRC32 so the backend can verify integrity without re-reading the payload. The classic use case is an upload tier in front of a PHP/Python/Ruby app that would otherwise choke on big multipart bodies — offload the heavy lifting to NGINX, keep the app stateless and fast.

## When NOT to use

- **Low-activity, fork-of-a-fork lineage — the headline caution.** The original module (by Valery Kholodkov) went unmaintained; this `fdintino` fork is the de-facto continuation but is itself **low-activity** (last push 2024-07; see Health). Compiling an aging third-party C module into NGINX is a real maintenance and security commitment — weigh it before adopting.
- **You can offload to object storage.** If clients can upload directly to S3/GCS via presigned URLs, you avoid the upload-tier disk, the NGINX recompile, and the cleanup problem entirely. That's the modern default for many apps.
- **You're not willing to compile NGINX.** It's a static C module (no dynamic-module guarantee across versions) — you build NGINX with it, and re-validate on every NGINX upgrade. If you want config-only or a managed setup, this is friction.
- **You need a maintained, vendor-supported path.** No foundation/company backing; if a future NGINX release breaks it, you may be patching C yourself. For supported large-upload handling, NGINX's own `client_body_*` buffering plus an app-level chunked/tus protocol may be safer.
- **Modern resumable/tus workflows.** For robust resumable uploads, a dedicated tus server/implementation has a more active ecosystem than this module's resumable protocol. [未验证]
- **Disk lifecycle you won't manage.** It writes files to `upload_store` on the NGINX box; you own cleanup, quotas, and the failure modes (partial files, full disks). Forgetting this is an operational landmine.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| NGINX `client_body_*` buffering + app handling | 未收录 | Choose built-in NGINX buffering when first-party config matters more than offloading multipart parsing from the app. | Simpler to keep working, but the app still parses uploads and gets less offload than this module provides. |
| Direct-to-S3 presigned uploads | 未收录 | Choose direct-to-S3 when upload bytes can bypass your servers entirely. | Best scalability and durability, but pushes object-storage and client-upload logic into the product. |
| [tusd](tusd.md) | ✅ | Choose tusd when robust resumable uploads and SDK ecosystem matter more than staying inside NGINX. | Separate service rather than an NGINX module, but better suited to full tus workflows. |
| [lua-nginx-module](lua-nginx-module.md) | ✅ | Choose lua-nginx-module only if general OpenResty scripting is what you need, not a purpose-built streaming multipart receiver. | Programmable edge runtime, not a specialized upload-offload module. |
| Application framework upload handlers | 未收录 | Choose framework upload handlers when uploads are small enough that zero extra infrastructure beats edge offload. | Django/Rails/Express can handle it, but the app server absorbs the slow-client cost. |

## Tech stack

- **Language:** C — an NGINX HTTP module compiled into the server.
- **Protocol:** parses `multipart/form-data` (RFC 1867); supports a **resumable** upload protocol via `Content-Range`.
- **Integration:** streams uploaded files to `upload_store` directories on disk, then issues an internal request to `upload_pass` (your backend) carrying the file's path/name/content-type/size (and optional CRC32/hash) as form fields.
- **Build:** added at NGINX `./configure --add-module=...` time (static); dynamic-module builds are version-sensitive. [未验证]

## Dependencies

- **An NGINX source tree to compile against** — the module is built into NGINX, not loaded standalone.
- **Local disk** for `upload_store` (the staging area uploads land in) — and a cleanup strategy for it.
- **A backend** to receive the `upload_pass` request — yours to run.
- **No external services or datastores** required by the module itself.

## Ops difficulty

**Medium.** Configuration is straightforward (a few `upload_*` directives), but the operational weight is in two places. First, **builds**: it's a static C module, so you recompile NGINX to add it and **re-validate on every NGINX upgrade** — and because the module's activity is low, a future NGINX API change could require patching C yourself. Second, **disk lifecycle**: uploaded files land on the NGINX host's `upload_store`; you own cleanup, disk-full handling, partial-file cleanup on aborted uploads, and any quota enforcement. Once compiled and with a cleanup job in place it runs quietly, but the upgrade/maintenance tail is the part teams underestimate.

## Health & viability

- **Responsiveness**: Cannot be scored — no_data.
- **Maintenance (2026-06) — low activity.** Last push **2024-07** (≈2 years stale at writing); tags through **v2.3.0**. Not archived, but reads as **maintenance-mode / low-activity**, not actively developed. This fork exists precisely because the upstream stalled — so the lineage is "kept alive when needed," not vibrant. [推断]
- **Governance / bus factor.** `User`-owned (Frankie Dintino's fork of Valery Kholodkov's original). A ~1k-star `User`-owned C module with low activity is a **clear bus-factor flag** — survival depends on one maintainer's continued attention, and there's no organizational backing. [推断]
- **Age × Lindy.** The lineage is old (this repo created **2008-12**, ~17 years) — Lindy on the *concept* and the original code is strong, but the **low recent activity weakens the "still-active" half**: old-and-coasting, not old-and-thriving. Use age × activity together; here activity is the weak factor. [推断]
- **Adoption.** Historically well-known for NGINX upload offload (~1k stars, ~378 forks); but the modern trend toward direct-to-object-storage and dedicated tus servers has reduced its centrality. License is **BSD-3-Clause** (read from the `LICENCE` file: © 2006, 2008 Valery Kholodkov, 3-clause BSD text). [推断]
- **Risk flags.** Aging low-activity third-party C compiled into your NGINX is the principal security/maintenance risk — a future NGINX release could break it with no vendor to fix it. No relicense history found. [推断]

## Caveats (unverified)

- [未验证] ~1.0k stars / ~55 open issues / last push 2024-07 / tags through v2.3.0 as of 2026-06 — volatile, re-check.
- [未验证] License: GitHub's API reported `NOASSERTION`; the repo's `LICENCE` file is a **3-clause BSD** license (© 2006, 2008 Valery Kholodkov — "Neither the name... may be used to endorse...") — recorded as BSD-3-Clause from reading that file.
- [未验证] Resumable-upload protocol support and CRC32/hash fields are from the module's docs/feature list; exact current behavior and NGINX-version compatibility not verified against the code here.
- [未验证] Whether a clean dynamic-module build works against current NGINX releases is version-sensitive and not verified.
- [推断] "Maintenance-mode / low-activity" and the bus-factor verdict are inferred from push recency + a single `User` owner, not a stated project status.
