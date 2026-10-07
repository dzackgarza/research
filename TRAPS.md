# Engine traps

Measured facts about the engines this repository delegates to, kept because each one is the product of the work and costs an afternoon to rediscover (`CONTRIBUTING.md`: *The artifacts are instruments; the product is a map of Sage*; `DEV-63` owns this file).
A row is a finding, never a hypothesis: it records the operation, the spelling measured, the specimen and its size parameter, the wall times, the version, the command that reproduces it, and the route chosen.
A cost is a curve in the size parameter, or it is a single data point and says so.
`COMPLAINTS.md` holds the unresolved need; this file holds the fact, which delivery uses and never resolves.

Read this file before choosing any engine route.
Write to it in the turn the measurement is made.

## Sage

### Lazy Taylor series do not implement `is_field()`

On SageMath 10.10.beta10, the lazy Taylor series parent used for `QQ[[t]]` raises `NotImplementedError` from `is_field()` rather than returning a Boolean.
This is a single capability probe with no size parameter.
Reproduce with the repository's selected full Sage driver:

```bash
/home/dzack/gitclones/sage-dev-allopts/sage -python -c \
  "from sage.all import QQ; from sage.rings.lazy_series_ring import LazyPowerSeriesRing; print(LazyPowerSeriesRing(QQ, 't').is_field())"
```

Route chosen: the private ring-classification boundary treats this as an unrepresented field decision and retains only category facts the engine does establish.
Depends on this: owned formal power-series/adically-complete ring construction.

### Importing `sage.all` costs about a second; one module costs a tenth of that

Per-invocation tooling that needs one Sage module pays for the whole library when it imports `sage.all`, and almost nothing when it imports the module.
Single data points, not a curve: there is no size parameter.

| import | wall time, three runs |
| --- | --- |
| bare interpreter (`python -c pass`) | 0.74 s, 0.44 s, 0.46 s |
| `import sage.all` | 1.59 s, 1.11 s, 1.02 s |
| `from sage.graphs.graph import Graph` | 0.58 s, 0.53 s, 0.72 s |
| `from sage.topology.simplicial_complex import SimplicialComplex` | 0.48 s, 0.53 s, 0.50 s |
| `import sage.all`, then `Graph` | 1.34 s, 1.21 s, 1.22 s |
| `sage -c pass` (the launcher) | 1.02 s, 1.04 s, 0.93 s |

Sage 10.10.beta8, Python 3.14.7, the `.envrc` interpreter `/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python`, 2026-09-16. The first run of a set is slower; the steady value is the last two.
Reproduce with:

```bash
PY=/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python
for i in 1 2 3; do /usr/bin/time -f '%e s' $PY -c 'from sage.graphs.graph import Graph'; done
```

Route chosen: a tool that runs once per invocation imports the module it computes with, never `sage.all`. Spawning one Sage process per item is a design defect at either import.
Depends on this: the `category-graph` recipes (TODO node `category-graph-engine`).

The `sage` on `PATH` is a symlink to `sage-dev-allopts/.venv/bin/sage`, a Python script that accepts `-c` and rejects `-python`; time module imports with the venv's `python` directly.

Importing `sage.topology.simplicial_complex` without `sage.all` prints `UserWarning: Resolving lazy import ... during startup` three times on first use.
The results are unaffected; loading `sage.all` first silences it and costs the second above.

### `Graph.minimum_cycle_basis()` takes integer vertices only, and costs seconds on a few hundred vertices

The default route is `sage.graphs.base.boost_graph.min_cycle_basis`. On string vertices it raises `TypeError: an integer is required` (the edge set is a `pair<int,int>`); relabel first with `relabel(return_map=True)` and map back.
Each returned cycle is a vertex set, not in cyclic order (its own docstring); order it with `subgraph(cycle).cycle_basis()`.

Wall time on the declared category graph, 312 vertices, 397 edges, 88 independent cycles, one 2-connected block of 135 vertices holding 86 of them:

| call | wall time |
| --- | --- |
| `minimum_cycle_basis()` default, whole graph | 30.3 s |
| `minimum_cycle_basis(algorithm='NetworkX')`, whole graph | 8.2 s |
| `minimum_cycle_basis()` default, block by block | 6.6 s |
| `minimum_cycle_basis(algorithm='NetworkX')`, block by block | 1.8 s |
| `cycle_basis()` (spanning tree, not minimum) | milliseconds |
| `blocks_and_cut_vertices()`, `transitive_reduction()`, `level_sets()` | milliseconds |
| `SimplicialComplex(edges).homology(reduced=False)` default `'pari'` / `'dhsw'` | 0.19 s / 0.02 s |

Single graph, one run each, Sage 10.10.beta8, 2026-09-16; the shape of the cost in the vertex count is not measured.
Reproduce with `just category-graph cells` (whole run about 9 s) and the calls above on `_graph(_declared_edges(...))` from `dzack_research.utilities.category_graph`.

Route chosen: the cycle space is the direct sum over 2-connected blocks, so the `cells` view computes the default basis per block and reports the blocks; a large block is the audit finding, not an obstacle.
The per-block cost is paid once per run.

### An axiom applies to every declared supercategory, so a base-restriction edge asserts descent of every property

