---
name: copyparty
slug: copyparty
repo: https://github.com/9001/copyparty
category: document-management
tags: [file-server, file-sharing, webdav, ftp, sftp, resumable-upload, dedup, media-indexer, self-hosted, mit]
language: Python
license: MIT
maturity: v1.20.24, active, ~47k stars (2026-09)
last_verified: 2026-09-28
type: app
upstream:
  pushed_at: 2026-09-27T19:13:03Z
  default_branch: hovudstraum
  default_branch_sha: ab2299e3db705fad1cde78cc979b44fa833bc264
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T06:02:45Z
  overall: B
  overall_score: 3.33
  scored_axes: 6
  applicable_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: A
      raw:
        archived: false
        last_commit_age_days: 0
        active_weeks_13: 12
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 1.8
        qualifying_issues: 44
        band: relaxed_solo
        window_offset_days: 8
        source: issue
        inferred: false
    adoption:
      grade: B
      raw:
        registry: pypi.org
        canonical_package: copyparty
        dependent_repos_count: 1
        downloads_last_month: 8767
        graph_tier: D
        volume_tier: D
        cross_check_divergence: null
        homebrew_installs_90d: 817
        homebrew_tier: B
        release_downloads: 524267
        release_assets: 765
        release_tier: C
        signal_basis: homebrew+releases
        tier_source: homebrew+releases
    longevity:
      grade: A
      raw:
        repo_age_days: 2682
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 66
        top1_share: 0.82
        top3_share: 0.853
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# copyparty

A single-file, zero-required-dependency portable file server with accelerated resumable uploads, dedup, and a media indexer — reachable over HTTP, WebDAV, FTP/FTPS, SFTP, TFTP, and SMB.

![copyparty — health radar](../../assets/health/copyparty.svg)

## When to use

You're the homelab person for a small team, and you keep needing a place to *drop files* — share a folder of scans with a colleague, let a non-technical client upload a 4 GB video that has to survive a flaky connection, expose an archive over WebDAV so a phone can browse it, and have FTP/SFTP available for the one legacy device that only speaks FTP. Spinning up a full DMS or an S3 stack for this is overkill, and you don't want to install a database and three services just to move bytes around. You copy one file — `copyparty-sfx.py` (or run the Docker image) — point it at a directory, define a couple of per-volume read/write users, and you have a browser-accessible server with a real upload UI, resumable multithreaded uploads (`up2k`/`u2c`) that shrug off dropped connections, and content-matching dedup so re-uploads don't bloat the disk. The built-in indexer makes the tree searchable by name, path, date, size, and audio tags, and renders thumbnails for images/video/audio — so for a pile of media and loose files it's "stand it up and forget it," with no Postgres, no Redis, no Angular build.

It also shines as the *ingest and transport* layer in front of something heavier: copyparty's event hooks and file-parser plugins can fire a program on each upload (move it, transcode it, or hand it to a real DMS), so you can use it as the friendly upload front door while a downstream system does OCR and archival.

## How it works

copyparty is one Python script that is simultaneously the server, the web UI, and the search index. You start it pointed at a folder — a "volume" — and it listens on HTTP(S); everything else layers onto that: optional WebDAV, FTP(S), SFTP, TFTP and SMB listeners, and per-volume, per-user read/write accounts declared on the command line (e.g. `-v /mnt/music:/music:r:rw,foo -a foo:bar`). Uploads from the browser go through **up2k**, a chunked uploader — the file is split into blocks and hashed, so a dropped connection resumes only the missing blocks, and a file (or block) that already exists on disk is never re-transferred; with `--dedup` a duplicate upload becomes a symlink instead of a copy. An optional per-volume SQLite index (`.hist/up2k.db`) powers name/tag search and undo/recent lists, and thumbnails appear only if you install the optional accelerators (Pillow, FFmpeg) — the core runs on Python alone. What copyparty does for you: serve, resume, dedup, index. What stays yours: the machine, TLS/reverse-proxy if you expose it, and backups of the served folders *plus* their `.hist` directories.

![copyparty — backbone user story](../../assets/flow/copyparty.svg)

