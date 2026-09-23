# blockchain-dev-infrastructure

> 分类节点。EVM 与区块链开发网络的 faucet、本地链及配套测试基础设施。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **PoWFaucet** | 运营共享 EVM 测试网 faucet，需要分发运营方注资的原生币或 ERC-20 token，并配置奖励策略与模块化防滥用控制。 | C（5/6） | [→](powfaucet.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [PoWFaucet](powfaucet.zh.md) | ✅ | C（5/6） | 公共或社区 EVM faucet 需要分层防滥用与策略配置时选它；代价是热钱包托管、持久服务运维和 AGPL 义务。 |
| FaucetETH（上游名：FaucETH） | 未收录 | — | 只需带 hCaptcha 和多链配置的较小型传统 EVM faucet 时选它；控制面比 PoWFaucet 窄，但仍需承担钱包注资与私钥托管。 |
| Ethereum-Faucet | 未收录 | — | MIT 许可和紧凑实现比 PoWFaucet 的成熟模块集更重要时选它；更多防滥用与运维控制需要采用方自行补齐。 |
| Nethereum.Faucet | 未收录 | — | C#、.NET 与 Nethereum 技术栈需要 Blazor 前端和 REST API 时选它；它贴合该生态，但没有 PoWFaucet 那么丰富的工作量证明与身份模块。 |
| Foundry Anvil | 未收录 | — | 需要确定性的本地或临时 EVM 账户与预置余额时选它；它几乎零运维，但不能向既有共享测试网的用户分发资产。 |

## 什么该放这里

支持 EVM 或其他区块链开发网络的仓库：测试网 faucet、本地开发链、账户注资工具，以及运行或测试链上应用所需的相邻基础设施。生产资产分发、钱包、交易所和通用 CAPTCHA 系统应归入其他分类。
