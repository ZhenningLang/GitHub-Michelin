# optimization-solvers

> Category node. Libraries and solvers that take a *declared* optimization model — assignment, LP/MIP, constraint satisfaction, resource allocation — and search for a good or provably optimal solution, instead of you hand-rolling the search.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **Rebalancer** | Use it when the job is "re-place these objects under these policies" at shard/host scale — capacity, balance, failure-domain spread, minimize-movement — and you would rather declare named specs plus a tuned local search than write a linear program. | B (5/6) | [→](rebalancer.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [Rebalancer](rebalancer.md) | ✅ | B (5/6) | Meta's assignment DSL + scalable local search with a MIP (HiGHS/Gurobi/Xpress) fallback on the same model — narrow, three months old, and its source build pulls in Folly/fbthrift. |
| OR-Tools · HiGHS · Timefold / OptaPlanner · Gurobi / Xpress | 未收录 | — | General LP/MIP/CP solvers and heuristic planners — far broader and longer-lived, but you write the model and the search yourself; Rebalancer's MIP path already calls HiGHS, Gurobi and Xpress, so those are its backends before they are its rivals. |

## What belongs here

Solvers, modelling layers and planners for **mathematical optimization**: assignment and resource allocation, LP/MIP/integer programming, constraint satisfaction, and the modelling DSLs built on top. Not ML research demos and evolutionary frameworks (see `ml-research`), not DAG pipeline orchestrators (see `workflow-orchestration`), not in-cluster schedulers or job queues (see `task-queue`).