`CategoryWithAxiom.super_categories` (sage/categories/category_with_axiom.py, `def super_categories`, Sage 10.10.beta8) returns the join of the base category, `category._with_axiom_as_tuple(axiom)` for every supercategory of the base, and `extra_super_categories()`. `_with_axiom_as_tuple` (category.py) applies the axiom to any category whose class hierarchy defines it, and `Modules(ZZ)` defines the same axioms as `Modules(QQ)`. Consequence, read from source on 2026-09-16 and not executed: if `Modules(QQ)` declared `Modules(ZZ)` (restriction of scalars), then `Modules(QQ).FinitelyGenerated()` would have `Modules(ZZ).FinitelyGenerated()` as a supercategory, which is false; the same for every property stated relative to the base (finite type, smooth, projective, free of finite rank).
Absolute properties (commutative, associative, finite) descend truly, but the mechanism cannot tell the two apart.

Route chosen: no owned category declares itself over a lower base.
Restriction of scalars is a functor obtained from the category, and a preservation theorem on that functor states which properties descend.
Depends on this: the `Modules`, `Algebras` and `Schemes` bases (AGENTS.md, *Red flags*).

### A Python subclass of a category class loses its axiom classes

A nested axiom class such as `MagmaticAlgebras.Unital` is bound to its base class by `CategoryWithAxiom.__classget__` (sage/categories/category_with_axiom.py, `def __classget__`, Sage 10.10.beta8): it asserts that `_base_category_class_and_axiom[0]` is the class the attribute is read from. `Category._with_axiom_as_tuple` (category.py) reads the axiom with `getattr(self.__class__, axiom)`, so a category whose class is a Python subclass of the base class raises on every axiom. Reproduction, 2026-10-07, no preamble in the process:

```bash
/home/dzack/gitclones/sage-dev-allopts/.venv/bin/python3 -c "
from sage.all import QQ
from sage.categories.magmatic_algebras import MagmaticAlgebras
class MagmaticAlgebrasSubclass(MagmaticAlgebras):
    pass
print(MagmaticAlgebras(QQ).Unital())
print(MagmaticAlgebrasSubclass(QQ).Unital())
"
```

The first line prints `Category of unital algebras over Rational Field`; the second raises `AssertionError: base category class for <class 'sage.categories.unital_algebras.UnitalAlgebras'> mismatch; expected <class 'sage.categories.magmatic_algebras.MagmaticAlgebras'>, got <class '__main__.MagmaticAlgebrasSubclass'>`.
The preamble meets it at `ModulesOverGroupAlgebra(Modules)` (`modules/group_modules/group_modules.py`): `Modules(ZZ[C2]).Free()` raises the same assertion for `Modules.Free`.

Consequence: a category class whose objects use Sage's axiom classes cannot be refined by a Python subclass.
Route chosen: none yet; the owner rules (`TODO.md`, `modules-over-a-group-algebra-keep-the-module-axioms`).

### An axiom that no class on the path implements returns the category itself

`Category._with_axiom_as_tuple` (sage/categories/category.py, Sage 10.10.beta8) returns `(self,)` when `getattr(self.__class__, axiom)` is `None`. When the attribute exists but the base class does not hold it in its own `__dict__`, it returns `self` joined with the same axiom applied to each supercategory. A `SubcategoryMethods.Commutative` that calls `self._with_axiom("Commutative")` satisfies the first test, because the dynamic class inherits that method. So if no category on the path declares a nested `Commutative(CategoryWithAxiom)`, `C.Commutative()` is `C`, and nothing warns.

Observed 2026-10-07 in a preamble session: `Magmas().Commutative() is Magmas()` was `True`. `Magmas.ParentMethods.is_commutative` answers `True` on membership in `Magmas().Commutative()`, so every owned magma that does not override `is_commutative` answered `True`. This was observed on `T(QQ^2)`. For `End(QQ^2)` and `S_3` it follows from the same membership test and was not run. `_algebra_from_native_ring` then placed the tensor algebra in the commutative algebras on that answer.

Consequence: a category that introduces a law must declare the nested axiom class for every axiom its `SubcategoryMethods` names.
Route chosen: `Magmas.Commutative(CategoryWithAxiom)` and `AdditiveMagmas.AdditiveCommutative(CategoryWithAxiom)` in `categories/group/magmas.py`. Sage joins each into every category with its axiom whose path reaches the base. A 2026-10-07 probe over the 204 owned categories that construct with no parameter or with `ZZ`, `QQ` or `Groups.C(2)` found no other accessor that returns its own category for an axiom outside `axioms()`, except the group shorthands `FinitelyGenerated` and `FinitelyPresented`, which name `FinitelyGeneratedAsMagma` and `FinitelyPresentedAsGroup`.

### Conjugacy in a free group: `FreeGroup` elements have `is_conjugate`, `IndexedFreeGroup` elements do not

An element of a finite-rank `FreeGroup` inherits `ElementLibGAP.is_conjugate` (`sage/groups/libgap_wrapper.pyx`, line 747), which is GAP's `IsConjugate`. On a free group GAP dispatches it to the FGA package method "RepresentativeActionOp for conjugation of elements in a free group" (`/usr/share/gap/pkg/fga/lib/ReprAct.gi`, line 14, FGA 1.5.0), which compares cyclically reduced words. An `IndexedFreeGroup` element has no `is_conjugate` and no GAP model.

