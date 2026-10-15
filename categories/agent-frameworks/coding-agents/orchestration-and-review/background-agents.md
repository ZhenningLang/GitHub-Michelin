---
name: Background Agents (Open-Inspect)
slug: background-agents
repo: https://github.com/ColeMurray/background-agents
category: orchestration-and-review
tags: [coding-agent, background-jobs, sandbox, cloudflare, github-app, multi-repo, automation]
language: TypeScript
license: MIT
maturity: v0.1.0 private workspace, active, 3354 stars, no GitHub Releases (as of 2026-10-13)
last_verified: 2026-10-13
type: app
upstream:
  pushed_at: 2026-10-13T16:39:16Z
  default_branch: main
  default_branch_sha: 31d199996e4cc33fcc1f80c08785820db2f05537
  archived: false
health:
  schema: 1
  computed_at: 2026-10-13T16:46:52Z
  overall: B
  overall_score: 3.2
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
        last_commit_age_days: 0
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 10.6
        qualifying_issues: 29
        band: relaxed_solo
        window_offset_days: 10
        source: issue
        inferred: false
    adoption:
      grade: "?"
      raw: {}
    longevity:
      grade: C
      raw:
        repo_age_days: 261
        last_commit_age_days: 0
        cohort: app
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 68
        top1_share: 0.741
        top3_share: 0.924
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: MIT
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
  unknowns:
    adoption: { reason: no_package_structural }
---

# Background Agents (Open-Inspect)

Your team's coding task stops when someone closes their laptop, and a CI job cannot provide an interactive shared session. Open-Inspect keeps the work in cloud sandboxes, with a self-hosted session UI and integration triggers.

![Background Agents — health radar](../../../../assets/health/background-agents.svg)

## When to use

You're operating one trusted engineering organization: a Linear issue needs a patch while its requester is away, and a colleague must be able to inspect progress or add a prompt without taking over that person's terminal. Open-Inspect runs background sandbox sessions, streams their progress to collaborators, and supports web, Slack, GitHub, Linear, schedules and webhooks. Pick it over a local coding CLI when those shared sessions, up to ten repositories per session and reusable sandbox lifecycle justify a separate control plane.

Choose it only when you can operate identity, a GitHub App, model credentials, a sandbox provider and the single-tenant trust model. Cloudflare is the main deployment guide; an AWS-hosted control-plane path is also documented. It is internal engineering automation, not an out-of-the-box personal assistant.

## When NOT to use

- **You need multi-tenant SaaS or authorization based on each user's personal GitHub permissions.** Choose a separately isolated deployment per organization or an explicitly tenant-isolated platform. Open-Inspect now has teams, repository grants and session-scoped GitHub credentials, but still shares an installation, does not compare personal GitHub permissions, defaults team-read enforcement to `shadow`, and cannot immediately revoke issued tokens. See the reviewed [security model](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/README.md#security-model-single-tenant-only).
- **You are an individual developer or only need terminal pair programming.** Choose [OpenCode](../terminal-agents/opencode.md); Terraform, GitHub App/OAuth setup, cloud control-plane and sandbox credentials are disproportionate for a local workflow.
- **Your policy forbids cloud sandbox providers.** Choose a local agent such as OpenCode or evaluate a self-managed [OpenHands](openhands.md) deployment; the documented sandbox paths use Modal, Daytona, Vercel Sandbox, OpenComputer or E2B. AWS hosting removes the Cloudflare requirement, not the sandbox-provider responsibility.
- **You only need one audited CI event to produce a patch.** Use GitHub Actions plus OpenCode rather than this session platform; sandbox credential caches and snapshots, secret scopes, bots and schedules add access paths that you must manage.
- **You need a long-lived, versioned production platform with established releases.** Choose a more mature hosted or self-managed option; this young repository had no GitHub Releases at review time and its workspace version is `0.1.0`.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [OpenCode](../terminal-agents/opencode.md) | ✅ | Choose OpenCode for a local developer-operated coding agent; choose Open-Inspect when trusted-team background sessions and integrations justify a cloud control plane. | OpenCode avoids infrastructure and shared credentials; Open-Inspect adds sandbox scheduling, integrations, and multi-repository automation. |
| [OpenHands](openhands.md) | ✅ | Choose OpenHands' Agent Canvas when one developer or a small team wants to start with a local backend; choose Open-Inspect when organizational sandbox lifecycle and attributed background work justify its single-tenant setup. | Agent Canvas starts on one machine and adds remote/automation backends; Open-Inspect starts with cloud infrastructure and a shared GitHub App trust boundary. |
| GitHub Actions plus an agent CLI | not a repo | Choose CI-triggered agent scripts when a narrow, audited event flow is enough; choose Open-Inspect when interactive sessions, live collaboration, and reusable sandbox lifecycle are required. | This is a composition pattern, not a single repository; scripts keep a smaller control plane but leave session UI and sandbox reuse to you. |
| [CC Switch](cc-switch.md) | ✅ | Choose CC Switch for one person's desktop management of installed agents; choose Open-Inspect for organizational cloud execution and asynchronous automation. | CC Switch is low-ops and local; Open-Inspect introduces credentials, sandboxes, data-plane operations, and a shared trust boundary. |

## Quick start

Follow the reviewed [deployment guide](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/docs/GETTING_STARTED.md): install Node 24+, Terraform 1.14+ and the Modal Python tooling, fork the repository, run `npm install` and `npm run build -w @open-inspect/shared`, then configure the cloud accounts and GitHub App in the provided Terraform files. From `terraform/environments/production`, run `terraform init -backend-config=backend.tfvars` and `terraform apply`; these create billable infrastructure, not a local demo. Bootstrap a workspace Owner using the guide's `npm run rbac:bootstrap-owner` procedure, create a team, grant its repositories, add model credentials, and explicitly enable `teams_enforcement = "on"` before relying on team-only reads. Select that team and repository in the web UI and send a coding task; the platform starts the sandbox and streams the agent's work, with pull-request creation available from the session. You pay for hosting, sandboxes and models, define access scopes, and review changes before merging; neither successful startup nor the health endpoint verifies authorization policy.

