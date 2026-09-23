# blockchain-dev-infrastructure

> Category node. EVM and blockchain development-network faucets, local chains, and supporting test infrastructure.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **PoWFaucet** | Operate a shared EVM testnet faucet with operator-funded native coins or ERC-20 tokens, configurable reward policy, and modular anti-abuse controls. | C (5/6) | [→](powfaucet.md) |

## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [PoWFaucet](powfaucet.md) | ✅ | C (5/6) | Pick for a public or community EVM faucet that needs layered abuse controls and policy knobs; pay for that breadth with hot-wallet custody, persistent service operations, and AGPL obligations. |
| FaucetETH (upstream: FaucETH) | 未收录 | — | Pick for a smaller conventional EVM faucet with hCaptcha and multi-chain configuration; it has a narrower control surface than PoWFaucet and does not remove wallet-funding or custody work. |
| Ethereum-Faucet | 未收录 | — | Pick when an MIT-licensed, compact faucet implementation matters more than PoWFaucet's mature module set; the adopter must supply more abuse prevention and operational controls. |
| Nethereum.Faucet | 未收录 | — | Pick for a C#/.NET and Nethereum stack with a Blazor front end and REST API; it fits that ecosystem but lacks PoWFaucet's breadth of proof-of-work and identity modules. |
| Foundry Anvil | 未收录 | — | Pick for deterministic local or ephemeral EVM accounts with pre-funded balances; it is nearly zero-ops but does not distribute assets to users on an existing shared testnet. |

## What belongs here

Repositories that support EVM or other blockchain development networks: testnet faucets, local development chains, account-funding utilities, and adjacent infrastructure used to run or test chain applications. Production asset distribution, wallets, exchanges, and general-purpose CAPTCHA systems belong elsewhere.
