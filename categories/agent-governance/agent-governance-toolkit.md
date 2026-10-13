---
name: agent-governance-toolkit
slug: agent-governance-toolkit
repo: https://github.com/microsoft/agent-governance-toolkit
category: agent-governance
tags: [agent-governance, agent-governance-toolkit, tool]
language: Python
license: MIT
maturity: Public Preview; main core manifests 5.0.0, latest GitHub Release v4.1.0, 6423 stars (as of 2026-10-13)
last_verified: 2026-10-13
type: tool
upstream:
  pushed_at: 2026-10-13T08:57:37Z
  default_branch: main
  default_branch_sha: 47abed7446d47e74cfa76d01a5913bb873ffcad9
  archived: false
health:
  schema: 1
  computed_at: 2026-10-13T17:53:18Z
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
        median_ttfr_hours: 73.8
        qualifying_issues: 39
        band: relaxed_solo
        window_offset_days: 2
        source: issue
        inferred: false
    adoption:
      grade: C
      raw:
        registry: pypi.org
        canonical_package: agent_governance_toolkit
        dependent_repos_count: 0
        downloads_last_month: 125645
        graph_tier: E
        volume_tier: C
        cross_check_divergence: null
        release_downloads: 1021
        release_assets: 83
        release_tier: D
        signal_basis: releases
        tier_source: registry
    longevity:
      grade: C
      raw:
        repo_age_days: 225
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: A
      raw:
        active_maintainers_12mo: 97
        top1_share: 0.324
        top3_share: 0.702
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
# agent-governance-toolkit

Your agent can call both a database and a messaging tool, but a prompt saying “do not leak data” cannot stop a bad tool invocation. AGT places policy checks before wrapped actions and records their decisions; you still own the enforcement points and data-flow rules.

![agent-governance-toolkit — health radar](../../assets/health/agent-governance-toolkit.svg)

## When to use

You are deploying an agent with `query_database` and `send_email`, and need to reject a forbidden operation before either tool runs, then explain the decision to an operator. Choose AGT over prompt-only rules when you can insert a callable wrapper or framework adapter at every action boundary and maintain explicit policy plus audit retention. It packages agent-oriented identity, approval, audit and adapters around policy decisions, rather than leaving all those integration concerns to a general-purpose authorization engine.

