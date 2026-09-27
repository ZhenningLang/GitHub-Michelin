# secrets-management

> 分类节点。你自建的、按身份发机器凭据的仓库——API 密钥、证书、数据库密码——带策略与审计。
> ← 返回[分类路由](../../INDEX.zh.md) · English：[INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **OpenBao** | 需要在 HashiCorp 改 Vault 许可证之后、用 MPL 自托管一套按身份把关的密钥服务端时用它——但它是你自己运维的 Raft／Postgres 集群，不是每个 Vault 插件的即插即用替代。 | B（6/6） | [→](openbao.zh.md) |

## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [OpenBao](openbao.zh.md) | ✅ | B（6/6） | MPL-2.0 加 OpenSSF 治理下的 Vault 形租约与屏障——集群自己跑，部分 Vault 插件没有。 |

## 什么该放这里

你自己运维、用来存放、签发、轮换和吊销**机器**密钥的服务端（API 密钥、证书、数据库密码、加密即服务）。不含人类密码管理器（那些和 Vaultwarden 一起在 ops-infra），不含没有运行时的 git 文件加密器（SOPS），也不含托管的云密钥 API。
