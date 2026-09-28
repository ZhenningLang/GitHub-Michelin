---
name: Cython
slug: cython
repo: https://github.com/cython/cython
category: python-tooling
tags: [python, c, compiler, performance, extension-modules, native]
language: Cython
license: Apache-2.0
maturity: v3.3.x, active (2026-09), ~10.9k stars
last_verified: 2026-09-28
type: tool
upstream:
  pushed_at: 2026-09-27T23:56:58Z
  default_branch: master
  default_branch_sha: 418acffa8c56b1b8767ab9993a5cdfb81d9e766f
  archived: false
health:
  schema: 1
  computed_at: 2026-09-28T08:23:53Z
  overall: A
  overall_score: 3.67
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
        active_weeks_13: 13
        carve_out: null
    responsiveness:
      grade: A
      raw:
        median_ttfr_hours: 3.0
        qualifying_issues: 46
        band: relaxed_solo
        window_offset_days: 9
        source: issue
        inferred: false
    adoption:
      grade: A
      raw:
        registry: pypi.org
        canonical_package: cython
        dependent_repos_count: 18920
        downloads_last_month: 78291231
        graph_tier: A
        volume_tier: A
        cross_check_divergence: 1.0
        homebrew_installs_90d: 1859
        homebrew_tier: B
        release_downloads: 1014046
        release_assets: 3120
        release_tier: B
        signal_basis: homebrew+releases
        tier_source: registry
    longevity:
      grade: A
      raw:
        repo_age_days: 5790
        last_commit_age_days: 0
        cohort: tool
    governance:
      grade: C
      raw:
        active_maintainers_12mo: 48
        top1_share: 0.612
        top3_share: 0.925
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

# Cython

A profiled Python inner loop crawls — pixel math, a parser, an N-body step — and rewriting it in C costs you the Python ergonomics you kept. Cython is a compiler that turns Python (plus optional C-type declarations) into C, built into a native CPython extension module, so the hot part runs near C speed while everything else stays Python.

![cython — health radar](../../assets/health/cython.svg)

## When to use

You profiled your Python program and found a tight numeric loop that dominates the runtime — pixel math, a parser inner loop, an N-body step. Rewriting the whole thing in C is overkill and you'd lose the Python ergonomics, but the pure-Python loop is just too slow. You rename the module `.py` → `.pyx`, add a few `cdef int`/`cdef double` type annotations to the hot variables, compile it with Cython into a C extension, and the loop now runs at near-C speed while the rest of your code stays Python. You didn't rewrite your program; you compiled the part that mattered.

You also reach for Cython when you need to **wrap a C or C++ library** and expose it to Python: you write a thin `.pyx` that declares the external `cdef extern from "lib.h"` signatures and Python-facing wrappers, and Cython generates the glue C that builds into an importable module. It's the workhorse behind a large slice of the scientific Python stack — many packages ship Cython-generated extensions — so it's the proven path when `ctypes`/`cffi` feel too loose or too slow and you want compiled, typed, statically-checkable bindings.

## How it works

Cython is a transpiler plus a language. It reads a `.py` or `.pyx` file and writes **C source** that talks to the CPython C-API; your ordinary C compiler then builds that C into an importable extension module (`.so`/`.pyd`). The speed comes from the optional type declarations: `cdef int a = 0` tells the compiler `a` is a machine integer, so the loop increments a raw register value instead of boxing an object, refcounting it, and dispatching `+` at runtime — untyped code still works, it just keeps Python's dynamic cost. To wrap an existing C/C++ library you declare its signatures in a `cdef extern from "header.h"` block and Cython generates the glue. What it does for you: code generation, the `cythonize()` hook you drop into `setup.py`, a one-shot `cythonize -i` CLI, and a Jupyter `%%cython` magic for experiments. What stays yours: a working C toolchain on every build platform, the wheel matrix if you distribute a library, and the profiling that tells you which loop is worth renaming to `.pyx` in the first place.

![Cython — backbone user story](../../assets/flow/cython.svg)

<!-- flow-steps:begin (generated from flows/cython.json by tools/flow_card.py — do not edit) -->
<details>
<summary>Text version of the flow</summary>

1. **You**: Install the compiler into your Python environment — `pip install Cython`
2. **You**: Type the hot loop in a .pyx file — `cdef int a = 0`
3. **You**: Compile the file in place — `cythonize -i filename.pyx`
4. **Cython**: Translates it to C and builds a native CPython extension module — component: `generated C + your C compiler`
5. **You**: Import it like any other module — typed loop now runs at near-C speed

**Value**: A profiled bottleneck running at C speed with one file renamed and a few cdef lines — the rest of the program stays plain Python

</details>
<!-- flow-steps:end -->

## When NOT to use

- **Your bottleneck is I/O or already-vectorized.** If the slow part is network/disk waiting, or already runs in NumPy/pandas C code, compiling your Python loop won't help — fix the algorithm or the I/O, not the language.
- **You want zero build step / pure-Python distribution.** Cython introduces a **C compiler and a build/wheel pipeline**; if you need a pip-installable pure-Python package with no compilation, that cost may not be worth it. Consider Numba (JIT, no separate build) or PyPy.
- **You'd be better served by a JIT.** For numeric kernels, **Numba** can give big speedups with a decorator and no C toolchain; for whole-program speed, **PyPy** may beat hand-Cythonizing — Cython shines when you want explicit C-level control and stable ABI extensions.
- **You're writing greenfield performance code with no Python-interop need.** If you don't need to live inside CPython, writing the component directly in C/C++/Rust (and binding via PyO3/pybind11) may be cleaner than the Cython superset.
- **You can't tolerate the .pyx/typing learning curve.** Getting real speedups requires understanding `cdef`, typed memoryviews, GIL handling, and the C build; naive Cythonization of untyped code yields little.