![background-agents — backbone user story](../../../../assets/flow/background-agents.svg)

<!-- flow-steps:begin (generated from flows/background-agents.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Deploy the control plane and configure the GitHub App and sandbox credentials — `terraform apply`
2. **You**: Create a team, grant repositories and add model credentials
3. **You**: Select the team and repository, then send a coding task in the web UI
4. **Background Agents (Open-Inspect)**: Start the sandbox, check out repositories and dispatch the prompt — component: `control plane`
5. **Background Agents (Open-Inspect)**: Stream the agent's progress to the shared session — component: `session event stream`

**Value**: Coding work continues in a shared cloud session after the requester leaves

</details>
<!-- flow-steps:end -->

## Key techniques

- **Persist first, dispatch when ready.** [`session/message-queue.ts:422–580`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/session/message-queue.ts#L422-L580) checks provider/harness compatibility, defers while the sandbox boots, and spawns unavailable sandboxes as background work rather than holding bot HTTP requests open. It claims a persisted prompt before WebSocket send; send failure returns it to pending and terminates the unresponsive sandbox. This is queue recovery, not proof that an arbitrary tool side effect runs exactly once.
- **Replayable session history.** [`session/event-stream.ts:21–107`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/session/event-stream.ts#L21-L107) reads the event repository with timeline cursors, excludes heartbeats and offers bounded replay/history pages. Reconnecting clients can recover recent progress without keeping the requesting tab alive; malformed stored events are skipped, so the UI replay is not a completeness guarantee for audit export.
- **Repository scope is resolved at credential issuance.** [`source-control/session-scope.ts`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/source-control/session-scope.ts) reloads session ownership and persisted repository members; [`source-control/repository-scope.ts`](https://github.com/ColeMurray/background-agents/blob/31d199996e4cc33fcc1f80c08785820db2f05537/packages/control-plane/src/source-control/repository-scope.ts) resolves numeric IDs and intersects current team grants. Missing identities fail closed rather than broadening scope. It narrows GitHub installation credentials, but cached tokens and filesystem snapshots remain a separate revocation boundary, and GitLab still uses a deployment-wide PAT.

## Tech stack

- **Control plane:** TypeScript on Cloudflare Workers, Durable Objects, D1, KV, R2, SQLite, and WebSockets.
- **Web:** Next.js 16, React 19, Tailwind CSS and Radix UI, confirmed by `packages/web/package.json`.
- **Sandbox runtime:** OpenCode or Claude Agent harness, Node.js, Python, Bun, Git, GitHub CLI, `agent-browser` and headless Chromium.
- **Infrastructure:** Terraform and Modal, Daytona, Vercel Sandbox, OpenComputer or E2B integrations; Python handles parts of sandbox provisioning. `docs/AWS_BRING_UP.md` also documents a Node control plane on EC2 with Docker Compose, EBS, S3 and Caddy rather than Cloudflare.

## Dependencies

- **Deployment core:** Node.js 24+ (`package.json` engines), npm, Terraform 1.14+; Cloudflare guide additionally requires Wrangler, Cloudflare credentials and Python 3.12+/uv for Modal. The AWS guide instead requires AWS CLI/Session Manager and corresponding accounts.
- **Source control:** GitHub App/OAuth configuration and deliberately constrained installation scope.
- **Sandbox:** one supported sandbox provider and its credentials/resources.
- **Models / integrations:** configure credentials for the selected model/harness; Anthropic API keys are not mandatory for the guide's bot-disabled core path. Optional Slack/Linear classifiers, Google sign-in, Sentry and webhooks bring additional credentials. Subscription-based paths still require provider login and eligibility.

## Ops difficulty

**High.** This is a distributed control plane with identity, GitHub installation credentials, secrets injection, worker state, cloud sandboxes, webhooks, and repository lifecycle scripts. Its own README limits deployment to one trusted tenant; secure operation means minimizing GitHub App scope, entry points, secret scope, and automation permissions.

## Health & viability

- **Maintenance snapshot (2026-10-13):** unarchived, default-branch commit `31d1999` on this date; GitHub reports 3354 stars, but stars do not measure installations. Workspace version remains `0.1.0`, with no GitHub Releases.
- **Governance / bus factor:** the repository is user-owned and contributor activity is heavily concentrated in ColeMurray. The project is actively developed but has a material key-maintainer risk. [推断]
- **Age / Lindy:** created 2026-01 and lacks GitHub Releases, so there is no long operational history or release-line stability signal.
- **Measured coverage:** overall B covers 5/6 axes. Adoption remains `? / no_package_structural`: the root workspace is private and the scorer found neither a canonical package nor an installation signal. This is an unmeasured axis, not zero users or a license exemption.
- **Security / operational risk:** team grants and scoped credentials do not turn a trusted single-tenant product into multi-tenant SaaS. Team-read enforcement's `shadow` default and credentials retained in snapshots require an explicit deployment review.

## Caveats (unverified)

- [未验证：cloud infrastructure was not deployed] Sandbox backends, AWS/Cloudflare deployment and subscription login were source-reviewed, not independently run or security-audited.
- [推断：shared installation, shadow defaults and snapshot credential boundaries] Start with a restricted internal pilot rather than broad repository access; source inspection alone cannot establish production isolation.