<!-- flow-steps:begin (generated from flows/copyparty.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install or fetch the server — Python alone is enough — `python3 -m pip install --user -U copyparty · uv tool run copyparty`
2. **You**: Point it at a folder and define who may write — `-v /mnt/music:/music:r:rw,foo -a foo:bar`
3. **copyparty**: Serves it over HTTP, WebDAV, FTP(S), SFTP, TFTP and SMB with a browser UI
4. **You**: Enable indexing and dedup, then drag files into the browser to upload — `-e2dsa · --dedup`
5. **copyparty**: up2k splits uploads into blocks, resumes dropped transfers, and stores duplicate bytes once — component: `up2k uploader`

**Value**: A durable, searchable file server in one Python script — no database, no stack to babysit

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You actually need a document-management system (OCR + full-text content search).** copyparty searches *filenames, paths, dates, sizes, and audio (ID3) tags* — it does **not** OCR scanned paperwork and does **not** full-text-index document *contents*. For "find the invoice that mentions account 1234," use [paperless-ngx](paperless-ngx.md) or [Twake Drive](twake-drive.md), not copyparty.
- **You want collaborative document editing / Office co-authoring.** It serves and (for Markdown) lightly edits files; it is not a Drive/Office-suite replacement.
- **You want a hardened internet-facing service by default.** It's powerful and exposes many protocols; the SMB server is explicitly labeled unsafe/slow and "not recommended for wan," and a broad protocol surface on the public internet wants a reverse proxy, TLS, and care. It is not a turnkey secure cloud.
- **You need folder *sync* (two-way, Dropbox-style).** The maintainer states full sync will never be supported — it's upload/download/serve, not a sync engine.
- **You need lifecycle/retention, approvals, e-signatures, versioning, or audit trails.** None of that is the goal; the project's stated philosophy is "do all the things, and do an *okay* job," prioritizing breadth over depth.
- **You need fine-grained, per-document multi-tenant privacy.** Permissions are per-volume / per-user (read/write/move/delete/admin/dotfiles), not per-document ACLs.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [paperless-ngx](paperless-ngx.md) | ✅ | Choose paperless-ngx when scanned-paper OCR, auto-tagging, and document full-text search are the job; keep copyparty when lightweight upload/download, multi-protocol serving, or an ingest front door is the deciding need. | A real DMS: OCR + full-text content search + auto-tagging of scanned paperwork, but a multi-container Django/Postgres/Redis stack. copyparty has zero of that OCR/FTS pipeline; it's a far lighter file server, not a document archive. |
| [Twake Drive](twake-drive.md) | ✅ | Choose Twake Drive when a team drive with document editing, sharing, and richer permissions is worth the platform weight; keep copyparty for standalone file drop, transfer, and serving without a suite dependency. | Collaborative drive with document editing, sharing, and a richer permission model; heavier to run. copyparty is single-file file-transfer/serving with no co-editing or per-document ACLs. |
| Nextcloud | 未收录 | Choose Nextcloud when you need the full self-hosted cloud shape: sync clients, apps, sharing, and groupware; keep copyparty when portability, protocol breadth, and no database matter more than an app ecosystem. | Full self-hosted "cloud" (files, sync clients, apps, sharing, optional OCR via add-ons) but a heavy PHP/DB/Redis stack. copyparty is dramatically lighter and faster to stand up, with no two-way sync and no app ecosystem. |
| Seafile | 未收录 | Choose Seafile when reliable two-way sync, delta sync, and client apps are mandatory; keep copyparty for ad hoc uploads and multi-protocol serving where sync is explicitly not required. | Block-based sync-and-share with strong delta sync and client apps. copyparty wins on portability/zero-deps and protocol breadth (WebDAV/FTP/SFTP/TFTP/SMB) but has no real sync. |
| Filebrowser | 未收录 | Choose Filebrowser when a simpler Go single-binary web file manager is enough; keep copyparty when resumable accelerated uploads, protocol breadth, or the media indexer are the deciding features. | Comparable lightweight single-binary web file manager (Go). Narrower protocol set and no `up2k`-style resumable accelerated uploads or media indexer; simpler to reason about. |
| MinIO | 未收录 | Choose MinIO for S3-compatible object storage consumed by programs and apps; keep copyparty for human-facing file sharing and ingest over browser, WebDAV, FTP, or SFTP. | S3-compatible object storage for programmatic/app access. Different shape entirely — copyparty is a human-facing multi-protocol file server, not an object store. |

## Tech stack

- **Language:** Python (server). Browser UI is vanilla JS/HTML/CSS (`up2k` client-side uploader).
- **Storage/index:** plain filesystem; a per-volume SQLite database (`.hist/up2k.db`) for the file index / dedup / tags.
- **Protocols:** HTTP(S), WebDAV, FTP(S), SFTP, TFTP, SMB/CIFS; zeroconf (mDNS/SSDP) discovery.
- **Optional accelerators:** Pillow / pyvips / FFmpeg (thumbnails + transcode), Mutagen / FFprobe (audio tags), libraw/rawpy (RAW thumbnails). All optional — the core server runs on Python alone.
- **Extensibility:** event hooks and file-parser plugins (run external programs on upload to add tags or trigger downstream processing).

## Dependencies

- **Required:** just a Python interpreter. The README (2026-09) still states verbatim: "server only needs Python (2 or 3), all dependencies optional." Modern Python 3 recommended; actual Python-2 execution was not tested here `[推断]`.
- **Optional (feature-gated):** Pillow / pyvips / FFmpeg for thumbnails & media transcoding; Mutagen for audio metadata; pyvips/libvips, rawpy/libraw for extra image formats.
- **Deployment artifacts:** `copyparty-sfx.py` (single self-contained file), Windows `copyparty.exe`, official Docker images, and packages on Arch / Homebrew / NixOS.
- **Infra:** no external database, message broker, or other service required — it is genuinely self-contained.

## Ops difficulty

**Low** for the common case: copy one file (or `docker run`), pass a few flags or a small config to define volumes and users, and it's up — no DB to provision, no migrations, no extra services. Difficulty rises to **low-to-medium** when you (a) enable the optional media/thumbnail/transcode stack (now you're managing FFmpeg/Pillow versions), or (b) expose it to the internet, where the broad protocol surface (WebDAV/FTP/SFTP/TFTP/SMB) means you own TLS, a reverse proxy, real-IP handling, and locking down the riskier protocols (SMB is flagged unsafe for WAN). You own backups of the served directories and the `.hist` index.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 1.8 hours across 44 qualifying issues/PRs.
- **Maintenance (2026-09).** Fast release train: v1.20.16 (2026-05-26) → v1.20.24 (2026-09-19, GitHub API), last pushed 2026-09-27 — **active**, not archived.
- **Governance / bus factor.** This is the standout flag: a **single-maintainer, `User`-owned repo** (`9001/copyparty`) with ~47k stars. Heavy adoption resting on one person is a real bus-factor risk — if the maintainer steps away, there is no foundation or vendor to carry it. The opinionated, single-author design (e.g. "sync will never be supported") is the flip side of that. [推断]
- **Age & Lindy verdict.** ~7 years old (created 2019-05) and still actively maintained ⇒ a **moderate Lindy** signal — long enough to have proven durable, but it lives or dies with its maintainer rather than an institution. [推断]
- **Adoption.** Strong for its niche (~47k stars, gh api 2026-09-28; packaged on Arch/Homebrew/NixOS, official Docker), which is exactly what makes the bus-factor concentration matter.
- **Risk flags.** MIT, no relicense or open-core found; the broad protocol surface (SMB flagged "unsafe, slow, not recommended for wan" in the README) is a *security* concern when internet-facing, separate from project viability.

## Caveats (unverified)

- [推断] "Single-file / zero required dependencies" reflects the project's own framing (`copyparty-sfx.py` + "server only needs Python (2 or 3), all dependencies optional", verbatim in the 2026-09 README); the exact minimum Python 3 version for the current release was not pinned in the fetched docs — verify against the running release before relying on a specific interpreter version.
- [推断] up2k's per-block content-addressed resume/dedup behavior is read from the README's own claims (resumable, multithreaded; dropping a file shows if it already exists; `--dedup` symlinks duplicates), not tested against the protocol.
- [未验证] Search is filename/path/date/size + audio-tag based; no OCR and no document full-text-content indexing were found in the README — confirm against current docs if content search is a hard requirement.
- [未验证] File-parser plugins / event hooks can run external programs to add custom tags or trigger downstream processing, but the breadth of out-of-the-box (non-audio) media tagging — e.g. EXIF, video resolution — was not clearly enumerated in the fetched docs.
