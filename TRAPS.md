# Engine traps

Measured facts about the engines this repository delegates to, kept because
each one is the product of the work and costs an afternoon to rediscover
(`CONTRIBUTING.md`: *The artifacts are instruments; the product is a map of
Sage*; `DEV-63` owns this file). A row is a finding, never a hypothesis: it
records the operation, the spelling measured, the specimen and its size
parameter, the wall times, the version, the command that reproduces it, and the
route chosen. A cost is a curve in the size parameter, or it is a single data
point and says so. `COMPLAINTS.md` holds the unresolved need; this file holds
the fact, which delivery uses and never resolves.

Read this file before choosing any engine route. Write to it in the turn the
measurement is made.

## Sage

### Importing `sage.all` costs about a second; one module costs a tenth of that

Per-invocation tooling that needs one Sage module pays for the whole library
when it imports `sage.all`, and almost nothing when it imports the module.
Single data points, not a curve: there is no size parameter.

| import | wall time, three runs |
| --- | --- |
| bare interpreter (`python -c pass`) | 0.74 s, 0.44 s, 0.46 s |
| `import sage.all` | 1.59 s, 1.11 s, 1.02 s |
| `from sage.graphs.graph import Graph` | 0.58 s, 0.53 s, 0.72 s |
| `from sage.topology.simplicial_complex import SimplicialComplex` | 0.48 s, 0.53 s, 0.50 s |
| `import sage.all`, then `Graph` | 1.34 s, 1.21 s, 1.22 s |
| `sage -c pass` (the launcher) | 1.02 s, 1.04 s, 0.93 s |

Sage 10.10.beta8, Python 3.14.7, the `.envrc` interpreter
`/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python`, 2026-09-16. The
first run of a set is slower; the steady value is the last two. Reproduce with:

```bash
PY=/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python
for i in 1 2 3; do /usr/bin/time -f '%e s' $PY -c 'from sage.graphs.graph import Graph'; done
```

Route chosen: a tool that runs once per invocation imports the module it
computes with, never `sage.all`. Spawning one Sage process per item is a design
defect at either import. Depends on this: the `category-graph` recipes
(TODO node `category-graph-engine`).

The `sage` on `PATH` is a symlink to `sage-dev-allopts/.venv/bin/sage`, a
Python script that accepts `-c` and rejects `-python`; time module imports with
the venv's `python` directly.

Importing `sage.topology.simplicial_complex` without `sage.all` prints
`UserWarning: Resolving lazy import ... during startup` three times on first
use. The results are unaffected; loading `sage.all` first silences it and
costs the second above.

### `Graph.minimum_cycle_basis()` takes integer vertices only, and costs seconds on a few hundred vertices

The default route is `sage.graphs.base.boost_graph.min_cycle_basis`. On string
vertices it raises `TypeError: an integer is required` (the edge set is a
`pair<int,int>`); relabel first with `relabel(return_map=True)` and map back.
Each returned cycle is a vertex set, not in cyclic order (its own docstring);
order it with `subgraph(cycle).cycle_basis()`.

Wall time on the declared category graph, 312 vertices, 397 edges, 88
independent cycles, one 2-connected block of 135 vertices holding 86 of them:

| call | wall time |
| --- | --- |
| `minimum_cycle_basis()` default, whole graph | 30.3 s |
| `minimum_cycle_basis(algorithm='NetworkX')`, whole graph | 8.2 s |
| `minimum_cycle_basis()` default, block by block | 6.6 s |
| `minimum_cycle_basis(algorithm='NetworkX')`, block by block | 1.8 s |
| `cycle_basis()` (spanning tree, not minimum) | milliseconds |
| `blocks_and_cut_vertices()`, `transitive_reduction()`, `level_sets()` | milliseconds |
| `SimplicialComplex(edges).homology(reduced=False)` default `'pari'` / `'dhsw'` | 0.19 s / 0.02 s |

