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

### `Localization.is_unit` answers True for any nonzero element of a number-field order

`Localization(O, S).is_unit` returns
`_cut_off_extra_units_from_base_ring_element(numerator).is_unit()`, whose
first test is `x.numerator().is_unit()` (`sage/rings/localization.py` 448,
872). For an element of a number-field order, `numerator()` is an element of
the field, where every nonzero element is a unit, so the localization reports
every nonzero numerator a unit. Specimen, Sage alone (no preamble):
`QuadraticField(-1, "a").maximal_order().localization((2,))(3).is_unit()` is
`True`, although 3 is prime in `Z[i]` and `S = {2^k}`; `ZZ.localization((2,))(3)`
answers `False` correctly. Sage 10.10.beta8, 2026-09-25.

Route chosen: a localization of a number-field order decides units from the
definition in the source ring -- `a/s` is a unit exactly when saturating `(a)`
by the inverted elements gives the unit ideal
(`LocalizationRings.ElementMethods.is_unit`).  Other sources keep the engine's
decision, which is exact when numerators lie in the source ring; the owned
ideal machinery cannot yet saturate in every such ring (`Z[1/2][x]`).

### Sage's default conversion into a parent needs the source in Sage's categories

`SR(x)` for an element of a parent whose category is not one of Sage's own
(the owned `ZZ`) fails with `ValueError: Integer Ring is not in Category of
sets with partial maps`. `Parent._internal_convert_map_from` finds no
registered map and falls back to `_generic_convert_map`. That builds
`DefaultConvertMap_unique(S, self)`, whose homset is
`S.Hom(self, category=self.category()._meet_(S.category()))`. The meet of the
symbolic ring's category and an owned category is Sage's
`SetsWithPartialMaps`, and `Hom` asserts that both endpoints lie in it
(`sage/structure/parent.pyx` 1963, `sage/categories/homset.py` 449). The
coercion model's `bin_op` does not reach the element's `_symbolic_`, so
`1/2 + pi` and `binomial(5, 2)` fail the same way. Observed with Sage 10.9
(`sage-dev-allopts`) on 2026-09-23.

Sage's `ZZ` and `QQ` fail the same way on an owned element: `SageZZ(n)`,
`SageQQ(n)`, `CartanType(["A", n])` raise, and `n in SageZZ` is False, for
the session literal `n`. Sage's `ZZ` alone has a way around the default map:
its `_convert_method_name` is `_integer_`, so it converts any element whose
class has an `_integer_` method (`parent.pyx` 1958, `convert_method_map`).
`QQ._convert_method_name` is `None`. Observed 2026-09-25.

Route chosen: owned numbers never enter `SR`, and owned code lowers a session
value to the engine itself before calling Sage (`_engine_element`), never
relying on Sage to convert it. The preamble owns `pi`, `e` and
the elementary functions over its exact real field (`rings/real.py`), and the
owned rings declare their coercions among themselves (`_coerce_map_from_`).

A related fact: under the `sage` command a script runs in `sage.all`'s own
namespace (`globals() is vars(sage.all)`), so a star import rebinds the
attributes of `sage.all`. Owned code that falls back to a Sage function takes
it from its defining module (`sage.functions.trig`, `sage.misc.functional`),
never through `sage.all`.

### A class-body alias of a `cached_method` discards the original's cache

`h = g` for a `@cached_method g` does not share `g`'s cache. Reached through
`h`, `CachedMethod.__get__` looks for an existing caller only in
`inst._cached_methods`, builds a fresh caller with an empty cache, and stores
it under the function's own name with `setattr(inst, "g", caller)`
(`sage/misc/cachefunc.pyx`, `CachedMethod.__get__`). So `x.h()` replaces the
cache of `x.g()`, and a later `x.g()` recomputes and returns a different
object. Reproducer, Sage 10.9 (`sage-dev-allopts`), 2026-09-24:

```python
class P(Parent):
    @cached_method
    def g(self): return object()
    h = g
p = P(); a = p.g(); p.h(); p.g() is a   # False
```

Observed as `ToricSchemes.weil_divisor_group = torus_invariant_divisor_group`:
a divisor built in `Div_T(X)` stopped belonging to `Div_T(X)` after the alias was
called. Route chosen: an alias of a cached method is a method that calls it.

### `krull_dimension` is missing on generic quotients of multivariate polynomial rings

`R.quotient(I)` for `R = PolynomialRing(QQ, ['x','y'])` is a
`QuotientRing_generic` whose `krull_dimension` is the `CommutativeRings`
category default, which raises `NotImplementedError`
(`sage/categories/commutative_rings.py`). There `I.dimension()` (Singular)
gives the answer. Every other engine measured has its own method:
`Zmod(6)` and `ZZ.quotient(2)` give 0 (`IntegerModRing_generic`),
`ZZ['x'].quotient(x^2+1)` gives 1 (`PolynomialQuotientRing_generic`), and
`QQ['x']`, `ZZ` and `ZZ.localization(2)` give 1. `Zmod(n)` is itself a
`QuotientRing_generic`, over `ZZ`, whose ideals have no `dimension`, so a
dispatch on `QuotientRing_generic` alone sends it to the wrong route.
Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: the
defining-ideal route applies only when the cover ring is an
`MPolynomialRing_base`.

### `is_maximal` raises on multivariate polynomial ideals, and univariate ideals have no `dimension`

Over `S = PolynomialRing(QQ, ['x','y'])`, `S.ideal(x, y).is_maximal()` and
`S.ideal(x).is_maximal()` raise `NotImplementedError`, as does
`ZZ['x'].ideal(2, x).is_maximal()`. `MPolynomialIdeal.dimension()` answers
(`S.ideal(x).dimension() == 1`). Over `QQ['x']` the opposite holds:
`Ideal_1poly_field` has no `dimension`, and `is_maximal()` answers
(`(x^2+1)` gives `True`). Measured on Sage 10.9 (`sage-dev-allopts`),
2026-09-25. Route chosen: multivariate ideals over a field use Zariski's
lemma, prime with quotient of dimension zero; every other ideal asks Sage's
`is_maximal`.
