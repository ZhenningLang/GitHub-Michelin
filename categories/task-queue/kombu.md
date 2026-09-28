---
name: Kombu
slug: kombu
repo: https://github.com/celery/kombu
category: task-queue
tags: [messaging, amqp, rabbitmq, redis, sqs, python, transport, broker-abstraction]
language: Python
license: BSD-3-Clause
maturity: v5.6.2, active (2026-09), ~3.1k stars
last_verified: 2026-09-28
type: library
upstream:
  pushed_at: 2026-09-28T04:30:32Z
  default_branch: main
  default_branch_sha: 09f26b00c0fbe40da2d111eae17344f07126e7a9
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T09:04:32Z
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
        last_commit_age_days: 1
        active_weeks_13: 10
        carve_out: null
    responsiveness:
      grade: C
      raw:
        median_ttfr_hours: 267.4
        qualifying_issues: 10
        band: default
        window_offset_days: 3
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: kombu
        dependent_repos_count: 26706
        downloads_last_month: 43453410
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5941
        last_commit_age_days: 1
        cohort: library
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 19
        top1_share: 0.787
        top3_share: 0.836
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: BSD-3-Clause
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# Kombu

A Python messaging library that gives one idiomatic high-level API over many message brokers — AMQP/RabbitMQ plus pluggable "virtual" transports (Redis, Amazon SQS, MongoDB, ZooKeeper, in-memory) — and is the transport layer Celery is built on.

![kombu — health radar](../../assets/health/kombu.svg)

## When to use

You're a backend engineer building a Python service that needs to publish and consume messages, and you don't want to hard-code the AMQP wire details or marry your code to one broker. Today you're on RabbitMQ, but ops is talking about moving to Redis or Amazon SQS, and you'd rather not rewrite your producers and consumers when that happens. You pull in Kombu, declare your exchanges/queues as Python objects, and write a `Producer`/`Consumer` against its high-level API. The same code runs over `amqp://`, `redis://`, or `sqs://` by swapping a connection URL, because Kombu abstracts each broker behind a common transport interface, and it handles the messaging plumbing — connection pooling, automatic reconnection, serialization (JSON/pickle/msgpack/YAML), and compression — that you'd otherwise reimplement.

You also reach for Kombu when you're building framework-level infrastructure rather than an app: a task queue, an event bus, or a worker pool where you need fine control over acknowledgement, prefetch, and consumer mixins. It's the foundation Celery itself uses, so if you've outgrown Celery's task abstraction but still want a battle-tested broker layer, Kombu is the lower-level primitive to build on directly.

## How it works

Kombu is a client library, not a service — it lives inside your process and talks the broker's protocol for you. You declare the AMQP-shaped pieces (an *exchange* — the post office that routes messages; a *queue* — the mailbox consumers read from) as plain Python objects, then open one `Connection` from a URL. Publishing goes through a `Producer`, which serializes your payload (JSON/pickle/msgpack/YAML) and hands it to the exchange over pooled, auto-reconnecting connections. Consuming goes through a `Consumer` plus a `conn.drain_events()` loop (it waits on the socket for the next message), which dispatches to your callback until your `message.ack()` tells the broker the delivery is settled. The trick is the **transport layer**: on RabbitMQ it speaks real AMQP (via py-amqp); on Redis, SQS, MongoDB and friends a "virtual transport" emulates those semantics using the backend's own primitives — which is why portability is at the API level, not the guarantee level. What stays yours: running the broker itself and getting ack/visibility-timeout/prefetch right per transport.

![Kombu — backbone user story](../../assets/flow/kombu.svg)

<!-- flow-steps:begin (generated from flows/kombu.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install Kombu into your Python service — `pip install kombu` — component: `application environment`
2. **You**: Declare exchanges and queues as Python objects, then open one Connection by URL — `with Connection('amqp://guest:guest@localhost//') as conn:`
3. **Kombu**: The same transport interface serves amqp://, redis:// or sqs:// behind the URL — component: `transport layer`
4. **You**: Publish through a Producer, declaring the queue with the message — `producer = conn.Producer(serializer='json')`
5. **Kombu**: Serializes the payload and routes it to the bound queue
6. **You**: Consume with a callback list plus an event loop — `conn.drain_events()` — component: `Consumer`
7. **Kombu**: Delivers each message to your callback; your message.ack() confirms it

**Value**: One producer/consumer API across AMQP, Redis, SQS and more — moving brokers is a URL change, not a rewrite

</details>
<!-- flow-steps:end -->

## When NOT to use

- **You just need to run background tasks.** If your goal is "call a function later, with retries and a worker pool", use [Celery](celery.md) (which sits on top of Kombu) rather than wiring producers/consumers by hand. Kombu is the plumbing, not the task framework.
- **You're not on Python.** Kombu is Python-only. For polyglot messaging, talk to the broker via its native client or a cross-language protocol (raw AMQP, Kafka, NATS).
- **You want a full event-streaming platform.** Kombu is a broker *client/abstraction*, not a log-structured stream store. For high-throughput, replayable event streams with consumer-group semantics, Kafka/Redpanda/Pulsar are the right tier.
- **You need every broker to behave identically.** The virtual transports (Redis, SQS, …) emulate AMQP semantics imperfectly — features like exchange types, priorities, and delivery guarantees differ per backend. Portability is "swap the URL", not "identical behavior". [推断]
- **You want first-class async/await.** Kombu's core consumer model is synchronous/event-loop-driven in the Celery style; if your stack is built around `asyncio`, an async-native AMQP client (e.g. `aio-pika`) may fit better. [未验证]

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Celery](celery.md) | ✅ | Choose Celery when you need a task queue built *on* Kombu rather than the raw broker abstraction. | Use Celery for "run this job"; use Kombu when you need transport-level broker abstraction. Not a substitute, a higher layer. |
| py-amqp / pika | 未收录 | Choose py-amqp or pika when you need lower-level AMQP-only clients. | Less abstraction and no multi-broker portability, but fewer moving parts if you will only ever use RabbitMQ. |
| aio-pika | 未收录 | Choose aio-pika when you need an async-native AMQP client for `asyncio`. | Better async ergonomics, RabbitMQ-only, and smaller in scope than Kombu's multi-transport model. |
| confluent-kafka-python / [kafka-python](../kafka-tools/kafka-python.md) | 部分已收录 | Choose Kafka clients when you need log-structured streaming rather than broker abstraction. | Different semantics: replay, partitions, and consumer groups. confluent-kafka-python is not indexed separately. |
| NATS / Redis Streams (direct) | 未收录 | Choose direct system clients when you have committed to one broker or stream. | Simpler for a single system, but no broker-agnostic layer. |