Measured on SageMath 10.10.beta8, 2026-10-07, Sage alone, in `FreeGroup(2)`: `w = (a b a^-1 b^2)^(n/5)` against `v = g w g^-1` with `g = (b a^2)^(n/3)` (conjugate), and against `w a` (not conjugate).

| length of `w` | length of `v` | `w.is_conjugate(v)` | `w.is_conjugate(w*a)` |
| --- | --- | --- | --- |
| 10 | 28 | 0.79 ms (first call) | 0.06 ms |
| 100 | 298 | 0.03 ms | 0.02 ms |
| 1000 | 2998 | 0.10 ms | 0.02 ms |
| 10000 | 29998 | 0.91 ms | 0.05 ms |

The cost grows about linearly in the word length.
Reproduce: in Sage, `F = FreeGroup(2); a, b = F.gens(); w = (a*b*a^-1*b^2)^200; g = (b*a^2)^333; timeit('w.is_conjugate(g*w*~g)')`.

Route chosen: `_free_group_conjugacy` in `categories/group/groups.py` reads both reduced words, renames the finitely many letters they use to the generators of a finite-rank `FreeGroup`, and asks `is_conjugate` there. The retraction of `F(S)` onto the free group on those letters makes the answer the same in `F(S)`, so the route serves `IndexedFreeGroup` and an infinite basis.
Depends on this: `GroupsWithChosenFreeBasis._conjugacy_decision`, hence `conjugation_g_set().in_same_orbit` and conjugacy classes of free groups.

### `DiGraph.longest_path()` is a MILP by default; a DAG's longest chain is `level_sets()`

`longest_path(algorithm='MILP')` is the default and `'heuristic'` the only alternative (its docstring).
For an acyclic digraph, `level_sets()` puts a vertex in level `k` exactly when its longest path from a source has `k` edges, in `O(n + m)` (its docstring and body).
The longest chain is `len(level_sets()) - 1`, and the longest chain *from* each vertex to a sink is its level in `reverse().level_sets()`. Verified on a seven-vertex DAG with a shortcut edge; used by the `shape` view.

### `==` between symbolic variables is a proof attempt, and costs a coercion search

`SR.var("e_0") == SR.var("e_1")` is a symbolic equation, not a boolean.
Asking its truth (`bool`, `any`, `in` over a list of symbols) makes Sage try to prove it, and one route evaluates the difference at random points of `ComplexIntervalField` (`complex_interval_field.py`, `random_element`). A membership test that scanned a list of symbolic labels with `==` made each Gram entry of a lattice cost milliseconds and the star import take 460 s on 2026-09-23 (rank 4: 0.44 s, rank 8: 3.3 s per lattice, cubic).

Route chosen: decide membership of hashable points by hashing (`sage.sets.set.Set`, a `frozenset`), never by comparing a candidate with every point.
Symbols hash consistently with identity of name.

Measured again on SageMath 10.10.beta8, 2026-10-07, Sage alone, over all `n^2` ordered pairs of `n` distinct `SR.var`s (host load average about 7; the `n = 2` row includes first-call warm-up):

| n | `bool(a == b)` per pair | `a.is_trivially_equal(b)` per pair | `a is b` per pair |
| --- | --- | --- | --- |
| 2 | 21.6 ms | 7.3 µs | 1.7 µs |
| 4 | 1.41 ms | 3.3 µs | 0.44 µs |
| 8 | 1.76 ms | 1.6 µs | 0.16 µs |
| 16 | 1.29 ms | 1.5 µs | 0.14 µs |

The cost per pair does not fall with `n`, so a scan that identifies `k` points pairwise costs on the order of `k^2` ms.
The scan still stands in `FiniteOrderedSets._on_points` (`point is present or point == present`), which every `support()` of a framed-free element reaches through `finite_subsets()`.
On a catalogue lattice, whose basis labels are `SR` symbols, one `L.b(x, y)` with full-support `x`, `y` on `E_8` cost 0.24 s; deleting a second identical scan in `Subsets._from_finite_members` took it to 0.07 s.
Reproduce: `/home/dzack/gitclones/sage-dev-allopts/sage -python -c "from sage.all import SR; import timeit; a, b = SR.var('e_0'), SR.var('e_1'); print(timeit.timeit(lambda: bool(a == b), number=100) / 100)"`.

### pytest-timeout's `SIGALRM` inside Cython code stops the whole run

With `--timeout-method=signal`, the alarm that pytest-timeout raises can land inside a Sage `sig_on()` block.
cysignals then raises `cysignals.signals.AlarmInterrupt`, which pytest treats as an interrupt: the run stops with "!!! cysignals.signals.AlarmInterrupt !!!" and the remaining tests never execute.
Observed on the 2026-09-23 triage run with `--timeout=1`, at 84% of 16,311 tests.
With the default per-test timeout (`func_only` false) the alarm can also fire while pytest builds a failure report, and pytest aborts with `INTERNALERROR ... Failed: Timeout`; `-o timeout_func_only=true` confines the alarm to the test function.

Route chosen: a triage catalogue run resumes after the interrupted file; the gated default run treats any test at its time limit as a failed run anyway.

### `Localization.is_unit` answers True for any nonzero element of a number-field order

