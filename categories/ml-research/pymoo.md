---
name: pymoo
slug: pymoo
repo: https://github.com/anyoptimization/pymoo
category: ml-research
tags: [optimization, multi-objective, evolutionary-algorithms, nsga2, genetic-algorithm, python, operations-research]
language: Python
license: Apache-2.0
maturity: v0.6.x, active (last pushed 2026-06), ~2.9k stars (as of 2026-06)
last_verified: 2026-06-28
type: library
upstream:
  pushed_at: 2026-06-28T22:14:17Z
  default_branch: main
  default_branch_sha: 04c77b4cbb01a51cd98be8ad74774d4ea588e35a
  archived: false
health:
  schema: 1
  computed_at: 2026-07-03T14:50:12Z
  overall: C
  overall_score: 2.17
  scored_axes: 6
  capped: false
  cap_reason: null
  needs_human_review: false
  axes:
    maintenance:
      grade: B
      raw:
        archived: false
        last_commit_age_days: 4
        active_weeks_13: 2
        carve_out: null
    responsiveness:
      grade: D
      raw:
        median_ttfr_hours: 752.4
        qualifying_issues: 6
        band: default
        window_offset_days: 3
    adoption:
      grade: E
      raw:
        registry: null
        canonical_package: null
        dependent_repos_count: 0
        downloads_last_month: null
        graph_tier: E
        volume_tier: null
        cross_check_divergence: null
        archived: false
    longevity:
      grade: A
      raw:
        repo_age_days: 3209
        last_commit_age_days: 4
        cohort: library
    governance:
      grade: D
      raw:
        active_maintainers_12mo: 12
        top1_share: 0.857
        top3_share: 0.901
        window_source: stats_contributors
        carve_out: null
    risk_license:
      grade: A
      raw:
        spdx_id: Apache-2.0
        permissiveness: permissive
        relicense_36mo: false
        content_license: null
---

# pymoo

A Python framework for single- and multi-objective optimization: NSGA-II/III, MOEA/D, GA, DE, CMA-ES, PSO and more, plus test problems, constraint handling, visualization, and decision-making tools — built on NumPy/SciPy with optional compiled speedups.

![pymoo — health radar](../../assets/health/pymoo.svg)

## When to use

You're a researcher or engineer with an optimization problem that has **multiple conflicting objectives** — minimize cost *and* weight, maximize throughput *and* reliability — and you need to find the Pareto front, not a single scalar optimum. You define a `Problem` (variables, objectives, constraints), pick an algorithm like `NSGA2`, call `minimize(problem, algorithm, termination)`, and pymoo evolves a population toward the trade-off frontier; then you use its visualization (scatter, PCP) and decision-making modules (e.g. pseudo-weights, compromise programming) to pick a solution. It ships the standard benchmark suites (ZDT, DTLZ, WFG) so you can validate an algorithm before pointing it at your real problem, and it handles mixed/integer variables, constraints, and custom operators.

