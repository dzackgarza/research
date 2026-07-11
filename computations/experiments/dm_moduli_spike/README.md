# Deligne-Mumford compactification spike

A stack-aware **combinatorial** model of the moduli space of stable curves
`Mbar(g, n)`. It models the dual-graph stratification exactly -- strata,
dimensions, automorphisms (including loop branch swaps), clutching
presentations, and closure incidence -- while making no claim to implement the
algebraic stack as a functor of points.

"Weighted stable curve" here means a **stable dual graph whose vertex weights
are component genera**. The public graph type is named `StableCurveType` to
avoid confusion with Hassett-weighted marked curves.

## Public object model

| Type | Role |
|------|------|
| `DMCompactificationModel(g, n)` | typed ambient `Mbar(g, n)` |
| `StableCurveTypes(g, n)` | Sage `Parent` of all stable graph types (a `FiniteEnumeratedSet`, `UniqueRepresentation`) |
| `StableCurveType` | immutable `Element`: an isomorphism class of stable dual graphs (an *index* for a stratum) |
| `StableGraphContraction` | a contraction morphism between curve types |
| `DMStratum` | the geometric stratum indexed by a graph (distinct from the graph) |
| `DMStratification` | the finite / rank-truncated stratification |
| `StratificationPoset` | a typed poset carrying its order convention |
| `StableGraphRecord` | the immutable half-edge source of truth |
| `QuotientStackPresentation`, `ClutchingMorphism`, `ModuliFactor` | symbolic stack-geometric presentations |

## Quick start

```python
sage: from dm_moduli_spike import DMCompactificationModel
sage: M = DMCompactificationModel(2, 1)
sage: M.dimension()
4
sage: S = M.stratification()          # backend="pure-sage" by default
sage: S.rank_sizes()                  # strata by codimension
(1, 2, 5, 5, 3)
sage: S.cardinality()
16
sage: P = S.specialization_poset()    # generic below special; rank = num_edges
sage: Q = S.closure_poset()           # special below generic (P.dual())
```

Direct construction of a boundary type and its stratum:

```python
sage: M04 = DMCompactificationModel(0, 4)
sage: T04 = M04.curve_types()
sage: gamma = T04.from_vertices(genera=(0, 0), markings=((1, 2), (3, 4)), edges=((0, 1),))
sage: gamma.codimension(), gamma.stratum_dimension()
(1, 0)
sage: M04.stratum(gamma).open_stack_presentation()
QuotientStackPresentation(product=(M(0, 3) x M(0, 3)), group=Aut order 1)
```

## Design invariants (non-negotiable)

1. The semantic representation is **half-edge** based (loops expose two branches).
2. The public graph type is **independent of `admcycles`**.
3. A stratum and its indexing graph are **separate objects**.
4. Contractions are retained as **typed morphisms**.
5. The poset **order convention is explicit** (no bare `poset()`).
6. Truncated enumeration is marked **incomplete** (`is_complete()`).
7. Automorphisms act on **branches and flags**, not merely vertices.
8. The spike uses Sage and `admcycles`; external CAS processes are extension
   points, not dependencies.

## Backends

* `backend="pure-sage"` (default): rank-by-rank enumeration by one-edge
  degeneration, an independent reference implementation.
* `backend="admcycles-stable"`: enumeration via the established `admcycles`
  `StableGraph` interface (converted to owned `StableCurveType`s); the
  correctness-oriented cross-check.
* `backend="admcycles-decorated"`: optional faster enumerator over the
  experimental `admcycles.decorated_graph` module, kept behind an adapter with a
  pinned-compatibility check (absent in current `admcycles` releases).

Covers are always recomputed by contraction, independently of the enumeration
backend, and every mathematical invariant is checked in `tests/`.

## Verification

Tests are `.sage` files under `tests/`, run through the global Sage QC:

```
just -f computations/experiments/dm_moduli_spike/justfile test
```

The acceptance fixtures pin the exact rank vectors for `(0,3)`, `(0,4)`,
`(1,1)`, `(0,5)`, `(1,2)`, `(2,0)`, `(2,1)` and cross-check the pure-Sage and
`admcycles` backends on all of them.