`Localization(O, S).is_unit` returns `_cut_off_extra_units_from_base_ring_element(numerator).is_unit()`, whose first test is `x.numerator().is_unit()` (`sage/rings/localization.py` 448, 872). For an element of a number-field order, `numerator()` is an element of the field, where every nonzero element is a unit, so the localization reports every nonzero numerator a unit.
Specimen, Sage alone (no preamble): `QuadraticField(-1, "a").maximal_order().localization((2,))(3).is_unit()` is `True`, although 3 is prime in `Z[i]` and `S = {2^k}`; `ZZ.localization((2,))(3)` answers `False` correctly.
Sage 10.10.beta8, 2026-09-25.

Route chosen: a localization of a number-field order decides units from the definition in the source ring -- `a/s` is a unit exactly when saturating `(a)` by the inverted elements gives the unit ideal (`LocalizationRings.ElementMethods.is_unit`). Other sources keep the engine's decision, which is exact when numerators lie in the source ring; the owned ideal machinery cannot yet saturate in every such ring (`Z[1/2][x]`).

### Sage's default conversion into a parent needs the source in Sage's categories

`SR(x)` for an element of a parent whose category is not one of Sage's own (the owned `ZZ`) fails with `ValueError: Integer Ring is not in Category of sets with partial maps`. `Parent._internal_convert_map_from` finds no registered map and falls back to `_generic_convert_map`. That builds `DefaultConvertMap_unique(S, self)`, whose homset is `S.Hom(self, category=self.category()._meet_(S.category()))`. The meet of the symbolic ring's category and an owned category is Sage's `SetsWithPartialMaps`, and `Hom` asserts that both endpoints lie in it (`sage/structure/parent.pyx` 1963, `sage/categories/homset.py` 449). The coercion model's `bin_op` does not reach the element's `_symbolic_`, so `1/2 + pi` and `binomial(5, 2)` fail the same way.
Observed with Sage 10.9 (`sage-dev-allopts`) on 2026-09-23.

Sage's `ZZ` and `QQ` fail the same way on an owned element: `SageZZ(n)`, `SageQQ(n)`, `CartanType(["A", n])` raise, and `n in SageZZ` is False, for the session literal `n`. Sage's `ZZ` alone has a way around the default map: its `_convert_method_name` is `_integer_`, so it converts any element whose class has an `_integer_` method (`parent.pyx` 1958, `convert_method_map`). `QQ._convert_method_name` is `None`. Observed 2026-09-25.

Route chosen: owned numbers never enter `SR`, and owned code lowers a session value to the engine itself before calling Sage (`_engine_element`), never relying on Sage to convert it.
The preamble owns `pi`, `e` and the elementary functions over its exact real field (`rings/real.py`), and the owned rings declare their coercions among themselves (`_coerce_map_from_`).

A related fact: under the `sage` command a script runs in `sage.all`'s own namespace (`globals() is vars(sage.all)`), so a star import rebinds the attributes of `sage.all`. Owned code that falls back to a Sage function takes it from its defining module (`sage.functions.trig`, `sage.misc.functional`), never through `sage.all`.

### A class-body alias of a `cached_method` discards the original's cache

`h = g` for a `@cached_method g` does not share `g`'s cache.
Reached through `h`, `CachedMethod.__get__` looks for an existing caller only in `inst._cached_methods`, builds a fresh caller with an empty cache, and stores it under the function's own name with `setattr(inst, "g", caller)` (`sage/misc/cachefunc.pyx`, `CachedMethod.__get__`). So `x.h()` replaces the cache of `x.g()`, and a later `x.g()` recomputes and returns a different object.
Reproducer, Sage 10.9 (`sage-dev-allopts`), 2026-09-24:

```python
class P(Parent):
    @cached_method
    def g(self): return object()
    h = g
p = P(); a = p.g(); p.h(); p.g() is a   # False
```

Observed as `ToricSchemes.weil_divisor_group = torus_invariant_divisor_group`: a divisor built in `Div_T(X)` stopped belonging to `Div_T(X)` after the alias was called.
Route chosen: an alias of a cached method is a method that calls it.

### `krull_dimension` is missing on generic quotients of multivariate polynomial rings

`R.quotient(I)` for `R = PolynomialRing(QQ, ['x','y'])` is a `QuotientRing_generic` whose `krull_dimension` is the `CommutativeRings` category default, which raises `NotImplementedError` (`sage/categories/commutative_rings.py`). There `I.dimension()` (Singular) gives the answer.
Every other engine measured has its own method: `Zmod(6)` and `ZZ.quotient(2)` give 0 (`IntegerModRing_generic`), `ZZ['x'].quotient(x^2+1)` gives 1 (`PolynomialQuotientRing_generic`), and `QQ['x']`, `ZZ` and `ZZ.localization(2)` give 1. `Zmod(n)` is itself a `QuotientRing_generic`, over `ZZ`, whose ideals have no `dimension`, so a dispatch on `QuotientRing_generic` alone sends it to the wrong route.
Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: the defining-ideal route applies only when the cover ring is an `MPolynomialRing_base`.

### `is_maximal` raises on multivariate polynomial ideals, and univariate ideals have no `dimension`

Over `S = PolynomialRing(QQ, ['x','y'])`, `S.ideal(x, y).is_maximal()` and `S.ideal(x).is_maximal()` raise `NotImplementedError`, as does `ZZ['x'].ideal(2, x).is_maximal()`. `MPolynomialIdeal.dimension()` answers (`S.ideal(x).dimension() == 1`). Over `QQ['x']` the opposite holds: `Ideal_1poly_field` has no `dimension`, and `is_maximal()` answers (`(x^2+1)` gives `True`). Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: multivariate ideals over a field use Zariski's lemma, prime with quotient of dimension zero; every other ideal asks Sage's `is_maximal`.

