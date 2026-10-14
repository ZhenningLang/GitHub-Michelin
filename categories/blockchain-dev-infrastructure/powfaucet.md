---
name: PoWFaucet
slug: powfaucet
repo: https://github.com/pk910/PoWFaucet
category: blockchain-dev-infrastructure
tags: [evm, ethereum, testnet, faucet, proof-of-work, anti-abuse, token-distribution]
language: TypeScript
license: AGPL-3.0
maturity: v2.5.2, 5636 stars, new external module loader (as of 2026-10-14)
last_verified: 2026-10-14
type: service
upstream:
  pushed_at: 2026-10-13T22:26:23Z
  default_branch: master
  default_branch_sha: 92b8f7ba01a8ba694269bb35c1848966a3a8a75d
  archived: false
health:
  schema: 1
  computed_at: 2026-10-14T05:25:33Z
  overall: C
  overall_score: 2.2
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
        last_commit_age_days: 1
        active_weeks_13: 9
        carve_out: null
    responsiveness:
      grade: "?"
      raw: {}
    adoption:
      grade: D
      raw:
        registry: npmjs.org
        canonical_package: "@powfaucet/sdk"
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: "?"
        cross_check_divergence: null
        release_downloads: 4242
        release_assets: 210
        release_tier: D
        docker_pulls: 42916
        docker_image: pk910/powfaucet
        docker_tier: D
        signal_basis: releases+docker
        tier_source: releases+docker
    longevity:
      grade: A
      raw:
        repo_age_days: 1667
        last_commit_age_days: 1
        cohort: service
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 5
        top1_share: 0.821
        top3_share: 0.923
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: D
      raw:
        spdx_id: AGPL-3.0
        permissiveness: strong_network_copyleft
        relicense_36mo: false
        content_license: null
  unknowns:
    responsiveness: { reason: no_window_signal }
---

# PoWFaucet

Bots drain your testnet giveaway wallet through a simple address form; PoWFaucet makes recipients pass configurable checks before it queues transfers from your funded wallet.

![PoWFaucet health radar](../../assets/health/powfaucet.svg)

## When to use

You're operating a public or community EVM testnet whose users need small amounts of native currency or an ERC-20 token, but a simple address form is drained by bots. You are prepared to fund and secure a faucet hot wallet, connect reliable RPC endpoints, and run a persistent web service. PoWFaucet gives you a complete distribution service with transaction queues, wallet and outflow controls, SQLite or MySQL persistence, and optional protection modules for browser proof-of-work, CAPTCHA, IP reputation, recurring limits, GitHub identity, mainnet-wallet checks, Gitcoin Passport, Zupass, ENS, vouchers, and whitelists.

You choose it over a small faucet script when abuse resistance and configurable reward policy justify the larger operational surface. Browser proof-of-work spends computation to qualify for a payout; it does not create coins. You supply native currency and gas, and arrange the token supply for ERC-20 distribution. The demo token's separately granted minting role is not a way to mint arbitrary assets ([README.md:16–18](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/README.md#L16-L18), [docs/demo/README.md:3–4](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/docs/demo/README.md#L3-L4)).

## When NOT to use