## Tech stack

- **Language:** Python — released 5.6.x requires Python ≥3.9; the 5.7 line (alpha since 2026-09) moves to ≥3.10 with classifiers through 3.14. Pure-Python library.
- **Core abstraction:** a pluggable **transport** interface — a real AMQP transport (via `py-amqp` or `qpid`) plus "virtual" transports that emulate AMQP semantics over other backends.
- **Built-in transports:** Redis, Amazon SQS, MongoDB, ZooKeeper, Pyro, SoftLayer MQ, and an in-memory transport for unit testing; PGMQ joins the README's built-in list on the 5.7 (main) line. Released 5.6.2 additionally ships extras for Google Cloud Pub/Sub, Confluent Kafka, Azure Storage Queues / Service Bus, and Consul; SQS fan-out works via AWS SNS behind an option.
- **Serialization & framing:** pluggable serializers (JSON, pickle, msgpack, YAML) and compression; connection pooling and automatic failover/reconnect.

## Dependencies

- **Runtime:** Python plus a transport driver — `amqp` (py-amqp) for RabbitMQ, `redis` for the Redis transport, `boto3`/SQS deps for Amazon SQS, etc. You install only the extras for the broker you use.
- **A running broker (yours to operate):** RabbitMQ, Redis, an SQS account, MongoDB, or ZooKeeper depending on the transport. Kombu is a client; it doesn't run the broker.
- **Install:** `pip install kombu` from PyPI; broker-specific extras like `kombu[redis]` / `kombu[sqs]`.

## Ops difficulty

**Low for the library; the broker is the real ops.** Kombu adds no service of its own — it's a `pip` dependency inside your process, so there's nothing extra to deploy or monitor for Kombu itself. The operational weight is whatever **broker** you point it at: running and clustering RabbitMQ, sizing Redis and reasoning about its weaker delivery guarantees, or managing SQS quotas and visibility timeouts. The library-level concerns are getting prefetch/acknowledgement/heartbeat settings right so you don't lose or duplicate messages under failure, and being aware that each virtual transport has its own quirks. If you already run Celery, you're already running Kombu and its broker — this is the same operational surface.

## Health & viability

- **Responsiveness**: Grade C — median first-response time 267.4 hours across 10 qualifying issues/PRs.
- **Maintenance (2026-09).** Default branch is under daily commit flow (last pushed 2026-09-28); latest stable v5.6.2 (2025-12) with the v5.7.0a1 prerelease out 2026-09 — releases move slower than commits, but the project is **active**, not coasting. Not archived.
- **Governance / bus factor.** Lives under the **celery** GitHub organization with multiple long-term maintainers (ask, auvipy, thedrow, matusvalo, …), not a single-maintainer project — a healthier bus factor than a solo repo, though still community-run rather than foundation-governed. [推断]
- **Age & Lindy verdict.** Created 2010-06 (GitHub `created_at`), ~16 years old and **still actively shipping** ⇒ a **strong Lindy** signal; it has been the broker layer under Celery for over a decade.
- **Adoption.** Effectively ubiquitous wherever Celery is used (Celery depends on it), giving it very broad transitive adoption far beyond its ~3.1k direct stars (2026-09); 43,453,410 monthly PyPI downloads. Mature docs on Read the Docs.
- **Risk flags.** BSD-3-Clause, no relicense history found; main consideration is that virtual-transport parity with real AMQP is imperfect and shifts release-to-release.

## Caveats (unverified)

- [未验证] ~3.1k GitHub stars, stable v5.6.2 (2025-12) and v5.7.0a1 prerelease read from the GitHub/PyPI APIs on 2026-09-28; star/version numbers are date-sensitive — treat as indicative.
- [未验证] The supported Python-version floor moves with the line (3.9 for 5.6.x, 3.10 for 5.7-dev) and the exact set of broker extras changes across releases — check the current `setup.py`/PyPI metadata before pinning.
- [推断] Virtual transports (Redis, SQS, MongoDB, …) emulate AMQP semantics with backend-specific gaps; "swap the URL" portability is not identical behavior across brokers.
- [未验证] Async/await ergonomics are limited relative to async-native AMQP clients; the core model follows Celery's event-loop/synchronous style.