### Sage's localizations of polynomial rings decide units on only one shape

`L(e).is_unit()` measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25, for `e` in `x, 2, 3, x+1, 2x`:

| engine | nonconstant `e` | constants |
| --- | --- | --- |
| `ZZ['x'].localization((2, x))` | `TypeError: cannot convert nonconstant polynomial` | correct |
| `ZZ['x'].localization(2).localization(x)` | same `TypeError` | correct |
| `PolynomialRing(ZZ, 'x,y').localization((2, x))`, nested or flat | same `TypeError` | correct |
| `ZZ.localization(2)['x'].localization(x)` | correct (`x`, `2x` units; `x+1` not) | correct |
| `PolynomialRing(ZZ.localization(2), 'x,y').localization(x)` | `NotImplementedError` | `NotImplementedError` |

So a localization that inverts a constant in a polynomial ring over `ZZ` cannot decide units of nonconstant elements, and only the univariate ring over Sage's own `ZZ.localization(2)` answers.
Route chosen: a univariate polynomial algebra over a localized base keeps that engine; flattening is used only in several variables, where no engine answers and the gap is still open.

### `x in RealBallField(p)` is not "the field can enclose x"

`pi^2 in RealBallField(64)` and `sqrt(2) in RealBallField(64)` are both `False`, while `RealBallField(64)(pi^2)` returns `[9.8696... +/- 3.20e-18]`. Conversion succeeds for every closed real symbolic expression measured (`pi^2`, `sqrt(2)`, `e + log(3)`, `sin(1)`, `3/7`) and raises `TypeError` for `x + 1`, `I` and `I*pi`. `expression.variables() == ()` together with `expression.is_real()` separates the two.
`pi^2 in AA` is `False` and `sqrt(2) in AA` is `True`, so `AA` membership does test algebraicity.
Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: the ball-sign certificate is attempted on closed real expressions.

### `FreeAlgebra.__contains__` rejects constants

`ZZ(2) in FreeAlgebra(QQ, 2, 'x,y')` and `QQ(2) in FreeAlgebra(QQ, 2, 'x,y')` are `False`, and so is `ZZ(2) in FreeAlgebra(ZZ, 2, 'x,y')`, although the coercion exists and `F(2)` is twice the unit.
`ZZ(2) in QQ['x,y']` is `True`. Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: an owned ring decides membership of another owned ring's element by the canonical map first, then by the engine's `in`.

### Over `ZZ`, Sage's multivariate ideals decide neither primality nor maximality, and have no `syzygy_module`

For `R = PolynomialRing(ZZ, ['x','y'])`, `R.ideal(...).is_prime()` and `is_maximal()` raise `NotImplementedError`, and `syzygy_module()` raises `ValueError: Coefficient ring must be a field`. Singular answers all three over `ZZ`: `minAssZ` from `primdecint.lib` gives the minimal primes (`(6, x, y)` gives `(2, x, y)` and `(3, x, y)`; `(2, x^2+1, y)` gives `(2, x+1, y)`), `syz` gives the syzygies (`(2, x, y)` gives `(y, 0, -2)`, `(x, -2, 0)`, `(0, -y, x)`), and a Groebner basis over `ZZ` exposes `I cap ZZ` as its constant.
Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: primality by `minAssZ`, maximality by `I cap ZZ = (p)` and Zariski's lemma in `F_p[x_1, ..., x_n]`, syzygies by Singular `syz`.

### Over `AA`, multivariate ideals have no primality test

`PolynomialRing(AA, ['x','y']).ideal(x, y).is_prime()` raises `TypeError: cannot call Singular function 'primdecSY'`: Singular has no algebraic-real coefficients, and Sage has no other primary decomposition over `AA`. Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: whether such a quotient is a field is left undecided (`Unknown`), so it is not placed in fields.
Over `Zmod(n)` the question reduces to `ZZ`, because `(Z/n)[x]/I = Z[x]/(n, I)`.

### `Qp(p).quotient(I)` invents an invalid generator name

`Qp(3, 20).quotient(Qp(3, 20).ideal(3))` raises `ValueError: variable name '3bar' does not start with a letter`: Sage names the quotient's generator after the field's generator, which is `3`. With `names=('u',)` it returns the zero ring.
Measured on Sage 10.9 (`sage-dev-allopts`), 2026-09-25. Route chosen: a field engine's quotient is built with an explicit private name.

### `IntegralLattice(G).orthogonal_group().order()` recomputes in GAP the order that PARI already returned

For a definite lattice, `IntegralLattice.orthogonal_group()` takes its generators from PARI's `qfauto` (through `QuadraticForm.automorphism_group()`), which returns `|O(L)|` with them, and discards the order.
`.order()` then asks GAP for `Size` of the matrix group, which GAP computes from the generators by an orbit algorithm.
`QuadraticForm(ZZ, 2*G).number_of_automorphisms()` reads the PARI order.
Best of three runs, except the GAP order and the group construction (one run each, since both are cached), SageMath 10.10.beta8, 2026-10-07, `G = CartanMatrix(['E', n]).change_ring(ZZ)`:

| n | `pari(G).qfauto()` | `number_of_automorphisms()` | `orthogonal_group()` | `.gens()` | `.order()` from GAP | `.order()` after `gap().SetSize(...)` | order of O(L) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 1.26 ms | 1.44 ms | 489 ms (first call, includes warm-up) | 24.8 ms | 771 ms | 0.008 ms | 103680 |
| 7 | 1.06 ms | 2.03 ms | 47.6 ms | 24.5 ms | 1760 ms | 0.008 ms | 2903040 |
| 8 | 2.58 ms | 3.55 ms | 34.9 ms | 20.3 ms | 8366 ms | 0.008 ms | 696729600 |

Reproduce with `~/.local/bin/sage probe.sage`, where the probe times the calls above for `n = 6, 7, 8`.
Route chosen: the private engine of `O(L)` (`LatticeIsometryMor._engine_group`, `src/dzack_research/preamble/categories/lattice_morphisms.py`) records the PARI order on the GAP model with `SetSize`, so the group's cardinality is the engine's order and never a GAP orbit computation.
Depends on this: `O(L).cardinality()` for every definite lattice.

### `TorsionQuadraticModule.orthogonal_group()` enumerates isometries by brute force in `_isom_fqf`

With no generators given, `TorsionQuadraticModule.orthogonal_group()` calls `sage.groups.fqf_orthogonal._isom_fqf`, which its own docstring calls "a slow brute force approach", and caches the generators on the module as `_orthogonal_group_gens`.
At `n = 6` almost all of the time is in `_isom_fqf`: 394 calls of `fgp_module.submodule` take 2.49 s cumulative, `free_quadratic_module.span` and `FreeModule.__init__` about 2.3 s, `TorsionQuadraticModule._mul_` 1.40 s, and `matrix_space._element_constructor_` 1.02 s of own time.
`.order()` after construction costs 0.001 s.
The first GAP call in a process costs about 0.6 s; the times below exclude it, because the probe calls `libgap.eval("1")` first.
First call, minimum of three fresh processes, SageMath 10.10.beta8, 2026-10-07, specimen `IntegralLattice(2*identity_matrix(n)).discriminant_group()`, the discriminant form of `A1^n`:

| n | `orthogonal_group().order()` | order |
| --- | --- | --- |
| 2 | 0.113 s | 2 |
| 3 | 0.197 s | 6 |
| 4 | 0.356 s | 24 |
| 6 | 4.90 s | 1440 |

Reproduce with `sage -python probe.py n`, where the probe warms GAP, builds the specimen and times `orthogonal_group().order()`.
Route chosen: the private engine of the orthogonal group of a torsion form (`_engine_group` in `src/dzack_research/preamble/categories/modules/framed/formed/torsion_form_modules.py`) calls this method on the engine module of the invariant-factor form, so its first `cardinality()` is bounded below by this curve.
Sage ships no other route to the full orthogonal group of a torsion quadratic form; whether Hecke/Oscar's `orthogonal_group(::TorQuadModule)` is faster is untested.
Depends on this: `D.orthogonal_group()` for every discriminant form `D`, and through it `rho_L` and the stable orthogonal group.

### PARI's definite isometry test costs the number of vectors up to the largest diagonal entry, and Sage has no other route

Sage's `QuadraticForm.is_globally_equivalent_to` calls PARI `qfisom`, so PARI is the only definite isometry test Sage ships.
`qfisominit(G)` and `qfauto(G)` enumerate every vector of norm at most the largest diagonal entry of `G`, so their cost follows that vector count, not the rank.
`qfisom(init, G')` against a stored `qfisominit` costs about a tenth of the init, and `qfauto(init)` on the same structure reuses its enumeration.
`D_n^+` with an LLL-reduced Gram matrix needs a vector of norm `n/4` among its basis vectors, which is what makes `D_20^+` expensive; its `qfisominit` needs more than 1 GiB of PARI stack, so with Sage's default stack it raises a stack overflow.
`qfrep(G, 4, 0)`, the numbers of vectors of norm 1 to 4, costs under 1 ms on every specimen.
The mass of a definite genus is a closed formula and costs a few ms.
SageMath 10.10.beta8, PARI stack set to 8 GiB by `pari.allocatemem(2^33, 2^34)`, 2026-10-07, one run each; `D_n^+` is `span(ZZ, rows)` of `D_n` and the glue vector `(1/2, ..., 1/2)`, reduced by `LLL_gram`:

| lattice | vector pairs up to the largest diagonal entry | `Genus(G)` | `.mass()` | `qfauto(G)` | `qfisominit(G)` | `qfauto(init)` | `qfisom(init, G)` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `E7` | not measured | 63.8 ms | 8.2 ms | 6.6 ms | 3.1 ms | 0.7 ms | 0.9 ms |
| `E8` | not measured | 26.8 ms | 8.6 ms | 10.5 ms | 5.8 ms | 2.0 ms | 1.1 ms |
| `D12^+` | 1,156 | 23.5 ms | 3.6 ms | 42.3 ms | 24.8 ms | 15.1 ms | 4.8 ms |
| `D16^+` | 31,200 | 25.3 ms | 6.3 ms | 2838.8 ms | 2374.6 ms | 565.9 ms | 262.8 ms |
| `D20^+` | 301,304 | 32.2 ms | 6.1 ms | 78055.9 ms | 73099.5 ms | not measured | 6768.1 ms |