You reach for it as the **de-facto Python library for evolutionary multi-objective optimization** — when you want well-tested implementations of the canonical algorithms (it's the reference for NSGA-II/III in Python) with a clean, extensible API, rather than re-implementing genetic operators yourself or wiring up a heavier OR solver. [推断]

## When NOT to use

- **Your problem is convex / linear / smooth and single-objective.** For LP/QP/convex problems, a proper solver (SciPy, CVXPY, Gurobi/OR-Tools) is vastly faster and gives optimality guarantees that population metaheuristics do not. Don't bring an evolutionary algorithm to a problem gradient descent or an LP solver owns.
- **You need gradient-based / large-scale continuous optimization.** Evolutionary methods are derivative-free and sample-hungry; for high-dimensional differentiable objectives, gradient methods (PyTorch/JAX, scipy.optimize) converge far more efficiently.
- **Each evaluation is very expensive and you have a tiny budget.** Population EAs need many function evaluations; if a single objective eval costs hours, look at Bayesian/surrogate optimization (Ax/BoTorch, Optuna) instead, or pymoo's surrogate-assisted patterns with care. [推断]
- **You want hyperparameter tuning specifically.** Optuna/Ax are purpose-built for that workflow (pruning, dashboards, trial storage); pymoo is a general optimization framework, not an HPO platform.
- **You can't tolerate stochastic, non-reproducible-by-default results.** EAs are randomized; you must fix seeds and run multiple times to characterize performance — that's inherent, not a bug.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| DEAP | 未收录 | Choose DEAP when you need a flexible low-level evolutionary-computation toolkit. | Flexible evolutionary-computation toolkit; very general/low-level, but you assemble more yourself — pymoo gives higher-level, ready multi-objective algorithms and benchmarks. |
| Platypus | 未收录 | Choose Platypus when you need another Python multi-objective EA library. | Another Python multi-objective EA library; smaller scope/community than pymoo's algorithm + tooling breadth. [推断] |
| Optuna / Ax (BoTorch) | 未收录 | Choose Optuna or Ax when you need Bayesian/surrogate optimization for expensive evaluations or HPO. | Bayesian/surrogate optimization, ideal for expensive evaluations and HPO; different paradigm (sample-efficient, not population-based) — complementary, not a drop-in. |
| jMetal (Java/Py) | 未收录 | Choose jMetal when you need an established multi-objective metaheuristics framework in the Java/Python ecosystem. | Established multi-objective metaheuristics framework; jMetalPy mirrors it in Python — comparable goals, different ecosystem and API style. |
| [OR-Tools](../optimization-solvers/or-tools.md) | ✅ | Choose OR-Tools when your problem is structured — linear, integer or routing — and you want an exact answer inside the same Python process; choose pymoo when the objectives genuinely conflict and what you need is a trade-off front, not one optimum. | OR-Tools returns an optimum with a bound but requires the problem to be written as a model; pymoo takes an arbitrary evaluation function and hands back a Pareto set with no optimality guarantee and far more evaluations. |
| SciPy / Gurobi | 未收录 | Choose SciPy when a single-objective LP/convex problem fits `scipy.optimize` and you already depend on it; choose Gurobi when a hard MIP needs commercial performance. Neither is indexed here: SciPy is a general scientific-computing library rather than an optimization solver, and Gurobi is closed-source with no repository. | Exact/convex/MILP solvers; the right tool when your problem is structured, where EAs are the wrong hammer. They are complementary to pymoo rather than substitutes — you reach for them when the problem stops being a black-box multi-objective search. |

## Tech stack

- **Language:** Python (>= 3.10 per `pyproject.toml`).
- **Numeric core:** NumPy + SciPy; `autograd`, `cma`, `moocore` for specific algorithm/metric support; `matplotlib` for visualization; `alive_progress` for progress.
- **Speedups:** some modules ship optional **Cython-compiled** versions for performance (build via the included setup); pure-Python fallback exists if compilation didn't run.
- **Surface:** `Problem`/`Algorithm`/`minimize` API, operator library (sampling/crossover/mutation), test-problem suites, visualization, and MCDM/decision-making modules.

## Dependencies

- **Runtime:** `numpy`, `scipy`, `matplotlib`, `moocore`, `autograd`, `cma`, `alive_progress`, `Deprecated` — all pip-installable, no external services.
- **Build (optional):** a C compiler + `Cython` to build the compiled speedups from source; `pip install pymoo` ships wheels for the common case.
- **Hardware:** CPU-bound; no GPU required (or used) by the core algorithms.
- **Your problem:** you supply the objective/constraint evaluation — that's where real-world cost lives (e.g. wrapping a simulator).

## Ops difficulty

**Low.** It's a pip-installable library with no services, datastores, or deployment — `pip install -U pymoo` and import. The only operational nuances are: optionally compiling the Cython modules for speed (a build-time concern, with a pure-Python fallback), and the inherent cost of *your* objective function — for expensive simulators you'll manage parallel evaluation (pymoo supports parallelized/vectorized evaluation) and run-time budgets, but that's your problem's cost, not pymoo's. Reproducibility requires fixing random seeds. There is nothing to operate beyond the Python process.

## Health & viability

- **Responsiveness**: Grade D — median first-response time 752.4 hours across 6 qualifying issues/PRs.
- **Maintenance (2026-06).** Last pushed **2026-06-28** (the day of verification) with only ~2 open issues — strong signs of an **actively maintained, well-tended** project on the v0.6.x line. Not coasting, not abandoned. [推断]
- **Governance / backing.** Developed under the `anyoptimization` org (Organization-owned) with a lead maintainer (blankjul) and a real contributor list; tied to academic work (the pymoo IEEE Access paper). Bus factor leans on the lead maintainer but with org structure and multiple contributors — healthier than a lone-author repo. [推断]
- **Age & Lindy verdict.** Created 2017-09 (~8–9 years) **and still actively shipping** ⇒ a **strong Lindy** signal: a mature, long-proven library that remains current, not a hyped newcomer. [推断]
- **Adoption.** ~2.9k stars / ~475 forks, a citable paper, and use across academic/industrial optimization work; it is a standard reference for NSGA-II/III in Python. [未验证]
- **Risk flags.** Few. Apache-2.0 (permissive, no relicense history found); the main practical caveat is the general EA caveat (stochastic, evaluation-hungry), not a project-health risk. [推断]

## Caveats (unverified)

- [未验证] ~2.9k stars / ~475 forks / ~2 open issues as of 2026-06; counts are date-sensitive and indicative only.
- [未验证] v0.6.x is the current line (tags 0.6.2 / 0.6.1.x observed); the exact latest patch version and its release date are not pinned here.
- [推断] "De-facto / reference Python library for evolutionary multi-objective optimization" is an inference from adoption + the canonical algorithm set + the paper, not a measured ranking against every alternative.
- [推断] "Wheels ship for the common case so you rarely need to compile Cython" is inferred from typical PyPI packaging; verify for your platform if compiled-speed paths matter.
