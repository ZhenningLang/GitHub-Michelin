# auth

> 分类节点。认证与授权库——登录提供方与权限规则。
> ← 返回[分类路由](../../INDEX.zh.md) · English: [INDEX.md](INDEX.md)

## 本分类项目

| 项目 | 何时用 | 健康度 | 页面 |
| --- | --- | --- | --- |
| **Authomatic** | 当需要框架无关的 Python 应用通过 OAuth1／OAuth2／OpenID 实现轻量「用 X 登录」、且会话持久化自己负责时用它——但它迭代缓慢，而认证库修复迟缓本身就是安全风险。 | C（5/6） | [→](authomatic.zh.md) |
| **django-rules** | 当 Django 的对象级权限是由逻辑（谓词）计算得出、而非存储授权、且不想加数据库表时用它——但若管理员需在运行时为单个对象分配权限，则应改用 django-guardian。 | B（4/6） | [→](django-rules.zh.md) |
| **Keycloak** | Open Source Identity and Access Management For Modern Applications and Services | A（6/6） | [→](keycloak.zh.md) |
| **Casbin** | Apache Casbin: an authorization library that supports access control models like ACL, RBAC, ABAC. | B（5/6） | [→](casbin.zh.md) |
| **OpenFGA** | A high performance and flexible authorization/permission engine built for developers and inspired by Google Zanzibar | A（5/6） | [→](openfga.zh.md) |


## 对比矩阵

| 选项 | 是否收录 | 健康度 | 一句话取舍 |
| --- | --- | --- | --- |
| [Authomatic](authomatic.zh.md) | ✅ | C（5/6） | 当需要框架无关的 Python 应用通过 OAuth1／OAuth2／OpenID 实现轻量「用 X 登录」、且会话持久化自己负责时用它——但它迭代缓慢，而认证库修复迟缓本身就是安全风险。 |
| [django-rules](django-rules.zh.md) | ✅ | B（4/6） | 当 Django 的对象级权限是由逻辑（谓词）计算得出、而非存储授权、且不想加数据库表时用它——但若管理员需在运行时为单个对象分配权限，则应改用 django-guardian。 |
| （各页对比里点到的替代品） | 未收录 | — | 详见各页 Comparison。 |

## 什么该放这里

主要职责是**认证或授权**的库——登录/OAuth 提供方、权限/规则引擎。
