# optimization-solvers

> Category node. Libraries, engines and planners that take a *declared* optimization model — assignment, LP/MIP, constraint satisfaction, resource allocation — and search for a good or provably optimal solution, instead of you hand-rolling the search.
> ← back to [category route](../../INDEX.md) · 中文：[INDEX.zh.md](INDEX.zh.md)

## Projects in this category

| Project | Use when | Health | Page |
| --- | --- | --- | --- |
| **OR-Tools** | Use it when the problem is combinatorial and broad — routing, scheduling, packing, assignment — and you want one suite covering CP-SAT, LP/MIP wrappers and routing behind Python/Java/.NET/C++ bindings. | A (6/6) | [→](or-tools.md) |
| **HiGHS** | Use it when the model already exists as a matrix or an MPS/LP file and you want a dependency-free, MIT-licensed LP/QP/MIP engine with no modelling layer in the way. | A (6/6) | [→](highs.md) |
| **Rebalancer** | Use it when the job is "re-place these objects under these policies" at shard/host scale — capacity, balance, failure-domain spread, minimize-movement — and you would rather declare named specs plus a tuned local search than write a linear program. | B (5/6) | [→](rebalancer.md) |
| **Timefold Solver** | Use it when the plan is governed by long lists of soft business rules over rich domain entities on the JVM — rostering, routing, timetabling — and the rules must stay editable as Java. | B (6/6) | [→](timefold-solver.md) |
| **OptaPlanner** | Read it only to understand or migrate an existing 9.x codebase: the repository is archived, its code moved into Apache KIE Drools, and new work belongs on Timefold Solver. | C (4/6) | [→](optaplanner.md) |


## Comparison matrix

| Option | Indexed | Health | One-line tradeoff |
| --- | --- | --- | --- |
| [OR-Tools](or-tools.md) | ✅ | A (6/6) | Google's combinatorial suite — CP-SAT, Glop/PDLP, MIP wrappers, routing — behind one install in four languages; you write the model and pay in dependency size. |
| [HiGHS](highs.md) | ✅ | A (6/6) | A dependency-free MIT LP/QP/MIP engine, reachable as `highs model.mps` or an embedded library — it is only the solve, so bring your own model. |
| [Rebalancer](rebalancer.md) | ✅ | B (5/6) | Meta's assignment DSL plus a scalable local search with a MIP (HiGHS/Gurobi/Xpress) fallback on the same model — narrow, three months old, and its source build pulls in Folly/fbthrift. |
| [Timefold Solver](timefold-solver.md) | ✅ | B (6/6) | Score-based planning on the JVM (the OptaPlanner lineage, maintained) — best when the rules are soft, numerous and frequently edited; open-core with a commercial Enterprise Edition. |
| [OptaPlanner](optaplanner.md) | ✅ | C (4/6) | The archived origin of that lineage: read it as a pattern source or a migration target, never as a new dependency. |
| Gurobi · FICO Xpress | 未收录 | — | Commercial closed-source MIP engines with per-seat licensing and support — no public repository to index; OR-Tools and Rebalancer can both call them. |

## What belongs here

Solvers, modelling layers and planners for **mathematical optimization**: assignment and resource allocation, LP/MIP/integer programming, constraint satisfaction and constraint programming, and the modelling DSLs built on top. Not ML research demos and evolutionary frameworks (see `ml-research`), not DAG pipeline orchestrators (see `workflow-orchestration`), not in-cluster controllers that only apply a placement inside Kubernetes (see `dev-utilities/ops-infra`) or job queues (see `task-queue`).
