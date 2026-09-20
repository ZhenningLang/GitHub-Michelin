# object-storage

> Category node. S3-compatible object storage servers you run yourself — the store behind backups, log archives and application blobs.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Silo** | Use it when you already run MinIO and upstream's community edition has ended — Silo keeps the S3 API, on-disk format and `MINIO_*` names alive, but the executable/packages/image rename to `silo` and it is a single-maintainer fork of one codebase. | B (4/6) | [→](silo.md) |
| **MinIO** | Use this page to decide what to do about MinIO you already run: the community repository is archived (2026-04) and unmaintained, so the choice is an exit to a maintained fork or another store — not a new deployment. | D (5/6) | [→](minio.md) |
| **Garage** | Use it when you want one S3 endpoint over a few cheap machines in different places, replicating across sites and surviving one being offline — but its S3 surface is deliberately partial (no ACL/policy semantics). | B (4/6) | [→](garage.md) |
| **SeaweedFS** | Use it when the real constraint is object count — billions of small files — and you want one `weed` binary serving S3, a filesystem and a table layer, growing capacity by adding volume servers. | B (5/6) | [→](seaweedfs.md) |
| **Ceph** | Use it when you need object, block and file from one foundation-governed platform and can staff a real storage cluster — overkill if all you need is one S3 bucket. | A (3/6) | [→](ceph.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Silo](silo.md) | ✅ | B (4/6) | MinIO's codebase with a maintained release line and no data migration — paid for with single-org backing, AGPL obligations, and a conditional rather than no-touch upgrade path. |
| [MinIO](minio.md) | ✅ | D (5/6) | The S3 server a generation standardized on, now archived and unmaintained — its format and API live on in Silo, so choose it only to reproduce a frozen legacy build. |
| [Garage](garage.md) | ✅ | B (4/6) | Multi-site S3 from unreliable, heterogeneous machines with a single Rust binary — not a MinIO drop-in, and not the full S3 feature surface. |
| [SeaweedFS](seaweedfs.md) | ✅ | B (5/6) | One binary, one disk read per blob, capacity by adding volume servers, plus a filesystem and lakehouse face — a different architecture with more moving parts than a single S3 server. |
| [Ceph](ceph.md) | ✅ | A (3/6) | Object + block + file under non-profit foundation governance at cluster scale — the heaviest operational bill here, and more than most S3-only needs require. |

## What belongs here

Object storage you operate yourself: S3-compatible servers (and, as the category grows, S3 gateways in front of other backends) plus their clients and companions. The current set splits by design center — MinIO/Silo for one S3 server and MinIO-format compatibility, Garage for multi-site clusters of cheap machines, SeaweedFS for very large object counts plus a filesystem face, Ceph for a foundation-governed platform that also provides block and file. Not block/file-only storage platforms, not the backup software that writes to an object store, and not hosted object storage services.