Single graph, one run each, Sage 10.10.beta8, 2026-09-16; the shape of the
cost in the vertex count is not measured. Reproduce with `just category-graph
cells` (whole run about 9 s) and the calls above on `_graph(_declared_edges(...))`
from `dzack_research.utilities.category_graph`.

Route chosen: the cycle space is the direct sum over 2-connected blocks, so the
`cells` view computes the default basis per block and reports the blocks; a
large block is the audit finding, not an obstacle. The per-block cost is paid
once per run.

### An axiom applies to every declared supercategory, so a base-restriction edge asserts descent of every property

`CategoryWithAxiom.super_categories` (sage/categories/category_with_axiom.py,
`def super_categories`, Sage 10.10.beta8) returns the join of the base
category, `category._with_axiom_as_tuple(axiom)` for every supercategory of
the base, and `extra_super_categories()`. `_with_axiom_as_tuple`
(category.py) applies the axiom to any category whose class hierarchy
defines it, and `Modules(ZZ)` defines the same axioms as `Modules(QQ)`.
Consequence, read from source on 2026-09-16 and not executed: if `Modules(QQ)`
declared `Modules(ZZ)` (restriction of scalars), then
`Modules(QQ).FinitelyGenerated()` would have `Modules(ZZ).FinitelyGenerated()`
as a supercategory, which is false; the same for every property stated
relative to the base (finite type, smooth, projective, free of finite rank).
Absolute properties (commutative, associative, finite) descend truly, but the
mechanism cannot tell the two apart.

Route chosen: no owned category declares itself over a lower base. Restriction
of scalars is a functor obtained from the category, and a preservation
theorem on that functor states which properties descend. Depends on this: the
`Modules`, `Algebras` and `Schemes` bases (AGENTS.md, *Red flags*).

### `DiGraph.longest_path()` is a MILP by default; a DAG's longest chain is `level_sets()`

`longest_path(algorithm='MILP')` is the default and `'heuristic'` the only
alternative (its docstring). For an acyclic digraph, `level_sets()` puts a
vertex in level `k` exactly when its longest path from a source has `k` edges,
in `O(n + m)` (its docstring and body). The longest chain is
`len(level_sets()) - 1`, and the longest chain *from* each vertex to a sink is
its level in `reverse().level_sets()`. Verified on a seven-vertex DAG with a
shortcut edge; used by the `shape` view.

### `==` between symbolic variables is a proof attempt, and costs a coercion search

`SR.var("e_0") == SR.var("e_1")` is a symbolic equation, not a boolean.
Asking its truth (`bool`, `any`, `in` over a list of symbols) makes Sage try to
prove it, and one route evaluates the difference at random points of
`ComplexIntervalField` (`complex_interval_field.py`, `random_element`). A
membership test that scanned a list of symbolic labels with `==` made each
Gram entry of a lattice cost milliseconds and the star import take 460 s on
2026-09-23 (rank 4: 0.44 s, rank 8: 3.3 s per lattice, cubic).

Route chosen: decide membership of hashable points by hashing
(`sage.sets.set.Set`, a `frozenset`), never by comparing a candidate with every
point. Symbols hash consistently with identity of name.

### pytest-timeout's `SIGALRM` inside Cython code stops the whole run

With `--timeout-method=signal`, the alarm that pytest-timeout raises can land
inside a Sage `sig_on()` block. cysignals then raises
`cysignals.signals.AlarmInterrupt`, which pytest treats as an interrupt: the
run stops with "!!! cysignals.signals.AlarmInterrupt !!!" and the remaining
tests never execute. Observed on the 2026-09-23 triage run with
`--timeout=1`, at 84% of 16,311 tests. With the default per-test timeout
(`func_only` false) the alarm can also fire while pytest builds a failure
report, and pytest aborts with `INTERNALERROR ... Failed: Timeout`;
`-o timeout_func_only=true` confines the alarm to the test function.

Route chosen: a triage catalogue run resumes after the interrupted file; the
gated default run treats any test at its time limit as a failed run anyway.