## Comparison

| Alternative | In index | Our verdict | Tradeoff |
|---|---|---|---|
| Numba | 未收录 | Choose Numba for decorator-based numeric JIT when array/loop kernels matter more than extension ABI or C/C++ wrapping. | No separate C build and strong for numeric kernels, but narrower in scope and tied to a runtime-JIT model. |
| PyPy | 未收录 | Choose PyPy for whole-program no-code-change JIT experiments before hand-Cythonizing targeted modules. | Can speed whole programs, but C-extension compatibility and ecosystem fit can be the catch. |
| pybind11 / nanobind | 未收录 | Choose pybind11 or nanobind when the performance-critical code is already C++ and Python only needs bindings. | Ideal for C++ libraries, but you write C++, not a Python superset. |
| cffi / ctypes | 未收录 | Choose cffi or ctypes for thin C FFI when compiling a custom CPython extension would be unnecessary overhead. | Simpler for calling C, but no compiled-speed Python and weaker static typing than Cython. |
| mypyc | 未收录 | Choose mypyc when standard type-annotated Python is the source of truth and Cython-specific syntax is unacceptable. | Closer to "compile my Python" with standard typing, but younger and narrower than Cython. |
| Rust + PyO3 | 未收录 | Choose Rust + PyO3 when the hot component should be rewritten in Rust rather than kept in a Python-superset language. | Memory-safe and fast, but it brings a different language and toolchain. |

## Tech stack

- **What it is:** a compiler written largely in Cython/Python that emits **C** (and can target C++), which a C compiler then builds into a CPython extension module. [推断]
- **Language model:** Python plus optional C type declarations (`cdef`, typed memoryviews, `cpdef`, `nogil`), pure-Python mode annotations, and `extern` blocks to bind C/C++ APIs.
- **Build integration:** `cythonize()` in setup.py / build backends, plus Jupyter `%%cython` magic for inline use; produces standard wheels.
- **Targets:** CPython (the primary target); generated C is portable across the platforms CPython supports.

## Dependencies

- **Runtime (of generated modules):** just CPython — a Cython-built extension imports like any other compiled module, with no Cython runtime dependency for end users.
- **Build-time:** a **C compiler** (and a C++ compiler if targeting C++) plus the CPython development headers; Cython itself is a pip-installable Python package.
- **Optional:** a build backend (setuptools/meson) for packaging; NumPy headers if you compile against its C API. [未验证]

## Ops difficulty

**Low-to-medium, and it's build-time, not runtime.** Once compiled, the resulting extension is just an importable module — no service, no ops. The burden is the **build pipeline**: you need a working C toolchain on every build platform, and shipping a library means producing wheels for each OS/Python-version combination (manylinux, macOS, Windows), which is the usual native-extension packaging chore. Debugging compiled Cython (gdb, typed-vs-object pitfalls, GIL bugs) is harder than debugging pure Python. For a single app on one platform it's easy; for a widely-distributed library the matrix is the work.

## Health & viability

- **Responsiveness**: Grade A — median first-response time 3.0 hours across 46 qualifying issues/PRs.
- **Maintenance (2026-09).** Last pushed 2026-09-27; releases are frequent and current — 3.2.8 (2026-06-24) and 3.2.9 (2026-07-24) on the 3.2 line, then **3.3.0 stable on 2026-08-22** (GitHub releases) — clearly **very active**. Not archived.
- **Governance / bus factor.** Organization-owned (`cython`) with a deep, long-standing core team (scoder/Stefan Behnel, robertwb/Robert Bradshaw, da-woods, dalcinl, and others) — a real multi-maintainer project, not a one-person repo. [推断]
- **Age & Lindy verdict.** This repo dates to 2010-11 (~15 years) and Cython's lineage (from Pyrex) is older still; **continuously active for over a decade** ⇒ **very strong Lindy**. It is foundational infrastructure under much of scientific Python. [推断]
- **Adoption.** ~10.9k stars, 1.6k forks, and an enormous transitive install base — a large fraction of the PyData/scientific ecosystem ships Cython-compiled extensions; 78,291,231 PyPI downloads last month (health scorer, 2026-09-28; the README itself cites "more than 70 million"). Apache-2.0 licensed. [未验证]
- **Risk flags.** Few — permissive license, broad governance, heavy real-world dependency. The realistic "risk" is fit, not viability: a JIT (Numba/PyPy) or a Rust binding may suit a given task better than the Cython superset.

## Caveats (unverified)

- [未验证] ~10.9k stars, 1629 forks, 1527 open issues as of 2026-09 — volatile, date-sensitive; the large open-issue count is consistent with a big, old, widely-used project, not a red flag on its own.
- [未验证] Latest release observed: 3.3.0 stable (2026-08-22, GitHub releases API); release lines and dates shift, verify the current stable line before pinning.
- [推断] The compiler-emits-C / targets-CPython architecture and the typed-superset language model are described from Cython's documented design and the `language: Cython` metadata, not a source audit.
- [未验证] Exact build-time dependencies (which C/C++ compilers, NumPy headers, build backend) depend on your target and packaging choices; verify against current Cython docs.