The `qfauto(init)` column comes from a second run, in which `qfisominit` took 2.8, 2.6, 26.3 and 2899.6 ms; the `D20^+` row ran beside another Sage process, and alone `qfisominit` took 31.07 s and `qfisom` 3.30 s.

Sage's `GenusSymbol_global_ring.__eq__` compares the local symbols and never the signature, and the class defines no `__hash__`, so genera cannot key a dictionary.
Sage decides neither which spinor genus of a genus a lattice lies in nor isometry of indefinite lattices of rank at least 3 when the genus has more than one spinor genus; `Genus.spinor_generators(proper=False)` only says whether it has more than one.
Sage's `Genus` exposes the group of spinor operators and the improper spinor kernel only through the private `_improper_spinor_kernel()` (`sage/quadratic_forms/genera/genus.py`, line 2586 in `sage-dev-allopts`); `spinor_generators(proper)` returns primes whose operators generate the quotient and cannot decide whether a given prime's operator lies in the kernel. `_genus_classes` in `lattices.py` calls the private method to choose a neighbour prime whose operator lies in the kernel, so that `QuadraticForm.neighbor_iteration` stays in one spinor genus.
Hecke's `is_isometric(::ZZLat, ::ZZLat)` decides every case, the indefinite one by `p`-adic approximation and the spinor operators.

Reproduce with `~/.local/bin/sage probe.sage`, where the probe builds the specimens above and times each call.
Route chosen: `_isometry_class_representatives` in `src/dzack_research/preamble/categories/lattices.py` computes each lattice's rank, determinant, signature and `qfrep(G, 4, 0)` once and groups by them, then groups by the owned genus `L.genus()`, whose equality compares the signature, the determinant and the canonical local symbols, and decides only inside a genus with more than one member.
A definite genus of three or more members with `mass · |O(L)| = 1` is one class and needs no comparison; otherwise `qfisominit` runs once per class representative and `qfisom` tests each member against them.
An indefinite genus of rank at least 3 with one spinor genus is one class; otherwise each member goes to Hecke `is_isometric` through `_OscarLatticeAdapter.integer_lattices_are_isometric` in `lattice_engines.py`.
The PARI stack is left at Sage's default, so a lattice like `D_20^+` that reaches a comparison raises PARI's stack error rather than growing a process-wide setting.
The wall time of the whole partition as a function of the number of lattices is untested.
Depends on this: `Lattices(ZZ).isometry_classes`, and through it lattice-db duplicate detection.

### `IntegralLattice.short_vectors` enumerates a rank-8 shell of 66,805 vectors in about a second; a preamble element per vector costs about 2 ms

`IntegralLattice(G).short_vectors(n)` returns every vector of norm below `n`, grouped by norm, through fplll.
On `K8` (lattice-db record `0096`: rank 8, minimum 4, discriminant group `(Z/2)^2 + (Z/12)^2`), SageMath 10.10.beta8, 2026-10-08, one run each:

| bound `n` | vectors of norm below `n` | `short_vectors(n)` |
| --- | --- | --- |
| 9 | 1,153 | 0.09 s |
| 13 | 5,101 | 0.16 s |
| 25 | 66,805 | 1.34 s |

The preamble's cost is above the engine.  Raising one engine vector into the lattice by `_element_from_coordinates` costs about 1.8 ms (132, 828 and 2,796 vectors in 0.27, 1.24 and 5.04 s).  The element predicate `is_root()` costs about 32 ms, most of it in the pairings `b(v, e_i)` against each generator, each a separate form evaluation.
`reflective_roots` asks every vector of norm dividing `2 exp(A_L)`, up to norm 24 on `K8`, so testing each element took about 35 min.
Sage ships no reflective-root routine: `free_quadratic_module_integer_symmetric.py` has no root method.

Reproduce with `.tmp/`-local probes that build `Lattices(ZZ)(G)` from the card and time `short_vectors`, `vectors_of_square` and `is_root`.
Route chosen: `_roots_of_square` in `src/dzack_research/preamble/categories/definite_lattices.py` takes the shell from `short_vectors`, pairs it against the basis in one product with the symmetric Gram matrix, keeps the rows where `b(v,v)` divides `2 b(v,w)`, and raises only the roots.  `reflective_roots` on `K8` then takes 5.3 s, and its derive 11.9 s.
Depends on this: `reflective_roots`, `reflective_root_system_components`, and through them the lattice-db `root_system` of a definite card.

### The rational spinor norm costs nothing per isometry; reaching it through OSCAR costs about 25 s once per process

Sage has no spinor norm of an isometry of a rational quadratic space: `sage/quadratic_forms/genera/spinor_genus.py` and `genus.py` hold only spinor operators and the spinor kernel of a genus, and `sage/groups/matrix_gps/` has nothing.
PARI has no spinor norm function.
GAP's `SpinorNorm` (`grp/classic.gi`) covers only finite fields of odd characteristic, but the `WallForm(form, m)` it calls works over any field, `QQ` included.
The Wall form of `g` on `W = im(1 - g)` has discriminant the Zassenhaus spinor norm (Taylor, *The Geometry of the Classical Groups*, p. 163); with `form = 2G`, `DeterminantMat(WallForm(2G, g).form)` is in the square class of OSCAR's `rational_spinor_norm(...; b = 1)`, which is `b(v_1, v_1) ... b(v_m, v_m)` for `g = s_{v_1} ... s_{v_m}`.
For `g = 1`, `WallForm` returns an empty form whose `DeterminantMat` raises; the spinor norm is 1, as GAP's own `SpinorNorm` returns.
GAP and the preamble's isometry matrices both act on rows.