- **You only need a local development chain.** Use Foundry Anvil rather than exposing a public giveaway service and its signing key.
- **You do not want to custody keys or replenish funds.** Use the target network's established public faucet or a trusted managed faucet; PoWFaucet requires an operator-funded wallet and incident ownership.
- **The chain is not EVM-compatible.** Use that chain's native faucet implementation and SDK; PoWFaucet's transaction, RPC, address, and token assumptions are Ethereum-oriented.
- **You are distributing valuable mainnet assets, an airdrop, or user entitlements.** Use an audited Merkle-claim or allowlist contract backed by a multisig treasury; a testnet faucet is not a high-value distribution control plane.
- **You only need to rate-limit a web form.** Keep protection inside your application; PoWFaucet adds unnecessary wallet, session and payout infrastructure.
- **You cannot meet AGPL obligations.** Do not adopt it without license review. Its AGPL v3 license includes source-offer obligations for modified versions used through a network; the health scorer's D bucket is not a legal analysis.
- **You require protection to fail closed at startup.** Audit enabled modules and startup logs: the loader skips modules that fail to load, and the application initialization catch exits with code 0, not a reliable readiness signal ([ModuleLoader.ts:249–280](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/loader/ModuleLoader.ts#L249-L280), [app.ts:74–76](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/app.ts#L74-L76)).

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| [FaucETH](https://github.com/komputing/FaucETH) | not indexed | Choose FaucETH for an hCaptcha-protected multi-chain address form; choose PoWFaucet when configurable mining sessions and reward policies decide the choice. | FaucETH's documented setup is narrower; both require operator funding and both declare AGPLv3. |
| [Nethereum.Faucet](https://github.com/Nethereum/Nethereum.Faucet) | not indexed | Choose its C# template when you need Blazor and REST inside a .NET stack; choose PoWFaucet for its browser proof-of-work and module hooks. | The template supplies a conventional funding API, not PoWFaucet's mining-session platform. |
| [Foundry Anvil](https://github.com/foundry-rs/foundry) | not indexed | Choose Anvil for a local Ethereum development node; choose PoWFaucet when independent users need payouts on an existing shared chain. | A local test chain avoids public wallet operations but does not fund users on that shared chain. |

## Quick start

Use the operator instructions linked from [README.md:63–69](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/README.md#L63-L69) to obtain a server distribution or Docker image; do not substitute the unstable `snapshot` release for a pinned stable artifact. Configure `faucet-config.yaml` with your chain, RPC address—the service that reads and broadcasts chain transactions—funded wallet and protection policy; secrets can be supplied through `FAUCET_ETH_WALLET_KEY` and `FAUCET_SECRET` instead of copied demo keys. For the browser-mining path, enable `modules.pow`, start the configured server and publish its web page behind TLS. A recipient enters a destination address, completes the configured mining session and claims the reward; the service checks the session and queues a wallet transfer. You pay for funding and transaction fees, maintain storage and RPC availability, and verify confirmations; this page did not run a faucet or transact.

![PoWFaucet — backbone user story](../../assets/flow/powfaucet.svg)

<!-- flow-steps:begin (generated from flows/powfaucet.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the server; configure chain, funded wallet and mining policy — `faucet-config.yaml` — component: `faucet server`
2. **PoWFaucet**: Load configured modules and expose the recipient page — component: `module loader / web server`
3. **You**: Have a recipient enter an address and complete browser mining
4. **PoWFaucet**: Release the mining block so the session can proceed — component: `PoW module`
5. **You**: Have the recipient claim the qualified reward
6. **PoWFaucet**: Check claim state and limits, then queue a funded-wallet transfer — component: `claim manager`

**Value**: Qualified recipients reach a controlled payout queue, not an unrestricted address form

</details>
<!-- flow-steps:end -->

## Key techniques

- **Make work gate eligibility, not mint money.** [PoWModule.ts:142–158](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/modules/pow/PoWModule.ts#L142-L158) adds a blocking mining task, resets the reward and creates a random session preimage; [PoWModule.ts:184–187](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/modules/pow/PoWModule.ts#L184-L187) releases that block when mining closes. This separates qualification from payout, but configuration can explicitly skip the module.
- **Recover and constrain the payout queue.** [EthClaimManager.ts:78–116](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/eth/EthClaimManager.ts#L78-L116) restores queued and pending claims from persisted sessions. [EthClaimManager.ts:187–231](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/eth/EthClaimManager.ts#L187-L231) checks claimable state, applies amount limits and guards duplicate claims; [EthClaimManager.ts:239–253](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/eth/EthClaimManager.ts#L239-L253) can pause for missing wallet funds or gas. Persistence helps recovery, not guaranteed chain finality.
- **Load extensions against the live faucet registry.** [ModuleLoader.ts:169–198](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/loader/ModuleLoader.ts#L169-L198) discovers program, data-directory and configured module paths; [ModuleLoader.ts:249–340](https://github.com/pk910/PoWFaucet/blob/92b8f7ba01a8ba694269bb35c1848966a3a8a75d/src/loader/ModuleLoader.ts#L249-L340) tries candidates, checks the API version and injects the shared SDK before registration. This avoids disconnected duplicate registries, but modules are executable trusted code and loading errors can leave the faucet running without them.

## Tech stack

- **Server:** TypeScript on Node.js, HTTP and WebSocket APIs, `web3` and Ethereum transaction libraries.
- **Client:** React 19, React Router, Bootstrap, Webpack, and Web Workers for proof-of-work algorithms.
- **Persistence:** SQLite by default or MySQL for higher-traffic and separated database deployments.
- **Proof-of-work:** bundled WASM implementations for Argon2, scrypt, CryptoNight, and the optional `nickminer` mode.
- **Packaging:** release archives and standalone binaries, plus a multi-stage Docker image combining Node.js with unprivileged Nginx.

## Dependencies

- An EVM execution-layer RPC endpoint, chain ID, funded hot-wallet private key, and enough native coins or ERC-20 tokens to distribute.
- Persistent SQLite storage or MySQL, plus disk for configuration, logs, session state, and optional passport caches.
- A version-compatible Node.js runtime or the published Docker image. The checked Dockerfile uses Node 22, while all-in-one release descriptions embed Node 18; this is not proof that every fresh dependency supports Node 18.
- A reverse proxy and TLS for public production deployment; the Docker image includes Nginx for static files and API/WebSocket proxying.
- Optional external credentials for hCaptcha, reCAPTCHA, Turnstile, GitHub OAuth, Gitcoin Passport, identity providers, and third-party IP information.

## Ops difficulty

**High.** The service holds a transaction-signing key, sends real on-chain transfers, persists user and session state, depends on RPC health, and exposes public HTTP and WebSocket surfaces. Operators must manage wallet funding, gas limits, pending transaction queues, database backups and migrations, rate and outflow policy, secrets, TLS, monitoring, abuse response, and upgrades. The optional vault contract can limit hot-wallet exposure, but adds contract configuration and on-chain failure modes rather than removing custody risk.

## Health & viability

- **Measured signals (2026-10-14):** A/?/D/A/D/D, overall C with 5/6 axes scored. The existing responsiveness gap remains `no_window_signal`: the scorer found traffic but no qualifying response in its sampled window, not proof of slow responses.
- **Maintenance:** v2.5.2 was published on 2026-10-13; the checked default branch includes the external module loader and runtime secret overrides. The repository is not archived; only 2.x is supported in `SECURITY.md`.
- **Governance:** 5 measured active maintainers, with top-1 share 0.821, produce D rather than the old C. The security policy explicitly names the primary maintainer; community contributors do not eliminate concentration risk.
- **Age and Lindy:** created in 2022 and still active after roughly four years, with public Sepolia, Hoodi, and Ephemery instances named in the README. This is a useful but not long-established infrastructure track record.
- **Adoption:** 5636 stars and the README's named instances show interest, not security or load capacity. The measured install signals give D; the SDK's dependent count is not the number of faucet deployments.
- **Risk flags:** AGPL network obligations, hot-wallet custody, many optional secrets and identity integrations, privacy-sensitive IP and wallet data, external RPC dependencies, and public abuse economics.

## Caveats (unverified)

- [未验证：未执行上游] Installation, runtime compatibility, wallet/RPC failure recovery and chain transfers were not tested here; source and release descriptions are the evidence.
- [未验证：未取得独立审计或压测] Security and capacity under concurrent mining, RPC failures and malicious verifiers remain unproven.
- [未验证] The effectiveness and fairness of CAPTCHA, IP, GitHub, Passport, Zupass, and proof-of-work modules depend on operator configuration and external services.
- [未验证] The public instances listed in the README may run configurations or patches that differ from the default branch.
- [推断] The primary category is blockchain development infrastructure because token distribution is the service's purpose; CAPTCHA and proof-of-work are optional anti-abuse modules.
- [推断] The low bus factor raises long-term maintenance risk despite active releases and a substantial test suite.