Adopt only the layers you need: Python `govern()` for a tool boundary, or the ACS host API for explicit allow/deny/transform decisions; framework and language adapters have their own surfaces. The [reviewed README](https://github.com/microsoft/agent-governance-toolkit/blob/47abed7446d47e74cfa76d01a5913bb873ffcad9/README.md#L59-L86) moves the main policy path to upstream Agent Control Specification and warns about package migration. Public Preview and a main manifest version ahead of the latest GitHub Release mean you must distinguish reviewed source from an installed wheel.

## When NOT to use

- **You need a stable authorization engine but not an agent-governance stack.** Choose Open Policy Agent or Cedar and own a smaller integration; AGT still declares Public Preview with possible breaking changes before GA.
- **OS-level containment is the primary control.** Use containers or a separately isolated sandbox alongside your agent; AGT's application middleware shares the process boundary and does not replace that isolation.
- **You cannot cover every tool execution path.** First centralize dispatch in your own middleware; wrapping one callable does not govern direct calls to the original function or unrelated external processes.
- **Your goal is detecting hallucinations, malicious action sequences or confidential-data flow.** Add result validation and content/data-classification controls; the [limitations](https://github.com/microsoft/agent-governance-toolkit/blob/47abed7446d47e74cfa76d01a5913bb873ffcad9/docs/LIMITATIONS.md#L12-L67) explicitly say individually allowed actions can still form a harmful workflow, and audits do not verify external outcomes.
- **You need approval annotations or default audit logging to be a durable blocking control.** Use an explicit approval coordinator and persistent sink, or a custom enforcement service. `flag_for_review` is annotation-only and default wrapper audit entries live in memory; neither is a merge gate or durable compliance record by itself.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [Open Policy Agent](https://github.com/open-policy-agent/opa) | not indexed | Choose OPA when general policy evaluation is enough and you already control dispatch; choose AGT when agent-specific wrappers, approval and audit reduce your integration work. | OPA supplies the policy engine; agent action context, identity mapping and decision retention stay with your application. |
| [Cedar](https://github.com/cedar-policy/cedar) | not indexed | Choose Cedar when fine-grained authorization is the main problem; choose AGT when enforcement must attach to agent tools and framework lifecycle. | An authorization language/runtime has less agent-specific surface, but does not install the agent's enforcement points for you. |
| [Cedarling (Janssen)](https://github.com/JanssenProject/jans) | not indexed | Choose Cedarling for a Cedar policy decision point in an identity-oriented system; choose AGT for its agent integration stack, optionally using its Cedarling adapter. | Cedarling belongs to a real multi-component IAM repository; it is a decision backend, not a substitute for action dispatch wiring. |
| Custom middleware | not a repo | Write a small dispatcher when one service has only a few tools; choose AGT when reusable policy, approval and audit infrastructure outweigh package complexity. | This is an implementation strategy, not a missing repository; you own failure semantics and audit integrity. |

## Quick start

The [README](https://github.com/microsoft/agent-governance-toolkit/blob/47abed7446d47e74cfa76d01a5913bb873ffcad9/README.md#L59-L129) installs `pip install "agent-governance-toolkit[full]"`; the base wheel provides compliance tooling rather than all wrapper modules, and the reviewed main core manifest requires Python 3.11+. Import `govern` from `agentmesh.governance`, write `policy.yaml` with explicit rules, and replace your tool registration with `safe_tool = govern(my_tool, policy="policy.yaml")`. Call that wrapper with the action/context your policy expects; it evaluates and logs the decision before allowing execution, or raises `GovernanceDenied` by default. For async callables use its documented `acall()` path, and configure `audit_file` plus an audit signing key if records must survive process exit. You own all dispatch wiring, conservative policy defaults, approval handling, secret management and result validation; no Azure account or model API is required for the basic local policy wrapper, while optional cloud/model adapters have their own costs. Pin a compatible package set and check its installed API: the source reviewed here and latest GitHub release do not have the same version number.

![agent-governance-toolkit — backbone user story](../../assets/flow/agent-governance-toolkit.svg)

<!-- flow-steps:begin (generated from flows/agent-governance-toolkit.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the full Python package set — `pip install "agent-governance-toolkit[full]"`
2. **You**: Write policy rules and register the wrapped tool instead of the original — `safe_tool = govern(my_tool, policy="policy.yaml")`
3. **You**: Call the wrapped tool with the policy's action context
4. **agent-governance-toolkit**: Evaluate policy and record the decision before tool execution — component: `GovernedCallable`
5. **agent-governance-toolkit**: Reject forbidden calls or invoke the permitted tool

**Value**: Tool execution follows explicit application policy rather than prompt-only requests

</details>
<!-- flow-steps:end -->

## Key techniques

- **Decide and audit before calling the tool.** [`agent-governance-python/agent-mesh/src/agentmesh/governance/govern.py:319–505`](https://github.com/microsoft/agent-governance-toolkit/blob/47abed7446d47e74cfa76d01a5913bb873ffcad9/agent-governance-python/agent-mesh/src/agentmesh/governance/govern.py#L319-L505) loads policy at construction, builds call context, checks any configured ring, evaluates policy and logs the decision before invoking `_fn`. Denial raises `GovernanceDenied` unless a caller-supplied denial callback handles it. The optional advisory check runs after deterministic allow; [`govern.py:965–1004`](https://github.com/microsoft/agent-governance-toolkit/blob/47abed7446d47e74cfa76d01a5913bb873ffcad9/agent-governance-python/agent-mesh/src/agentmesh/governance/govern.py#L965-L1004) shows ordinary classifier errors failing open. Its flag-for-review path does not block execution. This boundary protects calls routed through the wrapper, not arbitrary activity in the process.
- **Bind coordinated approval to the exact action.** [`govern.py:780–917`](https://github.com/microsoft/agent-governance-toolkit/blob/47abed7446d47e74cfa76d01a5913bb873ffcad9/agent-governance-python/agent-mesh/src/agentmesh/governance/govern.py#L780-L917) builds a canonical action binding and records request IDs, policy version, chain version and expiry. The coordinator path revalidates the action digest immediately before execution and records audit linkage; an expired, unpermitted or non-terminal approval denies. This stronger path is conditional on configuration, not proof that every legacy approval handler has the same semantics.
- **Expose host enforcement rather than claiming a verdict executes itself.** [`examples/acs-email-tool/run.py:27–52`](https://github.com/microsoft/agent-governance-toolkit/blob/47abed7446d47e74cfa76d01a5913bb873ffcad9/examples/acs-email-tool/run.py#L27-L52) calls `pre_tool_call`, returns without executing on denial, and substitutes transformed arguments before the tool call. It demonstrates the decision-to-side-effect handoff using a stand-in email function, not a real delivery test. The host must keep that branch connected for every relevant action.

## Tech stack

- **Python-first monorepo** — wrapper/governance code plus consolidated runtime, integration and CLI distributions; the current main core manifest is `5.0.0`. The policy host path delegates to upstream ACS via the `agent-control-specification` dependency and a Rust-core runtime.
- **CLI and SDKs** — README documents `agt doctor`, `agt verify`, `agt red-team scan`, `agt lint-policy`, Python `govern()`, TypeScript `PolicyEngine`, .NET MCP integration, Rust, and Go examples.
- **Agent framework adapters** — documented integrations include Microsoft Agent Framework, Semantic Kernel, AutoGen, LangGraph/LangChain, CrewAI, OpenAI Agents SDK, Claude Code, Google ADK, LlamaIndex, Haystack, Mastra, Dify, and MCP.

## Dependencies

- **Python 3.11+** for the reviewed main core/compliance manifests and README quick start; the generic prerequisites table still says 3.10+, so do not use that lower value for these packages. Other language minimums are adapter-specific and do not establish functional parity.
- **Package registries** — PyPI (`agent-governance-toolkit`), npm (`@microsoft/agent-governance-sdk` and related packages), NuGet, crates.io, plus source packages in the monorepo.
- **Optional Azure credentials** — README lists `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, and `AZURE_CLIENT_SECRET` for Azure-integrated features.
- **Framework-specific hooks** — real deployment depends on where you insert AGT into dispatch. Main core depends on `agent-control-specification`, Pydantic, PyYAML and cryptographic/HTTP/logging packages; Rego integration additionally needs the OPA CLI. Persistent wrapper audit requires a caller-managed HMAC key, not merely `audit=True`.

## Ops difficulty

**Medium to high.** `pip install agent-governance-toolkit[full]` and a two-line `govern()` wrapper are easy to try, but production rollout means defining policies, enforcement points, audit retention, identity/trust model, framework adapters, and OS/container boundaries.

## Health & viability

- **Maintenance snapshot (2026-10-13):** unarchived; main `47abed7` was committed that day. Maintenance and responsiveness score A; latest GitHub Release is `v4.1.0` from 2026-06-09, while reviewed main core manifests say `5.0.0`.
- **Adoption snapshot:** 6423 stars; this scorer run measured 125645 last-month PyPI downloads for `agent_governance_toolkit`, with adoption C. Stars and downloads do not prove enforcement coverage in your application.
- **License snapshot:** MIT verified from GitHub metadata and root `LICENSE` in the read-only upstream check.
- **Lindy / governance:** created 2026-03-02, with longevity C at 225 days, not D. The Microsoft-owned repository publishes governance/maintainer documents naming Microsoft and other organizations; contributor statistics yield governance A. Foundation-style charter language is not independent proof of foundation hosting or a support SLA.
- **Risk flags:** Public Preview status, broad package surface, and middleware-level security boundary are the main practical risks.

## Caveats (unverified)

- [未验证：no package installation or conformance run] Installed wheel contents, multi-language equivalence, the full conformance suite and real framework enforcement were not reproduced; this review read source, manifests and examples.
- [未验证：no production attack simulation or audit-retention deployment] Source-level deny branches do not establish end-to-end containment, classifier quality, persistent audit durability or external action success.
- [推断：Public Preview plus source/release version divergence] Pin and verify a compatible package set; the main migration surface cannot be assumed identical to the latest GitHub release or a registry wheel.