Per-isometry cost, in ms per isometry, isometries of the Gram matrix by row action (`g G g^T = G`), SageMath 10.10.beta8 with GAP 4.16dev, Julia 1.10.11 with Oscar 1.7.1 through `sage-julia-bridge` 6625927, 2026-10-07, second of two runs:

| specimen | rank | isometries | Sage, Wall form by hand | libgap `WallForm` | OSCAR through the bridge |
| --- | --- | --- | --- | --- | --- |
| `A1+A1` | 2 | 8 | 1.44 | 0.70 | 1.12 |
| `U+A1` | 3 | 8 | 0.37 | 0.71 | 0.81 |
| `A1+A1+A1` | 3 | 48 | 0.12 | 1.61 | 0.62 |
| `E8` (reflection words) | 8 | 48 | 0.51 | 1.92 | 1.70 |
| `U+U+E8` | 12 | 48 | 0.17 | 1.65 | 6.48 |

The three routes agree on the square class of all 160 isometries.
The first libgap `WallForm` call took 595 ms and 246 ms in two runs; starting Julia and defining the adapter module took 36.55 s and 29.37 s.
Engine alone, OSCAR: Julia process start 1.76 s, `using Oscar` 21.50 s, the adapter module 1.64 s, the first call 1.43 s.
Through the preamble, `L.spinor_kernel().cardinality()` for `L = NamedLattices.A1 + NamedLattices.A1` took 29.36 s after a 2.47 s session import; `|spinor kernel| = 4`; the first of eight spinor-norm calls took 27.08 s, of which the bridge's `eval` loading Oscar took 23.16 s, and the other seven took 0.80 s together; `O(L)` through GAP took 0.57 s.

Reproduce with `direnv exec /home/dzack/research /home/dzack/gitclones/sage-dev-allopts/sage -python probe.py src/dzack_research/preamble/categories/lattice_engines.py --oscar`, where the probe enumerates the isometries of the specimens above and times the three routes on each.
Route chosen: `_gap_rational_spinor_norm_class` in `src/dzack_research/preamble/categories/lattice_engines.py` computes the rational spinor norm by libgap `WallForm`; the number-field spinor norm stays on OSCAR, since GAP has no general number fields.
On that route, one run each, `L.spinor_kernel().cardinality()` took 1.87 s for `A1+A1` (`|spinor kernel| = 4`, the eight spinor-norm calls 0.10 s together) and 1.74 s for `A1+A1+A1` (`|spinor kernel| = 24`, the 48 calls 0.85 s together), with no Julia process started.
Depends on this: `spinor_norm`, `spinor_norm_class`, `spinor_kernel` and `spinorial_kernel` of a lattice over `ZZ` or `QQ`.

## mypy

### A star import that rebinds a name is rejected, and the first binding wins

A Sage session file that loads the preamble rebinds Sage names on purpose: the lowered file starts with `from sage.all_cmdline import *`, and `from dzack_research.preamble.all import *` then rebinds `Integer` and `RealNumber` to the preamble's own constructors.
Python binds the later import.
mypy 2.4.0 reports `Incompatible import of "Integer"` at the second import, and `reveal_type(Integer)` after it is still the first module's class, so every later use is checked against the wrong type.
Neither `--allow-redefinition` nor `--allow-redefinition-new --local-partial-types` changes either result.
This is upstream python/mypy#16972, open on 2026-10-02; Pyright takes the later binding.
Three-file specimen:

```bash
printf 'class Integer: ...\n' > a.py
printf 'def Integer(value: int = 0) -> int:\n    return value\n' > b.py
printf 'from a import *\nfrom b import *\nreveal_type(Integer)\n' > c.py
uvx mypy@2.4.0 --no-incremental c.py
```

Route chosen: none in this repository.
The rebinding is the design of the session, and a suppression would hide the wrong inferred type as well as the error.
The two errors stay on the lowered `sage-init.sage` until mypy models the later binding.

### mypy cannot see `sageparse` through a default editable install

`tree-sitter-sage` maps two package roots in `setup.py`: `bindings/python` for `tree_sitter_sage` and `src/sageparse` for `sageparse`. The default editable install of setuptools puts an import-hook finder in site-packages; Python imports `sageparse` through it, but mypy reads only the paths of `.pth` files and reports `Cannot find implementation or library stub for module named "sageparse"`. `editable_mode=compat` writes one `.pth` line, the first root `bindings/python`, so `sageparse` is not importable at all after it.
Checked with setuptools in the Sage venv on 2026-10-02 by `sage -pip show -f tree-sitter-sage` and the `.pth` contents.

Route chosen: `editable_mode=strict`, which builds a tree of symbolic links under `build/__editable__.*` and puts that tree on a `.pth` line.
Edits to existing files are live; a new module needs the install again.

```bash
direnv exec ~/research "$SAGE_BIN" -pip install --no-deps \
  --config-settings editable_mode=strict -e ~/gitclones/tree-sitter-sage
```
